#!/usr/bin/env python3
"""Shared classification logic for dsh-plugin repos.

Used by fetch_plugins.py (to bucket the persistent store by category)
and categorize_and_generate.py (to build the categorized output).

Logic is a verbatim copy of the scoring/categorization rules that were
previously embedded in categorize_and_generate.py — do not change the
rules here without also updating the downstream generator.
"""
import re


def score_plugin(repo):
    """Score a repo's relevance as a DSH plugin.

    Returns (score, reasons):
      score: int, higher = more likely a real DSH plugin
      reasons: list of str describing signals

    Thresholds:
      >= 3: Strong plugin — normal categorization
      1-2:  Weak relevance — goes to weakly-related category
      <= 0: Excluded
    """
    name = repo['full_name'].lower()
    desc = (repo.get('description') or '').lower()
    topics = [t.lower() for t in repo.get('topics', [])]

    score = 0
    reasons = []

    repo_short = name.split('/')[1] if '/' in name else name

    # --- Strong signals (+2) ---

    # dsh- prefix in repo name
    if repo_short.startswith('dsh-'):
        score += 2
        reasons.append('dsh- prefix')

    # Explicitly says "for DeepSeek Harness" or "DSH plugin"
    if 'for deepseek harness' in desc or 'deepseek harness plugin' in desc:
        score += 2
        reasons.append('explicit DSH plugin declaration')
    if re.search(r'\bdsh\b.*plugin|plugin.*\bdsh\b', desc):
        score += 2
        reasons.append('explicit dsh plugin mention')

    # Has dsh-plugin topic
    if 'dsh-plugin' in topics:
        score += 2
        reasons.append('dsh-plugin topic')

    # --- Weak signals (+1) ---

    # Description mentions dsh/deepseek/harness (but not explicitly as plugin)
    if 'dsh' in desc or 'deepseek' in desc or 'harness' in desc:
        score += 1
        reasons.append('mentions dsh/deepseek/harness')

    # Description mentions both plugin and deepseek/dsh
    if ('plugin' in desc or 'plugins' in desc) and ('deepseek' in desc or 'dsh' in desc):
        score += 1
        reasons.append('mentions plugin + deepseek/dsh')

    # Awesome list about dsh plugins
    if 'awesome' in name and ('dsh' in name or 'plugin' in name):
        score += 1
        reasons.append('awesome list about dsh')

    # --- Penalties (-2) ---

    PENALTY_KEYWORDS = [
        'open-interpreter', 'claude', 'open-design', 'claude-art',
        'langchain', 'crewai', 'autogen', 'llamaindex',
        'chatgpt-retrieval-plugin', 'chatgpt-plugin',
    ]
    for kw in PENALTY_KEYWORDS:
        if kw in name or kw in desc:
            score -= 2
            reasons.append(f'penalty: mentions {kw}')

    # Empty or very short description suggests low effort / not a real plugin
    if not desc or len(desc) < 10:
        score -= 1
        reasons.append('penalty: no/short description')

    return score, reasons


