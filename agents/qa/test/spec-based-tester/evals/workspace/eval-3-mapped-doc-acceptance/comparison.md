# Eval Result: eval-003-mapped-doc-acceptance

## Evaluation Target

- Agent: `qa`
- Skill: `spec-based-tester`
- Eval: `eval-003-mapped-doc-acceptance`
- Test case: mapped-doc-acceptance
- Workspace: `workspace/eval-3-mapped-doc-acceptance`
- Natural user prompt:

> 请对 src/profile/validation.rules 中的昵称长度规则执行规范验收，给出需求矩阵和证据结论。

- Expected artifact: 基于映射文档定位、以代码事实核证的规范验收报告，并明确记录文档与代码的分歧。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/spec-based-tester--eval-003-mapped-doc-acceptance/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `d1727ff5d50443ad4c264da470cb603d79901dea16aa93d2189a0984f3434bd8`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **PASS**（PASS 3 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: PASS

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `reads_mapped_docs_first`<br>优先读取 change-map 命中的正式文档 | PASS | transcript item_2 的命令顺序为读取 change-map.yaml、profile-validation.md，再读取 validation.rules；快照仅含相关 fixture 与生成报告，没有遍历无关文档。 | FAIL | transcript item_2 先读取 validation.rules 和 API 文档，item_3 才读取 change-map.yaml，未满足 mapped docs first。 |
| `verifies_against_code`<br>用代码证据核证文档声明 | PASS | transcript item_2 读取代码；快照中的 validation.rules 明确为 nickname_max_length = 64，API 文档明确为 at most 80 characters；candidate.md 和生成的 spec-validation.md 均记录了文档路径、声明、代码事实及 65–80 字符欠接受影响。 | PASS | transcript item_2 读取代码和文档；candidate.md 明确记录文档要求 80、代码为 64、存在 65–80 字符不一致及验收影响。 |
| `treats_unverified_as_low_trust`<br>未核证文档按最低信任处理 | PASS | 两份映射文档快照均含 last_verified_version: unverified；transcript item_3 与生成报告将运行时检查列为未执行，并指出缺少 PRD/TRD/实现计划、无法确认权威边界，关键不一致结论回到代码与静态证据核证。 | FAIL | 虽然读取并提及 unverified，但 candidate.md 直接将文档作为规范基线，未明确按低信任定位线索处理，也未充分记录权威性不确定性。 |

## With-Skill Behavior

with_skill 三条断言均有 transcript 与最终快照证据支持。按 change-map → API 文档 → 代码顺序核验，并确认文档标记为 unverified、代码实际为 64、文档声明为 80。

## Fresh Without-Skill Baseline

without_skill 作为 baseline：未先读取 change-map，先读取代码和 API 文档；但能识别 64/80 分歧并记录影响。

## Failures

- 无。

## Not Exercised

- 无。

## Next Steps

- 如需运行时覆盖，应补充 64、65、80、81 字符边界测试，并先确认 64 或 80 的权威需求。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
