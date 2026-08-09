# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-003-prefix-classification`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-003-prefix-classification`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `53f035563de038125d09b7a8997f87e900d099e00223f427a7c690e11ebbe449`
- Skill overlay SHA-256: `9534a5bf71391ac48cfd6a48ca8f80e93da520d6ea9d2026741fd864da0cb720`
- Judge schema SHA-256: `cc05e28bb9aed099804431e1cee55bda0cec7614cc8c780d6f8ad4d50c137367`
- Eval definition SHA-256: `02c7a6bcc66679fa2f47687ffd7cdba26fff303adab62c4e3435b49f28878db8`
- Metadata SHA-256: `7c295252d061c5f27afb73a5d2bc7ec230ac3e0e3896f6109062c7b18ee9cf2e`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feat_auth_added_add_oauth2_login_support` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; no Added entry was produced. |
| `fix_fixed` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; no Fixed section was produced. |
| `chore_deps` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; dependency handling was not exercised. |
| `build_deps_skipped` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; dependency handling was not exercised. |
| `perf_changed` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; no Changed section was produced. |
| `feat_added_breaking` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; breaking-change handling was not exercised. |
| `docs_release_workflow_changed` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; release-workflow handling was not exercised. |
| `test_release_acceptance_changed` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; release-acceptance handling was not exercised. |
| `ci_release_gate_changed` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; CI release-gate handling was not exercised. |
| `docs_typo_skipped` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; docs filtering was not exercised. |
| `ci_cache_skipped` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; CI filtering was not exercised. |
| `remove_removed` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; no Removed section was produced. |
| `security_security` | NOT_EXERCISED | With-skill output requests the target mode before generating the changelog; no Security section was produced. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=060c6a19e40c3ccd8dc27ae59ef3a4cf3e1384496e5d74fde7382b78e8a631ff; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly paused to request the required target changelog mode; content transformation was not yet exercised.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9be6d0e23157c436ac95fa175b7c253fc5c8a58bd7930d5f75b8e2f143978496; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a1708dc2c3a196376850cc13ad0c6d6b8bd1405d55e2464c05b91a2225f1001b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a complete Keep a Changelog-style result covering the requested user-visible changes and exclusions.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Select a target mode, then generate and evaluate the changelog content.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
