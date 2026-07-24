# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`
- Review context: PR #166 second-round P2 fresh paired validation and fresh Codex judge

## Test Set / Fixture Version

- Fixture: current deployment-verification evidence set with confirmed `ops/deployment/` Docker page tree, shared environment reference, Ops navigation, and `deploy/**` change-map scope
- Evidence set: confirmed deployment handoff, TRD surface, `.env.example`, Compose configuration, executed deployment results, environment differences, and future-only Kubernetes/Helm plan
- Actual validation date: `2026-07-22`

## Latest Result

**PASS (5/5 assertions)** — the fresh with-skill lane generated the deployment root index, shared environment reference, Docker runbook and image authority; synchronized only executed startup, upgrade, health and rollback facts; excluded the unexecuted Kubernetes/Helm plan; passed `npm run test:docs` with 76/76 tests; and returned the #117 handoff blocked on a maintainer-confirmed target version. The fresh Codex judge independently reran both lanes and confirmed all assertions.

## Assertions

- `uses_executed_deployment_evidence`: PASS. Current claims came from `deploy/compose.yaml`, `.env.example`, recorded command exits and health results, and confirmed environment differences rather than the TRD or plan alone.
- `writes_current_ops_upgrade_rollback`: PASS. The Docker runbook records development/staging startup, the `v1.4.2` pull and upgrade, `/healthz` HTTP 200 success, and rollback to `v1.4.1`; `docker/image-sources.md` owns the image coordinates and evidence boundary.
- `does_not_promote_plan_to_current_state`: PASS. Kubernetes/Helm remains an unsupported, unexecuted plan with no page or placeholder command.
- `writes_current_deployment_tree_atomically`: PASS. All four required pages exist and link to their authorities; the existing Ops navigation and `deploy/**` mapping cover them while preserving `deploy/examples/**`; all new pages remain `unverified`, and unrelated sections are unchanged.
- `runs_ops_host_checks_and_handoffs`: PASS. The judge reran `npm run test:docs` in both lanes, each exiting `0` with 76/76 tests; the with-skill report hands off #117 without executing deployment and blocks version stamping until a maintainer confirms `target_release_version`.

## With-Skill Behavior

- Used `doc_type: ops` throughout the deployment tree and produced the full environment-reference contract: type, requiredness, default, constraints, applicable class, safe example, sensitivity, activation timing, and evidence.
- Classified Development as out-of-scope, Docker as supported, and Kubernetes/Helm as unsupported; it also named missing image provenance, architecture, authentication, offline-source, logging, and data-check evidence without inventing commands.
- Kept the legacy single-page shape absent and treated the four pages, internal links, Ops navigation, and change map as one confirmed atomic scope.
- Preserved the formal #117 gate: missing confirmed release context leaves the handoff blocked and all pages `last_verified_version: unverified`.

## Fresh Without-Skill Baseline

- Source: a fresh lane copied from the same pristine input and run with the same `eval_metadata.json` prompt; it was instructed not to read the target skill, Agent README, eval definitions, comparison, with-skill output, or historical runs.
- The baseline also generated the four-page tree, recorded the executed Docker upgrade and rollback, excluded Kubernetes/Helm, and passed 76/76 tests.
- It was weaker than the skill lane: the root used `doc_type: landing`, the environment table omitted the complete ops contract fields, deployment-class and missing-evidence reporting was unstructured, and the #117 handoff did not explicitly enforce the maintainer-confirmed-version blocked state.

## Positioning Against Eval-011/012/013

- Eval-008 remains the deployment-verification regression for synchronizing already executed Docker upgrade facts into the current page tree; it no longer accepts `docs/site/ops/ai-hub-upgrade.md`.
- Eval-011 covers a full three-class existing-system backfill, eval-012 covers class-local blocking when Kubernetes/Helm evidence is missing, and eval-013 covers atomic migration from an existing aggregate deployment page.

## Failures

- No with-skill assertion failures.
- The `codex exec` lane streams and reports were generated and judged, but the with-skill last-message transcript path was resolved outside its intended lane and was overwritten by the baseline run. This reduces transcript-level provenance but does not change the file-level same-input proof, independent test reruns, or assertion result.
- The strong confirmed fixture lets the baseline satisfy the five core assertions, so this eval demonstrates correctness more strongly than skill-versus-baseline discrimination.

## Next Steps

- Keep this PASS and retain eval-008 as the focused executed-Docker-upgrade deployment-verification regression.
- On a future rerun, use absolute `--output-last-message` paths per lane so both transcript summaries remain available to the judge.

## Runtime Artifact Policy

- Pristine input, paired lane outputs, reports, dependencies, CLI streams, transcript summary, and judge verdict remain under `tmp/eval-runs/issue-161-review-round2-20260722-2002/` and are not submitted.
- Only this comparison is durable; no generated formal page, report, transcript, verdict, `node_modules`, or diagnostics file is committed.
