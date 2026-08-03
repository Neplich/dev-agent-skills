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

Clone or update the repository from the default branch:

```bash
REPO_URL="https://github.com/Neplich/dev-agent-skills.git"
if [ -d "$CLONE_ROOT/.git" ]; then
  git -C "$CLONE_ROOT" checkout main
  git -C "$CLONE_ROOT" pull --ff-only
else
  mkdir -p "$(dirname "$CLONE_ROOT")"
  git clone "$REPO_URL" "$CLONE_ROOT"
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
