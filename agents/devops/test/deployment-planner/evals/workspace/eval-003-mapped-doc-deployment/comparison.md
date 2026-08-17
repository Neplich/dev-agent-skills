# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-003-mapped-doc-deployment`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471` from `agents/devops/test/deployment-planner/evals/workspace/eval-003-mapped-doc-deployment`.
- Identity schema: `2`
- target_skill_sha256: `dfa906d01a96634826afcebe44c9732902f0bc2b120c6c7b7232879b93b8e923`
- eval_definition_sha256: `3a6f0e2dac2acec4b2146c1f3b14a82dc89e2d78da9249fb55fda45906586c82`
- metadata_sha256: `327b8d91b5679b5d6691e5c028c3cc9d4baaf0c68df0883449c838a3976294e7`
- fixture_sha256: `beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3fd213f6de3f610cad1c014e643471913a0678af0ef96531f1f973bd669f4005`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `a8511777e6b4f31217e6a6c17f2c1dc2d5abd375ef6253072404dae037d7bae7`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Raw trace shows the mapped runtime document was identified and read after the task file/change-map, without unrelated site-document traversal. |
| `verifies_against_code` | PASS | The output and raw trace explicitly compare documentation port 8080 with code configuration `listen_port = 8081`, and recommend 8081. |
| `treats_unverified_as_low_trust` | PASS | The output explicitly treats `last_verified_version: unverified` as low trust and bases the deployment parameter on runtime configuration. |
| `omits_unselected_targets` | PASS | The with_skill lane generated no files or assets and explicitly declined Docker/Compose generation; no deploy/local or deploy/helm targets appear. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6; fixture_sha256=beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471; output_sha256=3671b32b530f750b0636e1fee685fe04dd6e36b39969652ec0a03b27ee9a921f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies 8081 as the container port, explains the 8080 documentation drift and low-trust status, provides a minimal mapping recommendation, and generates no unselected deployment assets.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6; fixture_sha256=beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471; output_sha256=29fcb4444a387ce7ba375c67c2a23e83fb1a42d24a72e5c08e8caa171afe9112; snapshot_sha256=cb7f6641903f5e49631f89cb6602ceb9d93103f3184771f9000926aaee60cb7e
- Behavior: Also identifies 8081 and updates the runtime document with a container deployment example, but serves as comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
