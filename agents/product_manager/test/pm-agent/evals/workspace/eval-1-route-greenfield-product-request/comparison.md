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
- target_skill_sha256: `a37bf10fca64a8e15e6213ecdd45b65783814d307c78fd8d8ce6ab45b20effef`
- eval_definition_sha256: `4e776e14ac2c8d3f3aa33718b92238355ee2d15eab3267a50cdada6bb3d4a1de`
- metadata_sha256: `98a5616a9f22e4ba7d6ed10c98a36b572ccd9f5c0bfcfaf868ea982ef672635f`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `8e99b873e976898a8a9714405f69dce2d81e6c553f7d4c2b0a99b8b832eee831`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81`
- Repository HEAD: `3f5e81c4837ef85284a7d5381575e40267796c92`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6f4abf80e411dc3e6124c51093f07046c341195b1b2f0e9981a535c9960cb623`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `route_to_idea_to_spec` | PASS | With-skill output identifies a greenfield discovery lane, keeps feature_path unresolved, and continues product definition for the AI assistant. |
| `pm_first_guardrail` | PASS | With-skill output recognizes the empty-directory context, keeps scope unresolved, and explicitly states it will not write code or perform technical implementation. |
| `context_to_collect` | PASS | With-skill output asks the highest-information discovery question about the assistant's primary use case and requests the user's answer before proceeding. |
| `expected_pm_artifacts` | NOT_EXERCISED | The with-skill lane explicitly keeps PRD / DECISIONS pending while awaiting the core direction, so discovery is not yet complete. |
| `handoff_boundary` | NOT_EXERCISED | No handoff occurs in the with-skill output; it remains at the first PM discovery question. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=9fd14ddce425d122409287d93a082320ab2e698a101b12667af7769b0c386d35; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Routes the empty-directory idea into PM greenfield discovery, asks one focused product question, and preserves the no-code boundary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=8b9f700db950b8616b0b11dfd80c008bd1757ad930a2457a389264d481ea351e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a broad speculative MVP and several discovery questions, including implementation-oriented scope, without an explicit PM route.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain the user's answer to the primary use-case question, then continue discovery before producing PRD / DECISIONS or handing off.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
