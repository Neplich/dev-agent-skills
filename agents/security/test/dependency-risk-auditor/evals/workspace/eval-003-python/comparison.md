# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-003-python`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3` from `agents/security/test/dependency-risk-auditor/evals/workspace/eval-003-python`.
- Fixture SHA-256: `8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3`
- Prompt SHA-256: `109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9847519784146234ee8e6186ebd4f58b4e08cc25986e95e53a8cdbe8be3e0635`
- Skill overlay SHA-256: `b8089650410317e7cdca1594ef3aeb917b416730f8419e99172c09b88f6c8fc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b851960b1dd4c6ab11f9c42f685034d6bd0e27ae3c26e4256af19942329ed614`
- Metadata SHA-256: `86d72efa91ee3890167dbac2135eac8aaff379e02491ea01e89a3595936d759c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dependency_inventory` | PASS | Identifies all three pinned dependencies and maps them to HTTP, TLS, and template risk surfaces. |
| `risk_classification` | PASS | Distinguishes vulnerabilities, maintenance risk, supply-chain observations, severity, and conditional exploitability. |
| `evidence` | PASS | Cites exact versions from requirements.txt and provides CVE, release-history, and limitation evidence. |
| `upgrade_plan` | PASS | Provides target versions, temporary mitigations, upgrade sequencing, regression tests, and release gates. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=681819f077024758640ff7c9832fbcaf971824a19cbb6c48fdea0145f9c17be8; snapshot_sha256=55c87f847faa464dc6809820a05d6c7b402bd3e6ff748ee000a5ae03257f4369
- Behavior: Provides a structured, evidence-grounded audit with classifications, remediation, validation, and release gates.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=109b986b4018ed5121d20e83d0f03f39a0aaef687eb5dd7c1936ee4b3a089210; fixture_sha256=8307ea1325de4c132e54824c9dd507ed174ce29fe901e9f04e5a56bc654490e3; output_sha256=6e6a6ab566635b436ad0cc9b4f339f58200e83194343f847058f0e25a36390a6; snapshot_sha256=a4f4201f83e05090830a661b6c7faaabd490746e485c99577ced83c87d61894c
- Behavior: Identifies dependencies, risks, upgrade targets, and mitigations, but is less comprehensive.
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

# Eval Result: eval-003-python

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-003-python`
- Test case: Python Dependency Audit
- Workspace: `workspace/eval-003-python`
- Natural user prompt:

> pm-agent has completed entry classification and routed this confirmed `dependency-inventory` security scope to dependency-risk-auditor. Use the PM handoff packet in workspace `PM_HANDOFF.md` and the confirmed source document `docs/pm/dependency-inventory/PRD.md`. Review Python dependencies for security issues.

- Expected artifact: Structured dependency risk audit that identifies vulnerable, outdated, or abandoned packages with severity, evidence, and upgrade or mitigation guidance.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/dependency-risk-auditor--eval-003-python/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `6e2bb4aec3b87f9503c5fc46324b2258d9ef732b80318b6d5c0ebb7bb9b3f56c`。
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
| `dependency_inventory`<br>识别依赖生态、关键包和风险来源 | PASS | 报告明确识别 Python 生态，并列出 requests==2.19.1、urllib3==1.23、Jinja2==2.10.1 及其 HTTP、TLS、模板相关风险。 | PASS | 报告列出三项 Python 直接依赖及对应 HTTP、TLS、模板风险。 |
| `risk_classification`<br>区分漏洞、废弃、过期或供应链风险并说明严重度 | PASS | 报告区分漏洞、过期/不受支持版本和供应链/补丁滞后风险，并按 Critical、High、Medium 说明严重度及可利用条件。 | PASS | 报告区分已知漏洞、不受支持版本和模板风险，并给出 High/Medium 严重度与利用条件。 |
| `evidence`<br>引用依赖文件、版本或已知风险作为证据 | PASS | 报告引用 requirements.txt 中的精确版本和行号，并提供多个 CVE/GHSA 及外部 advisory 链接作为证据。 | PASS | 报告引用 requirements.txt:1-3、精确版本及多个 CVE/GHSA advisory。 |
| `upgrade_plan`<br>给出升级、替换或缓解建议 | PASS | 报告给出协调升级到 requests 2.34.2、urllib3 2.7.0、Jinja2 3.1.6+ 的优先级、测试要求、CI 审计和升级延迟时的临时缓解措施。 | PASS | 报告给出替换全部 pin、协调升级、DevOps 临时控制和 lockfile/SBOM 后续计划。 |

## With-Skill Behavior

With-skill 明确读取 handoff、PRD 和 requirements.txt，创建了符合契约的 dependency-audit.md，包含三项依赖、版本证据、漏洞/过期分类、严重度、CVE、限制条件及升级和缓解建议。

## Fresh Without-Skill Baseline

Without-skill 也完成了依赖审计并创建报告，作为 baseline 各项断言均满足。

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
