---
name: spec-based-tester
description: "Internal QA specialist invoked by qa-agent after pm-agent handoff to validate spec-backed requirements using PM docs, implementation context, repo instructions, and the safest executable test path."
visibility: internal
---

# Spec-Based Tester

Validate documented requirements against the implementation using the best available repository harness, then fall back to manual or browser-based checks only when the repo does not provide a stronger path.

This is a QA validation protocol, not a router and not a generic execution script. It stays within QA boundaries: read the spec and implementation context, choose an execution path, collect evidence, and report confirmed results, blocked items, and handoff risks.

## PM Handoff Entry Gate

Before validating, require a PM/QA handoff packet or equivalent confirmed test
basis. If the user directly invokes this specialist without PM handoff context,
confirmed specs, or an existing QA memory scope, return the request to
`pm-agent` for classification instead of inventing acceptance expectations.

Use the PM-side packet definition in
`agents/product_manager/skills/idea-to-spec/_internal/_shared/skill-map.md`.

## Shared QA Directory Contract

For E2E or feature-scoped QA, use the function-tree directory as the durable
source of truth:

`docs/qa/e2e/{feature_path}/`

- `TEST_SUITE.md` is the suite index and traceability summary.
- `FLOW_INDEX.md` maps flows, pages, routes, APIs, states, and requirements to
  TC files.
- `cases/` stores reusable test cases. Every E2E test case must be stored as
  exactly one Markdown file: `cases/TC-NNN-<short-slug>.md`.
- `scripts/` stores matching repeatable steps or executable snippets:
  `scripts/TC-NNN-<short-slug>.spec.md`.
- `results/TC-NNN-<short-slug>/{platform-version}/` stores append-only
  execution results and `testcase.snapshot.md`.
- Feature-update reports go to
  `_reports/{platform-version}/test-reports-{test-time}.md`; release reports go
  to `docs/qa/e2e/_reports/{platform-version}/test-reports-{test-time}.md`.

If a PM PRD / TRD / Test Spec is absent or does not include concrete E2E cases,
do not rediscover the whole project by default. First use the function-tree QA
directory as persistent memory.

## Feature Path Gate

For existing-feature changes, bug fixes, or code-complete E2E documentation
updates, QA consumes a confirmed `feature_path`; it does not infer a new one
from the leaf feature name. Before creating, updating, or executing acceptance
TC, read:

- `docs/pm/{feature_path}/PRD.md`
- `docs/engineer/{feature_path}/TRD.md`
- `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md`

All three documents must refer to the same feature path. If PRD is missing or
the parent feature is unclear, return to `pm-agent:idea-to-spec`. If TRD is
missing, stale, incomplete, or on a different path, return to
`engineer-agent:trd-gen`. If the confirmed implementation plan is missing,
stale, or on a different path, return to
`engineer-agent:feature-implementor`. In all of these cases, mark the E2E
acceptance work `blocked`.

If the target agent's plugin for a cross-agent handoff is not installed or
unavailable, state the missing stage and required plugin, mark that handoff
stage as blocked, and do not perform the missing agent's responsibilities
yourself.

## Top-Level Contract

Before running anything, gather repository evidence and confirm what is in scope.

- Read the PM/spec documents that define the expected behavior.
- Read the target `docs/qa/e2e/{feature_path}/TEST_SUITE.md`,
  `FLOW_INDEX.md`, `cases/*.md`, `scripts/*.spec.md`, previous `results/`, and
  `_reports/` before exploring source files when a function-tree QA directory
  exists.
- Read implementation context for the changed area, including changed files, engineer notes, release notes, or handoff notes if they exist.
- Read existing repository instructions for how tests are normally run in this project.
- If this is an existing-feature change, bug fix, or code-complete E2E
  documentation update, confirm PRD/TRD expectation alignment and a confirmed
  `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` before creating,
  updating, or executing E2E acceptance TC.
- Gate strength for that alignment follows the `change_tier` contract in
  `AGENTS.md` (变更分级契约). Consume `change_tier` from the handoff when
  present, or self-assess it per that contract. For `hotfix` with unchanged
  approved PRD/TRD expectations, only require validating the direct impact
  paths and appending results, and accept the confirmed lightweight plan form
  for the plan gate; for `standard` and above, keep the full PRD/TRD
  expectation alignment gate. Tiering never waives evidence, and a request
  that changes approved PRD/TRD expectations is never `hotfix` — route it
  back to PM.
- Confirm the E2E scenario: `feature-update` validates changed functionality
  and direct impact paths; `release` validates all active E2E TC.
- Confirm the platform version before execution. If missing, mark the run
  `blocked`; do not archive under `unknown`.
