from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any, Callable


RUNTIME_SURFACES = ("processes", "ports", "database", "browser", "login_state", "downloads")
EXCLUDED_DIRECTORY_NAMES = {
    ".git", "with_skill", "without_skill", "baseline", "iteration2", "outputs",
    "diagnostics", "snapshots", "preflight", "judge", "node_modules",
}
EXCLUDED_FILE_NAMES = {
    "evals.json", "eval_metadata.json", "comparison.md", "comparison.auto.md",
    "transcript.md", "candidate-output.md", "subagent-verdict.md",
    "judge-verdict.json", "judge-package.json", "workspace-snapshot.json",
    "timing.json", "run_status.json",
}
ANSWER_GUIDANCE = ("expected behavior:", "dispatcher should", "fixture verifies")
README_SCAFFOLDING = (
    "eval workspace", "evaluation workspace", "the eval expects", "the eval asks",
    "regression target",
)


def reset_directory(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def remove_path(path: Path) -> None:
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    elif path.exists() or path.is_symlink():
        path.unlink()


def readme_is_eval_scaffolding(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore").lower()
    return any(phrase in text for phrase in (*ANSWER_GUIDANCE, *README_SCAFFOLDING))


def _is_excluded(relative_path: Path, source: Path | None = None) -> bool:
    parts = relative_path.parts
    if not parts:
        return False
    if parts[0] == ".agents":
        return True
    if parts[-1] == "README.md" and source is not None and readme_is_eval_scaffolding(source):
        return True
    if any(part in EXCLUDED_DIRECTORY_NAMES for part in parts):
        return True
    return parts[-1] in EXCLUDED_FILE_NAMES


def copy_canonical_fixture(
    fixture_root: Path, destination: Path, *, cleanup_paths: list[str] | None = None,
) -> None:
    """Copy only candidate-visible host facts into a fresh directory."""
    fixture_root = fixture_root.resolve()
    reset_directory(destination)
    cleanup_specs = tuple(PurePosixPath(value) for value in cleanup_paths or ())

    for source in sorted(fixture_root.rglob("*")):
        relative = source.relative_to(fixture_root)
        if _is_excluded(relative, source):
            continue
        relative_posix = PurePosixPath(relative.as_posix())
        candidates = (relative_posix, *relative_posix.parents)
        if any(any(candidate.match(str(spec)) for candidate in candidates) for spec in cleanup_specs):
            continue
        target = destination / relative
        if source.is_symlink():
            raise ValueError(f"canonical fixture must not contain symlinks: {relative}")
        if source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        elif source.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)


def fixture_manifest(root: Path) -> dict[str, str]:
    manifest: dict[str, str] = {}
    if not root.exists():
        return manifest
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(root)
        if _is_excluded(relative, path):
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        manifest[relative.as_posix()] = digest
    return manifest


def manifest_hash(manifest: dict[str, str]) -> str:
    encoded = json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def _git(workspace: Path, *args: str) -> None:
    env = {
        **os.environ,
        "GIT_AUTHOR_DATE": "2000-01-01T00:00:00+00:00",
        "GIT_COMMITTER_DATE": "2000-01-01T00:00:00+00:00",
    }
    subprocess.run(
        ["git", *args], cwd=workspace, check=True, env=env,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def _git_output(workspace: Path, *args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=workspace, text=True, stderr=subprocess.DEVNULL,
    ).rstrip()


def _valid_ref_name(value: Any, *, full: bool) -> bool:
    if (not isinstance(value, str) or not value or value in {"@", "HEAD"}
            or any(ord(char) < 32 or ord(char) == 127 for char in value)):
        return False
    if full and not value.startswith((
        "refs/heads/", "refs/tags/", "refs/release-evidence/",
    )):
        return False
    if not full and value.startswith("refs/"):
        return False
    forbidden = ("..", "@{", "\\", " ", "~", "^", ":", "?", "*", "[")
    parts = value.split("/")
    return (
        not any(token in value for token in forbidden)
        and all(part and not part.startswith((".", "-")) and not part.endswith((".", ".lock"))
                for part in parts)
    )


def git_topology_errors(topology: Any, fixture_root: Path | None = None) -> list[str]:
    if topology is None:
        return []
    if not isinstance(topology, dict):
        return ["must be an object"]
    allowed = {
        "base_ref", "target_ref", "target_patch", "target_patch_state", "target_patch_states",
        "base_files", "refs", "tags", "absent_refs",
    }
    errors = [f"has unsupported fields: {sorted(set(topology) - allowed)}"] \
        if set(topology) - allowed else []
    base_ref, target_ref = topology.get("base_ref"), topology.get("target_ref")
    for field_name, value in (("base_ref", base_ref), ("target_ref", target_ref)):
        if not _valid_ref_name(value, full=False):
            errors.append(f"{field_name} must be a safe shorthand ref name")
        elif value == "main":
            errors.append(f"{field_name} must not collide with the internal main branch")
    if base_ref == target_ref and isinstance(base_ref, str):
        errors.append("base_ref and target_ref must differ")

    patch = topology.get("target_patch")
    parsed_patch: list[tuple[str, bool, list[list[str]]]] | None = None
    if patch is not None:
        if not isinstance(patch, str) or not PurePosixPath(patch).suffix == ".patch" \
                or not _safe_relative_path(patch):
            errors.append("target_patch must be a safe relative .patch path")
        elif _is_excluded(
            Path(patch), fixture_root / patch if fixture_root is not None else None,
        ):
            errors.append("target_patch is excluded from candidate fixtures")
        elif fixture_root is not None and not (fixture_root / patch).is_file():
            errors.append(f"target_patch does not exist: {patch!r}")
        elif fixture_root is not None:
            try:
                parsed_patch = _parse_fixture_patch(fixture_root / patch)
                missing = [relative for relative, _is_new, _hunks in parsed_patch
                           if not (fixture_root / relative).is_file()]
                if missing:
                    errors.append(f"target_patch target files do not exist: {missing}")
                for relative, is_new, hunks in parsed_patch:
                    candidate = fixture_root / relative
                    if is_new and candidate.is_file():
                        expected = "".join(
                            f"{line[1:]}\n" for hunk in hunks for line in hunk
                            if line.startswith("+")
                        ).encode()
                        if candidate.read_bytes() != expected:
                            errors.append(
                                f"target_patch new-file bytes do not exactly match {relative!r}"
                            )
                applies = subprocess.run(
                    ["git", "apply", "--check", "--reverse", "--", patch],
                    cwd=fixture_root, capture_output=True, text=True,
                )
                if applies.returncode:
                    errors.append("target_patch does not apply to current fixture bytes")
            except ValueError as exc:
                errors.append(f"target_patch is not a supported fixture patch: {exc}")
    if "target_patch_state" in topology:
        state = topology["target_patch_state"]
        if not isinstance(state, str) or state not in {"committed", "uncommitted", "staged"}:
            errors.append("target_patch_state must be committed, uncommitted, or staged")
        if patch is None:
            errors.append("target_patch_state requires target_patch")
    states = topology.get("target_patch_states")
    if states is not None:
        if "target_patch_state" in topology:
            errors.append("target_patch_state and target_patch_states are mutually exclusive")
        if patch is None:
            errors.append("target_patch_states requires target_patch")
        if not isinstance(states, dict):
            errors.append("target_patch_states must be an object")
        else:
            for relative, value in states.items():
                if not isinstance(relative, str) or not _safe_relative_path(relative):
                    errors.append(f"target_patch_states has unsafe path {relative!r}")
                if not isinstance(value, str) or value not in {
                    "committed", "staged", "unstaged", "untracked",
                }:
                    errors.append(f"target_patch_states[{relative!r}] has invalid state")
            if parsed_patch is not None:
                patch_kinds = {relative: is_new for relative, is_new, _hunks in parsed_patch}
                if set(states) != set(patch_kinds):
                    errors.append("target_patch_states must exactly cover target_patch paths")
                for relative, value in states.items():
                    if relative in patch_kinds and value == "untracked" and not patch_kinds[relative]:
                        errors.append(f"target_patch_states[{relative!r}] untracked requires /dev/null addition")
                    if relative in patch_kinds and value == "unstaged" and patch_kinds[relative]:
                        errors.append(f"target_patch_states[{relative!r}] new file must be staged or untracked")

    base_files = topology.get("base_files", [])
    if not isinstance(base_files, list):
        errors.append("base_files must be an array")
    else:
        targets: set[str] = set()
        for index, entry in enumerate(base_files):
            if not isinstance(entry, dict) or set(entry) != {"source", "path"}:
                errors.append(f"base_files[{index}] must contain only source and path")
                continue
            source, target = entry["source"], entry["path"]
            if not all(isinstance(value, str) and _safe_relative_path(value)
                       for value in (source, target)):
                errors.append(f"base_files[{index}] paths must be safe and relative")
                continue
            if source == target or target in targets:
                errors.append(f"base_files[{index}] target must be unique and differ from source")
            source_path = fixture_root / source if fixture_root is not None else None
            if _is_excluded(
                Path(source), source_path if source_path is not None and source_path.is_file() else None,
            ):
                errors.append(f"base_files[{index}] source is excluded from candidate fixtures")
            if _is_excluded(Path(target)):
                errors.append(f"base_files[{index}] target is excluded from candidate fixtures")
            targets.add(target)
            if fixture_root is not None and not (fixture_root / source).is_file():
                errors.append(f"base_files[{index}] source does not exist: {source!r}")

    tags = topology.get("tags", [])
    refs = topology.get("refs", [])
    present: dict[str, str] = {"refs/heads/main": "internal"}
    if not isinstance(tags, list):
        errors.append("tags must be an array")
        tags = []
    for index, entry in enumerate(tags):
        if not isinstance(entry, dict) or set(entry) != {"name", "target", "kind"}:
            errors.append(f"tags[{index}] must contain only name, target, and kind")
            continue
        name, target, kind = entry["name"], entry["target"], entry["kind"]
        name_ok = _valid_ref_name(name, full=False)
        target_ok = isinstance(target, str) and target in {"base", "target"}
        kind_ok = isinstance(kind, str) and kind in {"lightweight", "annotated"}
        if not name_ok:
            errors.append(f"tags[{index}] has an invalid ref name")
        if not target_ok:
            errors.append(f"tags[{index}].target must be base or target")
        if not kind_ok:
            errors.append(f"tags[{index}].kind must be lightweight or annotated")
        if name_ok and target_ok:
            full_name = f"refs/tags/{name}"
            if full_name in present:
                errors.append(f"duplicate present ref {full_name!r}")
            present[full_name] = target
    if not isinstance(refs, list):
        errors.append("refs must be an array")
        refs = []
    for index, entry in enumerate(refs):
        if not isinstance(entry, dict) or set(entry) != {"name", "target"}:
            errors.append(f"refs[{index}] must contain only name and target")
            continue
        name, target = entry["name"], entry["target"]
        name_ok = _valid_ref_name(name, full=True) and isinstance(name, str) and (
            name.startswith("refs/heads/") or name.startswith("refs/release-evidence/")
        )
        target_ok = isinstance(target, str) and target in {"base", "target"}
        if not name_ok:
            errors.append(
                f"refs[{index}] has an invalid ref name; only refs/heads/* and "
                "refs/release-evidence/* are allowed"
            )
        elif name == "refs/heads/main":
            errors.append("refs must not override the internal main branch")
            name_ok = False
        if not target_ok:
            errors.append(f"refs[{index}].target must be base or target")
        if name_ok and target_ok:
            if name in present:
                errors.append(f"duplicate present ref {name!r}")
            present[name] = target

    implicit: set[str] = set()
    for logical, alias in (("base", base_ref), ("target", target_ref)):
        if not _valid_ref_name(alias, full=False):
            continue
        tag_name = f"refs/tags/{alias}"
        if tag_name in present:
            if present[tag_name] != logical:
                errors.append(f"{logical}_ref tag must target {logical}")
        else:
            implicit.add(f"refs/heads/{alias}")
    for name in implicit:
        if name in present:
            errors.append(f"explicit refs must not override implicit ref {name!r}")
        present[name] = "implicit"
    head_names = {
        name.removeprefix("refs/heads/") for name in present
        if name.startswith("refs/heads/")
    }
    tag_names = {
        name.removeprefix("refs/tags/") for name in present
        if name.startswith("refs/tags/")
    }
    for name in sorted(head_names & tag_names):
        errors.append(f"head and tag share ambiguous short name {name!r}")

    absent = topology.get("absent_refs", [])
    if not isinstance(absent, list):
        errors.append("absent_refs must be an array")
    else:
        seen_absent: set[str] = set()
        for index, name in enumerate(absent):
            if not _valid_ref_name(name, full=True):
                errors.append(f"absent_refs[{index}] has an invalid ref name")
                continue
            if name in seen_absent:
                errors.append(f"absent_refs duplicates {name!r}")
            if name in present:
                errors.append(f"ref {name!r} is both present and absent")
            seen_absent.add(name)
    return errors


def _safe_relative_path(value: str) -> bool:
    path = PurePosixPath(value)
    return bool(
        value and not path.is_absolute() and ".." not in path.parts
        and all(part and not part.startswith("-") for part in path.parts)
        and not any(ord(char) < 32 or ord(char) == 127 for char in value)
    )


def _parse_fixture_patch(path: Path) -> list[tuple[str, bool, list[list[str]]]]:
    blocks = path.read_text(encoding="utf-8").split("diff --git ")[1:]
    parsed: list[tuple[str, bool, list[list[str]]]] = []
    if not blocks:
        raise ValueError("missing diff --git block")
    for block in blocks:
        lines = block.splitlines()
        header = lines[0].split()
        if len(header) != 2 or not header[0].startswith("a/") or not header[1].startswith("b/"):
            raise ValueError("diff paths must use matching a/ and b/ paths")
        target_path = header[1][2:]
        if header[0][2:] != target_path or not _safe_relative_path(target_path):
            raise ValueError(f"unsafe or renamed path {target_path!r}")
        try:
            old_header = next(line for line in lines[1:] if line.startswith("--- "))[4:]
            new_header = next(line for line in lines[1:] if line.startswith("+++ "))[4:]
        except StopIteration as exc:
            raise ValueError(f"missing file headers for {target_path!r}") from exc
        is_new = old_header == "/dev/null"
        if new_header != f"b/{target_path}" or (not is_new and old_header != f"a/{target_path}"):
            raise ValueError(f"file headers do not match {target_path!r}")
        hunks: list[list[str]] = []
        index = 0
        while index < len(lines):
            if not lines[index].startswith("@@"):
                index += 1
                continue
            match = re.fullmatch(
                r"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@(?: .*)?",
                lines[index],
            )
            if not match:
                raise ValueError(f"invalid unified hunk header for {target_path!r}")
            old_count = int(match.group(2) or 1)
            new_count = int(match.group(4) or 1)
            index += 1
            hunk: list[str] = []
            while index < len(lines) and not lines[index].startswith("@@"):
                line = lines[index]
                if line.startswith(("diff --git ", "\\ No newline")):
                    break
                if line[:1] not in {" ", "+", "-"}:
                    raise ValueError(f"invalid unified hunk body for {target_path!r}")
                hunk.append(line)
                index += 1
            if sum(line[:1] in {" ", "-"} for line in hunk) != old_count \
                    or sum(line[:1] in {" ", "+"} for line in hunk) != new_count:
                raise ValueError(f"unified hunk counts do not match for {target_path!r}")
            hunks.append(hunk)
        if not hunks:
            raise ValueError(f"missing unified hunk for {target_path!r}")
        removed = [line[1:] for hunk in hunks for line in hunk if line.startswith("-")]
        added = [line[1:] for hunk in hunks for line in hunk if line.startswith("+")]
        if removed and not added:
            raise ValueError(f"deletion-only fixture patch is unsupported for {target_path!r}")
        if removed == added:
            raise ValueError(f"no-op fixture patch is unsupported for {target_path!r}")
        parsed.append((target_path, is_new, hunks))
    return parsed


def _replace_unique(lines: list[str], old: list[str], new: list[str], path: str) -> list[str]:
    matches = [index for index in range(len(lines) - len(old) + 1)
               if lines[index:index + len(old)] == old]
    if len(matches) != 1:
        raise ValueError(f"patch context for {path!r} matched {len(matches)} locations")
    index = matches[0]
    return lines[:index] + new + lines[index + len(old):]


def _reverse_hunk(lines: list[str], hunk: list[str], path: str) -> list[str]:
    current = [line[1:] for line in hunk if line[:1] in {" ", "+"}]
    previous = [line[1:] for line in hunk if line[:1] in {" ", "-"}]
    if not any(line.startswith("+") for line in hunk):
        raise ValueError(f"deletion-only fixture patch is unsupported for {path!r}")
    return _replace_unique(lines, current, previous, path)


def _reverse_fixture_patch(workspace: Path, patch: Path) -> dict[str, bool]:
    changed: dict[str, bool] = {}
    for relative, is_new, hunks in _parse_fixture_patch(patch):
        target = workspace / relative
        changed[relative] = is_new
        if is_new:
            remove_path(target)
            continue
        trailing_newline = target.read_bytes().endswith(b"\n")
        lines = target.read_text(encoding="utf-8").splitlines()
        for hunk in reversed(hunks):
            lines = _reverse_hunk(lines, hunk, relative)
        target.write_text("\n".join(lines) + ("\n" if trailing_newline else ""), encoding="utf-8")
    return changed


def _restore_paths(workspace: Path, canonical_root: Path, paths: list[str]) -> None:
    for relative in paths:
        source, target = canonical_root / relative, workspace / relative
        if source.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        else:
            remove_path(target)


def _commit(workspace: Path, message: str) -> str:
    _git(workspace, "add", "-A")
    _git(workspace, "-c", "user.name=Repository Maintainer", "-c",
         "user.email=maintainer@example.invalid", "commit", "-q",
         "--allow-empty", "-m", message)
    return _git_output(workspace, "rev-parse", "HEAD")


def _copy_base_files(workspace: Path, topology: dict[str, Any]) -> None:
    for entry in topology.get("base_files", []):
        source, target = workspace / entry["source"], workspace / entry["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def _restore_base_file_targets(
    workspace: Path, canonical_root: Path, topology: dict[str, Any],
) -> None:
    for entry in topology.get("base_files", []):
        source, target = canonical_root / entry["path"], workspace / entry["path"]
        if source.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        else:
            remove_path(target)


def _patch_states(topology: dict[str, Any], paths: dict[str, bool]) -> dict[str, str]:
    declared = topology.get("target_patch_states")
    if isinstance(declared, dict):
        return declared
    state = topology.get("target_patch_state", "committed")
    if state != "uncommitted":
        return {path: state for path in paths}
    return {path: "untracked" if is_new else "unstaged" for path, is_new in paths.items()}


def _topology_evidence(workspace: Path, topology: dict[str, Any]) -> dict[str, Any]:
    def resolve(name: str) -> dict[str, Any]:
        return {
            "present": True,
            "object": _git_output(workspace, "rev-parse", "--verify", name),
            "commit": _git_output(workspace, "rev-parse", "--verify", f"{name}^{{commit}}"),
            "tree": _git_output(workspace, "rev-parse", "--verify", f"{name}^{{tree}}"),
        }

    evidence: dict[str, Any] = {
        "base_ref": {"name": topology["base_ref"], **resolve(topology["base_ref"])},
        "target_ref": {"name": topology["target_ref"], **resolve(topology["target_ref"])},
        "refs": {}, "tags": {}, "absent_refs": {},
        "status_porcelain": _git_output(
            workspace, "status", "--porcelain=v1", "--untracked-files=all",
        ),
    }
    for entry in topology.get("refs", []):
        evidence["refs"][entry["name"]] = resolve(entry["name"])
    for entry in topology.get("tags", []):
        name = f"refs/tags/{entry['name']}"
        evidence["tags"][name] = {
            **resolve(name),
            "kind": _git_output(workspace, "cat-file", "-t", name),
        }
    for name in topology.get("absent_refs", []):
        result = subprocess.run(
            ["git", "rev-parse", "--verify", name], cwd=workspace,
            capture_output=True, text=True,
        )
        evidence["absent_refs"][name] = {"present": result.returncode == 0}
    custom_refs = [
        entry["name"] for entry in topology.get("refs", [])
        if entry["name"].startswith("refs/release-evidence/")
    ]
    if custom_refs:
        clone_root = Path(tempfile.mkdtemp(prefix="repository-clone-", dir=workspace))
        clone = clone_root / "checkout"
        try:
            _git(workspace, "clone", "-q", "--no-local", ".", str(clone))
            evidence["fresh_clone"] = {
                "custom_refs": {
                    name: {
                        "source_present": subprocess.run(
                            ["git", "rev-parse", "--verify", name], cwd=workspace,
                            capture_output=True,
                        ).returncode == 0,
                        "clone_present": subprocess.run(
                            ["git", "rev-parse", "--verify", name], cwd=clone,
                            capture_output=True,
                        ).returncode == 0,
                    }
                    for name in custom_refs
                },
                "tags": {
                    (name := f"refs/tags/{entry['name']}"): {
                        "clone_present": subprocess.run(
                            ["git", "rev-parse", "--verify", name], cwd=clone,
                            capture_output=True,
                        ).returncode == 0,
                        "tree_matches": _git_output(
                            workspace, "rev-parse", f"{name}^{{tree}}",
                        ) == _git_output(clone, "rev-parse", f"{name}^{{tree}}"),
                    }
                    for entry in topology.get("tags", [])
                },
            }
        finally:
            remove_path(clone_root)
        evidence["fresh_clone"]["cleaned"] = not clone_root.exists()
    return evidence


def _init_git(
    workspace: Path, canonical_root: Path, topology: dict[str, Any] | None,
) -> dict[str, Any]:
    _git(workspace, "init", "-q", "-b", "main")
    if topology is None:
        _commit(workspace, "repository snapshot")
        return {}
    errors = git_topology_errors(topology, workspace)
    if errors:
        raise ValueError("invalid git_topology: " + "; ".join(errors))
    patch = topology.get("target_patch")
    patch_paths = _reverse_fixture_patch(workspace, workspace / patch) if patch else {}
    states = _patch_states(topology, patch_paths)
    _copy_base_files(workspace, topology)
    base = _commit(workspace, "repository baseline snapshot")
    committed = [path for path, state in states.items() if state == "committed"]
    _restore_paths(workspace, canonical_root, committed)
    target = _commit(workspace, "release candidate snapshot")
    _restore_base_file_targets(workspace, canonical_root, topology)
    pending = [path for path, state in states.items() if state != "committed"]
    _restore_paths(workspace, canonical_root, pending)
    staged = [path for path, state in states.items() if state == "staged"]
    if staged:
        _git(workspace, "add", "--", *staged)

    tags = {entry["name"]: entry for entry in topology.get("tags", [])}
    for logical, alias, commit in (
        ("base", topology["base_ref"], base), ("target", topology["target_ref"], target),
    ):
        if alias not in tags:
            _git(workspace, "update-ref", f"refs/heads/{alias}", commit)
    for entry in topology.get("refs", []):
        _git(workspace, "update-ref", entry["name"], base if entry["target"] == "base" else target)
    for entry in topology.get("tags", []):
        commit = base if entry["target"] == "base" else target
        if entry["kind"] == "annotated":
            _git(workspace, "-c", "user.name=Repository Maintainer", "-c",
                 "user.email=maintainer@example.invalid", "tag", "-a", entry["name"],
                 "-m", f"Release {entry['name']}", commit)
        else:
            _git(workspace, "tag", entry["name"], commit)
    evidence = _topology_evidence(workspace, topology)
    if evidence["base_ref"]["commit"] == evidence["target_ref"]["commit"]:
        raise ValueError("invalid git_topology: base and target resolved to the same commit")
    if patch and "committed" in states.values() and _git_output(
        workspace, "rev-parse", f"{base}^{{tree}}",
    ) == _git_output(workspace, "rev-parse", f"{target}^{{tree}}"):
        raise ValueError("invalid git_topology: committed target_patch did not change target tree")
    if _git_output(workspace, "rev-parse", "HEAD") != target:
        raise ValueError("invalid git_topology: internal HEAD no longer resolves to target")
    if any(not item["present"] for item in evidence["refs"].values()) \
            or any(not item["present"] for item in evidence["tags"].values()) \
            or any(item["present"] for item in evidence["absent_refs"].values()):
        raise ValueError("invalid git_topology: present/absent ref evidence does not match")
    return evidence


def _copy_auth(codex_home: Path, auth_source: Path | None) -> None:
    codex_home.mkdir(parents=True, exist_ok=True)
    os.chmod(codex_home, stat.S_IRWXU)
    if auth_source is None:
        active_home = Path(
            os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))
        )
        auth_source = active_home / "auth.json"
    if not auth_source.is_file():
        return
    auth_target = codex_home / "auth.json"
    shutil.copy2(auth_source, auth_target)
    os.chmod(auth_target, stat.S_IRUSR | stat.S_IWUSR)


