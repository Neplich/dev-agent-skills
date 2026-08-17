# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `spec-based-tester`
- Eval: `eval-001-test-from-spec`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a434f6abe187edb75db35d4f3fb8bb622d73bfabcbaa68935c4416b36759d838` from `agents/qa/test/spec-based-tester/evals/workspace/eval-1-test-from-spec`.
- Identity schema: `2`
- target_skill_sha256: `a902e30cb15a83b00f6e242ec0746a619c9c75741852be4c26efbe1dc710f3e3`
- eval_definition_sha256: `1c095f56ebf8188b170d450f4a4c64b7797467faefd997d04a5961dc178ee24e`
- metadata_sha256: `beabc33b6b3cb3b4fcbdd2cd76be881ee37dbed2c10afbbb6515f52def856618`
- fixture_sha256: `a434f6abe187edb75db35d4f3fb8bb622d73bfabcbaa68935c4416b36759d838`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `af6defb3674eb2b870c7db7cceb8e07b1bc81b7056b91617749018c2cf4bddc5`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `9354357763da0add30a1325fbbb8939ec16a97d466c020a03be8548593c2f944`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `2ae6df1e5892f15e69faa5eb27f67247be532cf172f30b6323b139a66d25acc0`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | Trace shows the with_skill lane read the test spec, same-path PRD/TRD/implementation plan, QA docs, package metadata, and ran the repository command; the delivered report records scope, environment, unknowns, and blockers. |
| `assertion_2` | PASS | Trace and report show TEST_SUITE.md, FLOW_INDEX.md, TC-001, scripts absence, prior results absence, and prior reports absence were checked; the existing TC was reused. |
| `assertion_3` | PASS | The documented repo harness was selected and executed first; the report correctly records browser execution as unavailable because no QA URL or browser script exists. |
| `assertion_4` | PASS | Both locked result.md and the summary report contain requirement matrices with each requirement classified as blocked, with no blocked check misreported as a product failure. |
| `assertion_5` | PASS | Locked reports contain preflight, execution path, requirement matrix, per-item status/evidence/notes, risks, blocked items, and handoff decision sections. |
| `e2e` | PASS | The existing TC is a standalone Markdown file and is referenced by the locked reports; no new or modified E2E TC was delivered, so no new case/script requirement was triggered. |
| `versioned_report_archive` | PASS | Locked artifacts use feature-update and platform version v0.3.0-dev, archive the per-TC result and testcase snapshot under the required versioned results path, and write the summary under the corresponding versioned _reports path. |
| `assertion_7` | PASS | The locked reports explicitly state no bug-analyzer handoff because the harness failed before test execution and no reproducible product failure exists. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9354357763da0add30a1325fbbb8939ec16a97d466c020a03be8548593c2f944; fixture_sha256=a434f6abe187edb75db35d4f3fb8bb622d73bfabcbaa68935c4416b36759d838; output_sha256=cea3cf09e020af314f3ada5e615d914716c1f7279b0f0b1b64d1e420b657b381; snapshot_sha256=f56a4d75c0815cc2073f8943eca9ea998e5cc8a7e3393414a1febd6ace0bc8b2
- Behavior: Correctly selected the narrow repo harness, classified all three behavior checks as blocked, and produced versioned per-TC plus summary reports with structured evidence and no improper handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9354357763da0add30a1325fbbb8939ec16a97d466c020a03be8548593c2f944; fixture_sha256=a434f6abe187edb75db35d4f3fb8bb622d73bfabcbaa68935c4416b36759d838; output_sha256=4081aa3861efd6d3da05eb1163e15b8f7e01f31e8f1dcab1ebe71b4ae3dba116; snapshot_sha256=16fe7dc79baaf118955a967ea85d0f973f4bd6823f54b8412f6f83825623b826
- Behavior: Also detected the missing Vitest dependency and reported the behavior checks as unverified, but produced only a less complete top-level report without the durable per-TC result/archive structure.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Restore the repository test dependencies and rerun npm test -- checkout-discount.
- Next: If needed, provide the configured QA URL and execute the documented browser path.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
