# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-001-verify-bug-fix`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308` from `agents/qa/test/regression-suite/evals/workspace/eval-1-verify-bug-fix`.
- Fixture SHA-256: `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308`
- Prompt SHA-256: `c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `850108c3e4722feb1b9e0417b1554f0fb5b41d47001505d7da16c6bcd9946093`
- Skill overlay SHA-256: `3af177f0dcd9723964fdbcbf144832d8c6b68b267a850af3da918d86fe27d617`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8ca6ea4c46c7a5a2c854d9ff5def7ea0ec612ddbf9888a829e50de270f1b84c4`
- Metadata SHA-256: `732278c998a10f6e6333dc13e2fc4edfbaed96da1abb806d2dc29682a3a79f75`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 报告明确引用 BUG-001 与 PR-001，并以有效登录 500、会话创建和 dashboard 跳转界定原始与修复范围。 |
| `qa` | FAIL | 报告引用了 TEST_SUITE 相关范围和 TC-001，但未提供读取 FLOW_INDEX、case、script 以及历史 results/ 和 _reports/ 的证据。 |
| `assertion_3` | PASS | 报告分别标明 Status: blocked、Original failure recheck: not executed、Expected fixed behavior: not executed，并说明运行验证结果被环境阻塞。 |
| `assertion_4` | PASS | 报告按 feature-update 限定原始成功登录、无效凭据和锁定账户等直接相邻路径，未扩展到 release 全量 E2E。 |
| `alignment_version_archive` | FAIL | 报告确认 PRD、TRD、IMPLEMENTATION_PLAN 均为 Confirmed 且平台版本为 v1.2.0-fix.1，但结果写入 _reports/test-reports-2026-08-08.md，未按要求追加 results/TC-001-login-session/{platform-version}/result.md 和 testcase.snapshot.md。 |
| `assertion_5` | PASS | 报告包含 Release Recommendation，并明确区分 Fix Verification 的 blocked run status 与 low evidence confidence。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=b5c90a74fb86fc96d16b185e8c617b295010d8781f358c81bdf9b7591af7e070; snapshot_sha256=36ea3a4d753d486f29f2cd7fef5bcdf5b064cf55ea5cea92948c12e5025c7063
- Behavior: 完成对齐门禁、定向范围和相邻路径规划，明确 blocked 状态及低证据置信度，但结果归档路径不合规且未证明完整复用 QA 资料。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=b9559ec782e260e1f16c2533e144c630eacf84069027ae94bc31a13da8378071; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到缺少 package.json 和运行环境，结论为 blocked；范围和发布建议较简略。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足完整 QA 用例资料读取证据。
- with_skill 未按规定的 results/{TC}/{platform-version}/result.md 与 testcase.snapshot.md 归档结果。
- Next: 补充完整 QA 资料读取记录，并按规定路径追加 result.md 和 testcase.snapshot.md。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

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
