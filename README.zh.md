# Awesome DeepSeek Harness (DSH) Plugin


[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


> [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）插件分类精选列表。


DeepSeek Harness 是 DeepSeek 开源的 agent harness——既是可直接运行的 Coding Agent，底层又是一套「一切皆插件」的框架。


**1102 个插件**，来自 GitHub 话题 [`dsh-plugin`](https://github.com/topics/dsh-plugin) · 欢迎 [PR](#贡献)


## 分类

| 分类 | 数量 | 说明 |

|------|------|------|

| 🎨 [UI 增强](categories/ui-enhancements.md) | 298 | 增强 DSH Web/终端用户界面的插件。 |

| 🎭 [主题与外观](categories/themes-appearance.md) | 22 | DSH 皮肤、主题与外观定制。 |

| 💬 [会话与消息](categories/sessions-messages.md) | 135 | 会话管理、消息编辑、分享与对话工具。 |

| 🧠 [记忆](categories/memory.md) | 30 | 持久记忆、知识库与上下文保留插件。 |

| 🛠️ [工具与能力](categories/tools-capabilities.md) | 296 | 视觉、浏览器、终端、SSH、Docker 等能力扩展。 |

| 🔁 [工作流与自动化](categories/workflow-automation.md) | 154 | 自动化循环、定时任务、多智能体团队与工作流引擎。 |

| 🔔 [通知与集成](categories/notifications-integrations.md) | 2 | 微信、Telegram、IM 桥接、桌面通知与外部集成。 |

| 🔌 [模型与账号接入](categories/models-providers.md) | 2 | 多模型支持、OAuth 登录、LLM 回退策略与提供商桥接。 |

| 🧑‍💻 [开发与运行时](categories/development-runtime.md) | 4 | 插件管理器、SDK、CLI、桌面壳与开发者工具。 |

| 🎮 [娱乐](categories/fun.md) | 3 | 游戏、桌宠、娱乐与趣味插件。 |

| 📋 [精选列表与合集](categories/awesome-lists.md) | 53 | DSH 插件精选列表与合集。 |

| ⚠️ [弱相关](categories/weakly-related.md) | 61 | 标记了 dsh-plugin 但关联性较弱的仓库——可能只是使用了 DeepSeek API 或关联松散。 |


## 精选插件


### 🎨 UI 增强

- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐1290 — DSH 官方公众号收录的 TUI 补位插件：Claude Code 风，鲸鱼顶栏/实时状态/流式思考/双击 Esc 回滚/上下文进度+TPS。npm 一键装。  DSH official WeChat featured TUI plugin — Claude Code style: whale bar, live status, streaming thoughts, double-Esc rollback, context bar + TPS. npm one-click.
- [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐1272 — 一个侧边栏的完整工作台，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/Git/子代理
- [Anionex/dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) ⭐439 — 让纯文本模型更好地做视觉任务的DeepSeek Harness插件：带意图的图片问答、长截图 OCR、UI 还原等｜DeepSeek Harness-native integration for agent-vision-toolkit: image Q&A, long-screenshot OCR, UI restoration, grounding, pixel diff, Artifacts, and Web UI.

▶️ [查看全部 298 个插件 →](categories/ui-enhancements.md)


### 🎭 主题与外观

- [SenmuuuuW/dsh-whale-report](https://github.com/SenmuuuuW/dsh-whale-report) ⭐14 — 🐋 鲸鱼记事本 — 你的 Agent 年度报告：从会话事件日志生成日报/周报/月报/年报，任意区间、只读不改写
- [Mochabafey/whale-notify](https://github.com/Mochabafey/whale-notify) ⭐4 — 鲸鱼通知——基于DeepSeek Harness的通知和鲸鱼娘人设插件
- [rongzi5/dsh-whale-pet](https://github.com/rongzi5/dsh-whale-pet) ⭐4

▶️ [查看全部 22 个插件 →](categories/themes-appearance.md)


### 💬 会话与消息

- [hikariming/dshfind](https://github.com/hikariming/dshfind) ⭐86 — DSH (DeepSeek Harness) 原理学习、插件市场与最佳实践 · Learn DSH principles, plugin marketplace & best practices
- [Ayase34/gal-view](https://github.com/Ayase34/gal-view) ⭐53 — 把dsh会话界面切换成galgame游戏界面的插件
- [Nwflower/dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) ⭐35 — 从Claude Code、Codex、Reasonix等Agent工具导入迁移历史消息，并在DeepSeek Harness(DSH)中继续对话

▶️ [查看全部 135 个插件 →](categories/sessions-messages.md)


### 🧠 记忆

- [bowenliang123/dsh-context](https://github.com/bowenliang123/dsh-context) ⭐42 — A DeepSeek Harness plugin for  Context insight dashboard — showing what the model's context window is made of and how it evolves.
- [btspoony/mstar-harness](https://github.com/btspoony/mstar-harness) ⭐45 — A Skill-driven Harness/Loop Engineering Workflow Agent Plugin
- [knqiufan/powercontext-dsh](https://github.com/knqiufan/powercontext-dsh) ⭐10 — DeepSeek Harness plugin that connects to a PowerContext Server over HTTP for recall, memory, handoff, experience, and skills.
- [nowledge-co/nowledge-mem-deepseek-harness](https://github.com/nowledge-co/nowledge-mem-deepseek-harness) ⭐5 — One memory layer for every AI tool and agent, packaged for DeepSeek Harness

▶️ [查看全部 30 个插件 →](categories/memory.md)


### 🛠️ 工具与能力

- [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) ⭐6163 — 为 DeepSeek Harness (DSH) 生态打造的现代化桌面端体验
- [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) ⭐4088 — A next-generation, source-available AI workspace with a self-evolving agent runtime for editable code, design, presentations, websites, and video—a Codex alternative that integrates DeepSeek Harness for subagent delegation, combining iPolloWork’s complete AI workbench with DSH’s specialized agents and both plugin ecosystems in one workflow.
- [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) ⭐2253 — Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99)

▶️ [查看全部 296 个插件 →](categories/tools-capabilities.md)


### 🔁 工作流与自动化

- [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2583 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）
- [dsh-market/dsh-market](https://github.com/dsh-market/dsh-market) ⭐298 — The plugin market inside DeepSeek Harness — browse, search, one-click install · DSH 可视化插件市场

▶️ [查看全部 154 个插件 →](categories/workflow-automation.md)


### 🔔 通知与集成

- [gameswu/dsh-notifacation-frame](https://github.com/gameswu/dsh-notifacation-frame) ⭐1 — dsh通知消息统一管理框架
- [thuang3316/dsh-live-notify](https://github.com/thuang3316/dsh-live-notify) ⭐1 — DSH plugin for live notification

▶️ [查看全部 2 个插件 →](categories/notifications-integrations.md)


### 🔌 模型与账号接入

- [HB00/dsh-llm-failover](https://github.com/HB00/dsh-llm-failover) — dsh-llm-failover
- [kingsunb/dsh-model-plus](https://github.com/kingsunb/dsh-model-plus)

▶️ [查看全部 2 个插件 →](categories/models-providers.md)


### 🧑‍💻 开发与运行时

- [wzxaaaa/dsh-w-plugin-ecosystem](https://github.com/wzxaaaa/dsh-w-plugin-ecosystem) ⭐2 — 为dsh专属打造的贴近原生的自定义插件生态，支持插件可配置，独立协议，热拔插
- [2128627267/dsh-qbetter-config](https://github.com/2128627267/dsh-qbetter-config) ⭐1
- [omdsh-dev/dsh-sandbox-micro](https://github.com/omdsh-dev/dsh-sandbox-micro) ⭐1

▶️ [查看全部 4 个插件 →](categories/development-runtime.md)


### 🎮 娱乐

- [gameswu/dsh-pref-kit](https://github.com/gameswu/dsh-pref-kit) ⭐1 — 缓解部分dsh性能问题的插件
- [pk7j7sqryy-ops/dsh-token-pet](https://github.com/pk7j7sqryy-ops/dsh-token-pet) ⭐1 — DSH 动态 Cordis 插件：卡通用量小部件 + 天气/预报/预警（Token Pet 布布玩偶）
- [gxx950224/ggame](https://github.com/gxx950224/ggame) — dsh ggame plugin

▶️ [查看全部 3 个插件 →](categories/fun.md)


### 📋 精选列表与合集

- [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐3092 — A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表
- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐2764 — Plugin and skin collection for DeepSeek Harness (DSH) Web UI - task board, git graph, right-side panel, remote mobile UI, pet, live token stats, and skin center.
- [AdamPlatin123/awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐975 — 前部索引仓库（Radar）：自动扫描发现的所有 dsh 插件候选；经测试合格的将移入后序精选目录仓库

▶️ [查看全部 53 个插件 →](categories/awesome-lists.md)


### ⚠️ 弱相关


61 个标记了 `dsh-plugin` 但关联性较低的仓库。


▶️ [查看全部 61 个仓库 →](categories/weakly-related.md)


## 贡献


发现了一个应该收录的插件？欢迎提交 PR 或 Issue！


1. 确保你的仓库有 `dsh-plugin` 话题标签

2. 插件应声明 `dsh.bundle` manifest

3. 提交 PR 将插件添加到对应分类文件


## 许可


[CC0 1.0 Universal](LICENSE)
