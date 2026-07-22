# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-012-deployment-class-evidence-gap`
- Review context: PR #166 fourth-round P2 fresh paired validation and fresh Codex judge

## Test Set / Fixture Version

- Fixture: verified Development/Docker evidence plus an unexecuted Kubernetes plan and no cluster authority; tightened deployment-root/shared-environment assertion and host test
- Actual validation date: `2026-07-22`

## Latest Result

**PASS (4/4 assertions)** — the fresh with-skill lane blocked only Kubernetes/Helm, generated the deployment root, shared environment authority, Development/Docker pages and Docker image authority with all required links and change-map entries, and passed `npm run test:docs` with 3/3 tests. The fresh judge independently reran both lanes and confirmed all with-skill assertions.

## With-Skill Behavior

- Used settings/tests to constrain shared environment fields to evidenced Development/Docker applicability.
- Generated the required five-page atomic scope: deployment root, shared `environment-reference.md`, Development index, Docker index and Docker `image-sources.md`.
- Linked the deployment root to both confirmed classes and the shared authority, linked both class pages back to the shared authority, linked the Docker image authority, and covered all five pages in the change map.
- Kept complete and separate prerequisites, commands, success criteria, rollback and troubleshooting for Development and Docker; no Kubernetes/Helm directory, command, map entry or success claim was created.
- Reported the missing Chart, values, template, permission, image and execution evidence, kept pages `unverified`, and preserved the #117 version gate.

## Fresh Without-Skill Baseline

- Source: fresh lane from the same pristine fixture and `eval_metadata.json` prompt without the target skill, Agent README, eval definition, comparisons or with-skill output.
- It passed the same 3/3 host tests and generated all five required pages, links and change-map paths, but the fresh judge rated it **PARTIAL (3/4 assertions)**.
- It failed `keeps_class_boundaries`: the Development page omitted rollback and troubleshooting, while the Docker page omitted troubleshooting.
- It also inferred a literal `docker compose ... up -d` command not recorded by the fixture, left the updated Ops index without the required frontmatter, and omitted the formal #117 handoff.

## Failures

- No with-skill assertion failures.
- The baseline failed one assertion even though its 3/3 deterministic host tests passed; those tests do not cover category-level rollback/troubleshooting completeness or report classification.
- Matching fixture, metadata, template and test hashes prove the paired inputs. The judge found no lane transcript at review time, so generation-process and prohibited-read provenance rely on workspace isolation and lane reports rather than a complete file-access audit.

## Next Steps

- Keep this PASS; the tightened assertion and host test now reject candidates that omit the deployment root, shared environment authority, their links, or any of the five required change-map paths.
- Preserve the semantic assertion review because the deterministic host tests do not by themselves detect incomplete per-class runbooks.
- Require new evidence and a separately confirmed batch before Kubernetes/Helm documentation is created.

## Runtime Artifact Policy

- Paired lanes, reports, available transcript and judge verdict remain under `tmp/eval-runs/pr166-review-round4-20260722-2053/` and are not submitted.
- Only this comparison is durable.
