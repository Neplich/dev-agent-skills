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
- target_skill_sha256: `e17c69ef6e179644f91ff00df55f141c375753f4668f30aca4e37e8247a60506`
- eval_definition_sha256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- metadata_sha256: `97d6e27f41f4971c47d9cb45fcc18ec16575e5aae533718195d23b38c3bf2c56`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `0e6be21ab02e72aa076a9b774d5cc60139434feba550f781574340027908427d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d3ccf1feb2a2b63aa5deb225990edb65d2b64cd2211e04c10dfc7fea67e865ab`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | PASS | With-skill output explicitly selects `docs-agent:release-notes-gen` and states site/user Release Notes belong there, not to PM or changelog. |
| `routes_github_release_to_pm_specialist` | PASS | The output routes the downstream GitHub Release work to `github-release-gen`; raw skill evidence identifies the PM owner as `pm-agent:github-release-gen`, and states Docs must not perform Release operations. |
| `preserves_release_sequence` | PASS | The output preserves the order: Docs confirmation and `docs-audit` `ready_for_tag` precede the GitHub Release preview, with no release action before those gates. |
| `does_not_use_old_pm_skill_name` | PASS | `release-notes-gen` is used only under `docs-agent`; the GitHub Release owner is separately identified as `github-release-gen`/`pm-agent:github-release-gen`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=2e13bd7593764232848c0f8a5bcd3129792bbea7829335f7d750d9777da959cd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes site notes to Docs, preserves the Docs-gated sequence, and identifies the separate PM GitHub Release owner while blocking unsupported execution.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=75f631c447213f1409cfbd5ef8b8948be961c7fdde44cb32481f8cdd2aa43478; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline only requests missing release facts and does not provide the required specialist routing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
