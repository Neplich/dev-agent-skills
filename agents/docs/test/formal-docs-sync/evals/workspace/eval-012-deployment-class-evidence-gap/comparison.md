# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-012-deployment-class-evidence-gap`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `94a440475528b183f978a35b0a119247396e300b3f4d27c6c1d0f2046bc60924` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-012-deployment-class-evidence-gap`.
- Identity schema: `2`
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `649fb22000e8030404ac6361df8372e15d8183baaa675df886e6c740c229829a`
- metadata_sha256: `9b6d976d4601ac0de151b2a46d4bd90f68a76a475f804b7878df438cf1dba8d6`
- fixture_sha256: `94a440475528b183f978a35b0a119247396e300b3f4d27c6c1d0f2046bc60924`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `e93bcd19b2a81fd498c0a0b76bf2788577403b4eb3f684a80f1adbb170c93ef8`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_only_missing_class` | PASS | With-skill report and deployment index explicitly mark Kubernetes/Helm blocked and name missing Chart, values, template consumers, cluster authority, and execution/verification results. Fixture confirms those materials are absent. |
| `continues_confirmed_classes` | PASS | Locked delivery snapshot contains all five required deployment pages, correct cross-links, evidence-backed Development/Docker parameters, and change-map entries covering those pages. Git evidence shows the confirmed batch continued despite Kubernetes being excluded. |
| `creates_no_placeholder_commands` | PASS | Locked delivery snapshot and git status show no kubernetes-helm directory. Delivered files contain no Helm commands, namespace, imagePullSecrets, or Kubernetes success claims; the report lists the missing evidence required to proceed. |
| `keeps_class_boundaries` | PASS | Development and Docker snapshots each provide distinct prerequisites, commands, success criteria, rollback, and troubleshooting. Docker uses the pinned image evidence and does not infer Kubernetes provenance from the tag; no Kubernetes plan is embedded in Docker content. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=94a440475528b183f978a35b0a119247396e300b3f4d27c6c1d0f2046bc60924; output_sha256=1c90798c7c43928950915ec8df6ca4d38dedf290538f0b986c5837e9d5a8304e; snapshot_sha256=5d11715708054fe781abebbbce89da5cf804934078ee91d7e0e8078e7327c835
- Behavior: Completed the confirmed Development and Docker documentation batch, preserved evidence boundaries, and explicitly blocked Kubernetes/Helm without placeholder artifacts.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=94a440475528b183f978a35b0a119247396e300b3f4d27c6c1d0f2046bc60924; output_sha256=9bebcf2abce87555c00fa4453dd7a797278858ba56fb6a30a7bd0a4da7ee3f69; snapshot_sha256=daf5cd74f2a145653fd4a0b588f030f0c007e27d20125fcb0b2004b7edd880f0
- Behavior: Fresh baseline also produced confirmed deployment documentation and avoided creating Kubernetes pages, but its change-map and documentation evidence coverage was less complete.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
