---
name: regression-suite
description: "Verify a repaired defect or changed feature and exercise adjacent behavior selected from actual change impact."
---

# Regression Verification

Start with the reported failure, expected behavior, final diff, and previous
verification evidence. Select tests by affected runtime paths and shared
components. Reuse the existing suite and persistent E2E cases.

## Verify the change

1. Identify the revision, environment, and test data used for the run.
2. Re-run the original reproduction or acceptance case against the updated code.
3. Check neighboring behavior sharing state, validation, permissions, storage,
   APIs, or UI components with the change.
4. Exercise relevant error handling and recovery, including repeated operations
   or stale state where they could reveal a regression.
5. Record the command or flow, expected and observed result, and evidence.

Investigate failing checks and distinguish a remaining defect from an
unavailable test prerequisite. Expand coverage when a new failure or uncovered
risk warrants it. Keep independent checks progressing while a dependency is
unavailable.

Report fix verification, adjacent coverage, new findings, and material remaining
risk. A broader release recommendation reflects the actual scope tested.
Use [the report reference](../qa-agent/references/e2e-test-report.md) for a durable
report when the result will be reused.
