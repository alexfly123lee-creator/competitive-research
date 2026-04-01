from __future__ import annotations

import json
from pathlib import Path
from typing import List

REQUIRED_FILES = [
  "README.md",
  "LICENSE",
  ".gitignore",
  "pyproject.toml",
  "docs/methodology.md",
  "templates/competitor-profile.md",
  "templates/research-report.md",
  "skills/competitive-research/SKILL.md",
  "skills/competitive-research/evals/evals.json",
  "skills/competitive-research/trigger-eval-set.json",
  "src/competitive_research/__init__.py",
  "src/competitive_research/cli.py",
  "src/competitive_research/validator.py",
  "tests/test_repository.py",
  ".github/workflows/ci.yml",
]


def validate_repository(repo_root: Path) -> List[str]:
  """验证仓库结构和 fixture 是否齐全。"""
  errors: List[str] = []

  for relative_path in REQUIRED_FILES:
    if not (repo_root / relative_path).exists():
      errors.append(f"Missing required file: {relative_path}")

  evals_path = repo_root / "skills/competitive-research/evals/evals.json"
  trigger_path = repo_root / "skills/competitive-research/trigger-eval-set.json"
  skill_path = repo_root / "skills/competitive-research/SKILL.md"

  if evals_path.exists():
    try:
      evals = json.loads(evals_path.read_text(encoding="utf-8"))
      if evals.get("skill_name") != "competitive-research":
        errors.append("evals.json skill_name must be competitive-research")
      if len(evals.get("evals", [])) < 3:
        errors.append("evals.json should contain at least 3 eval cases")
    except json.JSONDecodeError as exc:
      errors.append(f"evals.json is invalid JSON: {exc}")

  if trigger_path.exists():
    try:
      trigger_evals = json.loads(trigger_path.read_text(encoding="utf-8"))
      if len(trigger_evals) < 20:
        errors.append("trigger-eval-set.json should contain at least 20 trigger eval queries")
      trigger_count = sum(1 for item in trigger_evals if item.get("should_trigger") is True)
      no_trigger_count = sum(1 for item in trigger_evals if item.get("should_trigger") is False)
      if trigger_count == 0 or no_trigger_count == 0:
        errors.append("trigger-eval-set.json should include both positive and negative trigger cases")
    except json.JSONDecodeError as exc:
      errors.append(f"trigger-eval-set.json is invalid JSON: {exc}")

  if skill_path.exists():
    skill_text = skill_path.read_text(encoding="utf-8")
    required_markers = [
      "name: competitive-research",
      "## Intake First",
      "## Research Rules",
      "## Product Detail",
      "## Report Template",
    ]
    for marker in required_markers:
      if marker not in skill_text:
        errors.append(f"SKILL.md missing required section marker: {marker}")

  return errors
