#!/usr/bin/env python3
"""generate_site.py — Generate landing-page data (site/data/*.json) from data/plugins.json.

Reads the categorized plugin database produced by the sync pipeline and writes
per-category JSON shards plus a meta.json consumed by the static site in /site.
Run automatically by scripts/sync-plugins.sh after generate_project.py.
"""
import json
import os
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "data", "plugins.json")
OUT = os.path.join(ROOT, "site", "data")

MAX_TOPICS = 6

# slug, zh name, en name, icon, zh description, en description
CATEGORIES = [
    ("ui-enhancements", "UI 增强", "UI Enhancements", "🎨",
     "增强 DSH 网页与终端界面。", "Enhance the DSH web/terminal interface."),
    ("themes-appearance", "主题外观", "Themes & Appearance", "🎭",
     "皮肤、主题与外观定制。", "Skins, themes, and appearance customization."),
    ("sessions-messages", "会话消息", "Sessions & Messages", "💬",
     "会话管理、消息编辑与分享。", "Session management, message editing, and sharing."),
    ("memory", "记忆", "Memory", "🧠",
     "持久记忆、知识库与上下文保留。", "Persistent memory, knowledge bases, and context retention."),
    ("tools-capabilities", "工具能力", "Tools & Capabilities", "🛠️",
     "视觉、浏览器、终端、SSH 等能力扩展。", "Vision, browser, terminal, SSH, and other capability extensions."),
    ("workflow-automation", "工作流自动化", "Workflow & Automation", "🔁",
     "自动化循环、定时任务与多智能体协作。", "Automation loops, scheduled tasks, and multi-agent teams."),
    ("notifications-integrations", "通知集成", "Notifications & Integrations", "🔔",
     "微信、Telegram、IM 桥接与外部集成。", "WeChat, Telegram, IM bridges, and external integrations."),
    ("models-providers", "模型接入", "Models & Providers", "🔌",
     "多模型支持与 Provider 桥接。", "Multi-model support and provider bridges."),
    ("development-runtime", "开发运行时", "Development & Runtime", "🧑‍💻",
     "插件管理器、SDK、CLI 与开发工具。", "Plugin managers, SDKs, CLIs, and developer tooling."),
    ("security-privacy", "安全隐私", "Security & Privacy", "🔒",
     "凭证管理、加密与审计工具。", "Credential management, encryption, and audit tooling."),
    ("fun", "趣味", "Just for Fun", "🎮",
     "游戏、宠物与娱乐插件。", "Games, pets, and playful plugins."),
    ("awesome-lists", "清单合集", "Awesome Lists", "📋",
     "DSH 插件精选清单与合集。", "Curated collections and awesome lists of DSH plugins."),
    ("uncategorized", "未分类", "Uncategorized", "📦",
     "尚未归类的插件。", "Plugins not yet categorized."),
    ("weakly-related", "弱相关", "Weakly Related", "⚠️",
     "关联信号较弱的仓库，可能仅使用 DeepSeek API。", "Repos with weak relevance signals — may use the DeepSeek API."),
]


def main() -> int:
    if not os.path.exists(SRC):
        print(f"error: {SRC} not found — run fetch_plugins.py first", file=sys.stderr)
        return 1

    with open(SRC, encoding="utf-8") as f:
        db = json.load(f)
    cats = db.get("categories", {})

    os.makedirs(OUT, exist_ok=True)
    meta_cats = []
    total = 0
    for slug, zh, en, icon, desc_zh, desc_en in CATEGORIES:
        items = cats.get(slug, [])
        items = sorted(items, key=lambda x: (-x.get("stars", 0), x.get("full_name", "")))
        slim = [
            {
                "full_name": it.get("full_name", ""),
                "url": it.get("url", ""),
                "description": it.get("description") or "",
                "stars": it.get("stars", 0),
                "topics": (it.get("topics") or [])[:MAX_TOPICS],
                "updated_at": it.get("updated_at", ""),
            }
            for it in items
        ]
        with open(os.path.join(OUT, f"{slug}.json"), "w", encoding="utf-8") as f:
            json.dump(slim, f, ensure_ascii=False, separators=(",", ":"))
        meta_cats.append({
            "slug": slug, "zh": zh, "en": en, "icon": icon,
            "desc_zh": desc_zh, "desc_en": desc_en, "count": len(slim),
        })
        total += len(slim)

    meta = {
        "total": total,
        "generated_at": db.get("meta", {}).get("generated_at") or str(date.today()),
        "categories": meta_cats,
    }
    with open(os.path.join(OUT, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, separators=(",", ":"))

    print(f"site data written: {total} plugins across {len(meta_cats)} categories -> {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
