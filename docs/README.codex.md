# Dev Agent Skills for Codex

通过 Codex 的原生 skill 发现机制安装本仓库的 Agent skills。

## 快速安装

在 Codex 中输入：

```text
Fetch and follow instructions from https://raw.githubusercontent.com/Neplich/dev-agent-skills/refs/heads/main/.codex/INSTALL.md
```

Codex 会先反问你两个问题，再执行安装：

1. 安装范围是 `personal` 还是 `project`
2. 安装 `all` agents，还是从多个 agents 中选择安装

## 可安装的 Agent

- `pm-agent`：产品规划、需求文档、路线图、发版说明
- `engineer-agent`：代码分析、项目搭建、功能实现、测试、调试、交付
- `qa-agent`：探索测试、规范测试、Bug 分析、回归验证
- `devops-agent`：部署规划、CI/CD、环境审计、故障处理
- `designer-agent`：UI/UX 设计、reference-backed 视觉系统、界面规范，仅产出设计文档不写代码
- `security-agent`：应用安全、权限审查、依赖风险、隐私映射

如果选择 `selected`，支持一次选择多个 Agent。

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

## 手动安装

### 前置条件

- 已安装 Codex
- 已安装 Git

### 1. 选择安装层级

`personal` 和 `project` 二选一。

Personal:

```bash
CLONE_ROOT="$HOME/.agents/dev-agent-skills"
SKILL_ROOT="$HOME/.agents/skills"
```

Project:

```bash
PROJECT_ROOT="$PWD"
CLONE_ROOT="$PROJECT_ROOT/.agents/dev-agent-skills"
SKILL_ROOT="$PROJECT_ROOT/.agents/skills"
```

### 2. clone 或更新仓库

如果目标目录已存在：

```bash
git -C "$CLONE_ROOT" pull --ff-only
```

否则：

```bash
mkdir -p "$(dirname "$CLONE_ROOT")"
git clone https://github.com/Neplich/dev-agent-skills.git "$CLONE_ROOT"
```

### 3. 创建 Codex skill 软链接

```bash
mkdir -p "$SKILL_ROOT"
```

使用下面的函数链接某个 Agent 下的所有 skills：

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

例如只安装 `pm-agent`、`engineer-agent`、`qa-agent`：

```bash
link_agent_skills "agents/product_manager/skills"
link_agent_skills "agents/engineer/skills"
link_agent_skills "agents/qa/skills"
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
/engineer-agent "实现用户登录功能"
/qa-agent "测试登录功能"
/devops-agent "配置 CI/CD"
/designer-agent "设计用户登录界面"
/security-agent "进行安全审查"
```

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

更新后如果没有立即生效，重启 Codex。

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
