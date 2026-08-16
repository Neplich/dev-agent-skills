# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-015-manual-page-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad` from `agents/docs/test/docs-audit/evals/workspace/eval-015-manual-page-evidence`.
- Identity schema: `2`
- target_skill_sha256: `dafd53371901dfd724f88c70262b157e59494d29da1c613d0ef130564b6ff4f9`
- eval_definition_sha256: `aa707a4a153cd14f8630bcfdbc7593482bcfc1de05bf7582ac2eeb6f645afb7d`
- metadata_sha256: `2b093794d817fa1de245fdac944141cf26e940fab11bd3c871b66f71a9c40eac`
- fixture_sha256: `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `cde7d254babf29e4546bfe9e69c491c81147f2f6aec782f40fd9d10a9dc4b4fd`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7e61bd8eca6431729aee1f3be4656be0a4348119eb1218623bafd54cfaead2ab`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_step_screenshot_files` | PASS | With-skill final output states step-2-save-member.png is nonexistent; locked trace records the SVG as a Scalable Vector Graphics image. |
| `checks_caption_step_correspondence` | PASS | Final output identifies the mismatch between step 1 opening access settings and the caption describing a delete-workspace confirmation dialog. |
| `checks_manual_navigation_reachability` | PASS | Final output states the page is not navigated to and the sidebar snapshot lacks it; locked trace records the public landing page and manual index lacking the target entry. |
| `checks_manual_redaction` | PASS | Final output identifies test.user@example.invalid in the page and token-demo-redact-me at SVG line 5 as redaction blockers. |
| `blocks_manual_stamp` | PASS | Final output concludes blocked and states no version stamp was performed; locked evidence shows last_verified_version remains unverified and no ready_for_tag result. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=f66d4334e3999cf060b4aa860c9a0f2857fe1afc676e45068333b9663f96eb48; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly performed the bounded manual audit, identified all required defects, and blocked stamping.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=7d38cbda41fac11d424cb21213b1614938e052e413a4ab3167c88f9b4ec5b868; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also identified the main defects and blocked release, but provided a less complete audit narrative.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
