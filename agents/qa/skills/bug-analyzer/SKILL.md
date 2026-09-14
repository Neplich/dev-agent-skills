---
name: bug-analyzer
description: "Analyze reported or observed failures and produce reproducible defect records with severity, confidence, and supporting evidence."
---

# Defect Analysis

Read the report, observed behavior, affected build, and available logs or
screenshots. Identify the user's expected outcome from the request and reliable
project evidence. Reproduce the failure where the environment permits it.

## Build the defect record

Include a precise title, affected journey and revision, preconditions, minimal
steps, expected result, observed result, and evidence. Describe affected users,
frequency, workaround, and impact when known. Reference related tests or
existing issues to avoid duplicating the same defect.

Separate observed defects from hypotheses, environment limitations, and product
choices that need clarification. Grade severity by actual impact and reach,
and confidence by the quality of reproduction and evidence. Keep code-level
root-cause claims tied to the relevant data or control flow.

For a local report, use the project's issue/report location or return the
record in the task. Create or update an external tracker when the user's scope
authorizes it. Preserve useful reproduction steps as a reusable case using
[the case reference](../qa-agent/references/e2e-case-format.md).

When repair is included in the request, continue from the defect evidence into
the fix and verification. Finish with the finding, its status, and the next
concrete action needed for any unresolved portion.
