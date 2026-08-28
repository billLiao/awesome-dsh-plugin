#!/usr/bin/env python3
"""Fetch all GitHub repos with topic dsh-plugin, paginated, and merge with persistent store.

The persistent store is split by category into data/raw/<category>/part-NNN.json.
Each shard is capped at MAX_FILE_BYTES; when a category exceeds the cap it is
split into multiple part files automatically.
"""
import glob
import json
import os
import sys
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dsh_classify import bucket_of  # noqa: E402

TOKEN = os.environ.get('GITHUB_TOKEN')
if not TOKEN:
    print("GITHUB_TOKEN not set")
    exit(1)

PROJECT_DIR = '/root/.nanobot/workspace/awesome-dsh-plugin'
RAW_DIR = f'{PROJECT_DIR}/data/raw'
MAX_FILE_BYTES = 10 * 1024 * 1024  # 10 MB per shard — well under GitHub's 50 MB warning

# Load existing persistent data from shards + legacy single file (if present)
existing_repos = {}
legacy = f'{PROJECT_DIR}/data/raw_plugins.json'

# Legacy file first (older data), shards second (newer data wins on conflicts)
if os.path.exists(legacy):
    with open(legacy) as f:
        for repo in json.load(f):
            existing_repos[repo['id']] = repo
    print(f"Loaded {len(existing_repos)} existing repos from legacy {legacy}")

if os.path.isdir(RAW_DIR):
    for path in sorted(glob.glob(f'{RAW_DIR}/*/*.json')):
        with open(path) as f:
            for repo in json.load(f):
                existing_repos[repo['id']] = repo
    print(f"Loaded {len(existing_repos)} existing repos from persistent store (shards + legacy)")

# Fetch from API
all_items = []
page = 1
per_page = 100

while True:
    url = f"https://api.github.com/search/repositories?q=topic:dsh-plugin&sort=updated&per_page={per_page}&page={page}"
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"token {TOKEN}")
    req.add_header("Accept", "application/vnd.github+json")

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
    except Exception as e:
        print(f"Error on page {page}: {e}")
        break

    items = data.get('items', [])
    if not items:
        break

    all_items.extend(items)
    print(f"Page {page}: got {len(items)} items (total: {len(all_items)})")
    page += 1
    time.sleep(0.3)

print(f"\nFetched: {len(all_items)} repos from API")

# Merge: add new repos, update metadata for existing ones
new_count = 0
updated_count = 0
for repo in all_items:
    repo_id = repo['id']
    if repo_id in existing_repos:
        # Update metadata for existing repo (stars, description, topics, etc.)
        existing_repos[repo_id].update({
            'description': repo.get('description'),
            'stargazers_count': repo['stargazers_count'],
            'updated_at': repo.get('updated_at'),
            'topics': repo.get('topics', []),
            'html_url': repo['html_url'],
        })
        updated_count += 1
    else:
        # Add new repo
        existing_repos[repo_id] = repo
        new_count += 1

merged_list = list(existing_repos.values())
print(f"New: {new_count}, Updated: {updated_count}")
print(f"Total in persistent store: {len(merged_list)}")

# Save merged data to temp file for downstream scripts
with open('/tmp/all_dsh_plugins.json', 'w') as f:
    json.dump(merged_list, f, ensure_ascii=False)
print("Saved to /tmp/all_dsh_plugins.json")

# --- Save persistent store split by category, sharded by size ---
buckets = {}
for repo in merged_list:
    buckets.setdefault(bucket_of(repo), []).append(repo)

os.makedirs(RAW_DIR, exist_ok=True)
new_paths = set()
total_files = 0
for cat in sorted(buckets):
    repos = buckets[cat]
    cat_dir = f'{RAW_DIR}/{cat}'
    os.makedirs(cat_dir, exist_ok=True)
    part = 1
    chunk = []
    chunk_bytes = 0
    for repo in repos:
        item_bytes = len(json.dumps(repo, ensure_ascii=False).encode('utf-8')) + 1  # +1 for comma
        if chunk and chunk_bytes + item_bytes > MAX_FILE_BYTES:
            path = f'{cat_dir}/part-{part:03d}.json'
            with open(path, 'w') as f:
                json.dump(chunk, f, ensure_ascii=False)
            print(f"Saved {path} ({len(chunk)} repos)")
            new_paths.add(path)
            total_files += 1
            part += 1
            chunk = []
            chunk_bytes = 0
        chunk.append(repo)
        chunk_bytes += item_bytes
    if chunk:
        path = f'{cat_dir}/part-{part:03d}.json'
        with open(path, 'w') as f:
            json.dump(chunk, f, ensure_ascii=False)
        print(f"Saved {path} ({len(chunk)} repos)")
        new_paths.add(path)
        total_files += 1

# Remove stale shards (category files that no longer exist in the new set)
for old in glob.glob(f'{RAW_DIR}/*/*.json'):
    if old not in new_paths:
        os.remove(old)
        print(f"Removed stale shard {old}")

# Remove legacy single-file store only when nothing was lost in the split
if os.path.exists(legacy):
    with open(legacy) as f:
        legacy_count = len(json.load(f))
    if len(merged_list) >= legacy_count:
        os.remove(legacy)
        print(f"Removed legacy {legacy} (all {legacy_count} repos preserved in shards)")
    else:
        print(f"WARNING: kept legacy {legacy} — shards have {len(merged_list)} repos < legacy {legacy_count}")

print(f"Saved {len(merged_list)} repos into {total_files} shard files under {RAW_DIR}")
