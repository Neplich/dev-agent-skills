# Eval Result: eval-002-empty-qa-directory-expands-cases

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`
- Test case: empty-qa-directory-expands-cases
- Workspace: `workspace/eval-2-empty-qa-directory-expands-cases`
- Review context: PR #204 / issue #196 eval assertion alignment fix round

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture base: repository commit `f808d82`, with the approved pointer-style `assertion_2` alignment in this fix round.
- Fixture: existing but empty `docs/qa/e2e/account/profile-settings/profile-form/` tree, target route/page/form files, and QA environment guidance.
- Validation date: `2026-08-01 09:57:18 +0800`.
- With-skill source: fresh candidate generated after fully reading `agents/qa/README.md`, `agents/qa/skills/qa-agent/SKILL.md`, the current `evals.json`, `eval_metadata.json`, and every fixture file.
- Without-skill source: fresh candidate generated from the same prompt and an independent fixture copy only; it did not read or apply the QA Agent README or target skill and did not reuse the with-skill candidate, old comparison, or historical baseline.

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL** (4/4 assertions exercised)
- No assertion was `NOT EXERCISED`.

Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | The with-skill candidate recognizes that the existing feature tree has no active TC, reusable flow, or case, does not treat the empty directory as coverage, and preserves the full `account/profile-settings/profile-form` path instead of falling back to a single-level directory. |
| `assertion_2` | PASS | It passes the target source files, QA indexes, environment guidance, confirmed `feature-update` scenario, and exploration authorization to the specialist; it declares the specialist's authoritative gates applicable without asking again for exploration permission or returning immediately blocked. |
| `specialist_gate_pointer` | PASS | It selects `spec-based-tester` and points to that specialist's authoritative E2E memory, platform-version, credential, execution-entry, PRD/TRD/implementation-plan, and blocked-condition gates without reproducing their internal protocol. |
| `assertion_6` | PASS | It keeps a single `spec-based-tester` primary route and does not run another QA skill or enter implementation repair. |

## With-Skill Behavior

The fresh candidate chooses `spec-based-tester` as the narrowest route for turning the confirmed feature update into traceable E2E acceptance evidence. It identifies the empty functional tree correctly, passes the targeted project and environment context downstream, describes the expected durable TC/index/script evidence, and keeps specialist execution rules behind the authoritative gate pointer.

## Fresh Without-Skill Baseline

The fresh baseline identifies the empty tree and proposes creating cases before execution, but it does not name a constrained repository specialist. It also expands platform-version, environment, and execution blocking details and suggests both exploratory and acceptance testing, so it lacks the router's single-route and pointer boundaries. This contrast supports the with-skill PASS without treating the baseline as a separate machine verdict.

## Failures

- None.
- The previous `assertion_2` failure is removed by aligning it with the router's specialist-gate pointer contract; the router is no longer required to reproduce specialist-internal test-command discovery details.
- No runtime, credential, or external-service blocker occurred.

## Next Steps

- No eval-specific correction is required.
- Retain the pointer-style assertion and keep specialist protocol details out of future `qa-agent` router candidates.

## Runtime Artifact Policy

- Fresh paired evidence is stored only under `tmp/eval-runs/pr-204-fix-round-20260801/qa-agent/eval-002-empty-qa-directory-expands-cases/`.
- The runtime directory contains independent `with_fixture/` and `without_fixture/` copies plus `with_skill.md`, `without_skill.md`, and `judge.md`.
- Runtime candidates, fixture copies, verdicts, transcripts, timing, status, diagnostics, and generated outputs are scratch artifacts and are not committed.
- The durable committed result is this `comparison.md` only.
