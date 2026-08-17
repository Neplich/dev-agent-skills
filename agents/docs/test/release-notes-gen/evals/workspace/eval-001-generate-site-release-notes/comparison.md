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
- target_skill_sha256: `3da1a9a1466d6ecd43ed5c082adf803d01b5c2ca25dfee7a882fcc8113f7ce5c`
- eval_definition_sha256: `65fbac4fd20096e04fd9044ef9811d00f14a304548ada95a65b3bc87c1320345`
- metadata_sha256: `f1489da43deb17946a7db1865ce4492ffcbc2d33d7073fbbdc572711b748a76c`
- fixture_sha256: `5f0f5b3062eae992b755cdc1ae78582ce41bb32058f8a49d6044db233c5966f5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `37b31d01c6d97d7403db04c5a14501c9f7c823331bdaca410487353335744541`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `9d7abf20333b60efc8aeaad2d302ecd422e44bb547e52f5a4d9623347a2b048b`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_version_confirmation` | PASS | With-skill output explicitly identifies v1.0.0 as proposed only and cites both the planning note and confirmation record as lacking maintainer version confirmation. |
| `stops_before_loading_execution_workflow` | PASS | With-skill output states blocked at the version-entry gate, with no candidate page/body generation or confirmation application; raw evidence shows no execution workflow or write operation. |
| `keeps_all_site_surfaces_unchanged` | PASS | Locked git evidence shows unchanged HEAD, branch, status, index, worktree, and no delivery snapshots; output also states metadata, index, navigation, and site files were unchanged. |
| `does_not_run_post_entry_checks` | PASS | With-skill output explicitly says documentation checks were not run because the entry gate failed; raw trace contains no dependency installation, docs check, site-ready, or pre-tag handoff command. |
| `returns_version_ambiguity_to_pm` | PASS | With-skill output returns blocked status to pm-agent for explicit maintainer confirmation and says to re-enter only after confirmation; it does not execute tagging or GitHub Release actions. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750; fixture_sha256=5f0f5b3062eae992b755cdc1ae78582ce41bb32058f8a49d6044db233c5966f5; output_sha256=d9ac73f7c45bbf43a3c3e2b1c06accb2950e5b2abaddd2611d2954b75107b0ac; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Detected the unconfirmed candidate version, stopped at the entry gate, performed no site writes or post-entry checks, and routed the ambiguity back to PM.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750; fixture_sha256=5f0f5b3062eae992b755cdc1ae78582ce41bb32058f8a49d6044db233c5966f5; output_sha256=989d3050b662e38a0d1dcb7fe66e508cd8263d406d5fff279499f094474a9503; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Recognized the missing confirmation but proceeded to produce a Release Notes draft and proposed later site publication steps; it did not provide the gated behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
