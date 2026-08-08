# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-004-mapped-profile-retention`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-004-mapped-profile-retention`.
- Fixture SHA-256: `ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb`
- Prompt SHA-256: `15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `32486beb9db21ed173f2083e3323014ff05de4963e7a8b1d84d40eb43ab3aa33`
- Skill overlay SHA-256: `874b129b045f44af288c1af739a4a66f07931a151f79399740585f1fce30c452`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8768d40f89a0835f8bc18dc793ab9c71861c190253ab19b6d21f19d51aa1ed50`
- Metadata SHA-256: `7059498df03f32583db887e25af006a8504ba7d72f9cb363375b4bcdb24efad6`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | With-skill output cites the change map, its required document, and the linked privacy configuration, with no unrelated formal documents presented. |
| `verifies_against_code` | FAIL | It correctly identifies the 30-day versus 90-day conflict and distinguishes configuration from runtime evidence, but does not evaluate the compliance impact using the configuration fact as required. |
| `treats_unverified_as_low_trust` | FAIL | The fixture marks last_verified_version as unverified, but the with-skill output never identifies or discusses this status. |
| `escalates_fact_changing_conclusion_to_pm` | FAIL | The output recommends confirmation and document synchronization but does not return the changed conclusion to pm-agent, classify it, or create an issue; it also provides no required Security process report. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f; fixture_sha256=ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb; output_sha256=47389664dcf3785f4d2a4a1847a1f560943e6ded15f4203a7779d1c5bf53fc80; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Uses the change map and linked documents, accurately separates configuration declarations from runtime evidence, but omits unverified-status handling, compliance-impact evaluation, and required pm-agent issue escalation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=15781c686db28c8e23be7d15ddb44295e5640725a6c0d3e97e4814f9916ad62f; fixture_sha256=ae2f7b18628f3022eadc959d5f64f8f6cc91f393bb8423cb17fc823cb3e454bb; output_sha256=5ac6fbda5924bcde872bc30514dd09b5bd1ed9b0dbf4ffad3a06fcb53dac5b22; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly reports the field and purpose matches and identifies the 30-day versus 90-day retention conflict, but does not demonstrate the required unverified-document handling or pm-agent escalation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- verifies_against_code: missing explicit compliance-impact evaluation grounded in the 90-day configuration.
- treats_unverified_as_low_trust: does not address last_verified_version: unverified.
- escalates_fact_changing_conclusion_to_pm: no pm-agent classification or issue creation, and no applicable Security process report.
- Next: Explicitly treat the unverified document as low trust and expand configuration-based verification.
- Next: State the compliance impact of the 90-day configured retention conflicting with the 30-day formal documentation.
- Next: Escalate the changed conclusion to pm-agent with classification and create the required issue.

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
