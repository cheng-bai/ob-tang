# Git 跨平台工作流指南

> 本指南规范在 Windows 和 macOS 上的 Git 使用方式

---

## 🔧 初始化（每台设备只需一次）

### macOS 上首次配置
```bash
cd /Users/thj/Downloads/ob-tang

# 1. 配置个人信息
git config user.name "cheng-bai"
git config user.email "1005873883@qq.com"

# 2. 跨平台核心配置
git config core.autocrlf input           # 提交时转换为 LF，检出时不转换
git config core.ignorecase false         # 严格区分文件大小写
git config core.safecrlf warn            # 警告不安全的换行符转换

# 3. 编码配置
git config core.quotepath false          # 支持中文文件名显示

# 4. 全局缓存忽略配置（防止各项目缓存污染）
touch ~/.gitignore_global
git config --global core.excludesfile ~/.gitignore_global
```

### Windows 上首次配置
```bash
cd /path/to/ob-tang

# 1. 配置个人信息（保持一致！）
git config user.name "cheng-bai"
git config user.email "1005873883@qq.com"

# 2. 跨平台核心配置
git config core.autocrlf true            # 提交时转换为 LF，检出时转换为 CRLF
git config core.longpaths true           # 支持长文件名（Windows 260 字符限制）
git config core.safecrlf warn            # 警告不安全的转换

# 3. 编码配置
git config core.quotepath false          # 支持中文文件名显示
```

---

## 📌 日常工作流

### ✅ 提交前检查清单
```bash
# 1. 检查状态
git status

# 2. 查看改动（确保没有意外文件）
git diff

# 3. 暂存改动
git add .

# 4. 确认暂存内容
git status

# 5. 提交（使用规范的提交信息）
git commit -m "type: 描述信息"
```

### 🔀 提交信息规范（两平台统一）
```
feat:  新增功能          (New feature)
fix:   修复缺陷          (Bug fix)
docs:  文档更新          (Documentation)
style: 格式/空格调整     (Formatting)
chore: 维护/清理/配置    (Chore)
test:  测试添加/修改     (Test)
perf:  性能优化          (Performance)
```

**例子：**
```bash
git commit -m "feat: 添加高中数学函数知识点汇总"
git commit -m "fix: 修复题目收集模板的 frontmatter"
git commit -m "chore: 清理过期的临时文件"
```

### 📤 推送到远程
```bash
# 推送当前分支
git push origin main

# 或设置跟踪关系后直接推送
git push
```

---

## 🛡️ 防止缓存文件提交

### 问题：本地电脑产生的缓存（.cache、.DS_Store 等）被推送

### 解决方案

#### 方案 1️⃣：全局 .gitignore（推荐 - 一次配置，所有项目生效）

```bash
# 1. 创建全局忽略文件
touch ~/.gitignore_global

# 2. 添加常见缓存规则
cat >> ~/.gitignore_global << 'EOF'
# macOS
.DS_Store
.AppleDouble
.LSOverride
*.swp

# Windows
Thumbs.db
ehthumbs.db
Desktop.ini

# Obsidian & 第三方工具
.makemd/
.smart-env/
.obsidian/cache/
.obsidian/workspace.json

# 编辑器
.vscode/settings.json
.idea/
EOF

# 3. 配置 Git 使用全局文件
git config --global core.excludesfile ~/.gitignore_global

# 4. 验证配置
git config --global core.excludesfile
```

#### 方案 2️⃣：项目级 .gitignore（已在本项目配置）

本库的 `.gitignore` 已包含常见缓存规则，如需添加：

```bash
# 添加新规则
echo "新规则" >> .gitignore

# 提交更新
git add .gitignore
git commit -m "chore: 添加忽略规则"
```

#### 方案 3️⃣：Git 预提交钩子（自动检查）

本库已在 `.git/hooks/pre-commit` 配置自动检查机制：

```bash
# 钩子会在提交时自动检查是否有缓存文件
# 如果发现问题，会阻止提交并给出修复提示

# 若需强制提交，可使用：
git commit --no-verify
```

#### 方案 4️⃣：定期清理缓存

```bash
# 创建清理脚本
cat > cleanup-cache.sh << 'EOF'
#!/bin/bash
echo "🧹 清理缓存文件..."
rm -rf .obsidian/cache
rm -f .obsidian/workspace.json
rm -rf .makemd/
find . -name ".DS_Store" -delete
find . -name "Thumbs.db" -delete
echo "✅ 清理完成"
EOF

chmod +x cleanup-cache.sh

# 在 push 之前运行
./cleanup-cache.sh
git add .
git commit -m "chore: 清理缓存"
git push
```

### 了解 .gitignore 的工作原理

```bash
# 检查文件是否被忽略
git check-ignore -v <文件名>

# 查看目前忽略的所有规则
git status -u

# 强制追踪被忽略的文件（不推荐）
git add -f <文件>
```

### ⚡ 快速参考

