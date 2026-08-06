# Eval Result: eval-004-mapped-profile-retention

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-004-mapped-profile-retention`
- Test case: Mapped Profile Data Retention
- Workspace: `workspace/eval-004-mapped-profile-retention`
- Natural user prompt:

> 请梳理 src/privacy/profile-processing.yaml 的个人资料处理面，重点核对收集字段、处理目的和删除后的保留期限。

- Expected artifact: 优先读取 change-map 命中的个人资料处理文档，再以配置核对保留期限；将 unverified 文档按最低信任处理并报告 30 天声明与 90 天配置事实的不一致。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/privacy-surface-mapper--eval-004-mapped-profile-retention/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `fe202006e2cd8c214b98b02eac15e2f5aa8a803e13a5f2bb5e302fccc9ac60ba`。
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
| `reads_mapped_docs_first`<br>命中 change-map 后优先读取个人资料 required_docs | FAIL | transcript 先读取 profile-processing.yaml，再读取接口文档和 change-map；未先反查 change-map 后优先读取 required_docs。 | FAIL | transcript 未读取 change-map 或 required_docs 文档。 |
| `verifies_against_code`<br>以处理配置核对删除后的保留期限 | PASS | transcript 回读配置并明确指出配置为 90 天、文档声称 30 天；candidate 以配置事实识别冲突并要求统一规则。 | FAIL | 仅报告配置中的 90 天，未读取或识别 required 文档中的 30 天冲突。 |
| `treats_unverified_as_low_trust`<br>将 unverified 隐私文档按最低信任处理 | PASS | candidate 明确识别文档 last_verified_version 为 unverified，并说明 30 天不能作为已核实有效规则，同时以配置进行核证。 | FAIL | 未读取文档元数据，未识别 unverified，也未扩大配置核证。 |
| `escalates_fact_changing_conclusion_to_pm`<br>改变正式文档事实的结论升级 | FAIL | 期限冲突改变正式 docs/site 文档事实，且契约要求回交 pm-agent 分类并创建 issue、产出 docs/security 报告；最终快照中仅有原始 fixture，没有报告、升级或 issue 证据。 | NOT EXERCISED | baseline 未读取正式文档，未形成改变正式文档事实的结论，故该触发条件未实际发生。 |

## With-Skill Behavior

发现配置与 unverified 文档的 90/30 天保留期限冲突，并完成字段、目的与配置核对；但未按 change-map 优先顺序读取文档，也未生成 Security 报告或回交 pm-agent 分类建 issue。

## Fresh Without-Skill Baseline

仅读取配置并总结 90 天，未读取 change-map、required_docs，也未识别文档冲突或 unverified 信任问题。

## Failures

- with-skill 未遵守 change-map → required_docs 的读取顺序。
- with-skill 未产出 Security-owned privacy-map 报告，也未按触发条件升级至 pm-agent 分类并创建 issue。

## Not Exercised

- 无。

## Next Steps

- 若补测，应检查 transcript 中 change-map 反查及 required_docs 优先读取顺序。
- 应在最终工作区核验 docs/security/{feature_path}/privacy-map.md、pm-agent 升级证据及 issue 创建结果。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
