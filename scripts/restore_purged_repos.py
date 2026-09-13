#!/usr/bin/env python3
"""One-off restore: re-add repos wrongly purged by the owner==name heuristic.

They were purged from the persistent store on 2026-09-13 but still exist on
GitHub with the dsh-plugin topic; the topic search window (top 1000 by updated)
no longer returns them, so they must be re-inserted from the repos API.
"""
import glob
import json
import os
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dsh_classify import bucket_of  # noqa: E402

TOKEN = os.environ.get('GITHUB_TOKEN')
PROJECT_DIR = '/root/.nanobot/workspace/awesome-dsh-plugin'
RAW_DIR = f'{PROJECT_DIR}/data/raw'

REPOS = [
    'awesome-dsh-plugin/awesome-dsh-plugin',
    'Awesome-AI-Pedia/Awesome-AI-Pedia',
    'WhaleHarness/WhaleHarness',
    'DshMarketPlace/dshmarketplace',
    'dsh-ssh/dsh-ssh',
    'Co-Engram/Co-Engram',
]

restored = 0
for full in REPOS:
    req = urllib.request.Request(f'https://api.github.com/repos/{full}')
    req.add_header('Authorization', f'token {TOKEN}')
    req.add_header('Accept', 'application/vnd.github+json')
    with urllib.request.urlopen(req) as resp:
        repo = json.loads(resp.read().decode())
    cat = bucket_of(repo)
    cat_dir = f'{RAW_DIR}/{cat}'
    os.makedirs(cat_dir, exist_ok=True)
    shards = sorted(glob.glob(f'{cat_dir}/part-*.json'))
    target = shards[-1] if shards else f'{cat_dir}/part-001.json'
    with open(target) as f:
        items = json.load(f)
    if any(x.get('id') == repo['id'] for x in items):
        print(f'already present: {full} in {target}')
        continue
    items.append(repo)
    with open(target, 'w') as f:
        json.dump(items, f, ensure_ascii=False)
    restored += 1
    print(f'restored {full} -> {target} ({cat})')

print(f'done, {restored} repos restored')
