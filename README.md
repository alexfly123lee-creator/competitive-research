# competitive-research

A reusable research-skill repository for evidence-led competitor analysis of internet and AI products.

## What this repo contains

- `skills/competitive-research/SKILL.md` — the skill definition
- `skills/competitive-research/evals/evals.json` — behavior eval prompts
- `skills/competitive-research/trigger-eval-set.json` — trigger eval prompts
- `docs/methodology.md` — research method and output rules
- `templates/` — reusable report templates
- `src/competitive_research/` — small validation utilities for this repository
- `tests/` — smoke tests for repository structure and fixtures

## Scope

This skill is designed for:
- competitor research
- product comparison
- substitute analysis
- pricing and positioning analysis
- research memos for internet and AI products

It is intentionally optimized for:
- progressive intake questions
- external retrieval first
- user-feedback-aware evidence handling
- strong product detail, not just strategic summaries

## Repository layout

```text
competitive-research/
├── .github/workflows/ci.yml
├── docs/
│   └── methodology.md
├── skills/
│   └── competitive-research/
│       ├── SKILL.md
│       ├── trigger-eval-set.json
│       └── evals/
│           └── evals.json
├── src/competitive_research/
├── templates/
├── tests/
├── LICENSE
├── README.md
└── pyproject.toml
```

## Quick start

### 1. Review the skill

Read:
- `skills/competitive-research/SKILL.md`
- `docs/methodology.md`

### 2. Run repository validation

```bash
PYTHONPATH=src python3 -m competitive_research.cli --repo-root .
```

### 3. Run tests

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## Installation / 安装方式

This repository ships the reusable skill at:

```text
skills/competitive-research/
```

The general installation rule is:

1. Copy the entire `skills/competitive-research/` directory
2. Paste it into your coding agent's local skills directory
3. Keep the folder name as `competitive-research`

通用安装规则：

1. 复制整个 `skills/competitive-research/` 目录
2. 粘贴到你的 coding agent 本地 skills 目录下
3. 保持目录名为 `competitive-research`

### Option A — Claude Code

**Install path / 安装路径**

```text
~/.claude/skills/competitive-research/
```

**Example / 示例**

```bash
mkdir -p ~/.claude/skills
cp -R skills/competitive-research ~/.claude/skills/
```

### Option B — Codex / OpenAI Agents-compatible setups

**Install path / 安装路径**

```text
~/.agents/skills/competitive-research/
```

**Example / 示例**

```bash
mkdir -p ~/.agents/skills
cp -R skills/competitive-research ~/.agents/skills/
```

### Option C — OpenCode user skills

In many OpenCode setups, user-installed skills are also loaded from:

很多 OpenCode 环境里，用户自定义 skill 也可以直接放在：

```text
~/.agents/skills/competitive-research/
```

If your OpenCode environment uses a different custom skills path, copy the same folder into that configured directory.

如果你的 OpenCode 环境配置了其他自定义 skills 路径，把同一个目录复制到该配置路径即可。

### Option D — Other coding agents

If your coding agent supports local skills but uses a different folder name, install the same directory into that agent's configured skills path.

如果你的 coding agent 支持本地 skills，但使用不同的目录约定，也可以把同一个目录安装到该 agent 自己的 skills 路径中。

### Verify the skill is loaded / 验证是否安装成功

Ask the agent a natural trigger prompt such as:

可以直接给 agent 一个自然触发的请求，例如：

- `帮我做一下 Figma 和 Framer 的竞品分析`
- `Compare Linear and Jira for startup product teams`
- `我想看看 Cursor、Windsurf、Cline 在开发者市场里的差异`

If the agent starts with progressive intake and asks about research goal, competitors, geography, and output format before researching, the skill is likely loaded correctly.

如果 agent 在正式研究前先做渐进式 intake，询问研究目标、竞品范围、地域范围、输出形式等信息，通常说明 skill 已正确加载。

## Design principles

- External retrieval is the default path for competitor facts and market evidence
- Local materials are used only for task constraints, existing context, and user-provided assets
- Facts, observations, and judgments must stay separate
- Product detail matters: feature pages, pricing, workflow evidence, screenshots, team and funding context
- The skill should ask questions progressively, not dump a long intake form

## Outputs expected from the skill

A strong run should usually include:
- short in-chat summary
- Markdown report
- comparison table
- key product page links
- pricing and feature evidence
- visual references when useful
- founder/team/funding context when relevant
- information gaps and disputes

## Packaging note

This repository is structured as a shareable skill repository. If you want to install it manually, copy the `skills/competitive-research/` directory into your local skills directory.

## License

MIT
