---
name: spec-based-tester
description: "QA validation protocol for spec-backed requirements. Reads PM docs, implementation context, and repo instructions before choosing the safest executable test path."
---

# Spec-Based Tester

Validate documented requirements against the implementation using the best available repository harness, then fall back to manual or browser-based checks only when the repo does not provide a stronger path.

This is a QA validation protocol, not a router and not a generic execution script. It stays within QA boundaries: read the spec and implementation context, choose an execution path, collect evidence, and report confirmed results, blocked items, and handoff risks.

## Top-Level Contract

Before running anything, gather repository evidence and confirm what is in scope.

- Read the PM/spec documents that define the expected behavior.
- Read implementation context for the changed area, including changed files, engineer notes, release notes, or handoff notes if they exist.
- Read existing repository instructions for how tests are normally run in this project.
- Prefer the repo’s documented acceptance, e2e, integration, or manual QA harness over inventing a new runner.
- Only use targeted browser automation when no better harness or documented script exists.
- Do not assume a fixed localhost port.
- Do not assume Playwright is the only valid tool.
- Do not install dependencies globally or add new tooling unless the repository conventions explicitly require it.

## Preflight

Complete preflight before any execution step.

### 1) Gather scope sources

Read whatever is available from the following sources, in this order of usefulness:

- Test Spec or equivalent QA acceptance doc
- PRD or product spec
- TRD or technical design doc
- Release notes, changelog, migration notes, or rollout notes
- Acceptance checklist, QA checklist, or handoff checklist
- Implementation context such as changed files, PR diff, engineer notes, or commit summary
- Existing test commands, local setup instructions, environment notes, and known prerequisites

If a source does not exist, note it as absent rather than inventing a substitute.

### 2) Record the validation frame

Before execution starts, capture:

- What is being validated
- Which requirement IDs, acceptance points, or checklist items are in scope
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

1. Existing repo acceptance/e2e command
   - Use a documented acceptance, e2e, smoke, or scenario command if it exists.
   - Prefer commands that already encode project conventions, setup, and teardown.

2. Existing integration or manual QA script
   - Use a repository-provided integration script, scenario runner, or QA checklist automation if that is the standard path.
   - Prefer scripts that validate the changed area directly over broad end-to-end runs.

3. Targeted browser automation
   - Use browser automation only if the repo has no better harness for the requirement.
   - Keep it scoped to the changed flows and documented acceptance points.

4. Custom ad hoc execution
   - Only as a last resort, and only if it is consistent with repository conventions.

Do not guess the server port. Do not hardcode `3000`. Discover the running app, configured host, or documented launch path from the repository context.

Do not assume Playwright. If browser automation is needed, use whatever browser tooling the repository already documents or the project conventions support.

Do not install browser tooling globally. If dependencies or browsers are missing, first check project scripts, lockfiles, package manager conventions, and repo instructions.

## Execution

Execute only the tests that are justified by the preflight scope.

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

Recommended artifact path:

`docs/qa-reports/YYYY-MM-DD-<feature>-spec-validation.md`

The report should include:

### 1) Validation summary

- Scope
- Environment
- Execution path used
- What was validated
- What was not validated

### 2) Requirement matrix

For each in-scope requirement or acceptance point, record:

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
