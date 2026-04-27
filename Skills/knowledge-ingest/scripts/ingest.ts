#!/usr/bin/env bun
/**
 * Knowledge Ingest 核心脚本
 *
 * 用法:
 *   bun ingest.ts <url>              # 抓取 URL 并入库
 *   bun ingest.ts --file <path>      # 读取本地文件入库
 *   bun ingest.ts --rebuild          # 重建整个知识库索引
 */

import { existsSync, mkdirSync, readFileSync, readdirSync, writeFileSync } from "fs";
import { basename, dirname, extname, join, resolve } from "path";

// ==================== 配置 ====================
const VAULT_PATH = "/Users/tangchengbaiair/Downloads/ob-tang";
const DIRS = {
  raw: join(VAULT_PATH, "01零散资料"),
  wiki: join(VAULT_PATH, "10-Atlas"),
  inbox: join(VAULT_PATH, "Inbox"),
  clippings: join(VAULT_PATH, "Clippings"),
};

const QWEN_API_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions";
const QWEN_MODEL = "qwen-plus";
const API_KEY = process.env.DASHSCOPE_API_KEY;

// ==================== 类型定义 ====================
interface Frontmatter {
  title: string;
  source?: string;
  date: string;
  tags: string[];
  concepts: string[];
  summary: string;
  status: "raw" | "processed" | "indexed";
}

interface IngestResult {
  filePath: string;
  frontmatter: Frontmatter;
  linkedConcepts: string[];
}

// ==================== 工具函数 ====================
function getToday(): string {
  return new Date().toISOString().split("T")[0];
}

