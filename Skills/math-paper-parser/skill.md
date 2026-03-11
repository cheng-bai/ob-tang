# skill

## 触发条件

当用户请求以下操作时触发:
- "解析数学试卷"
- "把试卷转 Obsidian"
- "把 Markdown 试卷导出"
- "数学试卷变 Obsidian"
- 处理试卷文件

## 做什么

1. 找到用户的数学试卷 Markdown 文件
2. 使用 `math_paper_parser.py` 解析试卷为 JSON
3. 使用 `json_to_obsidian.py` 导出为 Obsidian 格式
4. 输出包含:
   - 每道题的独立 MD 文件（带 frontmatter）
   - 按题型分类
   - 按知识点分类
   - 学生版（答案隐藏）
   - Dataview 查询示例

## 前提条件

- 试卷必须是 Markdown 格式（.md）
- 试卷必须包含答案（【答案】）和解析（【解析】）
- 题型用 ## 一、选择题 / ## 二、填空题 / ## 三、解答题 标记

## 输出位置

```
Skills/math-paper-parser/obsidian/
```

## 使用示例

```
用户: 帮我解析这个试卷文件

AI: 好的，请提供试卷文件路径，或告诉我文件在哪里。
（用户提供路径后）
AI: 开始解析...
1. 解析试卷 JSON... ✅ 21 道题
2. 导出 Obsidian 格式... ✅
3. 生成学生版... ✅

已导出到: Skills/math-paper-parser/obsidian/
可以将这个文件夹复制到你的 Obsidian 库中使用。
```

## 相关文件

- `math_paper_parser.py` - 解析试卷为 JSON
- `json_to_obsidian.py` - 导出为 Obsidian 格式
- `README.md` - 详细使用说明
