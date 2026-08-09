# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-009-prd-iteration-split-proposal`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997` from `agents/product_manager/test/idea-to-spec/workspace/eval-009-prd-iteration-split-proposal`.
- Fixture SHA-256: `cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997`
- Prompt SHA-256: `ae03344941a8a5473fce84f07af68d8bb42c4c4dd8dbaf557b909886adf20c98`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c0da2e0366232678672d0c64ce9fa764d3b78f3caaaa8493348af1a7e1cd00fe`
- Skill overlay SHA-256: `8f09b52303d9393824dd3e732e656dd74f7ac606a082939547181274986dfb2d`
- Judge schema SHA-256: `9c9a733fc3c46fd3cb1cdea794218e66a7a987137063c1a3c970e8e9386d1a58`
- Eval definition SHA-256: `8ef466ccd13d937453c02f105817ced47839fb573011ea1ee300be62facb6b71`
- Metadata SHA-256: `ae189abbce9ec160b22d49ab4f79a0a7a8f521d1a6e2046930669caf75d7dab0`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `applies_requested_change` | PASS | Locked PRD snapshot changes FR-02 and the Delivery Strategy from polling to event-driven delivery, with version 1.4.0. |
| `detects_l2b_signals` | FAIL | The fixture contains three independent domains and 18 US/FR table rows, but the with_skill output and delivered PRD do not explicitly identify an L2b signal. |
| `presents_split_proposal` | FAIL | The with_skill output provides no feature_path tree, chapter migration mapping, or downstream mirror impact list. |
| `waits_for_confirmation` | NOT_EXERCISED | No split was attempted and no confirmation interaction occurred, so the confirmation gate was not exercised. |
| `rejection_keeps_current_flow` | NOT_EXERCISED | No proposal rejection occurred, so rejected-proposal continuation behavior was not exercised. |
| `body_consolidation` | FAIL | The delivered PRD directly states event-driven delivery, but it also retains a polling description under “Change From Current Behavior,” so the body is not fully consolidated to the target state. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ae03344941a8a5473fce84f07af68d8bb42c4c4dd8dbaf557b909886adf20c98; fixture_sha256=cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997; output_sha256=3d324510e7092bbf060302a56654252fa94c19e90a1345d2c4f91a89163f40d7; snapshot_sha256=d6bad58a25f176396976083250b18525d79c1a5b8a79d0443c8d724216dbfcbc
- Behavior: Applied the polling-to-event-driven PRD update, but omitted L2b split analysis and retained legacy polling details.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ae03344941a8a5473fce84f07af68d8bb42c4c4dd8dbaf557b909886adf20c98; fixture_sha256=cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997; output_sha256=c5b9a044e5714fc28d260f88a3487278dbedbe7d7748f46e6081afeced92724f; snapshot_sha256=cefdfef59d5967024142b4f6a87bd3043c66a0d159433eafafb2e48b0823f555
- Behavior: Applied the requested PRD update with a more complete event-driven rewrite and no split workflow evidence.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane omitted explicit L2b detection and the required split proposal.
- The delivered PRD retained polling details in a current-behavior section, contrary to full body consolidation.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
