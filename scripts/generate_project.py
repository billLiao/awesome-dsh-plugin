#!/usr/bin/env python3
"""Generate awesome-dsh-plugin project files."""
import json
import os

# Load categorized data
with open('/tmp/plugins_categorized.json') as f:
    data = json.load(f)

PROJECT_DIR = '/root/.nanobot/workspace/awesome-dsh-plugin'

cat_order = [
    'ui-enhancements', 'themes-appearance', 'sessions-messages', 'memory',
    'tools-capabilities', 'workflow-automation', 'notifications-integrations',
    'models-providers', 'development-runtime', 'security-privacy',
    'fun', 'awesome-lists',
]

weakly_related_cat = 'weakly-related'

cat_info = {
    'ui-enhancements': {
        'name': 'UI Enhancements', 'name_zh': 'UI 增强',
        'icon': '🎨', 'desc': 'Plugins that enhance the DSH web/terminal user interface.',
        'desc_zh': '增强 DSH Web/终端用户界面的插件。',
    },
    'themes-appearance': {
        'name': 'Themes & Appearance', 'name_zh': '主题与外观',
        'icon': '🎭', 'desc': 'Skins, themes, and appearance customization for DSH.',
        'desc_zh': 'DSH 皮肤、主题与外观定制。',
    },
    'sessions-messages': {
        'name': 'Sessions & Messages', 'name_zh': '会话与消息',
        'icon': '💬', 'desc': 'Session management, message editing, sharing, and conversation tools.',
        'desc_zh': '会话管理、消息编辑、分享与对话工具。',
    },
    'memory': {
        'name': 'Memory', 'name_zh': '记忆',
        'icon': '🧠', 'desc': 'Persistent memory, knowledge bases, and context retention plugins.',
        'desc_zh': '持久记忆、知识库与上下文保留插件。',
    },
    'tools-capabilities': {
        'name': 'Tools & Capabilities', 'name_zh': '工具与能力',
        'icon': '🛠️', 'desc': 'Vision, browser, terminal, SSH, Docker, and other capability extensions.',
        'desc_zh': '视觉、浏览器、终端、SSH、Docker 等能力扩展。',
    },
    'workflow-automation': {
        'name': 'Workflow & Automation', 'name_zh': '工作流与自动化',
        'icon': '🔁', 'desc': 'Automation loops, scheduled tasks, multi-agent teams, and workflow engines.',
        'desc_zh': '自动化循环、定时任务、多智能体团队与工作流引擎。',
    },
    'notifications-integrations': {
        'name': 'Notifications & Integrations', 'name_zh': '通知与集成',
        'icon': '🔔', 'desc': 'WeChat, Telegram, IM bridges, desktop notifications, and external integrations.',
        'desc_zh': '微信、Telegram、IM 桥接、桌面通知与外部集成。',
    },
    'models-providers': {
        'name': 'Models & Providers', 'name_zh': '模型与账号接入',
        'icon': '🔌', 'desc': 'Multi-model support, OAuth login, LLM fallback strategies, and provider bridges.',
        'desc_zh': '多模型支持、OAuth 登录、LLM 回退策略与提供商桥接。',
    },
    'development-runtime': {
        'name': 'Development & Runtime', 'name_zh': '开发与运行时',
        'icon': '🧑‍💻', 'desc': 'Plugin managers, SDKs, CLIs, desktop wrappers, and developer tooling.',
        'desc_zh': '插件管理器、SDK、CLI、桌面壳与开发者工具。',
    },
    'security-privacy': {
        'name': 'Security & Privacy', 'name_zh': '安全与隐私',
        'icon': '🔒', 'desc': 'Credential management, encryption, audit, and security tooling.',
        'desc_zh': '凭证管理、加密、审计与安全工具。',
    },
    'fun': {
        'name': 'Just for Fun', 'name_zh': '娱乐',
        'icon': '🎮', 'desc': 'Games, pets, entertainment, and playful plugins.',
        'desc_zh': '游戏、桌宠、娱乐与趣味插件。',
    },
    'awesome-lists': {
        'name': 'Awesome Lists & Collections', 'name_zh': '精选列表与合集',
        'icon': '📋', 'desc': 'Curated collections and awesome lists of DSH plugins.',
        'desc_zh': 'DSH 插件精选列表与合集。',
    },
    'weakly-related': {
        'name': 'Weakly Related', 'name_zh': '弱相关',
        'icon': '⚠️', 'desc': 'Repositories tagged dsh-plugin but with weak relevance signals — may use DeepSeek API or have loose association.',
        'desc_zh': '标记了 dsh-plugin 但关联性较弱的仓库——可能只是使用了 DeepSeek API 或关联松散。',
    },
}

