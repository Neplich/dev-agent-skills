# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-011-change-tier-standard-full-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-11-change-tier-standard-full-gate`.
- Identity schema: `2`
- target_skill_sha256: `cec475406cc49b4c9cebbfe9c62f8f1a19fc3e7ced9282825f8f2930bab1478a`
- eval_definition_sha256: `da85ba336c757be6c6ca84ef12c1d1a20655adb3e82559a2c2234b5462387973`
- metadata_sha256: `6652dce9ab8a85ed09b58d853b1bdac1fd0f6f3e5ccd74f38c1d4aa6171a8cf4`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `e0fce32f646911cc00fe0709c7d0e934a3657054c9fc5a2efda7653a3ac97ea6`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `2c9f63eba393d7546f89112ce3f1659145dc2f6ca60bdba6ba71df10258a35a4`
- Repository HEAD: `133a65e3c3b501be88257e9d3a557af4d5ccd242`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `5047311446f87e0c9eb6ef7577938db174e729f8d09b2851971cbb87a063bf63`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classify_standard` | PASS | With-skill output explicitly classifies the change as standard and says it is not hotfix. |
| `require_prd_trd_alignment` | NOT_EXERCISED | The candidate requires approval-semantics confirmation before implementation; downstream handoff cannot yet occur without user confirmation. |
| `request_type_existing_update` | PASS | With-skill output identifies an existing behavior update, and the trace describes it as an existing behavior product-rule change. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9f63eba393d7546f89112ce3f1659145dc2f6ca60bdba6ba71df10258a35a4; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=d2ae2fad20a5304dbaf9b01bedf7b24e2b6c3933e6ab18496b0ea5397784b5ab; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified the request as a standard existing-behavior update, gated implementation on product expectation confirmation, and made no repository mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9f63eba393d7546f89112ce3f1659145dc2f6ca60bdba6ba71df10258a35a4; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=1045ce581047e5e75cbec3ca893e74429a4cd841fd68a0a7ca2715d03524b83e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline attempted implementation-oriented inspection without classification or alignment gating, then stopped only because the workspace was empty.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain user confirmation of the proposed approval semantics, then complete the required PRD/TRD or equivalent alignment before any downstream handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
