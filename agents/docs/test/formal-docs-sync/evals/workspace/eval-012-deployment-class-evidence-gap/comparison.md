# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-012-deployment-class-evidence-gap`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-012-deployment-class-evidence-gap`.
- Fixture SHA-256: `1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0`
- Prompt SHA-256: `d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `e93bcd19b2a81fd498c0a0b76bf2788577403b4eb3f684a80f1adbb170c93ef8`
- Eval definition SHA-256: `649fb22000e8030404ac6361df8372e15d8183baaa675df886e6c740c229829a`
- Metadata SHA-256: `9b6d976d4601ac0de151b2a46d4bd90f68a76a475f804b7878df438cf1dba8d6`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_only_missing_class` | FAIL | with_skill 报告将 gate 标为 blocked，并列出缺少 Chart、values、kubeconfig/权限和执行验证；但未说明缺少模板消费点，而原始 handoff 明确包含该缺口。 |
| `continues_confirmed_classes` | FAIL | with_skill 的 delivery_snapshot 为空，报告明确写明未应用变更映射、completed_batch 为 none，五个已确认页面均未生成。 |
| `creates_no_placeholder_commands` | PASS | with_skill 未交付任何文件或命令；报告排除了 Kubernetes/Helm 路径，并列出 Chart、values、kubeconfig、权限和验证证据缺口，未创建占位内容。 |
| `keeps_class_boundaries` | FAIL | with_skill 的 delivery_snapshot 为空，因此没有 Development 或 Docker 页面来分别提供前置、命令、成功标准、回滚和故障处理；报告仅描述拟议页面树。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0; output_sha256=88a8c445884751e6e3138496872c86c31aa4825158a6f6a2ca51d88e1d29d711; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅输出阻塞决策和拟议页面树；git_status、git_diff 和 delivery_snapshot 均为空。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0; output_sha256=66e4936dfd5a571fe21470dde88b18fb5d8fe3e0b01587676d1a3e2a469aa230; snapshot_sha256=1f7917f1111f132997e6b7dfecf86d9b6fb3f6c25b4c49f122edf0b29068fd40
- Behavior: 交付了五个页面及 change-map/Operations 更新，并阻塞 Kubernetes/Helm；作为对比基线，不影响 with_skill 判定。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未生成已确认的五个部署文档及对应 change-map 条目。
- Kubernetes 缺口说明遗漏了模板消费点。
- 未交付 Development 与 Docker 页面，无法满足其独立类别边界要求。
- Next: 交付 deployment 根索引、共享环境引用、Development 页面、Docker 页面和镜像来源页，并更新 change-map。
- Next: 在 Kubernetes 状态中明确列出缺少模板消费点。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
