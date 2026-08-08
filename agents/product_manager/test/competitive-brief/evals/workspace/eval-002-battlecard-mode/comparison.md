# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-002-battlecard-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/competitive-brief/evals/workspace/eval-002-battlecard-mode`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `70b4fbc3e06dc263b49c3b8be67b315a355580959b808022e5988e647e7d834c`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9bcbaea9ed44a65b8b7c8fe2503291ec2b4f93690b7975aa2c81cb08e3724567`
- Skill overlay SHA-256: `e16b71c2700d685342e052804fd5eb5278935b75eddc6e749594182c8bc24969`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e8a999a639bd228ca705a12ae8869ebeef2f7342c542af9c88de16ec2f2c6c41`
- Metadata SHA-256: `afa74db5ddc57d2d44d180de2fcf13cf3e54e4afa39e70bed4f98d234bbdaa99`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `battlecard_fields` | FAIL | with_skill 输出虽分为 Linear/Jira 两页并覆盖定位、强项、短板、发现问题、话术和 POC，但未明确提供 Quick Overview、Their Pitch、Objection Handling、Landmines to Set、Landmines to Defuse、Win/Loss Themes 等要求字段，且未形成每家完整单页字段结构。 |
| `no_full_brief` | PASS | with_skill 输出以两页 battlecard 形式组织，没有执行摘要、完整竞品画像、messaging gap 分析或机会/威胁/行动项等完整 brief 章节。 |
| `evidence_boundary` | PASS | with_skill 标注研究日期，区分“事实”与“假设/需验证”，并提供官方及第三方来源链接；对迁移、体验、合规、成本等不确定结论明确要求验证。 |
| `no_battlecard_offer` | PASS | with_skill 直接交付 Linear/Jira 资料，没有询问是否需要创建 battlecard，也未将其作为后续追加项。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=70b4fbc3e06dc263b49c3b8be67b315a355580959b808022e5988e647e7d834c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=d525782eb9a219d5e3e2603e0d027bf02448a2d100fc15bb3a59df307450a18c; snapshot_sha256=018a4d6d824aaea8de3928890bb086060be80aab2b9c1df2f0aed0a56795a307
- Behavior: 交付了两页 Linear/Jira 单页版竞争资料，证据边界和研究日期处理良好，但未按要求显式覆盖全部 battlecard 字段。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=70b4fbc3e06dc263b49c3b8be67b315a355580959b808022e5988e647e7d834c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=289309de145b545cf9f9cc4ca1f22bedd2b8cce814868bd3ba3373312f50f1c4; snapshot_sha256=67417e63bde5a4033ce4764817ca7ecac0ba0837e208fc8ee27fdbb9aa876bf1
- Behavior: 交付了两页 battlecard，字段覆盖较多并标注事实/假设，但包含 Discovery 问题且未完整满足指定 battlecard 字段清单。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未显式覆盖要求的完整 battlecard 字段集合。
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

# Eval Result: eval-002-battlecard-mode

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; both lanes used the same empty fixture manifest.
- Behavior result: PASS — 4/4 assertions passed.
- Coverage result: FULL — all 4 assertion scenarios were exercised.
Overall result: PASS

### Assertion Results

- `battlecard_fields`: PASS — each competitor received all required one-page battlecard fields.
- `no_full_brief`: PASS — the result stayed in battlecard mode and omitted the full-brief section chain.
- `evidence_boundary`: PASS — recorded the research date, linked source categories, and marked inference/validation boundaries.
- `no_battlecard_offer`: PASS — did not offer battlecard creation as a later step.

### With-Skill / Baseline Comparison

The with-skill lane directly returned the two requested battlecards. The baseline also produced battlecards but additionally wrote three workspace files, including its own README; the input manifest contained no README, so this was an output write rather than fixture leakage.

### Failures / Next Steps

- No with-skill assertion failures and no coverage gaps.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-002-battlecard-mode/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-002-battlecard-mode`
- Test case: battlecard-mode
- Workspace: `workspace/eval-002-battlecard-mode`
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

- Historical result: PASS

## Review Context

- Date: 2026-08-03（issue #188 Battlecard Mode 新增后 fresh 双侧验证）
- Judge: fresh Codex validation agent，双侧 candidate 冻结后独立判定（`tmp/eval-runs/issue-188-battlecard/judge/verdict.md`）

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: live 联网研究（Linear 与 Jira 官方公开页面），无静态 fixture

## Assertions

- PASS `battlecard_fields`：Linear/Jira 各产出单页 battlecard，Quick Overview / Their Pitch / Strengths / Weaknesses / Objection Handling / Landmines to Set / Landmines to Defuse / Win-Loss Themes 字段齐全；without-skill FAIL（未呈现 Their Pitch、双向 Landmines、Win/Loss Themes 等指定字段）
- PASS `no_full_brief`：未展开完整 brief 章节，只输出单页 battlecard；without-skill 同 PASS
- PASS `evidence_boundary`：标注研究日期、来源类别，逐项区分官方事实/第三方评价/推断/假设；without-skill 同 PASS
- PASS `no_battlecard_offer`：直接交付 battlecard，未再询问是否创建 battlecard；without-skill 同 PASS

## With Skill Behavior

- Battlecard Mode 生效：pm-agent `battlecard` 信号路由时直接产出两页单页 battlecard（字段齐全），不输出完整 brief，不询问是否创建 battlecard；研究日期与证据标签完整。

## Without Skill Baseline

- 来源：2026-08-03 fresh baseline（同 prompt，未读 skill）；3/4 assertions PASS（no_full_brief、evidence_boundary、no_battlecard_offer 被 baseline 内化，battlecard_fields 因缺指定字段 FAIL——唯一区分项）。
- 区分度：结构契约（单页字段清单）保持 skill 增量；范围与证据边界已被 baseline 内化。

## Failures / Findings

- 无 with-skill assertion failure；无 NOT EXERCISED；Coverage FULL。
- 零区分度观察（no_full_brief/evidence_boundary/no_battlecard_offer 被 baseline 白捡，3/4）：属模型通用审慎；Battlecard Mode 的增量在固定字段清单（battlecard_fields 保持区分度）。

## Next Steps

- 保留 Battlecard Mode 与 eval-002；后续修改这些规则时重新运行。

## Runtime Artifacts Policy

- 双侧 candidates 与 judge verdict 位于 `tmp/eval-runs/issue-188-battlecard/`（ignored 运行期目录，未提交）。
- 长期只保留本 `comparison.md`；不提交 transcript、candidate、verdict、timing、run status 或 diagnostics。
