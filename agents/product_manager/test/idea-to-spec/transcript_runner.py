#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.eval_runtime import eval_runtime_root, reset_directory


RESERVED_CLEANUP_PATHS = (
    "with_skill",
    "without_skill",
    "comparison.auto.md",
    "comparison.md",
    "README.md",
    "eval_metadata.json",
)

DEFAULT_TIMEOUT_SECONDS = 180
DEFAULT_MODEL = "gpt-5.6-luna"
DEFAULT_REASONING_EFFORT = "medium"


class TranscriptRunError(RuntimeError):
    def __init__(self, message: str, status: dict):
        super().__init__(message)
        self.status = status


def load_metadata(path: Path) -> dict:
    return json.loads(path.read_text())


def remove_path(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
    elif path.exists():
        path.unlink()


def prepare_execution_workspace(
    eval_root: Path,
    execution_root: Path,
    cleanup_paths: list[str] | None = None,
) -> None:
    if execution_root.exists():
        shutil.rmtree(execution_root)

    shutil.copytree(eval_root, execution_root)

    for rel in RESERVED_CLEANUP_PATHS:
        remove_path(execution_root / rel)

    for rel in cleanup_paths or []:
        remove_path(execution_root / rel)


def read_result_file(path: Path) -> str:
    if not path.exists() or not path.read_text().strip():
        raise ValueError(f"Codex result file is missing or empty: {path}")

    return path.read_text()


def iter_output_paths(outputs: list) -> list[str]:
    paths = []
    for item in outputs:
        if isinstance(item, str):
            paths.append(item)
            continue
        if isinstance(item, list):
            paths.extend(iter_output_paths(item))
            continue
        raise TypeError(f"Unsupported output spec: {item!r}")
    return paths


def copy_path(source: Path, destination: Path) -> None:
    if source.is_dir():
        if destination.exists():
            shutil.rmtree(destination)
        shutil.copytree(source, destination)
        return

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def sync_declared_outputs(execution_root: Path, eval_root: Path, outputs: list) -> None:
    for rel in iter_output_paths(outputs):
        source = execution_root / rel
        if not source.exists():
            continue
        copy_path(source, eval_root / rel)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[4]


def build_codex_command(
    prompt: str,
    *,
    cwd: Path,
    output_path: Path,
) -> list[str]:
    return [
        "codex",
        "exec",
        "-C",
        str(cwd),
        "-s",
        "workspace-write",
        "--ephemeral",
        "--ignore-user-config",
        "--ignore-rules",
        "-m",
        DEFAULT_MODEL,
        "-c",
        f'model_reasoning_effort="{DEFAULT_REASONING_EFFORT}"',
        "-o",
        str(output_path),
        prompt,
    ]


def resolve_skill_dir(meta: dict) -> str:
    entry = meta.get("entry_command", "/idea-to-spec").lstrip("/")
    plugin = meta.get("plugin_dir", "agents/product_manager")
    return f"{plugin}/skills/{entry}"


# Routers whose entry skill delegates to a specialist that must also be
# discoverable for the delegation chain to execute in the lane.
ROUTER_SPECIALISTS = {
    "agents/product_manager/skills/pm-agent": [
        "agents/product_manager/skills/idea-to-spec",
    ],
}


def mirror_dependency_documents(execution_root: Path) -> None:
    """Stripped agents/ mirror shared by both lanes (identical visible context).

    Literal `agents/...` references inside skill documents and router-to-
    specialist delegation chains resolve from this tree; agent test
    directories are stripped (matching docs/README.codex.md) so eval
    assertions and prior comparison results never enter a lane. Both lanes
    receive the same mirror — only the discovery/loading of the entry skill
    differs, keeping the lane-isolation contract intact.
    """
    shutil.copytree(
        repo_root() / "agents",
        execution_root / "agents",
        ignore=shutil.ignore_patterns("test"),
    )


def install_entry_skill(execution_root: Path, skill_dir: str) -> None:
    """Expose the entry skill (and routed specialists) at Codex discovery."""
    entry_source = Path(skill_dir)
    if not entry_source.is_absolute():
        entry_source = repo_root() / entry_source
    for skill_path in [str(entry_source.relative_to(repo_root()))] + ROUTER_SPECIALISTS.get(
        skill_dir, []
    ):
        source = repo_root() / skill_path
        target = execution_root / ".agents" / "skills" / source.name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, target)


