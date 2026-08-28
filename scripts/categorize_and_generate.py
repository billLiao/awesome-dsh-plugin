#!/usr/bin/env python3
"""
Categorize dsh-plugin repos and generate awesome-dsh-plugin structure.
Loads the persistent store from data/raw/<category>/part-NNN.json shards.
"""
import glob
import json
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dsh_classify import score_plugin, categorize  # noqa: E402

PROJECT_DIR = '/root/.nanobot/workspace/awesome-dsh-plugin'
RAW_DIR = f'{PROJECT_DIR}/data/raw'

# Load data from shards (fall back to /tmp/all_dsh_plugins.json if shards missing)
repos = []
if os.path.isdir(RAW_DIR):
    for path in sorted(glob.glob(f'{RAW_DIR}/*/*.json')):
        with open(path) as f:
            repos.extend(json.load(f))
    print(f"Loaded {len(repos)} repos from {RAW_DIR}")
elif os.path.exists('/tmp/all_dsh_plugins.json'):
    with open('/tmp/all_dsh_plugins.json') as f:
        repos = json.load(f)
    print(f"Loaded {len(repos)} repos from /tmp/all_dsh_plugins.json")
else:
    print("No data found (neither data/raw shards nor /tmp/all_dsh_plugins.json)")
    exit(1)

# Filter: exclude repos that are clearly NOT dsh plugins
# (e.g., unrelated projects that just tagged dsh-plugin)
EXCLUDE_KEYWORDS = [
    'open-design', 'claude design', 'claude-art', 'design alternative',
    'iPivotWork', 'Devina-AXIS',
]

# Score and classify all repos
scored = []
for r in repos:
    s, reasons = score_plugin(r)
    scored.append((s, reasons, r))

# Separate into strong, weak, excluded
strong_plugins = []  # score >= 3
weak_plugins = []    # score 1-2
excluded = []        # score <= 0

for s, reasons, r in scored:
    if s >= 3:
        strong_plugins.append(r)
    elif s >= 1:
        weak_plugins.append(r)
    else:
        excluded.append(r)

print(f"Total repos: {len(repos)}")
print(f"Strong plugins (score >= 3): {len(strong_plugins)}")
print(f"Weakly-related (score 1-2): {len(weak_plugins)}")
print(f"Excluded (score <= 0): {len(excluded)}")

# Use strong plugins for categorization
plugins = strong_plugins

# Categorize all plugins
categories = defaultdict(list)
for p in plugins:
    cat = categorize(p)
    categories[cat].append(p)

# Sort each category by stars descending
for cat in categories:
    categories[cat].sort(key=lambda r: -r['stargazers_count'])

print("\n=== Category Distribution ===")
cat_order = [
    'ui-enhancements', 'themes-appearance', 'sessions-messages', 'memory',
    'tools-capabilities', 'workflow-automation', 'notifications-integrations',
    'models-providers', 'development-runtime', 'security-privacy',
    'fun', 'awesome-lists', 'uncategorized'
]
cat_names = {
    'ui-enhancements': 'UI Enhancements',
    'themes-appearance': 'Themes & Appearance',
    'sessions-messages': 'Sessions & Messages',
    'memory': 'Memory',
    'tools-capabilities': 'Tools & Capabilities',
    'workflow-automation': 'Workflow & Automation',
    'notifications-integrations': 'Notifications & Integrations',
    'models-providers': 'Models & Providers',
    'development-runtime': 'Development & Runtime',
    'security-privacy': 'Security & Privacy',
    'fun': 'Just for Fun',
    'awesome-lists': 'Awesome Lists & Collections',
    'uncategorized': 'Uncategorized',
    'weakly-related': 'Weakly Related',
}
cat_icons = {
    'ui-enhancements': '🎨',
    'themes-appearance': '🎭',
    'sessions-messages': '💬',
    'memory': '🧠',
    'tools-capabilities': '🛠️',
    'workflow-automation': '🔁',
    'notifications-integrations': '🔔',
    'models-providers': '🔌',
    'development-runtime': '🧑‍💻',
    'security-privacy': '🔒',
    'fun': '🎮',
    'awesome-lists': '📋',
    'uncategorized': '📦',
    'weakly-related': '⚠️',
}

for cat in cat_order:
    if cat in categories:
        print(f"  {cat_icons[cat]} {cat_names[cat]}: {len(categories[cat])} plugins")

# Add weakly-related plugins as a separate category
if weak_plugins:
    categories['weakly-related'] = weak_plugins
    print(f"  {cat_icons['weakly-related']} {cat_names['weakly-related']}: {len(weak_plugins)} plugins")

total_plugins = sum(len(v) for v in categories.values())
print(f"\nTotal categorized: {total_plugins}")

# Save categorized data
output = {
    'meta': {
        'total_repos': len(repos),
        'total_plugins': total_plugins,
        'generated_at': __import__('datetime').datetime.now().strftime('%Y-%m-%d'),
    },
    'categories': {}
}
for cat in list(cat_order) + ['weakly-related']:
    if cat in categories:
        output['categories'][cat] = [
            {
                'full_name': r['full_name'],
                'url': r['html_url'],
                'description': r.get('description') or '',
                'stars': r['stargazers_count'],
                'topics': r.get('topics', []),
                'updated_at': r.get('updated_at', ''),
            }
            for r in categories[cat]
        ]

with open('/tmp/plugins_categorized.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
print("\nSaved to /tmp/plugins_categorized.json")