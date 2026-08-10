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
- Fixture SHA-256: `beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471`
- Prompt SHA-256: `40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e850d2052b73e431758456627cb816e0d9a45db383146d1349cf24ca05b2aec1`
- Skill overlay SHA-256: `69cf7483c4142716ecdbb6a031121f60813fdaad8bcb74124bd2f705524d6549`
- Judge schema SHA-256: `3fd213f6de3f610cad1c014e643471913a0678af0ef96531f1f973bd669f4005`
- Eval definition SHA-256: `3a6f0e2dac2acec4b2146c1f3b14a82dc89e2d78da9249fb55fda45906586c82`
- Metadata SHA-256: `d4f866ac92cff8803e8f120ce38631fed1d054cce30a482192275834ed6880bf`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | 跟踪显示先读取 change-map，再精准读取 runtime-server.md，未遍历无关站点文档。 |
| `verifies_against_code` | PASS | 明确指出代码为 8081、文档为 8080，解释冲突，并建议 EXPOSE 8081 与 8081:8081 映射。 |
| `treats_unverified_as_low_trust` | PASS | 将文档标记为 unverified，并以配置代码确认端口；对绑定地址、启动命令和健康检查缺少证据明确标为待确认或 blocked。 |
| `omits_unselected_targets` | PASS | 矩阵仅列 Docker 容器，明确 Kubernetes/Helm 未选择，且未生成文件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6; fixture_sha256=beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471; output_sha256=b9468ee33c6ce47f8322dea518e6cf446fac6cb5a79b2bf475271da70bcb3592; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 按变更映射精准读取运行时文档并回到代码核证，给出 8081 容器部署建议；对缺失部署证据保持 blocked/待确认。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=40b086c239ff14f46936633adeb5d9079306a48046e93c803af236ab43d646d6; fixture_sha256=beceb4834aab461ec20117458ef66d8ba65e677ecbef5e80a9e59909d2fe5471; output_sha256=31735fb6274bdc9c5203f424441b0030d327582485a5c86cfc99cd6ef44be559; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别 8081 并给出容器建议，但未体现映射文档优先读取流程，且提出了无证据的绑定地址与文档修改建议。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
