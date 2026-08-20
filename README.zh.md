# Awesome DeepSeek Harness (DSH) Plugin


[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


> [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）插件分类精选列表。


DeepSeek Harness 是 DeepSeek 开源的 agent harness——既是可直接运行的 Coding Agent，底层又是一套「一切皆插件」的框架。


**7411 个插件**，来自 GitHub 话题 [`dsh-plugin`](https://github.com/topics/dsh-plugin) · 欢迎 [PR](#贡献)


## 分类

| 分类 | 数量 | 说明 |

|------|------|------|

| 🎨 [UI 增强](categories/ui-enhancements.md) | 1756 | 增强 DSH Web/终端用户界面的插件。 |

| 🎭 [主题与外观](categories/themes-appearance.md) | 149 | DSH 皮肤、主题与外观定制。 |

| 💬 [会话与消息](categories/sessions-messages.md) | 814 | 会话管理、消息编辑、分享与对话工具。 |

| 🧠 [记忆](categories/memory.md) | 160 | 持久记忆、知识库与上下文保留插件。 |

| 🛠️ [工具与能力](categories/tools-capabilities.md) | 1773 | 视觉、浏览器、终端、SSH、Docker 等能力扩展。 |

| 🔁 [工作流与自动化](categories/workflow-automation.md) | 1917 | 自动化循环、定时任务、多智能体团队与工作流引擎。 |

| 🔔 [通知与集成](categories/notifications-integrations.md) | 9 | 微信、Telegram、IM 桥接、桌面通知与外部集成。 |

| 🔌 [模型与账号接入](categories/models-providers.md) | 28 | 多模型支持、OAuth 登录、LLM 回退策略与提供商桥接。 |

| 🧑‍💻 [开发与运行时](categories/development-runtime.md) | 27 | 插件管理器、SDK、CLI、桌面壳与开发者工具。 |

| 🔒 [安全与隐私](categories/security-privacy.md) | 2 | 凭证管理、加密、审计与安全工具。 |

| 🎮 [娱乐](categories/fun.md) | 6 | 游戏、桌宠、娱乐与趣味插件。 |

| 📋 [精选列表与合集](categories/awesome-lists.md) | 164 | DSH 插件精选列表与合集。 |

| ⚠️ [弱相关](categories/weakly-related.md) | 374 | 标记了 dsh-plugin 但关联性较弱的仓库——可能只是使用了 DeepSeek API 或关联松散。 |


## 精选插件


### 🎨 UI 增强

- [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) ⭐34944 — DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.
- [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐2461 — 开放的侧边栏底座，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/Git/子代理页面 ｜ Open sidebar foundation, supports third-party extensions to register new sidebar pages. Built-in file rendering/editing, terminal, Git, and sub-agent pages.
- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐2182 — DSH 官方公众号收录的 TUI 补位插件：Claude Code 风，鲸鱼顶栏/实时状态/流式思考/双击 Esc 回滚/上下文进度+TPS。npm 一键装。  DSH official WeChat featured TUI plugin — Claude Code style: whale bar, live status, streaming thoughts, double-Esc rollback, context bar + TPS. npm one-click.

▶️ [查看全部 1756 个插件 →](categories/ui-enhancements.md)


### 🎭 主题与外观

- [Small-tailqwq/dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐1511 — Whale Girl skin series for DeepSeek Harness. 适用于 DeepSeek Harness 的，鲸鱼娘系列皮肤。
- [MeteorNOX/DeepSeek-Balance-Whale-Widget](https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget) ⭐203 — DeepSeek Harness（DSH）一只住在 DSH 界面右下角的小鲸鱼娘，帮你盯着DeepSeek账户余额。QQ弹弹，支持拖拽吸附、左吸附翻转、数字滚动动画，随界面自动启用，建议直接喊来你的dsh安装
- [d-dev0101/open-sea-skin](https://github.com/d-dev0101/open-sea-skin) ⭐177 — WebGPU ocean skin for DeepSeek Harness — DSH plugin, Harness-only Chrome/Edge extension, static installer, and native integration.

▶️ [查看全部 149 个插件 →](categories/themes-appearance.md)


### 💬 会话与消息

- [MemTensor/MemOS](https://github.com/MemTensor/MemOS) ⭐10844 — Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support.
- [adoresever/graph-memory](https://github.com/adoresever/graph-memory) ⭐562 — Deepseek Harness、Openclaw知识图谱记忆插件。2026年4月受邀发布在清华大学讨论会。Knowledge Graph + Memory；Knowledge Graph Context Engine for OpenClaw — extracts structured triples from conversations, compresses context 75%, enables cross-session experience reuse
- [csyangwen/dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) ⭐195 — 为 DeepSeek Harness 带来「跨会话长期记忆 + 后台自我进化」能力的纯插件实现：五轨记忆 · git 分支感知 · 回合内自我审查 · 技能自我进化与技能管理器 · 四轨待办 · COI 调度 · 会话广播 · 会话搜索 · 提示词管理器 · 临时信息便签——零核心修改、零运行时依赖，随装随用、卸载即净。

▶️ [查看全部 814 个插件 →](categories/sessions-messages.md)


### 🧠 记忆

- [text2future/flowix](https://github.com/text2future/flowix) ⭐327 — Notes for you, Memory for your agents. / 内置 Deepseek harness Agent / 适用 办公 & 写作 & Coding
- [ZSeven-W/dsh-noema](https://github.com/ZSeven-W/dsh-noema) ⭐116 — Noema long-term memory plugin for DSH: durable, inspectable agent memory with recall tools and a settings page.
- [btspoony/mstar-harness](https://github.com/btspoony/mstar-harness) ⭐52 — An omni-plugin for harness engineering workflows with multi-agents, programmatic gates and skills.

▶️ [查看全部 160 个插件 →](categories/memory.md)


### 🛠️ 工具与能力

- [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) ⭐16347 — 为 DeepSeek Harness (DSH) 插件生态打造的现代化桌面端解决方案。万物皆「插件」，桌面本身也是「插件」。
- [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) ⭐4332 — A next-generation, source-available AI workspace with a self-evolving agent runtime for editable code, design, presentations, websites, and video—a Codex alternative that integrates DeepSeek Harness for subagent delegation, combining iPolloWork’s complete AI workbench with DSH’s specialized agents and both plugin ecosystems in one workflow.
- [liustack/modlens](https://github.com/liustack/modlens) ⭐3388 — The first vision plugin for DeepSeek Harness, and the vision bridge for every text-only coding agent. Paste an image, get structured JSON evidence (OCR, layout, semantics). | 全网最强 DeepSeek Harness 外挂视觉插件，为 DeepSeek、GLM 等纯文本模型外挂视觉能力，粘贴图片即得结构化 JSON 证据（OCR、版面、语义）。

▶️ [查看全部 1773 个插件 →](categories/tools-capabilities.md)


### 🔁 工作流与自动化

- [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) ⭐166722 — DeepSeek Harness: Everything is a Plugin.
- [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) ⭐12459 — Harness engineering beginner tutorial, from 0 to 1
- [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) ⭐2957 — 本地私有、开源的自进化跨平台 AI 内容发现 Agent：先理解你，再主动从 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等平台与开放 Web 寻找内容。（支持 deepseek harness 插件） | Local-first open-source cross-platform AI content discovery agent: understands you, then proactively finds content across Bilibili, Xiaohongshu, Douyin, YouTube, X, Zhihu, Reddit, Weibo and the open web.（support deepseek harness plugin）

▶️ [查看全部 1917 个插件 →](categories/workflow-automation.md)


### 🔔 通知与集成

- [gameswu/dsh-notifacation-frame](https://github.com/gameswu/dsh-notifacation-frame) ⭐4 — dsh通知消息统一管理框架
- [asakumizy/dsh-trae-bridge](https://github.com/asakumizy/dsh-trae-bridge) ⭐2 — DSH和trae连接
- [thuang3316/dsh-live-notify](https://github.com/thuang3316/dsh-live-notify) ⭐1 — DSH plugin for live notification

▶️ [查看全部 9 个插件 →](categories/notifications-integrations.md)


### 🔌 模型与账号接入

- [detpecca/dsh-llm-wiki](https://github.com/detpecca/dsh-llm-wiki) ⭐4
- [534119219/chicheng-stats](https://github.com/534119219/chicheng-stats) ⭐2 — DSH 全局用量统计插件：高度可配置侧边栏组件（文字/卡片）+ 统计面板（模型分布/趋势/首字节/耗时明细）
- [NLeRWantFly/dsh-HoldThatBigBlueFatFish](https://github.com/NLeRWantFly/dsh-HoldThatBigBlueFatFish) ⭐2 — 约束蓝色大肥鱼过度思考暂时的方案~模型测试opencode go实现

▶️ [查看全部 28 个插件 →](categories/models-providers.md)


### 🧑‍💻 开发与运行时

- [omdsh-dev/fabric](https://github.com/omdsh-dev/fabric) ⭐15 — 一种类似MC Fabric的dsh hook处理器
- [omdsh-dev/dsh-mygo](https://github.com/omdsh-dev/dsh-mygo) ⭐11
- [omdsh-dev/dsh-fun-ticker](https://github.com/omdsh-dev/dsh-fun-ticker) ⭐5 — DSH 行情跑马灯插件：可自选标的的加密/汇率/A股/指数/港美股跑马灯，免 key 数据源，宿主代理+缓存

▶️ [查看全部 27 个插件 →](categories/development-runtime.md)


### 🔒 安全与隐私

- [ravenli059/dsh-login](https://github.com/ravenli059/dsh-login) — 用于dsh-web加强安全性的插件，可设置用户名密码进行登录
- [Huauauaa/privacy](https://github.com/Huauauaa/privacy) — dsh-privacy-mask

▶️ [查看全部 2 个插件 →](categories/security-privacy.md)


### 🎮 娱乐

- [Gin-7/dsh-pet-remielle](https://github.com/Gin-7/dsh-pet-remielle) ⭐22
- [gameswu/dsh-pref-kit](https://github.com/gameswu/dsh-pref-kit) ⭐4 — 缓解部分dsh性能问题的插件
- [pk7j7sqryy-ops/dsh-token-pet](https://github.com/pk7j7sqryy-ops/dsh-token-pet) ⭐1 — DSH 动态 Cordis 插件：卡通用量小部件 + 天气/预报/预警（Token Pet 布布玩偶）

▶️ [查看全部 6 个插件 →](categories/fun.md)


### 📋 精选列表与合集

- [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐10613 — A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表
- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐5149 — Plugin and skin collection for DeepSeek Harness (DSH) Web UI - task board, git graph, right-side panel, remote mobile UI, pet, live token stats, and skin center.
- [AdamPlatin123/awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐1281 — DSH 插件雷达与精选榜：多路自动发现 9000+ 候选，容器真实安装路径运行级实测（四档判定），精选 Top 50 · 11 类人工策展，全量索引 PLUGINS-ALL.md，自动更新。

▶️ [查看全部 164 个插件 →](categories/awesome-lists.md)


### ⚠️ 弱相关


374 个标记了 `dsh-plugin` 但关联性较低的仓库。


▶️ [查看全部 374 个仓库 →](categories/weakly-related.md)


## 贡献


发现了一个应该收录的插件？欢迎提交 PR 或 Issue！


1. 确保你的仓库有 `dsh-plugin` 话题标签

2. 插件应声明 `dsh.bundle` manifest

3. 提交 PR 将插件添加到对应分类文件


## 许可


[CC0 1.0 Universal](LICENSE)
