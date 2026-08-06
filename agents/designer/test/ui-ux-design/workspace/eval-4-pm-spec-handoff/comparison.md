# Eval Result: eval-004-pm-spec-handoff

## Evaluation Target

- Agent: `designer`
- Skill: `ui-ux-design`
- Eval: `eval-004-pm-spec-handoff`
- Test case: PM Spec Handoff Stops Before Implementation
- Workspace: `workspace/eval-4-pm-spec-handoff`

## Test Set or Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`
- Fresh run time: `2026-08-07 00:04:31 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/designer/ui-ux-design/eval-004-pm-spec-handoff/`
- Fixture: PRD, DECISIONS, TRD, current Settings shell/page; BRD fixture removed at current HEAD

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL** (3/3 assertions exercised)
Overall result: FAIL

## Assertion Results (Current)

- spec: **FAIL** — the candidate does not explicitly state that PM specs are design input only and do not authorize implementation.
- assertion_2: **FAIL** — ready-for-engineering-handoff is mentioned, but engineer-agent is not explicitly named as next owner.
- assertion_3: **PASS** — the fresh design artifact contains no code changes, implementation steps, test commands, or patch actions.

## With-Skill Behavior (Current)

The candidate creates the canonical billing notification UI/UX specification
and preserves source code, but omits both explicit boundary statements required
by the current assertions.

## Fresh Without-Skill Baseline (Current)

The baseline was generated first from the identical prompt and fixture in an
independent top-level workspace under isolated HOME/CODEX_HOME. It also stays
design-only and produces a differently named handoff file; it is comparison
evidence only.

## Failures (Current)

- Missing explicit PM-spec authorization boundary.
- Missing explicit engineer-agent next-owner handoff.

## Next Steps (Current)

- Align the completion response with the existing hard-boundary and completion criteria, then rerun.

## Runtime Artifact Policy (Current)

- Runtime lanes and judge evidence remain in independent /tmp workspaces and are not committed.
- Only this durable comparison is updated.

## Historical Result (Superseded: pre-#234 contract)

- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


All three assertions were exercised on the reachable design-generation path.

## Assertion Results

- `spec`: **PASS** — PRD, DECISIONS, TRD, and current UI context are explicitly treated as design input only, not implementation authorization.
- `assertion_2`: **PASS** — the candidate completes the design handoff and names `engineer-agent` as the next implementation owner.
- `assertion_3`: **PASS** — it contains no code edits, implementation steps, test commands, or patch actions.

## With-Skill Behavior

- Produces the canonical `docs/design/billing-notification-settings/ui-ux-spec.md` behavior with workspace-admin journey, event toggles, recipient alias, non-color urgent cues, loading/empty/save states, and reuse of the existing Settings shell.
- Respects the TRD warning not to hard-code unconfirmed API field assumptions.
- Reads only PRD/DECISIONS/TRD for product and technical context and never looks for or cites BRD. Removing BRD causes no assertion-level behavior difference.

## Fresh Without-Skill Baseline

- This baseline was newly generated in this run from only the same prompt and fixture files; it did not apply the Designer README, skill, with-skill result, historical baseline, or prior comparison.
- The explicit prompt keeps it code-free and it proposes similar settings controls, but it is less explicit about canonical artifact ownership and role boundaries.
- It also uses no BRD.

## Failures

- None.

## Next Steps

- No skill or fixture correction is required for the current assertions.

## Runtime Artifact Policy

- Runtime candidates, fresh baseline, and judge evidence remain under the ignored runtime directory and are not committed.
- Only this durable `comparison.md` is updated.
