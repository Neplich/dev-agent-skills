# Eval Result: eval-004-docs-build-variant-matrix

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-004-docs-build-variant-matrix`
- Workspace: `workspace/eval-004-docs-build-variant-matrix`
- Validation: 2026-07-31 fresh paired Codex subagent validation

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: documentation host evidence for Public, Internal, and Preview build variants
- With-skill source: `tmp/eval-runs/issue-196-l2-1-20260731-0008/with_skill/eval-004-docs-build-variant-matrix/`
- Fresh baseline source: `tmp/eval-runs/issue-196-l2-1-20260731-0008/without_skill_fresh2/eval-004-docs-build-variant-matrix/`

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
- All 3 with-skill assertions were exercised and passed.

Overall result: PASS

## Assertion Results

- PASS `enumerates_all_docs_variants`: the matrix includes Public, Internal, and host Preview and does not claim completeness.
- PASS `covers_deployment_unit_chain`: each row covers build target, context, static entry, image unit, Compose, Kubernetes/Helm resources and values, health check, runtime entry, and disposition.
- PASS `hands_units_to_cicd`: every variant receives an explicit integrated or blocked disposition, confirmed image coverage is handed to `cicd-bootstrap`, and no workflow is created.

## With-Skill Behavior

- The output makes missing evidence explicit instead of inventing deployment details and correctly concludes that overall completeness is blocked.
- Public, Internal, and Preview remain visible through the full deployment-unit chain, including the non-production Preview variant.
- The blockers recorded in the runtime result are fixture evidence gaps and expected matrix dispositions, not eval execution blockers or assertion failures.

## Fresh Without-Skill Baseline

- The valid fresh baseline used the same prompt and pristine fixture without reading or applying the target skill or DevOps Agent README.
- It satisfied 1/3 assertions by enumerating all three variants.
- It omitted build context, static entry, named image units, Kubernetes resource chain, values, health checks, and runtime entry, and it did not hand confirmed image units to `cicd-bootstrap` with canonical per-variant dispositions.
- The earlier `tmp/eval-runs/issue-196-l2-1-20260731-0008/without_skill/` run is excluded because its isolation was invalid; none of its output informed this result.

## Failures

- No with-skill assertion failure or eval execution blocker.
- The valid baseline missed deployment-unit-chain completeness and CI/CD handoff assertions.

## Next Steps

- Keep this completeness-gate regression case; fixture evidence gaps should continue to produce explicit blocked dispositions without reducing assertion coverage.

## Runtime Artifact Policy

- Runtime candidates, results, transcripts, and diagnostics remain under ignored `tmp/eval-runs/` paths and are not copied into the durable fixture.
- Only this durable `comparison.md` is updated.
