# Awesome DeepSeek Harness (DSH) Plugin

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A categorized curated list of plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`).

DeepSeek Harness is DeepSeek's open-source agent harness — a runnable coding agent (Web and headless), built on a framework where everything is a plugin: models, tools, sandboxes, session storage, UI, even the agent loop itself.

**939 plugins** collected from GitHub topic [`dsh-plugin`](https://github.com/topics/dsh-plugin) · [PRs welcome](#contributing)

## Categories

| Category | Count | Description |
|----------|-------|-------------|
| 🎨 [UI Enhancements](categories/ui-enhancements.md) | 151 | Plugins that enhance the DSH web/terminal user interface. |
| 🎭 [Themes & Appearance](categories/themes-appearance.md) | 13 | Skins, themes, and appearance customization for DSH. |
| 💬 [Sessions & Messages](categories/sessions-messages.md) | 65 | Session management, message editing, sharing, and conversation tools. |
| 🧠 [Memory](categories/memory.md) | 12 | Persistent memory, knowledge bases, and context retention plugins. |
| 🛠️ [Tools & Capabilities](categories/tools-capabilities.md) | 165 | Vision, browser, terminal, SSH, Docker, and other capability extensions. |
| 🔁 [Workflow & Automation](categories/workflow-automation.md) | 107 | Automation loops, scheduled tasks, multi-agent teams, and workflow engines. |
| 🔔 [Notifications & Integrations](categories/notifications-integrations.md) | 43 | WeChat, Telegram, IM bridges, desktop notifications, and external integrations. |
| 🔌 [Models & Providers](categories/models-providers.md) | 127 | Multi-model support, OAuth login, LLM fallback strategies, and provider bridges. |
| 🧑‍💻 [Development & Runtime](categories/development-runtime.md) | 144 | Plugin managers, SDKs, CLIs, desktop wrappers, and developer tooling. |
| 🔒 [Security & Privacy](categories/security-privacy.md) | 53 | Credential management, encryption, audit, and security tooling. |
| 🎮 [Just for Fun](categories/fun.md) | 38 | Games, pets, entertainment, and playful plugins. |
| 📋 [Awesome Lists & Collections](categories/awesome-lists.md) | 21 | Curated collections and awesome lists of DSH plugins. |

## Featured Plugins

A selection of notable plugins by category:


### 🎨 UI Enhancements

- [Anionex/dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) ⭐256 — 让纯文本模型更好地做视觉任务的DeepSeek Harness插件：带意图的图片问答、长截图 OCR、UI 还原等｜DeepSeek Harness-native integration for agent-vision-toolkit: image Q&A, long-screenshot OCR, UI restoration, grounding, pixel diff, Artifacts, and Web UI.
- [hust-open-atom-club/oh-dsh](https://github.com/hust-open-atom-club/oh-dsh) ⭐122 — 一站式 DeepSeek Harness 社区发行版：TUI、桌面端与 Web UI 三种形态统一体验，支持分层安装、一步到位，免去手工整合打包。
- [Electricitysheep/dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) ⭐106 — DeepSeek Harness (dsh) 从 0 到 1 深度手册：安装/插件开发/性能调优/实测案例/同模型多 Agent 实测对比（中文 + 英文 PDF）

▶️ [View all 151 plugins →](categories/ui-enhancements.md)


### 🎭 Themes & Appearance

- [Small-tailqwq/dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐339 — DSH Web 鲸鱼娘皮肤系列(深海女仆工坊 maid-atelier)——CC BY-NC-SA 4.0
- [147228/dsh-xiaoyao-skins](https://github.com/147228/dsh-xiaoyao-skins) ⭐10 — 夕小瑶 × DeepSeek Harness Web 皮肤合集、安装器与社区创作工具链
- [suzike/freestyle-dsh-theme](https://github.com/suzike/freestyle-dsh-theme) ⭐1 — DeepSeek Harness 主题体验插件：OKLCH 主题提案 + 主题设计器（跨重启持久化）

▶️ [View all 13 plugins →](categories/themes-appearance.md)


### 💬 Sessions & Messages

- [csyangwen/dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) ⭐29 — 为 DeepSeek Harness 带来「跨会话长期记忆 + 后台自我进化」能力的纯插件实现：五轨记忆 · git 分支感知 · 回合内自我审查 · 技能自我进化与技能管理器 · 四轨待办 · COI 调度 · 会话广播 · 会话搜索 · 提示词管理器 · 临时信息便签——零核心修改、零运行时依赖，随装随用、卸载即净。
- [Anionex/dsh-turn-rewind](https://github.com/Anionex/dsh-turn-rewind) ⭐27 — deepseek harness对话和代码状态回退插件 | DSH — rewind conversation and workspace state, powered by a persistent Change Ledger
- [titanwings/dsh-automation](https://github.com/titanwings/dsh-automation) ⭐21 — DSH 自动化插件：让 Coding 任务按计划在全新 Agent Session 中运行，并由用户或 Agent 创建和管理定时任务。 / Run coding tasks in fresh Agent sessions and manage schedules from DSH Web or an Agent.

▶️ [View all 65 plugins →](categories/sessions-messages.md)


### 🧠 Memory

- [btspoony/mstar-harness](https://github.com/btspoony/mstar-harness) ⭐41 — A Skill-driven Harness/Loop Engineering Workflow Agent Plugin
- [knqiufan/powercontext-dsh](https://github.com/knqiufan/powercontext-dsh) ⭐4 — DeepSeek Harness plugin that connects to a PowerContext Server over HTTP for recall, memory, handoff, experience, and skills.
- [modusensus/dsh-mneme](https://github.com/modusensus/dsh-mneme) ⭐3 — Mneme——把记忆主权还给人的记忆插件：SQLite + 可人工编辑的 Markdown 双写，autoDream 在梦境中巩固记忆，140 个测试护航。

▶️ [View all 12 plugins →](categories/memory.md)


### 🛠️ Tools & Capabilities

- [zhaoolee/notes](https://github.com/zhaoolee/notes) ⭐137 — 开源版锤子便签，复刻锤科美学，一键Docker私有化部署，支持skill调用，支持dsh plugin，支持多租户，一键生成公众号格式，支持导出便签为图片
- [Nagi-ovo/dsh-find-plugins](https://github.com/Nagi-ovo/dsh-find-plugins) ⭐59
- [icetomoyo/dsh_workflow](https://github.com/icetomoyo/dsh_workflow) ⭐49 — 把Claude Code的UltraCode模式带给DSH，把 DSH 的一次性多 Agent 调度，升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层

▶️ [View all 165 plugins →](categories/tools-capabilities.md)


### 🔁 Workflow & Automation

- [NanmiCoder/dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) ⭐170 — AgentTeams plugin for DeepSeek Harness
- [omdsh-dev/dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) ⭐10 — 定义了专用的Data Agent预设，让AI帮你查询、更新、分析。
- [hellodigua/dsh-emoji](https://github.com/hellodigua/dsh-emoji) ⭐9 — 为 DSH 的回复加入自定义的行内表情

▶️ [View all 107 plugins →](categories/workflow-automation.md)


### 🔔 Notifications & Integrations

- [liustack/modlens](https://github.com/liustack/modlens) ⭐939 — The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics).
- [liustack/modsearch](https://github.com/liustack/modsearch) ⭐76 — The web plugin for DeepSeek Harness, and the search bridge for every text-only coding agent. Ask the web or X, get structured JSON evidence (search, fetch, citations).
- [whiteguo233/dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) ⭐17 — OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。

▶️ [View all 43 plugins →](categories/notifications-integrations.md)


### 🔌 Models & Providers

- [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) ⭐3784 — A next-generation, source-available AI workspace with a self-evolving agent runtime for editable code, design, presentations, websites, and video—a Codex alternative that integrates DeepSeek Harness for subagent delegation, combining iPolloWork’s complete AI workbench with DSH’s specialized agents and both plugin ecosystems in one workflow.
- [omdsh-dev/dsh-at-file](https://github.com/omdsh-dev/dsh-at-file) ⭐78 — Codex-style @file mentions for DeepSeek Harness: search workspace files in the composer and attach their contents to prompts.
- [zenx0x/allinluna](https://github.com/zenx0x/allinluna) ⭐24 — Resource-aware multi-agent orchestration for Codex and DeepSeek Harness (All in Flash DSH plugin)

▶️ [View all 127 plugins →](categories/models-providers.md)


### 🧑‍💻 Development & Runtime

- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐586 — 解决DSH 官方尚无终端 TUI 痛点的补位之作，献给偏爱cli的各位极客：Claude Code 风格全屏交互终端插件——像素鲸鱼顶栏、实时工作状态行、思考流式展开、双击 Esc 回滚、上下文进度条 + TPS 仪表。npm 一键安装。
- [AdamPlatin123/awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐567 — 前部索引仓库（Radar）：自动扫描发现的所有 dsh 插件候选；经测试合格的将移入后序精选目录仓库
- [Ruler4396/dsh-launcher](https://github.com/Ruler4396/dsh-launcher) ⭐48 — Lightweight Windows launcher for DeepSeek Harness: silent autostart at logon + a minimal WebView2 window instead of a full browser

▶️ [View all 144 plugins →](categories/development-runtime.md)


### 🔒 Security & Privacy

- [PM-Shawn/Abu-Cowork](https://github.com/PM-Shawn/Abu-Cowork) ⭐318 — Open-source alternative to Claude Cowork — a local-first AI agent desktop app · multi-model · self-evolving skills · privacy-first · multi-Harness roadmap · DeepSeek Harness integration in progress
- [SenmuuuuW/dsh-group-photo](https://github.com/SenmuuuuW/dsh-group-photo) ⭐12 — DSH 内测收官合影墙：GitHub OAuth 零权限登录 + 冻结白名单校验的拍立得合影站（含 DSH Skill 包装）
- [omdsh-dev/dsh-security-audit](https://github.com/omdsh-dev/dsh-security-audit) ⭐9 — DSH 本机安全审计插件：配置/插件来源/会话/网络暴露面，只读脱敏风险报告

▶️ [View all 53 plugins →](categories/security-privacy.md)


### 🎮 Just for Fun

- [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2185 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）
- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐1144 — Plugin and skin collection for DeepSeek Harness (DSH) Web UI - task board, git graph, right-side panel, remote mobile UI, pet, live token stats, and skin center.
- [Nagi-ovo/dsh-ads](https://github.com/Nagi-ovo/dsh-ads) ⭐243 — 是兄弟就来蹬我！DSH Web UI 广告：2005 年中文站点风格的侧栏广告 / 对话内信息流 / 角落弹窗 + 一个真实热区比视觉小得多的关闭叉。素材全虚构，域名打码。

▶️ [View all 38 plugins →](categories/fun.md)


### 📋 Awesome Lists & Collections

- [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐375 — A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表
- [0xsline/awesome-deepseek-harness](https://github.com/0xsline/awesome-deepseek-harness) ⭐261 — DeepSeek Harness (DSH) ecosystem: curated plugins, tools, and infrastructure from dsh-external/hub and the public dsh-plugin topic.
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) ⭐45 — 用 30 秒找到适合你的 DeepSeek Harness 插件。 不只是仓库列表：这里告诉你插件解决什么问题、适合谁，以及从哪里开始。

▶️ [View all 21 plugins →](categories/awesome-lists.md)

## Contributing

Found a plugin that should be here? Open a PR or issue!

1. Ensure your repo has the `dsh-plugin` topic on GitHub
2. The plugin should declare a `dsh.bundle` manifest
3. Submit a PR adding it to the appropriate category file

## License

[CC0 1.0 Universal](LICENSE)
