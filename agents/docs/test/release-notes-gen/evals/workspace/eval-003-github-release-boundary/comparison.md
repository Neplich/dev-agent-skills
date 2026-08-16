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
- target_skill_sha256: `3da1a9a1466d6ecd43ed5c082adf803d01b5c2ca25dfee7a882fcc8113f7ce5c`
- eval_definition_sha256: `05f16fbca1905a6bf2d3e5279f6310a7d3001480023c03eb422e696627b86d5d`
- metadata_sha256: `79c5171e280a55a386cc65ee64ce2254d37bdb1b11edec578be748642efe98aa`
- fixture_sha256: `b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `b3d43ca97793c6a0f8faf70ea92518e7709890635e7a921da0c1ddde071762ab`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `9d7abf20333b60efc8aeaad2d302ecd422e44bb547e52f5a4d9623347a2b048b`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | Fixture lacks docs/site/release-notes and its writing contract; with_skill reports site_foundation: missing and blocks page generation. |
| `keeps_site_zero_diff_before_bootstrap` | PASS | With_skill reports zero modified release surfaces and pristine workspace; no release page, index, metadata, navigation, standards, or script changes appear in its snapshot or trace. |
| `hands_missing_foundation_to_bootstrap` | PASS | With_skill gives a blocked handoff to docs-site-bootstrap, identifies docs/site/release-notes as missing, and preserves docs-audit/GitHub Release ownership boundaries. |
| `preserves_release_chain_and_external_zero_writes` | PASS | With_skill explicitly reports no GitHub Release or v1.0.0 tag was prepared or created, keeps release execution unauthorized, and requires bootstrap plus renewed workflow/audit before continuation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720; output_sha256=30656598ded6204d42fc23cf1d03afdfcc710c8b1d799df79861844876f399ec; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly detects the missing Release Notes foundation, performs no site or external release writes, and hands off to docs-site-bootstrap.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720; output_sha256=e872d39f469100d7acc6520b60b4a8277056c13d06f2075446bbbba738c25a93; snapshot_sha256=70cec5c96e0addbd958f0d513b0ca2f84b577c2974b0c4462995185d8093b580
- Behavior: Fresh baseline incorrectly created Release Notes files, metadata, a handoff, a commit, and a local tag, while preparing release content.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
