# Eval Result: eval-001-route-greenfield-product-request

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-001-route-greenfield-product-request`
- Workspace: `eval-1-route-greenfield-product-request`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-001-route-greenfield-product-request/`.

## Latest result:

- Behavior result: FAIL — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 5/5 with-skill assertion scenarios were exercised.
Overall result: FAIL

## Assertion Results

- `route_to_idea_to_spec`: with-skill **FAIL**; without-skill **FAIL** — with_skill 最终回复未明确选择 `idea-to-spec` 或说明其职责；without_skill 同样未路由。
- `pm_first_guardrail`: with-skill **FAIL**; without-skill **FAIL** — with_skill 说明停留 PM 发现阶段但未明确无 skip-PM override 或返回 `pm-agent` 分类；without_skill 也未作该分类。
- `context_to_collect`: with-skill **PASS**; without-skill **FAIL** — with_skill 覆盖产品概念/目标、核心流程、MVP 与非目标、验收标准及待确认问题；without_skill 有部分问题清单，但缺少明确验收标准和完整核心流程。
- `expected_pm_artifacts`: with-skill **FAIL**; without-skill **FAIL** — with_skill 提到 PRD，但未声明 DECISIONS，也未说明 TRD 由 `engineer-agent:trd-gen` 负责；without_skill 未声明这些 PM 产物或 TRD 边界。
- `handoff_boundary`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确只有 PRD 稳定后才进入设计或工程阶段，满足稳定需求后的设计/工程交接边界；without_skill 未明确稳定需求后的 agent handoff。

## With-Skill Behavior

最终回复完成了 PM 需求发现、范围收敛、流程、验收和待决策整理，且未写代码；但缺少明确的 `idea-to-spec` 路由、pm-agent guardrail 分类，以及 DECISIONS/TRD 与 `engineer-agent:trd-gen` 的产物边界。status 显示无新增、删除或修改，trace 仅读取 pm-agent skill 和目录，没有外部 mutation。

## Fresh Without-Skill Baseline

回复停留在需求讨论且无文件写入，但未给出要求的 PM 路由、guardrail、PM 产物/TRD 边界，也未完整覆盖下游上下文与正式 handoff。status 显示无文件变化；trace 无工具调用。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- with_skill 未明确选择 `idea-to-spec` 主 route。
- with_skill 未明确说明空目录无 skip-PM override 并返回 `pm-agent` 正常分类。
- with_skill 未声明 DECISIONS 及 `engineer-agent:trd-gen` 负责 TRD。
- without_skill 未满足指定 PM 路由、guardrail、产物边界和完整下游上下文要求。

## Coverage Gaps

- None.

## Blockers

- None.

## Historical Result (Pre-#234)

- The previous durable result recorded Behavior **PASS**, Coverage **FULL**, and Overall **BLOCKED** after issue #234 identified prompt/fixture leakage.
- That pre-remediation result is retained only as history and is superseded by this strict fresh run.

## Next Steps

- Fix the with-skill failures listed above, then rerun this eval with the same strict isolation and independent-judge protocol.

## Runtime Artifacts Policy

- Candidate responses, traces, status manifests, isolation records, and judge evidence remain under the gitignored runtime path above and are not committed.