def generate_category_md(cat_key):
    """Generate a category markdown file."""
    plugins = data['categories'].get(cat_key, [])
    info = cat_info[cat_key]

    lines = []
    lines.append(f"# {info['icon']} {info['name']}\n")
    lines.append(f"\n> {info['desc']}\n")
    lines.append(f"\n**{len(plugins)} plugins**\n")
    lines.append("\n---\n")

    for p in plugins:
        desc = p['description'].strip()
        stars = p['stars']
        star_badge = f" ⭐{stars}" if stars > 0 else ""
        if desc:
            lines.append(f"- [{p['full_name']}]({p['url']}){star_badge} — {desc}")
        else:
            lines.append(f"- [{p['full_name']}]({p['url']}){star_badge}")

    lines.append("\n---\n")
    lines.append(f"\n*Generated on {data['meta']['generated_at']} · {len(plugins)} plugins in this category*\n")

    return '\n'.join(lines)

def generate_readme():
    """Generate the main README.md."""
    lines = []
    lines.append("# Awesome DeepSeek Harness (DSH) Plugin\n")
    lines.append("\n[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n")
    lines.append("\n> A categorized curated list of plugins for [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (`dsh`).\n")
    lines.append("\n🌐 **Browse online**: [https://billliao.github.io/awesome-dsh-plugin/](https://billliao.github.io/awesome-dsh-plugin/) — search & filter all plugins\n")
    lines.append("\nDeepSeek Harness is DeepSeek's open-source agent harness — a runnable coding agent (Web and headless), built on a framework where everything is a plugin: models, tools, sandboxes, session storage, UI, even the agent loop itself.\n")
    lines.append(f"\n**{data['meta']['total_plugins']} plugins** collected from GitHub topic [`dsh-plugin`](https://github.com/topics/dsh-plugin) · [PRs welcome](#contributing)\n")
    lines.append("\n## Categories\n")

    # Category overview table
    lines.append("| Category | Count | Description |")
    lines.append("|----------|-------|-------------|")
    all_cats = cat_order + ([weakly_related_cat] if weakly_related_cat in data['categories'] else [])
    for cat in all_cats:
        if cat in data['categories']:
            plugins = data['categories'][cat]
            info = cat_info[cat]
            count = len(plugins)
            filename = f"categories/{cat}.md"
            lines.append(f"| {info['icon']} [{info['name']}]({filename}) | {count} | {info['desc']} |")

    lines.append("\n## Featured Plugins\n")
    lines.append("\nA selection of notable plugins by category:\n")

    for cat in cat_order:
        if cat not in data['categories']:
            continue
        plugins = data['categories'][cat]
        if not plugins:
            continue
        info = cat_info[cat]
        filename = f"categories/{cat}.md"

        lines.append(f"\n### {info['icon']} {info['name']}\n")

        # Show top 3 by stars
        top = plugins[:3]
        for p in top:
            desc = p['description'].strip()
            stars = p['stars']
            star_str = f" ⭐{stars}" if stars > 0 else ""
            if desc:
                lines.append(f"- [{p['full_name']}]({p['url']}){star_str} — {desc}")
            else:
                lines.append(f"- [{p['full_name']}]({p['url']}){star_str}")

        lines.append(f"\n▶️ [View all {len(plugins)} plugins →]({filename})\n")

    # Also show weakly-related if present
    if weakly_related_cat in data['categories']:
        weak = data['categories'][weakly_related_cat]
        lines.append(f"\n### ⚠️ Weakly Related\n")
        lines.append(f"\n{len(weak)} repositories tagged `dsh-plugin` but with low relevance confidence.\n")
        lines.append(f"\n▶️ [View all {len(weak)} repos →](categories/{weakly_related_cat}.md)\n")

    lines.append("\n## Data\n")
    lines.append("\nThe raw repository store is split by category under `data/raw/<category>/part-NNN.json` (each shard capped at 10 MB; large categories span multiple parts). `data/plugins.json` holds the categorized summary used to generate the category pages.\n")

    lines.append("\n## Contributing\n")
    lines.append("\nFound a plugin that should be here? Open a PR or issue!\n")
    lines.append("\n1. Ensure your repo has the `dsh-plugin` topic on GitHub\n")
    lines.append("2. The plugin should declare a `dsh.bundle` manifest\n")
    lines.append("3. Submit a PR adding it to the appropriate category file\n")
    lines.append("\n## License\n")
    lines.append("\n[CC0 1.0 Universal](LICENSE)\n")

    return '\n'.join(lines)

