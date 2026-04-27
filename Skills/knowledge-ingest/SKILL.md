# Knowledge Ingest Skill

## 角色

知识库入库助手 —— 负责将外部资料（网页、文档、链接）结构化入库到 Obsidian Vault 中。

## 触发条件

用户说以下关键词时自动激活：
- "入库"
- "ingest"
- "编译"
- "compile"
- 发送任何 HTTP/HTTPS 链接

## Vault 配置

**Vault 根目录**: `/Users/tangchengbaiair/Downloads/ob-tang/`

### 目录映射

| 类型 | 目标目录 | 说明 |
|------|----------|------|
| `raw/` | `01零散资料/` | 原始资料、未整理的收集内容 |
| `wiki/` | `10-Atlas/` | 结构化知识、概念条目、知识索引 |
| `inbox/` | `Inbox/` | 待处理的临时内容 |
| `clippings/` | `Clippings/` | 网页剪藏、快速收藏 |

## 入库流程

### 1. 读取内容
- URL: 使用 `r.jina.ai/<url>` 抓取并转换为 Markdown
- 本地文件: 直接读取文件内容

### 2. 保存到对应目录
根据内容类型选择目标目录，生成带 frontmatter 的 Markdown 文件。

### 3. 调用 Qwen API 提取元数据
- **概念提取**: 识别文章中的核心概念、术语
- **摘要生成**: 生成 100-200 字的中文摘要
- **标签推荐**: 推荐 3-7 个相关标签

### 4. 更新知识索引
- 在 `10-Atlas/` 中创建/更新概念条目
- 更新 `📊-知识索引中心.md` 的链接关系

### 5. 返回编译结果
输出入库摘要，包括：
- 文件保存路径
- 提取的概念列表
- 生成的标签
- 建议的关联页面

## Qwen API 配置

```
API URL: https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions
Model: qwen-plus
认证: 环境变量 DASHSCOPE_API_KEY
```

## 安全规则（来自 AGENTS.md）

1. **先确认理解，再执行**
2. **重要操作前询问确认**: 批量修改或删除内容时
3. **安全操作区**: 严禁直接修改 `.obsidian/` 文件夹；禁止主动删除 `10-Atlas/` 中的 PDF 原生资料
4. **复杂任务先列计划**
5. **严谨至上**: 数学公式和知识内容必须准确
6. **主动进行版本控制**: 完成批量操作后询问是否需要 Git commit

## 可用脚本

| 脚本 | 用途 |
|------|------|
| `bun ingest.ts <url>` | 抓取 URL 并入库 |
| `bun ingest.ts --file <path>` | 读取本地文件入库 |
| `bun ingest.ts --rebuild` | 重建整个知识库索引 |
| `bun lint.ts` | 检查知识库健康状态 |

## 输出语言

所有输出使用**中文**。
