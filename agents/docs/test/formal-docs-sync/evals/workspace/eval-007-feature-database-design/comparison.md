# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-007-feature-database-design`
- Mode / types: feature delivery / Database + Design

## Test Set / Fixture Version

- Fixture version: `issue-160 design information architecture v2`
- Evidence: Approved PRD, Confirmed TRD, closed plan, actual diff, committed
  pytest fixtures, schema, invitation service, membership repository, and audit writer
- Fresh run: `tmp/eval-runs/pr-165-review-fix-20260722-194449/design/`
- Actual validation date: `2026-07-22`

## Latest Result

**PARTIAL（with-skill 6/8；fresh without-skill 5/8）** — the previously
un-runnable required tests are now reproducible: both fresh lanes and the
independent judge ran the requested command with 4/4 passing. Both lanes also
passed the locked host checks with 74/74 Node tests. The fresh judge found two
remaining behavioral gaps in the generated candidates: neither recorded a
page-by-page seven-item Design closeout matrix, and neither completed every
necessary ancestor-index mapping atomically.

## Assertions

- `loads_only_database_design_contracts`: with-skill PASS; without-skill FAIL.
  Only with-skill had verifiable access to the common contract and the
  Database/Design modules.
- `passes_design_closeout_gate`: both FAIL. The evidence chain is complete, but
  the candidates summarize all pages together instead of recording each
  proposed Design page against all seven closeout items.
- `synchronizes_database_current_state`: both PASS. The page records the unique
  workspace-user pair, allowed roles, required timestamp, logical references,
  and absence of physical foreign keys.
- `creates_domain_component_flow_tree`: both PASS. The expected roots, domains,
  components, flow, boundary, and compatibility entry exist.
- `keeps_reciprocal_and_authority_links`: both PASS. Components and flow link
  reciprocally, while API/Database remain authority links.
- `keeps_cross_domain_authority_unique`: both PASS. Invitation acceptance has
  one authority page; Audit Log only references it.
- `updates_atomic_map_and_unverified_pages`: both FAIL. Changed ancestor indexes
  are not consistently included in the relevant code-glob mappings; all
  changed pages do remain `unverified`.
- `runs_host_checks_and_handoffs_audit`: both PASS. Disposable locked installs
  passed frontmatter, strict affected, version metadata, and 74/74 Node tests,
  followed by #117 handoff.

## With-Skill Behavior

- Loaded only the Database and Design type contracts after the common entry.
- Produced accurate Database facts, the confirmed Design hierarchy, reciprocal
  flow/component links, and a unique cross-domain authority.
- Did not produce a verifiable page-by-page closeout matrix and did not include
  every changed ancestor index in the atomic change-map closure.

## Fresh Without-Skill Baseline

- Source: a new pristine copy with the same prompt, assertions, metadata, code,
  committed test support, and evidence; it did not contain or read the target
  skill, old comparison, with-skill output, or historical baseline.
- Result: 5/8 PARTIAL. It shares the two candidate-output failures and also
  cannot satisfy the target-module loading assertion.
- Skill-specific uplift: +1 assertion, or +12.5 percentage points.

## Required Test Reproduction

From each lane root, the independent judge ran:

`PYTHONDONTWRITEBYTECODE=1 uv run --with pytest python -m pytest -p no:cacheprovider tests/test_workspace_access.py -q`

- with-skill: exit `0`, `4 passed`
- without-skill: exit `0`, `4 passed`

The durable fixture command requested by the review also passes from the
fixture root:

`uv run --with pytest python -m pytest tests/test_workspace_access.py -q`

Result: exit `0`, `4 passed`.

## Failures

- With-skill: `passes_design_closeout_gate`,
  `updates_atomic_map_and_unverified_pages`.
- Without-skill: the same two assertions plus
  `loads_only_database_design_contracts`.
- Required pytest and host-check reproducibility are no longer failures.

## Next Steps

- Retain the committed `tests/conftest.py` support and executable test evidence.
- A later skill-behavior change should make the per-page gate matrix and full
  ancestor-index map closure deterministic before this eval can return PASS.

## Runtime Artifact Policy

- Both lanes, dependencies, candidate outputs, judge verdicts, logs, and
  disposable test copies remain under `tmp/eval-runs/` or `/tmp` and are not
  submitted.
- Only this `comparison.md` is durable; no `with_skill/`, `without_skill/`,
  transcript, verdict, timing, diagnostics, dependency, generated-site, or
  cache artifact is committed.
