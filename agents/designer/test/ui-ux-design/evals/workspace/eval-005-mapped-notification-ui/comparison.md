# Eval Result: eval-005-mapped-notification-ui

## Evaluation Target

- Agent: `designer`
- Skill: `ui-ux-design`
- Eval: `eval-005-mapped-notification-ui`
- Test case: Mapped Notification UI Documentation
- Workspace: `workspace/eval-005-mapped-notification-ui`

## Test Set or Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`
- Fresh run time: `2026-08-03 11:58:33 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/designer/ui-ux-design/eval-005-mapped-notification-ui/`
- Fixture: `change-map.yaml`, mapped notification document, and notification-preferences HTML

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

All three consumption-contract assertions were exercised.

## Assertion Results

- `reads_mapped_docs_first`: **PASS** — the task path is reverse-mapped to the sole required document, with no unrelated formal-doc traversal.
- `verifies_against_code`: **PASS** — the document says enabled by default while the checkbox lacks `checked`, so the current static markup is unchecked.
- `treats_unverified_as_low_trust`: **PASS** — `last_verified_version: unverified` triggers code verification of every key claim rather than blind trust or refusal.

## With-Skill Behavior

- Preserves a structured discrepancy containing the documentation claim, HTML fact, and design impact.
- Correctly stops at the PM handoff/feature-path gate instead of inventing a design artifact path.
- The reached consumption and gate behavior does not use BRD; its removal causes no difference.

## Fresh Without-Skill Baseline

- This baseline was newly generated in this run from only the same prompt and fixture; it did not apply the Designer README, skill, consumption contract, with-skill output, or old comparison.
- It notices the unchecked HTML control but does not systematically establish mapped-document-first ordering, lowest trust for `unverified`, or structured discrepancy evidence.
- It contains no BRD reference.

## Failures

- None.

## Next Steps

- No skill or fixture correction is required for this case.

## Runtime Artifact Policy

- Runtime candidates, fresh baseline, and judge evidence remain under the ignored runtime directory and are not committed.
- Only this durable `comparison.md` is updated.
