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
- Fixture SHA-256: `1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5`
- Prompt SHA-256: `449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e850d2052b73e431758456627cb816e0d9a45db383146d1349cf24ca05b2aec1`
- Skill overlay SHA-256: `69cf7483c4142716ecdbb6a031121f60813fdaad8bcb74124bd2f705524d6549`
- Judge schema SHA-256: `cfb4e9daef57a9f8f8f71bd53e7b9c04b3f443f035ca06014209a131297ec22b`
- Eval definition SHA-256: `4c14837e1c149db8fdda5fa172eb35b4e3c167d223226adbc87832c6a7126d6f`
- Metadata SHA-256: `ae56541ba154741dfb7ef84587ce065786aeb8ae82c4a282fa656aa8884b399e`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `enumerates_all_docs_variants` | PASS | With_skill 矩阵明确列出 Public、Internal 和 Preview 三个变体。 |
| `covers_deployment_unit_chain` | PASS | With_skill 为每个变体逐项列出 build target、context、static entry、image unit、Compose、Kubernetes/Helm、values、health check、runtime entry 和 disposition；缺失证据均显式标为 blocked。 |
| `hands_units_to_cicd` | NOT_EXERCISED | With_skill 为三个变体记录了 blocked 处置，但由于没有确认的镜像元数据且 cicd-bootstrap 不可用，无法证明已完成镜像单元交接；按规则该后续步骤未执行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087; fixture_sha256=1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5; output_sha256=37c2c4be03c801787d6c5533a3a663efcf59df598140e5f398fe922f8ccbd41c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整枚举变体并提供字段齐全、缺失证据显式阻塞的部署单元矩阵。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=449e8afe22d56be4ea49871dccbdfe925565441c9990c7332f547cf304565087; fixture_sha256=1133bdf01ec9b2682fe921196914971ab2c40caac0f63afd22f66198e7edede5; output_sha256=0feefa43aff71309c55b196bf4b24d38ed32fb2cf64a7859735d5be07449ebc7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 枚举了三个变体并识别主要部署缺口，但未覆盖完整部署链字段，也未涉及 CI/CD 交接。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补齐或确认镜像身份、不可变 tag、架构、registry、trigger 和验证要求后，将每个确认的镜像/运行时单元交给 cicd-bootstrap。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
