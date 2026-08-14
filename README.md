# Awesome DeepSeek Harness (DSH) Plugin


[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


> A categorized curated list of plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`).


DeepSeek Harness is DeepSeek's open-source agent harness — a runnable coding agent (Web and headless), built on a framework where everything is a plugin: models, tools, sandboxes, session storage, UI, even the agent loop itself.


**993 plugins** collected from GitHub topic [`dsh-plugin`](https://github.com/topics/dsh-plugin) · [PRs welcome](#contributing)


## Categories

| Category | Count | Description |

|----------|-------|-------------|

| 🎨 [UI Enhancements](categories/ui-enhancements.md) | 266 | Plugins that enhance the DSH web/terminal user interface. |

| 🎭 [Themes & Appearance](categories/themes-appearance.md) | 23 | Skins, themes, and appearance customization for DSH. |

| 💬 [Sessions & Messages](categories/sessions-messages.md) | 120 | Session management, message editing, sharing, and conversation tools. |

| 🧠 [Memory](categories/memory.md) | 22 | Persistent memory, knowledge bases, and context retention plugins. |

| 🛠️ [Tools & Capabilities](categories/tools-capabilities.md) | 255 | Vision, browser, terminal, SSH, Docker, and other capability extensions. |

| 🔁 [Workflow & Automation](categories/workflow-automation.md) | 148 | Automation loops, scheduled tasks, multi-agent teams, and workflow engines. |

| 🔔 [Notifications & Integrations](categories/notifications-integrations.md) | 2 | WeChat, Telegram, IM bridges, desktop notifications, and external integrations. |

| 🔌 [Models & Providers](categories/models-providers.md) | 3 | Multi-model support, OAuth login, LLM fallback strategies, and provider bridges. |

| 🧑‍💻 [Development & Runtime](categories/development-runtime.md) | 3 | Plugin managers, SDKs, CLIs, desktop wrappers, and developer tooling. |

| 🎮 [Just for Fun](categories/fun.md) | 2 | Games, pets, entertainment, and playful plugins. |

| 📋 [Awesome Lists & Collections](categories/awesome-lists.md) | 38 | Curated collections and awesome lists of DSH plugins. |

| ⚠️ [Weakly Related](categories/weakly-related.md) | 75 | Repositories tagged dsh-plugin but with weak relevance signals — may use DeepSeek API or have loose association. |


## Featured Plugins


A selection of notable plugins by category:


### 🎨 UI Enhancements

- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐894 — 解决DSH 官方尚无终端 TUI 痛点的补位之作，献给偏爱cli的各位极客：Claude Code 风格全屏交互终端插件——像素鲸鱼顶栏、实时工作状态行、思考流式展开、双击 Esc 回滚、上下文进度条 + TPS 仪表。npm 一键安装。
- [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐767 — 一个侧边栏的完整工作台，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/Git/子代理
- [Nagi-ovo/dsh-ads](https://github.com/Nagi-ovo/dsh-ads) ⭐336 — 把 DSH 变成 2005 年门户网站｜Parody ads, fake games, and popups for the DSH Web UI

▶️ [View all 266 plugins →](categories/ui-enhancements.md)


### 🎭 Themes & Appearance

- [Small-tailqwq/dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐595 — DSH Web 鲸鱼娘皮肤系列(深海女仆工坊 maid-atelier)——CC BY-NC-SA 4.0
- [linenxi-ctrl/dsh-vision](https://github.com/linenxi-ctrl/dsh-vision) ⭐10 — 为 DeepSeek Harness 增加外挂识图模型：圆形鲸鱼按钮、发送图片识图自动回传、模型自主截图+识图工具、多协议自动适配、小白一键安装（未装 Node.js 自动下载）
- [SenmuuuuW/dsh-whale-report](https://github.com/SenmuuuuW/dsh-whale-report) ⭐8 — 🐋 鲸鱼记事本 — 你的 Agent 年度报告：从会话事件日志生成日报/周报/月报/年报，任意区间、只读不改写

▶️ [View all 23 plugins →](categories/themes-appearance.md)


### 💬 Sessions & Messages

- [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) ⭐574 — Open-source CMA-compatible agent runtime for any model, with MCP tools, sandboxed sessions, audit, replay, and a local console. Includes a native DeepSeek Harness bundle over stdio MCP.
- [hikariming/dshfind](https://github.com/hikariming/dshfind) ⭐61 — DSH (DeepSeek Harness) 原理学习、插件市场与最佳实践 · Learn DSH principles, plugin marketplace & best practices
- [csyangwen/dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) ⭐58 — 为 DeepSeek Harness 带来「跨会话长期记忆 + 后台自我进化」能力的纯插件实现：五轨记忆 · git 分支感知 · 回合内自我审查 · 技能自我进化与技能管理器 · 四轨待办 · COI 调度 · 会话广播 · 会话搜索 · 提示词管理器 · 临时信息便签——零核心修改、零运行时依赖，随装随用、卸载即净。

▶️ [View all 120 plugins →](categories/sessions-messages.md)


### 🧠 Memory

- [modusensus/dsh-mneme](https://github.com/modusensus/dsh-mneme) ⭐8 — Mneme——把记忆主权还给人的记忆插件：SQLite + 可人工编辑的 Markdown 双写，autoDream 在梦境中巩固记忆，140 个测试护航。
- [xylt369/dsh-browser](https://github.com/xylt369/dsh-browser) ⭐3 — Browser capability for DeepSeek Harness: headed Edge/Playwright provider, SSRF-safe navigation, a11y-ref clicking, permission gate with auto-remember, gated evaluate
- [Zephyr-vibe/dsh-personalize](https://github.com/Zephyr-vibe/dsh-personalize) ⭐3 — Per-host personalization for DSH: custom instructions, local long-term memory, and reply-tone presets.

▶️ [View all 22 plugins →](categories/memory.md)


### 🛠️ Tools & Capabilities

- [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) ⭐1798 — 为 DeepSeek Harness (DSH) 生态打造的现代化桌面端体验
- [liustack/modlens](https://github.com/liustack/modlens) ⭐1291 — The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics). | 全网第一个 DeepSeek Harness 视觉插件，为 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义）。
- [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) ⭐326 — Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99)

▶️ [View all 255 plugins →](categories/tools-capabilities.md)


### 🔁 Workflow & Automation

- [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2367 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）
- [NanmiCoder/dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) ⭐247 — AgentTeams plugin for DeepSeek Harness
- [dsh-market/dsh-market](https://github.com/dsh-market/dsh-market) ⭐58 — The plugin market inside DeepSeek Harness — browse, search, one-click install · DSH 可视化插件市场

▶️ [View all 148 plugins →](categories/workflow-automation.md)


### 🔔 Notifications & Integrations

- [TerricSH/dsh-notify](https://github.com/TerricSH/dsh-notify) ⭐1
- [Hyna-hla/dsh-vscode](https://github.com/Hyna-hla/dsh-vscode)

▶️ [View all 2 plugins →](categories/notifications-integrations.md)


### 🔌 Models & Providers

- [detpecca/dsh-llm-wiki](https://github.com/detpecca/dsh-llm-wiki) ⭐4
- [omdsh-dev/dsh-llm-fallbacks](https://github.com/omdsh-dev/dsh-llm-fallbacks) ⭐3 — An dsh plugin for role-based LLM retry&fallback strategy. 基于角色的模型重试备用策略插件
- [kingsunb/dsh-model-plus](https://github.com/kingsunb/dsh-model-plus)

▶️ [View all 3 plugins →](categories/models-providers.md)


### 🧑‍💻 Development & Runtime

- [monk233/dsh-plugin-manager](https://github.com/monk233/dsh-plugin-manager) ⭐2 — DSH 插件管理, 一键启用/禁用插件
- [xbzbing/dsh-password-gate](https://github.com/xbzbing/dsh-password-gate) ⭐1 — 远程访问开发机使用，这只是一个 dsh 插件的 demo，安全功能只有最简单的频次兜底，切勿直接开放在外网。
- [zdjmrq/dsh-restart-plugin](https://github.com/zdjmrq/dsh-restart-plugin) — DSH web plugin: one-click backend shutdown & frontend refresh that keeps creation-mode hot plugins

▶️ [View all 3 plugins →](categories/development-runtime.md)


### 🎮 Just for Fun

- [Lanxing6480/dsh-galgame](https://github.com/Lanxing6480/dsh-galgame) ⭐2 — 我要成为Galgame高手！！将你的Vibe coding界面修改成为Galgame的样子，在不影响工作的情况下和赏心悦目的DeepSeek娘进行友好互动
- [chu557/douyin-plugin-dsh-plugin](https://github.com/chu557/douyin-plugin-dsh-plugin) ⭐2 — 在使用dsh等待的过程中刷抖音

▶️ [View all 2 plugins →](categories/fun.md)


### 📋 Awesome Lists & Collections

- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐1933 — Plugin and skin collection for DeepSeek Harness (DSH) Web UI - task board, git graph, right-side panel, remote mobile UI, pet, live token stats, and skin center.
- [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐1085 — A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表
- [AdamPlatin123/awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐825 — 前部索引仓库（Radar）：自动扫描发现的所有 dsh 插件候选；经测试合格的将移入后序精选目录仓库

▶️ [View all 38 plugins →](categories/awesome-lists.md)


### ⚠️ Weakly Related


75 repositories tagged `dsh-plugin` but with low relevance confidence.


▶️ [View all 75 repos →](categories/weakly-related.md)


## Contributing


Found a plugin that should be here? Open a PR or issue!


1. Ensure your repo has the `dsh-plugin` topic on GitHub

2. The plugin should declare a `dsh.bundle` manifest

3. Submit a PR adding it to the appropriate category file


## License


[CC0 1.0 Universal](LICENSE)
