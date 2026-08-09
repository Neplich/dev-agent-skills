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
- Fixture SHA-256: `a434f6abe187edb75db35d4f3fb8bb622d73bfabcbaa68935c4416b36759d838`
- Prompt SHA-256: `9354357763da0add30a1325fbbb8939ec16a97d466c020a03be8548593c2f944`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8ceb46669357c2ad2e3984067ae0ce5c97b019da23d3a0f850d2bedd7e38ab17`
- Skill overlay SHA-256: `fda3e87e887ba889a897540771dbb1fdc6d424a530b084850bba0cba716a1567`
- Judge schema SHA-256: `af6defb3674eb2b870c7db7cceb8e07b1bc81b7056b91617749018c2cf4bddc5`
- Eval definition SHA-256: `1c095f56ebf8188b170d450f4a4c64b7797467faefd997d04a5961dc178ee24e`
- Metadata SHA-256: `beabc33b6b3cb3b4fcbdd2cd76be881ee37dbed2c10afbbb6515f52def856618`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | NOT_EXERCISED | The report records scope, environment, unknowns, and blockers, but locked evidence cannot prove the required read-before-execution order. |
| `assertion_2` | NOT_EXERCISED | The report claims same-path QA materials were read and TC-001 reused, but locked evidence cannot prove the required read order. |
| `assertion_3` | PASS | The candidate selected the documented repository harness and recorded why browser fallback was unavailable. |
| `assertion_4` | PASS | The report requirement matrix explicitly marks each acceptance item blocked and does not classify the environment blocker as a product failure. |
| `assertion_5` | PASS | The archived report contains a requirement matrix with statuses and notes, execution path, evidence references, and risk notes. |
| `e2e` | NOT_EXERCISED | No new or supplemented E2E test case was delivered; the existing TC-001 was reused, so the file-creation constraint was not exercised. |
| `versioned_report_archive` | PASS | The report confirms the feature-update scenario and v0.3.0-dev, and locked snapshots show the required versioned result and testcase files plus the _reports summary path. |
| `assertion_7` | PASS | The report records no confirmed product failure and explicitly declines bug-analyzer handoff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9354357763da0add30a1325fbbb8939ec16a97d466c020a03be8548593c2f944; fixture_sha256=a434f6abe187edb75db35d4f3fb8bb622d73bfabcbaa68935c4416b36759d838; output_sha256=b5066f25455614047b4e8f36ad083b6ca992ddbb00f55b44c61bacf27c2be409; snapshot_sha256=1493d479f410aef828214d9a15891197f51347aedcab554054c6a45957cc5771
- Behavior: Produced a structured, versioned blocked QA report with requirement statuses, evidence, risks, and no unsupported product failure.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9354357763da0add30a1325fbbb8939ec16a97d466c020a03be8548593c2f944; fixture_sha256=a434f6abe187edb75db35d4f3fb8bb622d73bfabcbaa68935c4416b36759d838; output_sha256=1341d0d7465a7ad41927a16a03045fdc10842f587d5b3d8eb461ca69fbaba77b; snapshot_sha256=e698292ff0fb8d5a2bb455d5b3edeb0b35517edd258b98eb17e0c0fc5bece32b
- Behavior: Produced a blocked report with a missing-Vitest diagnosis, but without the required same-path versioned result artifacts and comparable structured QA detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Restore dependencies and implementation/test sources, then rerun TC-001 on v0.3.0-dev.
- Next: If the repository harness remains unavailable, provide a QA application URL and execute the documented browser fallback.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