def _safe_skill_source(path: Path, repository_root: Path) -> Path:
    resolved = path.resolve()
    repository_root = repository_root.resolve()
    if not resolved.is_relative_to(repository_root):
        raise ValueError(f"skill dependency escapes repository: {path}")
    if resolved.name == "SKILL.md":
        resolved = resolved.parent
    if not (resolved / "SKILL.md").is_file():
        raise ValueError(f"skill source is missing SKILL.md: {resolved}")
    return resolved


def content_tree_hash(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(value for value in root.rglob("*") if value.is_file()):
        digest.update(path.relative_to(root).as_posix().encode())
        digest.update(b"\0")
        digest.update(hashlib.sha256(path.read_bytes()).digest())
    return digest.hexdigest()


def skill_overlay_hash(skill_sources: list[Path], repository_root: Path) -> str:
    overlay = {
        source.relative_to(repository_root.resolve()).as_posix(): content_tree_hash(source)
        for source in (_safe_skill_source(path, repository_root) for path in skill_sources)
    }
    return hashlib.sha256(json.dumps(
        overlay, sort_keys=True, separators=(",", ":"),
    ).encode()).hexdigest()


def _labeled_overlay_hash(skill_sources: tuple[Path, ...], labels: tuple[str, ...]) -> str:
    overlay = {
        label: content_tree_hash(source) for source, label in zip(skill_sources, labels)
    }
    return hashlib.sha256(json.dumps(
        overlay, sort_keys=True, separators=(",", ":"),
    ).encode()).hexdigest()


def _lock_skill_overlay(
    runtime_root: Path, skill_sources: tuple[Path, ...], repository_root: Path,
) -> tuple[tuple[Path, ...], str]:
    locked_root = runtime_root / "locked-inputs/skill-overlay"
    locked: list[Path] = []
    labels: list[str] = []
    for index, source in enumerate(skill_sources):
        destination = locked_root / str(index) / source.name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, destination)
        locked.append(destination)
        labels.append(source.relative_to(repository_root).as_posix())
        for path in destination.rglob("*"):
            if path.is_file():
                path.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    locked_tuple = tuple(locked)
    return locked_tuple, _labeled_overlay_hash(locked_tuple, tuple(labels))