def generate_readme_zh(): 
    """Generate Chinese README.zh.md."""
    lines = []
    lines.append("# Awesome DeepSeek Harness (DSH) Plugin\n")
    lines.append("\n[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n")
    lines.append("\n> [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）插件分类精选列表。\n")
    lines.append("\n🌐 **在线浏览**：[https://billliao.github.io/awesome-dsh-plugin/](https://billliao.github.io/awesome-dsh-plugin/) — 支持搜索与分类筛选\n")
    lines.append("\nDeepSeek Harness 是 DeepSeek 开源的 agent harness——既是可直接运行的 Coding Agent，底层又是一套「一切皆插件」的框架。\n")
    lines.append(f"\n**{data['meta']['total_plugins']} 个插件**，来自 GitHub 话题 [`dsh-plugin`](https://github.com/topics/dsh-plugin) · 欢迎 [PR](#贡献)\n")
    lines.append("\n## 分类\n")

    lines.append("| 分类 | 数量 | 说明 |")
    lines.append("|------|------|------|")
    all_cats = cat_order + ([weakly_related_cat] if weakly_related_cat in data['categories'] else [])
    for cat in all_cats:
        if cat in data['categories']:
            plugins = data['categories'][cat]
            info = cat_info[cat]
            count = len(plugins)
            filename = f"categories/{cat}.md"
            lines.append(f"| {info['icon']} [{info['name_zh']}]({filename}) | {count} | {info['desc_zh']} |")

    lines.append("\n## 精选插件\n")

    for cat in cat_order:
        if cat not in data['categories']:
            continue
        plugins = data['categories'][cat]
        if not plugins:
            continue
        info = cat_info[cat]
        filename = f"categories/{cat}.md"

        lines.append(f"\n### {info['icon']} {info['name_zh']}\n")

        top = plugins[:3]
        for p in top:
            desc = p['description'].strip()
            stars = p['stars']
            star_str = f" ⭐{stars}" if stars > 0 else ""
            if desc:
                lines.append(f"- [{p['full_name']}]({p['url']}){star_str} — {desc}")
            else:
                lines.append(f"- [{p['full_name']}]({p['url']}){star_str}")

        lines.append(f"\n▶️ [查看全部 {len(plugins)} 个插件 →]({filename})\n")

    # Also show weakly-related if present
    if weakly_related_cat in data['categories']:
        weak = data['categories'][weakly_related_cat]
        lines.append(f"\n### ⚠️ 弱相关\n")
        lines.append(f"\n{len(weak)} 个标记了 `dsh-plugin` 但关联性较低的仓库。\n")
        lines.append(f"\n▶️ [查看全部 {len(weak)} 个仓库 →](categories/{weakly_related_cat}.md)\n")

    lines.append("\n## 数据\n")
    lines.append("\n原始仓库数据按分类拆分存储在 `data/raw/<分类>/part-NNN.json`（每个分片上限 10 MB，大分类自动拆分为多个分片）。`data/plugins.json` 保存用于生成分类页面的分类汇总。\n")

    lines.append("\n## 贡献\n")
    lines.append("\n发现了一个应该收录的插件？欢迎提交 PR 或 Issue！\n")
    lines.append("\n1. 确保你的仓库有 `dsh-plugin` 话题标签\n")
    lines.append("2. 插件应声明 `dsh.bundle` manifest\n")
    lines.append("3. 提交 PR 将插件添加到对应分类文件\n")
    lines.append("\n## 许可\n")
    lines.append("\n[CC0 1.0 Universal](LICENSE)\n")

    return '\n'.join(lines)

