#!/usr/bin/env bash
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
python3 /tmp/fetch_plugins.py

echo "=== Categorizing and generating files ==="
python3 /tmp/categorize_and_generate.py
python3 /tmp/generate_project.py

echo "=== Done ==="
echo "Review changes with: git diff"