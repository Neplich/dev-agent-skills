# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-003-route-release-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6` from `agents/docs/test/docs-agent/evals/workspace/eval-003-route-release-audit`.
- Fixture SHA-256: `aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6`
- Prompt SHA-256: `099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e64e4dc492a2ff92be09822529f9abb1fbd17f4d0148b3045e0162382c5d46d3`
- Skill overlay SHA-256: `c66ac938bf9158faa694d7c3e311e913ddc4a06da11de703a881234f257c470c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `76669427412e6a3d2662bf813faa0ce4c31fa19c75739559cabe530efd5682a6`
- Metadata SHA-256: `d582bafa2b7d4e637ef2b4b71f14f435256d70c30e92f7097a43cd40dc9da750`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_equivalent_chain` | FAIL | with_skill only says v0.4.0 was confirmed by release-entry.md; it does not identify the confirmed release scope, changelog, release evidence, and audit request as the equivalent entry chain. |
| `routes_docs_audit` | FAIL | It names docs-audit, but does not retain or pass through the release scope, changelog, or release evidence; it instead performs and reports the audit itself. |
| `references_audit_gate_only` | FAIL | It names docs-audit but proceeds beyond the router boundary with audit findings and internal details including base_ref, change-map, version sources, and evidence requirements. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230; fixture_sha256=aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6; output_sha256=1a358d182d6c15fa2305ab4b260b9566f3bd28f81e1e73905c6b0a4917cd3ebd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Names docs-audit but performs a detailed pre-release audit and reports blockers rather than stopping at the routing handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230; fixture_sha256=aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6; output_sha256=b1afda782b8f3be0e6a8cdf4e8b7fbb9f234db9683f0c36b6a5ab8afffbb06f8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline independently audits the fixture, reports missing files and evidence, and provides remediation steps; it does not route through docs-audit.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output does not recognize the complete equivalent confirmed release-entry chain.
- The with_skill output does not preserve the required release inputs at the routing handoff.
- The with_skill output goes beyond the docs-audit router boundary and exposes internal audit details.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-003-route-release-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6` from `agents/docs/test/docs-agent/evals/workspace/eval-003-route-release-audit`.
- Fixture SHA-256: `aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6`
- Prompt SHA-256: `099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9b5483c75770358083301bcb4f3e774af3a6e851f51536b52de7b7f0a1bd16fd`
- Skill overlay SHA-256: `40330c17a3b77f25a1b1a716fa5e9355e0011db79d19014344ed516affba11c8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `de5a2db0bd2b7f9e954e9508acd922a60bc65f454c61fbc72a9200f5a2156e7f`
- Metadata SHA-256: `d582bafa2b7d4e637ef2b4b71f14f435256d70c30e92f7097a43cd40dc9da750`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_equivalent_chain` | FAIL | with_skill 输出只明确提到 v0.4.0 和 docs-audit，未识别 release scope、changelog、release evidence 与审计请求组成等效确认入口。 |
| `routes_docs_audit` | FAIL | 虽选择了 docs-audit，但未保留 release scope、changelog 与 release evidence；输出反而将 changelog 标为缺失。 |
| `references_audit_gate_only` | FAIL | 未指向 docs-audit/SKILL.md 及其内部指令，且复制了基线、正式站、变更映射和统一 stamp 等执行细节。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230; fixture_sha256=aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6; output_sha256=2eb3c92c116b8cc705a40aaa8b584ae259a34f59ac7cbdcbc8128ac259f2603c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 选择 docs-audit 并返回 blocked，但未满足等效入口保留和仅引用 specialist gate 的路由要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230; fixture_sha256=aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6; output_sha256=272e4893ca5ac9b90838eaf7fa8d48d1b1d422254e0393e2894b26bb6cace7b1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 直接执行审计并判定不通过，未进行 docs-audit 路由识别。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill lane fails all three assertions.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-003-route-release-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6` from `agents/docs/test/docs-agent/evals/workspace/eval-003-route-release-audit`.
- Fixture SHA-256: `aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6`
- Prompt SHA-256: `099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9fbb92b16f91777ce613be24ad3cd630730cfccd4cce1cf1d33c3b6c917671d6`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `de5a2db0bd2b7f9e954e9508acd922a60bc65f454c61fbc72a9200f5a2156e7f`
- Metadata SHA-256: `d582bafa2b7d4e637ef2b4b71f14f435256d70c30e92f7097a43cd40dc9da750`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_equivalent_chain` | FAIL | With_skill does not recognize the fixture's confirmed release scope, version tag, changelog, release evidence, and audit request as an equivalent confirmation chain; it instead treats the documented artifacts as missing. |
| `routes_docs_audit` | FAIL | With_skill mentions re-running docs-audit but conditionally routes to docs-site-bootstrap and does not preserve and hand off the confirmed scope, tag, changelog, and evidence as required. |
| `references_audit_gate_only` | FAIL | With_skill does not point only to docs-audit/SKILL.md; it reproduces audit concepts such as base_ref, change-impact analysis, fact verification, and version stamping, and also introduces docs-site-bootstrap. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230; fixture_sha256=aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6; output_sha256=6d048f5e273aad70e994eef9ed8e7ce497b6dc7196b6a4ed90357ed7886cfb12; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Recognized an audit-related blockage and mentioned docs-audit, but contradicted the fixture's confirmed chain, introduced an alternate bootstrap route, and reproduced specialist audit details.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=099569afeec045caa3e4e020611c72b9def7b5897f52222810916bd2477fd230; fixture_sha256=aea5c9e95cc3674c80708ee78ba0276fef121e6d5652789edf0421371d054bf6; output_sha256=b21123997b5d99592462367fc7cd4cd2987ae78c1d336b1a562aea0b9e0ff94d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Performed a conventional release audit and reported missing repository evidence; did not identify or route the equivalent confirmed release-entry chain.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- All three with_skill assertions are unsatisfied.
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

# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-003-route-release-audit`

