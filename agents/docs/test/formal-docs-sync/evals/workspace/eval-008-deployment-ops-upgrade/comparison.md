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
- target_skill_sha256: `a3e1263ac8acb74f106913f935cefb0ebe0f7f059ccc011cd16715592fd0163d`
- eval_definition_sha256: `7fe3c7ecf4038349101f98fb6f2ef19330f01c150bee2276a165994129650157`
- metadata_sha256: `2f78367477eb99dc045585689bae85fd3302b30aa534650ea910cd64f9bdfbbe`
- fixture_sha256: `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f5d562d8581b8e42e3d9fc6fee3e3cf82b682235e3b52ce9b9c4f91a22e1e752`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b6ae3621879be63fa5b02212924eed11dd010ad027f0308f85d7666d26a57421`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_executed_deployment_evidence` | PASS | With-skill snapshots bind the pages to Compose, deployment-results.md, .env.example, and environment differences; the documented commands and results match the locked executed evidence. |
| `writes_current_ops_upgrade_rollback` | PASS | Docker pages record Compose startup, v1.4.2 upgrade, /healthz HTTP 200, v1.4.1 rollback, and the default AI_HUB_IMAGE with Compose evidence. |
| `does_not_promote_plan_to_current_state` | PASS | The deployment index explicitly states Kubernetes/Helm is unsupported and only an unexecuted plan, without presenting it as current capability. |
| `writes_current_deployment_tree_atomically` | PASS | All four required pages, navigation links, stable deploy/** mapping with existing exclude, unverified version metadata, and exclusion of unrelated page trees are present in the locked delivery snapshot. |
| `runs_ops_host_checks_and_handoffs` | NOT_EXERCISED | runner_captured_trace proves test:docs passed with 76 tests and the delivery reports a blocked audit handoff pending release-version confirmation; the downstream docs-audit handoff cannot be completed yet. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=df6cfeae536e3283b6dfc77a1337f2fdbbd0d562db8dee12253748c1e431fafe; snapshot_sha256=5ab082e03195efc58650f7f69865d74415e8283090d8d9db6f0dc01eb353df09
- Behavior: Delivered the required deployment documentation tree, corrected navigation links, used executed evidence, passed docs checks/builds, and stopped at the blocked audit handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=c5ab4817c738f1bc088b05aa0a94a33cdc758b220443450c2c6e2ab756576b0f; snapshot_sha256=cf3b54f2753b6e04253a52dc1ad7f8640710589e575b69ba26c2edaf825af1c0
- Behavior: Fresh baseline delivered four deployment pages and reported passing tests, but did not update the Ops navigation link or provide equivalent host-check/handoff evidence.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain release-version confirmation, then complete the docs-agent:docs-audit handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
