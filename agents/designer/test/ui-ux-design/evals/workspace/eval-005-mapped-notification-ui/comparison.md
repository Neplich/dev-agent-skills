# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `ui-ux-design`
- Eval: `eval-005-mapped-notification-ui`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a` from `agents/designer/test/ui-ux-design/evals/workspace/eval-005-mapped-notification-ui`.
- Identity schema: `2`
- target_skill_sha256: `2088a9b7ee00fc1f620b92a5141c4a34a4c48ca289c4be5cea831626687d85b8`
- eval_definition_sha256: `25a9beaf5037d128f11073d7bdad29e775b60a170f80ba9b4b2cd556e1ef1469`
- metadata_sha256: `2df7ffae351f05ff856a7ddf2ab545a06891ad7b1dee1da8ddccd64f5e254eea`
- fixture_sha256: `cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `2797a1f8eaaa6ec1663895e21733e03c38b2053355b7534ad87b60c49209372a`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `beec8510dfdfe8132ffae9f12e486d2c527ec9245f5752f40eaeb251a4d63e70`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Locked trace shows the candidate read the change-map, identified the single required document, then read that document and the page source; no unrelated formal documents were read. |
| `verifies_against_code` | PASS | Locked trace and delivery snapshot show direct inspection of the HTML input without `checked`, identification of the documented default-on conflict, and selection of code as current truth. |
| `treats_unverified_as_low_trust` | PASS | The locked evidence records `last_verified_version: unverified`, reads the document despite that status, and expands verification to the HTML source rather than rejecting or relying solely on the document. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2797a1f8eaaa6ec1663895e21733e03c38b2053355b7534ad87b60c49209372a; fixture_sha256=cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a; output_sha256=8b2576987187720a288d91eebfc801871e7321980103212a0c4cf0c36e1c323b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Verified the mapped document and source code, detected the default-state conflict, treated the document as unverified, and stopped at the required handoff gate.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2797a1f8eaaa6ec1663895e21733e03c38b2053355b7534ad87b60c49209372a; fixture_sha256=cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a; output_sha256=0671daf8775fa223070ce7d6591c9cc010ff2e773ebda5733a4943e5cc3806f0; snapshot_sha256=220c8d0d4f2d9ce4cb1d4426c94b78604d26ab15ccfe0ee3bc0ab0e32f61b330
- Behavior: Fresh baseline updated the formal document with a UI/UX specification and correctly recorded the code/document default conflict.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide a confirmed PM/design handoff and feature_path, then create the UI/UX specification.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
