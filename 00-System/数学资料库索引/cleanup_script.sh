#!/bin/bash
# mini-数学资料库清理脚本
# 执行前请确保已备份重要文件

echo "=== mini-数学资料库清理脚本 ==="
echo ""

# 统计清理前的文件数和大小
echo "清理前统计..."
BEFORE_COUNT=$(find . -type f | wc -l)
BEFORE_SIZE=$(du -sh . 2>/dev/null | cut -f1)
echo "当前文件数: $BEFORE_COUNT"
echo "当前总大小: $BEFORE_SIZE"
echo ""

# 1. 删除系统文件
echo "1. 删除 .DS_Store 文件..."
find . -name ".DS_Store" -type f -delete
echo "   ✓ 完成"

# 2. 删除LaTeX编译中间文件
echo "2. 删除 LaTeX编译中间文件..."
find . \( -name "*.aux" -o -name "*.log" -o -name "*.out" -o -name "*.toc" -o -name "*.synctex.gz" \) -delete
echo "   ✓ 完成"

# 3. 删除Python缓存
echo "3. 删除 Python缓存..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -name "*.pyc" -delete
echo "   ✓ 完成"

# 4. 删除备份文件
echo "4. 删除备份文件..."
find . -name "*.bak" -delete
echo "   ✓ 完成"

# 5. 删除空目录
echo "5. 删除空目录..."
find . -type d -empty -delete
echo "   ✓ 完成"

echo ""
echo "=== 清理完成 ==="
echo ""

# 统计清理后的文件数和大小
AFTER_COUNT=$(find . -type f | wc -l)
AFTER_SIZE=$(du -sh . 2>/dev/null | cut -f1)
echo "清理后文件数: $AFTER_COUNT"
echo "清理后总大小: $AFTER_SIZE"
echo ""
echo "减少文件数: $((BEFORE_COUNT - AFTER_COUNT))"
