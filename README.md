# Awesome DeepSeek Harness (DSH) Plugin


[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


> A categorized curated list of plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`).


DeepSeek Harness is DeepSeek's open-source agent harness — a runnable coding agent (Web and headless), built on a framework where everything is a plugin: models, tools, sandboxes, session storage, UI, even the agent loop itself.


**994 plugins** collected from GitHub topic [`dsh-plugin`](https://github.com/topics/dsh-plugin) · [PRs welcome](#contributing)


## Categories

| Category | Count | Description |

|----------|-------|-------------|

| 🎨 [UI Enhancements](categories/ui-enhancements.md) | 285 | Plugins that enhance the DSH web/terminal user interface. |

| 🎭 [Themes & Appearance](categories/themes-appearance.md) | 30 | Skins, themes, and appearance customization for DSH. |

| 💬 [Sessions & Messages](categories/sessions-messages.md) | 116 | Session management, message editing, sharing, and conversation tools. |

| 🧠 [Memory](categories/memory.md) | 20 | Persistent memory, knowledge bases, and context retention plugins. |

| 🛠️ [Tools & Capabilities](categories/tools-capabilities.md) | 248 | Vision, browser, terminal, SSH, Docker, and other capability extensions. |

| 🔁 [Workflow & Automation](categories/workflow-automation.md) | 140 | Automation loops, scheduled tasks, multi-agent teams, and workflow engines. |

| 🔔 [Notifications & Integrations](categories/notifications-integrations.md) | 2 | WeChat, Telegram, IM bridges, desktop notifications, and external integrations. |

| 🔌 [Models & Providers](categories/models-providers.md) | 6 | Multi-model support, OAuth login, LLM fallback strategies, and provider bridges. |

| 🧑‍💻 [Development & Runtime](categories/development-runtime.md) | 2 | Plugin managers, SDKs, CLIs, desktop wrappers, and developer tooling. |

| 🎮 [Just for Fun](categories/fun.md) | 1 | Games, pets, entertainment, and playful plugins. |

| 📋 [Awesome Lists & Collections](categories/awesome-lists.md) | 55 | Curated collections and awesome lists of DSH plugins. |

| ⚠️ [Weakly Related](categories/weakly-related.md) | 61 | Repositories tagged dsh-plugin but with weak relevance signals — may use DeepSeek API or have loose association. |


## Featured Plugins


A selection of notable plugins by category:


### 🎨 UI Enhancements

- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐1106 — 解决DSH 官方尚无终端 TUI 痛点的补位之作，献给偏爱cli的各位极客：Claude Code 风格全屏交互终端插件——像素鲸鱼顶栏、实时工作状态行、思考流式展开、双击 Esc 回滚、上下文进度条 + TPS 仪表。npm 一键安装。
- [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐974 — 一个侧边栏的完整工作台，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/Git/子代理
- [Electricitysheep/dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) ⭐261 — DeepSeek Harness (dsh) 从 0 到 1 深度手册：安装/插件开发/性能调优/实测案例/同模型多 Agent 实测对比（中文 + 英文 PDF）

▶️ [View all 285 plugins →](categories/ui-enhancements.md)


### 🎭 Themes & Appearance

- [Small-tailqwq/dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐790 — DSH Web 鲸鱼娘皮肤系列(深海女仆工坊 maid-atelier)——CC BY-NC-SA 4.0
- [LaplaceYoung/dsh-qq2006](https://github.com/LaplaceYoung/dsh-qq2006) ⭐10 — DSH (DeepSeek Harness) 的 QQ2006 皮肤插件：注册 qq2006 主题、镜像 body[data-ds-skin]、全局皮肤表与完整素材
- [SenmuuuuW/dsh-whale-report](https://github.com/SenmuuuuW/dsh-whale-report) ⭐9 — 🐋 鲸鱼记事本 — 你的 Agent 年度报告：从会话事件日志生成日报/周报/月报/年报，任意区间、只读不改写

▶️ [View all 30 plugins →](categories/themes-appearance.md)


### 💬 Sessions & Messages

- [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) ⭐584 — Open-source CMA-compatible agent runtime for any model, with MCP tools, sandboxed sessions, audit, replay, and a local console. Includes a native DeepSeek Harness bundle over stdio MCP.
- [vibeinging/deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) ⭐114 — DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.
- [hikariming/dshfind](https://github.com/hikariming/dshfind) ⭐79 — DSH (DeepSeek Harness) 原理学习、插件市场与最佳实践 · Learn DSH principles, plugin marketplace & best practices

▶️ [View all 116 plugins →](categories/sessions-messages.md)


### 🧠 Memory

- [btspoony/mstar-harness](https://github.com/btspoony/mstar-harness) ⭐45 — A Skill-driven Harness/Loop Engineering Workflow Agent Plugin
- [zhujunpeng12/dsh-memory-system](https://github.com/zhujunpeng12/dsh-memory-system) ⭐6 — Local-first persistent memory infrastructure for DeepSeek Harness: hot bootstrap, Chinese-BM25 cold recall, lease-lock transactional writes, read-only governance
- [limbo947/dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) ⭐5 — DSH 消息撤回插件：回到发送该消息时的状态

▶️ [View all 20 plugins →](categories/memory.md)


### 🛠️ Tools & Capabilities

- [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) ⭐4184 — 为 DeepSeek Harness (DSH) 生态打造的现代化桌面端体验
- [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) ⭐4083 — A next-generation, source-available AI workspace with a self-evolving agent runtime for editable code, design, presentations, websites, and video—a Codex alternative that integrates DeepSeek Harness for subagent delegation, combining iPolloWork’s complete AI workbench with DSH’s specialized agents and both plugin ecosystems in one workflow.
- [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) ⭐1614 — Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99)

▶️ [View all 248 plugins →](categories/tools-capabilities.md)


### 🔁 Workflow & Automation

- [NanmiCoder/dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) ⭐298 — AgentTeams plugin for DeepSeek Harness
- [dsh-market/dsh-market](https://github.com/dsh-market/dsh-market) ⭐192 — The plugin market inside DeepSeek Harness — browse, search, one-click install · DSH 可视化插件市场
- [LaplaceYoung/oh-my-dsh](https://github.com/LaplaceYoung/oh-my-dsh) ⭐45 — oh-my-dsh：面向 DSH (DeepSeek Harness) 的插件生态——700+ 插件，只通过扩展接缝注册，不修改 agent-loop 骨架

▶️ [View all 140 plugins →](categories/workflow-automation.md)


### 🔔 Notifications & Integrations

- [Zyy1997/dsh-sound-notify](https://github.com/Zyy1997/dsh-sound-notify) ⭐1 — dsh plugin: play a sound on the host when an agent finishes its turn or waits for approval
- [CACppuccino/dsh-multiagent-enhence](https://github.com/CACppuccino/dsh-multiagent-enhence)

▶️ [View all 2 plugins →](categories/notifications-integrations.md)


### 🔌 Models & Providers

- [HuanLinOTO/dsh-plugin-d399](https://github.com/HuanLinOTO/dsh-plugin-d399) ⭐5 — 模型生成时右下角弹出小游戏菜单（Wordle/消消乐/192 款参数化小游戏，可拓展注册表） | Pops up a mini-game menu while the model generates (Wordle/Match-3/192 parametric mini-games, extensible registry)
- [omdsh-dev/dsh-llm-fallbacks](https://github.com/omdsh-dev/dsh-llm-fallbacks) ⭐4 — An dsh plugin for role-based LLM retry&fallback strategy. 基于角色的模型重试备用策略插件
- [NLeRWantFly/dsh-HoldThatBigBlueFatFish](https://github.com/NLeRWantFly/dsh-HoldThatBigBlueFatFish) ⭐2 — 约束蓝色大肥鱼过度思考暂时的方案~模型测试opencode go实现

▶️ [View all 6 plugins →](categories/models-providers.md)


### 🧑‍💻 Development & Runtime

- [healing1/dsh-web-plugin-manager](https://github.com/healing1/dsh-web-plugin-manager)
- [V-dev-388/dsh-plugin-hello](https://github.com/V-dev-388/dsh-plugin-hello)

▶️ [View all 2 plugins →](categories/development-runtime.md)


### 🎮 Just for Fun

- [Gin-7/dsh-pet-remielle](https://github.com/Gin-7/dsh-pet-remielle)

▶️ [View all 1 plugins →](categories/fun.md)


### 📋 Awesome Lists & Collections

- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐2376 — Plugin and skin collection for DeepSeek Harness (DSH) Web UI - task board, git graph, right-side panel, remote mobile UI, pet, live token stats, and skin center.
- [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐2274 — A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表
- [AdamPlatin123/awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐926 — 前部索引仓库（Radar）：自动扫描发现的所有 dsh 插件候选；经测试合格的将移入后序精选目录仓库

▶️ [View all 55 plugins →](categories/awesome-lists.md)


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
