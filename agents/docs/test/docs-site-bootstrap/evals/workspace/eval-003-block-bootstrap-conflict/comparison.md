# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-003-block-bootstrap-conflict`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `67d646aaa1407e943f08140487b646ac63c9406ed33f7972e7921d67116c9f4a` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-003-block-bootstrap-conflict`.
- Identity schema: `2`
- target_skill_sha256: `2846695e854af26b77f56804bd16db1050e2bacd34407999d119ed4e4a881599`
- eval_definition_sha256: `ef71b65d8d90e0a7a85b11140f77333b6bccfac4b39b25f67875d33153f0ebea`
- metadata_sha256: `dd91ae0a6e0ac8c19ffeb9b16bf575dc1d6e559c0626e7027f9e04c671f270d0`
- fixture_sha256: `67d646aaa1407e943f08140487b646ac63c9406ed33f7972e7921d67116c9f4a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `8fb0a4310aa73072ce3915bd9569df86e49409cfb5df2e41bfa626f79fa1e1ef`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `7e27a0b4acbeb0bbab6d1ce4f4eaef1707f80d3f366d62ddd92d0e2d6f621f17`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `c4382a755d40b4c37cbb5843089f99a5655b439fd2c6460df6c8b5adeb479967`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_complete_conflict_list` | NOT_EXERCISED | With_skill output requests user confirmation before inspecting files or making changes; no delivery snapshot or git mutation exists, so this later conflict-handling assertion is not exercised. |
| `does_not_overwrite_conflict` | NOT_EXERCISED | The with_skill lane has an empty delivery snapshot and unchanged git state, but it has not yet reached the file-handling step because confirmation is pending. |
| `offers_explicit_resolution_choices` | NOT_EXERCISED | The with_skill lane has not yet presented resolution choices; it correctly pauses for confirmation before proceeding. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7e27a0b4acbeb0bbab6d1ce4f4eaef1707f80d3f366d62ddd92d0e2d6f621f17; fixture_sha256=67d646aaa1407e943f08140487b646ac63c9406ed33f7972e7921d67116c9f4a; output_sha256=74f6830586a8b23df838b0ee1d448033d8841c7a52252094986ab82bb13edef3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly pauses for confirmation before inspecting or modifying the workspace; no mutation is evidenced.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=7e27a0b4acbeb0bbab6d1ce4f4eaef1707f80d3f366d62ddd92d0e2d6f621f17; fixture_sha256=67d646aaa1407e943f08140487b646ac63c9406ed33f7972e7921d67116c9f4a; output_sha256=57f4bd698bb05da54b29290ea40f5406d85cc4119a8c26e86fc6d1544c4898bc; snapshot_sha256=1dee3607f55f5eca00e18d74e19d8d5ab4c1149f2715b14ff03df592725961b0
- Behavior: Fresh baseline proceeds without confirmation, modifies the manifest with a successful preservation status, and does not offer explicit overwrite/merge/keep choices.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain user confirmation, then evaluate the conflict list, blocked state, preservation, and resolution choices.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
