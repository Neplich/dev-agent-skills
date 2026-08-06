# Eval Result: eval-002-blocked-without-original-bug-context

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-002-blocked-without-original-bug-context`
- Test case: blocked-without-original-bug-context
- Workspace: `workspace/eval-2-blocked-without-original-bug-context`
- Natural user prompt:

> 复测上周修过的支付按钮问题，但仓库里找不到原始 bug 报告、失败证据、修复 PR 或可用测试环境。请给出回归验证结论。

- Expected artifact: blocked 回归验证报告，说明缺失上下文、无法复核 original failure、不能给 release ready 结论，并列出恢复验证所需证据

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/regression-suite--eval-002-blocked-without-original-bug-context/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `fcb18ed7faddb7313fd51c13f012a7fe051e13a2f764566630a63d003a998d9a`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **FAIL**（PASS 1 / FAIL 4 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>原始证据缺失 | PASS | candidate.md 明确写出缺少 bug 报告、失败证据、修复 PR、变更说明、测试命令和测试环境；transcript 中仅执行了读取/探索命令，最终快照也只有 notes/missing-context.md，因此没有直接执行泛化回归的证据。 | PASS | candidate.md 明确列出缺少原始 Bug 报告、失败证据、修复 PR、测试命令和测试环境；transcript 仅有只读探索命令，快照无测试产物。 |
| `blocked`<br>blocked 状态 | FAIL | 原始失败、修复验证和邻近回归被描述为无法复现/未执行，且 PRD/TRD 对齐不可用；但没有明确标记 platform version confirmation 为 blocked 或 not executed，也未完整逐项给出 fixed behavior、adjacent regression checks 和对齐状态。 | FAIL | 虽然说明无法复测并列出缺失证据，但没有逐项标记 fixed behavior、adjacent regression checks、平台版本确认及 PRD/TRD 对齐为 blocked/not executed；transcript 也只有失败的 git 检查和文件读取。 |
| `assertion_3`<br>结构化输出 | FAIL | candidate.md 使用了语义近似的“原始失败/修复验证/邻近回归/发布建议”，但缺少必需的 evidence confidence 字段，且未完整按 original failure recheck、fixed behavior、adjacent regression checks 等结构化字段输出。 | FAIL | candidate.md 未包含完整的 original failure recheck、fixed behavior、adjacent regression checks、release recommendation 和 evidence confidence 五项结构化输出。 |
| `assertion_4`<br>发布边界 | FAIL | “暂缓放行”语义上表示不放行，但断言规定 release recommendation 必须是 needs more verification 或 blocked；输出没有使用规定取值。 | FAIL | candidate.md 没有 release recommendation 字段，也没有明确给出 needs more verification 或 blocked 作为发布建议。 |
| `no_unknown_or_unscoped_release`<br>不得用 unknown 或误判发版范围 | FAIL | 最终快照没有 unknown 目录或 release 全量测试产物，transcript 也无写入证据；但恢复清单虽包含原始 bug、失败证据、修复 PR、测试环境和执行入口，未明确列出缺失的测试平台版本，因此未满足“版本、环境、原始 bug 和修复证据”完整清单要求。 | FAIL | 最终快照没有 unknown 目录或 release 全量测试产物，transcript 无写入证据；但候选未明确列出测试平台版本，恢复验证所需证据清单不完整。 |

## With-Skill Behavior

with_skill 正确识别上下文缺失并阻塞回归，但未完整满足结构化字段、平台版本状态和规定的 release recommendation 取值要求。最终快照仅有 notes/missing-context.md，且 transcript 仅显示读取命令，无写入或测试执行证据。

## Fresh Without-Skill Baseline

without_skill 同样识别了缺失上下文，但缺少更多必需的结构化状态与发布建议字段；仅作为 baseline 对照，不影响当前结果。两条 lane 的最终快照树、文件内容、SHA-256 和大小均一致，符合 fixture-manifest。

## Failures

- with_skill 的 blocked 断言未明确覆盖 platform version confirmation，且未逐项完整标记所有要求的检查状态。
- with_skill 缺少 evidence confidence，结构化输出字段不完整。
- with_skill 使用“暂缓放行”而非规定的 needs more verification 或 blocked。
- 两条 lane 均未在恢复验证清单中明确列出平台版本。

## Not Exercised

- 无。

## Next Steps

- 补充逐项结构化状态：original failure recheck、fixed behavior、adjacent regression checks、platform version confirmation、PRD/TRD alignment，均标为 blocked 或 not executed。
- 增加 evidence confidence 及简短依据。
- 将 release recommendation 明确写为 blocked 或 needs more verification，并列出平台版本、测试环境、原始 bug/失败证据、修复 PR/提交及预期行为。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
