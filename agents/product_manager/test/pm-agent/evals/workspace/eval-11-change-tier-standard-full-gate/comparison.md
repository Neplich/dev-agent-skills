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
- target_skill_sha256: `e17c69ef6e179644f91ff00df55f141c375753f4668f30aca4e37e8247a60506`
- eval_definition_sha256: `da85ba336c757be6c6ca84ef12c1d1a20655adb3e82559a2c2234b5462387973`
- metadata_sha256: `6652dce9ab8a85ed09b58d853b1bdac1fd0f6f3e5ccd74f38c1d4aa6171a8cf4`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `e0fce32f646911cc00fe0709c7d0e934a3657054c9fc5a2efda7653a3ac97ea6`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `2c9f63eba393d7546f89112ce3f1659145dc2f6ca60bdba6ba71df10258a35a4`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `15f4acf7caf3d5cd73abf45c67ad35faa887bc8f89f51c7e53854fb1514182b5`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classify_standard` | PASS | With-skill output explicitly sets `change_tier: standard` and `hotfix_disposition: rejected`. |
| `require_prd_trd_alignment` | PASS | With-skill output blocks implementation because PRD/DECISIONS, TRD, tests, and handoff evidence are missing; it requires approved change documentation/product alignment before handing work to engineering. |
| `request_type_existing_update` | PASS | With-skill output explicitly sets `request_type: existing_update` and identifies the behavior change from automatic approval to administrator confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9f63eba393d7546f89112ce3f1659145dc2f6ca60bdba6ba71df10258a35a4; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=4bd472fb5e36033c4a20e4a0dd86ea9ba0d827fcbd7c42eec657ca46525fb003; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified the request as an existing update with standard change tier, rejected the hotfix path, and retained the product-alignment gate before implementation handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9f63eba393d7546f89112ce3f1659145dc2f6ca60bdba6ba71df10258a35a4; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=2abaf7e8316a1a198b019e5108a2991272bf7a16ec795297f8dcfcaae33e26a9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline only reported the empty repository and did not classify the request or state the required product-alignment gates.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
