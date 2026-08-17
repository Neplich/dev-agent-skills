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
- target_skill_sha256: `e17c69ef6e179644f91ff00df55f141c375753f4668f30aca4e37e8247a60506`
- eval_definition_sha256: `ac2e29c8ea600b5bded6655e93f469267e3a3d70f27c2a43049a20f14780fa3c`
- metadata_sha256: `626240265d5c7ac5c06804a17b53a20dce96bac558a2504b82b9a8f747b23779`
- fixture_sha256: `0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `25ec3d21dbc5318b2aa7981fadceeb5bd08d4e0daef2594dfe1fa5018e038ab2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `548143066f55535e284127a49d04caed1052641b0e381dde2aacad45c5301978`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `52f05d4a15e835bc02af96227cfa6ed13176103348e840ad1421a1fac30b743e`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_read_only_bug_report` | PASS | With-skill output explicitly labels the request as `request_type: bug_report`, `mode: diagnosis_only`, and states no repair will be proposed or executed. |
| `sets_zero_mutation_boundary` | PASS | With-skill output explicitly sets `allowed_mutations: none` and prohibits modifying code, tests, E2E, configuration, databases, external state, commits, pushes, or PRs; git evidence shows no changes. |
| `allows_unaligned_diagnosis_handoff` | PASS | With-skill output routes read-only evidence collection to Engineer's `debugger`, marks `expected_behavior_alignment: unaligned`, states that `implementation_deviation` cannot be confirmed, and pauses for confirmation before continuing. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=548143066f55535e284127a49d04caed1052641b0e381dde2aacad45c5301978; fixture_sha256=0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638; output_sha256=4c656dde4f90ea613041d1b2b3d0857e92b37eed63b575e63027edc5ddf3a038; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified the incident as diagnosis-only, enforced a zero-mutation boundary, and prepared an unaligned Engineer/debugger handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=548143066f55535e284127a49d04caed1052641b0e381dde2aacad45c5301978; fixture_sha256=0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638; output_sha256=2aade89148702f5b2f10a7db3f90bdc932c8c6b8ee5394adbdf350c546575650; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a useful read-only incident summary and reported no mutations, but did not provide the explicit routing, mutation-boundary, or unaligned handoff structure.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
