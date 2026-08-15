# Awesome DeepSeek Harness (DSH) Plugin


[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


> [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）插件分类精选列表。


DeepSeek Harness 是 DeepSeek 开源的 agent harness——既是可直接运行的 Coding Agent，底层又是一套「一切皆插件」的框架。


**993 个插件**，来自 GitHub 话题 [`dsh-plugin`](https://github.com/topics/dsh-plugin) · 欢迎 [PR](#贡献)


## 分类

| 分类 | 数量 | 说明 |

|------|------|------|

| 🎨 [UI 增强](categories/ui-enhancements.md) | 281 | 增强 DSH Web/终端用户界面的插件。 |

| 🎭 [主题与外观](categories/themes-appearance.md) | 23 | DSH 皮肤、主题与外观定制。 |

| 💬 [会话与消息](categories/sessions-messages.md) | 120 | 会话管理、消息编辑、分享与对话工具。 |

| 🧠 [记忆](categories/memory.md) | 17 | 持久记忆、知识库与上下文保留插件。 |

| 🛠️ [工具与能力](categories/tools-capabilities.md) | 249 | 视觉、浏览器、终端、SSH、Docker 等能力扩展。 |

| 🔁 [工作流与自动化](categories/workflow-automation.md) | 141 | 自动化循环、定时任务、多智能体团队与工作流引擎。 |

| 🔔 [通知与集成](categories/notifications-integrations.md) | 2 | 微信、Telegram、IM 桥接、桌面通知与外部集成。 |

| 🔌 [模型与账号接入](categories/models-providers.md) | 3 | 多模型支持、OAuth 登录、LLM 回退策略与提供商桥接。 |

| 🧑‍💻 [开发与运行时](categories/development-runtime.md) | 4 | 插件管理器、SDK、CLI、桌面壳与开发者工具。 |

| 🎮 [娱乐](categories/fun.md) | 2 | 游戏、桌宠、娱乐与趣味插件。 |

| 📋 [精选列表与合集](categories/awesome-lists.md) | 43 | DSH 插件精选列表与合集。 |

| ⚠️ [弱相关](categories/weakly-related.md) | 70 | 标记了 dsh-plugin 但关联性较弱的仓库——可能只是使用了 DeepSeek API 或关联松散。 |


## 精选插件


### 🎨 UI 增强

- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐944 — 解决DSH 官方尚无终端 TUI 痛点的补位之作，献给偏爱cli的各位极客：Claude Code 风格全屏交互终端插件——像素鲸鱼顶栏、实时工作状态行、思考流式展开、双击 Esc 回滚、上下文进度条 + TPS 仪表。npm 一键安装。
- [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐823 — 一个侧边栏的完整工作台，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/Git/子代理
- [Nagi-ovo/dsh-ads](https://github.com/Nagi-ovo/dsh-ads) ⭐354 — 把 DSH 变成 2005 年门户网站｜Parody ads, fake games, and popups for the DSH Web UI

▶️ [查看全部 281 个插件 →](categories/ui-enhancements.md)


### 🎭 主题与外观

- [Small-tailqwq/dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐638 — DSH Web 鲸鱼娘皮肤系列(深海女仆工坊 maid-atelier)——CC BY-NC-SA 4.0
- [SenmuuuuW/dsh-whale-report](https://github.com/SenmuuuuW/dsh-whale-report) ⭐9 — 🐋 鲸鱼记事本 — 你的 Agent 年度报告：从会话事件日志生成日报/周报/月报/年报，任意区间、只读不改写
- [nevertoday/dsh-theme-plugin](https://github.com/nevertoday/dsh-theme-plugin) ⭐3

▶️ [查看全部 23 个插件 →](categories/themes-appearance.md)


### 💬 会话与消息

- [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) ⭐576 — Open-source CMA-compatible agent runtime for any model, with MCP tools, sandboxed sessions, audit, replay, and a local console. Includes a native DeepSeek Harness bundle over stdio MCP.
- [hikariming/dshfind](https://github.com/hikariming/dshfind) ⭐65 — DSH (DeepSeek Harness) 原理学习、插件市场与最佳实践 · Learn DSH principles, plugin marketplace & best practices
- [whiteguo233/dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) ⭐24 — OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。

▶️ [查看全部 120 个插件 →](categories/sessions-messages.md)


### 🧠 记忆

- [btspoony/mstar-harness](https://github.com/btspoony/mstar-harness) ⭐43 — A Skill-driven Harness/Loop Engineering Workflow Agent Plugin
- [xylt369/dsh-browser](https://github.com/xylt369/dsh-browser) ⭐4 — Browser capability for DeepSeek Harness: headed Edge/Playwright provider, SSRF-safe navigation, a11y-ref clicking, permission gate with auto-remember, gated evaluate
- [limbo947/DSH-recall-plugin](https://github.com/limbo947/DSH-recall-plugin) ⭐3 — DSH 消息撤回插件：回到发送该消息时的状态

▶️ [查看全部 17 个插件 →](categories/memory.md)


### 🛠️ 工具与能力

- [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) ⭐2483 — 为 DeepSeek Harness (DSH) 生态打造的现代化桌面端体验
- [liustack/modlens](https://github.com/liustack/modlens) ⭐1376 — The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics). | 全网第一个 DeepSeek Harness 视觉插件，为 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义）。
- [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) ⭐694 — Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99)

▶️ [查看全部 249 个插件 →](categories/tools-capabilities.md)


### 🔁 工作流与自动化

- [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2406 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）
- [NanmiCoder/dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) ⭐259 — AgentTeams plugin for DeepSeek Harness
- [dsh-market/dsh-market](https://github.com/dsh-market/dsh-market) ⭐91 — The plugin market inside DeepSeek Harness — browse, search, one-click install · DSH 可视化插件市场

▶️ [查看全部 141 个插件 →](categories/workflow-automation.md)


### 🔔 通知与集成

- [TerricSH/dsh-notify](https://github.com/TerricSH/dsh-notify) ⭐1
- [Hyna-hla/dsh-vscode](https://github.com/Hyna-hla/dsh-vscode)

▶️ [查看全部 2 个插件 →](categories/notifications-integrations.md)


### 🔌 模型与账号接入

- [omdsh-dev/dsh-llm-fallbacks](https://github.com/omdsh-dev/dsh-llm-fallbacks) ⭐3 — An dsh plugin for role-based LLM retry&fallback strategy. 基于角色的模型重试备用策略插件
- [eons2long/dsh-codex-oauth](https://github.com/eons2long/dsh-codex-oauth) ⭐1
- [kingsunb/dsh-model-plus](https://github.com/kingsunb/dsh-model-plus)

▶️ [查看全部 3 个插件 →](categories/models-providers.md)


### 🧑‍💻 开发与运行时

- [monk233/dsh-plugin-manager](https://github.com/monk233/dsh-plugin-manager) ⭐3 — DSH 插件管理, 一键启用/禁用插件
- [wzxaaaa/dsh-w-plugin-ecosystem](https://github.com/wzxaaaa/dsh-w-plugin-ecosystem) ⭐2 — 为dsh专属打造的贴近原生的自定义插件生态，支持插件可配置，独立协议，热拔插
- [xbzbing/dsh-password-gate](https://github.com/xbzbing/dsh-password-gate) ⭐2 — 远程访问开发机使用，这只是一个 dsh 插件的 demo，安全功能只有最简单的频次兜底，切勿直接开放在外网。

▶️ [查看全部 4 个插件 →](categories/development-runtime.md)


### 🎮 娱乐

- [Lanxing6480/dsh-galgame](https://github.com/Lanxing6480/dsh-galgame) ⭐3 — 我要成为Galgame高手！！将你的Vibe coding界面修改成为Galgame的样子，在不影响工作的情况下和赏心悦目的DeepSeek娘进行友好互动
- [chu557/douyin-plugin-dsh-plugin](https://github.com/chu557/douyin-plugin-dsh-plugin) ⭐3 — 在使用dsh等待的过程中刷抖音

▶️ [查看全部 2 个插件 →](categories/fun.md)


### 📋 精选列表与合集

- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐2043 — Plugin and skin collection for DeepSeek Harness (DSH) Web UI - task board, git graph, right-side panel, remote mobile UI, pet, live token stats, and skin center.
- [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐1375 — A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表
- [AdamPlatin123/awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐860 — 前部索引仓库（Radar）：自动扫描发现的所有 dsh 插件候选；经测试合格的将移入后序精选目录仓库

▶️ [查看全部 43 个插件 →](categories/awesome-lists.md)


### ⚠️ 弱相关


70 个标记了 `dsh-plugin` 但关联性较低的仓库。


▶️ [查看全部 70 个仓库 →](categories/weakly-related.md)


## 贡献


发现了一个应该收录的插件？欢迎提交 PR 或 Issue！


1. 确保你的仓库有 `dsh-plugin` 话题标签

2. 插件应声明 `dsh.bundle` manifest

3. 提交 PR 将插件添加到对应分类文件


## 许可


[CC0 1.0 Universal](LICENSE)
