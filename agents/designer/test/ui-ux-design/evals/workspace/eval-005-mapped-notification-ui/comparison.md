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
- target_skill_sha256: `749980e18a4ced3c2a9cbbdaeb6230841130618487b0995560867366d48b7d72`
- eval_definition_sha256: `25a9beaf5037d128f11073d7bdad29e775b60a170f80ba9b4b2cd556e1ef1469`
- metadata_sha256: `2df7ffae351f05ff856a7ddf2ab545a06891ad7b1dee1da8ddccd64f5e254eea`
- fixture_sha256: `cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `2797a1f8eaaa6ec1663895e21733e03c38b2053355b7534ad87b60c49209372a`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `e26256f2206c322bda9ae81b814ac63fff1a476a818df2afc0a6e339fb00af73`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace shows the with_skill lane identified the task path, inspected the change map, then read the matched required document `docs/site/api/notification-preferences.md`; no unrelated formal document contents were read. |
| `verifies_against_code` | PASS | The locked trace and final output both identify that `src/ui/notification-preferences.html` has no `checked` attribute, so the actual static default is unchecked, and explicitly contrast this with the document's enabled-by-default claim. |
| `treats_unverified_as_low_trust` | PASS | The final output explicitly identifies `last_verified_version: unverified` as low trust and bases the default-state conclusion on the HTML code while retaining the document claim as a conflict. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2797a1f8eaaa6ec1663895e21733e03c38b2053355b7534ad87b60c49209372a; fixture_sha256=cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a; output_sha256=d9cddf1e30dc5376f4fcbf05aa8ac8f17f546e5a7ad3b883cbb23ed7f07ef438; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Applied the design entry gate, verified the mapped document against the HTML, treated the unverified document as low trust, and stopped with an evidence-based handoff blocker without mutating files.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2797a1f8eaaa6ec1663895e21733e03c38b2053355b7534ad87b60c49209372a; fixture_sha256=cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a; output_sha256=9fde896516f3537b76301db3936387917e1aed6c3aed084a7d3b9f5b051863c8; snapshot_sha256=30379880e94fd1ab46c5f9d28b293c0ddc7f874dbd84b4a2915cc4fbe569b775
- Behavior: Produced and modified a formal notification-preferences document, correctly noted the HTML default was unchecked, but treated the documented enabled default as the product rule without the required low-trust process.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain the PM/design handoff and confirmed feature_path, then create the UI/UX specification.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
