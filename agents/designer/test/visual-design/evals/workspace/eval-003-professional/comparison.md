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
- target_skill_sha256: `be4ad3e2bd7a045eae2db8cc147a655dcc8a42c01f2783e36539d2888fdcbaaf`
- eval_definition_sha256: `730e4eb8de3e03b346a013a3d5577a175072336c34214d71e41ce4685c2c2ee1`
- metadata_sha256: `e736b74cad81064d52f58883a440db71240d4645566f7fc04859188bfb284e38`
- fixture_sha256: `567d74ee90d360991ab613f98d8049d53202d95a2bc7caeb2b7d46b23846a5f0`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `5ac69cf52c4833a0e74ebe39318957376e1be2b4d8142bcff9072bdd02569746`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `fe1184ee76579ac0041ea69b2abac6b0897add864da628d5ff0192673c2c0220`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `2dd23a101b1833a5f815a50f0bc085a1d9a95ddf55380df9fcbc12238f06ae99`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 的 delivery_snapshot 直接包含 WCAG AA 对比度阈值（普通文本 4.5:1、大文本和关键 UI 边界 3:1），并定义企业分析场景的用户层级、布局、密度和扫描规则。 |
| `assertion_2` | PASS | with_skill 的锁定交付文件仅为 visual-system.md；内容是规范性文字，无组件实现代码、样式文件改动或工程命令。git evidence 也显示仅有该文档未跟踪变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fe1184ee76579ac0041ea69b2abac6b0897add864da628d5ff0192673c2c0220; fixture_sha256=567d74ee90d360991ab613f98d8049d53202d95a2bc7caeb2b7d46b23846a5f0; output_sha256=de883cd766441c196bd6b34e1af079c56d1a80f2f2290a6ab7963028268c2f06; snapshot_sha256=073e959dec0f038c4b3addcb9855ee07ae4a7e33caaadc7fda442e937d323e79
- Behavior: 交付了面向企业分析平台的完整视觉规范，明确 WCAG 可访问性与高密度企业界面层级，并保持设计规范边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fe1184ee76579ac0041ea69b2abac6b0897add864da628d5ff0192673c2c0220; fixture_sha256=567d74ee90d360991ab613f98d8049d53202d95a2bc7caeb2b7d46b23846a5f0; output_sha256=f3cf0752a24e6ad90ccce1c2ce5c3d5b0e94b40cda9751e8f7f1b6feebd36829; snapshot_sha256=d6a7d26e6d4f73536d20784bedf3dde12687d696e19d13afaba620ec1918aa95
- Behavior: 同样交付了覆盖可访问性、层级和数据界面的视觉规范，作为新鲜基线表现也满足两项断言。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
