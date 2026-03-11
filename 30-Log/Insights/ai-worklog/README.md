# AI Worklog

用于记录 AI 每次生成/执行任务后的编程摘要。

## 使用示例

```bash
/Users/thj/Downloads/同步ob系统/memory/ai-worklog/log_ai_work.py \
  --task "构建记忆系统" \
  --purpose "创建分层记忆目录" \
  --actions "创建目录/写入 .abstract 和模板文件" \
  --files "/Users/thj/Downloads/同步ob系统/memory/ai-worklog/.abstract" \
  --result "完成 L0 索引与脚本" \
  --todo "无" \
  --base "/Users/thj/Downloads/同步ob系统/memory"
```

## 字段说明
- task: 任务标题
- purpose: 目的
- actions: 操作/命令
- files: 变更文件路径
- result: 结果
- todo: 待办/风险
