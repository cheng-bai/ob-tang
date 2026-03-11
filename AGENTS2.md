# AGENTS2

> 本文件供 AI 代理参考，帮助理解承白老师的 Obsidian 教学知识管理系统

---

## 项目概述

这是一个**高中数学教学知识管理系统**，用于：
- 管理教学资源（试卷、讲义、题目）
- 构建知识体系（高中数学知识点）
- 自动化输出（Markdown 转 PDF 打印）
- AI 辅助教学

---

## 目录结构

```
ob-tang/
├── 00-System/                 # 系统引擎：定义"怎么做"
│   ├── Context/              # AI 角色、Prompt、规则
│   ├── Templates/            # 文档模板
│   ├── Assets/               # Obsidian 配置、Excalidraw、资源库
│   └── Scripts/              # 自动化脚本
├── 10-Atlas/                 # 知识底座：定义"是什么"
│   └── 05-知识汇总-数学知识按主题分类/  # 知识索引
├── 20-Product/               # 教学产出：定义"做了什么"
│   ├── 01-数学教学/          # 试卷、讲义、题目集
│   └── Question-Bank/        # 结构化题库
├── 30-Log/                   # 认知流：定义"想了什么"
│   ├── Daily/                # 日记
│   ├── Inbox/                # 灵感收集
│   └── Insights/             # AI 工作日志、经验总结
├── Skills/                   # 技能系统
│   └── markdown-print-kit/   # 打印输出系统
└── .gitignore
```

---

## 模板使用规范

### 模板位置
`00-System/Templates/`

### 可用模板

| 模板              | 用途      |
| :-------------- | :------ |
| `试卷/高考模拟卷模板.md` | 一模、二模考试 |
| `试卷/功底考模板.md`   | 教师功底考核  |
| `讲义/新授课讲义模板.md` | 新课教学    |
| `讲义/复习课讲义模板.md` | 章节复习    |
| `练习/日日练模板.md`   | 每日练习    |
| `通用/题目收集模板.md`  | 单题精析    |

### 模板变量
使用 Templater 语法：`{{title}}`、`{{date}}`、`{{topic}}`

---

## Dataview 查询规范

### 索引页面
`10-Atlas/05-知识汇总-数学知识按主题分类/📊-知识索引中心.md`

### 常用查询

```dataview
FROM "01-数学教学"
WHERE contains(tags, "题目收集")
LIMIT 10
```

### Frontmatter 规范

```yaml
---
title: 题目名称
tags: [题目收集, 函数, 高考真题]
难度: ⭐⭐⭐
来源: 2024高考
年份: 2024
知识点: [函数, 零点]
---
```

---

## LLM Context 调用方式

### 基础配置
1. **个人简介**：`00-System/Context/Personal Profile/个人简介.md`
2. **使用规则**：`00-System/Context/Basic Rules/使用规则.md`
3. **解题规范**：`00-System/Context/Teaching Rules/解题步骤规范.md`
4. **教学风格**：`00-System/Context/Teaching Rules/教学风格偏好.md`

### 自定义 AI 角色
`00-System/Context/自定义助手/` 目录下的提示词可直接使用

---

## 工作日志记录规范

### 位置
`30-Log/Insights/`

### 命名格式
```
YYYY-MM-DD-序号-内容关键词.md
```

示例：
- `2026-02-18-01-obsidian五项改进.md`
- `2026-02-18-02-系统评价与总结.md`

### 内容要求
- 开头包含时间戳
- 记录 AI 执行的操作
- 列出变更的文件
- 说明待办事项

---

## 打印输出规范

### 工具
`Skills/markdown-print-kit/`

### 题块语法
```markdown
:::space type=mc level=A lines=2
:::

:::space type=fill level=B lines=3
:::

:::space type=solve level=C lines=10
:::
```

### 参数说明
- `type`: `mc`（选择）| `fill`（填空）| `solve`（解答）
- `level`: `A`（基础）| `B`（中档）| `C`（难题）
- `lines`: 留白行数

---

## AI 交互原则

1. **先确认理解，再执行**
2. **重要操作前询问确认**
3. **复杂任务先列计划**
4. **数学内容必须准确无误**

---

## 常用操作示例

### 创建新讲义
1. 复制 `00-System/Templates/讲义/新授课讲义模板.md`
2. 填写模板变量
3. 保存到 `20-Product/01-数学教学/讲义/`

### 添加题目索引
1. 使用 `00-System/Templates/通用/题目收集模板.md`
2. 填写 frontmatter（tags、难度、知识点）
3. 保存到 `20-Product/01-数学教学/1-题目集/`

### 查询知识资源
1. 打开 `📊-知识索引中心.md`
2. 使用 Dataview 查询

---

## 注意事项

- 所有 Markdown 文件使用中文标点
- 数学公式使用 LaTeX 语法
- 题目答案放在 HTML 注释 `<!-- -->` 中（学生版隐藏）
- 大型附件（PDF、图片）不加入版本控制
