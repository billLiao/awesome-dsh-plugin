# Awesome DeepSeek Harness (DSH) Plugin


[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


> A categorized curated list of plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`).


DeepSeek Harness is DeepSeek's open-source agent harness — a runnable coding agent (Web and headless), built on a framework where everything is a plugin: models, tools, sandboxes, session storage, UI, even the agent loop itself.


**920 plugins** collected from GitHub topic [`dsh-plugin`](https://github.com/topics/dsh-plugin) · [PRs welcome](#contributing)


## Categories

| Category | Count | Description |

|----------|-------|-------------|

| 🎨 [UI Enhancements](categories/ui-enhancements.md) | 286 | Plugins that enhance the DSH web/terminal user interface. |

| 🎭 [Themes & Appearance](categories/themes-appearance.md) | 19 | Skins, themes, and appearance customization for DSH. |

| 💬 [Sessions & Messages](categories/sessions-messages.md) | 120 | Session management, message editing, sharing, and conversation tools. |

| 🧠 [Memory](categories/memory.md) | 25 | Persistent memory, knowledge bases, and context retention plugins. |

| 🛠️ [Tools & Capabilities](categories/tools-capabilities.md) | 257 | Vision, browser, terminal, SSH, Docker, and other capability extensions. |

| 🔁 [Workflow & Automation](categories/workflow-automation.md) | 143 | Automation loops, scheduled tasks, multi-agent teams, and workflow engines. |

| 🔔 [Notifications & Integrations](categories/notifications-integrations.md) | 3 | WeChat, Telegram, IM bridges, desktop notifications, and external integrations. |

| 🔌 [Models & Providers](categories/models-providers.md) | 7 | Multi-model support, OAuth login, LLM fallback strategies, and provider bridges. |

| 🧑‍💻 [Development & Runtime](categories/development-runtime.md) | 5 | Plugin managers, SDKs, CLIs, desktop wrappers, and developer tooling. |

| 🎮 [Just for Fun](categories/fun.md) | 1 | Games, pets, entertainment, and playful plugins. |

| 📋 [Awesome Lists & Collections](categories/awesome-lists.md) | 28 | Curated collections and awesome lists of DSH plugins. |


## Featured Plugins


A selection of notable plugins by category:


### 🎨 UI Enhancements

- [crafter-station/petdex](https://github.com/crafter-station/petdex) ⭐3767 — A public gallery of animated pets for Codex, Claude Code, DeepSeek Harness, Hermes, OpenCode, Gemini CLI, and more.
- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐723 — 解决DSH 官方尚无终端 TUI 痛点的补位之作，献给偏爱cli的各位极客：Claude Code 风格全屏交互终端插件——像素鲸鱼顶栏、实时工作状态行、思考流式展开、双击 Esc 回滚、上下文进度条 + TPS 仪表。npm 一键安装。
- [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐629 — 一个侧边栏的完整工作台，支持三方拓展注册新Tab页面，内置文件渲染编辑/终端/Git/子代理

▶️ [View all 286 plugins →](categories/ui-enhancements.md)


### 🎭 Themes & Appearance

- [Small-tailqwq/dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐457 — DSH Web 鲸鱼娘皮肤系列(深海女仆工坊 maid-atelier)——CC BY-NC-SA 4.0
- [147228/dsh-xiaoyao-skins](https://github.com/147228/dsh-xiaoyao-skins) ⭐16 — 夕小瑶 × DeepSeek Harness Web 皮肤合集、安装器与社区创作工具链
- [suzike/freestyle-dsh-theme](https://github.com/suzike/freestyle-dsh-theme) ⭐9 — DeepSeek Harness 主题体验插件：OKLCH 主题提案 + 主题设计器（跨重启持久化）

▶️ [View all 19 plugins →](categories/themes-appearance.md)


### 💬 Sessions & Messages

- [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) ⭐571 — Open-source CMA-compatible agent runtime for any model, with MCP tools, sandboxed sessions, audit, replay, and a local console. Includes a native DeepSeek Harness bundle over stdio MCP.
- [hikariming/dshfind](https://github.com/hikariming/dshfind) ⭐36 — DSH (DeepSeek Harness) 原理学习、插件市场与最佳实践 · Learn DSH principles, plugin marketplace & best practices
- [Anionex/dsh-turn-rewind](https://github.com/Anionex/dsh-turn-rewind) ⭐34 — deepseek harness对话和代码状态回退插件 | DSH — rewind conversation and workspace state, powered by a persistent Change Ledger

▶️ [View all 120 plugins →](categories/sessions-messages.md)


### 🧠 Memory

- [btspoony/mstar-harness](https://github.com/btspoony/mstar-harness) ⭐42 — A Skill-driven Harness/Loop Engineering Workflow Agent Plugin
- [omdsh-dev/dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) ⭐9 — Mnemon 与 DSH 的深度集成插件，为 DSH 提供完备的本地记忆系统：运行时记忆、可检索档案与受监督记忆体。
- [modusensus/dsh-mneme](https://github.com/modusensus/dsh-mneme) ⭐8 — Mneme——把记忆主权还给人的记忆插件：SQLite + 可人工编辑的 Markdown 双写，autoDream 在梦境中巩固记忆，140 个测试护航。

▶️ [View all 25 plugins →](categories/memory.md)


### 🛠️ Tools & Capabilities

- [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) ⭐3854 — A next-generation, source-available AI workspace with a self-evolving agent runtime for editable code, design, presentations, websites, and video—a Codex alternative that integrates DeepSeek Harness for subagent delegation, combining iPolloWork’s complete AI workbench with DSH’s specialized agents and both plugin ecosystems in one workflow.
- [liustack/modlens](https://github.com/liustack/modlens) ⭐1090 — The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics). | 全网第一个 DeepSeek Harness 视觉插件，为 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义）。
- [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) ⭐696 — 基于官方 DeepSeek Harness 打造的 Electron 桌面端，深度适配 macOS 和 Windows，提供最佳的，开箱即用的体验。

▶️ [View all 257 plugins →](categories/tools-capabilities.md)


### 🔁 Workflow & Automation

- [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2278 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）
- [yejiming/MuseAI](https://github.com/yejiming/MuseAI) ⭐535 — 创建你的 AI 角色，进入你的故事世界。和角色聊天、冒险、穿书，让每一次互动都留下羁绊（支持 DeepSeek Harness 插件，欢迎使用）
- [NanmiCoder/dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) ⭐210 — AgentTeams plugin for DeepSeek Harness

▶️ [View all 143 plugins →](categories/workflow-automation.md)


### 🔔 Notifications & Integrations

- [bill9109/dsh-webbridge](https://github.com/bill9109/dsh-webbridge) ⭐3 — DSH 结合 Kimi WebBridge
- [hellosz/dsh-ntfy](https://github.com/hellosz/dsh-ntfy)
- [zbxzbx98/dsh-peak-alert](https://github.com/zbxzbx98/dsh-peak-alert) — DeepSeek 峰谷定价提示插件（DSH Web 客户端插件，纯前端，无后端依赖）

▶️ [View all 3 plugins →](categories/notifications-integrations.md)


### 🔌 Models & Providers

- [HuanLinOTO/dsh-plugin-d399](https://github.com/HuanLinOTO/dsh-plugin-d399) ⭐4 — 模型生成时右下角弹出小游戏菜单（Wordle/消消乐/192 款参数化小游戏，可拓展注册表） | Pops up a mini-game menu while the model generates (Wordle/Match-3/192 parametric mini-games, extensible registry)
- [detpecca/dsh-llm-wiki](https://github.com/detpecca/dsh-llm-wiki) ⭐3
- [omdsh-dev/dsh-llm-fallbacks](https://github.com/omdsh-dev/dsh-llm-fallbacks) ⭐2 — An dsh plugin for role-based LLM retry&fallback strategy. 基于角色的模型重试备用策略插件

▶️ [View all 7 plugins →](categories/models-providers.md)


### 🧑‍💻 Development & Runtime

- [multica-ai/dsh-multica-runtime](https://github.com/multica-ai/dsh-multica-runtime) ⭐27 — Support dsh runtime on Multica.
- [ophielel/dsh-devkit](https://github.com/ophielel/dsh-devkit) ⭐1
- [Yummyxl/dsh-eyecare](https://github.com/Yummyxl/dsh-eyecare) ⭐1 — dsh护眼插件

▶️ [View all 5 plugins →](categories/development-runtime.md)


### 🎮 Just for Fun

- [HuanLinOTO/dsh-plugin-anti-ads](https://github.com/HuanLinOTO/dsh-plugin-anti-ads) ⭐3 — DSH Web 广告拦截器，四层独立防御拦截 dsh-ads 插件的所有广告位 | DSH Web ad blocker with four independent defense layers targeting the dsh-ads plugin

▶️ [View all 1 plugins →](categories/fun.md)


### 📋 Awesome Lists & Collections

- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐1554 — Plugin and skin collection for DeepSeek Harness (DSH) Web UI - task board, git graph, right-side panel, remote mobile UI, pet, live token stats, and skin center.
- [AdamPlatin123/awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐672 — 前部索引仓库（Radar）：自动扫描发现的所有 dsh 插件候选；经测试合格的将移入后序精选目录仓库
- [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐627 — A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

▶️ [View all 28 plugins →](categories/awesome-lists.md)


## Contributing


Found a plugin that should be here? Open a PR or issue!


1. Ensure your repo has the `dsh-plugin` topic on GitHub

2. The plugin should declare a `dsh.bundle` manifest

3. Submit a PR adding it to the appropriate category file


## License


[CC0 1.0 Universal](LICENSE)
