# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `deployment-planner`
- Eval: `eval-004-docs-build-variant-matrix`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5` from `agents/devops/test/deployment-planner/evals/workspace/eval-004-docs-build-variant-matrix`.
- Identity schema: `2`
- target_skill_sha256: `ff61dcd9673d160376da3723849f195022899b8e8a38fe78c67e4488f9065a5f`
- eval_definition_sha256: `4c14837e1c149db8fdda5fa172eb35b4e3c167d223226adbc87832c6a7126d6f`
- metadata_sha256: `4e635caa906adf35d961968845b5d0b832f3417bf48adf4843143f2222641a1f`
- fixture_sha256: `1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `cfb4e9daef57a9f8f8f71bd53e7b9c04b3f443f035ca06014209a131297ec22b`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `aed4a3cdd1170f44446df97f66f60c0f6ae2151f3522fe982eb11ee05d551389`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `enumerates_all_docs_variants` | PASS | With-skill output explicitly includes Public, Internal, and Preview in the matrix. |
| `covers_deployment_unit_chain` | PASS | With-skill output provides per-variant columns for build target, context, static entry, image unit, Compose, Kubernetes/Helm resources, values, health check, runtime entry, and disposition; unavailable evidence is explicitly marked blocked. |
| `hands_units_to_cicd` | FAIL | The output lists image units for handoff but states the handoff is not complete; Public uses “部分覆盖” and Internal does not explicitly assign one of integrated/alternative/deferred/blocked as its disposition. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087; fixture_sha256=1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5; output_sha256=0e697f604c1e171f2c4287baa38b37ab6ae4d217983aa02e7c2f24af939f76fe; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Enumerates all variants and supplies a field-complete blocked-aware deployment matrix, but fails the required CI/CD handoff and disposition requirement.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087; fixture_sha256=1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5; output_sha256=8aa43e49b368c1bacc112f6cc459e1a9d726f92e479c6d457e1591e738768caf; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Enumerates all three variants and contrasts coverage gaps, but provides a less complete deployment-unit chain and no CI/CD handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane does not complete the required cicd-bootstrap handoff and does not give every variant an explicit required disposition.
- Next: Assign integrated, alternative, deferred, or blocked to every variant and complete the confirmed image-unit handoff to cicd-bootstrap.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
