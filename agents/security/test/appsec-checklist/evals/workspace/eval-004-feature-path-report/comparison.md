# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-004-feature-path-report`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c` from `agents/security/test/appsec-checklist/evals/workspace/eval-004-feature-path-report`.
- Fixture SHA-256: `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c`
- Prompt SHA-256: `05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `095129ad5c17fd8974fdea44f1054ac02e7fa8f954b0e4a1a1d1a0ef185f9ce5`
- Skill overlay SHA-256: `5839d5cfe31d4e5dc5e9520f24a99b1147c97570ef1cc156eb90972408a49170`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `cea867306caa7c154c38a57a7085c1f3dc292e28eb28f571e99034334c62710c`
- Metadata SHA-256: `8529cb6cbe6ab9523b4f7cf3b65440375e54cbaab5ce6a8376eb7a3bc4427f65`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_same_path_pm_engineer_docs` | PASS | with_skill workspace_manifest includes the PRD, TRD, and IMPLEMENTATION_PLAN at the exact required nested paths; the report also names them as review context. |
| `writes_nested_security_report` | PASS | with_skill output and delivery_snapshot show docs/security/chat-interface/messages/history/search/appsec-checklist.md. |
| `includes_feature_path_frontmatter` | PASS | The report frontmatter contains feature_path, parent_feature, and numeric feature_level 4 with the required values. |
| `does_not_invent_feature_directory` | PASS | The feature path is clear and all three same-path PM/Engineer documents exist; with_skill uses the established path and does not create a synonym directory. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The evidence shows a security assessment of implementation risks, but no conclusion that changes a formal-document fact; therefore the conditional PM escalation requirement is not triggered. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=c96550f98083768a10bdeb089717d665de6862738d73b4cde3ec74db5b61791c; snapshot_sha256=b9396df19f2b611fb99b3b3d60b6da35acc93ce57bfb88d94203bd998b68fa9c
- Behavior: Reviewed the code and all three same-path feature documents, produced the required nested Security report with correct frontmatter, and documented the observed security risks.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=0ffe5b1c8fdea11b438766c54c512bc283eee8087192ffc9a04b578daf8abf83; snapshot_sha256=9631b8621b81870395b2f7a88ea398dcdc18582816f3cdce893c82a0fbe76466
- Behavior: Reviewed the code and feature documents but wrote SECURITY_REVIEW.md under the Engineer feature directory; did not produce the required nested Security report or required frontmatter.
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

# Eval Result: eval-004-feature-path-report

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-004-feature-path-report`
- Test case: Feature Path Security Report
- Workspace: `workspace/eval-004-feature-path-report`
- Natural user prompt:

> 对 chat-interface/messages/history/search 做发布前应用安全检查。仓库中已有 docs/pm/chat-interface/messages/history/search/PRD.md、docs/engineer/chat-interface/messages/history/search/TRD.md 和 docs/engineer/chat-interface/messages/history/search/IMPLEMENTATION_PLAN.md。

- Expected artifact: 读取同一 feature_path 下的 PM/Engineer 文档，输出 docs/security/chat-interface/messages/history/search/appsec-checklist.md，frontmatter 包含 feature_path，不生成 docs/security/history-search/appsec-checklist.md 或 docs/security/chat-interface/history-search/appsec-checklist.md。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/appsec-checklist--eval-004-feature-path-report/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `c7233a79d75e848f621326abec96afbba234cf0071a3c7333681db1dbb0d397a`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **FAIL**（PASS 3 / FAIL 1 / NOT EXERCISED 1）
- Coverage result: **PARTIAL**
Overall result: FAIL

## Historical Contract Note

上一份 durable comparison 基于 issue #234 修复前会向 baseline 泄漏规则的旧契约，因此标记为 `BLOCKED`。本轮使用当前无泄漏 prompt/fixture 重新生成两条 lane，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `uses_same_path_pm_engineer_docs`<br>读取 chat-interface/messages/history/search 的 PRD、TRD 和 IMPLEMENTATION_PLAN | PASS | with-skill transcript 明确读取了 docs/pm/chat-interface/messages/history/search/PRD.md、docs/engineer/chat-interface/messages/history/search/TRD.md 和 IMPLEMENTATION_PLAN.md；最终快照中的对应文件也存在。 | PASS | without-skill transcript 明确读取了同一 PRD、TRD 和 IMPLEMENTATION_PLAN。 |
| `writes_nested_security_report`<br>输出嵌套 Security appsec 报告路径 | PASS | 最终快照存在 docs/security/chat-interface/messages/history/search/appsec-checklist.md，未发现错误的顶层替代路径。 | FAIL | without-skill 最终快照没有生成任何 docs/security 下的 appsec-checklist 报告。 |
| `includes_feature_path_frontmatter`<br>报告 frontmatter 包含 feature path 字段 | PASS | 报告 frontmatter 明确包含 feature_path: chat-interface/messages/history/search、parent_feature: chat-interface/messages/history、feature_level: 4。 | FAIL | without-skill 没有报告，因此没有满足要求的 frontmatter。 |
| `does_not_invent_feature_directory`<br>路径不清时回 PM/Engineer | NOT EXERCISED | fixture 中 feature_path 清晰，且三份同路径文档均存在；未触发回 PM/Engineer 的条件。 | NOT EXERCISED | 同一客观 fixture 未触发路径不清或文档缺失分支。 |
| `escalates_fact_changing_conclusion_to_pm`<br>改变正式文档事实的结论升级 | FAIL | 报告和最终结论确认实现未满足 TRD 的工作区授权要求，属于改变正式文档事实的安全结论；transcript 没有回交 pm-agent 分类或创建 issue 的证据，且直接结束在报告/结论输出。 | FAIL | without-skill transcript 也确认实现与 PRD/TRD 要求不一致，但没有回交 pm-agent 分类并创建 issue的证据。 |

## With-Skill Behavior

with-skill 正确读取了三份同路径文档，并在最终快照生成了正确嵌套路径的报告及所需 frontmatter；但确认实现与 TRD/PRD 存在安全事实偏差后，没有按契约回交 pm-agent 分类并创建 issue。

## Fresh Without-Skill Baseline

without-skill 读取了三份文档并识别出主要风险，但未生成 Security 报告，也未执行所需的 PM 升级。

## Failures

- with-skill 未执行触发条件已满足的 Security Conclusion Escalation to PM。

## Not Exercised

- does_not_invent_feature_directory：feature_path 清晰且 PRD、TRD、IMPLEMENTATION_PLAN 均存在。

## Next Steps

- 应将安全结论与 src/search.ts 及 PRD/TRD 要求的证据回交 pm-agent 分类并创建 issue；Security 报告可保留在当前嵌套 docs/security 路径。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
