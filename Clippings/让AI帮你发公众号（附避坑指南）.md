---
title: "让AI帮你发公众号（附避坑指南）"
source: "https://x.com/sitinme/status/2023930738773815314"
author:
  - "[[Unknown]]"
published: 2026-02-18
created: 2026-02-18
description:
tags:
  - "clippings"
---
# 让AI帮你发公众号（附避坑指南）
## 让AI帮你发公众号（附避坑指南）

跟 AI 说一句话，文章就自动出现在公众号草稿箱里。完整配置流程 + 所有踩过的坑。

\---

## 一、配置公众号 API（5分钟）

## 第1步：获取 AppID 和 AppSecret

登录 [mp.weixin.qq.com](https://mp.weixin.qq.com/) → 设置与开发 → 基本配置

• AppID：页面直接显示，复制即可

![图像](https://pbs.twimg.com/media/HBZyqkGbcAQy_hE?format=jpg&name=large)

• AppSecret：点"重置"生成新的（只显示一次，务必保存）

## 第2步：配置 IP 白名单

同页面找到 IP 白名单，加入服务器出口 IP。不加会报 40164 错误。

不知道出口 IP？终端执行 curl [ifconfig.me](https://ifconfig.me/)

如果通过代理上网，要加代理出口 IP，不是本机 IP。

## 第3步：告诉 AI

把 AppID 和 AppSecret 告诉你的 AI 助手，配置完成。

\---

## 二、AI 发文完整流程

你只需说："帮我写一篇 xxx 的文章，推到公众号草稿箱。"

AI 自动完成 4 个步骤：

1. 获取 access\_token — AppID + AppSecret 换临时令牌（2小时有效）
2. 上传图片到微信素材库 — 公众号只认 [mmbiz.qpic.cn](https://mmbiz.qpic.cn/) 域名的图片
3. 生成文章 HTML — 公众号本质是 HTML 渲染
4. 推送到草稿箱 — 调用 draft/add 接口

你的工作：打开草稿箱 → 预览 → 发布。

![图像](https://pbs.twimg.com/media/HBXOISIbcAIBPkm?format=png&name=large)

\---

## 三、最大的坑：中文乱码

第一次推送"成功"后，打开草稿箱看到的是这个：

![图像](https://pbs.twimg.com/media/HBXOIr0a8AAPfOG?format=png&name=large)

标题、正文，所有中文全变成了 \\u4eca\\u5929 这种转义码。只有英文和数字正常。

## 原因

Python requests 发 JSON 时默认 ensure\_ascii=True，所有中文被转成 \\uXXXX。正常情况服务端会自动解码，但微信公众号 API 不会——直接当原始文本存进去了。

## 错误写法（会乱码）

> \# 中文会变成 \\uXXXX

[requests.post](https://requests.post/)(url, json=data)

## 正确写法（解决乱码）

> \# 手动序列化，保留中文原文

[requests.post](https://requests.post/)(

url,

data=json.dumps(data, ensure\_ascii=False).encode("utf-8"),

headers={"Content-Type": "application/json; charset=utf-8"}

)

![图像](https://pbs.twimg.com/media/HBXOJDQasAAZF4o?format=png&name=large)

两个关键参数：

• ensure\_ascii=False：保留中文原文，不转义

• .encode("utf-8")：以 UTF-8 字节发送

\---

![图像](https://pbs.twimg.com/media/HBXOJavbcAQQE88?format=png&name=large)

## 四、其他踩坑记录

> 坑2：标题太长报 45003

微信标题限制约 64 字节（约20个中文字）。缩短标题即可。

> 坑3：图片不显示

公众号过滤所有非微信域名图片。必须先 uploadimg 到微信素材库。

> 坑4：HTML 标签兼容性差

公众号对 h2/ul/li/code 渲染不稳定。全部用 p + inline style。

> 坑5：IP 白名单是代理出口 IP

通过代理访问微信 API，白名单要加代理出口 IP，不是本机 IP。

\---

## 五、效果对比

以前：写稿1h + 排版30min + 配图20min + 检查10min = 2小时

现在：跟AI说一句话 + 检查5min + 发布 = 10分钟

节省 90% 时间。

![图像](https://pbs.twimg.com/media/HBXOJxhbcAcSohR?format=png&name=large)

\---

## 六、搭建步骤

1. npm install -g openclaw && openclaw onboard
2. 去 [aigocode.com](https://aigocode.com/) 注册拿 API Key
3. 连接 Telegram bot
4. 告诉 AI 公众号 AppID 和 AppSecret
5. 说"帮我写篇文章发公众号"

![图像](https://pbs.twimg.com/media/HBXOKI9bcAcLeaj?format=png&name=large)

\---

## 七、资源

• OpenClaw 开源：[github.com/openclaw/openclaw](https://github.com/openclaw/openclaw)

• 中文社区：[t.me/claw101](https://t.me/claw101)

• AI 模型 API（国内直连）：[aigocode.com](https://aigocode.com/)

\---

最后更新：2026-02-13

\---

🆓 免费社区

Telegram 开放群，随时加入，有 AI 机器人答疑：

👉 [t.me/claw101](https://t.me/claw101)

🔥 付费交流群（¥49）

入群送 $50 Claude/Codex 算力额度（来自 [aigocode.com](https://aigocode.com/) 中转服务）。

不卷不卖课，一起玩转 AI Agent。配置踩坑、模型对比、效率玩法……扫码加入 👇

![图像](https://pbs.twimg.com/media/HBXOKglbcAUSYCS?format=jpg&name=large)

别等到拍大腿的时候，才想起今天看过这篇文章。

\---

📖 往期推荐

👉 我给自己配了8个AI员工，它们每天比我早起

👉 花3186元给AI员工买了台电脑