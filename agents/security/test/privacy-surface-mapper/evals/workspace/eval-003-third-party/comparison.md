# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-003-third-party`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-003-third-party`.
- Fixture SHA-256: `a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73`
- Prompt SHA-256: `f08db36d8714dffcf75b41015d8dc4b37be4570b39ece9523f67238ebf8ed935`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `32486beb9db21ed173f2083e3323014ff05de4963e7a8b1d84d40eb43ab3aa33`
- Skill overlay SHA-256: `874b129b045f44af288c1af739a4a66f07931a151f79399740585f1fce30c452`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `fde37322a972618cf8b85d5463c8e7a856c7547f8c15123669fd15297f556852`
- Metadata SHA-256: `1b358949b025cd13ff498cda0a21978c243d4781824a1ceab1947fe97db21069`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | with_skill 明确列出分析、广告、支付接收的用户标识、邮箱、IP、页面 URL、购买金额、支付客户 ID 和内部用户 ID，并说明了代码入口、触发方式及处理目的。 |
| `sharing_and_retention` | PASS | with_skill 逐项说明三方共享、美国地域配置、广告地域缺失、730/2555 天保留、广告保留未记录，以及各方删除能力和生命周期风险。 |
| `user_rights` | PASS | with_skill 检查并明确指出未发现访问、导出、更正、删除、第三方请求传播或广告同意撤回流程，并区分了支付仅配置删除 API但未验证调用链。 |
| `compliance_gaps` | PASS | with_skill 提供了按风险优先级排列的整改建议，覆盖广告同意门控、分析最小化与删除、地域/保留/删除信息补齐、支付删除范围验证和处理依据记录。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f08db36d8714dffcf75b41015d8dc4b37be4570b39ece9523f67238ebf8ed935; fixture_sha256=a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73; output_sha256=9ad10a6a6406d31c0db447c6f3c77da044a4df334b80d8108c0de68769ef5559; snapshot_sha256=12504bb68bcba805a8a56171a72e1662fc74f2eaaf918aa7ddb30f66b7e9c05a
- Behavior: 输出形成结构化隐私处理面报告，基于原始代码和配置逐项盘点数据流、同意、地域、保留、删除及用户权利，并给出具体整改建议。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f08db36d8714dffcf75b41015d8dc4b37be4570b39ece9523f67238ebf8ed935; fixture_sha256=a0f9b5ed56aa92319d126897928b2da5ef1b5b085fbe003f0b4425dde5805c73; output_sha256=796f966a4252f9b2e1c5caf491006fd01a1e3e531a42cfb92fc8eff895ae56f9; snapshot_sha256=06822c9d604923df24b709e8ba41e48d3e91794c2be0bfc1ceeff702f8f2b3bc
- Behavior: 基线已覆盖主要供应商、字段、地域、保留、删除和整改结论，但用户权利与证据边界相对简略。
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

# Eval Result: eval-003-third-party

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-003-third-party`
- Test case: Third-Party Data Sharing
- Workspace: `workspace/eval-003-third-party`
- Natural user prompt:

> pm-agent has completed entry classification and routed this confirmed `third-party-sharing` security scope to privacy-surface-mapper. Use the PM handoff packet in workspace `PM_HANDOFF.md` and the confirmed source document `docs/pm/third-party-sharing/PRD.md`. Identify all third-party services receiving user data.

- Expected artifact: Structured privacy surface map that identifies personal data, processing purpose, third-party sharing, user-rights gaps, and compliance risks.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/privacy-surface-mapper--eval-003-third-party/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `ca8fffebb733ec434021e77c2c210929e461bda51c1e7d4a57f5a1893e191202`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **PASS**（PASS 4 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Historical Contract Note

上一份 durable comparison 基于 issue #234 修复前会向 baseline 泄漏规则的旧契约，因此标记为 `BLOCKED`。本轮使用当前无泄漏 prompt/fixture 重新生成两条 lane，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `data_inventory`<br>识别个人数据类型、收集入口和处理目的 | PASS | 最终快照中的 docs/security/third-party-sharing/privacy-map.md 明确列出内部用户 ID、邮箱、IP、页面 URL、订单金额和支付客户 ID，并说明各自用途、触发流程和保留信息；transcript 也显示其追溯了 PRD、user-events.js 与 vendors.json。 | PASS | 最终快照中的 privacy-surface-report.md 按服务列出发送字段、用途和 sendUserEvent 触发入口，足以支持数据类型、入口和目的识别。 |
| `sharing_and_retention`<br>识别第三方共享、存储或保留相关风险 | PASS | privacy-map.md 明确列出三家第三方、接收字段、区域、同意、保留和删除支持；同时指出 ExampleAds 默认开启且无需同意、ExampleAnalytics 无删除 API、ExampleAds 保留期限未记录等风险。 | PASS | baseline 报告列出三家服务及字段、区域、保留和删除状态，并指出广告同意、保留及权利请求传播缺口。 |
| `user_rights`<br>检查访问、删除、导出或同意等用户权利支持情况 | PASS | privacy-map.md 明确检查 Access、Deletion、Export/portability、Correction 四项状态，并说明 ExamplePay 有删除 API、ExampleAnalytics 无删除 API、ExampleAds 支持未记录，以及缺少传播工作流。 | PASS | baseline 报告明确记录删除支持和用户权利请求传播未文档化，并提出跨供应商 access、deletion、opt-out 等请求流程建议。 |
| `compliance_gaps`<br>给出隐私合规缺口和改进建议 | PASS | privacy-map.md 包含 HIGH/MEDIUM 隐私风险及具体整改建议，覆盖广告默认共享、同意、保留删除、数据最小化、传输地域和权利请求传播。 | PASS | baseline 报告包含合规风险和整改建议，覆盖广告同意、数据最小化、保留删除、传输地域和权利请求传播。 |

## With-Skill Behavior

with-skill 正确读取契约、PM handoff、PRD、代码和供应商配置，识别出 ExampleAnalytics、ExampleAds、ExamplePay，并在最终快照创建了完整 privacy-map.md。

## Fresh Without-Skill Baseline

without-skill 也识别出三家服务并创建报告，但报告结构和用户权利覆盖较不完整，作为 baseline 评估不影响 with-skill 行为结论。

## Failures

- 无。

## Not Exercised

- 未触发无 PM handoff 的入口拒绝分支；本 fixture 已提供有效 handoff。
- 未触发 docs/site/standards/change-map.yaml 存在时的 consumption-contract/change-map 探索分支；fixture 中不存在该文件。
- 未提供 docs/engineer 下的 TRD 或 IMPLEMENTATION_PLAN，因此相关架构文档读取分支未被实际执行。
- 未触发需要将结论升级回 PM 的额外 closeout 条件；transcript 仅显示完成报告并交付结论。

## Next Steps

- 如需 FULL coverage，增加直接调用、change-map 存在、工程文档存在及触发 PM escalation 的独立 fixture。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
