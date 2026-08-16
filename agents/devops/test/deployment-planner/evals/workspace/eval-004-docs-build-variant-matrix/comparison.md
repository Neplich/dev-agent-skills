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
- target_skill_sha256: `dfa906d01a96634826afcebe44c9732902f0bc2b120c6c7b7232879b93b8e923`
- eval_definition_sha256: `4c14837e1c149db8fdda5fa172eb35b4e3c167d223226adbc87832c6a7126d6f`
- metadata_sha256: `4e635caa906adf35d961968845b5d0b832f3417bf48adf4843143f2222641a1f`
- fixture_sha256: `1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `cfb4e9daef57a9f8f8f71bd53e7b9c04b3f443f035ca06014209a131297ec22b`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `a8511777e6b4f31217e6a6c17f2c1dc2d5abd375ef6253072404dae037d7bae7`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `enumerates_all_docs_variants` | PASS | The with_skill matrix includes Public, Internal, and Preview. |
| `covers_deployment_unit_chain` | PASS | It explicitly covers build target, context, static entry, image, Compose, Kubernetes/Helm resources, values, health check, runtime entry, and disposition for each variant. |
| `hands_units_to_cicd` | NOT_EXERCISED | No delivery snapshot or independent handoff event to cicd-bootstrap is present; the later handoff is therefore not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087; fixture_sha256=1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5; output_sha256=cf20c9a906d7298cc117761c8c11d5c46d988263868d18020cb4fb076c4a95f2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a complete three-variant deployment-unit matrix with explicit blocked gaps; CI/CD handoff is not evidenced.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087; fixture_sha256=1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5; output_sha256=5577fb93af952d7ae12241b53da5dd1389ec4ea62825b5c32b27261f62b47240; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Enumerated variants and broad coverage gaps but omitted the required full chain fields and disposition treatment.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide evidence of the cicd-bootstrap handoff for confirmed image/runtime units.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
