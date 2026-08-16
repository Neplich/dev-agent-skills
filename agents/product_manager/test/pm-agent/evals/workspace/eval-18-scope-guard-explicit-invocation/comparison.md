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
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `495fc0f825d65d1e7057e4dc84ea777d069a48dcb665a6ab231607b5f4f53d34`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `8b076cb82c470b131f01d4ac1cd0d36cbfb1e690ece346a8313d30b76a409813`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `explicit_invocation_proceeds` | FAIL | With-skill trace invokes pm-agent and reads its entry rules, but then classifies the request as ordinary non-R&D and proceeds with direct file-operation planning instead of stopping in PM after finding no matching category/owner. |
| `classifies_general_request` | FAIL | With-skill trace includes a classification discussion, but does not provide a stable request_type and selected owner, and proceeds directly toward file operations after stating no PM specialist can be routed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=495fc0f825d65d1e7057e4dc84ea777d069a48dcb665a6ab231607b5f4f53d34; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=6431e6bbad48733d37ed13995336cade41d468abf2f2679e30d7b977cf24ff72; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Used pm-agent's skill content and inspected the requested path, but incorrectly treated the unmatched ordinary file request as eligible for direct execution; no files were moved because permissions blocked access.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=495fc0f825d65d1e7057e4dc84ea777d069a48dcb665a6ab231607b5f4f53d34; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=9f32cb8ed90f3768ffd8ace0bde5cb12151a710324e6e02ee67ba6dbd682501e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline reported pm-agent unavailable and Downloads inaccessible, then stopped without classification or execution.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane violates the explicit pm-agent boundary by proceeding with file-operation execution after determining the request has no PM category or downstream owner.
- The with_skill lane does not satisfy the required PM classification output and does not stop after an unmatched classification.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
