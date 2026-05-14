# Installing Dev Agent Skills for Codex

Install this repository into Codex via native skill discovery.

This installer keeps the repository layout unchanged for Claude marketplace compatibility. Codex discovers skills through symlinks created under the selected `.agents/skills` directory.

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

Clone or update this repository under the selected `.agents` root, then expose each selected skill as a symlink under the selected `.agents/skills` directory.

- Personal install:
  - clone repo to `$HOME/.agents/dev-agent-skills`
  - symlink skills to `$HOME/.agents/skills/<skill-name>`
- Project install:
  - clone repo to `<project>/.agents/dev-agent-skills`
  - symlink skills to `<project>/.agents/skills/<skill-name>`

Do not move, flatten, or rewrite the repository's `agents/*/skills/*` directories.

Agent to source directory mapping:

- `pm-agent` -> `agents/product_manager/skills/*`
- `engineer-agent` -> `agents/engineer/skills/*`
- `qa-agent` -> `agents/qa/skills/*`
- `devops-agent` -> `agents/devops/skills/*`
- `designer-agent` -> `agents/designer/skills/*`
- `security-agent` -> `agents/security/skills/*`

Each linked skill should end up as one of these forms:

```text
$HOME/.agents/skills/<skill-name> -> $HOME/.agents/dev-agent-skills/agents/<agent>/skills/<skill-name>
<project>/.agents/skills/<skill-name> -> <project>/.agents/dev-agent-skills/agents/<agent>/skills/<skill-name>
```

## Installation Steps

### 1. Resolve target paths

For `personal`:

```bash
CLONE_ROOT="$HOME/.agents/dev-agent-skills"
SKILL_ROOT="$HOME/.agents/skills"
```

For `project`, from the project root:

```bash
PROJECT_ROOT="$PWD"
CLONE_ROOT="$PROJECT_ROOT/.agents/dev-agent-skills"
SKILL_ROOT="$PROJECT_ROOT/.agents/skills"
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

### 3. Create Codex skill symlinks

Create the selected Codex skill root:

```bash
mkdir -p "$SKILL_ROOT"
```

Use this helper to link every skill from a selected agent:

```bash
link_agent_skills() {
  agent_skills_dir="$CLONE_ROOT/$1"

  find "$agent_skills_dir" -mindepth 1 -maxdepth 1 -type d | while IFS= read -r skill_dir; do
    [ -f "$skill_dir/SKILL.md" ] || continue

    skill_name="$(basename "$skill_dir")"
    dest="$SKILL_ROOT/$skill_name"

    if [ -L "$dest" ]; then
      current_target="$(readlink "$dest")"
      case "$current_target" in
        "$CLONE_ROOT"/*)
          rm "$dest"
          ;;
        *)
          echo "Skip existing symlink not managed by this installer: $dest -> $current_target"
          continue
          ;;
      esac
    elif [ -e "$dest" ]; then
      echo "Skip existing non-symlink skill directory: $dest"
      continue
    fi

    ln -s "$skill_dir" "$dest"
    echo "Linked $skill_name"
  done
}
```

If the user chose `all`, run:

```bash
link_agent_skills "agents/product_manager/skills"
link_agent_skills "agents/engineer/skills"
link_agent_skills "agents/qa/skills"
link_agent_skills "agents/devops/skills"
link_agent_skills "agents/designer/skills"
link_agent_skills "agents/security/skills"
```

If the user chose a subset, run only the matching lines.

For example, for `pm-agent`, `engineer-agent`, and `qa-agent`:

```bash
link_agent_skills "agents/product_manager/skills"
link_agent_skills "agents/engineer/skills"
link_agent_skills "agents/qa/skills"
```

### 4. Restart Codex

Quit and relaunch Codex so it discovers the new skills. For a `project` install, reopen Codex in that same project directory.

## Verify

Check that Codex can see symlinked skill directories:

```bash
find -L "$SKILL_ROOT" -maxdepth 2 -name SKILL.md -print | sort
```

For this repository, expected entries include paths such as:

```text
$SKILL_ROOT/pm-agent/SKILL.md
$SKILL_ROOT/engineer-agent/SKILL.md
$SKILL_ROOT/qa-agent/SKILL.md
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

Remove only symlinks that point into the selected clone:

```bash
find "$SKILL_ROOT" -maxdepth 1 -type l -print | while IFS= read -r link; do
  target="$(readlink "$link")"
  case "$target" in
    "$CLONE_ROOT"/*)
      rm "$link"
      echo "Removed $link"
      ;;
  esac
done
```

Optionally remove the cloned repository:

```bash
rm -rf "$CLONE_ROOT"
```

## Troubleshooting

- If commands do not appear, verify the links under `"$SKILL_ROOT"` and restart Codex.
- If a skill name already exists under `"$SKILL_ROOT"` and is not a symlink to this repository, keep it and report the conflict instead of overwriting it.
- If the user changes from `all` to a subset, remove this repository's old symlinks first, then recreate only the selected agent skills.
- If the user chooses `project`, confirm Codex is opened in that same project directory after installation.
