# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-003-mapped-doc-bug-analysis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf` from `agents/qa/test/bug-analyzer/evals/workspace/eval-3-mapped-doc-bug-analysis`.
- Fixture SHA-256: `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf`
- Prompt SHA-256: `42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27d2fe5d8edb9052289c39964020afb301396abbc970275eb70967d32504d68`
- Skill overlay SHA-256: `bca841768a4850fe9fad50cd3d5afd91b738dda4eaad1293eea1e37d4bad841f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5055f21aa292e91a955bc3aa635c808239336415cf083aba532e9d19a7985220`
- Metadata SHA-256: `6e065f47b93dd01060b700c2c7836503fb5797f7c0c1bb375677811fe6fa6d5f`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | With-skill output identifies the change map, its mapping to notification-retry.md, and the mapped document; it cites no irrelevant site-document traversal. |
| `verifies_against_code` | PASS | It separately states the documentation says 3 retries and retry.rules sets max_retry_attempts = 2, while correctly withholding a definitive code-bug classification pending execution semantics. |
| `treats_unverified_as_low_trust` | PASS | It identifies last_verified_version: unverified and internal/dev metadata, treats the material as an unverified contract, and bases its conclusion on the code/document discrepancy while noting missing tests and runtime evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=6ebaf946f4437e13fe221c0db0e50a5c990eb9032036cfe7a4859d4944fde2f1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identified the mapped documentation, independently compared documentation and code, downgraded unverified material, and limited the conclusion to a documented drift risk.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=634dc76d56960459590fe01c7adab939246ca88e61861e0dcbf123eecd154c86; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identified the mapped documentation, the 2-versus-3 discrepancy, unverified metadata, and missing runtime/test evidence.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

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