function sanitizeFilename(name: string): string {
  return name
    .replace(/[<>:"/\\|?*\x00-\x1f]/g, "-")
    .replace(/\s+/g, "-")
    .slice(0, 100);
}

function generateFrontmatter(data: Frontmatter): string {
  const yaml = [
    "---",
    `title: ${data.title}`,
    data.source ? `source: ${data.source}` : "",
    `date: ${data.date}`,
    `tags: [${data.tags.join(", ")}]`,
    `concepts: [${data.concepts.join(", ")}]`,
    `summary: ${data.summary}`,
    `status: ${data.status}`,
    "---",
    "",
  ];
  return yaml.filter(Boolean).join("\n");
}

// ==================== Jina 抓取 ====================
async function fetchJinaContent(url: string): Promise<{ title: string; content: string }> {
  const jinaUrl = `https://r.jina.ai/${url}`;
  console.log(`[INGEST] 正在抓取: ${jinaUrl}`);

  const response = await fetch(jinaUrl, {
    headers: {
      "Accept": "text/markdown",
    },
  });

  if (!response.ok) {
    throw new Error(`Jina 抓取失败: ${response.status} ${response.statusText}`);
  }

  const content = await response.text();

  // 从内容中提取标题（第一行或前50字符）
  const lines = content.split("\n").filter((l) => l.trim());
  const title = lines[0]?.replace(/^#+\s*/, "").slice(0, 50) || "未命名文档";

  return { title, content };
}

// ==================== Qwen API ====================
async function callQwen(messages: Array<{ role: string; content: string }>): Promise<string> {
  if (!API_KEY) {
    throw new Error("未设置 DASHSCOPE_API_KEY 环境变量");
  }

  const response = await fetch(QWEN_API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${API_KEY}`,
    },
    body: JSON.stringify({
      model: QWEN_MODEL,
      messages,
      temperature: 0.3,
    }),
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`Qwen API 错误: ${response.status} - ${error}`);
  }

  const data = await response.json();
  return data.choices[0].message.content;
}

async function extractConcepts(content: string): Promise<{ concepts: string[]; summary: string; tags: string[] }> {
  const prompt = `请分析以下文本，提取关键信息并以 JSON 格式返回：

1. concepts: 提取5-10个核心概念/术语（简短词组）
2. summary: 生成100-200字的中文摘要
3. tags: 推荐3-7个标签（用于知识分类）

返回格式严格如下：
{
  "concepts": ["概念1", "概念2", ...],
  "summary": "摘要内容...",
  "tags": ["标签1", "标签2", ...]
}

文本内容：
${content.slice(0, 8000)}`;

  try {
    const result = await callQwen([{ role: "user", content: prompt }]);

    // 尝试解析 JSON
    const jsonMatch = result.match(/\{[\s\S]*\}/);
    if (jsonMatch) {
      const parsed = JSON.parse(jsonMatch[0]);
      return {
        concepts: parsed.concepts || [],
        summary: parsed.summary || "暂无摘要",
        tags: parsed.tags || ["未分类"],
      };
    }
  } catch (e) {
    console.warn("[WARN] Qwen 解析失败，使用默认提取");
  }

  // 兜底方案
  return {
    concepts: ["待整理"],
    summary: content.slice(0, 150) + "...",
    tags: ["未分类"],
  };
}

// ==================== 文件操作 ====================
function saveMarkdown(
  dir: string,
  filename: string,
  frontmatter: Frontmatter,
  content: string
): string {
  if (!existsSync(dir)) {
    mkdirSync(dir, { recursive: true });
  }

  const filePath = join(dir, `${filename}.md`);
  const fullContent = generateFrontmatter(frontmatter) + "\n" + content;

  writeFileSync(filePath, fullContent, "utf-8");
  return filePath;
}

// ==================== 索引更新 ====================
async function updateWikiIndex(frontmatter: Frontmatter, sourcePath: string): Promise<string[]> {
  const linkedConcepts: string[] = [];
  const wikiConceptsDir = join(DIRS.wiki, "概念条目");

  if (!existsSync(wikiConceptsDir)) {
    mkdirSync(wikiConceptsDir, { recursive: true });
  }

  for (const concept of frontmatter.concepts) {
    const conceptFile = join(wikiConceptsDir, `${sanitizeFilename(concept)}.md`);

    if (!existsSync(conceptFile)) {
      // 创建新概念条目
      const conceptContent = generateFrontmatter({
        title: concept,
        date: getToday(),
        tags: ["概念", ...frontmatter.tags],
        concepts: [concept],
        summary: `与"${frontmatter.title}"相关的概念`,
        status: "indexed",
      }) + `\n\n## 定义\n\n待补充...\n\n## 相关资料\n\n- [[${basename(sourcePath, ".md")}]]\n`;

      writeFileSync(conceptFile, conceptContent, "utf-8");
      linkedConcepts.push(concept);
    } else {
      // 追加反向链接
      const existing = readFileSync(conceptFile, "utf-8");
      const backlink = `- [[${basename(sourcePath, ".md")}]]`;
      if (!existing.includes(backlink)) {
        writeFileSync(conceptFile, existing + `\n${backlink}\n`, "utf-8");
      }
      linkedConcepts.push(concept);
    }
  }

  return linkedConcepts;
}

// ==================== 主流程 ====================
async function ingestUrl(url: string): Promise<IngestResult> {
  console.log(`[INGEST] 开始处理 URL: ${url}`);

  // 1. 抓取内容
  const { title, content } = await fetchJinaContent(url);
  console.log(`[INGEST] 标题: ${title}`);

  // 2. 提取概念
  console.log(`[INGEST] 调用 Qwen 提取概念...`);
  const extracted = await extractConcepts(content);
  console.log(`[INGEST] 提取到 ${extracted.concepts.length} 个概念`);

  // 3. 保存到 clippings
  const frontmatter: Frontmatter = {
    title,
    source: url,
    date: getToday(),
    tags: extracted.tags,
    concepts: extracted.concepts,
    summary: extracted.summary,
    status: "processed",
  };

  const filename = sanitizeFilename(title);
  const filePath = saveMarkdown(DIRS.clippings, filename, frontmatter, content);
  console.log(`[INGEST] 已保存到: ${filePath}`);

  // 4. 更新知识索引
  console.log(`[INGEST] 更新知识索引...`);
  const linkedConcepts = await updateWikiIndex(frontmatter, filePath);

  // 5. 同时保存到 inbox 作为备份
  saveMarkdown(DIRS.inbox, `${filename}-backup`, { ...frontmatter, status: "raw" }, content);

  return { filePath, frontmatter, linkedConcepts };
}

async function ingestFile(filePath: string): Promise<IngestResult> {
  console.log(`[INGEST] 开始处理文件: ${filePath}`);

  if (!existsSync(filePath)) {
    throw new Error(`文件不存在: ${filePath}`);
  }

  const content = readFileSync(filePath, "utf-8");
  const ext = extname(filePath);
  const filename = basename(filePath, ext);

  // 提取概念
  console.log(`[INGEST] 调用 Qwen 提取概念...`);
  const extracted = await extractConcepts(content);

  const frontmatter: Frontmatter = {
    title: filename,
    source: filePath,
    date: getToday(),
    tags: [...extracted.tags, "本地文件"],
    concepts: extracted.concepts,
    summary: extracted.summary,
    status: "processed",
  };

  // 保存到 raw
  const savedPath = saveMarkdown(DIRS.raw, filename, frontmatter, content);
  console.log(`[INGEST] 已保存到: ${savedPath}`);

  // 更新索引
  const linkedConcepts = await updateWikiIndex(frontmatter, savedPath);

  return { filePath: savedPath, frontmatter, linkedConcepts };
}

async function rebuildIndex(): Promise<void> {
  console.log("[INGEST] 开始重建知识库索引...");

  // 扫描所有目录收集概念
  const allFiles: string[] = [];
  const scanDirs = [DIRS.raw, DIRS.clippings, DIRS.inbox];

  for (const dir of scanDirs) {
    if (!existsSync(dir)) continue;

    const files = readdirSync(dir)
      .filter((f) => f.endsWith(".md"))
      .map((f) => join(dir, f));
    allFiles.push(...files);
  }

  console.log(`[INGEST] 扫描到 ${allFiles.length} 个文件`);

  const allConcepts = new Set<string>();
  const conceptToFiles = new Map<string, string[]>();

  // 提取所有概念
  for (const file of allFiles) {
    const content = readFileSync(file, "utf-8");
    const conceptMatch = content.match(/concepts:\s*\[(.*?)\]/s);

    if (conceptMatch) {
      const concepts = conceptMatch[1]
        .split(",")
        .map((c) => c.trim().replace(/["']/g, ""))
        .filter(Boolean);

      for (const concept of concepts) {
        allConcepts.add(concept);
        if (!conceptToFiles.has(concept)) {
          conceptToFiles.set(concept, []);
        }
        conceptToFiles.get(concept)!.push(file);
      }
    }
  }

  // 重建概念条目
  const wikiConceptsDir = join(DIRS.wiki, "概念条目");
  if (!existsSync(wikiConceptsDir)) {
    mkdirSync(wikiConceptsDir, { recursive: true });
  }

  for (const concept of allConcepts) {
    const conceptFile = join(wikiConceptsDir, `${sanitizeFilename(concept)}.md`);
    const files = conceptToFiles.get(concept) || [];

    const content = generateFrontmatter({
      title: concept,
      date: getToday(),
      tags: ["概念", "索引"],
      concepts: [concept],
      summary: `知识库中共有 ${files.length} 个文件涉及此概念`,
      status: "indexed",
    }) + "\n\n## 定义\n\n待补充...\n\n## 相关资料\n\n" +
      files.map((f) => `- [[${basename(f, ".md")}]]`).join("\n");

    writeFileSync(conceptFile, content, "utf-8");
  }

  console.log(`[INGEST] 索引重建完成，共处理 ${allConcepts.size} 个概念`);
}

// ==================== CLI ====================
async function main() {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.log(`
用法:
  bun ingest.ts <url>              # 抓取 URL 并入库
  bun ingest.ts --file <path>      # 读取本地文件入库
  bun ingest.ts --rebuild          # 重建整个知识库索引

环境变量:
  DASHSCOPE_API_KEY - Qwen API 密钥
`);
    process.exit(1);
  }

  try {
    if (args[0] === "--rebuild") {
      await rebuildIndex();
    } else if (args[0] === "--file") {
      if (!args[1]) {
        console.error("[ERROR] 请指定文件路径");
        process.exit(1);
      }
      const result = await ingestFile(resolve(args[1]));
      printResult(result);
    } else {
      // 假设是 URL
      const result = await ingestUrl(args[0]);
      printResult(result);
    }
  } catch (error) {
    console.error("[ERROR]", error instanceof Error ? error.message : error);
    process.exit(1);
  }
}

function printResult(result: IngestResult) {
  console.log("\n" + "=".repeat(50));
  console.log("✅ 入库完成");
  console.log("=".repeat(50));
  console.log(`📄 文件: ${result.filePath}`);
  console.log(`📝 标题: ${result.frontmatter.title}`);
  console.log(`🏷️  标签: ${result.frontmatter.tags.join(", ")}`);
  console.log(`💡 概念: ${result.frontmatter.concepts.join(", ")}`);
  console.log(`🔗 关联: ${result.linkedConcepts.length} 个概念条目`);
  console.log("-".repeat(50));
  console.log("摘要:");
  console.log(result.frontmatter.summary);
  console.log("=".repeat(50));
}

main();
