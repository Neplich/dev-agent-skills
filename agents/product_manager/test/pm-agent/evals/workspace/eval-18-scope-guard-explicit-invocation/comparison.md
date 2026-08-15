# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-018-scope-guard-explicit-invocation`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-18-scope-guard-explicit-invocation`.
- Identity schema: `2`
- target_skill_sha256: `ed93e443692bf05e76aaa38c8a5b8faff57190219ed48b9335316584424e6eb9`
- eval_definition_sha256: `fbd5b3a5e4c0be83eacf913e76dfe890f776915d3d24ba4fd45c191e31196a40`
- metadata_sha256: `d008e123b4ee70f7bf43fcaf109d74c9d72e4654db9631f703b1f4b299706113`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3a5175573f5c12faf8ef17031068ea4a3554be3c63ea98a9f0e35a5de2fe7ef6`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `495fc0f825d65d1e7057e4dc84ea777d069a48dcb665a6ab231607b5f4f53d34`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `23c155dfbbdaf3bf6fdaf16d337c16031340e19bffd6d7bb539e43bdc034b2af`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `explicit_invocation_proceeds` | PASS | with_skill 的锁定 trace 直接显示读取并遵循 pm-agent/SKILL.md；随后因 Downloads 访问权限受限而停止，没有执行文件移动，也未伪造下游角色。 |
| `classifies_general_request` | NOT_EXERCISED | 锁定 trace 证明进入了 pm-agent 能力并避免直接执行文件操作，但无法独立证明已明确记录 request_type 和 selected_owner；候选消息中的自述不作为独立证据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=495fc0f825d65d1e7057e4dc84ea777d069a48dcb665a6ab231607b5f4f53d34; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b07b7e0bdf06299aa383bbfabd4ce9ce2058fc4e6ee55d38c4c9ab4aa276c761; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 使用 pm-agent 入口并遵守其边界；确认 Downloads 无法读取后诚实停止，未移动文件或执行越权操作。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=495fc0f825d65d1e7057e4dc84ea777d069a48dcb665a6ab231607b5f4f53d34; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=114c6d8029789616dbf885d23f98561cebc93ad7a2fb12c02eafdb7f8a419676; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 未使用 pm-agent，仅报告环境限制；作为 fresh baseline 未进入 PM 分类流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
