# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-001-route-formal-docs-sync`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991` from `agents/docs/test/docs-agent/evals/workspace/eval-001-route-formal-docs-sync`.
- Fixture SHA-256: `5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991`
- Prompt SHA-256: `898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9fbb92b16f91777ce613be24ad3cd630730cfccd4cce1cf1d33c3b6c917671d6`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b427d27a75859a314db7ebafb8d73a16d8b21552e3c670e89632076d71f7b750`
- Metadata SHA-256: `320948f19ccb8c159c24fdc827ddc592aac02ee3f64236dd9e4896bae8e4979e`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | With-skill output selects `formal-docs-sync` for the confirmed delivery handoff and does not route to bootstrap, release notes, or audit. |
| `preserves_handoff_context` | FAIL | It preserves most core context, but omits fixture fields including `feature`, `parent_feature`, `feature_level`, and the explicit feature-path evidence reason. |
| `points_to_authoritative_gate` | FAIL | It names `formal-docs-sync` but does not explicitly point to `formal-docs-sync/SKILL.md` or its internal instructions as the authoritative contract. |
| `stops_at_router_boundary` | PASS | The output states the routing stage does not modify formal documents, and raw git evidence shows no changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=8070ecf97bc66a95e8b08bfdbda48dac77d552a91243b44c32195656a0ae9cb2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly selects `formal-docs-sync` and stops at the routing boundary, but incompletely preserves all handoff fields and does not cite the specialist SKILL.md contract.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; output_sha256=bbeac4491430ff2e607febe72ab7ce9154d4dc3a06e63d0d83b599de26cbcfab; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Routes generally toward delivery/API documentation and preserves much handoff context, but does not identify the required `formal-docs-sync` capability.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output omits several confirmed handoff fields.
- The with-skill output does not explicitly identify `formal-docs-sync/SKILL.md` and its internal instructions as the authoritative execution contract.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-001-route-formal-docs-sync`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991` from `agents/docs/test/docs-agent/evals/workspace/eval-001-route-formal-docs-sync`.
- Fixture SHA-256: `5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991`
- Prompt SHA-256: `898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9fbb92b16f91777ce613be24ad3cd630730cfccd4cce1cf1d33c3b6c917671d6`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b427d27a75859a314db7ebafb8d73a16d8b21552e3c670e89632076d71f7b750`
- Metadata SHA-256: `320948f19ccb8c159c24fdc827ddc592aac02ee3f64236dd9e4896bae8e4979e`
- Executor SHA-256: `c5ece8c6632badb84ff79ee67e4bea96a1d1db7e8afd66de87486af43e8fdd16`
- Runtime SHA-256: `5c4532cfa9ada91c16b3ae2d69922296ddc7c2c1c61841e01bc9c804be1b85fe`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_to_formal_docs_sync` | PASS | with_skill 明确选择 `formal-docs-sync`，并标注为 Feature delivery；未误派 bootstrap、release notes 或 audit。 |
| `preserves_handoff_context` | FAIL | 虽保留了功能、主要依据、同步范围、排除范围和风险，但遗漏了交接中的具体来源路径与状态、parent feature/level、feature-path 证据理由、downstream owner 及实现 diff/测试证据可供核验等字段，未达到无损保留。 |
| `points_to_authoritative_gate` | FAIL | 输出只说由 `formal-docs-sync` 处理，没有明确指向 `formal-docs-sync/SKILL.md` 或其内部指令作为权威执行合同。 |
| `stops_at_router_boundary` | PASS | 明确说明仅完成能力交接与范围确认，尚未执行文档写入；候选输出也没有修改 `docs/site/` 的证据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确完成 formal-docs-sync 路由并停在路由边界，但上下文保留不完整，且未指向 specialist 的权威 SKILL.md 合同。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=898aa52a50fa14b6ed2119a9c317cdc1f3e3e5286bf4d35a0cdd450c4352f602; fixture_sha256=5bfe584ec04ca9f6271a87eb0a6a94432a493cce40c865cd7e77c63d4d5a5991; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 新鲜基线错误路由至 `delivery`，但大部分交接字段和未写入边界得到保留。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未无损保留 pm-handoff.md 的全部已提供交接字段。
- 未明确指向 formal-docs-sync/SKILL.md 及其内部指令作为权威执行合同。
- Next: 补充完整的 handoff 字段与具体来源证据。
- Next: 明确将 formal-docs-sync/SKILL.md 及其内部指令作为后续执行权威。

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
- Eval: `eval-001-route-formal-docs-sync`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- 评估基线：`a273a00` 加本轮 cross-doc sync R2 working tree
- Harness：完整 `agents/docs/` 与 PM 共享契约；without-skill 零 skill/README；独立 fresh judge

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
| `routes_formal_docs_sync` | PASS | PASS | 两条 `result.txt` 均选择 `docs-agent:formal-docs-sync`，并明确排除 database、ops、Release；with_skill 第 3–8 行，without_skill 第 3–4 行。 |
| `accepts_complete_handoff` | FAIL | FAIL | with_skill 仅说明依据为 `pm-handoff.md` 及路径，未保留全部 packet 字段；without_skill 未说明接受完整 handoff，且只报告更新了阻塞项。完整字段虽存在于各自 `pm-handoff.md`，但未在路由产物中完整体现。 |
| `references_specialist_gate_only` | FAIL | FAIL | 两条产物均未指向 `formal-docs-sync/SKILL.md` 及其内部指令；仅称专家流程不可用。 |
| `recognizes_shared_consumption_contract` | FAIL | FAIL | 两条产物均未提及 `agents/product_manager/skills/idea-to-spec/_internal/_shared/consumption-contract.md`，也未给出该权威指针。 |

未满足断言（with/without 任一 FAIL）：``accepts_complete_handoff``、``references_specialist_gate_only``、``recognizes_shared_consumption_contract``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `routes_formal_docs_sync`：PASS。识别实现后正式文档同步，排除 bootstrap 与 audit。
- `accepts_complete_handoff`：PASS。保留 request_type、change_tier、全部 feature scope、source/scope/output/risk 字段。
- `references_specialist_gate_only`：PASS。只指向 `formal-docs-sync/SKILL.md` 及内部指令，不复制执行协议。
- `recognizes_shared_consumption_contract`：PASS。仅保留 PM 共享 `consumption-contract.md` 的权威指针。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：同一 prompt 与 fixture 全新生成，不含 skill/README，未复用历史 baseline。
- baseline 路由方向正确，但未逐字段保留 packet，也缺少 consumption contract 权威指针。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure；router pristine/with_skill 仅新增 candidate output，没有 specialist 执行产物。

## Next Steps

- 后续 router eval 继续使用完整 harness 与独立 judge。

## Runtime Artifact Policy

- 运行期产物仅保留在 `tmp/eval-runs/116/`，不提交到 git。
