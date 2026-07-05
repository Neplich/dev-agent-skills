# Installing Dev Agent Skills for Codex

Install this repository into Codex via native skill discovery.

This installer keeps the repository layout unchanged for Claude marketplace compatibility. Codex discovers skills through symlinks created under the selected `.agents/skills` directory.

## Before You Install

Before making any filesystem changes, ask the user these two questions and wait for both answers:

1. Do you want a `personal` install or a `project` install?
2. Do you want to install `pm-agent` only, `all` agents, or a selected subset from this list?

Available public entry and downstream capabilities:

- `pm-agent` - direct user entry for product planning, request classification, docs, GitHub status, and downstream handoff
- `engineer-agent` - downstream engineering capability for PM handoff after scope is confirmed
- `qa-agent` - downstream QA capability for PM handoff after expectations are confirmed
- `devops-agent` - downstream DevOps capability for PM handoff after operational scope is confirmed
- `designer-agent` - downstream design capability for PM handoff after design scope is confirmed
- `security-agent` - downstream security capability for PM handoff after security scope is confirmed

Select `pm-agent` as the direct user entry. If the user chooses a subset, allow multiple selections for downstream PM-orchestrated capabilities.

## Installation Model

Clone or update this repository under the selected `.agents` root, then expose each selected skill as a symlink under the selected `.agents/skills` directory.

- Personal install:
  - clone repo to `$HOME/.agents/dev-agent-skills`
  - symlink skills to `$HOME/.agents/skills/<skill-name>`
- Project install:
  - clone repo to `<project>/.agents/dev-agent-skills`
  - symlink skills to `<project>/.agents/skills/<skill-name>`

Do not move, flatten, or rewrite the repository's `agents/*/skills/*` directories.

The symlink model keeps downstream skills available for PM-orchestrated handoff. Prefer `pm-agent` for direct user requests; downstream role routers and specialist skills are intended for work whose scope has already been confirmed by PM handoff or an equivalent document chain.

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

The Bash commands below work on macOS, Linux, WSL, and Git Bash. For native Windows PowerShell, use the Windows example after Step 3 instead of the Bash snippets.

### 1. Resolve target paths

For `personal`:

```bash
CLONE_ROOT="$HOME/.agents/dev-agent-skills"
SKILL_ROOT="$HOME/.agents/skills"
LEGACY_CLONE_ROOT="$HOME/.codex/dev-agent-skills"
LEGACY_SKILL_ROOT="$HOME/.agents/skills/dev-agent-skills"
```

For `project`, from the project root:

```bash
PROJECT_ROOT="$PWD"
CLONE_ROOT="$PROJECT_ROOT/.agents/dev-agent-skills"
SKILL_ROOT="$PROJECT_ROOT/.agents/skills"
LEGACY_CLONE_ROOT="$PROJECT_ROOT/.codex/dev-agent-skills"
LEGACY_SKILL_ROOT="$PROJECT_ROOT/.agents/skills/dev-agent-skills"
```

### 2. Clone or update the repository

If `CLONE_ROOT` already exists, update it:

```bash
git -C "$CLONE_ROOT" pull --ff-only
```

For a routine update where the installed symlinks already use the current `.agents/skills/<skill-name>` layout and the selected agent set is unchanged, stop here and restart Codex if needed. Do not clean up or recreate symlinks.

Otherwise clone it:

```bash
mkdir -p "$(dirname "$CLONE_ROOT")"
git clone https://github.com/Neplich/dev-agent-skills.git "$CLONE_ROOT"
```

### 3. Create or migrate Codex skill symlinks

Create the selected Codex skill root:

```bash
mkdir -p "$SKILL_ROOT"
```

Use this helper to link every skill from a selected agent:

```bash
cleanup_legacy_agent_skill_root() {
  [ -d "$LEGACY_SKILL_ROOT" ] || return 0

  find "$LEGACY_SKILL_ROOT" -maxdepth 1 -type l -print | while IFS= read -r link; do
    target="$(readlink "$link")"
    case "$target" in
      "$LEGACY_CLONE_ROOT"/agents/*)
        rm "$link"
        echo "Removed legacy symlink $link"
        ;;
    esac
  done

  rmdir "$LEGACY_SKILL_ROOT" 2>/dev/null || true
}

cleanup_managed_skill_links() {
  find "$SKILL_ROOT" -maxdepth 1 -type l -print | while IFS= read -r link; do
    target="$(readlink "$link")"
    case "$target" in
      "$CLONE_ROOT"/*)
        rm "$link"
        echo "Removed managed symlink $link"
        ;;
    esac
  done
}

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

For a first install, legacy aggregate-layout migration, or selected-agent change, remove this repository's old managed links before creating the selected links:

```bash
cleanup_legacy_agent_skill_root
cleanup_managed_skill_links
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

If the user chose `pm-agent` only, run only the product manager line. If the user chose a subset, run only the matching lines.

For example, for `pm-agent`, `engineer-agent`, and `qa-agent`:

```bash
link_agent_skills "agents/product_manager/skills"
link_agent_skills "agents/engineer/skills"
link_agent_skills "agents/qa/skills"
```

### Windows PowerShell example

Use this equivalent flow in native Windows PowerShell. Creating symbolic links may require Developer Mode or an elevated shell, depending on the Windows configuration.

For a personal install:

