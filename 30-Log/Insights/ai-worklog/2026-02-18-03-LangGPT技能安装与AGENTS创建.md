# 2026-02-18-03-LangGPT技能安装与AGENTS创建

## 时间
2026-02-18 下午

## 背景
应承白老师要求，学习 LangGPT 框架并安装技能，同时为同步ob系统创建 AGENTS.md

---

## 完成内容

### 1. LangGPT 技能安装 ✅

#### 安装过程
- 研究 LangGPT 项目（https://github.com/langgptai/LangGPT）
- 由于原项目没有 Claude Code 的 skill 发布包，决定手动创建
- 参考现有技能结构（vue skill）构建 LangGPT 技能

#### 创建文件
| 文件 | 路径 |
|:---|:---|
| SKILL.md | ~/.agents/skills/langgpt/SKILL.md |
| GENERATION.md | ~/.agents/skills/langgpt/GENERATION.md |
| 符号链接 | ~/.codebuddy/skills/langgpt → ~/.agents/skills/langgpt |

#### 技能内容
- 基础角色模板（Role/Profile/Skills/Rules/Workflow/Initialization）
- 高级特性（变量系统、命令定义、条件逻辑）
- 常用模板（写作助手、代码审查、教学导师）
- 最佳实践

---

### 2. 错题分析助手提示词 ✅

应承白老师请求，生成完整的"高中数学错题分析助手"提示词

#### 创建文件
`00-LLM Context/自定义助手/错题分析助手.md`

#### 提示词结构
- Profile：角色定义
- Skills：错题诊断、知识点梳理、同类推荐、问题解析、反思总结
- Rules：准确无误、解析详细、推荐相关、亲切专业
- Workflow：六步流程
- OutputFormat：标准输出格式
- Initialization：友好开场白

---

### 3. 学习 AGENTS.md 规范 ✅

通过 WebFetch 学习 https://agents.md/ 网站内容

#### 核心要点
- AGENTS.md 是 AI 编程代理的标准化文档格式
- 被 60,000+ 开源项目采用
- 支持 OpenAI、Google、Cursor 等主流 AI 工具
- 相当于给 AI 看的 README

---

### 4. 为同步ob系统创建 AGENTS.md ✅

#### 创建文件
`/Users/thj/Downloads/同步ob系统/AGENTS.md`

#### 内容结构
| 章节 | 说明 |
|:---|:---|
| 项目概述 | 高中数学教学知识管理系统 |
| 目录结构 | 各文件夹用途说明 |
| 模板使用规范 | 模板位置、可变变量 |
| Dataview 查询规范 | 索引页面、frontmatter 规范 |
| LLM Context 调用方式 | AI 角色调用 |
| 工作日志记录规范 | 命名格式、内容要求 |
| 打印输出规范 | 题块语法、参数说明 |
| AI 交互原则 | 基本准则 |
| 常用操作示例 | 创建讲义、添加题目、查询资源 |
| 注意事项 | 中文标点、LaTeX、答案隐藏 |

---

## 新增/修改文件汇总

| 操作 | 文件路径 |
|:---|:---|
| 新建 | ~/.agents/skills/langgpt/SKILL.md |
| 新建 | ~/.agents/skills/langgpt/GENERATION.md |
| 新建 | ~/.codebuddy/skills/langgpt (符号链接) |
| 新建 | 同步ob系统/00-LLM Context/自定义助手/错题分析助手.md |
| 新建 | 同步ob系统/AGENTS.md |

---

## 待后续
- 测试 LangGPT 技能使用效果
- 完善自定义 AI 角色库
- 根据使用反馈优化 AGENTS.md

---

*由 CodeBuddy Code 自动记录*
