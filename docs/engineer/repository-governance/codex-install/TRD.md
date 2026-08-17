---
title: "Codex 统一全量安装 TRD"
type: TRD
version: "0.1.0"
status: Draft
author: "Neplich Claude"
date: "2026-08-17"
last_updated: "2026-08-17"
generated_by: "trd-gen"
feature: "codex-install"
feature_path: "repository-governance/codex-install"
parent_feature: "repository-governance"
feature_level: "2"
related_prd: "docs/pm/repository-governance/codex-install/PRD.md"
related_issue: "https://github.com/Neplich/dev-agent-skills/issues/288"
related_pr: "https://github.com/Neplich/dev-agent-skills/pull/293"
changelog:
  - version: "0.1.0"
    date: "2026-08-17"
    changes: "初始版本，定义 Codex 统一全量安装技术方案"
---

# Codex 统一全量安装 TRD

## 1. 概述

`scripts/install_codex_skills.py` 以全量安装为唯一形态：将仓库内容复制为隐藏镜像，
并在目标根目录为 marketplace 登记的全部 Skill 创建相对软链接。原 routers-only 模式
已移除（issue #288），安装器不提供也不接受 `--routers-only`。

## 2. 安装流程

1. 解析 `.claude-plugin/marketplace.json` 的 plugins / skills 条目，生成 `SkillSpec`
   列表；同名 Skill 冲突时按 plugin 名加限定前缀。
2. 执行 preflight 检查，确认目标根目录与镜像归属状态。
3. 重建隐藏镜像 `.dev-agent-skills/`：剔除 plugin manifest 与 test 目录，保留
   `SKILL.md` 引用的测试路径，并写入镜像 marker。
4. 在目标根目录为每个 Skill 创建指向镜像内 Skill 目录的相对软链接。

旧的仅-router 受管安装因目标软链接解析路径均落在镜像内，重新执行默认安装器时会被
识别为归属项并替换，从而自动补齐全部 specialist。

## 3. Ownership 规则

安装器只管理以下条目：

- 解析路径落在镜像 `.dev-agent-skills/` 内的软链接；
- 指向旧 `dev-agent-skills` checkout 的软链接；
- legacy aggregate `dev-agent-skills` 目录按 marker 判定归属。

真实目录与外部软链接默认跳过。`--force` 遇到非归属冲突即报错退出，不删除该条目。

## 4. `--force` 语义

`--force` 重建隐藏镜像并替换全部归属软链接；非归属条目不受影响（见上一节的报错
退出规则）。

## 5. 验证策略

```bash
uv run --with pytest pytest scripts/test_install_codex_skills.py
uv run scripts/check_repository_contract.py
uv run scripts/check_doc_contract.py
```

安装器测试包含"旧的仅-router 受管安装重新执行默认安装后补齐全部 specialist"的
回归覆盖；旧 routers-only 模式的测试已随模式移除一并删除。
