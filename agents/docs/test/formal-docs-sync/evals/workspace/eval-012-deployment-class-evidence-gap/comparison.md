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
- Fixture SHA-256: `94a440475528b183f978a35b0a119247396e300b3f4d27c6c1d0f2046bc60924`
- Prompt SHA-256: `d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f24bfeb12dba77a74fcf3f0161749ae4671b83762eac08484e7ae08621d9bacb`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
- Judge schema SHA-256: `e93bcd19b2a81fd498c0a0b76bf2788577403b4eb3f684a80f1adbb170c93ef8`
- Eval definition SHA-256: `649fb22000e8030404ac6361df8372e15d8183baaa675df886e6c740c229829a`
- Metadata SHA-256: `9b6d976d4601ac0de151b2a46d4bd90f68a76a475f804b7878df438cf1dba8d6`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_only_missing_class` | PASS | 根索引和最终报告均将 Kubernetes/Helm 标为 blocked，并列出 Chart、values、模板消费者、集群权限/authority 与执行验证缺失；未把计划或网络可达性当作证据。 |
| `continues_confirmed_classes` | PASS | 锁定快照包含五个要求页面；索引链接、共享环境参数的 Development/Docker 映射及 change-map 条目均存在，且已确认批次未因 Kubernetes 阻塞而停止。 |
| `creates_no_placeholder_commands` | PASS | 锁定快照未包含 kubernetes-helm 目录或 Helm 占位命令/事实；报告列出了补齐 Kubernetes/Helm 所需证据。 |
| `keeps_class_boundaries` | PASS | Development 与 Docker 快照分别包含前置、命令、成功标准、回滚和故障处理；Docker 内容未吸收 Kubernetes 计划，也未由镜像 tag 推断集群来源。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=94a440475528b183f978a35b0a119247396e300b3f4d27c6c1d0f2046bc60924; output_sha256=9da7237154fbd9535f890a485ee690391f7ae3295c09cd85c73655e98b6cb433; snapshot_sha256=d411549b03f29e10d12b0d404a15ff2fea15985aa710a957b49f1979c73e5de9
- Behavior: 完成 Development 与 Docker 的五页文档及映射，并仅阻塞证据不足的 Kubernetes/Helm 类别。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=94a440475528b183f978a35b0a119247396e300b3f4d27c6c1d0f2046bc60924; output_sha256=3c3d4c1ae4b88381f33aaa1edfba92f7885c9b1ab301361fe5b617868cc4ef2d; snapshot_sha256=1907bd4d688cb9f9719910f036c97649d7f4d455ef7e1da4485883cc81807827
- Behavior: 同样生成了确认类别文档并保留 Kubernetes/Helm 缺失状态；作为比较基线，其内容更简略。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
