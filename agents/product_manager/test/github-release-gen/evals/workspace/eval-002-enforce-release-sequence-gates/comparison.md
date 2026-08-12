# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-002-enforce-release-sequence-gates`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-002-enforce-release-sequence-gates`.
- Identity schema: `2`
- target_skill_sha256: `0c9b1305da43afbfc22e6d563651831ce45be05793224d552c008cc393a37b1e`
- eval_definition_sha256: `4ae771ce624f2d4218d5a0892756a08ab5deb5771e2156fa84d9cebf89f45e20`
- metadata_sha256: `6e1c66d9908de26eec5a81a59cb64d6d09ad4a2d9291406739a3d318995009f5`
- fixture_sha256: `d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `7387039bc0ee52f805d2ca2d9e0306841c5745b2dec693f7be7ed2c655d6f462`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `site_notes_before_github_release` | PASS | With-skill output identifies the confirmed site handoff, the ready_for_tag pre-tag handoff, and PM preview ownership before any write. |
| `ready_for_tag_allows_preview_only` | PASS | It explicitly limits ready_for_tag to preview, states the target tag is absent or conflicting, and prohibits draft/publish. |
| `draft_omits_latest_and_publish_rechecks` | NOT_EXERCISED | Preview flags are shown, but no draft or publish write occurred, so draft omission and publish recheck behavior was not exercised. |
| `blocks_missing_tag_and_post_tag_audit` | PASS | Request A is rejected for absent tag and missing post-tag release_verified, with tag ownership returned to the release owner and audit ownership to docs-agent:docs-audit. |
| `blocks_missing_independent_approval` | PASS | Request B is rejected despite its claimed tag and release_verified because independent current maintainer publish approval is missing; prior permissions are not reused. |
| `keeps_preview_or_draft` | PASS | The candidate presents a complete preview and states that GitHub publication, tag creation, draft/publish, and release-create operations were not performed. |
| `inline_preview_body_and_version_normalization` | PASS | The locked preview contains an inline title, upgrade notes, and change details; it normalizes the version to 1.0.0-rc.1 and derives --prerelease, while no draft command was exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=5ed6e1066d666d2be5d6b531fe03b3b822ab2f3c70816f008890ab2022d0107e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a complete inline prerelease preview, applied the site and publication gates, rejected both unsafe requests, and performed no forbidden mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=c7a1210f40830308f16d0c0ef0008781d86f872e61fff577b7f256f713187a02; snapshot_sha256=ba40c4f003b2a6c842a44ea57bf8a37ffd217c6a9712f5e54632fa8ffd7f12f5
- Behavior: Fresh baseline also produced a preview and blocked both requests, but lacked the with-skill lane's explicit normalized flag and ownership/recheck boundary details.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain confirmed tag, post-tag audit, and independent current publish approval before any publish workflow.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