| 场景 | 命令 |
|:---|:---|
| 检查状态前 | `git clean -fd`（删除未追踪文件） |
| 提交前清理 | `./cleanup-cache.sh` 或手动清理 |
| 如果已推送缓存 | `git rm --cached <文件>` 然后提交 |
| 查看所有忽略规则 | `git config --global core.excludesfile` |

---

## ⚠️ 跨平台常见问题

### 1️⃣ **换行符问题（CRLF vs LF）**

**问题说明：**
- Windows 使用 `CRLF`（\r\n）
- macOS/Linux 使用 `LF`（\n）
- Git 自动转换容易导致冲突

**解决方案：**
```bash
# 已在配置中设置：
# macOS: core.autocrlf = input
# Windows: core.autocrlf = true

# 如果出现警告，用这个修复所有文件
git add --renormalize .
git commit -m "chore: 修正换行符"
```

### 2️⃣ **文件大小写问题**

**问题说明：**
- Windows 不区分大小写（ThE_File.md == the_file.md）
- macOS 默认不区分（但配置后可以区分）
- 导致跨平台冲突

**解决方案：**
```bash
# 已配置 core.ignorecase=false
# 坚持使用小写文件名或规范命名

# 如果已经跟踪了大小写不同的文件，需要手动修复
git rm --cached OLD_NAME.md
git add new_name.md
git commit -m "chore: 统一文件命名大小写"
```

### 3️⃣ **编码问题（中文文件名）**

**已配置解决：**
```bash
git config core.quotepath false  # 两平台都执行
```

### 4️⃣ **路径分隔符问题**

**不要手动处理，Git 自动转换：**
```bash
# ❌ 不要这样写：
git add "10-Atlas\01零散资料\test.md"

# ✅ 这样写：
git add "10-Atlas/01零散资料/test.md"  # Git 自动适配平台

# 或使用通配符：
git add "10-Atlas/**/test.md"
```

---

## 🔄 同步工作流（多设备）

### 场景1：Mac 上修改后推送，Win 上拉取

```bash
# Mac 上：
git add .
git commit -m "feat: 更新讲义"
git push origin main

# Windows 上：
git fetch                  # 先获取远程更新（不合并）
git status                 # 检查差异
git pull origin main       # 合并到本地
```

### 场景2：Win 上修改，Mac 上工作

```bash
# 每次开始工作前：
git fetch origin           # 获取最新版本
git status                 # 检查本地修改

# 如果有本地改动：
git stash                  # 暂存本地改动
git pull origin main       # 拉取最新版本
git stash pop              # 恢复本地改动（可能需要解决冲突）
```

---

## 🚨 冲突处理

### 遇到冲突时：

```bash
# 1. 查看冲突文件
git status

# 2. 查看冲突内容
git diff

# 3. 手动编辑文件，解决冲突（查找 <<<<<<< =======  >>>>>>>）

# 4. 标记为已解决
git add <冲突文件>

# 5. 完成合并
git commit -m "chore: 解决合并冲突"
```

---

## 📊 版本管理建议

### 每个重要更新都打标签
```bash
# 添加标签
git tag -a v1.1.0 -m "春季期中前的完整版本"

# 推送标签
git push origin v1.1.0

# 查看所有标签
git tag -l
```

---

## 💡 跨平台最佳实践

| 规则 | 说明 |
|:---|:---|
| ✅ 使用 `/` 作为路径分隔符 | Git 自动处理 |
| ✅ 文件名全部小写 | 避免大小写冲突 |
| ✅ 避免特殊字符和空格 | 特别是 Windows 路径限制 |
| ✅ 提交前检查 `.gitignore` | 确保系统文件被忽略 |
| ✅ 每次切换设备先 `git fetch` | 同步最新版本 |
| ✅ 提交信息用英文 + 中文 | 保证可读性 |
| ❌ 不用混合 CRLF 和 LF | 已配置自动处理 |
| ❌ 不追踪二进制文件（PDF/图片） | 已在 .gitignore 中配置 |

---

## 🔍 监控脚本（可选）

### 创建 Git 钩子检查规范性

```bash
# 在项目根目录创建 .git/hooks/pre-commit
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
# 检查换行符是否正确
if git diff --cached --check 2>/dev/null | grep -E "CRLF|trailing whitespace"; then
    echo "⚠️ 检测到行尾格式问题，请使用："
    echo "git add --renormalize ."
    exit 1
fi
EOF

chmod +x .git/hooks/pre-commit
```

---

## 📞 快速参考

```bash
# 查看配置
git config --list | grep core

# 重新下载（覆盖本地改动）
git fetch origin
git reset --hard origin/main

# 查看提交历史
git log --oneline -10

# 撤销最后一次提交（未推送）
git reset --soft HEAD~1

# 清理本地未追踪的文件
git clean -fd
```

---

**最后提醒：** 跨平台最关键的是 **设置 `core.autocrlf`** 和 **使用统一的路径分隔符 `/`**。其他问题都能自动解决！
