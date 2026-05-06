from __future__ import annotations

import os
import shutil
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def display_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(repo_root()).as_posix()
    except ValueError:
        return str(resolved)


def eval_runtime_root(metadata_path: Path | str, suite: str) -> Path:
    metadata_path = Path(metadata_path).resolve()
    base = Path(os.environ.get("EVAL_RUN_OUTPUT_DIR", "tmp/eval-runs"))
    if not base.is_absolute():
        base = repo_root() / base

    try:
        eval_rel = metadata_path.parent.relative_to(repo_root())
    except ValueError:
        eval_rel = Path(metadata_path.parent.name)

    return base / suite / eval_rel


def reset_directory(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def remove_path(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def apply_cleanup_paths(root: Path, cleanup_paths: list[str]) -> None:
    for rel in cleanup_paths:
        if any(char in rel for char in "*?["):
            for target in root.glob(rel):
                remove_path(target)
            continue
        remove_path(root / rel)


def copy_fixture_to_runtime(fixture_root: Path, runtime_root: Path) -> None:
    if runtime_root.exists():
        shutil.rmtree(runtime_root)
    runtime_root.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(fixture_root, runtime_root)
