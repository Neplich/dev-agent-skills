# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-012-deployment-class-evidence-gap`
- Review context: issue #161 fresh paired rerun and fresh Codex judge

## Test Set / Fixture Version

- Fixture: verified Development/Docker evidence plus an unexecuted Kubernetes plan and no cluster authority
- Actual validation date: `2026-07-22`

## Latest Result

**PASS (4/4 assertions)** — the fresh with-skill lane blocked only Kubernetes/Helm, continued the confirmed Development/Docker scope, generated no cluster placeholders, and passed `npm run test:docs` with 2/2 tests. The fresh judge independently reran the check.

## With-Skill Behavior

- Used settings/tests to constrain shared environment fields to evidenced Development/Docker applicability.
- Generated separate Development and Docker contracts plus Docker image authority; no Kubernetes/Helm directory, command, map entry or success claim was created.
- Reported the missing Chart, values, template, permission, image and execution evidence, kept pages `unverified`, and preserved the #117 version gate.

## Fresh Without-Skill Baseline

- Source: fresh lane from the same pristine fixture and prompt without the target skill, Agent README, comparisons or with-skill output.
- It passed 2/2 tests and correctly blocked Helm, but omitted the Docker image-source authority, had weaker troubleshooting/map coverage, and did not produce the formal #117 handoff.

## Failures

- No with-skill assertion failures.
- Runtime provenance used lane transcripts and reports; a separate immutable input manifest was not retained.

## Next Steps

- Keep this PASS; require new evidence and a separately confirmed batch before Kubernetes/Helm documentation is created.

## Runtime Artifact Policy

- Paired lanes, transcripts, reports, generated pages and judge verdict remain under `tmp/eval-runs/issue-161-rerun/` and are not submitted.
- Only this comparison is durable.
