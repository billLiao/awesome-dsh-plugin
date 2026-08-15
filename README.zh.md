# Awesome DeepSeek Harness (DSH) Plugin


[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


> [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）插件分类精选列表。


DeepSeek Harness 是 DeepSeek 开源的 agent harness——既是可直接运行的 Coding Agent，底层又是一套「一切皆插件」的框架。


**994 个插件**，来自 GitHub 话题 [`dsh-plugin`](https://github.com/topics/dsh-plugin) · 欢迎 [PR](#贡献)


## 分类

| 分类 | 数量 | 说明 |

|------|------|------|

| 🎨 [UI 增强](categories/ui-enhancements.md) | 285 | 增强 DSH Web/终端用户界面的插件。 |

| 🎭 [主题与外观](categories/themes-appearance.md) | 30 | DSH 皮肤、主题与外观定制。 |

| 💬 [会话与消息](categories/sessions-messages.md) | 116 | 会话管理、消息编辑、分享与对话工具。 |

| 🧠 [记忆](categories/memory.md) | 20 | 持久记忆、知识库与上下文保留插件。 |

| 🛠️ [工具与能力](categories/tools-capabilities.md) | 248 | 视觉、浏览器、终端、SSH、Docker 等能力扩展。 |

| 🔁 [工作流与自动化](categories/workflow-automation.md) | 140 | 自动化循环、定时任务、多智能体团队与工作流引擎。 |

| 🔔 [通知与集成](categories/notifications-integrations.md) | 2 | 微信、Telegram、IM 桥接、桌面通知与外部集成。 |

| 🔌 [模型与账号接入](categories/models-providers.md) | 6 | 多模型支持、OAuth 登录、LLM 回退策略与提供商桥接。 |

| 🧑‍💻 [开发与运行时](categories/development-runtime.md) | 2 | 插件管理器、SDK、CLI、桌面壳与开发者工具。 |

| 🎮 [娱乐](categories/fun.md) | 1 | 游戏、桌宠、娱乐与趣味插件。 |

| 📋 [精选列表与合集](categories/awesome-lists.md) | 55 | DSH 插件精选列表与合集。 |

| ⚠️ [弱相关](categories/weakly-related.md) | 61 | 标记了 dsh-plugin 但关联性较弱的仓库——可能只是使用了 DeepSeek API 或关联松散。 |


## 精选插件


### 🎨 UI 增强

- [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) ⭐1106 — 解决DSH 官方尚无终端 TUI 痛点的补位之作，献给偏爱cli的各位极客：Claude Code 风格全屏交互终端插件——像素鲸鱼顶栏、实时工作状态行、思考流式展开、双击 Esc 回滚、上下文进度条 + TPS 仪表。npm 一键安装。
- [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) ⭐974 — 一个侧边栏的完整工作台，支持三方拓展注册新侧边栏页面。内置文件渲染编辑/终端/Git/子代理
- [Electricitysheep/dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) ⭐261 — DeepSeek Harness (dsh) 从 0 到 1 深度手册：安装/插件开发/性能调优/实测案例/同模型多 Agent 实测对比（中文 + 英文 PDF）

▶️ [查看全部 285 个插件 →](categories/ui-enhancements.md)


### 🎭 主题与外观

- [Small-tailqwq/dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐790 — DSH Web 鲸鱼娘皮肤系列(深海女仆工坊 maid-atelier)——CC BY-NC-SA 4.0
- [LaplaceYoung/dsh-qq2006](https://github.com/LaplaceYoung/dsh-qq2006) ⭐10 — DSH (DeepSeek Harness) 的 QQ2006 皮肤插件：注册 qq2006 主题、镜像 body[data-ds-skin]、全局皮肤表与完整素材
- [SenmuuuuW/dsh-whale-report](https://github.com/SenmuuuuW/dsh-whale-report) ⭐9 — 🐋 鲸鱼记事本 — 你的 Agent 年度报告：从会话事件日志生成日报/周报/月报/年报，任意区间、只读不改写

▶️ [查看全部 30 个插件 →](categories/themes-appearance.md)


### 💬 会话与消息

- [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) ⭐584 — Open-source CMA-compatible agent runtime for any model, with MCP tools, sandboxed sessions, audit, replay, and a local console. Includes a native DeepSeek Harness bundle over stdio MCP.
- [vibeinging/deepseek-harness-desktop-app](https://github.com/vibeinging/deepseek-harness-desktop-app) ⭐114 — DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.
- [hikariming/dshfind](https://github.com/hikariming/dshfind) ⭐79 — DSH (DeepSeek Harness) 原理学习、插件市场与最佳实践 · Learn DSH principles, plugin marketplace & best practices

▶️ [查看全部 116 个插件 →](categories/sessions-messages.md)


### 🧠 记忆

- [btspoony/mstar-harness](https://github.com/btspoony/mstar-harness) ⭐45 — A Skill-driven Harness/Loop Engineering Workflow Agent Plugin
- [zhujunpeng12/dsh-memory-system](https://github.com/zhujunpeng12/dsh-memory-system) ⭐6 — Local-first persistent memory infrastructure for DeepSeek Harness: hot bootstrap, Chinese-BM25 cold recall, lease-lock transactional writes, read-only governance
- [limbo947/dsh-recall-plugin](https://github.com/limbo947/dsh-recall-plugin) ⭐5 — DSH 消息撤回插件：回到发送该消息时的状态

▶️ [查看全部 20 个插件 →](categories/memory.md)


### 🛠️ 工具与能力

- [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) ⭐4184 — 为 DeepSeek Harness (DSH) 生态打造的现代化桌面端体验
- [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) ⭐4083 — A next-generation, source-available AI workspace with a self-evolving agent runtime for editable code, design, presentations, websites, and video—a Codex alternative that integrates DeepSeek Harness for subagent delegation, combining iPolloWork’s complete AI workbench with DSH’s specialized agents and both plugin ecosystems in one workflow.
- [xiaobright/dsh-anchored-standard](https://github.com/xiaobright/dsh-anchored-standard) ⭐1614 — Two-phase DeepSeek Harness preset: Minimal-aligned bootstrap, then full Standard tools (Project2 98/99)

▶️ [查看全部 248 个插件 →](categories/tools-capabilities.md)


### 🔁 工作流与自动化

- [NanmiCoder/dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) ⭐298 — AgentTeams plugin for DeepSeek Harness
- [dsh-market/dsh-market](https://github.com/dsh-market/dsh-market) ⭐192 — The plugin market inside DeepSeek Harness — browse, search, one-click install · DSH 可视化插件市场
- [LaplaceYoung/oh-my-dsh](https://github.com/LaplaceYoung/oh-my-dsh) ⭐45 — oh-my-dsh：面向 DSH (DeepSeek Harness) 的插件生态——700+ 插件，只通过扩展接缝注册，不修改 agent-loop 骨架

▶️ [查看全部 140 个插件 →](categories/workflow-automation.md)


### 🔔 通知与集成

- [Zyy1997/dsh-sound-notify](https://github.com/Zyy1997/dsh-sound-notify) ⭐1 — dsh plugin: play a sound on the host when an agent finishes its turn or waits for approval
- [CACppuccino/dsh-multiagent-enhence](https://github.com/CACppuccino/dsh-multiagent-enhence)

▶️ [查看全部 2 个插件 →](categories/notifications-integrations.md)


### 🔌 模型与账号接入

- [HuanLinOTO/dsh-plugin-d399](https://github.com/HuanLinOTO/dsh-plugin-d399) ⭐5 — 模型生成时右下角弹出小游戏菜单（Wordle/消消乐/192 款参数化小游戏，可拓展注册表） | Pops up a mini-game menu while the model generates (Wordle/Match-3/192 parametric mini-games, extensible registry)
- [omdsh-dev/dsh-llm-fallbacks](https://github.com/omdsh-dev/dsh-llm-fallbacks) ⭐4 — An dsh plugin for role-based LLM retry&fallback strategy. 基于角色的模型重试备用策略插件
- [NLeRWantFly/dsh-HoldThatBigBlueFatFish](https://github.com/NLeRWantFly/dsh-HoldThatBigBlueFatFish) ⭐2 — 约束蓝色大肥鱼过度思考暂时的方案~模型测试opencode go实现

▶️ [查看全部 6 个插件 →](categories/models-providers.md)


### 🧑‍💻 开发与运行时

- [healing1/dsh-web-plugin-manager](https://github.com/healing1/dsh-web-plugin-manager)
- [V-dev-388/dsh-plugin-hello](https://github.com/V-dev-388/dsh-plugin-hello)

▶️ [查看全部 2 个插件 →](categories/development-runtime.md)


### 🎮 娱乐

- [Gin-7/dsh-pet-remielle](https://github.com/Gin-7/dsh-pet-remielle)

▶️ [查看全部 1 个插件 →](categories/fun.md)


### 📋 精选列表与合集

- [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐2376 — Plugin and skin collection for DeepSeek Harness (DSH) Web UI - task board, git graph, right-side panel, remote mobile UI, pet, live token stats, and skin center.
- [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐2274 — A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表
- [AdamPlatin123/awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) ⭐926 — 前部索引仓库（Radar）：自动扫描发现的所有 dsh 插件候选；经测试合格的将移入后序精选目录仓库

▶️ [查看全部 55 个插件 →](categories/awesome-lists.md)


### ⚠️ 弱相关


61 个标记了 `dsh-plugin` 但关联性较低的仓库。


▶️ [查看全部 61 个仓库 →](categories/weakly-related.md)


## 贡献


发现了一个应该收录的插件？欢迎提交 PR 或 Issue！


1. 确保你的仓库有 `dsh-plugin` 话题标签

2. 插件应声明 `dsh.bundle` manifest

3. 提交 PR 将插件添加到对应分类文件


## 许可


[CC0 1.0 Universal](LICENSE)
