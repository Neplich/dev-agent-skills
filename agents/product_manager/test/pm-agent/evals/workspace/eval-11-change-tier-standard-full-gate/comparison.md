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
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `2c9f63eba393d7546f89112ce3f1659145dc2f6ca60bdba6ba71df10258a35a4`
- Repository HEAD: `d48403a0878a4efe20dfa8446b2f98657d804d37`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `74d69a1dabc5d0a63769f3255d309f6f5ee9ae4497e47a765a73111f6806fda7`
- Skill overlay SHA-256: `75f5799ddfa14cce5f07d58cae0c13a32be9d74a8c76053b724a7f014a523c6f`
- Judge schema SHA-256: `e0fce32f646911cc00fe0709c7d0e934a3657054c9fc5a2efda7653a3ac97ea6`
- Eval definition SHA-256: `da85ba336c757be6c6ca84ef12c1d1a20655adb3e82559a2c2234b5462387973`
- Metadata SHA-256: `6652dce9ab8a85ed09b58d853b1bdac1fd0f6f3e5ccd74f38c1d4aa6171a8cf4`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classify_standard` | PASS | with_skill explicitly sets change_tier: standard and hotfix_disposition: rejected. |
| `require_prd_trd_alignment` | PASS | with_skill requires updated PRD/DECISIONS and states downstream engineering handoff is paused pending product-scope confirmation. |
| `request_type_existing_update` | PASS | with_skill explicitly sets request_type: existing_update and identifies the change as an update to existing refund approval behavior. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9f63eba393d7546f89112ce3f1659145dc2f6ca60bdba6ba71df10258a35a4; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=fbec3a36cc9c06af54631754deb7097a942645264c65215f207797a4be425df5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified the request as an existing standard update, rejected hotfix treatment, and enforced PM/product-alignment gating before downstream implementation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9f63eba393d7546f89112ce3f1659145dc2f6ca60bdba6ba71df10258a35a4; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a31ffb242c12f6485ada2f9e960d06178eec440021ac60706df57a951ce6cc35; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline only reported the empty repository and did not classify or gate the requested behavior change.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
