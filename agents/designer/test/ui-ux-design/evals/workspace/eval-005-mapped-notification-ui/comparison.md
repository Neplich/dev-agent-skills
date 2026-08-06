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
- Fresh run time: `2026-08-07 00:04:31 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/designer/ui-ux-design/eval-005-mapped-notification-ui/`
- Fixture: `change-map.yaml`, mapped notification document, and notification-preferences HTML

## Latest Result

- Behavior result: **PASS**
- Coverage result: **PARTIAL** (2/3 assertions exercised; read-order evidence unavailable)
Overall result: PASS (partial coverage)

## Assertion Results (Current)

- reads_mapped_docs_first: **NOT EXERCISED** — current runtime evidence proves the mapped document was read and no unrelated formal document was used, but no persisted transcript proves read order.
- verifies_against_code: **PASS** — the candidate identifies the unchecked HTML control and reports the conflict with the document's enabled-by-default claim.
- treats_unverified_as_low_trust: **PASS** — last_verified_version: unverified triggers code verification and prevents blind trust in the formal document.

## With-Skill Behavior (Current)

The candidate correctly applies the low-trust and code-ground-truth rules,
reports the discrepancy, and stops at the missing feature-path gate. The
mapped-document-first ordering assertion could not be independently verified
from the retained runtime evidence.

## Fresh Without-Skill Baseline (Current)

The baseline was generated before the with-skill root existed, with the same
prompt and fixture in an independent top-level workspace under isolated
HOME/CODEX_HOME. It edits the HTML to match the stale document, demonstrating
the skill's code-ground-truth value; baseline behavior does not set Overall.

## Failures (Current)

- No behavior failure on exercised assertions.
- Coverage gap: read order was not retained as judgeable transcript evidence.

## Next Steps (Current)

- Persist the fresh lane transcript on the next run to exercise reads_mapped_docs_first.

## Runtime Artifact Policy (Current)

- Runtime lanes and judge evidence remain in independent /tmp workspaces and are not committed.
- Only this durable comparison is updated.

## Historical Result (Superseded: pre-#234 contract)

- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


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
