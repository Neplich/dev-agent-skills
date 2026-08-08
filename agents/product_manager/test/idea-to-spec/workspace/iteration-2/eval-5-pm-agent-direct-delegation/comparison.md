# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-005-pm-agent-direct-delegation`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/idea-to-spec/workspace/iteration-2/eval-5-pm-agent-direct-delegation`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `acbae9b70ef204aa5ea01807d9cde8c1bfaf036424605400b24871c7a447ebef`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9c3b136c6958582b2c5c3d552759bbe4fd3ef24876075804e91c5b21980a34af`
- Skill overlay SHA-256: `e4cc003a0e06320ef354c6c9cdbebb2b75980ec8b23ae530ac78b0667fab31da`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `073eeac01923328bf5fb812c3ab5852d6edb01936d4f17fc20c69c0d80324b2c`
- Metadata SHA-256: `2ddab779806f9b6e5f9359612bd5cef16f9b4ffd4913ec9f35576d1c0f06be89`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `dispatcher` | FAIL | with_skill 输出仅说明已完成界面原型及文件入口，没有进入 idea-to-spec 风格的上下文摘要或需求梳理。 |
| `skill` | PASS | with_skill 输出未出现询问是否唤起 idea-to-spec，也未要求手动执行 /pm-agent:idea-to-spec。 |
| `pm` | FAIL | with_skill 输出没有继续提炼产品定位、功能边界、MVP 或其他需求收敛问题。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acbae9b70ef204aa5ea01807d9cde8c1bfaf036424605400b24871c7a447ebef; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=ba59546534b59aee718d0080a36ff617cca5ef298d02ea020a388d1d3b336efe; snapshot_sha256=f7e0de486c3fb28105bea170994b3d378c81e8217206781df854888595429453
- Behavior: 直接交付 AI 对话助手原型，未进行上下文摘要、需求收敛或 PM 流程，也未反问是否调用子 skill。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acbae9b70ef204aa5ea01807d9cde8c1bfaf036424605400b24871c7a447ebef; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=3b8d670406e8cef69cf62ca8e927282929fe420db23e309da4d07e22781a3e1c; snapshot_sha256=3ef2f9c3979bee99b8614aa32ba1f532a9f37afdfce5886232a8e98ac8f03cf3
- Behavior: 直接交付 AI 对话助手界面实现，未进行需求梳理或 PM 流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- dispatcher 未满足：没有直接进入 idea-to-spec 风格的上下文摘要或需求梳理。
- pm 未满足：没有在同一轮继续进行产品定位、功能边界、MVP 或其他需求收敛。
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

# Eval Result: eval-005-pm-agent-direct-delegation

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; fresh paired manifests matched exactly.
- Behavior result: PASS — 3/3 assertions passed.
- Coverage result: FULL — all 3 assertion scenarios were exercised.
Overall result: PASS

### Assertion Results

- `dispatcher`: PASS — entered greenfield discovery directly instead of stopping at routing metadata.
- `skill`: PASS — did not ask the user to invoke `idea-to-spec` manually.
- `pm`: PASS — proposed an MVP-oriented product-positioning decision in the same turn.

### With-Skill / Baseline Comparison

The with-skill lane performed PM shaping without writing product code. The baseline directly created an HTML/CSS/JS prototype, providing clear behavioral separation.

### Failures / Next Steps

- No with-skill assertion failures and no coverage gaps.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-005-pm-agent-direct-delegation/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent` -> `idea-to-spec`
- Eval: `eval-005-pm-agent-direct-delegation`
- Workspace: `workspace/iteration-2/eval-5-pm-agent-direct-delegation`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; `/pm-agent` entry for a near-empty AI assistant product request.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-005-pm-agent-direct-delegation/`

## Latest Result

- Behavior result: PASS — all 3 assertions passed.
- Coverage result: FULL — 3/3 assertion scenarios were exercised; no `NOT EXERCISED` items.
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `dispatcher`: PASS — classifies through `pm-agent` and continues directly into `idea-to-spec` context shaping.
- `skill`: PASS — does not ask whether to invoke the specialist or require a manual command.
- `pm`: PASS — continues in the same turn with product-positioning and MVP-boundary discovery.

## With-Skill Behavior

The response selected `greenfield-discovery`, compared three product-positioning options, and stopped at one confirmation point. It describes the PM output as PRD/DECISIONS and contains no BRD generation, validation, or iteration behavior.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture, without reading or applying either target skill, Product Manager README, internal instructions, or historical comparison. It produced reasonable feature ideas but did not demonstrate dispatcher-to-specialist same-turn delegation or durable artifact ownership.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused no routing regression.

## Next Steps

- Keep this eval as coverage for direct PM delegation into the simplified PRD/DECISIONS chain.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-005-pm-agent-direct-delegation/` and are not committed.
