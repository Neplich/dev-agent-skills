# Dev Agent Skills for Codex

通过 Codex 的原生 skill 发现机制安装本仓库的 Agent skills。

## 快速安装

在 Codex 中输入：

```text
Fetch and follow instructions from https://raw.githubusercontent.com/Neplich/dev-agent-skills/refs/heads/main/.codex/INSTALL.md
```

Codex 会先反问你两个问题，再执行安装：

1. 安装范围是 `personal` 还是 `project`
2. 安装 `pm-agent` only、`all` agents，还是从多个 agents 中选择安装

## 公开入口与下游能力

- `pm-agent`：直接用户入口，负责需求分类、范围确认、文档产出、GitHub 状态读取和下游 handoff
- `engineer-agent`：PM handoff 后的下游工程能力，承接已确认范围内的代码分析、TRD、实现、测试、调试和交付
- `qa-agent`：PM handoff 后的下游 QA 能力，承接已确认预期下的探索测试、规范测试、Bug 分析和回归验证
- `devops-agent`：PM handoff 后的下游 DevOps 能力，承接已确认运维范围内的部署规划、CI/CD、环境审计和故障处理
- `designer-agent`：PM handoff 后的下游设计能力，承接已确认设计范围内的 UI/UX、视觉系统和界面规范
- `security-agent`：PM handoff 后的下游安全能力，承接已确认安全范围内的应用安全、权限审查、依赖风险和隐私映射

直接入口选择 `pm-agent`。如果选择 `selected`，支持一次选择多个下游 Agent 作为 PM 编排能力。

## 安装层级

### Personal

适合希望在所有项目里复用这些 Agent 的场景。

- 仓库 clone 到 `~/.agents/dev-agent-skills`
- 每个已选 Agent 下的 skills 软链接到 `~/.agents/skills/<skill-name>`

### Project

适合只想在当前项目里启用这些 Agent 的场景。

- 仓库 clone 到 `<project>/.agents/dev-agent-skills`
- 每个已选 Agent 下的 skills 软链接到 `<project>/.agents/skills/<skill-name>`

两种安装方式都保持仓库内的 `agents/*/skills/*` 目录不变，用于兼容 Claude marketplace。

Codex 会发现已链接的所有 skills；本仓库约定直接用户请求优先从 `pm-agent` 进入，下游 role router 和 specialist skill 用于 PM handoff 或等效已确认文档链已经明确范围后的工作。

## 手动安装

Bash 命令适用于 macOS、Linux、WSL 和 Git Bash。Windows 原生 PowerShell 请使用第 3 步后的 Windows 示例。

### 前置条件

- 已安装 Codex
- 已安装 Git

### 1. 选择安装层级

`personal` 和 `project` 二选一。

Personal:

```bash
CLONE_ROOT="$HOME/.agents/dev-agent-skills"
SKILL_ROOT="$HOME/.agents/skills"
LEGACY_CLONE_ROOT="$HOME/.codex/dev-agent-skills"
LEGACY_SKILL_ROOT="$HOME/.agents/skills/dev-agent-skills"
```

Project:

```bash
PROJECT_ROOT="$PWD"
CLONE_ROOT="$PROJECT_ROOT/.agents/dev-agent-skills"
SKILL_ROOT="$PROJECT_ROOT/.agents/skills"
LEGACY_CLONE_ROOT="$PROJECT_ROOT/.codex/dev-agent-skills"
LEGACY_SKILL_ROOT="$PROJECT_ROOT/.agents/skills/dev-agent-skills"
```

### 2. clone 或更新仓库

如果目标目录已存在：

```bash
git -C "$CLONE_ROOT" pull --ff-only
```

如果只是日常升级，且当前软链接已经是新的 `.agents/skills/<skill-name>` 布局，已选 Agent 也没有变化，到这里就可以停止；不需要清理或重建软链接，必要时重启 Codex 即可。

否则：

```bash
mkdir -p "$(dirname "$CLONE_ROOT")"
git clone https://github.com/Neplich/dev-agent-skills.git "$CLONE_ROOT"
```

### 3. 创建或迁移 Codex skill 软链接

```bash
mkdir -p "$SKILL_ROOT"
```

使用下面的函数链接某个 Agent 下的所有 skills：

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

首次安装、从旧聚合目录迁移，或本次改变已选 Agent 时，创建本次选择的链接前先删除本仓库旧的 managed links：

```bash
cleanup_legacy_agent_skill_root
cleanup_managed_skill_links
```

Agent 到目录的映射如下：

- `pm-agent` -> `agents/product_manager/skills`
- `engineer-agent` -> `agents/engineer/skills`
- `qa-agent` -> `agents/qa/skills`
- `devops-agent` -> `agents/devops/skills`
- `designer-agent` -> `agents/designer/skills`
- `security-agent` -> `agents/security/skills`

安装全部 Agent：

```bash
link_agent_skills "agents/product_manager/skills"
link_agent_skills "agents/engineer/skills"
link_agent_skills "agents/qa/skills"
link_agent_skills "agents/devops/skills"
link_agent_skills "agents/designer/skills"
link_agent_skills "agents/security/skills"
```

