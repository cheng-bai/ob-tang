# dataview-queries

## 按难度筛选

### 基础题
```dataview
TABLE type, number, tags
FROM "obsidian/questions"
WHERE difficulty = "基础"
SORT number ASC
```

### 较难题
```dataview
TABLE type, number, tags
FROM "obsidian/questions"
WHERE difficulty = "较难"
SORT number ASC
```

## 按题型筛选

### 解答题
```dataview
TABLE number, tags, analysis
FROM "obsidian/questions"
WHERE type = "解答题"
SORT number ASC
```

## 按知识点筛选

### 三角函数
```dataview
TABLE number, type
FROM "obsidian/questions"
WHERE contains(tags, "三角函数")
SORT number ASC
```

### 平面向量
```dataview
TABLE number, type
FROM "obsidian/questions"
WHERE contains(tags, "平面向量")
SORT number ASC
```

---

*查询示例文件，仅供参考*
