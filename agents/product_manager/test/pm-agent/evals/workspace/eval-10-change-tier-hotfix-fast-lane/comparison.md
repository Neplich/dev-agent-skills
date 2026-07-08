# Eval Result: pm-agent-change-tier-hotfix-fast-lane

## Evaluation Target

- Skill: `pm-agent`
- Test case: change-tier-hotfix-fast-lane
- Test set: change-tier contract evals for issue #55 / FR-008
- Entry: workspace `eval-10-change-tier-hotfix-fast-lane`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-08 after PR #98 trigger-description revisions.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: README link fix that does not change approved behavior and has local verification evidence
- Expected output: classify as `hotfix`, allow fast lane after classification, and preserve scope / source / verification evidence.

## Assertions

- PASS `classify_hotfix`: With `pm-agent` plus the AGENTS change-tier contract, the request is a `hotfix` because it is a single README link correction, it does not change approved expectations, and it is covered by the user's local link-verification evidence.
- PASS `allow_fast_lane`: The correct `request_type` is `delivery` / `status` or an equivalent already-scoped delivery request, so the `hotfix` fast lane is allowed only after PM entry classification confirms scope, source evidence, and verification status.
- PASS `preserve_evidence`: Fast lane does not weaken the evidence bar; the handoff still needs the bounded scope, source evidence for the README link fix, and verification evidence that the corrected link opens.

## With Skill Behavior

- Applied the current repository `pm-agent` skill, Product Manager Agent README, and AGENTS change-tier contract for the with-skill pass.
- The prompt is classified as `delivery` / `status` or an equivalent lightweight delivery request because the user asks for handling an already-scoped PR fix, not for new requirements or expectation changes.
- `change_tier` is `hotfix`: the fix is single-file documentation/link correction work, explicitly preserves approved behavior, and has direct local verification evidence.
- Fast lane is available only after classification; it can hand off to delivery / engineering execution without reopening full PRD/TRD alignment, but it must carry the evidence packet.
- Required handoff evidence: scope decision that only one README link is fixed and approved expectations are unchanged, source evidence from the PR/request/README link context, and verification evidence that the corrected link was locally opened.

## Without Skill Baseline

- Fresh without_skill baseline regenerated on 2026-07-08 from the same eval prompt and fixture without applying or citing the `pm-agent` skill or Product Manager Agent README.
- A generic assistant would likely call this a small documentation-only fix, low risk, and ready to proceed quickly because the user says the link was locally verified.
- The generic baseline may not emit the repository's stable `request_type` / `change_tier` fields, may treat the fast lane as an immediate shortcut rather than a post-classification path, and may summarize verification informally instead of requiring a durable scope / source / verification evidence packet.

## Failures

- None. The PR #98 trigger-description revisions still lead `pm-agent` to classify this unchanged-expectation README link fix as `hotfix`, allow fast lane after classification, and preserve evidence requirements.

## Next Steps

- Keep this eval as coverage for valid hotfix fast-lane handling.
- Re-run fresh validation if `pm-agent` trigger descriptions, change-tier definitions, or fast-lane evidence requirements change again.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed for this fresh validation. Transcripts, verdicts, timing, outputs, and diagnostics must remain outside git or under an untracked scratch path such as `tmp/eval-runs/eval-010-change-tier-hotfix-fast-lane/`.
