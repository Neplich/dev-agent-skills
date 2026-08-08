# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `ui-ux-design`
- Eval: `eval-002-ecommerce`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `066b89d2cc1dd835345cd6d39e99316bc4d1c11f89b8739eb2d1941c8791d32f` from `agents/designer/test/ui-ux-design/evals/workspace/eval-002-ecommerce`.
- Fixture SHA-256: `066b89d2cc1dd835345cd6d39e99316bc4d1c11f89b8739eb2d1941c8791d32f`
- Prompt SHA-256: `eb90dbc90941b21fe1cf928c689f4703e38f536b24e4a881de504f524de89ea3`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `78da31c45df217a9e90f29e80573d99066d6964c62a108fc4cb609c96341db51`
- Skill overlay SHA-256: `b9db71f44c6cca6e399d27edcc8fe58463a8d7a3c9a80f1728f1e7571f16e7df`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `931b5a68d664b4bafde7712fdb59980628e60528384f0dba2478ad10661f14cd`
- Metadata SHA-256: `40409fe16f5c840772ed9dc96d9a9bf18f86662171fdae939c0a1ec6acbc3c28`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 的交付文档明确采用 mobile-first，并覆盖商品列表、移动端筛选抽屉、商品详情、购物车及其数量调整、移除、撤销、价格汇总和状态反馈。 |
| `assertion_2` | PASS | with_skill 输出是设计规格文档，包含布局原型、页面清单、交互行为、状态和响应式规则；未包含代码、文件补丁、命令行步骤或实现任务拆解。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=eb90dbc90941b21fe1cf928c689f4703e38f536b24e4a881de504f524de89ea3; fixture_sha256=066b89d2cc1dd835345cd6d39e99316bc4d1c11f89b8739eb2d1941c8791d32f; output_sha256=53f10ebe9e50260f11033bab36ce4d7db3d9c5c8747b1e8966c1fd961a578c0a; snapshot_sha256=6ec1e29b37ee8a9ed00f46997797e27de6acaaec02a8b721a207427b8b13ea39
- Behavior: 满足两项断言，设计规格对 mobile-first 布局、筛选和购物车交互覆盖更明确，并保持在设计范围内。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=eb90dbc90941b21fe1cf928c689f4703e38f536b24e4a881de504f524de89ea3; fixture_sha256=066b89d2cc1dd835345cd6d39e99316bc4d1c11f89b8739eb2d1941c8791d32f; output_sha256=fa314cde7c2130dde3e9525de7487a08bed7a6336e5ad9f31cf65932ec5a0189; snapshot_sha256=b7e8e87ff87323e5e31f4436b9ffedb579f3e587e309b3cefa28c4b403b9b644
- Behavior: 满足两项断言，已交付覆盖列表、筛选、详情、购物车的 mobile-first 设计文档。
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

# Eval Result: eval-002-ecommerce

## Evaluation Target

- Agent: `designer`
- Skill: `ui-ux-design`
- Eval: `eval-002-ecommerce`
- Test case: E-commerce Product Page
- Workspace: `workspace/eval-002-ecommerce`

## Test Set or Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`
- Fresh run time: `2026-08-07 00:04:31 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/designer/ui-ux-design/eval-002-ecommerce/`
- Fixture: confirmed PM handoff and PRD for `handmade-crafts-store`

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL** (2/2 assertions exercised)
Overall result: PASS

## Assertion Results (Current)

- assertion_1: **PASS** — the new ui-ux-spec.md is mobile-first and covers listing, filters, product detail, cart, and required states.
- assertion_2: **PASS** — the output contains design specifications only, with no code, patch, command, or engineering task decomposition.

## With-Skill Behavior (Current)

The candidate generates the canonical feature-path artifact with mobile-first
journey, ASCII layouts, components, state behavior, responsive rules, and
accessibility constraints while staying within Designer scope.

## Fresh Without-Skill Baseline (Current)

The baseline was generated before the with-skill root existed, using the same
prompt and clean fixture in an independent top-level workspace with isolated
HOME/CODEX_HOME. It also satisfies the two broad assertions, so this eval has
low differentiation but no with-skill regression.

## Failures (Current)

- None.

## Next Steps (Current)

- Keep this case; consider future assertion review if maintainers want stronger skill-specific differentiation.

## Runtime Artifact Policy (Current)

- Runtime lanes and judge evidence remain in independent /tmp workspaces and are not committed.
- Only this durable comparison is updated.

## Historical Result (Superseded: pre-#234 contract)

- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


Both assertions were exercised on the reachable design-generation path.

## Assertion Results

- `assertion_1`: **PASS** — the candidate covers the mobile-first listing, filter drawer, detail, cart, quantity/removal, loading, empty-result, out-of-stock, and feedback states.
- `assertion_2`: **PASS** — the candidate contains no code, patch, command, or engineering task decomposition.

## With-Skill Behavior

- Produces the canonical `docs/design/handmade-crafts-store/ui-ux-spec.md` behavior with journey, page inventory, phone-first ASCII layouts, interaction states, 44px touch targets, and responsive expansion.
- Stops at Designer handoff and routes implementation to Engineer.
- Uses only PM handoff and PRD product inputs; no BRD is requested or cited, and its removal causes no tested behavior difference.

## Fresh Without-Skill Baseline

- This baseline was newly generated in this run from only the same prompt, PM handoff, and PRD; it did not apply the Designer README, skill, with-skill output, old baseline, or prior comparison.
- It satisfies the broad mobile flow and design-only requirements but is less complete in canonical structure, boundary-state coverage, and repository handoff discipline.
- It contains no BRD reference.

## Failures

- None.

## Next Steps

- No skill or fixture correction is required for this case.

## Runtime Artifact Policy

- Runtime candidates, fresh baseline, and judge evidence remain under the ignored runtime directory and are not committed.
- Only this durable `comparison.md` is updated.
