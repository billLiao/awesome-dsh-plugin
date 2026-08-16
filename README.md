# Awesome DeepSeek Harness (DSH) Plugin


[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


> A categorized curated list of plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`).


DeepSeek Harness is DeepSeek's open-source agent harness — a runnable coding agent (Web and headless), built on a framework where everything is a plugin: models, tools, sandboxes, session storage, UI, even the agent loop itself.


**1102 plugins** collected from GitHub topic [`dsh-plugin`](https://github.com/topics/dsh-plugin) · [PRs welcome](#contributing)


## Categories

| Category | Count | Description |

|----------|-------|-------------|

| 🎨 [UI Enhancements](categories/ui-enhancements.md) | 298 | Plugins that enhance the DSH web/terminal user interface. |

| 🎭 [Themes & Appearance](categories/themes-appearance.md) | 22 | Skins, themes, and appearance customization for DSH. |

| 💬 [Sessions & Messages](categories/sessions-messages.md) | 135 | Session management, message editing, sharing, and conversation tools. |

| 🧠 [Memory](categories/memory.md) | 30 | Persistent memory, knowledge bases, and context retention plugins. |

| 🛠️ [Tools & Capabilities](categories/tools-capabilities.md) | 296 | Vision, browser, terminal, SSH, Docker, and other capability extensions. |

| 🔁 [Workflow & Automation](categories/workflow-automation.md) | 154 | Automation loops, scheduled tasks, multi-agent teams, and workflow engines. |

| 🔔 [Notifications & Integrations](categories/notifications-integrations.md) | 2 | WeChat, Telegram, IM bridges, desktop notifications, and external integrations. |

| 🔌 [Models & Providers](categories/models-providers.md) | 2 | Multi-model support, OAuth login, LLM fallback strategies, and provider bridges. |

| 🧑‍💻 [Development & Runtime](categories/development-runtime.md) | 4 | Plugin managers, SDKs, CLIs, desktop wrappers, and developer tooling. |

| 🎮 [Just for Fun](categories/fun.md) | 3 | Games, pets, entertainment, and playful plugins. |

| 📋 [Awesome Lists & Collections](categories/awesome-lists.md) | 53 | Curated collections and awesome lists of DSH plugins. |

| ⚠️ [Weakly Related](categories/weakly-related.md) | 61 | Repositories tagged dsh-plugin but with weak relevance signals — may use DeepSeek API or have loose association. |


## Featured Plugins


A selection of notable plugins by category:


### 🎨 UI Enhancements

- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐1290 — DSH 官方公众号收录的 TUI 补位插件：Claude Code 风，鲸鱼顶栏/实时状态/流式思考/双击 Esc 回滚/上下文进度+TPS。npm 一键装。  DSH official WeChat featured TUI plugin — Claude Code style: whale bar, live status, streaming thoughts, double-Esc rollback, context bar + TPS. npm one-click.
- [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐1272 — 一个侧边栏的完整工作台，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/Git/子代理
- [Anionex/dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) ⭐439 — 让纯文本模型更好地做视觉任务的DeepSeek Harness插件：带意图的图片问答、长截图 OCR、UI 还原等｜DeepSeek Harness-native integration for agent-vision-toolkit: image Q&A, long-screenshot OCR, UI restoration, grounding, pixel diff, Artifacts, and Web UI.

▶️ [View all 298 plugins →](categories/ui-enhancements.md)


### 🎭 Themes & Appearance

- [SenmuuuuW/dsh-whale-report](https://github.com/SenmuuuuW/dsh-whale-report) ⭐14 — 🐋 鲸鱼记事本 — 你的 Agent 年度报告：从会话事件日志生成日报/周报/月报/年报，任意区间、只读不改写
- [Mochabafey/whale-notify](https://github.com/Mochabafey/whale-notify) ⭐4 — 鲸鱼通知——基于DeepSeek Harness的通知和鲸鱼娘人设插件
- [rongzi5/dsh-whale-pet](https://github.com/rongzi5/dsh-whale-pet) ⭐4

▶️ [View all 22 plugins →](categories/themes-appearance.md)


### 💬 Sessions & Messages

- [hikariming/dshfind](https://github.com/hikariming/dshfind) ⭐86 — DSH (DeepSeek Harness) 原理学习、插件市场与最佳实践 · Learn DSH principles, plugin marketplace & best practices
- [Ayase34/gal-view](https://github.com/Ayase34/gal-view) ⭐53 — 把dsh会话界面切换成galgame游戏界面的插件
- [Nwflower/dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) ⭐35 — 从Claude Code、Codex、Reasonix等Agent工具导入迁移历史消息，并在DeepSeek Harness(DSH)中继续对话

▶️ [View all 135 plugins →](categories/sessions-messages.md)


### 🧠 Memory

- [btspoony/mstar-harness](https://github.com/btspoony/mstar-harness) ⭐45 — A Skill-driven Harness/Loop Engineering Workflow Agent Plugin
- [knqiufan/powercontext-dsh](https://github.com/knqiufan/powercontext-dsh) ⭐10 — DeepSeek Harness plugin that connects to a PowerContext Server over HTTP for recall, memory, handoff, experience, and skills.
- [nowledge-co/nowledge-mem-deepseek-harness](https://github.com/nowledge-co/nowledge-mem-deepseek-harness) ⭐5 — One memory layer for every AI tool and agent, packaged for DeepSeek Harness

▶️ [View all 30 plugins →](categories/memory.md)


### 🛠️ Tools & Capabilities

- [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) ⭐6163 — 为 DeepSeek Harness (DSH) 生态打造的现代化桌面端体验
- [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) ⭐4088 — A next-generation, source-available AI workspace with a self-evolving agent runtime for editable code, design, presentations, websites, and video—a Codex alternative that integrates DeepSeek Harness for subagent delegation, combining iPolloWork’s complete AI workbench with DSH’s specialized agents and both plugin ecosystems in one workflow.
- [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) ⭐2253 — Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99)

▶️ [View all 296 plugins →](categories/tools-capabilities.md)


### 🔁 Workflow & Automation

- [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2583 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）
- [dsh-market/dsh-market](https://github.com/dsh-market/dsh-market) ⭐298 — The plugin market inside DeepSeek Harness — browse, search, one-click install · DSH 可视化插件市场
- [bowenliang123/dsh-context](https://github.com/bowenliang123/dsh-context) ⭐42 — A DeepSeek Harness plugin for  Context insight dashboard — showing what the model's context window is made of and how it evolves.

▶️ [View all 154 plugins →](categories/workflow-automation.md)


### 🔔 Notifications & Integrations

- [gameswu/dsh-notifacation-frame](https://github.com/gameswu/dsh-notifacation-frame) ⭐1 — dsh通知消息统一管理框架
- [thuang3316/dsh-live-notify](https://github.com/thuang3316/dsh-live-notify) ⭐1 — DSH plugin for live notification

▶️ [View all 2 plugins →](categories/notifications-integrations.md)


### 🔌 Models & Providers

- [HB00/dsh-llm-failover](https://github.com/HB00/dsh-llm-failover) — dsh-llm-failover
- [kingsunb/dsh-model-plus](https://github.com/kingsunb/dsh-model-plus)

▶️ [View all 2 plugins →](categories/models-providers.md)


### 🧑‍💻 Development & Runtime

- [wzxaaaa/dsh-w-plugin-ecosystem](https://github.com/wzxaaaa/dsh-w-plugin-ecosystem) ⭐2 — 为dsh专属打造的贴近原生的自定义插件生态，支持插件可配置，独立协议，热拔插
- [2128627267/dsh-qbetter-config](https://github.com/2128627267/dsh-qbetter-config) ⭐1
- [omdsh-dev/dsh-sandbox-micro](https://github.com/omdsh-dev/dsh-sandbox-micro) ⭐1

▶️ [View all 4 plugins →](categories/development-runtime.md)


### 🎮 Just for Fun

- [gameswu/dsh-pref-kit](https://github.com/gameswu/dsh-pref-kit) ⭐1 — 缓解部分dsh性能问题的插件
- [pk7j7sqryy-ops/dsh-token-pet](https://github.com/pk7j7sqryy-ops/dsh-token-pet) ⭐1 — DSH 动态 Cordis 插件：卡通用量小部件 + 天气/预报/预警（Token Pet 布布玩偶）
- [gxx950224/ggame](https://github.com/gxx950224/ggame) — dsh ggame plugin

▶️ [View all 3 plugins →](categories/fun.md)


### 📋 Awesome Lists & Collections

- [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐3092 — A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表
- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐2764 — Plugin and skin collection for DeepSeek Harness (DSH) Web UI - task board, git graph, right-side panel, remote mobile UI, pet, live token stats, and skin center.
- [AdamPlatin123/awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐975 — 前部索引仓库（Radar）：自动扫描发现的所有 dsh 插件候选；经测试合格的将移入后序精选目录仓库

▶️ [View all 53 plugins →](categories/awesome-lists.md)


### ⚠️ Weakly Related


61 repositories tagged `dsh-plugin` but with low relevance confidence.


▶️ [View all 61 repos →](categories/weakly-related.md)


## Contributing


Found a plugin that should be here? Open a PR or issue!


1. Ensure your repo has the `dsh-plugin` topic on GitHub

2. The plugin should declare a `dsh.bundle` manifest

3. Submit a PR adding it to the appropriate category file


## License


[CC0 1.0 Universal](LICENSE)
