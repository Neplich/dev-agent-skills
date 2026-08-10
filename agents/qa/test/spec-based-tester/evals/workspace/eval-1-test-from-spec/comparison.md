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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8ceb46669357c2ad2e3984067ae0ce5c97b019da23d3a0f850d2bedd7e38ab17`
- Skill overlay SHA-256: `5754523ab6dc67a27703c13629b577962774677f13b55627e2b1a056ffc0bc71`
- Judge schema SHA-256: `af6defb3674eb2b870c7db7cceb8e07b1bc81b7056b91617749018c2cf4bddc5`
- Eval definition SHA-256: `1c095f56ebf8188b170d450f4a4c64b7797467faefd997d04a5961dc178ee24e`
- Metadata SHA-256: `beabc33b6b3cb3b4fcbdd2cd76be881ee37dbed2c10afbbb6515f52def856618`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 原始 trace 显示读取测试规格、同路径 PRD/TRD/IMPLEMENTATION_PLAN、仓库状态、测试命令和变更上下文；交付报告记录范围、环境、未知项及 vitest/应用 URL 阻塞。 |
| `assertion_2` | PASS | trace 显示先检查并复用现有 QA function-tree 的 TEST_SUITE.md、FLOW_INDEX.md 和 TC-001；scripts、历史 results 和 reports 均核实为不存在，未回退到旧目录或进行无界项目探索。 |
| `assertion_3` | PASS | 依据 TEST_SUITE/TRD 选择最窄的 repo harness `npm test -- checkout-discount`；在 harness 因 vitest 缺失阻塞后，报告记录无应用 URL，未无依据切换浏览器或 Playwright。 |
| `assertion_4` | PASS | 交付的 result.md 和汇总报告均包含 requirement matrix，并将三个需求明确标为 blocked；同时明确无 confirmed failures，未将阻塞误报为缺陷。 |
| `assertion_5` | PASS | 锁定的 result.md 包含 preflight、execution path、requirement matrix、evidence、blocked items、risk notes、handoff decision；每个需求均有 status、evidence 和 notes。 |
| `e2e` | PASS | 复用的是已有的 `cases/TC-001-discount-code.md`，没有新增或补充 TC；报告引用该 case，且锁定快照保留其内容。该要求在本次运行中满足且无新增 TC 需要创建脚本。 |
| `versioned_report_archive` | PASS | 汇总报告确认 `feature-update` 与平台版本 `v0.3.0-dev`；锁定交付包含 `results/TC-001-discount-code/v0.3.0-dev/result.md`、`testcase.snapshot.md` 及对应 `_reports/v0.3.0-dev/test-reports-2026-08-10T16-10-55.md`，并符合已读取的 e2e-test-report reference。 |
| `assertion_7` | PASS | 锁定报告明确没有可复现的产品失败，Handoff decision 为阻塞后交回执行环境/Engineer，不转交 bug-analyzer。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9354357763da0add30a1325fbbb8939ec16a97d466c020a03be8548593c2f944; fixture_sha256=a434f6abe187edb75db35d4f3fb8bb622d73bfabcbaa68935c4416b36759d838; output_sha256=14911e204d9fd40aa489e90f82a344a2c0d429678ddf02e12157bd0762e15653; snapshot_sha256=a8ecaee2bae49925bd865e5be1b7a180088d4c79f09f16d0643a92535d6cfd3f
- Behavior: 准确完成基线、路径选择、阻塞分类和版本化 QA 归档；未声称三个折扣行为已验证。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9354357763da0add30a1325fbbb8939ec16a97d466c020a03be8548593c2f944; fixture_sha256=a434f6abe187edb75db35d4f3fb8bb622d73bfabcbaa68935c4416b36759d838; output_sha256=3f1e57934dc1d8c6df9275a7b69f4c652d8bdd3c25d7cebbe0a804b0782217d8; snapshot_sha256=e6168554993ab7a11c71d9052ee3424d8cef4cab11e19297fe3746df3be23d9b
- Behavior: 识别测试入口和 vitest 阻塞，但仅生成简单报告，未形成完整的 QA function-tree 结果、快照和结构化证据链。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 恢复 Node 测试依赖后重新执行 TC-001；若仍不可用，提供 QA 应用 URL 后执行同一三项检查。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
