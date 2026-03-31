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