def generate_contributing(): 
    lines = []
    lines.append("""# Contributing

Contributions are welcome! Here's how to add a plugin:

1. **Ensure your repo has the `dsh-plugin` topic** on GitHub
2. **The plugin should declare a `dsh.bundle` manifest** (so it's installable via `dsh plugin add`)
3. **Find the right category** in `categories/` and add your plugin entry
4. **Submit a Pull Request**

## Format

Each plugin entry follows this format:

```
- [owner/repo](url) — Description of what the plugin does.
```

If the entry already exists in the wrong category, open an issue instead.

## Categories

| Category | File |
|----------|------|
""")

    all_cats = cat_order + ([weakly_related_cat] if weakly_related_cat in data['categories'] else [])
    for cat in all_cats:
        if cat in data['categories']:
            info = cat_info[cat]
            lines.append(f"| {info['icon']} {info['name']} | `categories/{cat}.md` |\n")

    lines.append("""
## Not sure which category?

Open an issue and we'll help categorize it.
""")
    return ''.join(lines)

# Generate all files
os.makedirs(f'{PROJECT_DIR}/categories', exist_ok=True)
os.makedirs(f'{PROJECT_DIR}/scripts', exist_ok=True)
os.makedirs(f'{PROJECT_DIR}/data', exist_ok=True)

# Save plugins data
with open(f'{PROJECT_DIR}/data/plugins.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Generate category files
all_cats = cat_order + ([weakly_related_cat] if weakly_related_cat in data['categories'] else [])
for cat in all_cats:
    if cat in data['categories']:
        content = generate_category_md(cat)
        with open(f'{PROJECT_DIR}/categories/{cat}.md', 'w') as f:
            f.write(content)
        print(f"Generated categories/{cat}.md ({len(data['categories'][cat])} plugins)")

# Generate README
with open(f'{PROJECT_DIR}/README.md', 'w') as f:
    f.write(generate_readme())
print("Generated README.md")

with open(f'{PROJECT_DIR}/README.zh.md', 'w') as f:
    f.write(generate_readme_zh())
print("Generated README.zh.md")

# Generate CONTRIBUTING.md
with open(f'{PROJECT_DIR}/CONTRIBUTING.md', 'w') as f:
    f.write(generate_contributing())
print("Generated CONTRIBUTING.md")

# Generate sync script
sync_script = """#!/usr/bin/env bash
# sync-plugins.sh — Fetch latest dsh-plugin repos and regenerate files
# Usage: ./scripts/sync-plugins.sh [GITHUB_TOKEN]

set -euo pipefail

TOKEN="${1:-${GITHUB_TOKEN:-}}"
if [ -z "$TOKEN" ]; then
  echo "Error: GITHUB_TOKEN required"
  echo "Usage: $0 <github_token>"
  exit 1
fi

DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$DIR"

echo "=== Fetching dsh-plugin repos ==="
python3 scripts/fetch_plugins.py

echo "=== Categorizing and generating files ==="
python3 scripts/categorize_and_generate.py
python3 scripts/generate_project.py
python3 scripts/generate_site.py

echo "=== Done ==="
echo "Review changes with: git diff"
"""

with open(f'{PROJECT_DIR}/scripts/sync-plugins.sh', 'w') as f:
    f.write(sync_script)
os.chmod(f'{PROJECT_DIR}/scripts/sync-plugins.sh', 0o755)
print("Generated scripts/sync-plugins.sh")

print("\nAll files generated!")