如果只安装直接入口，运行：

```bash
link_agent_skills "agents/product_manager/skills"
```

例如安装 `pm-agent` 以及 PM handoff 可用的 `engineer-agent`、`qa-agent`：

```bash
link_agent_skills "agents/product_manager/skills"
link_agent_skills "agents/engineer/skills"
link_agent_skills "agents/qa/skills"
```

### Windows PowerShell 示例

Windows 原生 PowerShell 不能直接使用上面的 Bash 命令。创建符号链接可能需要开启开发者模式，或使用管理员权限启动 PowerShell。

Personal:

```powershell
$CloneRoot = Join-Path $HOME ".agents/dev-agent-skills"
$SkillRoot = Join-Path $HOME ".agents/skills"
$LegacyCloneRoot = Join-Path $HOME ".codex/dev-agent-skills"
$LegacySkillRoot = Join-Path $HOME ".agents/skills/dev-agent-skills"
```

Project，需要在项目根目录执行：

```powershell
$ProjectRoot = (Get-Location).Path
$CloneRoot = Join-Path $ProjectRoot ".agents/dev-agent-skills"
$SkillRoot = Join-Path $ProjectRoot ".agents/skills"
$LegacyCloneRoot = Join-Path $ProjectRoot ".codex/dev-agent-skills"
$LegacySkillRoot = Join-Path $ProjectRoot ".agents/skills/dev-agent-skills"
```

然后 clone 或更新仓库。如果只是日常升级，且当前软链接已经是 `.agents/skills/<skill-name>` 布局，到 `git pull` 后就可以停止，必要时重启 Codex。首次安装、旧路径迁移或改变已选 Agent 时，再继续执行清理和链接创建：

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

# 安装 all 时保留全部条目；安装子集时删除未选择的 Agent 条目。
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

### 4. 重启 Codex

退出并重新打开 Codex，让它重新发现 skills。Project 安装需要在同一个项目目录里重新打开 Codex。

## 这套安装方式是怎么工作的

Codex 会在启动时扫描 `.agents/skills`。这里采用的是“保持仓库结构 + 为每个 skill 创建软链接”的方式。

Personal 安装示意：

```text
~/.agents/dev-agent-skills/
└── agents/
    └── engineer/
        └── skills/
            ├── engineer-agent/
            ├── codebase-analyzer/
            └── feature-implementor/

~/.agents/skills/
├── engineer-agent -> ~/.agents/dev-agent-skills/agents/engineer/skills/engineer-agent
├── codebase-analyzer -> ~/.agents/dev-agent-skills/agents/engineer/skills/codebase-analyzer
└── feature-implementor -> ~/.agents/dev-agent-skills/agents/engineer/skills/feature-implementor
```

Project 安装时，路径换成当前项目下的 `.agents/`。

Claude marketplace 继续读取仓库内的 Agent 目录；Codex 通过 `.agents/skills/<skill-name>/SKILL.md` 识别 skills。

## 使用示例

安装完成后，可以在 Codex 中这样用：

```text
/pm-agent "我想做一个任务管理应用"
/pm-agent "登录流程有 bug，先确认预期再安排修复"
/pm-agent "按 spec 验证登录功能"
/pm-agent "配置 CI/CD 并做发布前检查"
/pm-agent "上线前做一次权限和依赖风险审查"
```

下游 role router 和 specialist skills 仍会被链接，供 PM 编排后的 handoff 使用；直接用户请求优先从 `pm-agent` 分类，下游 skills 用于 PM handoff 或等效已确认文档链已经明确范围后的工作。

## 验证

```bash
find -L "$SKILL_ROOT" -maxdepth 2 -name SKILL.md -print | sort
```

预期能看到类似路径：

```text
$SKILL_ROOT/pm-agent/SKILL.md
$SKILL_ROOT/engineer-agent/SKILL.md
$SKILL_ROOT/qa-agent/SKILL.md
```

## 更新

```bash
git -C "$CLONE_ROOT" pull --ff-only
```

新的 `.agents/skills/<skill-name>` 软链接会在 pull 后继续生效，所以日常升级不需要清理或重建软链接。如果是从旧的聚合目录安装方式升级，或本次改变了已选 Agent，才重新执行第 3 步，让旧的 managed links 先被删除，再创建新的软链接。更新后如果没有立即生效，重启 Codex。

## 卸载

删除指向本仓库的 Codex skill 软链接：

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

如果需要同时删除仓库 clone：

```bash
rm -rf "$CLONE_ROOT"
```

如果只想减少已安装 Agent，不需要删 clone，只需要删除本仓库旧软链接，再重新链接需要的 Agent skills。

## 排障

- 看不到命令时，先检查 `"$SKILL_ROOT"/<skill-name>/SKILL.md` 是否存在，再重启 Codex。
- 如果 `"$SKILL_ROOT"/<skill-name>` 已存在且不是指向本仓库的软链接，不要覆盖，先报告冲突。
- 如果从全部 Agent 改成部分 Agent，先删除本仓库旧软链接，再创建本次选择的软链接。
- 使用 `project` 安装时，需要在同一个项目目录里打开 Codex。
