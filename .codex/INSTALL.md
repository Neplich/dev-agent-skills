# Installing Dev Agent Skills for Codex

Install this repository into Codex with a hidden mirror and root-level relative
skill symlinks. Do not symlink skills directly from this repository clone into
the Codex skill directory.

## Before You Install

Ask the user two questions and wait for both answers:

1. Should this be a `personal` install or a `project` install?
2. Should Codex install all skills by default, or use the restricted `routers-only` mode?

Default all-skills install includes the role routers:

- `pm-agent` - direct user entry for product planning, request classification, docs, GitHub status, and downstream handoff
- `engineer-agent` - downstream engineering capability for PM handoff after scope is confirmed
- `qa-agent` - downstream QA capability for PM handoff after expectations are confirmed
- `devops-agent` - downstream DevOps capability for PM handoff after operational scope is confirmed
- `designer-agent` - downstream design capability for PM handoff after design scope is confirmed
- `security-agent` - downstream security capability for PM handoff after security scope is confirmed
- `docs-agent` - downstream formal documentation bootstrap, synchronization, and release-audit capability for PM handoff

The default all-skills install also includes every specialist skill so `pm-agent`
and role-router orchestration can call downstream specialist workflows. Select
`routers-only` only when the user explicitly wants the minimal entry
classification surface; specialist skills are not linked at the target root in
that mode, so PM and role-router orchestration cannot call downstream
specialists.

## Why Mirror Instead Of Clone Symlinks

Codex resolves skill symlinks to their real path before looking upward for
`.codex-plugin/plugin.json` or `.claude-plugin/plugin.json`. This repository must
keep `agents/{role}/.claude-plugin/plugin.json` files for Claude marketplace
compatibility. If a Codex skill points back into the clone by symlink, Codex can
find those manifests and add namespace prefixes such as `Pm Agent:` to the skill
names.

The installer below mirrors the repository `agents/` tree into
`$SKILL_ROOT/.dev-agent-skills/`, excluding plugin manifest directories and
agent test directories. It then creates relative symlinks such as
`$SKILL_ROOT/pm-agent -> .dev-agent-skills/agents/product_manager/skills/pm-agent`.
The resolved skill path stays inside the hidden mirror, whose ancestors do not
contain plugin manifests, and shared repo-relative skill references remain
available without path rewriting. Codex does not scan dot-prefixed directories
as skill roots, so the hidden mirror does not expose duplicate skills.

## Installation Steps

### 1. Resolve Paths

For a personal install:

```bash
CLONE_ROOT="$HOME/.agents/dev-agent-skills"
SKILL_ROOT="$HOME/.agents/skills"
```

A personal install is discoverable in every project Codex opens. In projects
without an enable marker, `pm-agent`'s scope guard stops general conversation,
local-machine operations, and generic file work with a one-line notice;
project-oriented requests and explicit invocation still proceed. Choose
`personal` only when that global trigger surface is intended; a project
install keeps the skills inside the project and gives it an explicit enable
marker (`.agents/skills/.dev-agent-skills-mirror.json`).

For a project install, run from the project root:

```bash
PROJECT_ROOT="$PWD"
CLONE_ROOT="$PROJECT_ROOT/.agents/dev-agent-skills"
SKILL_ROOT="$PROJECT_ROOT/.agents/skills"
```

### 2. Clone Or Update The Repository

Set `TARGET_TAG` to a release tag (for example `v0.3.6`) when this install
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
    # Fetch from the verified URL into the local tag ref so the checkout and
    # identity checks always read the official object, not a stale or forged
    # local tag or an unverified origin remote.
    git -C "$CLONE_ROOT" fetch "$REPO_URL" "refs/tags/${TARGET_TAG}:refs/tags/${TARGET_TAG}" \
      || { echo "error: fetch failed; aborting pinned install" >&2; exit 1; }
    git -C "$CLONE_ROOT" checkout --detach "refs/tags/${TARGET_TAG}^{commit}" \
      || { echo "error: cannot checkout $TARGET_TAG; aborting pinned install" >&2; exit 1; }
    test "$(git -C "$CLONE_ROOT" rev-parse HEAD)" = "$(git -C "$CLONE_ROOT" rev-parse "refs/tags/${TARGET_TAG}^{commit}")" \
      || { echo "error: checkout verification failed for $TARGET_TAG; aborting pinned install" >&2; exit 1; }
  else
    # A previous pinned install leaves a detached HEAD; return to main first
    # so the unpinned update applies to the branch and not a detached state.
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

### 3. Install Skills

Default all skills:

```bash
python3 "$CLONE_ROOT/scripts/install_codex_skills.py" --target "$SKILL_ROOT"
```

Restricted role routers only:

```bash
python3 "$CLONE_ROOT/scripts/install_codex_skills.py" --target "$SKILL_ROOT" --routers-only
```

`--routers-only` prints a warning because only the seven role router symlinks are
created at the target root, so `pm-agent` / role-router orchestration cannot
call downstream specialist workflows. The hidden mirror still contains the full
`agents/` tree so shared instruction references remain available. Use this mode
only for minimal entry classification.

The installer owns only two target shapes:

- symlinks whose resolved path is inside `$SKILL_ROOT/.dev-agent-skills/`
- symlinks whose resolved path is inside a dev-agent-skills checkout, detected
  by an ancestor `.claude-plugin/marketplace.json` with `name:
  dev-agent-skills`

Owned symlinks are replaced automatically. Older clone symlink installs are
migrated to hidden mirror symlinks. A legacy aggregate
`$SKILL_ROOT/dev-agent-skills` entry is removed before install when it is owned
by the same rule, or when a real directory contains a dev-agent-skills
marketplace file. Unowned aggregate entries are reported and left unchanged.

Real directories and symlinks to other locations are never deleted by this
installer. They are skipped by default. With `--force`, they are reported as
conflicts and the installer exits before rebuilding the mirror or changing any
target entries. Use `--force` to rebuild the hidden mirror and replace all owned
symlinks:

```bash
python3 "$CLONE_ROOT/scripts/install_codex_skills.py" --target "$SKILL_ROOT" --force
```

The installer prints the installed, updated, migrated, replaced, or skipped
skills and warns if the target ancestor chain contains
`.claude-plugin/plugin.json` or `.codex-plugin/plugin.json`.

## Disable One Skill By Path

To keep an installed skill on disk but hide it from Codex, add a path-specific entry
to `~/.codex/config.toml`:

```toml
[[skills.config]]
path = "/Users/you/.agents/skills/debugger"
enabled = false
```

Use the visible target-root symlink path on the user's machine.