def build_isolated_env(temp_root: Path) -> tuple[dict, Path]:
    """Isolate the lane from user-level Codex skills (~/.agents/skills).

    Codex resolves user skills under $HOME/.agents/skills and the auth store
    under $CODEX_HOME (default $HOME/.codex); pointing HOME and CODEX_HOME at
    fresh directories (with the auth.json copied from the active CODEX_HOME)
    drops personal skills while keeping authentication. Built-in Codex skills
    still load — they are unrelated to repo skills.
    """
    home = temp_root / "codex-home"
    codex_home = home / ".codex"
    codex_home.mkdir(parents=True, exist_ok=True)
    active_codex_home = os.environ.get("CODEX_HOME") or str(Path.home() / ".codex")
    auth_src = Path(active_codex_home) / "auth.json"
    if auth_src.exists():
        shutil.copy2(auth_src, codex_home / "auth.json")
    env = dict(os.environ)
    env["HOME"] = str(home)
    env["CODEX_HOME"] = str(codex_home)
    return env, home


def run_codex(
    command: list[str],
    cwd: Path,
    timeout_seconds: int,
    env: dict | None = None,
) -> tuple[str, dict]:
    started = time.time()
    try:
        completed = subprocess.run(
            command,
            cwd=cwd,
            env=env,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
        )
    except subprocess.TimeoutExpired as exc:
        status = {
            "command": command,
            "cwd": str(cwd),
            "timeout": True,
            "returncode": None,
            "stdout_length": len(exc.stdout or ""),
            "stderr": exc.stderr or "",
            "duration_ms": int((time.time() - started) * 1000),
        }
        raise TranscriptRunError("Codex command timed out", status) from exc

    status = {
        "command": command,
        "cwd": str(cwd),
        "timeout": False,
        "returncode": completed.returncode,
        "stdout_length": len(completed.stdout),
        "stderr": completed.stderr,
        "duration_ms": int((time.time() - started) * 1000),
    }

    if completed.returncode != 0:
        raise TranscriptRunError("Codex command failed", status)

    output_path = Path(command[command.index("-o") + 1])
    try:
        result_text = read_result_file(output_path)
    except Exception as exc:  # noqa: BLE001
        raise TranscriptRunError(str(exc), status) from exc

    status["result_length"] = len(result_text)
    return result_text, status


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def write_status(path: Path, status: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(status, ensure_ascii=False, indent=2) + "\n")


def generate_eval_outputs(
    metadata_path: Path,
    *,
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS,
) -> list[dict]:
    metadata_path = metadata_path.resolve()
    eval_root = metadata_path.parent
    runtime_root = eval_runtime_root(metadata_path, "product_manager")
    meta = load_metadata(metadata_path)
    cleanup_paths = meta.get("execution_cleanup", [])
    statuses = []

    reset_directory(runtime_root)

    with tempfile.TemporaryDirectory(prefix="idea-to-spec-eval-") as temp_dir:
        temp_root = Path(temp_dir)
        lane_env, _ = build_isolated_env(temp_root)
        skill_dir = meta.get("skill_dir") or resolve_skill_dir(meta)

        runs = [
            ("with_skill", meta.get("with_skill_outputs", []), True),
            ("without_skill", meta.get("without_skill_outputs", []), False),
        ]

        for label, outputs, with_skill in runs:
            execution_root = Path(temp_dir) / "workspace" / label
            prepare_execution_workspace(eval_root, execution_root, cleanup_paths=cleanup_paths)
            mirror_dependency_documents(execution_root)
            if with_skill:
                install_entry_skill(execution_root, skill_dir)
            output_path = execution_root / label / "outputs/result.txt"
            output_path.parent.mkdir(parents=True, exist_ok=True)
            command = build_codex_command(
                meta["prompt"],
                cwd=execution_root,
                output_path=output_path,
            )
            transcript_path = execution_root / label / "outputs/transcript.md"
            status_path = execution_root / label / "outputs/run_status.json"

            try:
                transcript, status = run_codex(
                    command,
                    execution_root,
                    timeout_seconds,
                    env=lane_env,
                )
            except TranscriptRunError as exc:
                status = exc.status
            else:
                write_text(transcript_path, transcript)
                copy_path(transcript_path, runtime_root / label / "outputs/transcript.md")

            write_status(status_path, status)
            sync_declared_outputs(execution_root, runtime_root, outputs)
            copy_path(status_path, runtime_root / label / "outputs/run_status.json")
            statuses.append({"label": label, **status})

    return statuses