```powershell
$CloneRoot = Join-Path $HOME ".agents/dev-agent-skills"
$SkillRoot = Join-Path $HOME ".agents/skills"
$LegacyCloneRoot = Join-Path $HOME ".codex/dev-agent-skills"
$LegacySkillRoot = Join-Path $HOME ".agents/skills/dev-agent-skills"
```

For a project install, run from the project root:

```powershell
$ProjectRoot = (Get-Location).Path
$CloneRoot = Join-Path $ProjectRoot ".agents/dev-agent-skills"
$SkillRoot = Join-Path $ProjectRoot ".agents/skills"
$LegacyCloneRoot = Join-Path $ProjectRoot ".codex/dev-agent-skills"
$LegacySkillRoot = Join-Path $ProjectRoot ".agents/skills/dev-agent-skills"
```

Then clone or update the repository. If this is a routine update and the current symlinks already use `.agents/skills/<skill-name>`, stop after `git pull` and restart Codex if needed. For a first install, legacy migration, or selected-agent change, continue with cleanup and link creation:

```powershell
if (Test-Path -LiteralPath $CloneRoot) {
  git -C $CloneRoot pull --ff-only
} else {
  New-Item -ItemType Directory -Force -Path (Split-Path $CloneRoot) | Out-Null
  git clone https://github.com/Neplich/dev-agent-skills.git $CloneRoot
}

New-Item -ItemType Directory -Force -Path $SkillRoot | Out-Null

function Test-ManagedTarget {
  param(
    [string]$Target,
    [string]$Root
  )

  if (-not $Target) { return $false }

  $targetFull = [System.IO.Path]::GetFullPath($Target)
  $rootFull = [System.IO.Path]::GetFullPath($Root).TrimEnd([char[]]@('\', '/'))
  return $targetFull.StartsWith($rootFull + [System.IO.Path]::DirectorySeparatorChar, [System.StringComparison]::OrdinalIgnoreCase)
}

function Cleanup-LegacyAgentSkillRoot {
  if (-not (Test-Path -LiteralPath $LegacySkillRoot -PathType Container)) { return }

  Get-ChildItem -LiteralPath $LegacySkillRoot -Force |
    Where-Object { $_.LinkType -eq "SymbolicLink" } |
    ForEach-Object {
      if (Test-ManagedTarget -Target $_.Target -Root (Join-Path $LegacyCloneRoot "agents")) {
        Remove-Item -LiteralPath $_.FullName
        Write-Host "Removed legacy symlink $($_.FullName)"
      }
    }

  Remove-Item -LiteralPath $LegacySkillRoot -ErrorAction SilentlyContinue
}

function Cleanup-ManagedSkillLinks {
  Get-ChildItem -LiteralPath $SkillRoot -Force |
    Where-Object { $_.LinkType -eq "SymbolicLink" } |
    ForEach-Object {
      if (Test-ManagedTarget -Target $_.Target -Root $CloneRoot) {
        Remove-Item -LiteralPath $_.FullName
        Write-Host "Removed managed symlink $($_.FullName)"
      }
    }
}

function Link-AgentSkills {
  param([string]$AgentSkillsPath)

  $agentSkillsDir = Join-Path $CloneRoot $AgentSkillsPath
  foreach ($skillItem in Get-ChildItem -LiteralPath $agentSkillsDir -Directory) {
    $skillDir = $skillItem.FullName
    if (-not (Test-Path -LiteralPath (Join-Path $skillDir "SKILL.md"))) { continue }

    $skillName = $skillItem.Name
    $dest = Join-Path $SkillRoot $skillName

    if (Test-Path -LiteralPath $dest) {
      $destItem = Get-Item -LiteralPath $dest -Force
      if ($destItem.LinkType -eq "SymbolicLink") {
        if (Test-ManagedTarget -Target $destItem.Target -Root $CloneRoot) {
          Remove-Item -LiteralPath $dest
        } else {
          Write-Host "Skip existing symlink not managed by this installer: $dest -> $($destItem.Target)"
          continue
        }
      } else {
        Write-Host "Skip existing non-symlink skill directory: $dest"
        continue
      }
    }

    New-Item -ItemType SymbolicLink -Path $dest -Target $skillDir | Out-Null
    Write-Host "Linked $skillName"
  }
}

Cleanup-LegacyAgentSkillRoot
Cleanup-ManagedSkillLinks

# Keep all entries for `all`, or remove entries for agents the user did not select.
$SelectedAgentSkillDirs = @(
  "agents/product_manager/skills",
  "agents/engineer/skills",
  "agents/qa/skills",
  "agents/devops/skills",
  "agents/designer/skills",
  "agents/security/skills"
)

foreach ($agentSkillsPath in $SelectedAgentSkillDirs) {
  Link-AgentSkills $agentSkillsPath
}
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

After restarting Codex, verify that the direct entry command is available:

- `/pm-agent`

Selected downstream skills may also be discoverable as linked skill directories, but they are PM-orchestrated capabilities rather than direct user entries.

## Updating

Update the clone in place:

```bash
git -C "$CLONE_ROOT" pull --ff-only
```

The current `.agents/skills/<skill-name>` links continue to work after the pull, so routine updates do not need cleanup or link recreation. If the install was created with the legacy aggregate layout or the selected agent set changed, run Step 3 once so old managed links are removed before new links are created. Restart Codex if the updated skills do not appear immediately.

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
