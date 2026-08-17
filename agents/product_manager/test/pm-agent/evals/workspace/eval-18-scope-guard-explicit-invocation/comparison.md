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
- target_skill_sha256: `e17c69ef6e179644f91ff00df55f141c375753f4668f30aca4e37e8247a60506`
- eval_definition_sha256: `fbd5b3a5e4c0be83eacf913e76dfe890f776915d3d24ba4fd45c191e31196a40`
- metadata_sha256: `d008e123b4ee70f7bf43fcaf109d74c9d72e4654db9631f703b1f4b299706113`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3a5175573f5c12faf8ef17031068ea4a3554be3c63ea98a9f0e35a5de2fe7ef6`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `495fc0f825d65d1e7057e4dc84ea777d069a48dcb665a6ab231607b5f4f53d34`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `8b076cb82c470b131f01d4ac1cd0d36cbfb1e690ece346a8313d30b76a409813`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `explicit_invocation_proceeds` | PASS | with_skill 输出明确以“pm-agent 判定”说明该请求不属于 PM/研发范围、不进入下游 PM 流程，并在权限受限时诚实停止；runner_captured_trace 还记录了读取 pm-agent 技能及尝试访问 Downloads。 |
| `classifies_general_request` | PASS | with_skill 输出先完成范围分类，明确本地文件整理不属于 PM/研发范围且不进入下游流程，随后才报告访问权限阻塞；没有跳过分类直接执行文件操作。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=495fc0f825d65d1e7057e4dc84ea777d069a48dcb665a6ab231607b5f4f53d34; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=6d4b042adabac3091f56c82356f5f3b5823d222f4e7782d6aa78c42cf3fa738f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别并使用 pm-agent 边界，诚实判定请求不属于 PM 范围；访问 Downloads 时因权限阻塞而停止。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=495fc0f825d65d1e7057e4dc84ea777d069a48dcb665a6ab231607b5f4f53d34; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=eb9d2a59c00cdc0ef9463f57ff2e96c934393a527513814aeeb29a5b363efe45; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 未使用 pm-agent，直接以能力不可用为由拒绝处理。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 授予会话访问 /Users/neplich/Downloads 的权限后继续整理文件。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
