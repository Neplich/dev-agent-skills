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
- target_skill_sha256: `cec475406cc49b4c9cebbfe9c62f8f1a19fc3e7ced9282825f8f2930bab1478a`
- eval_definition_sha256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- metadata_sha256: `7b48bd11ada861ee54366c474d903263630fabf2c5e0d3a66c9f38056e80908e`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `0e6be21ab02e72aa076a9b774d5cc60139434feba550f781574340027908427d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `133a65e3c3b501be88257e9d3a557af4d5ccd242`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `5047311446f87e0c9eb6ef7577938db174e729f8d09b2851971cbb87a063bf63`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | PASS | With_skill output explicitly selects `docs-agent:release-notes-gen -> pm-agent:github-release-gen` and identifies the confirmed scope as site Release Notes followed by GitHub Release preview. |
| `routes_github_release_to_pm_specialist` | PASS | With_skill output explicitly routes the downstream owner to `pm-agent:github-release-gen` and states it will not substitute for missing Docs/Release specialist capabilities. |
| `preserves_release_sequence` | NOT_EXERCISED | The fixture is empty and the required version sources, confirmed handoff, and runtime specialist capabilities are missing, so the later site-first execution and evidence consumption could not occur. |
| `does_not_use_old_pm_skill_name` | PASS | The output names `release-notes-gen` only as `docs-agent:release-notes-gen` and names the PM owner `pm-agent:github-release-gen`; it does not use the old PM owner name. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=10993bc43a037602da5c73e2167e87fa17e5396bc4ec1b6c548d8325d4ed5f97; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified and routed the workflow, preserved the execution boundary, and honestly stopped before unsupported release-note or preview generation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b8286580a3f51fa0a7cbe8dccd08d2bebce14ce91475401074e3b38f3aa992c1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline stopped at workspace inspection and did not provide the required specialist routing or release workflow structure.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the v1.0.0 change sources and confirmed handoff package.
- Next: Make the Docs and PM specialist capabilities available, then execute the site-first workflow.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
