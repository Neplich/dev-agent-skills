---
name: exploratory-tester
description: "Internal QA specialist—not a direct entry point. Invoked by qa-agent after pm-agent handoff to explore changed product surfaces, environmental risks, and nearby failure modes with evidence-backed charters."
visibility: internal
---

# Exploratory Tester

Use this skill to discover defects through guided exploration, not to generate random UI actions. The exploration strategy is chosen only after reading the product context, implementation changes, and environment instructions. The output is an exploratory QA report plus, when warranted, a defect-ready escalation path.

## Shared QA Directory Contract

For E2E or feature-scoped QA, use the function-tree directory as durable QA
memory:

`docs/qa/e2e/{feature_path}/`

- `TEST_SUITE.md` is the suite index and coverage summary.
- `FLOW_INDEX.md` records reusable flows, source/config clues, routes, pages,
  APIs, states, TC mapping, and coverage implications.
- `cases/` stores reusable test cases. Every E2E case produced or expanded by
  exploration must be one Markdown file:
  `cases/TC-NNN-<short-slug>.md`.
- `scripts/` stores matching repeatable steps or executable snippets:
  `scripts/TC-NNN-<short-slug>.spec.md`.
- `results/` and `_reports/` store versioned execution evidence and summary
  reports.

Exploration should supplement this function-tree memory instead of re-reading
the entire project on every standalone QA run. Existing equivalent flows should
be updated in place; do not create duplicate synonym TC.

## When to Use

- After implementation changes when you need discovery beyond scripted coverage
- When the team wants exploratory QA against a changed surface or risky workflow
- When prior QA reports, known bugs, or environment notes suggest adjacent risk
- When the user asks for exploratory testing, discovery testing, or broad defect hunting

## Role Boundary

- This skill performs exploratory discovery, not spec validation
- This skill does not write bug tickets itself
- This skill does not dump generic browser-script output without interpretation

## PM Handoff Entry Gate

Before exploring, require a PM/QA handoff packet or equivalent confirmed QA
scope. If the user directly invokes this specialist without PM handoff context,
an existing QA memory scope, or a confirmed exploration target, return the
request to `pm-agent` for classification instead of expanding broad discovery.