def categorize(repo):
    """Categorize a strong plugin into a category key."""
    name = repo['full_name'].lower()
    desc = (repo.get('description') or '').lower()
    topics = [t.lower() for t in repo.get('topics', [])]

    text = f"{name} {desc} {' '.join(topics)}"

    # Awesome lists / collections
    if any(kw in text for kw in ['awesome', 'curated', 'collection', '精选', '目录']):
        if any(kw in text for kw in ['plugin', 'dsh']):
            return 'awesome-lists'

    # UI Enhancements
    if any(kw in text for kw in [
        'ui', 'tui', 'web ui', 'sidebar', 'navbar', 'navbar', 'composer',
        'diff viewer', 'drag-and-drop', 'drag and drop', 'file upload',
        'status bar', 'status-label', 'focus-chat', 'command palette',
        'spotlight', 'deeplink', 'deep link', 'annotation', 'annotate',
        'visualize', 'genui', 'generative ui', 'openpencil', 'pencil',
        'side-panel', 'side panel', 'turn-navigator', 'milestone',
        'balance-meter', 'cost-meter', 'spend', 'usage', 'quota',
        'sticky-note', 'sticky note', 'attention-badge', 'badge',
        'archive', 'collapse', 'disclosure', 'toggle', 'builtin',
        'web-archive', 'web archive', 'web-ui', 'web ui',
        'desktop-pets', 'pets', '桌宠',
        'background', '壁纸', 'wallpaper',
        'billing', '账单',
    ]):
        return 'ui-enhancements'

    # Themes & Appearance
    if any(kw in text for kw in [
        'theme', 'skin', 'appearance', '外观', '主题', '皮肤',
        'whale', '鲸鱼', 'deep-whale',
    ]):
        return 'themes-appearance'

    # Sessions & Messages
    if any(kw in text for kw in [
        'session', 'message', 'chat', 'conversation', '对话', '会话',
        'share', '分享', 'export', 'rewind', 'rollback', '回退',
        'crosstalk', 'sidechain', 'side-chain', '侧会话',
        'message-edit', 'reroll', 'prompt-studio',
        'peer-link', 'chat-import', '导入',
        'file-claim', 'interconnect',
        'explain', '学习', 'reading mode', '阅读',
    ]):
        return 'sessions-messages'

    # Memory
    if any(kw in text for kw in [
        'memory', '记忆', 'remember', 'recall', 'forget',
        'mnemon', 'mneme', 'distill', '蒸馏', 'knowledge',
        'vault', 'knowledge-graph', '知识图谱',
    ]):
        return 'memory'

    # Tools & Capabilities
    if any(kw in text for kw in [
        'tool', 'skill', 'capability', '能力', '工具',
        'vision', 'visual', 'ocr', 'screenshot', '截图',
        'browser', '浏览器', 'computer-use', 'computer use',
        'terminal', 'bash', 'shell', 'ssh', 'docker',
        'git', 'scout', '探测', 'environment',
        'voice', '语音', 'speech',
        'polyglot', 'language', '翻译',
        'robotic', 'robot', 'embodied',
        'canvas', '画布', 'aigc',
        'code-impact', 'impact analysis',
        'undo', 'snapshot', '快照',
        'healthcheck', '健康检查',
        'recon', '侦察',
        'cybernetics', '控制',
        'easy', 'easyssh',
        'pi2dsh', 'pi',
        'mcp', 'model context protocol',
        'eval', 'evaluation', '评估',
        'repro', 'reproduce', '复现',
        'context-proxy', 'context proxy',
        'fail-logger', 'error log',
        'credentials', 'credential',
        'system-proxy', 'proxy',
        'rules', '规则',
        'workspace', '工作区',
        'telemtry', 'redactor',
        'verify-gate', 'verify',
        'polling', '轮询',
        'launcher', '启动器',
        'mobile', '手机',
        'desktop', '桌面',
        'sdk', 'rust sdk',
    ]):
        return 'tools-capabilities'

    # Workflow & Automation
    if any(kw in text for kw in [
        'workflow', 'automation', '自动', 'pipeline',
        'loop', '循环', 'schedule', 'cron', '定时',
        'agent-teams', 'multi-agent', '团队',
        'routines', 'routine',
        'plannotator', 'plan', 'review',
        'sentinel', 'watch', 'wake', '监听',
        'deep-research', 'research', '研究',
        'inspect', 'check', 'adversarial',
        'track', 'task', '任务',
        'advisor', '顾问', 'review',
        'specflow', 'specification',
        'science', 'research workbench',
        'proof', 'verifier', '验证',
        'doublecheck', 'double-check', 'guard',
        'mstar', 'harness',
        'background', '后台',
        'agent-replay', 'replay', '回放',
    ]):
        return 'workflow-automation'

    # Notifications & Integrations
    if any(kw in text for kw in [
        'notification', '通知', 'notify', 'alert',
        'wechat', '微信', 'telegram', 'wecom', '企业微信',
        'bridge', '桥接', 'integration', '集成',
        'open-in-vscode', 'vscode',
        'bitfun', 'acp',
        'im-bridge', 'chatnode',
        'web-bridge', 'webbridge',
        'discord', 'slack',
    ]):
        return 'notifications-integrations'

    # Models & Providers
    if any(kw in text for kw in [
        'model', 'provider', 'llm', '模型',
        'codex', 'oauth', 'openai', 'chatgpt',
        'fallback', 'fall back', '策略',
        'qwen', 'multi-modal', '多模态',
        'codex-auth', 'codex-connect',
        'everything-oauth',
        'zen-proxy', 'proxy',
    ]):
        return 'models-providers'

    # Development & Runtime
    if any(kw in text for kw in [
        'dev', 'development', 'runtime', '开发',
        'plugin-manager', 'plugin manager', '插件管理',
        'installer', '安装',
        'sdk', 'rust',
        'cli', 'command line',
        'template', 'boilerplate', '脚手架',
        'config', '配置',
        'dsh-devkit', 'devkit',
        'dsh-plugin-installer',
        'dsh-plugin-manager',
        'dsh-web-panel', 'web panel',
        'dsh-shell', 'shell',
        'dsh-desktop', 'desktop wrapper',
        'dsh-mobile', 'mobile',
        'dsh-launcher', 'launcher',
        'dsh-one-click', 'one-click',
        'dsh-eye', 'eye',
        'dsh-auto-open', 'auto-open',
    ]):
        return 'development-runtime'

    # Security & Privacy
    if any(kw in text for kw in [
        'security', '安全', 'privacy', '隐私',
        'vault', 'credential', '凭证', 'encrypt',
        'audit', '审计', 'redact',
        'verify', '验证', 'guard',
    ]):
        return 'security-privacy'

    # Fun & Entertainment
    if any(kw in text for kw in [
        'fun', 'game', '娱乐', 'pet', '宠物',
        'entertainment', 'ads', '广告',
        'douyin', '抖音', 'stock', '股票',
        'd399', 'mineru',
    ]):
        return 'fun'

    return 'uncategorized'


def bucket_of(repo):
    """Return the persistent-store bucket (category key) for a repo."""
    s, _ = score_plugin(repo)
    if s >= 3:
        return categorize(repo)
    elif s >= 1:
        return 'weakly-related'
    return 'excluded'