# Eval Result: eval-001-legacy-project-catalog

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-001-legacy-project-catalog`
- Test case: legacy-project-catalog
- Workspace: `workspace/eval-001-legacy-project-catalog`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: Node.js commerce backend with no PM docs and code evidence for auth, orders, notifications, model, and tests
- Expected output: pending-confirmation feature catalog draft with evidence, confidence, open questions, related code paths, and a maintainer confirmation gate; no formal catalog or PRD before confirmation.

## Assertions

- `draft_before_formal_docs`: draft first, no formal PM docs before confirmation
- `evidence_and_confidence`: candidate entries include evidence categories and confidence
- `business_capability_naming`: business capability names, not copied code directory names
- `open_questions_present`: unresolved ownership or boundary questions are explicit
- `confirmation_gate`: output stops by asking maintainers to confirm feature paths

## With Skill

- The `feature-catalog` protocol first scans existing PM docs, then README and shallow code entry points when no Project Profile exists.
- For this fixture it can produce a visible pending-confirmation draft with candidates such as login/authentication, order management, and order status notifications, backed by `src/routes/auth.js`, `src/routes/orders.js`, `src/services/order-service.js`, `src/services/notification-job.js`, `src/models/order.js`, and `test/orders.test.js`.
- Because the evidence comes from a lightweight fallback scan, confidence is conservative and open questions remain for maintainer confirmation.
- It stops at the confirmation gate and does not write `docs/pm/FEATURE_CATALOG.md` or any `docs/pm/{feature_path}/PRD.md`.

## Without Skill / without_skill Baseline

- The baseline read the eval item and fixture before target skill docs. A generic project scan could list routes and services, but may copy code directory names directly into feature names.
- It may generate a polished catalog or PRD immediately, omit confidence and open questions, or skip the explicit maintainer confirmation gate.

## Failures

- None. The current `feature-catalog` public and internal protocol satisfies the draft, evidence, naming, uncertainty, and confirmation assertions.

## Next Steps

- Keep this eval as coverage for inherited projects with no PM documentation.
- Re-run fresh validation if shallow-scan confidence rules or confirmation-gate behavior changes.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, outputs, timing, and diagnostics must remain outside git; the durable result is this `comparison.md`.
