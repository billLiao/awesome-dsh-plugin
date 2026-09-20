# Awesome DeepSeek Harness (DSH) Plugin


[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


> [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）插件分类精选列表。


🌐 **在线浏览**：[https://billliao.github.io/awesome-dsh-plugin/](https://billliao.github.io/awesome-dsh-plugin/) — 支持搜索与分类筛选


DeepSeek Harness 是 DeepSeek 开源的 agent harness——既是可直接运行的 Coding Agent，底层又是一套「一切皆插件」的框架。


**14214 个插件**，来自 GitHub 话题 [`dsh-plugin`](https://github.com/topics/dsh-plugin) · 欢迎 [PR](#贡献)


## 分类

| 分类 | 数量 | 说明 |
|------|------|------|
| 🎨 [UI 增强](categories/ui-enhancements.md) | 3606 | 增强 DSH Web/终端用户界面的插件。 |
| 🎭 [主题与外观](categories/themes-appearance.md) | 271 | DSH 皮肤、主题与外观定制。 |
| 💬 [会话与消息](categories/sessions-messages.md) | 1707 | 会话管理、消息编辑、分享与对话工具。 |
| 🧠 [记忆](categories/memory.md) | 314 | 持久记忆、知识库与上下文保留插件。 |
| 🛠️ [工具与能力](categories/tools-capabilities.md) | 3322 | 视觉、浏览器、终端、SSH、Docker 等能力扩展。 |
| 🔁 [工作流与自动化](categories/workflow-automation.md) | 3076 | 自动化循环、定时任务、多智能体团队与工作流引擎。 |
| 🔔 [通知与集成](categories/notifications-integrations.md) | 28 | 微信、Telegram、IM 桥接、桌面通知与外部集成。 |
| 🔌 [模型与账号接入](categories/models-providers.md) | 75 | 多模型支持、OAuth 登录、LLM 回退策略与提供商桥接。 |
| 🧑‍💻 [开发与运行时](categories/development-runtime.md) | 36 | 插件管理器、SDK、CLI、桌面壳与开发者工具。 |
| 🔒 [安全与隐私](categories/security-privacy.md) | 10 | 凭证管理、加密、审计与安全工具。 |
| 🎮 [娱乐](categories/fun.md) | 12 | 游戏、桌宠、娱乐与趣味插件。 |
| 📋 [精选列表与合集](categories/awesome-lists.md) | 291 | DSH 插件精选列表与合集。 |
| ⚠️ [弱相关](categories/weakly-related.md) | 989 | 标记了 dsh-plugin 但关联性较弱的仓库——可能只是使用了 DeepSeek API 或关联松散。 |

## 精选插件


### 🎨 UI 增强

- [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) ⭐35643 — DeepSeek-native AI coding agent for your terminal. Engineered around prefix-cache stability — leave it running.
- [zhu1090093659/dsh-web](https://github.com/zhu1090093659/dsh-web) ⭐7852 — DeepSeek Harness (DSH) Web 插件聚合生态 · 万物皆插件，通过创意工坊分发｜｜DeepSeek Harness (DSH) Web Plugin Aggregation Ecosystem · Everything is a plugin, distributed via the Creative Workshop
- [yjh051108/dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) ⭐7200 — dsh-routing-suite — injector + router-standard kit: install the runtime injector first, then the task-aware reasoning-mode router preset (measured P1-P23).

▶️ [查看全部 3606 个插件 →](categories/ui-enhancements.md)


### 🎭 主题与外观

- [MeteorNOX/DeepSeek-Balance-Whale-Widget](https://github.com/MeteorNOX/DeepSeek-Balance-Whale-Widget) ⭐2800 — DeepSeek Harness（DSH）一只住在 DSH 界面右下角的小鲸鱼娘，帮你盯着DeepSeek账户余额。QQ弹弹，支持拖拽吸附、左吸附翻转、数字滚动动画，随界面自动启用，建议直接喊来你的dsh安装
- [Small-tailqwq/dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) ⭐2154 — Whale Girl skin series for DeepSeek Harness. 适用于 DeepSeek Harness 的，鲸鱼娘系列皮肤。
- [kingOfSoySauce/dsh-skin-market](https://github.com/kingOfSoySauce/dsh-skin-market) ⭐150 — DeepSeek Harness skin market 皮肤市场 已收录200+DSH 皮肤 完善评分系统加人工审核，有便捷的社区收录入口；有在线页面方便在线浏览，也有插件方便管理本地皮肤

▶️ [查看全部 271 个插件 →](categories/themes-appearance.md)


### 💬 会话与消息

- [MemTensor/MemOS](https://github.com/MemTensor/MemOS) ⭐11461 — Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and cross-task skill reuse, with 35.24% token savings and DeepSeek Harness support.
- [adoresever/graph-memory](https://github.com/adoresever/graph-memory) ⭐608 — Deepseek Harness、Openclaw知识图谱记忆插件。2026年4月受邀发布在清华大学讨论会。Knowledge Graph + Memory；Knowledge Graph Context Engine for OpenClaw — extracts structured triples from conversations, compresses context 75%, enables cross-session experience reuse
- [vibeinging/dsh-desktop](https://github.com/vibeinging/dsh-desktop) ⭐589 — DeepSeek Harness Desktop App: a local AI desktop workspace for DSH Sessions, projects, files, web research, plugins, and Office artifacts.

▶️ [查看全部 1707 个插件 →](categories/sessions-messages.md)


### 🧠 记忆

- [text2future/flowix](https://github.com/text2future/flowix) ⭐415 — Notes for you, Memory for your agents. / 内置 Deepseek harness Agent / 适用 办公 & 写作 & Coding
- [seriousz158/dsh-memory](https://github.com/seriousz158/dsh-memory) ⭐180
- [ZSeven-W/dsh-noema](https://github.com/ZSeven-W/dsh-noema) ⭐129 — Noema long-term memory plugin for DSH: durable, inspectable agent memory with recall tools and a settings page.

▶️ [查看全部 314 个插件 →](categories/memory.md)


### 🛠️ 工具与能力

- [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop) ⭐28006 — 为 DeepSeek Harness (DSH) 插件生态打造的现代化桌面端解决方案。万物皆「插件」，桌面本身也是「插件」。
- [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) ⭐7985 — DSHDesktop：DeepSeek Harness Desktop / DeepSeek Harness 桌面版
- [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) ⭐6436 — Enterprise-grade, local-first Agent Workbench for people and agent teams. A unified multi-engine workspace for Codex Harness, DeepSeek Harness, and OpenCode, with unified plugins and Skills, multi-agent projects and tasks, and editable code, documents, presentations, design, and video.

▶️ [查看全部 3322 个插件 →](categories/tools-capabilities.md)


### 🔁 工作流与自动化

- [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) ⭐228468 — DeepSeek Harness: Everything is a Plugin.
- [walkinglabs/learn-harness-engineering](https://github.com/walkinglabs/learn-harness-engineering) ⭐14177 — Harness engineering beginner tutorial, from 0 to 1
- [dsh-market/dsh-market](https://github.com/dsh-market/dsh-market) ⭐4258 — The plugin market inside DeepSeek Harness — browse, search, one-click install · DSH 可视化插件市场

▶️ [查看全部 3076 个插件 →](categories/workflow-automation.md)


### 🔔 通知与集成

- [gameswu/dsh-notifacation-frame](https://github.com/gameswu/dsh-notifacation-frame) ⭐6 — dsh通知消息统一管理框架
- [minhdevtry/dsh-markdown-ide](https://github.com/minhdevtry/dsh-markdown-ide) ⭐5 — DSH Plugin for Markdown like Notion experience
- [bill9109/dsh-webbridge](https://github.com/bill9109/dsh-webbridge) ⭐4 — DSH 结合 Kimi WebBridge

▶️ [查看全部 28 个插件 →](categories/notifications-integrations.md)


### 🔌 模型与账号接入

- [HuanLinOTO/dsh-plugin-auto-blame](https://github.com/HuanLinOTO/dsh-plugin-auto-blame) ⭐11 — 模型回合结束后用 LLM 生成 3 条批判性跟进建议，点击即发送 | After a model turn, an LLM generates 3 critical follow-up suggestions shown as click-to-send chips
- [HuanLinOTO/dsh-plugin-d399](https://github.com/HuanLinOTO/dsh-plugin-d399) ⭐9 — 模型生成时右下角弹出小游戏菜单（Wordle/消消乐/192 款参数化小游戏，可拓展注册表） | Pops up a mini-game menu while the model generates (Wordle/Match-3/192 parametric mini-games, extensible registry)
- [licyer/dsh-token-monitor](https://github.com/licyer/dsh-token-monitor) ⭐7 — DSH Web 模型余量与用量监控插件

▶️ [查看全部 75 个插件 →](categories/models-providers.md)


### 🧑‍💻 开发与运行时

- [wzxaaaa/dsh-w-plugin-ecosystem](https://github.com/wzxaaaa/dsh-w-plugin-ecosystem) ⭐23 — 为dsh专属打造的贴近原生的自定义插件生态，支持插件可配置，独立协议，热拔插
- [omdsh-dev/stent](https://github.com/omdsh-dev/stent) ⭐19 — 灵感来源于MC Fabric的Cordis/DSH hook处理器
- [omdsh-dev/dsh-mygo](https://github.com/omdsh-dev/dsh-mygo) ⭐12

▶️ [查看全部 36 个插件 →](categories/development-runtime.md)


### 🔒 安全与隐私

- [simon300000/dsh-auto](https://github.com/simon300000/dsh-auto) ⭐7 — Auto Approve with Audit Agent
- [ravenli059/dsh-login](https://github.com/ravenli059/dsh-login) ⭐1 — 用于dsh-web加强安全性的插件，可设置用户名密码进行登录
- [tmpdot/dsh-audit-foundation](https://github.com/tmpdot/dsh-audit-foundation) ⭐1

▶️ [查看全部 10 个插件 →](categories/security-privacy.md)


### 🎮 娱乐

- [Gin-7/dsh-pet-remielle](https://github.com/Gin-7/dsh-pet-remielle) ⭐42
- [HuanLinOTO/dsh-plugin-anti-ads](https://github.com/HuanLinOTO/dsh-plugin-anti-ads) ⭐11 — DSH Web 广告拦截器，四层独立防御拦截 dsh-ads 插件的所有广告位 | DSH Web ad blocker with four independent defense layers targeting the dsh-ads plugin
- [gameswu/dsh-pref-kit](https://github.com/gameswu/dsh-pref-kit) ⭐5 — 缓解部分dsh性能问题的插件

▶️ [查看全部 12 个插件 →](categories/fun.md)


### 📋 精选列表与合集

- [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) ⭐16387 — A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表
- [AdamPlatin123/dsh-plugin-radar](https://github.com/AdamPlatin123/dsh-plugin-radar) ⭐1465 — DSH Plugin Radar — open-source ecosystem radar for DeepSeek Harness plugins: continuous discovery (21k+ candidates), k8s runtime validation (13k+ tests), 15-min snapshots; the catalog is a generated artifact — 开源 DSH 插件生态雷达：持续发现 2.1 万+ 候选、k8s 运行级实测 1.3 万+、15 分钟快照；插件目录为自动生成的产物
- [0xsline/awesome-deepseek-harness](https://github.com/0xsline/awesome-deepseek-harness) ⭐1074 — DeepSeek Harness (DSH) ecosystem: curated plugins, tools, and infrastructure from dsh-external/hub and the public dsh-plugin topic.

▶️ [查看全部 291 个插件 →](categories/awesome-lists.md)


### ⚠️ 弱相关


989 个标记了 `dsh-plugin` 但关联性较低的仓库。


▶️ [查看全部 989 个仓库 →](categories/weakly-related.md)


## 数据


原始仓库数据按分类拆分存储在 `data/raw/<分类>/part-NNN.json`（每个分片上限 10 MB，大分类自动拆分为多个分片）。`data/plugins.json` 保存用于生成分类页面的分类汇总。


## 贡献


发现了一个应该收录的插件？欢迎提交 PR 或 Issue！


1. 确保你的仓库有 `dsh-plugin` 话题标签

2. 插件应声明 `dsh.bundle` manifest

3. 提交 PR 将插件添加到对应分类文件


## 许可


[CC0 1.0 Universal](LICENSE)
