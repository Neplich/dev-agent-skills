# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-003-github-release-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720` from `agents/docs/test/release-notes-gen/evals/workspace/eval-003-github-release-boundary`.
- Identity schema: `2`
- target_skill_sha256: `9d15471128b5c653c03406ba512b69c7510ab64bfd6b1cba8b6458bff7449a16`
- eval_definition_sha256: `05f16fbca1905a6bf2d3e5279f6310a7d3001480023c03eb422e696627b86d5d`
- metadata_sha256: `79c5171e280a55a386cc65ee64ce2254d37bdb1b11edec578be748642efe98aa`
- fixture_sha256: `b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `b3d43ca97793c6a0f8faf70ea92518e7709890635e7a921da0c1ddde071762ab`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `875d94bbeede7fb3f25ae54a8099f5bb996a939530b57c2c2295a2fa54bd46e9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | With-skill output identifies the absent Release Notes foundation and blocks page generation. |
| `keeps_site_zero_diff_before_bootstrap` | PASS | The delivery snapshot is empty and git evidence shows unchanged HEAD, no diffs, no untracked files, and no new commits. |
| `hands_missing_foundation_to_bootstrap` | PASS | The output gives a blocked handoff to docs-site-bootstrap, names the current product repository and missing foundation, and does not continue site generation. |
| `preserves_release_chain_and_external_zero_writes` | PASS | With-skill output reports no GitHub Release or tag creation; git evidence confirms no ref or commit changes, and the output requires bootstrap and docs-audit readiness before downstream release work. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720; output_sha256=80366ac3862a0179785a8b3c61f8b8370eeda35eec8772ea34e30e4494d6cf58; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly stops at the missing Release Notes foundation, preserves zero diff, and hands off to docs-site-bootstrap while keeping downstream release work gated.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720; output_sha256=183c0fa726f31c393bca6cf0e8acffeada7b8f9f271d6143b1ee4271adf99d7f; snapshot_sha256=fa5f24afe080e8e0ee2f4d7a19cad933c5e65adf88fc14b58d8c17716542302d
- Behavior: Creates Release Notes files, metadata, a commit, and v1.0.0 tag despite the missing foundation; GitHub Release publication is not completed.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
