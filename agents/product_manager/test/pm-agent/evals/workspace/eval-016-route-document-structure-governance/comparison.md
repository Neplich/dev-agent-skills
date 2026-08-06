# Eval Result: eval-016-route-document-structure-governance

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-016-route-document-structure-governance`
- Workspace: `eval-016-route-document-structure-governance`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-016-route-document-structure-governance/`.

## Latest result:

- Behavior result: FAIL — determined only from the with-skill lane by an independent judge.
- Coverage result: PARTIAL — 4/5 with-skill assertion scenarios were exercised.
Overall result: FAIL

## Assertion Results

- `routes_to_structure_governance`: with-skill **PASS**; without-skill **NOT_EXERCISED** — with_skill trace 明确分类为 document_structure_governance，且读取的 pm-agent 路由表指定 idea-to-spec:structure-governance。
- `read_only_audit`: with-skill **PASS**; without-skill **PASS** — 两份最终回复及 trace 均声明只读检查；两份 status 的 added/removed/modified 均为空，且 result_manifest 与 fixture_manifest 一致。
- `report_form`: with-skill **FAIL**; without-skill **FAIL** — 两份最终回复都只提供 Markdown 对话内容；trace 中没有生成或写入 HTML 运行期 tmp 报告的工具调用。
- `scope_six_role_dirs`: with-skill **NOT_EXERCISED**; without-skill **NOT_EXERCISED** — fixture 实际仅包含 docs/pm 与 docs/engineer，缺少 design、qa、devops、security 实体，因此按规则标记为 NOT_EXERCISED。
- `structural_change_requires_confirmation`: with-skill **FAIL**; without-skill **FAIL** — with_skill trace/最终回复未说明合并、拆分、移动建议需用户确认、change_tier=major，或明确不在本次梳理中执行；without_skill 同样未覆盖该治理约束。

## With-Skill Behavior

正确识别并路由为 document_structure_governance，执行了只读扫描且没有文件变更；但未生成 HTML 运行期报告，也未在结论中落实 major/用户确认约束。六角色覆盖因 fixture 缺少实体而无法评估。

## Fresh Without-Skill Baseline

完成了基础只读目录检查且无文件变更，但没有可验证的结构治理路由、HTML 运行期报告或结构变更确认约束；六角色覆盖因 fixture 缺少实体而无法评估。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- with_skill 未生成 HTML 写入运行期 tmp 的报告。
- with_skill 未明确结构变更建议须用户确认并按 change_tier=major 另行执行。
- without_skill 同样未满足 HTML 报告形态和结构变更确认约束。

## Coverage Gaps

- fixture 仅有 pm、engineer 两个角色目录，design、qa、devops、security 缺失，六角色覆盖断言无法实际评估。

## Blockers

- None.

## Historical Result (Pre-#234)

- The previous durable result recorded Behavior **PASS**, Coverage **FULL**, and Overall **BLOCKED** after issue #234 identified prompt/fixture leakage.
- That pre-remediation result is retained only as history and is superseded by this strict fresh run.

## Next Steps

- Fix the with-skill failures listed above, then rerun this eval with the same strict isolation and independent-judge protocol.

## Runtime Artifacts Policy

- Candidate responses, traces, status manifests, isolation records, and judge evidence remain under the gitignored runtime path above and are not committed.
