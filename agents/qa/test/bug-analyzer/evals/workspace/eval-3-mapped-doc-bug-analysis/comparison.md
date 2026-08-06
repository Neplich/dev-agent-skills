# Eval Result: eval-003-mapped-doc-bug-analysis

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-003-mapped-doc-bug-analysis`
- Test case: mapped-doc-bug-analysis
- Workspace: `workspace/eval-3-mapped-doc-bug-analysis`
- Natural user prompt:

> 分析 src/notifications/retry.rules 中通知重试次数可能与预期不一致的问题，形成证据化缺陷分析。

- Expected artifact: 区分文档声明与代码事实的缺陷分析，并说明证据置信度和影响。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/bug-analyzer--eval-003-mapped-doc-bug-analysis/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `86705991ace13eac6c0d350b99408298f65b0e28353532852c7102d1e8b2d9b9`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **FAIL**（PASS 2 / FAIL 1 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `reads_mapped_docs_first`<br>从映射文档获取缺陷上下文 | FAIL | transcript 中首次探索命令先执行全库 rg --files；随后 item_3 的读取顺序也是 retry.rules、notification-retry.md、change-map.yaml，未在命中 change-map 后先读取 docs/site/api/notification-retry.md，且存在对无关文件的全库枚举。 | FAIL | transcript 先读取 retry.rules，并执行全库 rg --files/引用搜索；没有先读取 change-map 再精准读取 notification-retry.md。 |
| `verifies_against_code`<br>缺陷判断回到代码证据 | PASS | transcript item_3 读取 retry.rules、notification-retry.md 和 change-map.yaml；最终快照中 retry.rules 为 max_retry_attempts = 2，文档第 13 行声明最多重试 3 次。缺陷文档明确区分文档声明、代码事实，并说明缺少消费者实现时只能判为疑似。 | PASS | transcript item_1、item_3 读取代码和文档；candidate 明确记录代码值 2、文档值 3，并分别讨论 retries/total attempts 两种语义及其对缺陷结论的影响。 |
| `treats_unverified_as_low_trust`<br>降低未核证文档的证据权重 | PASS | 最终快照中的缺陷文档第 19 行识别 notification-retry.md 与 change-map.yaml 的 last_verified_version: unverified，并将报告分类为 suspected / needs more evidence；第 7、41、47-52 行以代码冲突为依据，同时明确要求消费者、批准的产品预期和运行时/单元测试来确认。 | FAIL | transcript 虽读取到文档中的 unverified 字段，但 candidate 未识别其为最低信任线索，且没有明确置信度；结论主要基于文档与配置冲突，未按该断言要求处理 unverified 状态。 |

## With-Skill Behavior

with_skill 成功核对代码、映射文档和未核证状态，并在最终快照中创建了缺陷文档；但读取顺序未满足 mapped docs first，因此有一条已触发断言失败。

## Fresh Without-Skill Baseline

without_skill 识别了代码与文档的数值冲突并讨论了字段语义不确定性，但未将 unverified 作为最低信任线索，也未明确置信度。

## Failures

- with_skill 的 reads_mapped_docs_first 已触发但失败：读取顺序和探索范围不符合要求。
- without_skill 的 treats_unverified_as_low_trust 已触发但失败；baseline 结果不改变 with_skill 的最终判定。

## Not Exercised

- 无。

## Next Steps

- 修正 with_skill 的探索顺序：先读取 change-map.yaml，确认映射后立即读取 docs/site/api/notification-retry.md，再回到代码验证，并避免无关全库遍历。
- 在分析中明确写出 unverified 仅为最低信任线索，并给出独立的证据置信度。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
