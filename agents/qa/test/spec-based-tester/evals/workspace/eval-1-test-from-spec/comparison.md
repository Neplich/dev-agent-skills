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
- target_skill_sha256: `14753ae64e96384b284b9c0b0f3a08e0639fc554929720623cd02fae3a9c29a0`
- eval_definition_sha256: `1c095f56ebf8188b170d450f4a4c64b7797467faefd997d04a5961dc178ee24e`
- metadata_sha256: `beabc33b6b3cb3b4fcbdd2cd76be881ee37dbed2c10afbbb6515f52def856618`
- fixture_sha256: `a434f6abe187edb75db35d4f3fb8bb622d73bfabcbaa68935c4416b36759d838`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `af6defb3674eb2b870c7db7cceb8e07b1bc81b7056b91617749018c2cf4bddc5`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `9354357763da0add30a1325fbbb8939ec16a97d466c020a03be8548593c2f944`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6cb100241ab8151af36dbd15ed1bd54941ad005e84cbff29ba2242c5550d11ef`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | Raw trace shows the test spec, same-path PRD/TRD/implementation plan, QA documents, and package.json were read before execution; the report records scope, environment, platform, unknowns, and blocked checks. |
| `assertion_2` | PASS | The trace enumerates the function-tree QA directory and reads TEST_SUITE.md, FLOW_INDEX.md, and the existing TC; the report records absent scripts/history and explicitly reuses TC-001 without broad project rediscovery. |
| `assertion_3` | PASS | The documented repo harness `npm test -- checkout-discount` was selected and attempted; browser or Playwright fallback was not used because the harness was preferred and no usable application URL or alternate script existed. |
| `assertion_4` | PASS | The per-TC requirement matrix marks all three checks `blocked` due to `vitest: command not found`, with no blocked check misclassified as a product failure. |
| `assertion_5` | PASS | The delivered result and summary files contain a requirement matrix with status and notes, execution path, evidence references, blocked items, risk notes, and handoff decision. |
| `e2e` | PASS | The existing TC-001 is a separate Markdown case file and is referenced by the delivered result and summary; no new TC was created requiring an additional case/script pair. |
| `versioned_report_archive` | PASS | The delivered artifacts confirm `feature-update` and `v0.3.0-dev` before execution, and include the required per-TC result.md, testcase.snapshot.md, and feature-update _reports summary paths. |
| `assertion_7` | PASS | The report records no confirmed failures and explicitly declines bug-analyzer handoff because the only observed issue is the reproducible environment prerequisite blocker. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9354357763da0add30a1325fbbb8939ec16a97d466c020a03be8548593c2f944; fixture_sha256=a434f6abe187edb75db35d4f3fb8bb622d73bfabcbaa68935c4416b36759d838; output_sha256=ce7daaea461d66e74a830265d9b8c6670378d6f10cb09b7f3b5f9a9a7ca4f12c; snapshot_sha256=b433ef311d74d08b52225a6f2c3fa4e4cab9dc16c2be599e762bfd164e3eba23
- Behavior: Selected the narrow documented harness, accurately classified all checks as blocked, and produced complete versioned QA artifacts without an unsupported bug handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9354357763da0add30a1325fbbb8939ec16a97d466c020a03be8548593c2f944; fixture_sha256=a434f6abe187edb75db35d4f3fb8bb622d73bfabcbaa68935c4416b36759d838; output_sha256=c25ef40534ac53d30e518a1cedcfaf6b2bda99285fd992296611ca8f299748ff; snapshot_sha256=f1b5d1a79edb30d29f87977d7c5c2315f53ccc44ca99538a835ed1416dd6ea6c
- Behavior: Fresh baseline also encountered the missing vitest dependency and produced a simpler root-level report, without the with_skill lane's per-TC result, snapshot, and structured QA report coverage.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Restore the repository test dependency or provide the configured QA harness, then rerun TC-001 on v0.3.0-dev.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
