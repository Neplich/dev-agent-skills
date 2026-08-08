# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-003-engineer-ui-maintenance-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `821c99c85df4188cff291d55bb3f776ec720f8cbbd3f93df4bf7a03b6520bf3a` from `agents/designer/test/designer-agent/evals/workspace/eval-003-engineer-ui-maintenance-handoff`.
- Fixture SHA-256: `821c99c85df4188cff291d55bb3f776ec720f8cbbd3f93df4bf7a03b6520bf3a`
- Prompt SHA-256: `92f4c4b043cb3aab774531019133e8d4e6f2d81d21a277f0cd9696a8cc0a58e7`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `516410461bd0c09f36f48a72fcff5f04e02a1fd7c3d7bf7c66ee6407ed3b789c`
- Skill overlay SHA-256: `a88badd5c39e8c98568ff4259ca011c27bd894b06440948f3ff19d0b8276099f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `138aebdae4a1049db8b791a6754cc321fff06d447fcae99b0206d1d5aa26e929`
- Metadata SHA-256: `f547a888a015d9e9862374a63fae63a3c03679e1e0f3c3c280b9cf0370c3b020`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_engineer_design_handoff` | FAIL | with_skill 输出仅说明可交给前端实现，未识别 engineer-agent 来源或 UI maintenance / frontend-update design handoff。 |
| `uses_confirmed_feature_path` | PASS | 两个设计产物均使用 customer-portal/profile-settings，并在 frontmatter 中引用对应 PM PRD 与 Engineer TRD。 |
| `routes_design_skills` | PASS | with_skill 产出分别覆盖信息层级/页面结构的 ui-ux-spec.md 与主按钮视觉规范的 visual-system.md；技能可见性证据包含 ui-ux-design 和 visual-design。 |
| `writes_design_outputs_only` | PASS | with_skill 仅新增 docs/design/customer-portal/profile-settings/ui-ux-spec.md 和 visual-system.md，未修改代码、测试或配置。 |
| `hands_back_to_engineer` | FAIL | 输出仅称交给前端实现，未说明 handoff 回 engineer-agent，也未明确由 Engineer 继续 TRD、IMPLEMENTATION_PLAN、code、test。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=92f4c4b043cb3aab774531019133e8d4e6f2d81d21a277f0cd9696a8cc0a58e7; fixture_sha256=821c99c85df4188cff291d55bb3f776ec720f8cbbd3f93df4bf7a03b6520bf3a; output_sha256=650895da511f79b0ea4fd0324a4284f4680acbf163db616d6105cfe9a8562337; snapshot_sha256=a8d2ec864498fe8195407ce69031a60a9ecac0106859a80b9113d1f2e6e45eba
- Behavior: 产出限定路径下的 UI/UX 与视觉系统设计文档，仅做设计交付，但未明确 engineer-agent 路由及回交责任。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=92f4c4b043cb3aab774531019133e8d4e6f2d81d21a277f0cd9696a8cc0a58e7; fixture_sha256=821c99c85df4188cff291d55bb3f776ec720f8cbbd3f93df4bf7a03b6520bf3a; output_sha256=0019d45a30ffa1bc63e05955568c6ed9e13db8b44602ebdea0d1cc7603a3b5ea; snapshot_sha256=040cbde6dcb83313513d984410470b5765f8732825dd921f1271c9a4a0323313
- Behavior: 基线新增通用 DESIGN.md，并修改 Engineer TRD；未使用限定的两个设计产物路径。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未明确识别 engineer-agent 的 UI maintenance / frontend-update design handoff。
- 未明确 handoff 回 engineer-agent 并交代后续 TRD / IMPLEMENTATION_PLAN / code / test 由 Engineer 继续。
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