- Prefer the repo’s documented acceptance, e2e, integration, or manual QA
  harness over inventing a new runner.
- Only use targeted browser automation when no better harness or documented
  script exists.
- For agent-driven browser checks, use the active Chrome plugin / browser
  connector when available. Use standalone Playwright only as fallback when
  Chrome is unavailable or the skill is running outside a Chrome-capable
  environment. A repo harness that internally uses Playwright still counts as
  the repo harness.
- Do not assume a fixed localhost port.
- Do not assume Playwright is the only valid tool.
- Do not install dependencies globally or add new tooling unless the repository conventions explicitly require it.

## Preflight

Complete preflight before any execution step.

### 0) Standalone E2E memory check

When the user asks for E2E, acceptance, or spec-based QA without supplying PM
test cases:

1. Identify the function-tree scope from the user request, PRD/TRD, branch,
   changed files, or nearby QA docs. If it cannot be inferred, ask one concise
   question for the `{feature_path}` target.
2. For existing-feature changes, bug fixes, or code-complete E2E documentation
   updates, identify the confirmed `feature_path` and check the same-path PRD,
   TRD, and implementation plan before writing or executing acceptance TC.
3. Confirm or infer the scenario: `feature-update` or `release`.
4. Confirm the platform version before execution; if absent, stop as
   `blocked` and ask for the version.
5. Read the agreed QA directory:
   - `docs/qa/e2e/{feature_path}/TEST_SUITE.md`
   - `docs/qa/e2e/{feature_path}/FLOW_INDEX.md`
   - `docs/qa/e2e/{feature_path}/cases/*.md`
   - `docs/qa/e2e/{feature_path}/scripts/*.spec.md`
   - prior `results/` and `_reports/`, if relevant
6. If reusable TC exist, treat them as the primary execution scope.
7. For `feature-update`, execute only the changed feature, direct impact paths,
   and related regression TC. For `release`, execute all active E2E TC.
8. If coverage is missing and the user authorizes expansion, perform targeted
   exploration or PRD/TRD case generation, then write or update `cases/`,
   `scripts/`, and `FLOW_INDEX.md` before execution.

### 1) Gather scope sources

Read whatever is available from the following sources, in this order of usefulness:

- Existing QA test cases in
  `docs/qa/e2e/{feature_path}/cases/*.md`
- Existing `TEST_SUITE.md`, `FLOW_INDEX.md`, `scripts/*.spec.md`, prior
  `results/`, and `_reports/`
- Test Spec or equivalent QA acceptance doc
- PRD or product spec
- TRD or technical design doc
- Release notes, changelog, migration notes, or rollout notes
- Acceptance checklist, QA checklist, or handoff checklist
- Implementation context such as changed files, PR diff, engineer notes, or commit summary
- Existing test commands, local setup instructions, environment notes, and known prerequisites

If a source does not exist, note it as absent rather than inventing a substitute.

Before reporting any pass/fail result, include a preflight baseline section with:

- scope and feature path
- environment and platform version status
- unknowns and blocked checks
- same-path PRD/TRD/confirmed `IMPLEMENTATION_PLAN.md` gate status when the
  request comes from an existing-feature change, bug fix, or code-complete E2E
  documentation update
- QA memory read status for `TEST_SUITE.md`, `FLOW_INDEX.md`, `cases/*.md`,
  `scripts/*.spec.md`, prior `results/`, and `_reports/`

If reusable TC exist, explicitly state whether they are reused. If `scripts/`,
prior `results/`, or `_reports/` are absent, record them as absent or blocked
rather than silently skipping them.

### 2) Record the validation frame

Before execution starts, capture:

- What is being validated
- Which test case files, requirement IDs, acceptance points, or checklist items
  are in scope
- Which implementation areas are affected
- Which environment assumptions are confirmed
- Which assumptions are still unknown
- Which checks are blocked and why

### 3) Confirm execution prerequisites

Look for:

- Repo-specific test commands or scripts
- Required environment variables or services
- Auth or test-user requirements
- Seed data or fixtures
- Whether a build or local server must be started first

If the repo already defines a harness, use that harness. If there are multiple harnesses, choose the narrowest one that covers the scoped requirements.

## Environment Decision Protocol

Choose the least-assumptive executable path that still proves the requirement.

1. Existing repo acceptance/e2e command or documented harness
   - Use a documented acceptance, e2e, smoke, or scenario command if it exists.
   - Prefer commands that already encode project conventions, setup, and teardown.

2. Existing integration or manual QA script
   - Use a repository-provided integration script, scenario runner, or QA checklist automation if that is the standard path.
   - Prefer scripts that validate the changed area directly over broad end-to-end runs.

