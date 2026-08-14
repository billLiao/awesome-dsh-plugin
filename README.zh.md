# Awesome DeepSeek Harness (DSH) Plugin


[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


> [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）插件分类精选列表。


DeepSeek Harness 是 DeepSeek 开源的 agent harness——既是可直接运行的 Coding Agent，底层又是一套「一切皆插件」的框架。


**924 个插件**，来自 GitHub 话题 [`dsh-plugin`](https://github.com/topics/dsh-plugin) · 欢迎 [PR](#贡献)


## 分类

| 分类 | 数量 | 说明 |

|------|------|------|

| 🎨 [UI 增强](categories/ui-enhancements.md) | 281 | 增强 DSH Web/终端用户界面的插件。 |

| 🎭 [主题与外观](categories/themes-appearance.md) | 22 | DSH 皮肤、主题与外观定制。 |

| 💬 [会话与消息](categories/sessions-messages.md) | 115 | 会话管理、消息编辑、分享与对话工具。 |

| 🧠 [记忆](categories/memory.md) | 26 | 持久记忆、知识库与上下文保留插件。 |

| 🛠️ [工具与能力](categories/tools-capabilities.md) | 257 | 视觉、浏览器、终端、SSH、Docker 等能力扩展。 |

| 🔁 [工作流与自动化](categories/workflow-automation.md) | 145 | 自动化循环、定时任务、多智能体团队与工作流引擎。 |

| 🔔 [通知与集成](categories/notifications-integrations.md) | 3 | 微信、Telegram、IM 桥接、桌面通知与外部集成。 |

| 🔌 [模型与账号接入](categories/models-providers.md) | 8 | 多模型支持、OAuth 登录、LLM 回退策略与提供商桥接。 |

| 🧑‍💻 [开发与运行时](categories/development-runtime.md) | 8 | 插件管理器、SDK、CLI、桌面壳与开发者工具。 |

| 🎮 [娱乐](categories/fun.md) | 1 | 游戏、桌宠、娱乐与趣味插件。 |

| 📋 [精选列表与合集](categories/awesome-lists.md) | 32 | DSH 插件精选列表与合集。 |


## 精选插件


### 🎨 UI 增强

- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐698 — 解决DSH 官方尚无终端 TUI 痛点的补位之作，献给偏爱cli的各位极客：Claude Code 风格全屏交互终端插件——像素鲸鱼顶栏、实时工作状态行、思考流式展开、双击 Esc 回滚、上下文进度条 + TPS 仪表。npm 一键安装。
- [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐606 — 一个侧边栏的完整工作台，支持三方拓展注册新Tab页面，内置文件渲染编辑/终端/Git/子代理
- [alaliqing/claude-paper](https://github.com/alaliqing/claude-paper) ⭐291 — 📖 Cross-agent research paper toolkit for Claude Code, Codex, OpenCode, and DeepSeek Harness—quick summaries, deep study materials, code demos, and a local web viewer.

▶️ [查看全部 281 个插件 →](categories/ui-enhancements.md)


### 🎭 主题与外观

- [Small-tailqwq/dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐435 — DSH Web 鲸鱼娘皮肤系列(深海女仆工坊 maid-atelier)——CC BY-NC-SA 4.0
- [suzike/freestyle-dsh-theme](https://github.com/suzike/freestyle-dsh-theme) ⭐9 — DeepSeek Harness 主题体验插件：OKLCH 主题提案 + 主题设计器（跨重启持久化）
- [lglglglgy/dsh-whale-pet](https://github.com/lglglglgy/dsh-whale-pet) ⭐2 — dsh-whale-pet

▶️ [查看全部 22 个插件 →](categories/themes-appearance.md)


### 💬 会话与消息

- [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) ⭐571 — Open-source CMA-compatible agent runtime for any model, with MCP tools, sandboxed sessions, audit, replay, and a local console. Includes a native DeepSeek Harness bundle over stdio MCP.
- [Anionex/dsh-turn-rewind](https://github.com/Anionex/dsh-turn-rewind) ⭐34 — deepseek harness对话和代码状态回退插件 | DSH — rewind conversation and workspace state, powered by a persistent Change Ledger
- [hikariming/dshfind](https://github.com/hikariming/dshfind) ⭐31 — DSH (DeepSeek Harness) 原理学习、插件市场与最佳实践 · Learn DSH principles, plugin marketplace & best practices

▶️ [查看全部 115 个插件 →](categories/sessions-messages.md)


### 🧠 记忆

- [btspoony/mstar-harness](https://github.com/btspoony/mstar-harness) ⭐42 — A Skill-driven Harness/Loop Engineering Workflow Agent Plugin
- [omdsh-dev/dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) ⭐8 — Mnemon 与 DSH 的深度集成插件，为 DSH 提供完备的本地记忆系统：运行时记忆、可检索档案与受监督记忆体。
- [modusensus/dsh-mneme](https://github.com/modusensus/dsh-mneme) ⭐8 — Mneme——把记忆主权还给人的记忆插件：SQLite + 可人工编辑的 Markdown 双写，autoDream 在梦境中巩固记忆，140 个测试护航。

▶️ [查看全部 26 个插件 →](categories/memory.md)


### 🛠️ 工具与能力

- [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) ⭐3842 — A next-generation, source-available AI workspace with a self-evolving agent runtime for editable code, design, presentations, websites, and video—a Codex alternative that integrates DeepSeek Harness for subagent delegation, combining iPolloWork’s complete AI workbench with DSH’s specialized agents and both plugin ecosystems in one workflow.
- [liustack/modlens](https://github.com/liustack/modlens) ⭐1055 — The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics). | 全网第一个 DeepSeek Harness 视觉插件，为 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义）。
- [PM-Shawn/Abu-Cowork](https://github.com/PM-Shawn/Abu-Cowork) ⭐321 — Open-source alternative to Claude Cowork — a local-first AI agent desktop app · multi-model · self-evolving skills · privacy-first · multi-Harness roadmap · DeepSeek Harness integration in progress

▶️ [查看全部 257 个插件 →](categories/tools-capabilities.md)


### 🔁 工作流与自动化

- [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2260 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）
- [yejiming/MuseAI](https://github.com/yejiming/MuseAI) ⭐535 — 创建你的 AI 角色，进入你的故事世界。和角色聊天、冒险、穿书，让每一次互动都留下羁绊（支持 DeepSeek Harness 插件，欢迎使用）
- [NanmiCoder/dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) ⭐204 — AgentTeams plugin for DeepSeek Harness

▶️ [查看全部 145 个插件 →](categories/workflow-automation.md)


### 🔔 通知与集成

- [bill9109/dsh-webbridge](https://github.com/bill9109/dsh-webbridge) ⭐3 — DSH 结合 Kimi WebBridge
- [hellosz/dsh-ntfy](https://github.com/hellosz/dsh-ntfy)
- [zbxzbx98/dsh-peak-alert](https://github.com/zbxzbx98/dsh-peak-alert) — DeepSeek 峰谷定价提示插件（DSH Web 客户端插件，纯前端，无后端依赖）

▶️ [查看全部 3 个插件 →](categories/notifications-integrations.md)


### 🔌 模型与账号接入

- [HuanLinOTO/dsh-plugin-d399](https://github.com/HuanLinOTO/dsh-plugin-d399) ⭐4 — 模型生成时右下角弹出小游戏菜单（Wordle/消消乐/192 款参数化小游戏，可拓展注册表） | Pops up a mini-game menu while the model generates (Wordle/Match-3/192 parametric mini-games, extensible registry)
- [detpecca/dsh-llm-wiki](https://github.com/detpecca/dsh-llm-wiki) ⭐3
- [benzhoupo/dsh-dardar](https://github.com/benzhoupo/dsh-dardar) ⭐2 — DSH 插件：在模型选择框左侧显示当前 DeepSeek V4 Pro / V4 Flash 的 codexradar IQ，每 5 分钟刷新（CC BY 4.0）

▶️ [查看全部 8 个插件 →](categories/models-providers.md)


### 🧑‍💻 开发与运行时

- [multica-ai/dsh-multica-runtime](https://github.com/multica-ai/dsh-multica-runtime) ⭐27 — Support dsh runtime on Multica.
- [omdsh-dev/dsh-mygo](https://github.com/omdsh-dev/dsh-mygo) ⭐5
- [ophielel/dsh-devkit](https://github.com/ophielel/dsh-devkit) ⭐1

▶️ [查看全部 8 个插件 →](categories/development-runtime.md)


### 🎮 娱乐

- [HuanLinOTO/dsh-plugin-anti-ads](https://github.com/HuanLinOTO/dsh-plugin-anti-ads) ⭐3 — DSH Web 广告拦截器，四层独立防御拦截 dsh-ads 插件的所有广告位 | DSH Web ad blocker with four independent defense layers targeting the dsh-ads plugin

▶️ [查看全部 1 个插件 →](categories/fun.md)


### 📋 精选列表与合集

- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐1484 — Plugin and skin collection for DeepSeek Harness (DSH) Web UI - task board, git graph, right-side panel, remote mobile UI, pet, live token stats, and skin center.
- [AdamPlatin123/awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐654 — 前部索引仓库（Radar）：自动扫描发现的所有 dsh 插件候选；经测试合格的将移入后序精选目录仓库
- [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐588 — A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表

▶️ [查看全部 32 个插件 →](categories/awesome-lists.md)


## 贡献


发现了一个应该收录的插件？欢迎提交 PR 或 Issue！


1. 确保你的仓库有 `dsh-plugin` 话题标签

2. 插件应声明 `dsh.bundle` manifest

3. 提交 PR 将插件添加到对应分类文件


## 许可


[CC0 1.0 Universal](LICENSE)