# Eval Result: eval-003-engineer-ui-maintenance-handoff

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-003-engineer-ui-maintenance-handoff`
- Workspace: `workspace/eval-003-engineer-ui-maintenance-handoff`
- Review context: issue #196 L2-4 router single-table convergence
- Latest run: fresh isolated paired Codex validation and independent judge on 2026-08-07

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt and assertions: current `agents/designer/test/designer-agent/evals/evals.json`
- Fixture documents: approved PRD and TRD for `customer-portal/profile-settings`
- With-skill source: current Designer README, `designer-agent/SKILL.md`, eval definition, fixture, and the referenced PM handoff/closeout contract; historical comparison was not read before candidate generation.
- Without-skill source: the same prompt and fixture in an isolated directory, without reading or applying Designer README, `designer-agent/SKILL.md`, with-skill output, assertions, historical comparison, or an old baseline.

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL** (5/5 declared assertions exercised)
Overall result: FAIL

## Assertion Results (Current)

- accepts_engineer_design_handoff: **FAIL** — the final response does not identify the request as an Engineer-sourced UI maintenance handoff.
- uses_confirmed_feature_path: **FAIL** — the final response does not cite customer-portal/profile-settings or its aligned PRD/TRD.
- routes_design_skills: **PASS** — information hierarchy routes to ui-ux-design and the primary button rule to visual-design.
- writes_design_outputs_only: **FAIL** — no design deliverable is generated; the response blocks on allegedly unavailable specialists.
- hands_back_to_engineer: **FAIL** — no explicit return to engineer-agent for TRD, plan, code, and tests.

## With-Skill Behavior (Current)

The candidate selects the correct specialists but falsely treats them as
unavailable, then omits the confirmed path, deliverables, Engineer-handoff
classification, and required return path.

## Fresh Without-Skill Baseline (Current)

The baseline was regenerated before the with-skill root existed, using the same
prompt and fixture under an isolated HOME/CODEX_HOME. It produced a generic
UI-SPEC.md and did not satisfy the router contract; it remains comparison input only.

## Failures (Current)

- Four of five router assertions fail; only specialist selection passes.

## Next Steps (Current)

- Correct installed-specialist availability handling and preserve the Engineer handoff packet in the response, then rerun.

## Runtime Artifact Policy (Current)

- Runtime lanes and judge evidence remain in independent /tmp workspaces and are not committed.
- Only this durable comparison is updated.

## Historical Result (Superseded: pre-#234 contract)

- Behavior result: PASS
- Coverage result: FULL (5/5 declared assertions exercised)
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


This Engineer handoff has a confirmed path and explicitly names both information hierarchy and primary-button visual rules. It matches the dedicated Engineer UI maintenance route and does not exercise the separate “范围已确认但设计类型模糊” fallback.

## Assertion Results

| Assertion | With skill | Without skill | Evidence |
| --- | --- | --- | --- |
| `accepts_engineer_design_handoff` | PASS | FAIL | With skill explicitly classifies an `engineer-agent` UI maintenance design handoff; baseline directly writes generic design guidance. |
| `uses_confirmed_feature_path` | PASS | PASS | Both retain `customer-portal/profile-settings`; with skill also states that it reads the aligned PRD/TRD. |
| `routes_design_skills` | PASS | FAIL | With skill routes information hierarchy to `ui-ux-design` and button rules to `visual-design`; baseline names neither specialist. |
| `writes_design_outputs_only` | PASS | FAIL | With skill names only the two canonical design files and excludes engineering work; baseline supplies design prose but no canonical artifact path. |
| `hands_back_to_engineer` | PASS | PASS | Both return the design result to Engineer; with skill additionally names `engineer-agent` and its downstream ownership. |

## With-Skill Behavior

The candidate recognizes the request as an Engineer-sourced frontend UI design
gap, preserves the confirmed path, selects both appropriate design specialists,
names the two allowed design artifacts, excludes code/tests/commands/config and
implementation lists, and returns implementation to `engineer-agent`. All 5
assertions pass.

## Without-Skill Baseline

The fresh baseline produces plausible design guidance and returns it to
Engineer, but it bypasses the repository router contract: it does not classify
the handoff, select the two specialist skills, or name the canonical durable
files. It also introduces fixed layout and component values in prose, further
showing that generic design guidance is not equivalent to the router's scoped
design handoff.

## Failures

- None in the with-skill candidate.

## Next Steps

- Keep this eval as regression coverage for the dedicated Engineer UI maintenance handoff route and its design-only boundary.
- A confirmed-scope but genuinely ambiguous design request would require a separate fixture; it was not fabricated in this run.

## Runtime Artifacts Policy

Paired runtime evidence is stored only under
`tmp/eval-runs/issue-196-l2-3-4/designer-agent/eval-003-engineer-ui-maintenance-handoff/`
as `with_skill/candidate-output.md` and
`without_skill/baseline-output.md`. Runtime outputs, transcripts, verdicts,
timing data, and diagnostics must not be committed. This `comparison.md` is the
durable result.
