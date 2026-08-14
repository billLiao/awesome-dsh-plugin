# Awesome DeepSeek Harness (DSH) Plugin

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）插件分类精选列表。

DeepSeek Harness 是 DeepSeek 开源的 agent harness——既是可直接运行的 Coding Agent，底层又是一套「一切皆插件」的框架。

**939 个插件**，来自 GitHub 话题 [`dsh-plugin`](https://github.com/topics/dsh-plugin) · 欢迎 [PR](#贡献)

## 分类

| 分类 | 数量 | 说明 |
|------|------|------|
| 🎨 [UI 增强](categories/ui-enhancements.md) | 151 | 增强 DSH Web/终端用户界面的插件。 |
| 🎭 [主题与外观](categories/themes-appearance.md) | 13 | DSH 皮肤、主题与外观定制。 |
| 💬 [会话与消息](categories/sessions-messages.md) | 65 | 会话管理、消息编辑、分享与对话工具。 |
| 🧠 [记忆](categories/memory.md) | 12 | 持久记忆、知识库与上下文保留插件。 |
| 🛠️ [工具与能力](categories/tools-capabilities.md) | 165 | 视觉、浏览器、终端、SSH、Docker 等能力扩展。 |
| 🔁 [工作流与自动化](categories/workflow-automation.md) | 107 | 自动化循环、定时任务、多智能体团队与工作流引擎。 |
| 🔔 [通知与集成](categories/notifications-integrations.md) | 43 | 微信、Telegram、IM 桥接、桌面通知与外部集成。 |
| 🔌 [模型与账号接入](categories/models-providers.md) | 127 | 多模型支持、OAuth 登录、LLM 回退策略与提供商桥接。 |
| 🧑‍💻 [开发与运行时](categories/development-runtime.md) | 144 | 插件管理器、SDK、CLI、桌面壳与开发者工具。 |
| 🔒 [安全与隐私](categories/security-privacy.md) | 53 | 凭证管理、加密、审计与安全工具。 |
| 🎮 [娱乐](categories/fun.md) | 38 | 游戏、桌宠、娱乐与趣味插件。 |
| 📋 [精选列表与合集](categories/awesome-lists.md) | 21 | DSH 插件精选列表与合集。 |

## 精选插件


### 🎨 UI 增强

- [Anionex/dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) ⭐256 — 让纯文本模型更好地做视觉任务的DeepSeek Harness插件：带意图的图片问答、长截图 OCR、UI 还原等｜DeepSeek Harness-native integration for agent-vision-toolkit: image Q&A, long-screenshot OCR, UI restoration, grounding, pixel diff, Artifacts, and Web UI.
- [hust-open-atom-club/oh-dsh](https://github.com/hust-open-atom-club/oh-dsh) ⭐122 — 一站式 DeepSeek Harness 社区发行版：TUI、桌面端与 Web UI 三种形态统一体验，支持分层安装、一步到位，免去手工整合打包。
- [Electricitysheep/dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) ⭐106 — DeepSeek Harness (dsh) 从 0 到 1 深度手册：安装/插件开发/性能调优/实测案例/同模型多 Agent 实测对比（中文 + 英文 PDF）

▶️ [查看全部 151 个插件 →](categories/ui-enhancements.md)


### 🎭 主题与外观

- [Small-tailqwq/dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐339 — DSH Web 鲸鱼娘皮肤系列(深海女仆工坊 maid-atelier)——CC BY-NC-SA 4.0
- [147228/dsh-xiaoyao-skins](https://github.com/147228/dsh-xiaoyao-skins) ⭐10 — 夕小瑶 × DeepSeek Harness Web 皮肤合集、安装器与社区创作工具链
- [suzike/freestyle-dsh-theme](https://github.com/suzike/freestyle-dsh-theme) ⭐1 — DeepSeek Harness 主题体验插件：OKLCH 主题提案 + 主题设计器（跨重启持久化）

▶️ [查看全部 13 个插件 →](categories/themes-appearance.md)


### 💬 会话与消息

- [csyangwen/dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) ⭐29 — 为 DeepSeek Harness 带来「跨会话长期记忆 + 后台自我进化」能力的纯插件实现：五轨记忆 · git 分支感知 · 回合内自我审查 · 技能自我进化与技能管理器 · 四轨待办 · COI 调度 · 会话广播 · 会话搜索 · 提示词管理器 · 临时信息便签——零核心修改、零运行时依赖，随装随用、卸载即净。
- [Anionex/dsh-turn-rewind](https://github.com/Anionex/dsh-turn-rewind) ⭐27 — deepseek harness对话和代码状态回退插件 | DSH — rewind conversation and workspace state, powered by a persistent Change Ledger
- [titanwings/dsh-automation](https://github.com/titanwings/dsh-automation) ⭐21 — DSH 自动化插件：让 Coding 任务按计划在全新 Agent Session 中运行，并由用户或 Agent 创建和管理定时任务。 / Run coding tasks in fresh Agent sessions and manage schedules from DSH Web or an Agent.

▶️ [查看全部 65 个插件 →](categories/sessions-messages.md)


### 🧠 记忆

- [btspoony/mstar-harness](https://github.com/btspoony/mstar-harness) ⭐41 — A Skill-driven Harness/Loop Engineering Workflow Agent Plugin
- [knqiufan/powercontext-dsh](https://github.com/knqiufan/powercontext-dsh) ⭐4 — DeepSeek Harness plugin that connects to a PowerContext Server over HTTP for recall, memory, handoff, experience, and skills.
- [modusensus/dsh-mneme](https://github.com/modusensus/dsh-mneme) ⭐3 — Mneme——把记忆主权还给人的记忆插件：SQLite + 可人工编辑的 Markdown 双写，autoDream 在梦境中巩固记忆，140 个测试护航。

▶️ [查看全部 12 个插件 →](categories/memory.md)


### 🛠️ 工具与能力

- [zhaoolee/notes](https://github.com/zhaoolee/notes) ⭐137 — 开源版锤子便签，复刻锤科美学，一键Docker私有化部署，支持skill调用，支持dsh plugin，支持多租户，一键生成公众号格式，支持导出便签为图片
- [Nagi-ovo/dsh-find-plugins](https://github.com/Nagi-ovo/dsh-find-plugins) ⭐59
- [icetomoyo/dsh_workflow](https://github.com/icetomoyo/dsh_workflow) ⭐49 — 把Claude Code的UltraCode模式带给DSH，把 DSH 的一次性多 Agent 调度，升级为可生成、可保存、可治理、可观察、可恢复的 Workflow 层

▶️ [查看全部 165 个插件 →](categories/tools-capabilities.md)


### 🔁 工作流与自动化

- [NanmiCoder/dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) ⭐170 — AgentTeams plugin for DeepSeek Harness
- [omdsh-dev/dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) ⭐10 — 定义了专用的Data Agent预设，让AI帮你查询、更新、分析。
- [hellodigua/dsh-emoji](https://github.com/hellodigua/dsh-emoji) ⭐9 — 为 DSH 的回复加入自定义的行内表情

▶️ [查看全部 107 个插件 →](categories/workflow-automation.md)


### 🔔 通知与集成

- [liustack/modlens](https://github.com/liustack/modlens) ⭐939 — The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics).
- [liustack/modsearch](https://github.com/liustack/modsearch) ⭐76 — The web plugin for DeepSeek Harness, and the search bridge for every text-only coding agent. Ask the web or X, get structured JSON evidence (search, fetch, citations).
- [whiteguo233/dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) ⭐17 — OpenBiliClaw 是本地运行的跨平台个性化内容推荐 Agent，持续理解你的兴趣并主动找内容。本仓库是它的 DeepSeek Harness 插件：DSH 界面常驻第四栏（推荐/内容库/对话/画像/设置），注册 22 个 Agent Bridge 工具，让 Agent 也能读推荐、答探测、闭环学习。

▶️ [查看全部 43 个插件 →](categories/notifications-integrations.md)


### 🔌 模型与账号接入

- [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) ⭐3784 — A next-generation, source-available AI workspace with a self-evolving agent runtime for editable code, design, presentations, websites, and video—a Codex alternative that integrates DeepSeek Harness for subagent delegation, combining iPolloWork’s complete AI workbench with DSH’s specialized agents and both plugin ecosystems in one workflow.
- [omdsh-dev/dsh-at-file](https://github.com/omdsh-dev/dsh-at-file) ⭐78 — Codex-style @file mentions for DeepSeek Harness: search workspace files in the composer and attach their contents to prompts.
- [zenx0x/allinluna](https://github.com/zenx0x/allinluna) ⭐24 — Resource-aware multi-agent orchestration for Codex and DeepSeek Harness (All in Flash DSH plugin)

▶️ [查看全部 127 个插件 →](categories/models-providers.md)


### 🧑‍💻 开发与运行时

- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐586 — 解决DSH 官方尚无终端 TUI 痛点的补位之作，献给偏爱cli的各位极客：Claude Code 风格全屏交互终端插件——像素鲸鱼顶栏、实时工作状态行、思考流式展开、双击 Esc 回滚、上下文进度条 + TPS 仪表。npm 一键安装。
- [AdamPlatin123/awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐567 — 前部索引仓库（Radar）：自动扫描发现的所有 dsh 插件候选；经测试合格的将移入后序精选目录仓库
- [Ruler4396/dsh-launcher](https://github.com/Ruler4396/dsh-launcher) ⭐48 — Lightweight Windows launcher for DeepSeek Harness: silent autostart at logon + a minimal WebView2 window instead of a full browser

▶️ [查看全部 144 个插件 →](categories/development-runtime.md)


### 🔒 安全与隐私

- [PM-Shawn/Abu-Cowork](https://github.com/PM-Shawn/Abu-Cowork) ⭐318 — Open-source alternative to Claude Cowork — a local-first AI agent desktop app · multi-model · self-evolving skills · privacy-first · multi-Harness roadmap · DeepSeek Harness integration in progress
- [SenmuuuuW/dsh-group-photo](https://github.com/SenmuuuuW/dsh-group-photo) ⭐12 — DSH 内测收官合影墙：GitHub OAuth 零权限登录 + 冻结白名单校验的拍立得合影站（含 DSH Skill 包装）
- [omdsh-dev/dsh-security-audit](https://github.com/omdsh-dev/dsh-security-audit) ⭐9 — DSH 本机安全审计插件：配置/插件来源/会话/网络暴露面，只读脱敏风险报告

▶️ [查看全部 53 个插件 →](categories/security-privacy.md)


### 🎮 娱乐

- [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2185 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）
- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐1144 — Plugin and skin collection for DeepSeek Harness (DSH) Web UI - task board, git graph, right-side panel, remote mobile UI, pet, live token stats, and skin center.
- [Nagi-ovo/dsh-ads](https://github.com/Nagi-ovo/dsh-ads) ⭐243 — 是兄弟就来蹬我！DSH Web UI 广告：2005 年中文站点风格的侧栏广告 / 对话内信息流 / 角落弹窗 + 一个真实热区比视觉小得多的关闭叉。素材全虚构，域名打码。

▶️ [查看全部 38 个插件 →](categories/fun.md)


### 📋 精选列表与合集

- [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐375 — A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表
- [0xsline/awesome-deepseek-harness](https://github.com/0xsline/awesome-deepseek-harness) ⭐261 — DeepSeek Harness (DSH) ecosystem: curated plugins, tools, and infrastructure from dsh-external/hub and the public dsh-plugin topic.
- [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) ⭐45 — 用 30 秒找到适合你的 DeepSeek Harness 插件。 不只是仓库列表：这里告诉你插件解决什么问题、适合谁，以及从哪里开始。

▶️ [查看全部 21 个插件 →](categories/awesome-lists.md)

## 贡献

发现了一个应该收录的插件？欢迎提交 PR 或 Issue！

1. 确保你的仓库有 `dsh-plugin` 话题标签
2. 插件应声明 `dsh.bundle` manifest
3. 提交 PR 将插件添加到对应分类文件

## 许可

[CC0 1.0 Universal](LICENSE)
