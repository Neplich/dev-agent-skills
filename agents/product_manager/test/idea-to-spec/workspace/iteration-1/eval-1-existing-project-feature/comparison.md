# Eval Result: eval-001-existing-project-feature-design

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-001-existing-project-feature-design`
- Test case: existing-project-feature-design
- Workspace: `workspace/iteration-1/eval-1-existing-project-feature`
- Latest result: PASS - fresh Codex subagent validation on 2026-06-23 after the feature_path doc-schema update

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Verifies that idea-to-spec handles existing-project-feature-design and produces the expected role-specific artifact.
- Expected output: 先给出项目上下文摘要，然后按单决策点推进设计；在关键点提供 2-3 个方案和 trade-off；按 section 逐段确认；把已确认内容沉淀到 docs/pm/{feature_path}/DECISIONS.md 与相关 PM 文档。
- Validation context: fresh Codex subagent semantic validation on 2026-06-23 after `prd-schema.md`, `brd-schema.md`, `test-spec-schema.md`, and `trd-schema.md` added explicit `feature_path` metadata requirements.

## Assertions

- `assertion_1`: 先做上下文检测
- `assertion_2`: 单决策点推进
- `assertion_3`: 关键点有选项比较
- `section`: 按 section 推进
- `assertion_5`: 文档作为记忆源

## With Skill

Observed behavior:

- The current `idea-to-spec` skill requires Phase 0 workspace/doc detection before formal design, then selects `existing-project-feature` for an existing repo adding a new capability.
- The skill contract requires one decision point per turn, 2-3 option trade-offs for meaningful design choices, section-based confirmation, and durable PM memory through `DECISIONS.md` / feature docs.
- The fixture is an existing web app with partial docs and an app-tags PM workspace, so the expected first-turn behavior is context summary, confirmation gate, and incremental PM design rather than final artifact generation.
- The feature_path schema update is compatible with this eval: `app-tags` is a valid level-1 `feature_path`, and any new or updated formal PM document for the feature must now carry `feature_path`, `feature`, `parent_feature`, and `feature_level`.

## Without Skill / Baseline

- Baseline behavior is diagnostic only.
- Without the skill contract, the likely risk is jumping straight to a complete solution or implementation plan before context detection, confirmation, and PM document memory are established.

## Failures

- None found in this fresh Codex subagent validation after the feature_path doc-schema update.
- No transcript, verdict, output, or diagnostics artifact was generated in this worker pass.

## Next Steps

- Keep deterministic checks focused on first-turn protocol. Add separate multi-turn or seeded artifact eval coverage if final `DECISIONS.md` / PRD generation needs automated verification against the feature_path frontmatter contract.

## Runtime Artifacts Policy

- No runtime artifacts were created in this worker pass. Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