## Test Set / Fixture Version

- Fixture version: `cross-doc audit 2026-07-19`（fixture 未变化）
- 本轮触发：issue #131 将 `docs-audit` frontmatter description 扩展为同时覆盖 pre-tag release audit 与 post-tag release verification 后的 routing 复验（2026-07-20）
- Fresh run：仓库外隔离 scratch Git 仓库（session scratchpad `eval-131-e003/`）
- Source head: `6040de9`，即 PR #137（关闭 issue #131，含本次复验针对的 `docs-audit` description 变更）的 squash 合并 commit；PR #136（关闭 issue #132）已在其之前合并

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| accepts_equivalent_chain | PASS | PASS | 两条 `release-entry.md` 均明确包含 release scope（第 3 行）、版本 tag（第 4 行）、changelog（第 5 行）、release evidence（第 6 行）及审计请求（第 8–11 行）；两条 result 也均识别该入口链。 |
| routes_docs_audit | PASS | FAIL | with_skill 明确写出“已正确路由至 `docs-audit`”，并保留版本、changelog、release evidence 后声明由专项能力执行；without_skill 未选择 `docs-audit`，而是自行给出审计结论和检查清单。 |
| references_audit_gate_only | FAIL | FAIL | with_skill 仅提到“`docs-agent:docs-audit` 专项能力未提供”，没有指向 `docs-audit/SKILL.md` 或内部指令；without_skill 同样没有该 gate 引用，并自行展开审计检查与后续步骤。 |

未满足断言（with/without 任一 FAIL）：`routes_docs_audit`、`references_audit_gate_only`



## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `accepts_equivalent_chain`：PASS。逐项识别已确认 scope、`verified_version_tag: v0.4.0`、已审阅 changelog、契约/CI 证据与既有 `docs/site/` 为等效确认入口。
- `routes_docs_audit`：PASS。明确“选定 specialist：`docs-agent:docs-audit`”，保留版本与 release 证据，执行责任交给 specialist，router 停在 handoff。
- `references_audit_gate_only`：PASS。以“由 `docs-audit` 按其权威执行门禁自行核验”指向 specialist gate，未复制 base/target、确定性层、事实层、三态或统一盖章协议。

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- fresh candidate 读取 main 上当前 `docs-agent` router SKILL.md、Docs README 与 `docs-audit` 新 frontmatter description，仅做入口检查、分流与上下文保留。
- 边界说明：candidate 输出中出现的 pre-tag/post-tag phase 建议不作为本 comparison 的通过证据——phase 判定归 `docs-audit` specialist 权威 gate，且 fixture 只含 Markdown 字段、无可核验的实际 git tag；本 eval 只验证 router 分流行为。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：同一 prompt 与 pristine fixture 副本的本轮 fresh `without_skill`，在仓库外隔离 scratch Git 仓库运行，禁止读取宿主仓库、skill 文档与历史输出；未复用历史 baseline。
- baseline 能泛化识别审计意图，但路由到自拟的 “Release Documentation Specialist” 而非 canonical `docs-agent:docs-audit`，缺少权威 gate 指针，且复制了五项审计检查与 `ready`/`blocked` 输出协议，违反 router 只引用 gate 的边界。
- 独立 judge 确认 baseline 输出无 skill 文档污染迹象。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 with-skill assertion failure。
- 上一轮记录的 harness limitation（baseline 可见父仓库 git 状态）本轮已通过仓库外隔离 scratch Git 仓库消除。

## Next Steps

- 保持 router 只引用 specialist gate；后续 router 或 `docs-audit` 入口语义再变化时重新 fresh 验证。

## Runtime Artifact Policy

- candidate、baseline、judge verdict 与 transcript 仅保留在会话 scratchpad 的隔离 scratch 仓库中，不提交到 git。
