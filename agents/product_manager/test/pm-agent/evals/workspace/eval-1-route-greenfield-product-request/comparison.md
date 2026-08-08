# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-001-route-greenfield-product-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-1-route-greenfield-product-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27bdda776386001cc566aec58e87a13d3b1f46246aed8961a6b1f71f6fe7164`
- Skill overlay SHA-256: `4c9723c1beabc3433045321f3b5731004dd2e67877c45ddeed6c79c96a17ba04`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6148645b04e0dacf3c4d3ef0529b8a742222f6ee577fdaccecfa0774adb9b043`
- Metadata SHA-256: `98a5616a9f22e4ba7d6ed10c98a36b572ccd9f5c0bfcfaf868ea982ef672635f`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `route_to_idea_to_spec` | FAIL | with_skill 输出未选择或提及 `idea-to-spec`，也未说明其产品发现、范围收敛和 spec 创建职责。 |
| `pm_first_guardrail` | FAIL | with_skill 输出未识别无 skip-PM override，也未提及 `pm-agent` 分类或禁止直跳工程执行。 |
| `context_to_collect` | FAIL | with_skill 输出未说明需要收集用户目标、核心流程、范围边界、验收标准和关键未决问题。 |
| `expected_pm_artifacts` | FAIL | with_skill 输出未声明 PRD、DECISIONS 或其他 PM 文档产物，也未说明由 `engineer-agent:trd-gen` 负责 TRD。 |
| `handoff_boundary` | FAIL | with_skill 输出未说明需求稳定后再交接给 `designer-agent` 或 `engineer-agent`。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=79b5c20d1670b837f55c74829538a9b598686950658f5a31c15b4ea8de473230; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别空目录并给出三个产品方向，推荐通用 AI 聊天助手；未包含要求的 route、PM guardrail、上下文收集、产物或 handoff 信息。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=6eaffe63a493e78443a8d8f3405c938d418dcdd711e419953485e824248842ce; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 直接提出 MVP 功能、排除项和技术方向，并询问三个产品问题；未提及任何技能 route 或 PM 交接边界。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出未满足全部五项断言。
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
