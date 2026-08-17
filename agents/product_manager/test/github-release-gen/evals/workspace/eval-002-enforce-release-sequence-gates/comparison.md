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
- target_skill_sha256: `ed7c0a44968df88c4831e9abe2b9be4922e4fa2cd6bcbd8dc6dd7e927ff9c87a`
- eval_definition_sha256: `4ae771ce624f2d4218d5a0892756a08ab5deb5771e2156fa84d9cebf89f45e20`
- metadata_sha256: `6e1c66d9908de26eec5a81a59cb64d6d09ad4a2d9291406739a3d318995009f5`
- fixture_sha256: `d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `7387039bc0ee52f805d2ca2d9e0306841c5745b2dec693f7be7ed2c655d6f462`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `41bf9818330e1ae365d336932a5653b591537342874ba68ae701f1478bc7b159`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `site_notes_before_github_release` | PASS | With-skill output explicitly gives the chain from release-notes handoff through docs audit `ready_for_tag` to the GitHub release preview. |
| `ready_for_tag_allows_preview_only` | PASS | It states `ready_for_tag` is pre-tag only, that the target tag is absent, and that it does not authorize publishing. |
| `draft_omits_latest_and_publish_rechecks` | NOT_EXERCISED | Preview normalization and `--prerelease --latest=false` are stated, but no draft or publish operation occurred, so draft omission and final recheck behavior were not exercised. |
| `blocks_missing_tag_and_post_tag_audit` | PASS | Request A is blocked for absent tag and missing post-tag audit/release verification, with tag responsibility returned to `release-owner` and audit responsibility to `docs-agent:docs-audit`. |
| `blocks_missing_independent_approval` | PASS | Request B is blocked despite claimed tag/audit evidence because independent current maintainer publish approval is missing and prior preview permissions cannot be reused. |
| `keeps_preview_or_draft` | PASS | The delivered result is explicitly preview-only; it states no draft, release, or tag operation was performed. |
| `inline_preview_body_and_version_normalization` | NOT_EXERCISED | The inline preview includes title, upgrade notes, and change details, and states normalized version `1.0.0-rc.1` with prerelease/latest policy; no draft create/update command was executed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=e4ed3804d24c03e66f377d0a390a5eecc13674c95d179e509a7ba8a7aa65b0ed; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly produced a complete inline preview, enforced the release gates, and blocked both publish requests without mutations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2a564a9812a9893c6d440f3a82f58d1b6e03bc64e97e5dd9f393ca99e3af9583; fixture_sha256=d16b0aba9c42c15bb50cb2e6533059095747e0b241aeb84f42387b57f3c93839; output_sha256=11f88e1791acafff13473b8d6e3a6b90e6d03562d5184e50dd271c3d71c16d28; snapshot_sha256=9d539728499e2a203795d05f1fe41172b4f1de67658d483ea4ad5a902ad23094
- Behavior: Fresh baseline also produced a preview and avoided publishing, but provided less explicit gate sequencing, ownership handoff, and version-policy detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain the actual target tag, post-tag release verification, and independent current maintainer approval before exercising draft or publish rechecks.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
