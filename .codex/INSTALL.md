# Installing Dev Agent Skills for Codex

Install this repository into Codex with copied skill directories. Do not symlink
skills from this repository clone into the Codex skill directory.

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

The default all-skills install also includes every specialist skill so `pm-agent`
and role-router orchestration can call downstream specialist workflows. Select
`routers-only` only when the user explicitly wants the minimal entry
classification surface; specialist skills are not installed in that mode, so PM
and role-router orchestration cannot call downstream specialists.

## Why Copy Instead Of Symlink

Codex resolves skill symlinks to their real path before looking upward for
`.codex-plugin/plugin.json` or `.claude-plugin/plugin.json`. This repository must
keep `agents/{role}/.claude-plugin/plugin.json` files for Claude marketplace
compatibility. If a Codex skill points back into the clone by symlink, Codex can
find those manifests and add namespace prefixes such as `Pm Agent:` to the skill
names.

The installer below copies each selected skill directory into the Codex skill
root so the target ancestor chain avoids those plugin manifests.

## Installation Steps

### 1. Resolve Paths

For a personal install:

```bash
CLONE_ROOT="$HOME/.agents/dev-agent-skills"
SKILL_ROOT="$HOME/.agents/skills"
```

For a project install, run from the project root:

```bash
PROJECT_ROOT="$PWD"
CLONE_ROOT="$PROJECT_ROOT/.agents/dev-agent-skills"
SKILL_ROOT="$PROJECT_ROOT/.agents/skills"
```

### 2. Clone Or Update The Repository

```bash
if [ -d "$CLONE_ROOT/.git" ]; then
  git -C "$CLONE_ROOT" pull --ff-only
else
  mkdir -p "$(dirname "$CLONE_ROOT")"
  git clone https://github.com/Neplich/dev-agent-skills.git "$CLONE_ROOT"
fi
```

### 3. Copy Skills

Default all skills:

```bash
uv run --directory "$CLONE_ROOT" scripts/install_codex_skills.py --target "$SKILL_ROOT"
```

Restricted role routers only:

```bash
uv run --directory "$CLONE_ROOT" scripts/install_codex_skills.py --target "$SKILL_ROOT" --routers-only
```

`--routers-only` prints a warning because specialist skills are not installed,
and `pm-agent` / role-router orchestration cannot call downstream specialist
workflows. Use it only for minimal entry classification.
If the target already contains managed specialist skills, `--routers-only`
stops with cleanup instructions unless `--force` is used to remove unselected
managed skills.

If a selected skill directory already exists, the installer skips it by default.
Use `--force` to delete and recopy existing selected skill directories:

```bash
uv run --directory "$CLONE_ROOT" scripts/install_codex_skills.py --target "$SKILL_ROOT" --force
```

The installer prints the copied or skipped skills and warns if the target
ancestor chain contains `.claude-plugin/plugin.json` or
`.codex-plugin/plugin.json`.

## Disable One Skill By Path

To keep a copied skill on disk but hide it from Codex, add a path-specific entry
to `~/.codex/config.toml`:

```toml
[[skills.config]]
path = "/Users/you/.agents/skills/debugger"
enabled = false
```

Use the actual copied skill path on the user's machine.
