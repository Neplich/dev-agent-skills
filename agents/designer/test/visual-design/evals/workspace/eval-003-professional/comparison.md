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
- Identity schema: `2`
- target_skill_sha256: `61b6f3a42424308b7a04ea0adf2a51b2b68f65f02fd796de4a724f6f357a579d`
- eval_definition_sha256: `730e4eb8de3e03b346a013a3d5577a175072336c34214d71e41ce4685c2c2ee1`
- metadata_sha256: `e736b74cad81064d52f58883a440db71240d4645566f7fc04859188bfb284e38`
- fixture_sha256: `567d74ee90d360991ab613f98d8049d53202d95a2bc7caeb2b7d46b23846a5f0`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `5ac69cf52c4833a0e74ebe39318957376e1be2b4d8142bcff9072bdd02569746`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `fe1184ee76579ac0041ea69b2abac6b0897add864da628d5ff0192673c2c0220`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `3beb7f3f01f53d491f571b17a7c7d87e2b0ca9e8ea7417fbcc27feda44e8e283`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 的 locked delivery_snapshot 文档明确写出普通文字对比度至少 4.5:1、大文本和关键 UI 边界至少 3:1，并包含键盘焦点、非颜色识别，以及概览—分析—证据的企业分析层级。 |
| `assertion_2` | PASS | with_skill 的 locked delivery_snapshot 是视觉规范 Markdown 文档，不含组件实现代码；git_evidence 仅显示新增该文档，HEAD 未变化且无样式文件改动。候选最终输出也未包含工程命令。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fe1184ee76579ac0041ea69b2abac6b0897add864da628d5ff0192673c2c0220; fixture_sha256=567d74ee90d360991ab613f98d8049d53202d95a2bc7caeb2b7d46b23846a5f0; output_sha256=f1062c1063441dc02b3d65457e29f02c4e21d6d28c31478ef69bf57577b755ea; snapshot_sha256=3650290eecfe92d5e38ef2dd6a0c44ea8608f1eabfe28e18d5b578ce8940bac4
- Behavior: 交付了面向企业分析平台的视觉规范文档，覆盖可访问性、清晰层级和设计交接边界，未落地代码或样式修改。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fe1184ee76579ac0041ea69b2abac6b0897add864da628d5ff0192673c2c0220; fixture_sha256=567d74ee90d360991ab613f98d8049d53202d95a2bc7caeb2b7d46b23846a5f0; output_sha256=2c627ac54db0371bf75d8b48c8b6981d7a00184904c4697065908c983b634e5a; snapshot_sha256=70f29d3d41e995258e7cf4a01989deae4f5866f6073fedbc5d3e4a42b5bcf3d4
- Behavior: 同样交付了视觉规范文档，覆盖对比度、角色阅读优先级和可访问性清单；作为 fresh baseline 与 with_skill 行为基本一致。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
