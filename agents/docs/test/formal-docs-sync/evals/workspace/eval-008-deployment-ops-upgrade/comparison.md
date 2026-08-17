# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-008-deployment-ops-upgrade`.
- Identity schema: `2`
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `7fe3c7ecf4038349101f98fb6f2ef19330f01c150bee2276a165994129650157`
- metadata_sha256: `2f78367477eb99dc045585689bae85fd3302b30aa534650ea910cd64f9bdfbbe`
- fixture_sha256: `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f5d562d8581b8e42e3d9fc6fee3e3cf82b682235e3b52ce9b9c4f91a22e1e752`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_executed_deployment_evidence` | PASS | Locked with_skill pages cite deploy/compose.yaml and deployment-evidence/deployment-results.md, including executed commands, exit 0, healthy status, HTTP 200, and environment differences. |
| `writes_current_ops_upgrade_rollback` | PASS | Docker pages record Compose startup, v1.4.2 upgrade, /healthz HTTP 200 success criteria, v1.4.1 rollback, and the default AI_HUB_IMAGE value with Compose evidence. |
| `does_not_promote_plan_to_current_state` | PASS | The deployment index explicitly classifies Kubernetes/Helm as unsupported and states the plan is unexecuted, with no Helm commands presented as current operations. |
| `writes_current_deployment_tree_atomically` | PASS | The locked delivery snapshot contains all four required pages, linked Ops/deployment/Docker navigation, a deploy/** map covering all four pages while retaining deploy/examples/** exclusion, unverified frontmatter, and git status showing only the scoped Ops/map changes and new deployment tree. |
| `runs_ops_host_checks_and_handoffs` | NOT_EXERCISED | Raw trace proves npm run test:docs ran in docs/site and ultimately passed 76/76. The final handoff is blocked pending confirmed release context, so the later docs-agent:docs-audit handoff cannot yet be exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=30b6b3f26c65cd24e4ee049b5cdf0ef8a26fd61b178f045fdf4cb854fe8bdc40; snapshot_sha256=46ebee885a07bf47498a3ed73d9932da21474109d88fca3280d9d09bcad2fc31
- Behavior: Produced the complete evidence-backed deployment documentation tree, passed the final 76-test docs check, and correctly left audit handoff blocked pending release context.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=71b2d6718c381100e943d646a3df55150a0cc27a71f4d2f122423d1c38cb3536; snapshot_sha256=5ec4a36d28867247bbe349db62f71c0166ec465a07c226ea1b56300d07c3bcd7
- Behavior: Produced four deployment pages and reported a passing docs test, but the locked snapshot left the Ops navigation and change-map unchanged and provided no completed audit handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain confirmed release context/target release version, then complete the docs-agent:docs-audit handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
