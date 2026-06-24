# Eval Result: eval-004-feature-path-report

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-004-feature-path-report`
- Test case: Feature Path Security Report
- Workspace: `workspace/eval-004-feature-path-report`
- Latest result: PARTIAL - prior skill validation evidence is preserved; without-skill baseline was not generated for this historical comparison.
- Prior validation note: fresh Codex subagent validation completed on 2026-06-23.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: nested feature path `chat-interface/history-search` with matching PM PRD, Engineer TRD, and implementation plan.
- Expected output: read same-path PM/Engineer documents and write `docs/security/chat-interface/history-search/appsec-checklist.md` with feature path frontmatter, not `docs/security/history-search/appsec-checklist.md`.

## Assertions

- `uses_same_path_pm_engineer_docs`: must read the PRD, TRD, and implementation plan under `chat-interface/history-search`.
- `writes_nested_security_report`: must output the nested security report path and must not output a top-level `history-search` report.
- `includes_feature_path_frontmatter`: report frontmatter must include `feature_path`, `parent_feature`, and `feature_level`.
- `does_not_invent_feature_directory`: unclear or missing feature path input must return to PM/Engineer instead of creating a synonymous top-level directory.

## With Skill

- The `appsec-checklist` skill now requires feature-scoped reviews to use the confirmed `feature_path`, read `docs/pm/{feature_path}/PRD.md`, read the matching Engineer TRD and implementation plan when architecture or release scope matters, and write `docs/security/{feature_path}/appsec-checklist.md`.
- The `security-agent` dispatcher preserves the confirmed `feature_path` and explicitly rejects inventing a top-level Security directory when the display name is ambiguous.
- The fixture supports the assertions: PM, TRD, and implementation plan all declare `feature_path: "chat-interface/history-search"` with `parent_feature: "chat-interface"` and `feature_level: "2"`; the TRD requires workspace-level authorization; `src/search.ts` includes a SQL string-concatenation risk that gives the AppSec review a concrete finding surface.
- Expected with-skill behavior is therefore to read the same-path PM/Engineer documents, produce frontmatter with `feature_path: chat-interface/history-search`, `parent_feature: chat-interface`, and `feature_level: 2`, and write `docs/security/chat-interface/history-search/appsec-checklist.md` without creating `docs/security/history-search/appsec-checklist.md`.

## Without Skill / Baseline
- BLOCKED: No actual without-skill baseline result is recorded for this historical comparison. This file is not treated as a full eval PASS until a baseline result is generated and written here.
- The feature-path gate adds the required behavior that unclear or missing path evidence must return to PM/Engineer instead of guessing a synonymous directory.

## Failures

- None found in fresh Codex subagent validation.

## Next Steps

- Keep this eval as issue #37 coverage for nested Security feature-path reports and required feature-path frontmatter.
- Future transcript or runner diagnostics, if executed, should be kept as runtime artifacts and summarized here only after review.

## Runtime Artifacts Policy

- This validation used direct review of the skill docs, Agent README, `evals.json`, and fixture workspace. No runtime transcript, generated output directory, verdict file, timing file, diagnostics, or `comparison.auto.md` was created or committed.
