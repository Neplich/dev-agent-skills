# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-002-thin-evidence-suspected-bug`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266` from `agents/qa/test/bug-analyzer/evals/workspace/eval-2-thin-evidence-suspected-bug`.
- Fixture SHA-256: `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266`
- Prompt SHA-256: `78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27d2fe5d8edb9052289c39964020afb301396abbc970275eb70967d32504d68`
- Skill overlay SHA-256: `bca841768a4850fe9fad50cd3d5afd91b738dda4eaad1293eea1e37d4bad841f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ee85b4030fea85acc8c079589b9268be5087962ef495cf3e3194580abf721432`
- Metadata SHA-256: `8fd7c615ab5c3a7f7edc961336d40be79c05d55d0c11dd967998bbb2abd4e9d7`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_status_unconfirmed` | PASS | With-skill output explicitly keeps the report as an unconfirmed investigation item and says not to treat it as a confirmed defect; it does not claim reproducibility or environment sensitivity. |
| `separates_impact_from_confidence` | FAIL | It describes weak evidence and uncertainty, but does not separately state the potential user impact or distinguish impact from confidence. |
| `requests_decisive_evidence` | FAIL | It requests reproduction details, expected/actual results, environment, screenshots/recordings, network responses, and logs, but omits product/app version. |
| `avoids_confirmed_bug_write` | PASS | It recommends an unconfirmed engineering investigation item and explicitly says not to treat it as a confirmed defect; no GitHub issue or confirmed bug is created. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=8cf410eb0e8561fa7fa0f6433c38a43b6fe8a0b86dc9fe602e37a6f48faddadb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Keeps the report unconfirmed and proposes an investigation workflow, but does not explicitly separate potential impact from confidence and omits product version from the evidence plan.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=1f4585bfa6f04c070038ce93cf41f408949471c74916d81db10c2cfd33386f64; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline correctly keeps the report unconfirmed and requests substantial follow-up evidence, including product version and impact-related details.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output does not explicitly distinguish potential user impact from evidence confidence.
- The with-skill evidence plan omits product/app version.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-002-thin-evidence-suspected-bug`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266` from `agents/qa/test/bug-analyzer/evals/workspace/eval-2-thin-evidence-suspected-bug`.
- Fixture SHA-256: `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266`
- Prompt SHA-256: `78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27d2fe5d8edb9052289c39964020afb301396abbc970275eb70967d32504d68`
- Skill overlay SHA-256: `bca841768a4850fe9fad50cd3d5afd91b738dda4eaad1293eea1e37d4bad841f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ee85b4030fea85acc8c079589b9268be5087962ef495cf3e3194580abf721432`
- Metadata SHA-256: `8fd7c615ab5c3a7f7edc961336d40be79c05d55d0c11dd967998bbb2abd4e9d7`
- Executor SHA-256: `c5ece8c6632badb84ff79ee67e4bea96a1d1db7e8afd66de87486af43e8fdd16`
- Runtime SHA-256: `5c4532cfa9ada91c16b3ae2d69922296ddc7c2c1c61841e01bc9c804be1b85fe`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_status_unconfirmed` | PASS | 明确保持为“待核实的问题线索”和“待复现/未确认缺陷”，未声称已确认或可复现。 |
| `separates_impact_from_confidence` | PASS | 说明当前证据不足以确认，并区分“保存失败”与“保存成功但界面无反馈”两种潜在影响。 |
| `requests_decisive_evidence` | FAIL | 要求了步骤、预期/实际结果、环境、截图或录屏及日志/请求记录，但未明确要求版本信息或 console 证据。 |
| `avoids_confirmed_bug_write` | PASS | 明确建议不要作为已确认 Bug，未创建 GitHub issue 或 confirmed bug。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 保持未确认状态并区分潜在原因，提出补证和工程调查建议，但补证清单未明确覆盖版本和 console。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 保持未确认状态，提出较完整的补证和调查建议，未创建缺陷记录。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完整提出环境版本和 console 等要求的直接证据收集计划。
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

# Eval Result: eval-002-thin-evidence-suspected-bug

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-002-thin-evidence-suspected-bug`
- Test case: thin-evidence-suspected-bug
- Workspace: `workspace/eval-2-thin-evidence-suspected-bug`
- Natural user prompt:

> 用户只提供一句反馈：偶尔点击保存后页面好像没反应，没有截图、日志、复现步骤、环境信息或版本号。请分析是否能生成 Bug 报告。

- Expected artifact: 证据不足的缺陷分析，明确 suspected / needs more evidence、缺失证据、下一步收集计划，并避免创建 confirmed bug

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/bug-analyzer--eval-002-thin-evidence-suspected-bug/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `10fdf1909715a6b1da7d96cc3c254a697af93b4cc9a6354268fbce4960a8ceb1`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **PASS**（PASS 4 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: PASS

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>薄证据分类 | PASS | candidate 明确写出“疑似问题 / 待补证据”和“suspected / needs more evidence”，并明确不能生成已确认 Bug；transcript 与快照无相反证据。 | PASS | candidate 明确称只能作为疑似问题，不能标记为已确认 Bug。 |
| `assertion_2`<br>缺失证据 | PASS | candidate 列出复现步骤、实际/期望结果、截图或录屏、日志、环境、版本、权限、数据状态、发生频率，并建议收集控制台、网络请求、错误日志等。 | FAIL | 列出了复现步骤、期望/实际结果、截图或录屏、日志、环境和版本，但未明确列出 console output、network output 或 trace 等关键缺口；“网络环境”不等于网络请求输出。 |
| `assertion_3`<br>结构化输出 | PASS | 输出包含分类（疑似问题/待补证据）、证据状态、低置信度陈述、缺失信息和建议补充证据等结构化内容。 | FAIL | 虽有当前证据、缺失信息和建议追问，但没有明确的 confidence statement，结构化段落不完整。 |
| `assertion_4`<br>持久化边界 | PASS | with_skill transcript 仅有读取技能文件和输出消息；最终 workspace-snapshot 只有 feedback/customer-note.md，未见 GitHub issue、confirmed bug artifact 或其他新文件。 | PASS | transcript 无写入/外部工具调用，最终快照同样只有原始 customer-note.md，candidate 仅建议登记疑似问题。 |

## With-Skill Behavior

with_skill 将反馈分类为 suspected / needs more evidence，明确列出证据缺口和下一步收集计划；最终快照仅保留原始 fixture，未创建确认缺陷或 GitHub artifact。

## Fresh Without-Skill Baseline

without_skill 同样避免确认 Bug，但结构化证据缺口不完整，且缺少明确的 confidence statement。

## Failures

- 无。

## Not Exercised

- 无。

## Next Steps

- 无。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
