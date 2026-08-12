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
- target_skill_sha256: `f9ea1bade234ebfd780e1e4773d4808a60f7baa61920e5859daea2b146c1ce93`
- eval_definition_sha256: `5311d447a76e8a9004cf025f69ba69a2ff818f798cd0da111a4a59a3c163d9c4`
- metadata_sha256: `3d6c30e198147d6fb34935d3b67ffafc86dff73948d015dcf7a4222ccb03c281`
- fixture_sha256: `0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `25ec3d21dbc5318b2aa7981fadceeb5bd08d4e0daef2594dfe1fa5018e038ab2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `548143066f55535e284127a49d04caed1052641b0e381dde2aacad45c5301978`
- Repository HEAD: `2ac10136f4ed18048058361915e66c52b4e038c5`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84ad07662e525000bb3bbf1da6aa3f2d49322c424326b70644431a72cdb52c55`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_read_only_bug_report` | PASS | With-skill output explicitly includes `request_type: bug_report` and `mode: diagnosis_only`. |
| `sets_zero_mutation_boundary` | PASS | With-skill handoff includes `allowed_mutations: none` and prohibits code, tests, configuration, database, external-state, commit, push, and PR changes; git evidence also shows no mutation. |
| `allows_unaligned_diagnosis_handoff` | PASS | With-skill output routes to Engineer for read-only evidence collection, states expected behavior is unaligned, and says the system root cause cannot yet be confirmed; no repair is entered. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=548143066f55535e284127a49d04caed1052641b0e381dde2aacad45c5301978; fixture_sha256=0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638; output_sha256=e2ec9ebb205a99b7f08c546d8c2eb269644524f9de7a43e8950282516db43ed7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classifies the request, establishes a zero-mutation diagnosis boundary, and provides an unaligned Engineer handoff despite missing expectation documents.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=548143066f55535e284127a49d04caed1052641b0e381dde2aacad45c5301978; fixture_sha256=0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638; output_sha256=3fad9ff42aadd98c2a8d95754cab89c55be694229505ca2c92654883972a8662; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a read-only incident diagnosis and confirms no mutation, but does not provide the required structured classification or Engineer handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
