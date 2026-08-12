# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-001-generate-site-release-notes`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5f0f5b3062eae992b755cdc1ae78582ce41bb32058f8a49d6044db233c5966f5` from `agents/docs/test/release-notes-gen/evals/workspace/eval-001-generate-site-release-notes`.
- Identity schema: `2`
- target_skill_sha256: `c8459f189e8d92d91e1c7ede8875090bfc1c2e1e04b8f18983b4339e6b65ba34`
- eval_definition_sha256: `65fbac4fd20096e04fd9044ef9811d00f14a304548ada95a65b3bc87c1320345`
- metadata_sha256: `f1489da43deb17946a7db1865ce4492ffcbc2d33d7073fbbdc572711b748a76c`
- fixture_sha256: `5f0f5b3062eae992b755cdc1ae78582ce41bb32058f8a49d6044db233c5966f5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `37b31d01c6d97d7403db04c5a14501c9f7c823331bdaca410487353335744541`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_version_confirmation` | PASS | with_skill identifies v1.0.0 as proposed and explicitly states the confirmation record does not confirm the target version. |
| `stops_before_loading_execution_workflow` | PASS | with_skill returns blocked at the entry gate and provides no candidate release-note body or generated page. |
| `keeps_all_site_surfaces_unchanged` | PASS | Locked git evidence shows no status, diff, commit, ref, or untracked-file changes; delivery_snapshot is empty. |
| `does_not_run_post_entry_checks` | PASS | The captured trace shows no dependency installation or docs-check command, and the output says checks were not run and no ready handoff was sent. |
| `returns_version_ambiguity_to_pm` | PASS | with_skill returns blocked, assigns missing version confirmation to pm-agent, specifies re-entry after traceable confirmation, and preserves GitHub Release/tag boundaries. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750; fixture_sha256=5f0f5b3062eae992b755cdc1ae78582ce41bb32058f8a49d6044db233c5966f5; output_sha256=77a07a0a4dc2aab271267543e772d8570a3ae196e452a8918fda2e7135868a6a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks on missing maintainer version confirmation, preserves site state, and avoids downstream workflow and handoff actions.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750; fixture_sha256=5f0f5b3062eae992b755cdc1ae78582ce41bb32058f8a49d6044db233c5966f5; output_sha256=932340e77cf1f31d244a7ef3628bdccc728e252889c5593c999f9ddfd9b1a1bc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline recognizes the missing version confirmation but proceeds to draft release-note content instead of stopping at the entry gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
