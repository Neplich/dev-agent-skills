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
- target_skill_sha256: `dd975083d3977d90b71b3396dff2498ef2b7e8d49c50fab50b5462a26f3248ee`
- eval_definition_sha256: `649fb22000e8030404ac6361df8372e15d8183baaa675df886e6c740c229829a`
- metadata_sha256: `9b6d976d4601ac0de151b2a46d4bd90f68a76a475f804b7878df438cf1dba8d6`
- fixture_sha256: `94a440475528b183f978a35b0a119247396e300b3f4d27c6c1d0f2046bc60924`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `e93bcd19b2a81fd498c0a0b76bf2788577403b4eb3f684a80f1adbb170c93ef8`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `f2aa9b2c49be68550ec45538c221425607f428ce`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_only_missing_class` | PASS | With-skill output explicitly marks Kubernetes/Helm blocked and lists the missing Chart, values, template consumers, cluster authority/permissions, and execution results. The delivery snapshot repeats these gaps and does not treat the plan as execution evidence. |
| `continues_confirmed_classes` | PASS | The with-skill delivery snapshot contains all five required pages, the required cross-links, evidence-backed environment mappings, and change-map entries. Development and Docker were completed despite Kubernetes/Helm remaining blocked. |
| `creates_no_placeholder_commands` | PASS | The with-skill snapshot contains no Kubernetes/Helm page tree or placeholder commands/content. The report lists the missing evidence required to complete that class. |
| `keeps_class_boundaries` | PASS | Development and Docker snapshots each contain separate prerequisites, commands, success criteria, rollback, and troubleshooting sections. Kubernetes content is excluded from Docker, and image provenance is limited to supplied manifest evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=94a440475528b183f978a35b0a119247396e300b3f4d27c6c1d0f2046bc60924; output_sha256=d82bb58cc484e9c3b27fdf9d5bc9dd2860f7feaef68053c5cae766c2b4254dc0; snapshot_sha256=d23d834d7f80e7e67d950bc763189128a291ed01e11eac7bf142bf9d321cae33
- Behavior: Completed confirmed Development and Docker documentation while blocking only unsupported Kubernetes/Helm work and preserving evidence boundaries.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=94a440475528b183f978a35b0a119247396e300b3f4d27c6c1d0f2046bc60924; output_sha256=624bcd5607440c64d1e4209f023ae05a1a4e7f5749e9eec430de0a58808e29d6; snapshot_sha256=4e63824ba02c7468f5a4711fddb88346025383cabac141e136a1370b59f3a67c
- Behavior: Fresh baseline also produced core deployment documentation and avoided fabricated Kubernetes content, but with less explicit evidence binding and change-map coverage.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
