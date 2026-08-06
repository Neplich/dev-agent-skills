# Eval Result: eval-004-mapped-report-export-authz

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-004-mapped-report-export-authz`
- Test case: Mapped Report Export Authorization
- Workspace: `workspace/eval-004-mapped-report-export-authz`
- Natural user prompt:

> 请审查 src/access/report-export-policy.js 的报表导出授权逻辑，说明哪些角色可以导出以及是否存在越权风险。

- Expected artifact: 优先读取 change-map 命中的报表导出文档，再以代码核对角色权限；将 unverified 文档按最低信任处理并报告管理员专属声明与 analyst 可导出事实的不一致。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/authz-reviewer--eval-004-mapped-report-export-authz/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `9639cce1288a627343633a3f6f1cd38e62beaa58df89ae4e8eb5100e906b8a7f`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **FAIL**（PASS 2 / FAIL 2 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Historical Contract Note

上一份 durable comparison 基于 issue #234 修复前会向 baseline 泄漏规则的旧契约，因此标记为 `BLOCKED`。本轮使用当前无泄漏 prompt/fixture 重新生成两条 lane，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `reads_mapped_docs_first`<br>命中 change-map 后优先读取报表导出 required_docs | FAIL | transcript 先读取目标代码并进行广泛搜索，之后才读取 change-map 和命中文档，未按 change-map 反查后优先读取 required_docs。 | FAIL | transcript 先读取代码并进行全局搜索，之后才读取 change-map 和 required_docs。 |
| `verifies_against_code`<br>以授权策略代码核对可导出角色 | PASS | transcript 和 candidate 明确引用 report-export-policy.js:2，确认 admin 与 analyst 均可导出，并指出与文档仅允许 admin 的冲突。 | PASS | candidate 和 transcript 均明确核对代码，正确识别 admin、analyst 均被放行及其与文档的不一致。 |
| `treats_unverified_as_low_trust`<br>将 unverified 授权文档按最低信任处理 | PASS | transcript 读取到 change-map 与 required_docs 的 last_verified_version 为 unverified，且授权结论回到代码事实核验，没有拒绝读取或直接采信文档。 | PASS | transcript 读取并显示 unverified 元数据，同时以代码结论为主进行判断；虽未明确阐述信任等级，但未直接依赖文档替代代码核验。 |
| `escalates_fact_changing_conclusion_to_pm`<br>改变正式文档事实的结论升级 | FAIL | 已确认代码改变正式文档事实，但 candidate 未回交 pm-agent、未创建 issue 分类交接，最终工作区也没有 docs/security 过程报告或其他升级产物。 | FAIL | 同样识别了代码与正式文档冲突，但没有 PM 交接、issue 或 Security 过程报告产物。 |

## With-Skill Behavior

代码核验和文档不一致识别正确，但未遵守 change-map 优先读取顺序，也未完成 PM 升级、创建 Security 过程报告及 issue 分类交接。

## Fresh Without-Skill Baseline

独立 baseline 正确识别 admin/analyst 均可导出及文档冲突，但同样未完成映射优先顺序和升级产物。

## Failures

- with-skill 未按 change-map 优先读取命中文档。
- with-skill 未按契约将改变正式文档事实的结论升级至 pm-agent，也未创建要求的报告/issue 交接产物。

## Not Exercised

- 无。

## Next Steps

- 补充按 change-map 顺序执行的审查证据。
- 在最终工作区创建 Security 自有过程报告，并将文档事实冲突回交 pm-agent 分类及创建 issue。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
