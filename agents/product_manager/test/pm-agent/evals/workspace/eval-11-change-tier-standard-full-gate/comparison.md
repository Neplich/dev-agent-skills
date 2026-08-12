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
- Repository HEAD: `715bd6b76fcd6f14f475aeabe141543063d431ba`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `be11ec63823b148323fef6c35d27c0861bd093b24d683f705e846234e98b7baa`
- Skill overlay SHA-256: `961e7aacbdec2d154ad578bc7bf54d5d734f34031af1384fb20aa67a8e2d392a`
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
| `classify_standard` | PASS | With-skill output explicitly sets `change_tier: standard` and `hotfix_disposition: rejected`. |
| `require_prd_trd_alignment` | PASS | With-skill output requires scope and process confirmation, calls for PRD/DECISIONS update, recommends change-impact analysis before downstream mirroring, and explicitly prohibits handing off to Engineer before alignment. |
| `request_type_existing_update` | PASS | With-skill output explicitly sets `request_type: existing_update` and identifies the approved behavior change from automatic approval to administrator confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9f63eba393d7546f89112ce3f1659145dc2f6ca60bdba6ba71df10258a35a4; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b9d15125b5c1d95f159154981655f8cfeefe48cf992003b06e521c38c615b047; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified the request as an existing standard update, rejected hotfix treatment, preserved the product-alignment gate, and paused for required scope confirmation before downstream implementation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9f63eba393d7546f89112ce3f1659145dc2f6ca60bdba6ba71df10258a35a4; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=e5cfcff8325c190b6f50023bf7cbc327d8813f0d9c3bddaf4afb7da7916300ea; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline reported only that the workspace lacked project files and did not provide the required request classification or governance handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
