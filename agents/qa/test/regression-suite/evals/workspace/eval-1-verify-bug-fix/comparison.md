# Eval Result: eval-001-verify-bug-fix

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-001-verify-bug-fix`
- Test case: verify-bug-fix
- Workspace: `workspace/eval-1-verify-bug-fix`
- Natural user prompt:

> 验证 Bug #001 的修复，执行回归测试

- Expected artifact: 回归验证报告，明确 original failure recheck、fixed behavior、adjacent regression checks 和 release recommendation

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/regression-suite--eval-001-verify-bug-fix/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `5923f8e6a9744051a7d093120915c47b16783a2f79be9b5e4c4bb0f0959c8c3f`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **PASS**（PASS 6 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: PASS

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>证据复用 | PASS | transcript item_3 读取 bugs/BUG-001.md、fixes/PR-001.md 及 QA 测试材料；item_9 的最终报告复用了原始失败和修复上下文。 | PASS | transcript item_2 读取了 BUG-001、PR-001 及测试文档，并据此说明无法执行回归。 |
| `qa`<br>QA 用例复用 | PASS | transcript item_3 在执行前读取 TEST_SUITE.md、FLOW_INDEX.md、cases/TC-001-login-session.md 和 scripts/TC-001-login-session.spec.md；最终快照确认这些文件均保留。初始 fixture 不存在历史 results/ 或 _reports/，因此无遗漏可读的历史结果。未新增用例，新增用例条件未触发。 | PASS | transcript item_2 读取了 TEST_SUITE、FLOW_INDEX、cases 和 scripts；没有新增用例需求。 |
| `assertion_3`<br>修复验证 | PASS | 最终快照中的 _reports/v1.2.0-fix.1/test-reports-20260807-003518.md 明确记录 Status=blocked、Original failure=not rechecked、Fixed behavior=not verified，并说明 verification evidence 不足。 | FAIL | candidate.md 只笼统说明无法验证，未将 original failure、fixed behavior 和 verification result 逐项明确标为 pass、fail 或 blocked。 |
| `assertion_4`<br>邻近回归 | PASS | TEST_SUITE.md 明确为 feature-update；最终报告只覆盖原始登录失败、直接影响的 invalid-credential 和 locked-account 路径，并明确未扩展到 release 全量 E2E。transcript 未显示执行无关全量测试。 | PASS | transcript item_2 读取了 feature-update 范围；candidate 仅讨论成功登录、无效凭据和锁定账户三条相关路径，未显示扩展到 release 全量 E2E。 |
| `alignment_version_archive`<br>对齐门禁与版本归档 | PASS | transcript item_3 检查并发现同路径 PRD/TRD/IMPLEMENTATION_PLAN 缺失；最终报告显式记录 alignment gate、platform version v1.2.0-fix.1 和下一责任方，并因门禁缺失保持 blocked。file_change trace 显示仅新增 _reports/v1.2.0-fix.1/test-reports-20260807-003518.md；最终快照无 results 覆盖或伪造归档。 | FAIL | transcript 和最终快照均未检查或引用同路径 PRD/TRD/IMPLEMENTATION_PLAN，也未生成要求的版本化回归归档。 |
| `assertion_5`<br>发布建议 | PASS | 最终报告包含 Release Recommendation=Hold release / do not close BUG-001，并在 Fix Verification 中分别记录 Status=blocked 与 Evidence confidence=low。 | FAIL | candidate.md 没有 release recommendation，也没有将 run status 与 evidence confidence 分开记录。 |

## With-Skill Behavior

with_skill 按要求读取并复用 Bug、修复说明及 QA 用例；发现 PRD/TRD/IMPLEMENTATION_PLAN、源码和测试环境缺失后，将原始失败、修复行为及邻近路径明确标为 blocked，并生成带版本归档的回归报告。

## Fresh Without-Skill Baseline

without_skill 执行了 npm 命令并识别 package.json 缺失，但未完成对齐门禁、结构化回归报告或版本归档。两条 lane 的初始 fixture 文件内容及 SHA-256 完全一致；with_skill 仅新增了 _reports 回归报告。

## Failures

- 无。

## Not Exercised

- 无。

## Next Steps

- 补齐同路径 PRD、TRD 和已确认的 IMPLEMENTATION_PLAN.md。
- 提供源码、package.json、可运行测试 harness 或 QA_BASE_URL。
- 重新执行 original failure、fixed behavior、invalid-credential 和 locked-account 检查，并追加对应版本结果。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
