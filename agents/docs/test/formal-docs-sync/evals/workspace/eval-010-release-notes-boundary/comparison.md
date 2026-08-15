# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-010-release-notes-boundary`.
- Identity schema: `2`
- target_skill_sha256: `a3e1263ac8acb74f106913f935cefb0ebe0f7f059ccc011cd16715592fd0163d`
- eval_definition_sha256: `73a1610671f9f97761837a796f3ae7908687bbe25fc17ad4582a0bb4ee5c7fae`
- metadata_sha256: `2352ae604513521c63a446b6d886e6c879f4a0cef5861b4ee1c9c3ee9f319eba`
- fixture_sha256: `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `b3a1a852c447e6e1ef51ed958da793390c6914ade2f68188c4962daac377d01b`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b6ae3621879be63fa5b02212924eed11dd010ad027f0308f85d7666d26a57421`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `recognizes_release_communication_outcome` | PASS | With-skill output identifies a release-mode workflow with release-note surfaces and a release-notes generator, distinct from Product/Ops synchronization. |
| `routes_complete_entry_to_site_owner` | FAIL | It lists version, scope, evidence, and target surfaces, but does not actually deliver a complete confirmed host-inclusive handoff to the Docs owner; it defers routing until additional material is supplied. |
| `keeps_entire_site_zero_diff` | PASS | The locked git evidence shows empty status and diffs, and the output explicitly reports zero modification; no delivery snapshot exists. |
| `preserves_external_release_boundary` | PASS | The output explicitly excludes GitHub Release or tag creation and keeps the proposed work within site documentation surfaces. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=0ae876e2e1439c9f9c3b99f5555bd6102d44901612613c4fd1b95590b286c762; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly recognized the release-documentation workflow, blocked site writes, and preserved the external-release boundary, but did not route a complete confirmed entry to the Docs owner.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=a3afb1144f31677118d342c810aa10b3f731307b2dd653c18233d0bd410b5085; snapshot_sha256=a9c5231c368a37de9acc93f84ee7cc7627f2a8e5ffe097520b70c8f9bc8698c7
- Behavior: Created the release page, version index, and metadata, but violated the required zero-diff boundary; it is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane did not complete the required host-inclusive handoff to the unique Docs owner and instead deferred routing.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
