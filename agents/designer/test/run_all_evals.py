#!/usr/bin/env python3

import json
import subprocess
import sys
from pathlib import Path

OUTPUT_FIELDS = (
    "with_skill_outputs",
    "without_skill_outputs",
    "baseline_outputs",
    "baseline_output",
    "baseline_skill_outputs",
)
MACHINE_ASSERTION_FIELDS = (
    "all_of",
    "any_of",
    "none_of",
    "count_at_least",
)


def has_deterministic_checks(path: Path) -> bool:
    meta = json.loads(path.read_text())
    if any(meta.get(field) for field in OUTPUT_FIELDS):
        return True

    for assertion in meta.get("assertions", []):
        if isinstance(assertion, dict) and any(field in assertion for field in MACHINE_ASSERTION_FIELDS):
            return True

    return False


def find_eval_metadata(root: Path) -> list[Path]:
    return [
        path for path in sorted(root.rglob("eval_metadata.json"))
        if has_deterministic_checks(path)
    ]


def main() -> int:
    test_root = Path(__file__).resolve().parent
    targets = [Path(arg).resolve() for arg in sys.argv[1:]] or find_eval_metadata(test_root)

    if not targets:
        print("No deterministic designer eval metadata found under agents/designer/test")
        return 0

    run_eval = test_root / "run_eval.py"
    failures = []

    for metadata_path in targets:
        print(
            f"==> Running {metadata_path.relative_to(test_root.parent.parent.parent)}",
            flush=True,
        )
        result = subprocess.run([sys.executable, str(run_eval), str(metadata_path)])
        if result.returncode != 0:
            failures.append(metadata_path)

    print("")
    print(f"Ran {len(targets)} eval(s)")

    if failures:
        print(f"Failures: {len(failures)}")
        for path in failures:
            print(f"- {path.relative_to(test_root.parent.parent.parent)}")
        return 1

    print("All designer evals passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