Use the PM-side packet definition in
`agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.

## Exploration Preflight

Before any testing action, gather the context needed to choose an exploration charter:

1. Read existing QA memory first when available:
   `docs/qa/e2e/{feature_path}/TEST_SUITE.md`,
   `FLOW_INDEX.md`, `cases/*.md`, `scripts/*.spec.md`, relevant `results/`,
   and `_reports/`.
2. Read the PM or release context for the feature, scope, and intended user
   value.
3. Read implementation notes, changed files, or the equivalent change summary
   to identify the exact surface that moved.
4. Read known bugs, risk notes, and prior QA reports so exploration can target
   realistic failure modes.
5. Read environment instructions that affect how the app should be exercised,
   including setup, auth, feature flags, test accounts, or required services.

If any of the above is missing, note the gap and make the smallest safe assumption needed to continue.

For standalone exploratory or E2E requests with no PM-authored test cases,
confirm the function-tree scope and scenario. If execution is requested, confirm
the platform version first; missing versions are `blocked`, never written to
`unknown`. Ask whether there are new feature updates and whether project-file
exploration should be used to expand TC. If they decline exploration, use
existing QA memory and execute only the scoped charter.

Even when exploration is blocked before browser or harness execution, the
preflight output must explicitly state:

- the full QA memory read set: `TEST_SUITE.md`, `FLOW_INDEX.md`,
  `cases/*.md`, `scripts/*.spec.md`, prior `results/`, and `_reports/`
- the scenario decision (`feature-update` or `release`) and platform version
  status
- the intended execution entry order and selected entry rationale using repo
  harness > Chrome plugin / browser connector > Playwright fallback
- that executable E2E TC are delegated to subagents by default, while the main
  agent owns scope and summary reporting
- whether expansion would update `FLOW_INDEX.md`, one TC file under `cases/`,
  and the matching `scripts/*.spec.md`

When exploration follows an existing-feature change, bug fix, or code-complete
E2E documentation update, first identify the confirmed `feature_path`, read
`docs/pm/{feature_path}/PRD.md`, `docs/engineer/{feature_path}/TRD.md`, and a
confirmed `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`. If the path or
PM expectation is unclear, return to PM. If TRD or the plan is missing, stale,
or not on the same path, block reusable TC creation/update/execution and send
the work back to the appropriate Engineer step.

Gate strength for that alignment follows the `change_tier` contract in
`AGENTS.md` (变更分级契约). Consume `change_tier` from the handoff when
present, or self-assess it per that contract. For `hotfix` with unchanged
approved PRD/TRD expectations, only require validating the direct impact
paths and appending results, and accept the confirmed lightweight plan form
for the plan gate; for `standard` and above, keep the full PRD/TRD
expectation alignment gate. Tiering never waives evidence, and a request that
changes approved PRD/TRD expectations is never `hotfix` — return it to PM.

## Exploration Charter

Define a short charter before interacting with the app. The charter must include:

- Surface to explore: the specific screen, flow, API-backed interaction, or change area
- Timebox: chosen from the context, not a fixed skill default
- Heuristics: what kinds of failures matter most for this pass
- Escalation signals: what observations are strong enough to become a bug report candidate

Do not use vague timebox phrasing such as "a short exploration window". If the
user or fixture provides a duration, use it exactly. If execution is blocked
before a timer can start, state that no execution timebox started and name the
source that would determine the timebox on retry.

Charter heuristics should be specific to the change and typically include:

- Changed-path smoke coverage
- Navigation and routing edges
- Validation and form-handling edges
- Empty states and data absence
- Permissions and access boundaries
- Interruptions, retries, cancellations, refreshes, and partial completion
- Nearby risk surfaces that are plausibly coupled to the changed area

## Exploration Strategy

Choose the exploration path after preflight and chartering, in this order:

1. Smoke the changed surface end to end to confirm the basic path still works.
2. Probe edge cases around navigation, validation, empty states, permissions, and interruptions.
3. Expand into nearby risk areas only if the first two steps reveal coupling, instability, or suspicious signals.

Randomized action generation is optional and should only be used as a supplement when it helps coverage. It is not the default contract and should never replace chartered exploration.

## Execution Methods

Use whichever tools best fit the charter and environment:

- Browser automation for repeatable UI traversal
- Active Chrome plugin / browser connector for agent-operated web checks when
  available in the user environment
- Manual walkthroughs when judgment, visual inspection, or auth handling matters
- Console and network inspection when client or backend signals need confirmation
- Existing QA scripts when they already target the relevant path
- Targeted randomized inputs or action variations only when they support a specific heuristic

Prefer the least brittle method that still produces clear evidence.
For E2E execution, choose repo harness first, Chrome plugin / browser connector
second, and standalone Playwright only as fallback when Chrome is unavailable.
A repo harness that internally uses Playwright still counts as repo harness.

## Exploration Procedure

1. Record the charter and the context used to derive it.
2. Execute the smoke path over the changed surface.
3. Probe the prioritized edge cases from the charter.
4. Branch into nearby risk exploration only when the observed behavior justifies it.
5. If exploration reads source or config files to derive coverage, write or
   update `FLOW_INDEX.md` with the files read, why they were read, and coverage
   implications.
6. If exploration identifies reusable E2E scenarios, write or update one case
   file under `cases/` and the matching flow snippet under `scripts/` when
   repeatable execution needs it.
7. Track what was covered, what was intentionally skipped, and what still needs
   follow-up.

During exploration, capture:

- Exact steps or script paths used
- Visible UI behavior
- Console errors and warnings relevant to the issue
- Network failures, abnormal responses, or suspicious timing
- Reproduction consistency
- Any conditions that make the result ambiguous or environment-dependent

Use account IDs from login-flow references when authentication is needed. Do
not write plaintext usernames, passwords, tokens, cookies, sessions, SSH
passwords, or SSH key contents into TC, scripts, results, or reports.

## Bug Escalation Rules

Escalate to bug-analyzer only when the exploration finds a reproducible failure with enough evidence for a defect report.

Escalation-quality evidence usually includes:

- Clear reproduction steps
- The affected surface and scenario
- Observable wrong behavior
- Supporting console, network, or log evidence when available
- Notes on frequency and any environment dependencies

Keep unconfirmed anomalies in the exploratory report. Do not promote them as defects unless reproduction or evidence quality crosses the threshold above.

## Evidence Output

For E2E exploration that executes TC, write per-TC evidence under
`results/TC-NNN-<short-slug>/{platform-version}/` and write the main-agent
summary report with
`agents/qa/skills/qa-agent/references/e2e-test-report.md`.

Report paths:

- `feature-update`:
  `docs/qa/e2e/{feature_path}/_reports/{platform-version}/test-reports-{test-time}.md`
- `release`:
  `docs/qa/e2e/_reports/{platform-version}/test-reports-{test-time}.md`

For non-E2E exploratory reports where the repo has no stronger convention, use
`docs/qa-reports/YYYY-MM-DD-<feature>-exploratory-report.md`.

The report must be concise, handoff-ready, and clearly separate these sections:

- Observed issues: confirmed failures and reproducible defects
- Suspicious but unconfirmed signals: anomalies worth watching, but not yet defect-ready
- Exploration path covered: what was actually tested
- Gaps not explored: what remains untested and why
- Recommended next actions: follow-up QA, engineering checks, or escalation candidates

The report should also record the charter, timebox, and the evidence used to reach conclusions.

When new E2E case files are created or changed, list those paths in the report
so a later spec-based run can execute from them without repeating the same file
exploration.

## Out of Scope

- Random UI clicking without a charter
- Pure spec conformance checking
- Writing bug tickets as the primary artifact
- Hardcoded environment assumptions such as a fixed local URL
- Self-mutating workflow instructions such as committing results from the skill contract
