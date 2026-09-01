---
title: "Codex 统一全量安装 PRD"
type: PRD
version: "0.1.1"
status: Draft
author: "Neplich Claude"
date: "2026-08-17"
last_updated: "2026-09-01"
generated_by: "idea-to-spec"
feature: "codex-install"
feature_path: "repository-governance/codex-install"
parent_feature: "repository-governance"
feature_level: "2"
child_features: "N/A"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/288"
related_pr: "https://github.com/Neplich/dev-agent-skills/pull/293"
changelog:
  - version: "0.1.1"
    date: "2026-09-01"
    changes: "按 skill 最新约定补齐 frontmatter 字段（child_features）"
  - version: "0.1.0"
    date: "2026-08-17"
    changes: "初始版本，定义 Codex 统一全量安装需求"
---

# Codex 统一全量安装 PRD

## 1. 背景与动机

Codex 按发现目录中的独立 Skill 目录注册能力。原 `routers-only` 安装模式只在
目标根目录暴露 7 个 role router，router 路由到 specialist 时会按"目标能力未安装"
停止。该模式已移除（issue #288），Codex 安装统一为全量安装。

## 2. 目标

1. Codex 安装只有一种形态：隐藏镜像 + 目标根目录暴露 marketplace 登记的全部 Skill。
2. 用户只需选择 personal 或 project 安装范围，不再面对安装模式选择。

## 3. 当前事实

1. 安装器 `scripts/install_codex_skills.py` 默认暴露 marketplace 登记的全部 Skill，
   不提供 `--routers-only` 参数。
2. 旧的 routers-only 受管安装重新执行默认安装器后自动补齐全部 specialist。
3. 安装文档（`.codex/INSTALL.md`、`docs/README.codex.md`）只保留 personal / project
   安装范围选择，不再提供或推荐 routers-only。

## 4. 验收口径

引用 issue #288 的七条验收标准，概括如下：

1. 安装器不再暴露或接受 `--routers-only`。
2. 默认安装和 `--force` 安装均暴露 marketplace 当前登记的全部 Skill。
3. 从"仅 7 个 router 软链接"的受管安装重新执行默认安装后，全部 specialist 被补齐。
4. `idea-to-spec` 等 specialist 能进入 Codex 可用 Skill 清单，router 不再因安装策略
   报告目标能力缺失。
5. 安装文档不再提供或推荐 routers-only。
6. 删除旧模式测试，并保留"旧受管安装升级到全量安装"的回归覆盖。
7. 仓库规定的静态契约、安装器测试和 `git diff --check` 通过。

## 5. 非目标

- 不改变 7 个 Agent 的角色边界。
- 不改变 PM-first 路由规则。
- 不改变 specialist 的 gate。
- 不改变 Claude / Kimi 插件注册方式。
