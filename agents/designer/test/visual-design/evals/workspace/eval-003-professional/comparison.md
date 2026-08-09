# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `visual-design`
- Eval: `eval-003-professional`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `567d74ee90d360991ab613f98d8049d53202d95a2bc7caeb2b7d46b23846a5f0` from `agents/designer/test/visual-design/evals/workspace/eval-003-professional`.
- Fixture SHA-256: `567d74ee90d360991ab613f98d8049d53202d95a2bc7caeb2b7d46b23846a5f0`
- Prompt SHA-256: `fe1184ee76579ac0041ea69b2abac6b0897add864da628d5ff0192673c2c0220`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9be23963f6e0e12e12a074b019666fb8a1f995677fec5a734a1b0b6be400f7fc`
- Skill overlay SHA-256: `b87e6c9b4a37c78d9c7cc608aee6187878beb1abc19fff1a5afb3d9645233d49`
- Judge schema SHA-256: `5ac69cf52c4833a0e74ebe39318957376e1be2b4d8142bcff9072bdd02569746`
- Eval definition SHA-256: `730e4eb8de3e03b346a013a3d5577a175072336c34214d71e41ce4685c2c2ee1`
- Metadata SHA-256: `0f7ee2304f9494f523bf0e9ffeed979b5af06eb7930b9cda8b5ec89883762703`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 的锁定交付文件明确规定普通文本对比度至少 4.5:1、大文本和 UI 边界至少 3:1，并通过标题、分组、栅格、表格和图表规则建立企业场景下的清晰层级。 |
| `assertion_2` | PASS | with_skill 的锁定交付内容是视觉规范文档，仅包含颜色、排版、布局、组件视觉规则和无障碍规范；git_evidence 显示无提交或工程变更，未包含组件代码、样式文件改动或工程命令。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fe1184ee76579ac0041ea69b2abac6b0897add864da628d5ff0192673c2c0220; fixture_sha256=567d74ee90d360991ab613f98d8049d53202d95a2bc7caeb2b7d46b23846a5f0; output_sha256=786486b32c69255b26072d8503f048eab839808da59764eaa8d039e1493dd975; snapshot_sha256=3034ebd79e4ebed75cdd185db5d7a645c92c98b8713e9d471940a3ca5508002d
- Behavior: 交付了完整的企业分析视觉规范，覆盖 WCAG 对比度、层级、数据密度、组件规则和无障碍要求，且未落代码。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fe1184ee76579ac0041ea69b2abac6b0897add864da628d5ff0192673c2c0220; fixture_sha256=567d74ee90d360991ab613f98d8049d53202d95a2bc7caeb2b7d46b23846a5f0; output_sha256=4b58b55e6faa254fd730ba27dd0e9235b8e0b309adf08e7a880407bc122c3341; snapshot_sha256=51f91f14f8cb99c627e15daef43ef653fdffb76e9df9f0bbd6d7db64edc72fad
- Behavior: 同样交付了视觉系统规范并满足两项要求，但内容和证据范围相对较基础。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