3. Targeted browser automation
   - Use browser automation only if the repo has no better harness for the requirement.
   - Keep it scoped to the changed flows and documented acceptance points.
   - Prefer the active Chrome plugin / browser connector for agent-operated
     clicks, typing, screenshots, console logs, network inspection, and DOM
     checks when it is available in the user environment.

4. Playwright fallback
   - Use standalone Playwright only when the repo harness does not cover the TC
     and Chrome plugin / browser connector is unavailable.
   - Do not add a new runner or install browser tooling globally.

Do not guess the server port. Do not hardcode `3000`. Discover the running app, configured host, or documented launch path from the repository context.

Do not assume Playwright. A repository-provided Playwright command is a repo
harness and can be used at priority 1; standalone Playwright remains the
fallback after Chrome is unavailable.

Do not install browser tooling globally. If dependencies or browsers are missing, first check project scripts, lockfiles, package manager conventions, and repo instructions.

## Execution

Execute only the tests that are justified by the preflight scope.

- For E2E validation, execute from the individual case files in
  `docs/qa/e2e/{feature_path}/cases/` whenever they exist.
- Execute each E2E TC through a subagent by default. The main agent confirms
  scope, consolidates evidence, and writes the summary report.
- Use account IDs from the TC or login-flow references. Do not write plaintext
  credentials into TC, scripts, results, or reports.
- Prefer targeted validation for the changed files and scoped requirements.
- Use environment-specific setup only when the repository documentation calls for it.
- Capture the exact command or tool path used.
- Capture any fixture, data, auth, or environment prerequisites that were necessary.
- If a prerequisite is missing, stop and mark the related checks as blocked instead of guessing.

During execution, distinguish:

- Confirmed behavior
- Confirmed failure with evidence
- Blocked check due to missing environment, missing access, or missing harness
- Assumption that could not be verified

## Evidence Contract

Produce a validation artifact that is useful for handoff and traceable back to the spec.

For E2E validation, write or update per-TC results under
`docs/qa/e2e/{feature_path}/results/TC-NNN-<short-slug>/{platform-version}/`
and write the main-agent summary report using
`agents/qa/skills/qa-agent/references/e2e-test-report.md`.

Report paths:

- `feature-update`:
  `docs/qa/e2e/{feature_path}/_reports/{platform-version}/test-reports-{test-time}.md`
- `release`:
  `docs/qa/e2e/_reports/{platform-version}/test-reports-{test-time}.md`

For non-E2E spec validation where the repo has no stronger reporting path, use
`docs/qa-reports/YYYY-MM-DD-<feature>-spec-validation.md`.

The report should include:

### 1) Validation summary

- Scope
- Environment
- Execution path used
- What was validated
- What was not validated

### 2) Requirement matrix

For each in-scope requirement or acceptance point, record:

- Test case file, when applicable
- Requirement ID or acceptance label
- Status: pass, fail, blocked, or assumed
- Evidence
- Notes

### 3) Confirmed failures only

List only failures that were directly reproduced and evidenced.

- Include the repro path, observed behavior, and supporting evidence.
- Do not turn blocked checks into bugs.
- Do not turn assumptions into bugs.
- Do not escalate flaky or ambiguous observations as confirmed defects unless you explicitly call out the uncertainty and why the result is not stable.

### 4) Blocked items

List blocked checks separately with the exact blocker.

### 5) Release or implementation risks

Call out any risks that need handoff even if they are not confirmed bugs, such as:

- Uncovered environments
- Missing prerequisites
- Spec gaps
- Implementation mismatches that need follow-up

## Bug-Analyzer Handoff

Hand off to bug-analyzer only when there is a confirmed, reproducible failure with evidence.

Do not auto-file bugs for:

- Blocked checks
- Unverified assumptions
- Flaky or inconsistent observations
- Missing environment access

If you are unsure whether a failure is reproducible, keep it in the report as uncertain and blocked from bug filing.

## Role Boundary

This skill validates documented behavior against implementation. It does not:

- Route work to other agents
- Invent a generic test harness
- Rewrite the implementation plan
- Commit code or self-mutate the repository

Its job ends at evidence-backed QA validation and a clear handoff report.

## Practical Workflow

1. Read spec and context
2. Build the preflight record
3. Choose the execution path using the environment decision protocol
4. Run the narrowest useful validation
5. Collect evidence and classify each result
6. Write the validation report
7. Hand off only confirmed reproducible failures

## Expected Outcome

A good run ends with:

- A scoped validation summary
- A requirement matrix tied to the spec
- Confirmed failures only where evidence exists
- Blocked items called out explicitly
- Risks and handoff notes for QA or engineering follow-up
