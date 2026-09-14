---
name: exploratory-tester
description: "Explore an application through its actual interface to discover reproducible usability and functional defects."
---

# Exploratory Testing

Start with a focused charter: the user journey, environment, build, data, and
risk being explored. Read existing cases and known failures so exploration adds
coverage. Use the running application and record the actual interactions.

## Explore useful dimensions

- Main journeys and alternate branches, including navigation and recovery.
- Empty, loading, error, partial, and populated states.
- Input boundaries, invalid values, repeated submission, and cancellation.
- Session changes, permission differences, multiple tabs, and stale state.
- Responsive layout, keyboard operation, focus order, and accessible feedback.
- Network failures, retries, concurrency, and state persistence where relevant.

Prefer the project's harness or the available browser integration. Inspect
observations before deciding whether they indicate a defect. Reproduce promising
findings with the smallest sequence and compare against the stated expectation.

Capture build or commit identity, environment, preconditions, steps, expected
and observed results, and sanitized evidence. Label unverified hypotheses as
such. Save useful reusable cases in the project's test assets, using the
[case reference](../qa-agent/references/e2e-case-format.md) when helpful.

Respect a testing-only scope. Where repair is requested, use the reproduced
failure to guide a focused fix and subsequent regression run. Report covered
journeys, confirmed defects, and meaningful coverage gaps.
