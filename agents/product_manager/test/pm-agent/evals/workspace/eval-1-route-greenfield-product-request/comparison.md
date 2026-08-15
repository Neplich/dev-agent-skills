# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-001-route-greenfield-product-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-1-route-greenfield-product-request`.
- Identity schema: `2`
- target_skill_sha256: `ed93e443692bf05e76aaa38c8a5b8faff57190219ed48b9335316584424e6eb9`
- eval_definition_sha256: `4e776e14ac2c8d3f3aa33718b92238355ee2d15eab3267a50cdada6bb3d4a1de`
- metadata_sha256: `98a5616a9f22e4ba7d6ed10c98a36b572ccd9f5c0bfcfaf868ea982ef672635f`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `8e99b873e976898a8a9714405f69dce2d81e6c553f7d4c2b0a99b8b832eee831`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `320ded3db25222eda1be26706a57ed0471cc438157b54925db0b045d15abf8e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `route_to_idea_to_spec` | PASS | With-skill output identifies the greenfield discovery lane, unresolved feature path, and pending product definition; it does not enter implementation. |
| `pm_first_guardrail` | PASS | With-skill output identifies an empty project, major new-product scope, pending technical stack, and explicitly says not to write durable docs yet; no code or engineering execution occurred. |
| `context_to_collect` | PASS | It asks the first product-discovery question about the target user and core use case, with three concrete options, while leaving later scope and acceptance decisions for subsequent interaction. |
| `expected_pm_artifacts` | NOT_EXERCISED | The output states PRD.md and DECISIONS.md are pending and asks for user confirmation before discovery is complete, so this artifact requirement is not yet exercised. |
| `handoff_boundary` | NOT_EXERCISED | No handoff occurs in this turn; the candidate remains in discovery awaiting the user's answer. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=16a2e4f2784a34a6d03a7ba1cdbf301d5381761b0795edff3dbf9f3f3d2ae4c2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly keeps the empty-directory request in PM greenfield discovery, identifies the unresolved scope, avoids implementation, and asks a focused first product question.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=bb9f8d0f412bf947a7364508088c82d47622732f172b33fdeb00b4037a9353d0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a broad MVP proposal and several decisions, remains code-free, but does not explicitly establish the narrow PM routing state or focus the first interaction on one highest-information discovery question.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Await the user's target-user choice, then continue product discovery before producing PRD/DECISIONS or handing off.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
