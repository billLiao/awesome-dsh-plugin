# Awesome DeepSeek Harness (DSH) Plugin


[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


> A categorized curated list of plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`).


DeepSeek Harness is DeepSeek's open-source agent harness — a runnable coding agent (Web and headless), built on a framework where everything is a plugin: models, tools, sandboxes, session storage, UI, even the agent loop itself.


**6549 plugins** collected from GitHub topic [`dsh-plugin`](https://github.com/topics/dsh-plugin) · [PRs welcome](#contributing)


## Categories

| Category | Count | Description |

|----------|-------|-------------|

| 🎨 [UI Enhancements](categories/ui-enhancements.md) | 1688 | Plugins that enhance the DSH web/terminal user interface. |

| 🎭 [Themes & Appearance](categories/themes-appearance.md) | 137 | Skins, themes, and appearance customization for DSH. |

| 💬 [Sessions & Messages](categories/sessions-messages.md) | 797 | Session management, message editing, sharing, and conversation tools. |

| 🧠 [Memory](categories/memory.md) | 154 | Persistent memory, knowledge bases, and context retention plugins. |

| 🛠️ [Tools & Capabilities](categories/tools-capabilities.md) | 1656 | Vision, browser, terminal, SSH, Docker, and other capability extensions. |

| 🔁 [Workflow & Automation](categories/workflow-automation.md) | 1303 | Automation loops, scheduled tasks, multi-agent teams, and workflow engines. |

| 🔔 [Notifications & Integrations](categories/notifications-integrations.md) | 10 | WeChat, Telegram, IM bridges, desktop notifications, and external integrations. |

| 🔌 [Models & Providers](categories/models-providers.md) | 27 | Multi-model support, OAuth login, LLM fallback strategies, and provider bridges. |

| 🧑‍💻 [Development & Runtime](categories/development-runtime.md) | 26 | Plugin managers, SDKs, CLIs, desktop wrappers, and developer tooling. |

| 🔒 [Security & Privacy](categories/security-privacy.md) | 2 | Credential management, encryption, audit, and security tooling. |

| 🎮 [Just for Fun](categories/fun.md) | 6 | Games, pets, entertainment, and playful plugins. |

| 📋 [Awesome Lists & Collections](categories/awesome-lists.md) | 160 | Curated collections and awesome lists of DSH plugins. |

| ⚠️ [Weakly Related](categories/weakly-related.md) | 362 | Repositories tagged dsh-plugin but with weak relevance signals — may use DeepSeek API or have loose association. |


## Featured Plugins


A selection of notable plugins by category:


### 🎨 UI Enhancements

- [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) ⭐34916 — DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.
- [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐2430 — 开放的侧边栏底座，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/Git/子代理页面 ｜ Open sidebar foundation, supports third-party extensions to register new sidebar pages. Built-in file rendering/editing, terminal, Git, and sub-agent pages.
- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐2152 — DSH 官方公众号收录的 TUI 补位插件：Claude Code 风，鲸鱼顶栏/实时状态/流式思考/双击 Esc 回滚/上下文进度+TPS。npm 一键装。  DSH official WeChat featured TUI plugin — Claude Code style: whale bar, live status, streaming thoughts, double-Esc rollback, context bar + TPS. npm one-click.

▶️ [View all 1688 plugins →](categories/ui-enhancements.md)


### 🎭 Themes & Appearance

- [Small-tailqwq/dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐1494 — Whale Girl skin series for DeepSeek Harness. 适用于 DeepSeek Harness 的，鲸鱼娘系列皮肤。
- [d-dev0101/open-sea-skin](https://github.com/d-dev0101/open-sea-skin) ⭐177 — WebGPU ocean skin for DeepSeek Harness — DSH plugin, Harness-only Chrome/Edge extension, static installer, and native integration.
- [MeteorNOX/DeepSeek-Balance-Whale-Widget](https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget) ⭐116 — DeepSeek Harness（DSH）一只住在 DSH 界面右下角的小鲸鱼娘，帮你盯着DeepSeek账户余额。QQ弹弹，支持拖拽吸附、左吸附翻转、数字滚动动画，随界面自动启用，建议直接喊来你的dsh安装

▶️ [View all 137 plugins →](categories/themes-appearance.md)


### 💬 Sessions & Messages

- [MemTensor/MemOS](https://github.com/MemTensor/MemOS) ⭐10835 — Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support.
- [csyangwen/dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) ⭐195 — 为 DeepSeek Harness 带来「跨会话长期记忆 + 后台自我进化」能力的纯插件实现：五轨记忆 · git 分支感知 · 回合内自我审查 · 技能自我进化与技能管理器 · 四轨待办 · COI 调度 · 会话广播 · 会话搜索 · 提示词管理器 · 临时信息便签——零核心修改、零运行时依赖，随装随用、卸载即净。
- [hikariming/dshfind](https://github.com/hikariming/dshfind) ⭐188 — DSH (DeepSeek Harness) 原理学习、插件市场与最佳实践 · Learn DSH principles, plugin marketplace & best practices

▶️ [View all 797 plugins →](categories/sessions-messages.md)


### 🧠 Memory

- [text2future/flowix](https://github.com/text2future/flowix) ⭐327 — Notes for you, Memory for your agents. / 内置 Deepseek harness Agent / 适用 办公 & 写作 & Coding
- [ZSeven-W/dsh-noema](https://github.com/ZSeven-W/dsh-noema) ⭐113 — Noema long-term memory plugin for DSH: durable, inspectable agent memory with recall tools and a settings page.
- [btspoony/mstar-harness](https://github.com/btspoony/mstar-harness) ⭐51 — An omni-plugin for harness engineering workflows with multi-agents, programmatic gates and skills.

▶️ [View all 154 plugins →](categories/memory.md)


### 🛠️ Tools & Capabilities

- [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) ⭐16125 — 为 DeepSeek Harness (DSH) 插件生态打造的现代化桌面端解决方案。万物皆「插件」，桌面本身也是「插件」。
- [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) ⭐4311 — A next-generation, source-available AI workspace with a self-evolving agent runtime for editable code, design, presentations, websites, and video—a Codex alternative that integrates DeepSeek Harness for subagent delegation, combining iPolloWork’s complete AI workbench with DSH’s specialized agents and both plugin ecosystems in one workflow.
- [liustack/modlens](https://github.com/liustack/modlens) ⭐3362 — The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics). | 全网最强 DeepSeek Harness 外挂视觉插件，为 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义）。

▶️ [View all 1656 plugins →](categories/tools-capabilities.md)


### 🔁 Workflow & Automation

- [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) ⭐166722 — DeepSeek Harness: Everything is a Plugin.
- [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) ⭐12459 — Harness engineering beginner tutorial, from 0 to 1
- [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2949 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）

▶️ [View all 1303 plugins →](categories/workflow-automation.md)


### 🔔 Notifications & Integrations

- [gameswu/dsh-notifacation-frame](https://github.com/gameswu/dsh-notifacation-frame) ⭐4 — dsh通知消息统一管理框架
- [asakumizy/dsh-trae-bridge](https://github.com/asakumizy/dsh-trae-bridge) ⭐2 — DSH和trae连接
- [thuang3316/dsh-live-notify](https://github.com/thuang3316/dsh-live-notify) ⭐1 — DSH plugin for live notification

▶️ [View all 10 plugins →](categories/notifications-integrations.md)


### 🔌 Models & Providers

- [detpecca/dsh-llm-wiki](https://github.com/detpecca/dsh-llm-wiki) ⭐4
- [534119219/chicheng-stats](https://github.com/534119219/chicheng-stats) ⭐2 — DSH 全局用量统计插件：高度可配置侧边栏组件（文字/卡片）+ 统计面板（模型分布/趋势/首字节/耗时明细）
- [NLeRWantFly/dsh-HoldThatBigBlueFatFish](https://github.com/NLeRWantFly/dsh-HoldThatBigBlueFatFish) ⭐2 — 约束蓝色大肥鱼过度思考暂时的方案~模型测试opencode go实现

▶️ [View all 27 plugins →](categories/models-providers.md)


### 🧑‍💻 Development & Runtime

- [omdsh-dev/fabric](https://github.com/omdsh-dev/fabric) ⭐15 — 一种类似MC Fabric的dsh hook处理器
- [omdsh-dev/dsh-mygo](https://github.com/omdsh-dev/dsh-mygo) ⭐11
- [omdsh-dev/dsh-fun-ticker](https://github.com/omdsh-dev/dsh-fun-ticker) ⭐5 — DSH 行情跑马灯插件：可自选标的的加密/汇率/A股/指数/港美股跑马灯，免 key 数据源，宿主代理+缓存

▶️ [View all 26 plugins →](categories/development-runtime.md)


### 🔒 Security & Privacy

- [ravenli059/dsh-login](https://github.com/ravenli059/dsh-login) — 用于dsh-web加强安全性的插件，可设置用户名密码进行登录
- [Huauauaa/privacy](https://github.com/Huauauaa/privacy) — dsh-privacy-mask

▶️ [View all 2 plugins →](categories/security-privacy.md)


### 🎮 Just for Fun

- [Gin-7/dsh-pet-remielle](https://github.com/Gin-7/dsh-pet-remielle) ⭐22
- [gameswu/dsh-pref-kit](https://github.com/gameswu/dsh-pref-kit) ⭐4 — 缓解部分dsh性能问题的插件
- [pk7j7sqryy-ops/dsh-token-pet](https://github.com/pk7j7sqryy-ops/dsh-token-pet) ⭐1 — DSH 动态 Cordis 插件：卡通用量小部件 + 天气/预报/预警（Token Pet 布布玩偶）

▶️ [View all 6 plugins →](categories/fun.md)


### 📋 Awesome Lists & Collections

- [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐10460 — A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表
- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐5075 — Plugin and skin collection for DeepSeek Harness (DSH) Web UI - task board, git graph, right-side panel, remote mobile UI, pet, live token stats, and skin center.
- [AdamPlatin123/awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐1273 — DSH 插件雷达与精选榜：多路自动发现 9000+ 候选，容器真实安装路径运行级实测（四档判定），精选 Top 50 · 11 类人工策展，全量索引 PLUGINS-ALL.md，自动更新。

▶️ [View all 160 plugins →](categories/awesome-lists.md)


### ⚠️ Weakly Related


362 repositories tagged `dsh-plugin` but with low relevance confidence.


▶️ [View all 362 repos →](categories/weakly-related.md)


## Contributing


Found a plugin that should be here? Open a PR or issue!


1. Ensure your repo has the `dsh-plugin` topic on GitHub

2. The plugin should declare a `dsh.bundle` manifest

3. Submit a PR adding it to the appropriate category file


## License


[CC0 1.0 Universal](LICENSE)
