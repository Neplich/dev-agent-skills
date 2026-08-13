# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-017-scope-guard-unenabled-general`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-17-scope-guard-unenabled-general`.
- Identity schema: `2`
- target_skill_sha256: `f9ea1bade234ebfd780e1e4773d4808a60f7baa61920e5859daea2b146c1ce93`
- eval_definition_sha256: `2b26ec5b13cba548fe19b4f508977afc54ba26189b14fbc48be376e4d57b8178`
- metadata_sha256: `05ea9f60607f11132b0f5ec8ca00cda463398f718c44648a9e2be81e39b17991`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `c5629d3608d1f142562d32ed4b435e3d2c557d9aa8b1c8b5f72fce35ca63e9a2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `0d80b9dec86a17116de51354d4b9cf60c96709a915b3655bf693ad2757979eb9`
- Repository HEAD: `2ac10136f4ed18048058361915e66c52b4e038c5`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `38ced6e12625600fae30e78c9378396b744a4b51798a40c97ef23b9d7aa57e71`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `scope_guard_stops_general_request` | PASS | With-skill trace checks the current directory for dev-agent-skills markers, finds none, then outputs that the directory is not enabled and stops without routing fields or downstream artifacts. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0d80b9dec86a17116de51354d4b9cf60c96709a915b3655bf693ad2757979eb9; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=80189bc5e6ea34383f68f8da07afdd24d2483347460737fedbe36b350e8d2fff; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Checks directory enablement, correctly identifies it as not enabled, briefly explains the scope boundary, and stops.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0d80b9dec86a17116de51354d4b9cf60c96709a915b3655bf693ad2757979eb9; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=33131b50b70e43e3a9eb560217114ebe0f21fd911ad03ce6d5c466c26e031782; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Attempts to inspect ~/Downloads and reports sandbox access limitations; does not perform the required enablement-based scope guard.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
