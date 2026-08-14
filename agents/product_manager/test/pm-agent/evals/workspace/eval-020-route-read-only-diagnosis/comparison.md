# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-020-route-read-only-diagnosis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638` from `agents/product_manager/test/pm-agent/evals/workspace/eval-020-route-read-only-diagnosis`.
- Identity schema: `2`
- target_skill_sha256: `cec475406cc49b4c9cebbfe9c62f8f1a19fc3e7ced9282825f8f2930bab1478a`
- eval_definition_sha256: `ac2e29c8ea600b5bded6655e93f469267e3a3d70f27c2a43049a20f14780fa3c`
- metadata_sha256: `3d6c30e198147d6fb34935d3b67ffafc86dff73948d015dcf7a4222ccb03c281`
- fixture_sha256: `0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `25ec3d21dbc5318b2aa7981fadceeb5bd08d4e0daef2594dfe1fa5018e038ab2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `548143066f55535e284127a49d04caed1052641b0e381dde2aacad45c5301978`
- Repository HEAD: `133a65e3c3b501be88257e9d3a557af4d5ccd242`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `5047311446f87e0c9eb6ef7577938db174e729f8d09b2851971cbb87a063bf63`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_read_only_bug_report` | PASS | With-skill output explicitly records `request_type: bug_report` and `mode: diagnosis_only`, states the conclusion is read-only, and does not enter repair. |
| `sets_zero_mutation_boundary` | PASS | With-skill output records `allowed_mutations: none`, states no code, configuration, external state, or Git content was modified, and locked git evidence shows unchanged HEAD/branch, no diffs, and no new commits. |
| `allows_unaligned_diagnosis_handoff` | NOT_EXERCISED | The candidate identifies Engineer as the downstream owner and marks the handoff blocked because engineer-agent is unavailable. The later handoff cannot be exercised, so the locked evidence cannot establish the required unaligned expectation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=548143066f55535e284127a49d04caed1052641b0e381dde2aacad45c5301978; fixture_sha256=0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638; output_sha256=f8ea82dffb299e02638192ef9c62b8bb0ca5e72d6e1f8614250002ed179570a6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified the request as read-only bug diagnosis, enforced a zero-mutation outcome, and stopped at a blocked downstream handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=548143066f55535e284127a49d04caed1052641b0e381dde2aacad45c5301978; fixture_sha256=0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638; output_sha256=495aeb8006752f3e11b49c6247a8c48a12d167ce359e4ff10aca7f4557c837d9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a read-only evidence summary and preserved workspace state, but did not provide the explicit bug-report routing and downstream handoff classification.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the unavailable Engineer/debugger capability or runtime evidence to exercise the unaligned diagnosis handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
