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
- target_skill_sha256: `6f8f132bc1f6eba3f9eb10727126ee30960b503351486b4fb6204e20571ffb35`
- eval_definition_sha256: `c9288fa3642ba9620547b9cef097cb305dbbd76229e2d8a01a3398cb410b16ae`
- metadata_sha256: `9bbacd8d1d30aecb1b4dd5b9add9750bc75aa04b90825b7bca13141ac06f87e8`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3a5175573f5c12faf8ef17031068ea4a3554be3c63ea98a9f0e35a5de2fe7ef6`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `495fc0f825d65d1e7057e4dc84ea777d069a48dcb665a6ab231607b5f4f53d34`
- Repository HEAD: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6c6b79d36b8b3a1bf132fd82bfece3cf6e7b256e3a9a58a0cdb78f4a09e26e69`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `explicit_invocation_proceeds` | PASS | With_skill output explicitly states classification ran, identifies the request as local file organization, says no PM category or downstream role matched, and keeps the task in PM without claiming the unenabled-directory guard blocked it. |
| `classifies_general_request` | PASS | With_skill output provides the required semantic classification: local file organization, no matching PM category or downstream role, task remains in PM; it does not skip classification or invent an incompatible owner. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=495fc0f825d65d1e7057e4dc84ea777d069a48dcb665a6ab231607b5f4f53d34; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=e12254e6c765f8d2adba89993a3a66ffa6b2ae7b62d32300602a6aa4eca12a52; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly proceeds through classification for the explicitly invoked pm-agent request and honestly keeps the unmatched general file operation in PM.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=495fc0f825d65d1e7057e4dc84ea777d069a48dcb665a6ab231607b5f4f53d34; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=adecfe5a25a28b305aacb6bed994480fbcd599fcdcb5e271305c0eec3f004740; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline stops because pm-agent is unavailable and the Downloads directory is missing, without performing the required classification.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
