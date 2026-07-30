# Eval Result: eval-003-mapped-doc-deployment

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-003-mapped-doc-deployment`
- Workspace: `workspace/eval-003-mapped-doc-deployment`
- Validation: 2026-07-31 fresh paired Codex subagent validation

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: `change-map.yaml`, mapped unverified runtime document, and conflicting code configuration
- With-skill source: `tmp/eval-runs/issue-196-l2-1-20260731-0008/with_skill/eval-003-mapped-doc-deployment/`
- Fresh baseline source: `tmp/eval-runs/issue-196-l2-1-20260731-0008/without_skill_fresh2/eval-003-mapped-doc-deployment/`

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
- All 4 with-skill assertions were exercised and passed.

Overall result: PASS

## Assertion Results

- PASS `reads_mapped_docs_first`: the recorded read order is change-map, mapped runtime document, then code verification; the output reports no unrelated site-doc traversal.
- PASS `verifies_against_code`: the output identifies documentation port 8080 versus code port 8081 and explains health-check and traffic-routing impact.
- PASS `treats_unverified_as_low_trust`: it explicitly treats `last_verified_version: unverified` as lowest trust and uses code to confirm the critical port.
- PASS `omits_unselected_targets`: the matrix contains only containerization advice, creates no deploy assets, and explicitly omits local and Helm targets.

## With-Skill Behavior

- The output followed the change-map consumption path, separated documentation claims from verified code facts, and based the deployment advice on port 8081.
- It kept the output to the requested minimal container recommendation instead of generating unselected deployment targets.

## Fresh Without-Skill Baseline

- The valid fresh baseline used the same prompt and pristine fixture without reading or applying the target skill, DevOps Agent README, or consumption contract.
- It satisfied 2/4 assertions: it correctly selected code port 8081 and generated no unselected assets.
- It did not satisfy the mapped-doc-first assertion because its recorded read order began with the mapped document before the change-map. It also called the document stale but did not explicitly connect the `unverified` marker to the lowest-trust rule for critical parameters.
- The earlier `tmp/eval-runs/issue-196-l2-1-20260731-0008/without_skill/` run is excluded because its isolation was invalid; none of its output informed this result.

## Failures

- No with-skill assertion failure or validation blocker.
- The valid baseline missed the contract-specific read-order and unverified-trust assertions.

## Next Steps

- Keep this case to preserve the change-map-first and low-trust verification behavior.

## Runtime Artifact Policy

- Runtime candidates, results, transcripts, and diagnostics remain under ignored `tmp/eval-runs/` paths and are not copied into the durable fixture.
- Only this durable `comparison.md` is updated.
