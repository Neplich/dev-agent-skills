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


def has_deterministic_outputs(path: Path) -> bool:
    meta = json.loads(path.read_text())
    return any(meta.get(field) for field in OUTPUT_FIELDS)


def find_eval_metadata(root: Path) -> list[Path]:
    return [
        path for path in sorted(root.rglob("eval_metadata.json"))
        if has_deterministic_outputs(path)
    ]


def main() -> int:
    test_root = Path(__file__).resolve().parent
    repo_root = test_root.parents[2]
    targets = [Path(arg).resolve() for arg in sys.argv[1:]] or find_eval_metadata(test_root)

    if not targets:
        print("No deterministic QA eval metadata found under agents/qa/test")
        return 0

    runner = test_root / "run_eval.py"
    failures = []

    for metadata_path in targets:
        print(f"==> Running {metadata_path.relative_to(repo_root)}", flush=True)
        result = subprocess.run([sys.executable, str(runner), str(metadata_path)])
        if result.returncode != 0:
            failures.append(metadata_path)

    print("")
    print(f"Ran {len(targets)} QA eval(s)")

    if failures:
        print(f"Failures: {len(failures)}")
        for path in failures:
            print(f"- {path.relative_to(repo_root)}")
        return 1

    print("All QA evals passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
