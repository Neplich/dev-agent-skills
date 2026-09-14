---
name: debugger
description: "Reproduce failures, identify their root cause, repair the affected code, and verify the fix with focused regression coverage."
---

# Debugging

Use the reported symptom, observed behavior, code, and tests to establish what
failed. Derive the expected behavior from the user's request and reliable
project evidence. State uncertainty where those sources conflict.

## Investigation and repair

1. Capture the failing command or interaction, error, environment, revision,
   inputs, and reproduction frequency. Keep sensitive values in protected local
   storage and use sanitized evidence in reports.
2. Reproduce the smallest failure. Compare a known working path or revision
   when that helps isolate the cause.
3. Trace the responsible data and control flow. Inspect recent changes,
   assumptions, boundary conditions, dependency behavior, and error handling.
4. Test a concrete root-cause hypothesis. Distinguish the triggering condition
   from the code responsible for the failure.
5. Make the focused repair within the requested scope. Add regression coverage
   that fails for the original defect and exercises the intended behavior.
6. Re-run the reproduction and relevant adjacent checks. Review the diff and
   summarize the cause, fix, evidence, and any remaining uncertainty.

When the user requests diagnosis only, deliver the investigation and proposed
repair as an evidence-based report. A repair request includes implementation
and verification within its scope. Clarify a product decision when the evidence
supports materially different expected outcomes; continue useful investigation
while that decision is pending.

For intermittent failures, collect timing, concurrency, retry, and resource
signals. For environment-only failures, compare versions and configuration
without exposing secrets. When reproduction is unavailable, label hypotheses
and explain the observation that would distinguish them.
