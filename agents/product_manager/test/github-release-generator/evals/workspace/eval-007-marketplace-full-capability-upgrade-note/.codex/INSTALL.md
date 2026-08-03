# Dev Agent Skills Installer (Codex)

Install the dev-agent-skills marketplace into a Codex project.

## Project Layout

For a project install, run from the project root:

```bash
PROJECT_ROOT="$PWD"
CLONE_ROOT="$PROJECT_ROOT/.agents/dev-agent-skills"
SKILL_ROOT="$PROJECT_ROOT/.agents/skills"
```

## Clone Or Update The Repository

Set `TARGET_TAG` to a release tag (for example `v1.0.0`) when this install
must match a specific released version, as the Release upgrade instructions
do. Omit it for a plain latest install.

```bash
REPO_URL="https://github.com/Neplich/dev-agent-skills.git"
if [ -d "$CLONE_ROOT/.git" ]; then
  if [ -n "$(git -C "$CLONE_ROOT" status --porcelain)" ]; then
    echo "error: $CLONE_ROOT has uncommitted or untracked changes; commit or stash them before installing" >&2
    exit 1
  fi
  if [ -n "${TARGET_TAG:-}" ]; then
    git ls-remote --exit-code --tags "$REPO_URL" "refs/tags/${TARGET_TAG}" >/dev/null \
      || { echo "error: release tag $TARGET_TAG not found on origin; aborting pinned install" >&2; exit 1; }
    git -C "$CLONE_ROOT" fetch "$REPO_URL" "refs/tags/${TARGET_TAG}:refs/tags/${TARGET_TAG}" \
      || { echo "error: fetch failed; aborting pinned install" >&2; exit 1; }
    git -C "$CLONE_ROOT" checkout --detach "refs/tags/${TARGET_TAG}^{commit}" \
      || { echo "error: cannot checkout $TARGET_TAG; aborting pinned install" >&2; exit 1; }
    test "$(git -C "$CLONE_ROOT" rev-parse HEAD)" = "$(git -C "$CLONE_ROOT" rev-parse "refs/tags/${TARGET_TAG}^{commit}")" \
      || { echo "error: checkout verification failed for $TARGET_TAG; aborting pinned install" >&2; exit 1; }
  else
    git -C "$CLONE_ROOT" checkout main || { echo "error: cannot switch to main; aborting update" >&2; exit 1; }
    git -C "$CLONE_ROOT" pull --ff-only || { echo "error: update failed; aborting install" >&2; exit 1; }
  fi
else
  mkdir -p "$(dirname "$CLONE_ROOT")"
  if [ -n "${TARGET_TAG:-}" ]; then
    git ls-remote --exit-code --tags "$REPO_URL" "refs/tags/${TARGET_TAG}" >/dev/null \
      || { echo "error: release tag $TARGET_TAG not found on origin; aborting pinned install" >&2; exit 1; }
    git clone "$REPO_URL" "$CLONE_ROOT"
    git -C "$CLONE_ROOT" checkout --detach "refs/tags/${TARGET_TAG}^{commit}" \
      || { echo "error: cannot checkout $TARGET_TAG; aborting pinned install" >&2; exit 1; }
    test "$(git -C "$CLONE_ROOT" rev-parse HEAD)" = "$(git -C "$CLONE_ROOT" rev-parse "refs/tags/${TARGET_TAG}^{commit}")" \
      || { echo "error: checkout verification failed for $TARGET_TAG; aborting pinned install" >&2; exit 1; }
  else
    git clone "$REPO_URL" "$CLONE_ROOT"
  fi
fi
```

## Install Or Update Skills

Run the installer script, which reads the cloned repository and syncs the
skill symlinks:

```bash
python3 "$CLONE_ROOT/scripts/install_codex_skills.py" --root "$SKILL_ROOT"
```

Verify the install:

```bash
ls "$SKILL_ROOT" | sort
```

## Uninstall

Remove the project install directory:

```bash
rm -rf "$CLONE_ROOT" "$SKILL_ROOT"
```
