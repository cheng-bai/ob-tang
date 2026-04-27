#!/usr/bin/env bun
/**
 * Knowledge Ingest 体检脚本
 *
 * 检查知识库健康状况：
 * - 概念条目是否互相链接
 * - 孤儿页面检测
 * - 过时结论检查
 * - 索引同步状态
 */

import { existsSync, readFileSync, readdirSync, statSync } from "fs";
import { basename, join } from "path";

// ==================== 配置 ====================
const VAULT_PATH = "/Users/tangchengbaiair/Downloads/ob-tang";
const DIRS = {
  raw: join(VAULT_PATH, "01零散资料"),
  wiki: join(VAULT_PATH, "10-Atlas"),
  inbox: join(VAULT_PATH, "Inbox"),
  clippings: join(VAULT_PATH, "Clippings"),
};

// ==================== 类型定义 ====================
interface LintResult {
  orphaned: string[];           // 孤儿页面（无入链也无出链）
  brokenLinks: string[];        // 断链（指向不存在的文件）
  staleFiles: string[];         // 过时文件（超过90天未更新）
  unindexedConcepts: string[];  // 未索引的概念
  unlinkedConcepts: string[];   // 概念条目互相未链接
}

// ==================== 工具函数 ====================
function getAllMarkdownFiles(dir: string): string[] {
  if (!existsSync(dir)) return [];

  const files: string[] = [];
  const items = readdirSync(dir, { withFileTypes: true });

  for (const item of items) {
    const fullPath = join(dir, item.name);
    if (item.isDirectory()) {
      files.push(...getAllMarkdownFiles(fullPath));
    } else if (item.name.endsWith(".md")) {
      files.push(fullPath);
    }
  }

  return files;
}

function extractWikiLinks(content: string): string[] {
  const links: string[] = [];
  // 匹配 [[文件名]] 或 [[文件名|显示文本]]
  const regex = /\[\[([^\]|]+)(?:\|[^\]]+)?\]\]/g;
  let match;

  while ((match = regex.exec(content)) !== null) {
    links.push(match[1].trim());
  }

  return links;
}

