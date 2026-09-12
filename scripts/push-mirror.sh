#!/usr/bin/env bash
set -e
cd /root/.nanobot/workspace/awesome-dsh-plugin
source /root/.config/env/github.sh
git push "https://${GITHUB_TOKEN}@ghfast.top/https://github.com/billLiao/awesome-dsh-plugin.git" main
