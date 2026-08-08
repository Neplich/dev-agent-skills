# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-003-greenfield-discovery`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a4faa6eb1bc545a0fcd2b0f3491c8b376050fe70e6b532b62cd5d45f16655b85` from `agents/product_manager/test/idea-to-spec/workspace/iteration-1/eval-3-greenfield-discovery`.
- Fixture SHA-256: `a4faa6eb1bc545a0fcd2b0f3491c8b376050fe70e6b532b62cd5d45f16655b85`
- Prompt SHA-256: `0af25e0d51f2fb040654e6f1d54a6ad79ea082de53fb485f0d81b3fe8a3d6ee6`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9c3b136c6958582b2c5c3d552759bbe4fd3ef24876075804e91c5b21980a34af`
- Skill overlay SHA-256: `e4cc003a0e06320ef354c6c9cdbebb2b75980ec8b23ae530ac78b0667fab31da`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `c665f0cae1373d04b176b75bc723732674aeb9f3630f01eadac8f7310d65bdb7`
- Metadata SHA-256: `aa700f49d0f32cf47f3b535bd526e4ad2ade501da428e296936ddccef0bcdcbd`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 仅提出探索问题并给出选项，没有输出完整 PRD 或 TRD。 |
| `assertion_2` | PASS | with_skill 聚焦一个决策点：优先解决哪类团队知识问题，并要求用户回复 1/2/3 或描述真实场景。 |
| `assertion_3` | NOT_EXERCISED | 当前方向尚未稳定，with_skill 尚未进入推荐 PRD 或其他下游文档动作的阶段；因此无法验证稳定后是否会推荐。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0af25e0d51f2fb040654e6f1d54a6ad79ea082de53fb485f0d81b3fe8a3d6ee6; fixture_sha256=a4faa6eb1bc545a0fcd2b0f3491c8b376050fe70e6b532b62cd5d45f16655b85; output_sha256=3fbbe6c42e0f70e98107702bc571aafbc582d1c4504af297a0b7292c0a74faf8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 聚焦单一决策点，以编号选项推动团队知识问答方向收敛，未提前文档化。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0af25e0d51f2fb040654e6f1d54a6ad79ea082de53fb485f0d81b3fe8a3d6ee6; fixture_sha256=a4faa6eb1bc545a0fcd2b0f3491c8b376050fe70e6b532b62cd5d45f16655b85; output_sha256=22979128a3635af5987803b5e11c7cdac14f3b2c3b8425e0809796bade6cf61e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 未直接写完整 PRD，但一次提出 6 个问题，探索范围较宽。
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

# Eval Result: eval-003-greenfield-discovery

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; fresh paired manifests matched exactly.
- Behavior result: PASS — 3/3 assertions passed.
- Coverage result: FULL — all 3 assertion scenarios were exercised.
Overall result: PASS

### Assertion Results

- `assertion_1`: PASS — no PRD or TRD was generated in the first turn.
- `assertion_2`: PASS — one core product-scenario decision was presented with options and a recommendation.
- `assertion_3`: PASS — the response correctly stayed in discovery until the direction stabilizes.

### With-Skill / Baseline Comparison

The with-skill response stayed in `greenfield-discovery` and advanced one decision. The baseline also avoided a PRD but asked five questions and presented five routes at once.

### Failures / Next Steps

- No with-skill assertion failures and no coverage gaps.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-003-greenfield-discovery/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-003-greenfield-discovery`
- Workspace: `workspace/iteration-1/eval-3-greenfield-discovery`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; near-empty knowledge Q&A workspace with minimal notes, no formal PM docs, and no selected stack.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-003-greenfield-discovery/`

## Latest Result

- Behavior result: PASS — all 3 assertions passed.
- Coverage result: FULL — 3/3 assertion scenarios were exercised; no `NOT EXERCISED` items.
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `assertion_1`: PASS — does not generate a full PRD or TRD in the first turn.
- `assertion_2`: PASS — selects `greenfield-discovery` and asks one use-case decision.
- `assertion_3`: PASS — defers PRD/DECISIONS formalization until direction stabilizes.

## With-Skill Behavior

The response explicitly avoided assumptions about users, sources, permissions, and metrics, compared three primary-use-case options, and stopped at one confirmation point. The post-discovery artifact chain is PRD plus DECISIONS; no BRD stage appears.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It avoided an immediate PRD but asked several discovery questions in parallel and did not make lane or durable-memory timing explicit.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused no behavioral regression.

## Next Steps

- Keep this eval as coverage for greenfield discovery discipline and direct PRD/DECISIONS formalization after scope stability.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-003-greenfield-discovery/` and are not committed.
