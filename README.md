# Awesome DeepSeek Harness (DSH) Plugin


[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


> A categorized curated list of plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`).


DeepSeek Harness is DeepSeek's open-source agent harness — a runnable coding agent (Web and headless), built on a framework where everything is a plugin: models, tools, sandboxes, session storage, UI, even the agent loop itself.


**996 plugins** collected from GitHub topic [`dsh-plugin`](https://github.com/topics/dsh-plugin) · [PRs welcome](#contributing)


## Categories

| Category | Count | Description |

|----------|-------|-------------|

| 🎨 [UI Enhancements](categories/ui-enhancements.md) | 278 | Plugins that enhance the DSH web/terminal user interface. |

| 🎭 [Themes & Appearance](categories/themes-appearance.md) | 21 | Skins, themes, and appearance customization for DSH. |

| 💬 [Sessions & Messages](categories/sessions-messages.md) | 117 | Session management, message editing, sharing, and conversation tools. |

| 🧠 [Memory](categories/memory.md) | 22 | Persistent memory, knowledge bases, and context retention plugins. |

| 🛠️ [Tools & Capabilities](categories/tools-capabilities.md) | 271 | Vision, browser, terminal, SSH, Docker, and other capability extensions. |

| 🔁 [Workflow & Automation](categories/workflow-automation.md) | 146 | Automation loops, scheduled tasks, multi-agent teams, and workflow engines. |

| 🔔 [Notifications & Integrations](categories/notifications-integrations.md) | 1 | WeChat, Telegram, IM bridges, desktop notifications, and external integrations. |

| 🔌 [Models & Providers](categories/models-providers.md) | 4 | Multi-model support, OAuth login, LLM fallback strategies, and provider bridges. |

| 🧑‍💻 [Development & Runtime](categories/development-runtime.md) | 4 | Plugin managers, SDKs, CLIs, desktop wrappers, and developer tooling. |

| 🎮 [Just for Fun](categories/fun.md) | 2 | Games, pets, entertainment, and playful plugins. |

| 📋 [Awesome Lists & Collections](categories/awesome-lists.md) | 46 | Curated collections and awesome lists of DSH plugins. |

| ⚠️ [Weakly Related](categories/weakly-related.md) | 44 | Repositories tagged dsh-plugin but with weak relevance signals — may use DeepSeek API or have loose association. |


## Featured Plugins


A selection of notable plugins by category:


### 🎨 UI Enhancements

- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐1247 — 解决DSH 官方尚无终端 TUI 痛点的补位之作，献给偏爱cli的各位极客：Claude Code 风格全屏交互终端插件——像素鲸鱼顶栏、实时工作状态行、思考流式展开、双击 Esc 回滚、上下文进度条 + TPS 仪表。npm 一键安装。
- [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐1242 — 一个侧边栏的完整工作台，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/Git/子代理
- [Anionex/dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) ⭐429 — 让纯文本模型更好地做视觉任务的DeepSeek Harness插件：带意图的图片问答、长截图 OCR、UI 还原等｜DeepSeek Harness-native integration for agent-vision-toolkit: image Q&A, long-screenshot OCR, UI restoration, grounding, pixel diff, Artifacts, and Web UI.

▶️ [View all 278 plugins →](categories/ui-enhancements.md)


### 🎭 Themes & Appearance

- [SenmuuuuW/dsh-whale-report](https://github.com/SenmuuuuW/dsh-whale-report) ⭐14 — 🐋 鲸鱼记事本 — 你的 Agent 年度报告：从会话事件日志生成日报/周报/月报/年报，任意区间、只读不改写
- [linenxi-ctrl/dsh-vision](https://github.com/linenxi-ctrl/dsh-vision) ⭐11 — 为 DeepSeek Harness 增加外挂识图模型：圆形鲸鱼按钮、发送图片识图自动回传、模型自主截图+识图工具、多协议自动适配、小白一键安装（未装 Node.js 自动下载）
- [zhijun-dai/Catppuccin-dsh-theme](https://github.com/zhijun-dai/Catppuccin-dsh-theme) ⭐6 — 🐱 Soothing pastel theme for DeepSeek Harness

▶️ [View all 21 plugins →](categories/themes-appearance.md)


### 💬 Sessions & Messages

- [hikariming/dshfind](https://github.com/hikariming/dshfind) ⭐84 — DSH (DeepSeek Harness) 原理学习、插件市场与最佳实践 · Learn DSH principles, plugin marketplace & best practices
- [Nwflower/dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) ⭐35 — 从Claude Code、Codex、Reasonix等Agent工具导入迁移历史消息，并在DeepSeek Harness(DSH)中继续对话
- [omdsh-dev/dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) ⭐27 — Data Agent for DeepSeek Harness: session-scoped database connections with a dedicated agent preset that lets AI write SQL and iterate against live execution feedback.

▶️ [View all 117 plugins →](categories/sessions-messages.md)


### 🧠 Memory

- [IAMLieutenant/dsh-tool-user-memory](https://github.com/IAMLieutenant/dsh-tool-user-memory) ⭐3 — DeepSeek Harness 用户记忆插件
- [fan969690/dsh-desktop-tools](https://github.com/fan969690/dsh-desktop-tools) ⭐3 — DeepSeek Harness 工具集导航:Web 插件集(dsh-web-plugins)/ Windows 桌面端(dsh-desktop-app)/ AI 知识库模板(ai-knowledge-base)
- [cwbcheng/dsh-knowledge-graph](https://github.com/cwbcheng/dsh-knowledge-graph) ⭐2 — DSH Cordis plugin: turn any source text into an AI knowledge graph (facts/inferences/concepts/definitions/examples/counter-examples/rules) with two-way linking between the graph and the original text.

▶️ [View all 22 plugins →](categories/memory.md)


### 🛠️ Tools & Capabilities

- [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) ⭐5670 — 为 DeepSeek Harness (DSH) 生态打造的现代化桌面端体验
- [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) ⭐4122 — A next-generation, source-available AI workspace with a self-evolving agent runtime for editable code, design, presentations, websites, and video—a Codex alternative that integrates DeepSeek Harness for subagent delegation, combining iPolloWork’s complete AI workbench with DSH’s specialized agents and both plugin ecosystems in one workflow.
- [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) ⭐2128 — Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99)

▶️ [View all 271 plugins →](categories/tools-capabilities.md)


### 🔁 Workflow & Automation

- [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2550 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）
- [NanmiCoder/dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) ⭐332 — AgentTeams plugin for DeepSeek Harness
- [dsh-market/dsh-market](https://github.com/dsh-market/dsh-market) ⭐279 — The plugin market inside DeepSeek Harness — browse, search, one-click install · DSH 可视化插件市场

▶️ [View all 146 plugins →](categories/workflow-automation.md)


### 🔔 Notifications & Integrations

- [thuang3316/dsh-live-notify](https://github.com/thuang3316/dsh-live-notify) ⭐1 — DSH plugin for live notification

▶️ [View all 1 plugins →](categories/notifications-integrations.md)


### 🔌 Models & Providers

- [omdsh-dev/dsh-llm-fallbacks](https://github.com/omdsh-dev/dsh-llm-fallbacks) ⭐5 — An dsh plugin for role-based LLM retry&fallback strategy. 基于角色的模型重试备用策略插件
- [HB00/dsh-llm-failover](https://github.com/HB00/dsh-llm-failover) — dsh-llm-failover
- [kingsunb/dsh-model-plus](https://github.com/kingsunb/dsh-model-plus)

▶️ [View all 4 plugins →](categories/models-providers.md)


### 🧑‍💻 Development & Runtime

- [YEYEYEYESHIFU/dsh-result-only-view](https://github.com/YEYEYEYESHIFU/dsh-result-only-view) ⭐1
- [ophielel/dsh-devkit](https://github.com/ophielel/dsh-devkit) ⭐1
- [2128627267/dsh-qbetter-config](https://github.com/2128627267/dsh-qbetter-config) ⭐1

▶️ [View all 4 plugins →](categories/development-runtime.md)


### 🎮 Just for Fun

- [pk7j7sqryy-ops/dsh-token-pet](https://github.com/pk7j7sqryy-ops/dsh-token-pet) ⭐1 — DSH 动态 Cordis 插件：卡通用量小部件 + 天气/预报/预警（Token Pet 布布玩偶）
- [gxx950224/ggame](https://github.com/gxx950224/ggame) — dsh ggame plugin

▶️ [View all 2 plugins →](categories/fun.md)


### 📋 Awesome Lists & Collections

- [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐2927 — A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表
- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐2674 — Plugin and skin collection for DeepSeek Harness (DSH) Web UI - task board, git graph, right-side panel, remote mobile UI, pet, live token stats, and skin center.
- [AdamPlatin123/awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐967 — 前部索引仓库（Radar）：自动扫描发现的所有 dsh 插件候选；经测试合格的将移入后序精选目录仓库

▶️ [View all 46 plugins →](categories/awesome-lists.md)


### ⚠️ Weakly Related


44 repositories tagged `dsh-plugin` but with low relevance confidence.


▶️ [View all 44 repos →](categories/weakly-related.md)


## Contributing


Found a plugin that should be here? Open a PR or issue!


1. Ensure your repo has the `dsh-plugin` topic on GitHub

2. The plugin should declare a `dsh.bundle` manifest

3. Submit a PR adding it to the appropriate category file


## License


[CC0 1.0 Universal](LICENSE)