def _install_skill_overlay(
    workspace: Path, skill_sources: list[tuple[Path, str]],
) -> tuple[str, ...]:
    installed: list[str] = []
    seen_names: set[str] = set()
    for source, source_label in skill_sources:
        if source.name in seen_names:
            raise ValueError(f"skill overlay name collision: {source.name}")
        seen_names.add(source.name)
        destination = workspace / ".agents" / "skills" / source.name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, destination)
        installed.append(source_label)
    return tuple(installed)


@dataclass
class IsolatedContext:
    mode: str
    outer_root: Path
    workspace_root: Path
    git_root: Path
    home: Path
    codex_home: Path
    fixture_manifest: dict[str, str] = field(default_factory=dict)
    fixture_hash: str = ""
    skill_sources: tuple[str, ...] = ()
    permission_profile: str = ""
    profile_text: str = ""
    git_topology: dict[str, Any] = field(default_factory=dict)
    topology_matches: bool = True
    dependency_evidence: dict[str, Any] = field(default_factory=dict)

    @property
    def env(self) -> dict[str, str]:
        return {
            **os.environ, "HOME": str(self.home), "CODEX_HOME": str(self.codex_home),
            "NPM_CONFIG_UPDATE_NOTIFIER": "false", "NPM_CONFIG_OFFLINE": "true",
            "NPM_CONFIG_AUDIT": "false", "NPM_CONFIG_FUND": "false",
            "NPM_CONFIG_SCRIPT_SHELL": "/bin/sh",
        }

    def cleanup(self) -> None:
        remove_path(self.outer_root)


