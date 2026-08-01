# Eval Result: eval-003-engineer-ui-maintenance-handoff

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-003-engineer-ui-maintenance-handoff`
- Workspace: `workspace/eval-003-engineer-ui-maintenance-handoff`
- Review context: issue #196 L2-4 router single-table convergence
- Latest run: fresh paired Codex validation on 2026-07-31

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt and assertions: current `agents/designer/test/designer-agent/evals/evals.json`
- Fixture documents: approved PRD and TRD for `customer-portal/profile-settings`
- With-skill source: current Designer README, `designer-agent/SKILL.md`, eval definition, fixture, and the referenced PM handoff/closeout contract; historical comparison was not read before candidate generation.
- Without-skill source: the same prompt and fixture in an isolated directory, without reading or applying Designer README, `designer-agent/SKILL.md`, with-skill output, assertions, historical comparison, or an old baseline.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL (5/5 declared assertions exercised)
- Overall result: PASS

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
