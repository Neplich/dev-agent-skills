# Installing Dev Agent Skills for Codex

Install this repository into Codex via native skill discovery.

## Before You Install

Before making any filesystem changes, ask the user these two questions and wait for both answers:

1. Do you want a `personal` install or a `project` install?
2. Do you want to install `all` agents, or a selected subset from this list?

Available agents:

- `pm-agent` - product planning and docs
- `engineer-agent` - implementation, testing, debugging, delivery
- `qa-agent` - exploratory and spec-based testing
- `devops-agent` - deployment, CI/CD, environment audits
- `designer-agent` - UI/UX and visual design
- `security-agent` - appsec, authz, dependency, privacy review

If the user chooses a subset, allow multiple selections.

## Installation Model

Use a single aggregate skill directory and expose only the requested agent folders inside it.

- Personal install:
  - clone repo to `~/.codex/dev-agent-skills`
  - expose skills from `~/.agents/skills/dev-agent-skills/`
- Project install:
  - clone repo to `<project>/.codex/dev-agent-skills`
  - expose skills from `<project>/.agents/skills/dev-agent-skills/`

Each selected agent should be linked into the aggregate directory using this mapping:

- `pm-agent` -> `agents/product_manager`
- `engineer-agent` -> `agents/engineer`
- `qa-agent` -> `agents/qa`
- `devops-agent` -> `agents/devops`
- `designer-agent` -> `agents/designer`
- `security-agent` -> `agents/security`

## Installation Steps

### 1. Resolve target paths

For `personal`:

```bash
CLONE_ROOT="$HOME/.codex/dev-agent-skills"
SKILL_ROOT="$HOME/.agents/skills/dev-agent-skills"
```

For `project`, from the project root:

```bash
PROJECT_ROOT="$PWD"
CLONE_ROOT="$PROJECT_ROOT/.codex/dev-agent-skills"
SKILL_ROOT="$PROJECT_ROOT/.agents/skills/dev-agent-skills"
```

### 2. Clone or update the repository

If `CLONE_ROOT` already exists, update it:

```bash
git -C "$CLONE_ROOT" pull --ff-only
```

Otherwise clone it:

```bash
mkdir -p "$(dirname "$CLONE_ROOT")"
git clone https://github.com/Neplich/dev-agent-skills.git "$CLONE_ROOT"
```

### 3. Rebuild the aggregate skill directory

Make the installed set exactly match the user's choice:

```bash
rm -rf "$SKILL_ROOT"
mkdir -p "$SKILL_ROOT"
```

Then create symlinks for each selected agent. Example for `pm-agent` and `engineer-agent`:

```bash
ln -s "$CLONE_ROOT/agents/product_manager" "$SKILL_ROOT/product_manager"
ln -s "$CLONE_ROOT/agents/engineer" "$SKILL_ROOT/engineer"
```

If the user chose `all`, create all six links.

### 4. Restart Codex

Quit and relaunch Codex so it discovers the new skills.

## Verify

Check the aggregate directory:

```bash
ls -la "$SKILL_ROOT"
```

After restarting Codex, verify that the installed agent commands are available, such as:

- `/pm-agent`
- `/engineer-agent`
- `/qa-agent`
- `/devops-agent`
- `/designer-agent`
- `/security-agent`

Only the commands for the selected agents need to be present.

## Updating

Update the clone in place:

```bash
git -C "$CLONE_ROOT" pull --ff-only
```

The links continue to work after the pull. Restart Codex if the updated skills do not appear immediately.

## Uninstalling

Remove the aggregate skill directory:

```bash
rm -rf "$SKILL_ROOT"
```

Optionally remove the cloned repository:

```bash
rm -rf "$CLONE_ROOT"
```

## Troubleshooting

- If commands do not appear, verify the links under `"$SKILL_ROOT"` and restart Codex.
- If the user changes from `all` to a subset, rebuild `"$SKILL_ROOT"` so only the selected agent links remain.
- If the project install is used, confirm the user opened that same project in Codex after installation.
