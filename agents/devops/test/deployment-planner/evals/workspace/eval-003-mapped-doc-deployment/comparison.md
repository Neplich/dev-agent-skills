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
- target_skill_sha256: `ff61dcd9673d160376da3723849f195022899b8e8a38fe78c67e4488f9065a5f`
- eval_definition_sha256: `3a6f0e2dac2acec4b2146c1f3b14a82dc89e2d78da9249fb55fda45906586c82`
- metadata_sha256: `327b8d91b5679b5d6691e5c028c3cc9d4baaf0c68df0883449c838a3976294e7`
- fixture_sha256: `beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3fd213f6de3f610cad1c014e643471913a0678af0ef96531f1f973bd669f4005`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `aed4a3cdd1170f44446df97f66f60c0f6ae2151f3522fe982eb11ee05d551389`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill trace shows the change map and its required runtime document were read before the final code verification, with no unrelated site-document traversal. |
| `verifies_against_code` | PASS | The locked with_skill output identifies the code setting as 8081, contrasts it with the document's 8080, explains the conflict's deployment impact, and recommends EXPOSE/mapping for 8081. |
| `treats_unverified_as_low_trust` | PASS | The with_skill output explicitly notes last_verified_version: unverified, treats the document as low-trust/outdated navigation, and bases the port conclusion on server.conf. |
| `omits_unselected_targets` | PASS | The with_skill delivery has no generated assets and explicitly limits the matrix to the container service, marking Compose and Kubernetes/Helm unselected. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6; fixture_sha256=beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471; output_sha256=25ef30aaf8fc995b8c49084f61bea6714d1cdeceb04c52be2d092c3dd60a371b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly follows the mapped-document workflow, verifies the stale 8080 documentation against server.conf, treats unverified documentation as low trust, and gives only the container deployment recommendation with port 8081.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6; fixture_sha256=beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471; output_sha256=4de12024f46e311b80f93fe4777d29b963f3824dd8ae579e7d60a77ece25286a; snapshot_sha256=e65878b314f4077e0374b6b007a2eb695361b99c8aeaae0bf8ca7c0c94fb7695
- Behavior: Fresh baseline also found port 8081 and updated the runtime document, but did not explicitly demonstrate the low-trust treatment of the unverified document or provide the scoped deployment matrix.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
