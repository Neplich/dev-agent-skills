# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-012-deployment-class-evidence-gap`
- Review context: PR #166 fifth-round P2 fresh paired validation and fresh Codex judge

## Test Set / Fixture Version

- Fixture: verified Development/Docker evidence plus an unexecuted Kubernetes plan and no cluster authority; deployment-root links are resolved semantically so directory and explicit `index.md` targets are equivalent
- Actual validation date: `2026-07-22`

## Latest Result

**PASS (4/4 assertions)** — the fresh with-skill lane blocked only Kubernetes/Helm, generated the deployment root, shared environment authority, Development/Docker pages and Docker image authority with all required links and change-map entries, and passed `npm run test:docs` with 3/3 tests. The fresh judge independently reran both lanes, confirmed all with-skill assertions, and verified that directory-style class links resolve to the required index pages without weakening the two-class link requirement.

## With-Skill Behavior

- Used settings/tests to constrain shared environment fields to evidenced Development/Docker applicability.
- Generated the required five-page atomic scope: deployment root, shared `environment-reference.md`, Development index, Docker index and Docker `image-sources.md`.
- Linked the deployment root to both confirmed classes and the shared authority, linked both class pages back to the shared authority, linked the Docker image authority, and covered all five pages in the change map.
- Kept complete and separate prerequisites, commands, success criteria, rollback and troubleshooting for Development and Docker; no Kubernetes/Helm directory, command, map entry or success claim was created.
- Reported the missing Chart, values, template, permission, image and execution evidence, kept pages `unverified`, and preserved the #117 version gate.

## Fresh Without-Skill Baseline

- Source: fresh lane from the same pristine fixture and `eval_metadata.json` prompt without the target skill, Agent README, eval definition, comparisons or with-skill output.
- It passed the same 3/3 host tests after correcting a missing deployment-root change-map entry and generated all five required pages, links and final change-map paths, but the fresh judge rated it **PARTIAL (3/4 assertions)**.
- It failed `keeps_class_boundaries`: the Docker page omitted the current startup command, so it did not fully maintain the required per-class command surface.
- Its deployment root used directory-style Development and Docker links, which the repaired host test accepted after resolving them to the corresponding index pages.

## Failures

- No with-skill assertion failures.
- The baseline failed one assertion even though its final 3/3 deterministic host tests passed; those tests do not cover category-level command completeness or report classification.
- Matching hashes for all 13 immutable fixture inputs prove the paired inputs. The judge intentionally did not read lane execution logs, so generation-process and prohibited-read provenance rely on workspace isolation and lane reports rather than a complete file-access audit.

## Next Steps

- Keep this PASS; the host test now resolves Markdown targets before comparison, accepts `development/`, `./development/`, `docker/`, `./docker/` and explicit `index.md` equivalents, and still rejects candidates that omit either confirmed class link, the shared authority links, or any required change-map path.
- Preserve the semantic assertion review because the deterministic host tests do not by themselves detect incomplete per-class runbooks.
- Require new evidence and a separately confirmed batch before Kubernetes/Helm documentation is created.

## Runtime Artifact Policy

- Paired lanes, reports, last-message outputs and judge verdict remain under `tmp/eval-runs/pr166-review-round5-20260722-2117/` and are not submitted.
- Only this comparison is durable.
