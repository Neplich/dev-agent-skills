# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-012-deployment-class-evidence-gap`
- Review context: PR #166 third-round P2 fresh paired validation and fresh Codex judge

## Test Set / Fixture Version

- Fixture: verified Development/Docker evidence plus an unexecuted Kubernetes plan and no cluster authority; tightened Docker image-authority assertion and host test
- Actual validation date: `2026-07-22`

## Latest Result

**PASS (4/4 assertions)** — the fresh with-skill lane blocked only Kubernetes/Helm, continued the confirmed Development/Docker scope, generated the Docker `image-sources.md` authority with its index link and change-map entry, and passed `npm run test:docs` with 3/3 tests. The fresh judge independently reran both lanes and confirmed all assertions.

## With-Skill Behavior

- Used settings/tests to constrain shared environment fields to evidenced Development/Docker applicability.
- Generated separate Development and Docker contracts plus the Docker image authority; the Docker index links the authority and `deploy/docker/**` maps it atomically.
- Created the shared environment authority and deployment root index; no Kubernetes/Helm directory, command, map entry or success claim was created.
- Reported the missing Chart, values, template, permission, image and execution evidence, kept pages `unverified`, and preserved the #117 version gate.

## Fresh Without-Skill Baseline

- Source: fresh lane from the same pristine fixture and `eval_metadata.json` prompt without the target skill, Agent README, eval definition, comparisons or with-skill output.
- It passed 4/4 assertions and 3/3 tests, including the tightened Docker image-authority page, index-link and change-map checks.
- It remained weaker than the skill lane: it omitted the shared `environment-reference.md`, deployment root index, complete deployment classification fields, image provenance gaps, compliant Ops-index frontmatter, and the formal #117 handoff.

## Failures

- No with-skill assertion failures.
- The fresh judge noted that the with-skill rollback prose restates an executable `up -d` step while the fixture records only a successful rollback to the digest; this is outside the current assertions and did not change the result.
- Input hashes and matching metadata prove the paired fixture and prompt; the baseline's prohibited-read boundary is supported by its isolated workspace and report but not by a complete file-access audit.

## Next Steps

- Keep this PASS; the tightened assertion and host test now prevent a candidate that omits Docker `image-sources.md`, its Docker-index link, or its change-map entry from passing.
- Require new evidence and a separately confirmed batch before Kubernetes/Helm documentation is created.

## Runtime Artifact Policy

- Paired lanes, transcripts, reports, generated pages and judge verdict remain under `tmp/eval-runs/pr166-review-round3-20260722-2034/` and are not submitted.
- Only this comparison is durable.
