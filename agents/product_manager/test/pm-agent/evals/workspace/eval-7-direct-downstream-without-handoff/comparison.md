# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-007-direct-downstream-without-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-7-direct-downstream-without-handoff`.
- Identity schema: `2`
- target_skill_sha256: `a37bf10fca64a8e15e6213ecdd45b65783814d307c78fd8d8ce6ab45b20effef`
- eval_definition_sha256: `186d8c8ca55f244592124c29f316a47679d008908c7385a9f2c3b6deef26649d`
- metadata_sha256: `70b36659756bbd4d7fc0e09d0fabc7ee5ba1a168323c148fa735110fb59ec768`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `e2570bd95ea9768bb87ca218eab9d1b8a91216a2492cd9d22af400362c435dbb`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f`
- Repository HEAD: `3f5e81c4837ef85284a7d5381575e40267796c92`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6f4abf80e411dc3e6124c51093f07046c341195b1b2f0e9981a535c9960cb623`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_pm_alignment` | PASS | With-skill output keeps the request blocked at PM alignment, marks entry_basis as blocked, and explicitly says no code or implementation files will be created; it does not claim Engineer handoff completion or downstream execution. |
| `stay_in_pm_alignment` | PASS | With-skill output marks feature_path unresolved, provides no source documents or handoff packet, routes the next action to PM alignment, and states that Engineer implementation cannot begin. |
| `blocks_engineering_without_basis` | FAIL | With-skill output identifies missing product/design materials and unresolved layout expectations and prohibits code changes, but it does not clearly state that technical scope or implementation basis must also be confirmed before engineering begins. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=4eb9f1b88fa2db791dc6679c4e6bd1d8458515adc0ef18acbc67f40d96bcd962; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly remains in PM alignment and blocks implementation, but incompletely states the required pre-engineering evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a9732072f998bd1a38d23d070a078968d50a2c909ad366dab14ca9990553fca5; snapshot_sha256=3b65e785d8be8b5f0c17dd40a56b0f8b26f60cfe99c35278fef612435bebcc9c
- Behavior: Fresh baseline immediately implemented and delivered new settings-page files without product, design, or engineering-basis alignment.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- blocks_engineering_without_basis: missing explicit technical-scope or implementation-basis gate.
- Next: Require explicit confirmation of technical scope or implementation basis, alongside product scope and design/requirements evidence, before engineering handoff or code changes.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
