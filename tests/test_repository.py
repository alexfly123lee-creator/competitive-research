from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
  sys.path.insert(0, str(SRC))

from competitive_research.validator import validate_repository  # noqa: E402


class RepositoryValidationTests(unittest.TestCase):
  def test_repository_validation_passes(self) -> None:
    errors = validate_repository(ROOT)
    self.assertEqual(errors, [])


if __name__ == "__main__":
  unittest.main()
