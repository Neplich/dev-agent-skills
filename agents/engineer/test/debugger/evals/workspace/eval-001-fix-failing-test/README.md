# Debugger Failing Test Fixture

This workspace represents a small existing-feature bug report for `debugger`.
The notification API should omit archived notifications from the active list,
but the fixture implementation currently returns them.

Expected behavior: `debugger` should reproduce the failing test, identify the
root cause from the implementation and PRD/TRD expectation, output a bug
analysis report, and ask whether to produce a repair implementation plan before
changing code.
