#!/usr/bin/env python3

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.run_skill_eval import compatibility_main


def main() -> int:
    return compatibility_main("designer")


if __name__ == "__main__":
    raise SystemExit(main())
