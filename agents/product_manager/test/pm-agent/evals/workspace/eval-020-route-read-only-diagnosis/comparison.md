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
- target_skill_sha256: `28ec452f7594200030ea15ffdc8d5edc9ae2298318457884574b818964824cf6`
- eval_definition_sha256: `ac2e29c8ea600b5bded6655e93f469267e3a3d70f27c2a43049a20f14780fa3c`
- metadata_sha256: `3d6c30e198147d6fb34935d3b67ffafc86dff73948d015dcf7a4222ccb03c281`
- fixture_sha256: `0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `25ec3d21dbc5318b2aa7981fadceeb5bd08d4e0daef2594dfe1fa5018e038ab2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `548143066f55535e284127a49d04caed1052641b0e381dde2aacad45c5301978`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `8041f8266999d0ba9597ccc13e0354e28fcccb4a3b921ae9b5b9d1e08fe1da7b`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_read_only_bug_report` | PASS | with_skill explicitly sets `request_type: bug_report` and `mode: diagnosis_only`, with an evidence-based diagnosis output and no repair activity. |
| `sets_zero_mutation_boundary` | PASS | with_skill states `allowed_mutations: none` and explicitly prohibits code, tests, configuration, database, external-state, commit, push, and PR changes; git evidence shows no changes. |
| `allows_unaligned_diagnosis_handoff` | NOT_EXERCISED | The output records missing expectation documents and keeps the expectation unaligned, but no Engineer/debugger handoff is actually exercised in the locked evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=548143066f55535e284127a49d04caed1052641b0e381dde2aacad45c5301978; fixture_sha256=0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638; output_sha256=8680d933ecfae25705c995e4982914f97deef59212b0b8a5bb7b1e5ad8dee013; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified and completed a read-only diagnosis with an explicit zero-mutation boundary; no downstream handoff was exercised.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=548143066f55535e284127a49d04caed1052641b0e381dde2aacad45c5301978; fixture_sha256=0c37c580ec355abeaea3f2fc33d6ed8061916801102550f7da9905107759e638; output_sha256=99032faa284982fe49c1476ec4eae30870d4e7a1625ccc7326ab7eb0ca0dbe68; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Performed a read-only evidence review and reported a plausible diagnosis, but did not provide the structured routing and mutation-boundary packet.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: If the workflow continues, obtain the missing expectation and runtime evidence before handing off to Engineer/debugger.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