@dataclass
class PreflightResult:
    status: str
    checks: dict[str, bool]
    blockers: list[str]
    fixture_hash: str
    prompt_hash: str
    skill_visibility: dict[str, list[str]]
    permission_probes: dict[str, dict[str, Any]]
    git_topology: dict[str, dict[str, Any]] = field(default_factory=dict)
    dependencies: dict[str, dict[str, Any]] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        return vars(self)


@dataclass
class MaterializedEvalRun:
    repository_root: Path
    runtime_root: Path
    canonical_root: Path
    canonical_manifest: dict[str, str]
    canonical_hash: str
    prompt: str
    prompt_hash: str
    runtime_isolation: dict[str, Any]
    model_available: bool | None
    skill_source_paths: tuple[Path, ...]
    expected_skill_sources: tuple[str, ...]
    locked_overlay_hash: str
    locked_judge_schema_path: Path | None
    locked_judge_schema_hash: str | None
    preflight: PreflightResult | None
    preflight_path: Path
    source_probe_path: Path
    auth_source: Path | None
    dependency_staging: tuple[tuple[str, Path, str], ...] = ()
    dependency_evidence: dict[str, Any] = field(default_factory=dict)
    git_topology: dict[str, Any] | None = None
    git_topology_snapshot: dict[str, Any] | None = None
    active_context: IsolatedContext | None = None
    phase: str = "ready"
    preflight_results: dict[str, PreflightResult] = field(default_factory=dict)

    def cleanup(self) -> None:
        if self.active_context:
            self.active_context.cleanup()
            self.active_context = None
        remove_path(self.runtime_root / "dependencies")


