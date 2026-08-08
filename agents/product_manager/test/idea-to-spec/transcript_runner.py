#!/usr/bin/env python3
"""Compatibility entry for the historical idea-to-spec transcript runner."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.run_skill_eval import definition_from_metadata, run_selected_eval


DEFAULT_TIMEOUT_SECONDS = 300


def generate_eval_outputs(
    metadata_path: Path,
    *,
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
) -> list[dict]:
    definition = definition_from_metadata(metadata_path)
    result = run_selected_eval(
        repository_root=definition.repository_root,
        agent=definition.agent,
        skill=definition.skill,
        eval_id=definition.eval_id,
        timeout_seconds=timeout_seconds,
    )
    return [result]
