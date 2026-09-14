# Codex 安装指南

本仓库通过隐藏镜像与根目录相对软链安装全部四十个 Skill。每项能力均可直接使用，按用户目标选择所需方法。

## 安装

向 Codex 提供：

```text
Fetch and follow instructions from https://raw.githubusercontent.com/Neplich/dev-agent-skills/refs/heads/main/.codex/INSTALL.md
```

指定 `personal` 可供多个项目发现，指定 `project` 则安装在当前项目。已明确的安装范围直接沿用。

| 范围 | 仓库位置 | Skill 位置 |
| --- | --- | --- |
| personal | `~/.agents/dev-agent-skills` | `~/.agents/skills` |
| project | `<project>/.agents/dev-agent-skills` | `<project>/.agents/skills` |

完整 clone、更新、固定 release tag 和安装命令见 [.codex/INSTALL.md](../.codex/INSTALL.md)。默认安装当前 `main`；设置 `TARGET_TAG` 可固定发布版本，并核对 tag 对应提交。

## 镜像与更新

安装器将 `agents/` 复制到 `<target>/.dev-agent-skills/agents/`，并在目标根目录为各 Skill 创建相对软链。镜像包含专业参考，排除插件 manifest 和测试目录，使 Skill 在 Codex 中以自身名称被发现。

`.dev-agent-skills-mirror.json` 标记镜像归属。安装器管理自己拥有的镜像和软链，迁移可识别的旧版安装；遇到其他目录或软链时保留其内容并报告冲突。`--force` 重建归属镜像和软链，存在非归属同名目标时先报告冲突。

```bash
python3 "$CLONE_ROOT/scripts/install_codex_skills.py" --target "$SKILL_ROOT"
```

`CLONE_ROOT` 和 `SKILL_ROOT` 使用安装步骤中选定的路径。更新后检查安装器输出的 installed、updated、migrated、replaced 或 skipped 项。

## 按路径禁用

在 `~/.codex/config.toml` 中指定可见 Skill 软链的绝对路径：

```toml
[[skills.config]]
path = "/Users/you/.agents/skills/debugger"
enabled = false
```
