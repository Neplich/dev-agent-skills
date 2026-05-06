#!/usr/bin/env python3

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.eval_runtime import display_path, eval_runtime_root
from transcript_runner import generate_eval_outputs


def load_metadata(path: Path) -> dict:
    return json.loads(path.read_text())


def check_outputs(root: Path, outputs: list) -> list[tuple[str, bool]]:
    results = []
    for item in outputs:
        if isinstance(item, str):
            target = root / item
            ok = target.exists() and (target.is_dir() or target.stat().st_size > 0)
            results.append((item, ok))
            continue

        if isinstance(item, list):
            checks = []
            for rel in item:
                target = root / rel
                ok = target.exists() and (target.is_dir() or target.stat().st_size > 0)
                checks.append((rel, ok))
            label = " OR ".join(rel for rel, _ in checks)
            results.append((label, any(ok for _, ok in checks)))
            continue

        raise TypeError(f"Unsupported output spec: {item!r}")
    return results


def read_targets(root: Path, target_spec) -> str:
    if isinstance(target_spec, str):
        path = root / target_spec
        if not path.exists() or path.is_dir():
            return ""
        return path.read_text()

    if isinstance(target_spec, list):
        chunks = []
        for item in target_spec:
            chunks.append(read_targets(root, item))
        return "\n\n".join(chunk for chunk in chunks if chunk)

    raise TypeError(f"Unsupported target spec: {target_spec!r}")


def evaluate_assertion(root: Path, assertion: dict) -> dict:
    target = assertion.get("target", "with_skill/outputs/transcript.md")
    text = read_targets(root, target)

    all_of = assertion.get("all_of", [])
    all_of_any = assertion.get("all_of_any", [])
    any_of = assertion.get("any_of", [])
    none_of = assertion.get("none_of", [])
    count_at_least = assertion.get("count_at_least", [])

    if not any([all_of, all_of_any, any_of, none_of, count_at_least]):
        return {
            "id": assertion["id"],
            "description": assertion["description"],
            "status": "MANUAL",
            "details": "No machine-checkable fields present",
        }

    failures = []
    if all_of:
        missing = [item for item in all_of if item not in text]
        if missing:
            failures.append(f"Missing required text: {missing}")

    if all_of_any:
        grouped_missing = []
        for group in all_of_any:
            if not any(item in text for item in group):
                grouped_missing.append(group)
        if grouped_missing:
            failures.append(f"Missing required any-of groups: {grouped_missing}")

    if any_of and not any(item in text for item in any_of):
        failures.append(f"Missing any-of text: {any_of}")

    if none_of:
        present = [item for item in none_of if item in text]
        if present:
            failures.append(f"Found forbidden text: {present}")

    if count_at_least:
        count_failures = []
        for item in count_at_least:
            needle = item["text"]
            minimum = item["count"]
            actual = text.count(needle)
            if actual < minimum:
                count_failures.append(
                    f"'{needle}' count {actual} < required {minimum}"
                )
        if count_failures:
            failures.append("; ".join(count_failures))

    return {
        "id": assertion["id"],
        "description": assertion["description"],
        "status": "PASS" if not failures else "FAIL",
        "details": "; ".join(failures) if failures else "All checks passed",
    }


def render_report(
    meta: dict,
    with_results: list[tuple[str, bool]],
    without_results: list[tuple[str, bool]],
    assertion_results: list[dict],
) -> str:
    lines = []
    lines.append(f"# Eval {meta['eval_id']}: {meta['eval_name']}")
    lines.append("")
    lines.append("## Prompt")
    lines.append("")
    lines.append(meta["prompt"])
    lines.append("")
    lines.append("## Expected Assertions")
    lines.append("")
    for item in meta.get("assertions", []):
        lines.append(f"- `{item['id']}`: {item['description']}")
    lines.append("")
    lines.append("## Output Presence Check")
    lines.append("")
    lines.append("### With Skill")
    lines.append("")
    for rel, ok in with_results:
        icon = "PASS" if ok else "FAIL"
        lines.append(f"- [{icon}] `{rel}`")
    lines.append("")
    lines.append("### Without Skill")
    lines.append("")
    for rel, ok in without_results:
        icon = "PASS" if ok else "FAIL"
        lines.append(f"- [{icon}] `{rel}`")
    lines.append("")
    lines.append("## Assertion Checks")
    lines.append("")
    for result in assertion_results:
        lines.append(
            f"- [{result['status']}] `{result['id']}`: {result['description']}"
        )
        lines.append(f"  - {result['details']}")
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("- Fill in qualitative comparison after reviewing transcripts and docs.")
    return "\n".join(lines) + "\n"


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print("Usage: run_eval.py <path-to-eval_metadata.json> [--skip-generate]")
        return 2

    metadata_path = Path(sys.argv[1]).resolve()
    should_generate = "--skip-generate" not in sys.argv[2:]
    root = eval_runtime_root(metadata_path, "product_manager")
    meta = load_metadata(metadata_path)

    if should_generate:
        generate_eval_outputs(metadata_path)

    with_results = check_outputs(root, meta.get("with_skill_outputs", []))
    without_results = check_outputs(root, meta.get("without_skill_outputs", []))
    assertion_results = [
        evaluate_assertion(root, assertion) for assertion in meta.get("assertions", [])
    ]

    report = render_report(meta, with_results, without_results, assertion_results)
    report_path = root / "comparison.auto.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report)

    failed = any(not ok for _, ok in with_results + without_results) or any(
        result["status"] == "FAIL" for result in assertion_results
    )
    print(display_path(report_path))
    print("Manual review template: agents/product_manager/test/idea-to-spec/COMPARISON_TEMPLATE.md")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
