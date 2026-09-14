---
name: spec-based-tester
description: "Validate user requirements, issue expectations, or documented behavior against a running system and report traceable test results."
---

# Behavior-Based Validation

Build a small expectation-to-test map from the user request, issue, specification,
API contract, or existing cases. Resolve material ambiguity in expected results
and state which assumptions the evidence supports.

## Execute

1. Identify the target environment and a useful build identifier, such as a
   release version, commit SHA, or local working-tree description.
2. Inspect the available harness, existing cases, accounts, and test data.
   Exercise independently runnable checks while an unavailable prerequisite is
   being resolved.
3. Run representative success, failure, boundary, and permission scenarios.
   Reuse established cases before adding new ones.
4. Record expected and actual behavior, execution command or browser flow,
   sanitized evidence, and the result for each checked expectation.
5. Investigate failures enough to distinguish product defects, environment
   failures, and incorrect test assumptions.

Use `pass` for observed success, `fail` for an observed expectation violation,
and `blocked` for checks that could not execute. Identify untested expectations
separately from successful checks. Link recurring journeys to persistent cases
and attach new findings to their reproduction evidence.

Scale the report to the task. For durable E2E reports, the
[report reference](../qa-agent/references/e2e-test-report.md) provides a compact
structure. Continue into a requested repair or regression pass with the same
scope and evidence.
