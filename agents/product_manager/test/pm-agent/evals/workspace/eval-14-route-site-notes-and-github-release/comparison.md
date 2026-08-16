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
- target_skill_sha256: `ed93e443692bf05e76aaa38c8a5b8faff57190219ed48b9335316584424e6eb9`
- eval_definition_sha256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- metadata_sha256: `97d6e27f41f4971c47d9cb45fcc18ec16575e5aae533718195d23b38c3bf2c56`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `0e6be21ab02e72aa076a9b774d5cc60139434feba550f781574340027908427d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `93ad7bb06cc0fc8447a9937ca3e9f764d2a2c745d97e115ce6e8522948fec408`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | PASS | With_skill output explicitly names `docs-agent:release-notes-gen` as the first owner and does not route the site notes to PM or changelog-gen. |
| `routes_github_release_to_pm_specialist` | PASS | With_skill output explicitly names `pm-agent:github-release-gen` as the downstream owner and blocks all release actions; Docs is not shown executing the GitHub Release. |
| `preserves_release_sequence` | NOT_EXERCISED | The workflow is blocked before confirmed site notes, Docs gates, and audit evidence exist, so the later consumption sequence cannot be exercised. |
| `does_not_use_old_pm_skill_name` | PASS | The PM owner is named `pm-agent:github-release-gen`; `release-notes-gen` appears only as the Docs owner. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=97229e73b50f6d7506bf9c1ffdf076c0af1f871f0ef9be1e9b48c4b384122f5c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the empty fixture, routes site notes to Docs then GitHub Release work to PM, and safely blocks without confirmed release evidence or mutations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=67cba33b22bf0a2a364504c7f619d7ed753029936f7b01bd6552973a0185e629; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline only reports the empty repository and requests version facts; it provides no specialist routing or release-gate handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
