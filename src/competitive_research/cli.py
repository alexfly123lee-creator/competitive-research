from __future__ import annotations

import argparse
from pathlib import Path

from .validator import validate_repository


def main() -> int:
  parser = argparse.ArgumentParser(description="Validate the competitive-research repository structure.")
  parser.add_argument("--repo-root", default=".", help="Repository root to validate")
  args = parser.parse_args()

  repo_root = Path(args.repo_root).resolve()
  errors = validate_repository(repo_root)

  if errors:
    for error in errors:
      print(error)
    return 1

  print("Repository validation passed.")
  return 0


if __name__ == "__main__":
  raise SystemExit(main())
