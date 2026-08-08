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
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9bc7bc56a69ed03539b92f8b1b5ab784d65f1b99345268b0e2860387a93c400f`
- Skill overlay SHA-256: `5682fc1ffcb4eb879c1789588b290db4ff6dc8f83dc85473fb6c12c8ad0ebd72`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `1c095f56ebf8188b170d450f4a4c64b7797467faefd997d04a5961dc178ee24e`
- Metadata SHA-256: `beabc33b6b3cb3b4fcbdd2cd76be881ee37dbed2c10afbbb6515f52def856618`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With-skill report records scope, feature-update scenario, platform version, source documents, repository command, environment assumptions, and blocked checks. |
| `assertion_2` | PASS | It reads and reuses TEST_SUITE.md, FLOW_INDEX.md, and TC-001; it records scripts and prior results as absent. |
| `assertion_3` | PASS | It selected and attempted the documented repo harness before any browser fallback. |
| `assertion_4` | PASS | The requirement matrix marks each acceptance item blocked and distinguishes the runner prerequisite issue from product failure. |
| `assertion_5` | PASS | The report contains a requirement matrix, execution details, evidence references, blocked-item/risk notes, and per-requirement status. |
| `e2e` | PASS | No new or supplemented E2E case was created; the existing TC-001 file was reused and referenced in the report. |
| `versioned_report_archive` | FAIL | Scenario and platform version are recorded, and a snapshot plus versioned result are present, but the result is timestamp-named rather than the required result.md path. |
| `assertion_7` | PASS | No bug handoff was made because the only observed issue was an unreproducible test-runner blockage, not a confirmed product failure. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9354357763da0add30a1325fbbb8939ec16a97d466c020a03be8548593c2f944; fixture_sha256=a434f6abe187edb75db35d4f3fb8bb622d73bfabcbaa68935c4416b36759d838; output_sha256=15a18d6e003f33a8427044dbc74af4954476d47047f3dcc71ee1379f30c7d811; snapshot_sha256=38d0210e0bda18a3b9baf04cac88ea234cbc2859d5e0330aa204376a7dc042cd
- Behavior: Read the prescribed documentation and reused TC-001, selected the repo harness, recorded blocked statuses with traceable versioned artifacts, and avoided filing a product defect.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9354357763da0add30a1325fbbb8939ec16a97d466c020a03be8548593c2f944; fixture_sha256=a434f6abe187edb75db35d4f3fb8bb622d73bfabcbaa68935c4416b36759d838; output_sha256=e90b4d646d2f1531f9e297e96161cc8c5134c758463d7d9e8bd260459b8906ed; snapshot_sha256=12c805b0b490f62c9b99eb67de74621f4d407032b050cacffcee155b8ec47eda
- Behavior: Ran the same test command and reported blocked execution, but produced a less complete report outside the feature QA archive path.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- versioned_report_archive is not fully satisfied because the archived execution result is timestamp-named instead of result.md.
- Next: Append or rename the per-TC execution artifact to results/TC-001-discount-code/v0.3.0-dev/result.md while retaining testcase.snapshot.md and the feature-update summary report.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Eval Result: eval-001-test-from-spec

## Evaluation Target

- Agent: `qa`
- Skill: `spec-based-tester`
- Eval: `eval-001-test-from-spec`
- Test case: test-from-spec
- Workspace: `workspace/eval-1-test-from-spec`
- Natural user prompt:

> 根据 docs/test-spec.md 执行规范测试

- Expected artifact: 测试报告，包含通过/失败统计和失败用例详情

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/spec-based-tester--eval-001-test-from-spec/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `7ef446892bf23cfc8a5ca77968d6cec1ebd365f5c1e597cc19bb69332686e105`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **FAIL**（PASS 6 / FAIL 1 / NOT EXERCISED 1）
- Coverage result: **PARTIAL**
Overall result: FAIL

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>上下文基线 | PASS | transcript item_4 在执行 item_5 前读取了 test-spec、prd、trd、QA 用例和测试命令；报告记录了范围、环境、未知项和阻塞项。 | FAIL | transcript item_2 未读取 prd/trd，item_5 执行测试后才在 item_5 补读；执行前也没有完整记录范围、环境假设和阻塞检查。 |
| `assertion_2`<br>独立用例复用 | PASS | transcript item_4 在执行前读取 TEST_SUITE.md、FLOW_INDEX.md、cases/TC-001；item_2/item_7 证实 scripts、历史 results 不存在，且报告明确复用已有 TC。 | FAIL | 执行前仅读取 suite、flow、case；scripts 和历史 results 的检查在测试执行后的 item_7，且未形成完整 QA memory 记录。 |
| `assertion_3`<br>执行路径选择 | PASS | transcript item_5 实际执行了仓库规定的最窄命令 npm test -- checkout-discount；vitest 缺失后未虚构浏览器或 Playwright 路径，报告记录 QA_BASE_URL 缺失。 | PASS | transcript item_4 实际执行了 TEST_SUITE/TRD 指定的 npm test -- checkout-discount，并确认浏览器路径缺少 QA_BASE_URL。 |
| `assertion_4`<br>结果分级 | PASS | 快照中的报告 requirement matrix 将三个需求项均标为 blocked，并区分了执行阻塞与产品失败。 | FAIL | candidate 只称三项“未验证”，没有 requirement matrix，也没有逐项标记 pass/fail/blocked/assumed。 |
| `assertion_5`<br>结构化证据 | PASS | 快照中的 _reports/v0.3.0-dev/test-reports-20260807-003634.md 包含 requirement matrix、execution path、逐项 evidence/status/notes 和 risks/handoff。 | FAIL | without_skill 快照没有报告文件；candidate 也没有 requirement matrix、evidence references 或 risk notes 的结构化报告。 |
| `e2e`<br>E2E 单文件约束 | NOT EXERCISED | 已有 TC-001-discount-code，transcript 与报告均表明是复用既有用例；没有新增或补充 E2E TC 的触发条件。 | NOT EXERCISED | 同样只有既有 TC，未新增或补充 E2E TC。 |
| `versioned_report_archive`<br>版本结果与汇总报告 | FAIL | 虽在 transcript item_4/报告中确认 feature-update 与 v0.3.0-dev，并在快照写入了 _reports/.../test-reports-20260807-003634.md，但最终树缺少 results/TC-001-discount-code/v0.3.0-dev/result.md 和 testcase.snapshot.md。 | FAIL | without_skill 快照没有 _reports、results 或 testcase.snapshot.md；candidate 明确称没有生成报告。 |
| `assertion_7`<br>交接边界 | PASS | 测试被 vitest: command not found 阻断，没有 hand off 给 bug-analyzer；报告将其作为 blocked/risk 而非 confirmed failure。 | PASS | 同样没有将环境阻塞升级为 bug-analyzer handoff 或确认产品缺陷。 |

## With-Skill Behavior

with_skill 正确完成大部分预检、路径选择和结构化报告，但缺少 results/TC-001-discount-code/v0.3.0-dev/result.md 与 testcase.snapshot.md，导致版本化归档断言失败。

## Fresh Without-Skill Baseline

without_skill 仅成功执行了测试命令并确认 vitest 缺失；预检顺序、结构化报告和归档均不完整，作为 baseline 对照。

## Failures

- with_skill 的 versioned_report_archive 失败：缺少按 TC/平台版本归档的 result.md 与 testcase.snapshot.md。
- without_skill 的 assertion_1、assertion_2、assertion_4、assertion_5、versioned_report_archive 失败。

## Not Exercised

- e2e：没有新增或补充 E2E TC，因此单文件约束未触发。

## Next Steps

- 补写并落盘 docs/qa/e2e/commerce/checkout/discount-code/results/TC-001-discount-code/v0.3.0-dev/result.md 与 testcase.snapshot.md；依赖恢复后重新执行并追加结果。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