function extractFrontmatter(content: string): Record<string, any> | null {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return null;

  const fm: Record<string, any> = {};
  const lines = match[1].split("\n");

  for (const line of lines) {
    const colonIndex = line.indexOf(":");
    if (colonIndex > 0) {
      const key = line.slice(0, colonIndex).trim();
      const value = line.slice(colonIndex + 1).trim();

      // 解析数组
      if (value.startsWith("[") && value.endsWith("]")) {
        fm[key] = value
          .slice(1, -1)
          .split(",")
          .map((v) => v.trim().replace(/["']/g, ""))
          .filter(Boolean);
      } else {
        fm[key] = value.replace(/["']/g, "");
      }
    }
  }

  return fm;
}

function getFileAgeDays(filePath: string): number {
  const stats = statSync(filePath);
  const now = Date.now();
  const modified = stats.mtime.getTime();
  return Math.floor((now - modified) / (1000 * 60 * 60 * 24));
}

// ==================== 检查函数 ====================
function checkOrphans(allFiles: string[], fileContents: Map<string, string>): string[] {
  const orphans: string[] = [];
  const allFileNames = new Set(allFiles.map((f) => basename(f, ".md")));
  const incomingLinks = new Map<string, number>();

  // 统计每个文件的入链数
  for (const [path, content] of fileContents) {
    const links = extractWikiLinks(content);
    for (const link of links) {
      incomingLinks.set(link, (incomingLinks.get(link) || 0) + 1);
    }
  }

  // 检查孤儿页面：无入链且无出链
  for (const file of allFiles) {
    const content = fileContents.get(file) || "";
    const fileName = basename(file, ".md");
    const outgoingLinks = extractWikiLinks(content).length;
    const incoming = incomingLinks.get(fileName) || 0;

    if (outgoingLinks === 0 && incoming === 0) {
      orphans.push(file);
    }
  }

  return orphans;
}

function checkBrokenLinks(allFiles: string[], fileContents: Map<string, string>): string[] {
  const broken: string[] = [];
  const allFileNames = new Set(allFiles.map((f) => basename(f, ".md")));

  for (const [path, content] of fileContents) {
    const links = extractWikiLinks(content);
    for (const link of links) {
      // 忽略外部链接和锚点
      if (link.startsWith("http") || link.includes("#")) continue;

      if (!allFileNames.has(link)) {
        broken.push(`${basename(path)} -> [[${link}]]`);
      }
    }
  }

  return broken;
}

function checkStaleFiles(allFiles: string[]): string[] {
  const stale: string[] = [];
  const STALE_DAYS = 90;

  for (const file of allFiles) {
    const age = getFileAgeDays(file);
    if (age > STALE_DAYS) {
      stale.push(`${file} (${age}天)`);
    }
  }

  return stale;
}

function checkUnindexedConcepts(allFiles: string[], fileContents: Map<string, string>): string[] {
  const unindexed: string[] = [];
  const wikiConceptsDir = join(DIRS.wiki, "概念条目");

  if (!existsSync(wikiConceptsDir)) return [];

  const conceptFiles = new Set(
    readdirSync(wikiConceptsDir)
      .filter((f) => f.endsWith(".md"))
      .map((f) => basename(f, ".md"))
  );

  // 收集所有 frontmatter 中的概念
  const allConcepts = new Set<string>();
  for (const [path, content] of fileContents) {
    const fm = extractFrontmatter(content);
    if (fm?.concepts) {
      for (const concept of fm.concepts) {
        allConcepts.add(concept);
      }
    }
  }

  // 检查哪些概念没有对应的条目
  for (const concept of allConcepts) {
    const sanitized = concept.replace(/[<>:"/\\|?*\x00-\x1f]/g, "-").slice(0, 100);
    if (!conceptFiles.has(sanitized) && !conceptFiles.has(concept)) {
      unindexed.push(concept);
    }
  }

  return unindexed;
}

function checkUnlinkedConcepts(): string[] {
  const unlinked: string[] = [];
  const wikiConceptsDir = join(DIRS.wiki, "概念条目");

  if (!existsSync(wikiConceptsDir)) return [];

  const conceptFiles = getAllMarkdownFiles(wikiConceptsDir);
  const conceptNames = new Set(
    conceptFiles.map((f) => basename(f, ".md"))
  );

  for (const file of conceptFiles) {
    const content = readFileSync(file, "utf-8");
    const links = extractWikiLinks(content);
    const fileName = basename(file, ".md");

    // 检查该概念条目是否链接到其他概念
    let hasConceptLink = false;
    for (const link of links) {
      if (conceptNames.has(link) && link !== fileName) {
        hasConceptLink = true;
        break;
      }
    }

    if (!hasConceptLink && links.length <= 1) {
      // 只有自身链接或没有链接
      unlinked.push(fileName);
    }
  }

  return unlinked;
}

// ==================== 主流程 ====================
async function runLint(): Promise<LintResult> {
  console.log("[LINT] 开始知识库体检...\n");

  // 收集所有文件
  const allFiles: string[] = [];
  const scanDirs = [DIRS.raw, DIRS.wiki, DIRS.inbox, DIRS.clippings];

  for (const dir of scanDirs) {
    const files = getAllMarkdownFiles(dir);
    allFiles.push(...files);
  }

  console.log(`[LINT] 共扫描到 ${allFiles.length} 个 Markdown 文件`);

  // 预加载文件内容
  const fileContents = new Map<string, string>();
  for (const file of allFiles) {
    try {
      fileContents.set(file, readFileSync(file, "utf-8"));
    } catch (e) {
      console.warn(`[WARN] 无法读取文件: ${file}`);
    }
  }

  // 执行各项检查
  const result: LintResult = {
    orphaned: checkOrphans(allFiles, fileContents),
    brokenLinks: checkBrokenLinks(allFiles, fileContents),
    staleFiles: checkStaleFiles(allFiles),
    unindexedConcepts: checkUnindexedConcepts(allFiles, fileContents),
    unlinkedConcepts: checkUnlinkedConcepts(),
  };

  return result;
}

function printReport(result: LintResult) {
  console.log("\n" + "=".repeat(60));
  console.log("📊 知识库体检报告");
  console.log("=".repeat(60));

  // 总体健康度
  const totalIssues =
    result.orphaned.length +
    result.brokenLinks.length +
    result.staleFiles.length +
    result.unindexedConcepts.length +
    result.unlinkedConcepts.length;

  if (totalIssues === 0) {
    console.log("\n✅ 知识库状态良好，未发现异常！");
  } else {
    console.log(`\n⚠️  发现 ${totalIssues} 个问题需要处理\n`);

    // 孤儿页面
    if (result.orphaned.length > 0) {
      console.log(`🚫 孤儿页面 (${result.orphaned.length}个)`);
      console.log("   这些页面既无入链也无出链，建议:");
      console.log("   - 添加相关链接到其他页面");
      console.log("   - 或考虑归档/删除");
      result.orphaned.slice(0, 5).forEach((f) => {
        console.log(`   • ${basename(f)}`);
      });
      if (result.orphaned.length > 5) {
        console.log(`   ... 还有 ${result.orphaned.length - 5} 个`);
      }
      console.log();
    }

    // 断链
    if (result.brokenLinks.length > 0) {
      console.log(`🔗 断链 (${result.brokenLinks.length}个)`);
      console.log("   以下链接指向不存在的页面:");
      result.brokenLinks.slice(0, 5).forEach((link) => {
        console.log(`   • ${link}`);
      });
      if (result.brokenLinks.length > 5) {
        console.log(`   ... 还有 ${result.brokenLinks.length - 5} 个`);
      }
      console.log();
    }

    // 过时文件
    if (result.staleFiles.length > 0) {
      console.log(`⏰ 过时文件 (${result.staleFiles.length}个)`);
      console.log("   超过90天未更新的文件:");
      result.staleFiles.slice(0, 5).forEach((f) => {
        console.log(`   • ${basename(f)}`);
      });
      if (result.staleFiles.length > 5) {
        console.log(`   ... 还有 ${result.staleFiles.length - 5} 个`);
      }
      console.log();
    }

    // 未索引概念
    if (result.unindexedConcepts.length > 0) {
      console.log(`📑 未索引概念 (${result.unindexedConcepts.length}个)`);
      console.log("   这些概念在文档中被提到但无对应条目:");
      result.unindexedConcepts.slice(0, 10).forEach((c) => {
        console.log(`   • ${c}`);
      });
      if (result.unindexedConcepts.length > 10) {
        console.log(`   ... 还有 ${result.unindexedConcepts.length - 10} 个`);
      }
      console.log();
    }

    // 孤立概念
    if (result.unlinkedConcepts.length > 0) {
      console.log(`🌐 孤立概念条目 (${result.unlinkedConcepts.length}个)`);
      console.log("   这些概念条目未与其他概念建立链接:");
      result.unlinkedConcepts.slice(0, 5).forEach((c) => {
        console.log(`   • ${c}`);
      });
      if (result.unlinkedConcepts.length > 5) {
        console.log(`   ... 还有 ${result.unlinkedConcepts.length - 5} 个`);
      }
      console.log();
    }
  }

  console.log("=".repeat(60));
  console.log("建议操作:");
  console.log("  • 定期运行: bun lint.ts");
  console.log("  • 修复孤儿页面: 添加相关双向链接");
  console.log("  • 修复断链: 更新或删除失效链接");
  console.log("  • 更新概念索引: bun ingest.ts --rebuild");
  console.log("=".repeat(60));
}

// ==================== CLI ====================
async function main() {
  const args = process.argv.slice(2);

  if (args.includes("--help") || args.includes("-h")) {
    console.log(`
用法:
  bun lint.ts           # 运行完整体检
  bun lint.ts --json    # 输出 JSON 格式报告

检查项:
  - 孤儿页面: 既无入链也无出链的文件
  - 断链: 指向不存在页面的链接
  - 过时文件: 超过90天未更新的文件
  - 未索引概念: 被提到但无条目的概念
  - 孤立概念: 未与其他概念链接的条目
`);
    return;
  }

  const result = await runLint();

  if (args.includes("--json")) {
    console.log(JSON.stringify(result, null, 2));
  } else {
    printReport(result);
  }
}

main().catch((err) => {
  console.error("[ERROR]", err.message);
  process.exit(1);
});