def _run_locked_npm_ci(staging: Path) -> subprocess.CompletedProcess[str]:
    npm = shutil.which("npm")
    if not npm:
        return subprocess.CompletedProcess([], 127, "", "npm is unavailable")
    return subprocess.run(
        [npm, "ci", "--ignore-scripts", "--no-audit", "--no-fund"],
        cwd=staging, capture_output=True, text=True,
        env={**os.environ, "npm_config_ignore_scripts": "true"},
    )


def _dependency_tree_hash(root: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix().encode()
        if path.is_symlink():
            value = b"link\0" + os.readlink(path).encode()
        elif path.is_file():
            value = b"file\0" + hashlib.sha256(path.read_bytes()).digest()
        else:
            continue
        digest.update(relative + b"\0" + value)
    return digest.hexdigest()


def _materialize_dependencies(
    canonical_root: Path, runtime_root: Path,
) -> tuple[tuple[tuple[str, Path, str], ...], dict[str, Any]]:
    locks = sorted(canonical_root.rglob("package-lock.json"))
    if not locks:
        return (), {"status": "NOT_REQUIRED", "sites": []}
    staging_root = runtime_root / "dependencies"
    staging: list[tuple[str, Path, str]] = []
    sites: list[dict[str, Any]] = []
    for index, lock in enumerate(locks):
        relative = lock.parent.relative_to(canonical_root).as_posix()
        package = lock.parent / "package.json"
        if not package.is_file():
            sites.append({"path": relative, "status": "BLOCKED", "error": "package.json missing"})
            continue
        destination = staging_root / str(index)
        destination.mkdir(parents=True)
        shutil.copy2(package, destination / "package.json")
        shutil.copy2(lock, destination / "package-lock.json")
        lock_payload = json.loads(lock.read_text(encoding="utf-8"))
        package_payload = json.loads(package.read_text(encoding="utf-8"))
        declared = {
            name for field in ("dependencies", "devDependencies", "optionalDependencies")
            for name in package_payload.get(field, {})
        }
        manifest = [
            {"path": path, "version": value.get("version"), "integrity": value.get("integrity")}
            for path, value in sorted(lock_payload.get("packages", {}).items())
            if path and isinstance(value, dict)
        ]
        manifest_hash = hashlib.sha256(json.dumps(
            manifest, sort_keys=True, separators=(",", ":"),
        ).encode()).hexdigest()
        completed = _run_locked_npm_ci(destination)
        modules = destination / "node_modules"
        status = "PASS" if completed.returncode == 0 and modules.is_dir() else "BLOCKED"
        tree_hash = _dependency_tree_hash(modules) if status == "PASS" else None
        sites.append({
            "path": relative,
            "lock_sha256": hashlib.sha256(lock.read_bytes()).hexdigest(),
            "dependency_manifest": manifest,
            "dependency_manifest_sha256": manifest_hash,
            "node_modules_sha256": tree_hash,
            "probe_package": min(declared) if declared else None,
            "install_command": "npm ci --ignore-scripts --no-audit --no-fund",
            "status": status,
            "error": "" if status == "PASS" else completed.stderr[-2000:],
        })
        if status == "PASS":
            staging.append((relative, modules, tree_hash))
    status = "PASS" if sites and all(site["status"] == "PASS" for site in sites) else "BLOCKED"
    return tuple(staging), {"status": status, "sites": sites}


def _install_runtime_dependencies(
    workspace: Path, staging: tuple[tuple[str, Path, str], ...],
) -> dict[str, Any]:
    sites: list[dict[str, Any]] = []
    exclude = workspace / ".git/info/exclude"
    for relative, source, expected_hash in staging:
        destination = workspace / relative / "node_modules"
        shutil.copytree(source, destination, symlinks=True)
        observed_hash = _dependency_tree_hash(destination)
        package = json.loads((workspace / relative / "package.json").read_text(encoding="utf-8"))
        declared = {
            name for field in ("dependencies", "devDependencies", "optionalDependencies")
            for name in package.get(field, {})
        }
        sites.append({
            "path": relative, "node_modules_sha256": observed_hash,
            "expected_sha256": expected_hash,
            "probe_package": min(declared) if declared else None,
            "matches_staging": observed_hash == expected_hash,
        })
        with exclude.open("a", encoding="utf-8") as handle:
            prefix = "" if relative == "." else f"{relative}/"
            handle.write(f"/{prefix}node_modules/\n")
    return {"status": "PASS" if all(site["matches_staging"] for site in sites) else "BLOCKED",
            "sites": sites}


def _runtime_read_roots() -> tuple[Path, ...]:
    roots: set[Path] = set()
    xcode_select = shutil.which("xcode-select")
    if xcode_select:
        developer = subprocess.run([xcode_select, "-p"], capture_output=True, text=True)
        if developer.returncode == 0:
            roots.add(Path(developer.stdout.strip()))
    roots.add(Path("/System/Library/OpenSSL"))
    for name in ("node", "npm", "python3"):
        executable = shutil.which(name)
        if not executable:
            continue
        resolved = Path(executable).resolve()
        for parent in resolved.parents:
            if (parent / "bin" / name).exists() or (
                name == "npm" and (parent / "bin/node").exists()
            ):
                roots.add(parent)
                break
    broad = {Path("/"), Path("/usr"), Path("/opt"), Path("/System"), Path("/Library"), Path.home()}
    return tuple(sorted(path for path in roots if path.is_dir() and path not in broad))


def _profile_text(
    profile: str, writable: bool, home: Path, codex_home: Path,
    dependency_sites: tuple[str, ...] = (),
) -> str:
    access = "write" if writable else "read"
    protected = f'\n".git" = "{access}"\n".agents" = "read"'
    runtime_access = "".join(
        f'\n{json.dumps(str(path))} = "read"'
        for path in (*_runtime_read_roots(), Path("/bin/sh")) if path.exists()
    )
    dependency_access = "".join(
        f'\n{json.dumps("node_modules" if site == "." else f"{site}/node_modules")} = "read"'
        for site in dependency_sites
    )
    return f'''default_permissions = "{profile}"

[permissions.{profile}.filesystem]
":root" = "deny"
":minimal" = "read"
{json.dumps(str(home))} = "{access}"
{json.dumps(str(codex_home))} = "deny"{runtime_access}

[permissions.{profile}.filesystem.":workspace_roots"]
"." = "{access}"{protected}{dependency_access}

[permissions.{profile}.network]
enabled = false
'''


def _new_context(
    mode: str,
    repository_root: Path,
    auth_source: Path | None,
    *,
    canonical_root: Path | None = None,
    skill_sources: list[tuple[Path, str]] | None = None,
    git_topology: dict[str, Any] | None = None,
    dependency_staging: tuple[tuple[str, Path, str], ...] = (),
) -> IsolatedContext:
    prefix = "review-workspace-" if mode == "judge" else "candidate-workspace-"
    outer_root = Path(tempfile.mkdtemp(prefix=prefix))
    workspace = outer_root / "workspace"
    home = outer_root / "home"
    codex_home = outer_root / "codex-home"
    home.mkdir(mode=0o700)
    _copy_auth(codex_home, auth_source)
    if canonical_root is None:
        workspace.mkdir()
    else:
        copy_canonical_fixture(canonical_root, workspace)
    topology_evidence = _init_git(workspace, canonical_root or workspace, git_topology)
    installed = _install_skill_overlay(workspace, skill_sources or [])
    if installed:
        (workspace / ".git/info/exclude").write_text("/.agents/\n", encoding="utf-8")
    dependency_evidence = _install_runtime_dependencies(workspace, dependency_staging)
    profile = "eval-judge" if mode == "judge" else "eval-candidate"
    dependency_sites = tuple(relative for relative, _source, _hash in dependency_staging)
    profile_text = _profile_text(
        profile, mode != "judge", home, codex_home, dependency_sites,
    )
    (codex_home / "config.toml").write_text(profile_text, encoding="utf-8")
    manifest = fixture_manifest(workspace) if canonical_root else {}
    return IsolatedContext(
        mode, outer_root, workspace, workspace, home, codex_home,
        manifest, manifest_hash(manifest), installed, profile, profile_text,
        topology_evidence,
        True,
        dependency_evidence,
    )


def open_context(materialized: MaterializedEvalRun, mode: str) -> IsolatedContext:
    required_phase = {"without_skill": "ready", "with_skill": "without_locked", "judge": "with_locked"}
    if mode not in required_phase or materialized.active_context or materialized.phase != required_phase[mode]:
        raise RuntimeError(f"cannot open {mode} context during {materialized.phase}")
    sources = list(zip(
        materialized.skill_source_paths, materialized.expected_skill_sources,
    )) if mode == "with_skill" else []
    canonical = materialized.canonical_root if mode != "judge" else None
    context = _new_context(
        mode.replace("_", "-"), materialized.repository_root, materialized.auth_source,
        canonical_root=canonical, skill_sources=sources,
        git_topology=materialized.git_topology if mode != "judge" else None,
        dependency_staging=materialized.dependency_staging if mode != "judge" else (),
    )
    if mode != "judge":
        if materialized.git_topology_snapshot is None:
            materialized.git_topology_snapshot = context.git_topology
        else:
            context.topology_matches = context.git_topology == materialized.git_topology_snapshot
    materialized.active_context = context
    materialized.phase = f"{mode}_active"
    return context


def close_context(
    materialized: MaterializedEvalRun, context: IsolatedContext, *, evidence_locked: bool,
) -> None:
    if materialized.active_context is not context or not evidence_locked:
        raise RuntimeError("active context evidence must be locked before destruction")
    mode = context.mode.replace("-", "_")
    context.cleanup()
    materialized.active_context = None
    materialized.phase = {
        "without_skill": "without_locked", "with_skill": "with_locked", "judge": "complete",
    }[mode]


def _runtime_state_is_proven(value: Any) -> bool:
    if isinstance(value, str):
        return value == "not_used"
    if not isinstance(value, dict):
        return False
    return (
        value.get("state") in {"isolated", "reset"}
        and isinstance(value.get("evidence"), str)
        and bool(value["evidence"].strip())
    )


def validate_runtime_isolation(runtime_isolation: Any) -> tuple[bool, list[str]]:
    blockers: list[str] = []
    if not isinstance(runtime_isolation, dict):
        return False, ["runtime_isolation must be an object"]
    for surface in RUNTIME_SURFACES:
        if surface not in runtime_isolation:
            blockers.append(f"runtime isolation is unknown for {surface}")
        elif not _runtime_state_is_proven(runtime_isolation[surface]):
            blockers.append(f"runtime isolation is not proven for {surface}")
    extras = sorted(set(runtime_isolation) - set(RUNTIME_SURFACES))
    if extras:
        blockers.append(f"runtime_isolation has unsupported surfaces: {extras}")
    return not blockers, blockers


def _visible_overlay_sources(context: IsolatedContext) -> tuple[str, ...]:
    overlay = context.workspace_root / ".agents" / "skills"
    if not overlay.exists():
        return ()
    return tuple(sorted(path.name for path in overlay.iterdir() if path.is_dir()))


def _candidate_tree_findings(
    context: IsolatedContext, repository_root: Path,
) -> tuple[list[str], list[str]]:
    excluded: list[str] = []
    source_refs: list[str] = []
    repository_text = str(repository_root.resolve())
    for path in context.workspace_root.rglob("*"):
        relative = path.relative_to(context.workspace_root)
        if relative.parts[0] in {".agents", ".git"} or "node_modules" in relative.parts:
            continue
        if _is_excluded(relative, path):
            excluded.append(relative.as_posix())
            continue
        if not path.is_file() or path.stat().st_size > 1_000_000:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if path.name == "README.md" and readme_is_eval_scaffolding(path):
            excluded.append(relative.as_posix())
        if repository_text in text:
            source_refs.append(relative.as_posix())
    return excluded, source_refs


def verify_context_dependencies(context: IsolatedContext) -> dict[str, Any]:
    sites = []
    for site in context.dependency_evidence.get("sites", []):
        modules = context.workspace_root / site["path"] / "node_modules"
        observed = _dependency_tree_hash(modules) if modules.is_dir() else None
        sites.append({
            "path": site["path"], "node_modules_sha256": observed,
            "matches_staging": observed == site["expected_sha256"],
        })
    return {
        "status": "PASS" if all(site["matches_staging"] for site in sites) else "BLOCKED",
        "sites": sites,
    }


def _dependency_probe_sites(context: IsolatedContext) -> list[dict[str, Any]]:
    return sorted([
        {"path": site["path"], "package": site["probe_package"]}
        for site in context.dependency_evidence.get("sites", [])
    ], key=lambda site: site["path"])


def run_permission_probe(
    context: IsolatedContext, repository_root: Path, source_probe: Path, *, writable: bool,
    git_ref: str = "HEAD",
) -> dict[str, Any]:
    read_probe = context.workspace_root / ".eval-probe-input"
    write_probe = context.workspace_root / ".eval-probe-output"
    home_probe = context.home / ".eval-probe-output"
    codex_probe = context.codex_home / "auth.json"
    if not codex_probe.exists():
        codex_probe = context.codex_home / "config.toml"
    read_probe.write_text("workspace-visible", encoding="utf-8")
    sibling_root = Path(tempfile.mkdtemp(prefix="boundary-sibling-"))
    sibling_probe = sibling_root / "secret.txt"
    sibling_probe.write_text("must-not-be-visible", encoding="utf-8")
    script = r'''
readable() { line=; if IFS= read -r line < "$1" || [ -n "$line" ]; then printf true; else printf false; fi; }
writable() { if printf probe > "$1"; then printf true; else printf false; fi; }
git_available=false; git_read=false; git_write=false; git_cleanup=false
node_run=null; npm_run=null; python_run=null; dependency_run=null
if /usr/bin/git --version >/dev/null 2>&1; then git_available=true; fi
if /usr/bin/git -C "$7" rev-parse --verify "$8^{commit}" >/dev/null 2>&1; then git_read=true; fi
probe_ref=refs/heads/repository-permission-probe
if /usr/bin/git -C "$7" update-ref "$probe_ref" "$8^{commit}" >/dev/null 2>&1 \
  && /usr/bin/git -C "$7" rev-parse --verify "$probe_ref" >/dev/null 2>&1; then git_write=true; fi
/usr/bin/git -C "$7" update-ref -d "$probe_ref" >/dev/null 2>&1 || true
if ! /usr/bin/git -C "$7" show-ref --verify --quiet "$probe_ref"; then git_cleanup=true; fi
if [ "$9" = true ]; then
  node_run=false; npm_run=false; python_run=false
  if node -e 'process.exit(0)' >/dev/null 2>&1; then node_run=true; fi
  if npm --version >/dev/null 2>&1; then npm_run=true; fi
  if python3 -c 'raise SystemExit(0)' >/dev/null 2>&1; then python_run=true; fi
fi
if [ "${10}" != '[]' ]; then
  dependency_run=false
  if node -e 'const fs=require("fs"),p=require("path"),{createRequire}=require("module");const root=process.argv[1],sites=JSON.parse(process.argv[2]);for(const site of sites){const modules=p.join(root,site.path,"node_modules");if(!fs.readdirSync(modules).length)process.exit(2);if(site.package)createRequire(p.join(root,site.path,"package.json")).resolve(site.package)}' "$7" "${10}" >/dev/null 2>&1; then dependency_run=true; fi
fi
printf '{"workspace_read":%s,"workspace_write":%s,"home_write":%s,"codex_home_read":%s,"source_read":%s,"sibling_read":%s,"git_available":%s,"git_read":%s,"git_write":%s,"git_cleanup":%s,"node_run":%s,"npm_run":%s,"python_run":%s,"dependency_run":%s}\n' \
  "$(readable "$1")" "$(writable "$2")" "$(writable "$3")" \
  "$(readable "$4")" "$(readable "$5")" "$(readable "$6")" \
  "$git_available" "$git_read" "$git_write" "$git_cleanup" \
  "$node_run" "$npm_run" "$python_run" "$dependency_run"
'''
    command = [
        "codex", "sandbox", "-P", context.permission_profile, "-C",
        str(context.workspace_root), "--", "/bin/sh", "-c", script, "probe",
        str(read_probe), str(write_probe), str(home_probe), str(codex_probe),
        str(source_probe), str(sibling_probe), str(context.workspace_root), git_ref,
        "true" if writable else "false",
        json.dumps(_dependency_probe_sites(context)) if writable else "[]",
    ]
    try:
        completed = subprocess.run(command, env=context.env, capture_output=True, text=True, timeout=30)
        observed = json.loads(completed.stdout.strip()) if completed.returncode == 0 else {}
    except (OSError, subprocess.TimeoutExpired, json.JSONDecodeError):
        observed = {}
    finally:
        remove_path(read_probe)
        remove_path(write_probe)
        remove_path(home_probe)
        remove_path(sibling_root)
    expected = {"workspace_read": True, "workspace_write": writable,
                "home_write": writable, "codex_home_read": False,
                "source_read": False, "sibling_read": False,
                "git_available": True, "git_read": True, "git_write": writable,
                "git_cleanup": True,
                "node_run": True if writable else None,
                "npm_run": True if writable else None,
                "python_run": True if writable else None}
    expected["dependency_run"] = (
        True if writable and context.dependency_evidence.get("sites")
        else None
    )
    return {"status": "PASS" if observed == expected else "BLOCKED", **observed}


PermissionProbe = Callable[..., dict[str, Any]]


def evaluate_context_preflight(
    materialized: MaterializedEvalRun, context: IsolatedContext, mode: str,
    permission_probe: PermissionProbe = run_permission_probe,
) -> PreflightResult:
    candidate = mode != "judge"
    root = context.workspace_root.resolve()
    repository = materialized.repository_root.resolve()
    profile = "eval-candidate" if candidate else "eval-judge"
    dependency_sites = tuple(
        relative for relative, _source, _hash in materialized.dependency_staging
    ) if candidate else ()
    expected_profile = _profile_text(
        profile, candidate, context.home, context.codex_home, dependency_sites,
    )
    git_ref = (
        materialized.git_topology["target_ref"]
        if candidate and materialized.git_topology else "HEAD"
    )
    probe = permission_probe(
        context, repository, materialized.source_probe_path,
        writable=candidate, git_ref=git_ref,
    )
    expected_probe = {
        "workspace_read": True, "workspace_write": candidate, "home_write": candidate,
        "codex_home_read": False, "source_read": False, "sibling_read": False,
        "git_available": True, "git_read": True, "git_write": candidate,
        "git_cleanup": True,
        "node_run": True if candidate else None,
        "npm_run": True if candidate else None,
        "python_run": True if candidate else None,
        "dependency_run": True if candidate and materialized.dependency_staging else None,
    }
    runtime_ok, runtime_blockers = validate_runtime_isolation(materialized.runtime_isolation)
    findings = _candidate_tree_findings(context, repository) if candidate else ([], [])
    visible = _visible_overlay_sources(context)
    expected_skills = () if mode == "without_skill" else tuple(
        sorted(PurePosixPath(path).name for path in materialized.expected_skill_sources)
    )
    try:
        current_topology = (
            _topology_evidence(context.workspace_root, materialized.git_topology)
            if candidate and materialized.git_topology else {}
        )
    except subprocess.CalledProcessError:
        current_topology = {"invalid": True}
    topology_ok = not candidate or (
        context.topology_matches
        and context.git_topology == materialized.git_topology_snapshot
        and context.git_topology == current_topology
    )
    current_dependencies = verify_context_dependencies(context)
    dependency_ok = not candidate or (
        materialized.dependency_evidence.get("status") in {"PASS", "NOT_REQUIRED"}
        and current_dependencies.get("status") == "PASS"
    )
    current_locked_overlay_hash = _labeled_overlay_hash(
        materialized.skill_source_paths, materialized.expected_skill_sources,
    )
    current_locked_schema_hash = (
        hashlib.sha256(materialized.locked_judge_schema_path.read_bytes()).hexdigest()
        if materialized.locked_judge_schema_path is not None
        and materialized.locked_judge_schema_path.is_file() else None
    )
    locked_inputs_ok = (
        current_locked_overlay_hash == materialized.locked_overlay_hash
        and current_locked_schema_hash == materialized.locked_judge_schema_hash
    )
    checks = {
        "workspace": (context.git_root / ".git").is_dir(),
        "fixture": not candidate or (
            fixture_manifest(context.workspace_root) == materialized.canonical_manifest
            and context.fixture_hash == materialized.canonical_hash
        ),
        "prompt": hashlib.sha256(materialized.prompt.encode()).hexdigest() == materialized.prompt_hash,
        "exclusions": not findings[0],
        "skill_visibility": not candidate or visible == expected_skills,
        "source_isolation": (
            not repository.is_relative_to(root) and not root.is_relative_to(repository)
            and str(repository) not in materialized.prompt and not findings[1]
        ),
        "permission_profile": (
            context.permission_profile == profile and context.profile_text == expected_profile
            and (context.codex_home / "config.toml").read_text(encoding="utf-8") == expected_profile
        ),
        "os_boundary": probe.get("status") == "PASS" and all(
            probe.get(name) is expected for name, expected in expected_probe.items()
        ),
        "model": materialized.model_available is True,
        "runtime": runtime_ok,
        "git_topology": topology_ok,
        "dependencies": dependency_ok,
        "locked_inputs": locked_inputs_ok,
        "judge": candidate or (
            materialized.phase == "judge_active"
            and (context.workspace_root / "judge-package.json").is_file()
            and (context.workspace_root / "fixture").is_dir()
        ),
    }
    messages = {
        "workspace": "independent workspace, Git, HOME, or CODEX_HOME is not proven",
        "fixture": "candidate fixture differs from the canonical fixture",
        "prompt": "candidate prompt bytes differ from the locked prompt",
        "exclusions": "candidate-visible tree contains excluded eval scaffolding",
        "skill_visibility": "skill visibility differs from the exact declared overlay",
        "source_isolation": "source repository path isolation is not proven",
        "permission_profile": "least-privilege permission profile is not exact",
        "os_boundary": "OS profile probe did not prove Git/workspace/HOME access and source/sibling/CODEX_HOME denial",
        "model": "gpt-5.6-luna availability is false or unknown",
        "git_topology": "declared Git commits, refs, or lane topology are not proven identical",
        "dependencies": "locked dependency materialization is unavailable or differs between lanes",
        "locked_inputs": "locked skill overlay or judge schema changed during the eval run",
        "judge": "fresh judge context is not ready or lacks locked evidence",
    }
    blockers = [message for name, message in messages.items() if not checks[name]] + runtime_blockers
    return PreflightResult(
        "PASS" if all(checks.values()) else "BLOCKED", checks, blockers,
        materialized.canonical_hash, materialized.prompt_hash, {mode: list(visible)}, {mode: probe},
        {mode: context.git_topology},
        {mode: {"materialized": materialized.dependency_evidence,
                "lane": current_dependencies}},
    )


def record_preflight(
    materialized: MaterializedEvalRun, mode: str, result: PreflightResult,
) -> PreflightResult:
    materialized.preflight_results[mode] = result
    checks = {f"{lane}.{name}": passed for lane, current in materialized.preflight_results.items()
              for name, passed in current.checks.items()}
    combined = PreflightResult(
        "PASS" if checks and all(checks.values()) else "BLOCKED", checks,
        [f"{lane}: {blocker}" for lane, current in materialized.preflight_results.items()
         for blocker in current.blockers], materialized.canonical_hash, materialized.prompt_hash,
        {lane: values for current in materialized.preflight_results.values()
         for lane, values in current.skill_visibility.items()},
        {lane: values for current in materialized.preflight_results.values()
         for lane, values in current.permission_probes.items()},
        {lane: values for current in materialized.preflight_results.values()
         for lane, values in current.git_topology.items()},
        {lane: values for current in materialized.preflight_results.values()
         for lane, values in current.dependencies.items()},
    )
    materialized.preflight = combined
    materialized.preflight_path.parent.mkdir(parents=True, exist_ok=True)
    materialized.preflight_path.write_text(
        json.dumps(combined.as_dict(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8",
    )
    return combined


def materialize_eval_run(
    *,
    fixture_root: Path, repository_root: Path, target_skill: Path,
    skill_dependencies: list[Path], prompt: str, runtime_isolation: dict[str, Any],
    runtime_root: Path, model_available: bool | None,
    cleanup_paths: list[str] | None = None,
    auth_source: Path | None = None,
    git_topology: dict[str, Any] | None = None,
    judge_schema_bytes: bytes | None = None,
) -> MaterializedEvalRun:
    repository_root = repository_root.resolve()
    reset_directory(runtime_root)
    canonical_root = runtime_root / "canonical"
    copy_canonical_fixture(fixture_root, canonical_root, cleanup_paths=cleanup_paths)
    canonical_manifest = fixture_manifest(canonical_root)
    canonical_hash = manifest_hash(canonical_manifest)
    dependency_staging, dependency_evidence = _materialize_dependencies(
        canonical_root, runtime_root,
    )
    topology_errors = git_topology_errors(git_topology, canonical_root)
    if topology_errors:
        raise ValueError("invalid git_topology: " + "; ".join(topology_errors))
    sources = [target_skill, *skill_dependencies]
    safe_sources = tuple(_safe_skill_source(path, repository_root) for path in sources)
    expected_sources = tuple(path.relative_to(repository_root).as_posix() for path in safe_sources)
    locked_sources, locked_overlay_hash = _lock_skill_overlay(
        runtime_root, safe_sources, repository_root,
    )
    locked_schema_path: Path | None = None
    locked_schema_hash: str | None = None
    if judge_schema_bytes is not None:
        locked_schema_path = runtime_root / "locked-inputs/eval_judge_result.schema.json"
        locked_schema_path.parent.mkdir(parents=True, exist_ok=True)
        locked_schema_path.write_bytes(judge_schema_bytes)
        locked_schema_path.chmod(stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
        locked_schema_hash = hashlib.sha256(judge_schema_bytes).hexdigest()
    prompt_hash = hashlib.sha256(prompt.encode()).hexdigest()
    materialized = MaterializedEvalRun(
        repository_root=repository_root, runtime_root=runtime_root, canonical_root=canonical_root,
        canonical_manifest=canonical_manifest, canonical_hash=canonical_hash, prompt=prompt,
        prompt_hash=prompt_hash, runtime_isolation=runtime_isolation,
        model_available=model_available, skill_source_paths=locked_sources,
        expected_skill_sources=expected_sources,
        locked_overlay_hash=locked_overlay_hash,
        locked_judge_schema_path=locked_schema_path,
        locked_judge_schema_hash=locked_schema_hash,
        preflight=PreflightResult(
            "BLOCKED", {}, ["no isolated context has passed preflight"], canonical_hash,
            prompt_hash, {}, {}, {},
        ),
        preflight_path=runtime_root / "preflight/preflight.json",
        source_probe_path=safe_sources[0] / "SKILL.md", auth_source=auth_source,
        dependency_staging=dependency_staging, dependency_evidence=dependency_evidence,
        git_topology=git_topology,
    )
    return materialized
