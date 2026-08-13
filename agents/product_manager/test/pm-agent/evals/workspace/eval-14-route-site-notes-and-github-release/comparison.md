# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-14-route-site-notes-and-github-release`.
- Identity schema: `2`
- target_skill_sha256: `f9ea1bade234ebfd780e1e4773d4808a60f7baa61920e5859daea2b146c1ce93`
- eval_definition_sha256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- metadata_sha256: `7b48bd11ada861ee54366c474d903263630fabf2c5e0d3a66c9f38056e80908e`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `0e6be21ab02e72aa076a9b774d5cc60139434feba550f781574340027908427d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `2ac10136f4ed18048058361915e66c52b4e038c5`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84ad07662e525000bb3bbf1da6aa3f2d49322c424326b70644431a72cdb52c55`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | PASS | With_skill trace routes the request to docs-agent:release-notes-gen and explicitly assigns the site notes step first. |
| `routes_github_release_to_pm_specialist` | NOT_EXERCISED | The trace names pm-agent:github-release-gen as the subsequent owner, but that later step cannot occur because the required specialist and confirmed release source are unavailable. |
| `preserves_release_sequence` | NOT_EXERCISED | The trace explicitly states site Release Notes first, followed by Docs gates and then the PM GitHub Release step; actual downstream consumption is not exercised because the handoff is blocked. |
| `does_not_use_old_pm_skill_name` | PASS | The with_skill routing names docs-agent:release-notes-gen for Docs and pm-agent:github-release-gen for PM; it does not use release-notes-gen as the PM owner. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=300846dc1a9cab996c3cbdf497c1fb5d9a74be9ae422282ccdbc75ab08361060; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes site-facing release notes to the Docs specialist, preserves the intended site-first boundary, and identifies the PM GitHub Release specialist, but stops before downstream execution because required capabilities and release evidence are unavailable.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=d9df2fbc3eaa3691e4cbc274446d2b5402c89de6201ed6131ee225855487795d; snapshot_sha256=3312afa0b5db859f79176642d45cc34f3b99e64674f725a4a307729054b00e9f
- Behavior: Creates two uncoordinated draft files and does not provide the specialist routing or gated handoff behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide confirmed v1.0.0 release evidence and make the Docs and PM GitHub Release specialists available before exercising the downstream handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
