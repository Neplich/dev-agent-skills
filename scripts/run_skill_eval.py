#!/usr/bin/env python3
"""Run paired skill evals through the shared execution protocol."""

from __future__ import annotations

import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts import eval_execution as _execution  # noqa: E402
from scripts import eval_judging as _judging  # noqa: E402
from scripts import eval_persistence as _persistence  # noqa: E402


for _name in dir(_execution):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_execution, _name)

JUDGE_SCHEMA = _judging.JUDGE_SCHEMA
_stage_file = _persistence._stage_file
_transactional_replace = _persistence.transactional_replace
_durable_comparison = _persistence.durable_comparison
_updated_inventory = _persistence.updated_inventory
persist_durable_result = _persistence.persist_durable_result


def build_judge_schema_bytes(assertions: list[dict[str, Any]]) -> bytes:
    return _judging.build_judge_schema_bytes(assertions, schema_path=JUDGE_SCHEMA)


def source_identity(definition: Any, *, judge_schema_bytes: bytes | None = None) -> dict[str, Any]:
    schema = judge_schema_bytes or build_judge_schema_bytes(definition.item["assertions"])
    return _execution.eval_identity.source_identity(definition, judge_schema_bytes=schema)


def _targets(
    repository_root: Path, agent: str | None, skill: str | None, eval_id: str | None,
) -> list[tuple[str, str, str]]:
    if eval_id and not skill:
        raise ValueError("--eval requires --skill")
    if skill and not agent:
        raise ValueError("--skill requires --agent")
    targets: list[tuple[str, str, str]] = []
    for path in sorted(repository_root.glob("agents/*/test/*/evals/evals.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        agent_name, skill_name = payload.get("agent"), payload.get("skill_name")
        if (agent and agent_name != agent) or (skill and skill_name != skill):
            continue
        for item in payload.get("evals", []):
            if not eval_id or item.get("id") == eval_id:
                targets.append((agent_name, skill_name, item["id"]))
    return targets


def compatibility_main(agent: str, argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    skip_generate = len(argv) == 2 and argv[1] == "--skip-generate"
    if len(argv) != 1 and not skip_generate:
        print("Usage: run_eval.py <path-to-eval_metadata.json> [--skip-generate]", file=sys.stderr)
        return 2
    try:
        definition = definition_from_metadata(Path(argv[0]))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if definition.agent != agent:
        print(f"ERROR: metadata belongs to {definition.agent}, not {agent}", file=sys.stderr)
        return 2
    if skip_generate:
        comparison = definition.workspace_root / "comparison.md"
        if not comparison.is_file():
            print(f"ERROR: durable comparison does not exist: {comparison}", file=sys.stderr)
            return 2
        conclusion = comparison.read_text(encoding="utf-8")
        match = re.search(
            r"^Overall result: (PASS \(partial coverage\)|PASS|FAIL|BLOCKED)$",
            conclusion, re.MULTILINE,
        )
        if not match:
            print("ERROR: durable comparison lacks Overall result", file=sys.stderr)
            return 2
        print(conclusion, end="" if conclusion.endswith("\n") else "\n")
        return 0 if match.group(1).startswith("PASS") else 1
    result = run_selected_eval(
        repository_root=definition.repository_root, agent=definition.agent,
        skill=definition.skill, eval_id=definition.eval_id,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["overall_result"].startswith("PASS") else 1


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent")
    parser.add_argument("--skill")
    parser.add_argument("--eval", dest="eval_id")
    parser.add_argument("--select", action="append", default=[], metavar="AGENT/SKILL/EVAL")
    parser.add_argument("--metadata", type=Path)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--jobs", type=int, choices=range(1, 11), default=10)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    repository_root = Path(__file__).resolve().parents[1]
    try:
        if args.metadata:
            if any((args.agent, args.skill, args.eval_id, args.select)):
                raise ValueError("--metadata cannot be combined with filters or --select")
            definition = definition_from_metadata(args.metadata)
            targets = [(definition.agent, definition.skill, definition.eval_id)]
        else:
            if args.select and any((args.agent, args.skill, args.eval_id)):
                raise ValueError("--select cannot be combined with agent/skill/eval filters")
            targets = _targets(repository_root, args.agent, args.skill, args.eval_id)
            if args.select:
                selected = {tuple(value.split("/", 2)) for value in args.select}
                if any(len(target) != 3 or not all(target) for target in selected):
                    raise ValueError("invalid --select target")
                missing = selected - set(targets)
                if missing:
                    raise ValueError("unknown --select target(s): " + ", ".join(
                        "/".join(target) for target in sorted(missing)
                    ))
                targets = [target for target in targets if target in selected]
        if not targets:
            raise ValueError("no eval targets matched")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    model_available = check_model_available(repository_root)
    outcomes: dict[tuple[str, str, str], dict[str, Any] | Exception] = {}
    with ThreadPoolExecutor(max_workers=min(args.jobs, len(targets))) as executor:
        futures = {
            executor.submit(
                run_selected_eval, repository_root=repository_root, agent=agent, skill=skill,
                eval_id=eval_id, timeout_seconds=args.timeout, model_available=model_available,
            ): (agent, skill, eval_id)
            for agent, skill, eval_id in targets
        }
        for future in as_completed(futures):
            try:
                outcomes[futures[future]] = future.result()
            except Exception as exc:  # noqa: BLE001
                outcomes[futures[future]] = exc
    failures = 0
    for target in targets:
        outcome = outcomes[target]
        label = "/".join(target)
        if isinstance(outcome, Exception):
            failures += 1
            print(f"{label}: ERROR: {outcome}", file=sys.stderr)
        else:
            print(f"{label}: Overall result: {outcome['overall_result']}")
            if outcome["overall_result"] == "BLOCKED" and outcome.get("blockers"):
                print(f"{label}: blockers: {'; '.join(outcome['blockers'])}")
            failures += not outcome["overall_result"].startswith("PASS")
    print(f"Ran {len(targets)} eval(s); {failures} non-passing")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
