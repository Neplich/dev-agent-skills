# Eval Result: eval-004-mapped-client-dependency

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-004-mapped-client-dependency`
- Test case: Mapped Client Dependency Documentation
- Workspace: `workspace/eval-004-mapped-client-dependency`
- Natural user prompt:

> 请审计 src/dependencies/manifest.json 中网络客户端依赖的风险，核对当前版本并给出升级或缓解建议。

- Expected artifact: 优先读取 change-map 命中的依赖文档，再以清单核对实际版本；将 unverified 文档按最低信任处理并报告文档版本与依赖清单不一致。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/dependency-risk-auditor--eval-004-mapped-client-dependency/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `50286ee8a9457cdaf5db903f683f85a450cef6f52b1dc5e362fb5ca91aa38ed7`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **FAIL**（PASS 3 / FAIL 1 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Historical Contract Note

上一份 durable comparison 基于 issue #234 修复前会向 baseline 泄漏规则的旧契约，因此标记为 `BLOCKED`。本轮使用当前无泄漏 prompt/fixture 重新生成两条 lane，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `reads_mapped_docs_first`<br>命中 change-map 后优先读取网络客户端 required_docs | PASS | transcript 中读取 manifest 后读取 change-map，并紧接着读取其命中的 docs/site/api/network-client.md；未读取其他正式文档。 | FAIL | transcript 未读取 change-map，直接读取 network-client 文档，未按映射反查流程执行。 |
| `verifies_against_code`<br>以依赖清单核对网络客户端版本 | PASS | candidate 明确引用 manifest.json 中 network-client@1.4.0，并识别其与文档声称的 2.1.0 不一致，且以清单版本评估风险。 | PASS | candidate 明确核对 manifest.json 的 1.4.0，并识别与文档 2.1.0 的冲突。 |
| `treats_unverified_as_low_trust`<br>将 unverified 依赖文档按最低信任处理 | PASS | transcript 读取 change-map 和 required_docs 均显示 last_verified_version: unverified；candidate 未直接采信文档，扩大到 manifest、包管理元数据缺失和来源核验。 | PASS | candidate 识别文档标记为 unverified，并结合 manifest 版本冲突，将真实版本和漏洞结论列为不可验证。 |
| `escalates_fact_changing_conclusion_to_pm`<br>改变正式文档事实的结论升级 | FAIL | 版本冲突实际改变了正式文档事实，但最终 with_skill-workspace 仅保留原始三份 fixture 文件；没有 docs/security 过程报告，也没有回交 pm-agent 或创建 issue 的明确证据。 | FAIL | 同样未创建 Security 报告、未回交 pm-agent、未创建 issue。 |

## With-Skill Behavior

读取顺序最终先读取 change-map，再读取命中的 network-client 文档，并回到 manifest 核验 1.4.0 与文档 2.1.0 的冲突；正确识别 unverified，但未产出 Security-owned 报告，也未将改变正式文档事实的结论回交 pm-agent 并创建 issue。

## Fresh Without-Skill Baseline

直接读取依赖与网络客户端文档，识别版本冲突并给出建议，但未读取 change-map，且同样未执行要求的 PM 升级与报告产出。

## Failures

- with-skill 未满足事实变更结论的 PM 升级与 issue 创建要求。
- with-skill 最终工作区没有要求的 docs/security 过程报告。

## Not Exercised

- 无。

## Next Steps

- 补充 Security-owned dependency audit 报告，并将版本冲突及证据交回 pm-agent 分类和创建 issue。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
