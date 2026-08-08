# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-003-xss`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `746acb9424bcff0e7d1cdbd84db8418dc8fed63831bb1cdba56197295fa9433e` from `agents/security/test/appsec-checklist/evals/workspace/eval-003-xss`.
- Fixture SHA-256: `746acb9424bcff0e7d1cdbd84db8418dc8fed63831bb1cdba56197295fa9433e`
- Prompt SHA-256: `4fbcbae96df725d2ae68317bce92f64188686abcfd62940b28a42e14a09de97f`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `095129ad5c17fd8974fdea44f1054ac02e7fa8f954b0e4a1a1d1a0ef185f9ce5`
- Skill overlay SHA-256: `5839d5cfe31d4e5dc5e9520f24a99b1147c97570ef1cc156eb90972408a49170`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6b75287b771a74771292ff6a9a4b1d4288f8c6b58ea121782df92af92abb087a`
- Metadata SHA-256: `8b9d5478f14d810cc31c023b6e6a4956d8afc5605aa60470f7733640de6334fb`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `security_findings` | PASS | with_skill 识别出 author/body 通过模板字符串进入 innerHTML，导致用户控制的 HTML 注入/XSS，并结合纯文本需求说明事件处理器、SVG 等风险。 |
| `evidence_and_impact` | PASS | with_skill 给出 src/ui/comment-display.js:2-4、API response 到 innerHTML 的完整数据流，指出 author 和 body 为受影响入口，并说明同源脚本、页面篡改及影响其他查看用户的后果。 |
| `severity_rationale` | PASS | with_skill 将风险评为 High，并以持久化用户输入、HTML 解析、查看者触发及源站脚本权限为依据，同时说明 CSP 等控制不能替代正确渲染。 |
| `remediation` | PASS | with_skill 提供了使用 DOM API、textContent 和 replaceChildren 的具体修复方案，以及覆盖恶意载荷、DOM 结构、事件执行、文本一致性和真实浏览器回归的验证步骤。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4fbcbae96df725d2ae68317bce92f64188686abcfd62940b28a42e14a09de97f; fixture_sha256=746acb9424bcff0e7d1cdbd84db8418dc8fed63831bb1cdba56197295fa9433e; output_sha256=bc205487e11ce6d2de961b40fc39b7a5b8ab70646dade66e609f8ca4e5492754; snapshot_sha256=40d65b5cbd9d3e88464292742a014d62a7977901f2568466e8fabbaef2057ca2
- Behavior: 完整覆盖用户输入到 innerHTML 的路径、XSS 风险、影响入口、严重度依据、DOM API/textContent 修复和详细浏览器验证，符合纯文本产品边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4fbcbae96df725d2ae68317bce92f64188686abcfd62940b28a42e14a09de97f; fixture_sha256=746acb9424bcff0e7d1cdbd84db8418dc8fed63831bb1cdba56197295fa9433e; output_sha256=5141a24c70c8e1ab5cc56c2cb23f25fbda9a270e4f689fc8809ecd8cac9c7dee; snapshot_sha256=fd0e748877a0f2717af5b727a7b7d0bb65c9c884ed2fa2007089034427439af6
- Behavior: 识别存储型 XSS，提供代码与数据流证据、影响和高危依据，并给出 textContent 修复及浏览器回归验证；内容较为完整。
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

# Eval Result: eval-003-xss

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-003-xss`
- Test case: XSS Vulnerability
- Workspace: `workspace/eval-003-xss`
- Natural user prompt:

> pm-agent 已完成入口分类并路由至 appsec-checklist；PM handoff packet 见 workspace `PM_HANDOFF.md`，已确认 feature_path 为 `comment-display`。Review the security of the comment display feature.

- Expected artifact: Structured application security checklist with prioritized findings, affected surfaces, evidence, impact, and remediation guidance.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/appsec-checklist--eval-003-xss/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `d940a702f03b83adaf3c38dd97f8116ae575e2bf5ca15b4193b4953da2c1f1d1`。
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
| `security_findings`<br>识别与场景匹配的应用安全风险，例如注入、认证绕过或 XSS | PASS | 最终报告明确指出 src/ui/comment-display.js:2-4 将 comment.author 和 comment.body 拼入 innerHTML，给出 img/onerror 等可利用证据，并匹配 DOM XSS 场景。 | PASS | 最终报告同样明确识别 author/body 经模板字符串写入 innerHTML 导致 High 持久型 XSS。 |
| `evidence_and_impact`<br>说明证据、受影响入口和业务或安全影响 | PASS | 报告提供具体代码位置、数据流、可复现载荷，并说明其他 viewer 浏览器中的脚本执行、页面篡改、同源操作和数据暴露影响。 | PASS | 报告提供代码行号、数据流、载荷及对其他用户浏览器、页面完整性和同源操作的影响。 |
| `severity_rationale`<br>给出严重度并说明判断依据 | PASS | 报告将问题定为 High，并依据可执行脚本注入、commenter 到其他 viewer 的跨用户边界影响进行说明。 | PASS | 报告将问题定为 High，并说明持久型 XSS、攻击者权限、受害者触发条件及可能升级为 Critical 的条件。 |
| `remediation`<br>提供具体、可执行的修复建议或验证步骤 | PASS | 最终报告已实际存在于 _eval/with_skill-workspace/docs/security/comment-display/appsec-checklist.md，包含使用 DOM API/textContent 的具体修复代码，以及覆盖载荷、DOM 结构和脚本执行的浏览器/CI 验证步骤。 | PASS | 最终报告已实际存在于 without-skill 最终快照，包含 textContent 修复示例、allowlist 注意事项、测试载荷和浏览器回归验收清单。 |

## With-Skill Behavior

With-skill 最终快照包含规定报告；逐项明确满足四条 assertion，识别并定位了 author/body 经 innerHTML 导致的 High DOM XSS，并提供影响、分级依据、修复代码和回归验证步骤。

## Fresh Without-Skill Baseline

Without-skill 也独立产出了内容充分的安全报告，四条 assertion 均满足；其结果仅作为 baseline，不影响 with-skill 判定。

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
