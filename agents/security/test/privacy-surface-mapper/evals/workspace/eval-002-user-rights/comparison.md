# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-002-user-rights`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-002-user-rights`.
- Fixture SHA-256: `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8`
- Prompt SHA-256: `f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `32486beb9db21ed173f2083e3323014ff05de4963e7a8b1d84d40eb43ab3aa33`
- Skill overlay SHA-256: `874b129b045f44af288c1af739a4a66f07931a151f79399740585f1fce30c452`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ba5034d1b895bcb95cc9d848045b869189eec2c98d23c0a5d5ce381059a73047`
- Metadata SHA-256: `b655e3698222cf189fb740616c1df41fb5ccc3d4bf71526ca29a7ecf05ef368a`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | With_skill identifies user profiles, orders/transaction metadata, analytics events, and additional data in sessions, tokens, logs, backups, and caches; it maps collection/read paths and purposes. |
| `sharing_and_retention` | PASS | With_skill identifies analytics systems, third-party processors, caches, backups, logs, and retention/legal-hold gaps, with deletion propagation and expiry recommendations. |
| `user_rights` | PASS | With_skill evaluates access, export, deletion, and rectification support, including session binding, incomplete export scope, deletion propagation, status tracking, CSRF, and token revocation. |
| `compliance_gaps` | PASS | With_skill provides concrete privacy/security gaps, impacts, remediation steps, and a pre-launch acceptance checklist. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=0eeed96e8c196777ee6814b71de4f864d24b1f4e17b8ffac6ff10031fe523917; snapshot_sha256=40d35781ced0f5bf2a9a6b98bbca9126bbd26953c255647e4fe3626a9dd4a7b2
- Behavior: Structured privacy-surface review maps data categories and flows, evaluates user rights and sharing/retention risks, and provides evidence-backed compliance gaps and remediation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=ba6800663a1eb268339c3c50cdd805529789f7637b59076506cf902f7185177f; snapshot_sha256=61a3e4e2d227e03e03035ba48e06c64d076e39b4287e74c84eaab23884d5baf0
- Behavior: Fresh baseline identifies major authorization, export completeness, deletion propagation, delivery, error handling, audit, retention, and rate-limit gaps, but gives less explicit data inventory and privacy-surface mapping.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

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

# Eval Result: eval-002-user-rights

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-002-user-rights`
- Test case: User Rights Implementation
- Workspace: `workspace/eval-002-user-rights`
- Natural user prompt:

> pm-agent has completed entry classification and routed this confirmed `user-rights` security scope to privacy-surface-mapper. Use the PM handoff packet in workspace `PM_HANDOFF.md` and the confirmed source document `docs/pm/user-rights/PRD.md`. Check if user rights (access, deletion, export) are implemented.

- Expected artifact: Structured privacy surface map that identifies personal data, processing purpose, third-party sharing, user-rights gaps, and compliance risks.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/privacy-surface-mapper--eval-002-user-rights/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `51099ecfc1cc6407a2a8395e70e437687a8d984b7702e62660481c6549a657be`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **PASS**（PASS 4 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: PASS

## Historical Contract Note

上一份 durable comparison 基于 issue #234 修复前会向 baseline 泄漏规则的旧契约，因此标记为 `BLOCKED`。本轮使用当前无泄漏 prompt/fixture 重新生成两条 lane，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `data_inventory`<br>识别个人数据类型、收集入口和处理目的 | PASS | 报告明确识别用户资料、订单/交易元数据、分析行为事件及备份副本，并列出收集/处理入口和目的；最终快照存在 privacy-map.md。 | PASS | PRIVACY_SURFACE_REPORT.md 明确列出用户资料、订单、行为事件及相关数据范围，并说明处理上下文。 |
| `sharing_and_retention`<br>识别第三方共享、存储或保留相关风险 | PASS | 报告识别 analytics 为下游接收方、备份为内部副本，并明确缺少传输/供应商信息、保留期限、删除传播和法定保留策略。 | PASS | 报告识别 analytics、后台任务和备份中的数据副本，并明确删除传播、保留期限和法定保留处理缺口。 |
| `user_rights`<br>检查访问、删除、导出或同意等用户权利支持情况 | PASS | 报告逐项核验 access、export、deletion，并以 src/api/user-rights.js 行号说明 session 身份、userId 越权、数据不完整、软删除及无传播/追踪。 | PASS | 报告逐项评估 /me、/data-export 和 DELETE /me，准确指出访问部分实现、导出越权且不完整、删除仅软删除。 |
| `compliance_gaps`<br>给出隐私合规缺口和改进建议 | PASS | 报告包含 CRITICAL/HIGH/MEDIUM 风险、GDPR/CCPA 影响及 Engineer/DevOps/Product Legal 分工的具体整改建议。 | PASS | 报告包含风险评级、PRD 验收缺口及工程、DevOps 的具体修复建议。 |

## With-Skill Behavior

已按 PM handoff 和 PRD 核验代码，并在最终快照创建了符合契约的 docs/security/user-rights/privacy-map.md。报告覆盖数据范围、入口、目的、共享/保留风险、用户权利状态及整改建议。

## Fresh Without-Skill Baseline

Baseline 也创建了结构化隐私报告并覆盖四项断言，作为对照不影响 with-skill 判定。

## Failures

- 无。

## Not Exercised

- 无。

## Next Steps

- 无。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
