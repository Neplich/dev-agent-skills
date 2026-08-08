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
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
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
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `649fb22000e8030404ac6361df8372e15d8183baaa675df886e6c740c229829a`
- Metadata SHA-256: `9b6d976d4601ac0de151b2a46d4bd90f68a76a475f804b7878df438cf1dba8d6`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_only_missing_class` | PASS | with_skill 标记 Kubernetes/Helm 为 blocked，并明确列出 Chart、values、模板消费点、集群权限及执行验证缺失；未将未执行计划作为支持证据。 |
| `continues_confirmed_classes` | PASS | 锁定 delivery_snapshot 包含五个要求页面；根索引、环境引用、Development/Docker 链接及 change-map 对应条目均已交付，且 Development 与 Docker 批次继续完成。 |
| `creates_no_placeholder_commands` | PASS | 锁定交付内容未创建 kubernetes-helm 目录或 Helm/namespace/values/imagePullSecrets/成功状态占位内容；输出列出了待补齐的 Kubernetes/Helm 证据。 |
| `keeps_class_boundaries` | PASS | Development 与 Docker 页面分别包含各自的前置、命令、成功标准、回滚和故障处理；Docker 页面未吸收 Kubernetes 计划，镜像来源页明确 Kubernetes 映射仍未确认。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0; output_sha256=75ba5abdb4e44e32dae59fb5307de91213ee84b05a33643397c95b66a694378e; snapshot_sha256=75c926941965bf8ccb30a345db30003d0921d47c53a66a2d09f932dc5ab52226
- Behavior: 完成五个确认范围页面及完整对应映射；仅阻塞缺证据的 Kubernetes/Helm 类别，并避免占位内容。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0; output_sha256=71a185af2356b6e5d4c87892bc0e27ab742c895f87333c130fc5ced10a012372; snapshot_sha256=eafe4e9de7f5f2a0108c2b46c6025835be719d81faae474a1437903b0b65fceb
- Behavior: 完成 Development/Docker 文档并阻塞 Kubernetes，但 change-map 覆盖较少，未充分维护全部已确认映射。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Target skill tree SHA-256: `a612d50c32b84c65fad3cad08aad2d416a3a33647abfa1462784c1e58022424b`
- Skill overlay SHA-256: `e55ecf59b3cd8d90a2ed4cf555bed2ad2fc2131494e0914246a868317b68f4e8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `649fb22000e8030404ac6361df8372e15d8183baaa675df886e6c740c229829a`
- Metadata SHA-256: `3a580f8006b08e3032c21158c9a19664711df2d67798fea0ee5220d77bc7e01c`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_only_missing_class` | PASS | with_skill marks Kubernetes/Helm blocked and cites missing Chart, values, template consumers, kubeconfig/cluster authority, and execution/verification evidence; it does not treat the unexecuted plan as support. |
| `continues_confirmed_classes` | FAIL | All five required pages and links are present, and change-map entries cover them. However, image-sources.md incorrectly states that architecture and image manifest results are unavailable, contradicting the raw OCI manifest evidence. |
| `creates_no_placeholder_commands` | PASS | with_skill creates no kubernetes-helm directory or Helm placeholder commands/content, and explicitly lists the missing evidence needed before completion. |
| `keeps_class_boundaries` | PASS | Development and Docker pages maintain separate prerequisites, commands, success criteria, rollback, and troubleshooting sections; no Kubernetes plan or cluster-source inference is placed in Docker documentation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0; output_sha256=4141a90eefaa2964de8ab3e3ac68c8f90ab4c8f8b35be49c72235ef67c1bc449; snapshot_sha256=9d2ad1af858f744a6f03ff94e5cbff13ec08fcaacc86d2f0069f656c57c5e9b2
- Behavior: Completed the required confirmed deployment documentation and correctly blocked Kubernetes/Helm, but included an unsupported claim that OCI architecture/manifest evidence was unavailable.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0; output_sha256=e0a48333b5ffea0d9533f3c0d36a56a1ff48cde4f17abb397cc50972773dc6ff; snapshot_sha256=f158a2d28431bcc20a9f8be6e63802857e7a433627b86fc15d1b900f17a642bc
- Behavior: Completed the confirmed documentation batch and blocked Kubernetes/Helm, with concise validation reporting.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill image-sources.md falsely says architecture and image manifest results are unavailable, despite fixture/deployment-evidence/manifests/app-v2.0.0.json providing both.
- Next: Correct image-sources.md to incorporate or accurately reference the available OCI manifest and architecture evidence.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `52db6badcefada59a1d42e81de2581f06256f43c060b7699c281ab21bfb40949`
- Skill overlay SHA-256: `f896903fa1a8ae6886eb0b6365065625a2e60f6809acd0af6c7c8dc8f8f2bd40`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `649fb22000e8030404ac6361df8372e15d8183baaa675df886e6c740c229829a`
- Metadata SHA-256: `3a580f8006b08e3032c21158c9a19664711df2d67798fea0ee5220d77bc7e01c`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_only_missing_class` | FAIL | with_skill correctly keeps Kubernetes/Helm ungenerated, but does not list all required missing evidence, including template consumers and cluster authority, nor clearly enumerate the evidence needed to unblock it. |
| `continues_confirmed_classes` | FAIL | with_skill performs no document generation and gives an unsupported blocker, `docs/site/standards/doc-granularity.md`, which is absent from the fixture and not required by the supplied standards. |
| `creates_no_placeholder_commands` | FAIL | with_skill indicates no Kubernetes page or placeholder commands, but omits the required report of the specific evidence needed to complete that class. |
| `keeps_class_boundaries` | FAIL | with_skill generates no Development or Docker pages, so it does not deliver the required separate prerequisites, commands, success criteria, rollback, and troubleshooting content. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0; output_sha256=19887ef3e72507eed2c631f5bec03e9f8c38f379b301114f34189889038d9171; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Stopped without making changes, citing an unsupported missing documentation contract despite sufficient fixture evidence to complete the confirmed classes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0; output_sha256=72224f22d06b1d2a138e9d067e070e5d8d063c5cddb490d41c458862ccadea7d; snapshot_sha256=61a1db1b4ed413d8eae409a2431e80dc0107e577a6ce9e368568764e4a7c1c2d
- Behavior: Generated the confirmed Development and Docker documentation, mappings, and image-source page while leaving Kubernetes/Helm ungenerated.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane failed to generate the five required confirmed deployment pages and change-map entries.
- It cited a nonexistent or unsupported prerequisite and did not fully enumerate Kubernetes/Helm unblock evidence.],
- next_steps":[]}್ಯರ್ಥхыҵ?}assistant Rectified JSON malformed. Need resend correct only. Wait final already malformed. Must issue correct final likely.яда.񎟢Толуқ?}＿欧美? We need output valid. Use exact. 񟿿、】【json {
- next_steps
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1e290565a84b926a128928ccdd91365a2235adff18f999307c0a3553f0b41f34`
- Skill overlay SHA-256: `0c6a49eed1db242a95632eb0d142c1760f60ffc995c96026908ec8c0e6bd8d63`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `649fb22000e8030404ac6361df8372e15d8183baaa675df886e6c740c229829a`
- Metadata SHA-256: `3a580f8006b08e3032c21158c9a19664711df2d67798fea0ee5220d77bc7e01c`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_only_missing_class` | PASS | with_skill 将 Kubernetes/Helm 明确标为 blocked，并列出缺少 Chart、values、模板证据、集群 authority、权限检查及执行/rollout 结果；未把计划或网络可达性当作证据。 |
| `continues_confirmed_classes` | PASS | with_skill 交付了要求的五个页面及导航链接；根索引、Development、Docker 和镜像来源链接关系满足要求，环境参数仅记录 APP_PORT 与 DATABASE_URL 的有证据映射，change-map 覆盖五页，且未因 Kubernetes 阻塞停止其他批次。 |
| `creates_no_placeholder_commands` | PASS | with_skill 的交付快照中不存在 kubernetes-helm 目录；Development/Docker 页面无 Helm 占位命令或 Kubernetes 事实，且明确说明所缺 Chart、values、模板、集群权限与验证证据。 |
| `keeps_class_boundaries` | PASS | with_skill 分别为 Development 与 Docker 提供前置、命令、成功标准、回滚和故障处理；页面未塞入 Kubernetes 计划，也未从同名 tag 推断集群来源。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0; output_sha256=4c814348aaec4f38c31e432e846024553ddb3033621bc99289f455d27a049820; snapshot_sha256=44727b962838ed5755dfe92e34532fbef4576295cd8645c8b025a1f630dca323
- Behavior: 正确阻塞仅缺证据的 Kubernetes/Helm 类别，同时完整交付 Development、Docker、共享环境、镜像来源及映射文档，并保持证据边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0; output_sha256=2a1d85c0eeda0f1bc5d0c94aedb3fec106d1ab8a90b3323610115868fdf904c8; snapshot_sha256=169ebef21e55f659ea2a1f59ecf80f74e4cc8684f0d8dfe87b90a52c9b13d0e7
- Behavior: 完成了主要部署文档回填并正确避免 Kubernetes 占位内容；页面结构和证据边界总体符合要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `649fb22000e8030404ac6361df8372e15d8183baaa675df886e6c740c229829a`
- Metadata SHA-256: `3a580f8006b08e3032c21158c9a19664711df2d67798fea0ee5220d77bc7e01c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_only_missing_class` | FAIL | with_skill 仅表示将 Kubernetes/Helm 标记为 blocked，但未具体说明 Chart、values、模板消费点、集群权限和执行验证均缺失。 |
| `continues_confirmed_classes` | FAIL | with_skill 仍在等待批准，未生成五个要求的页面、导航或 change-map 条目，也未运行验证。 |
| `creates_no_placeholder_commands` | FAIL | with_skill 未创建 Kubernetes 页面或占位命令，但也未在报告中列出补齐该类所需的具体证据，因此未满足完整断言。 |
| `keeps_class_boundaries` | FAIL | with_skill 未写入 Development 或 Docker 页面，无法证明两类分别维护前置、命令、成功标准、回滚和故障处理，或未吸收 Helm 内容。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0; output_sha256=466f80195612eb55902a2c3e27ba700b34621ae101eaa19bdde34d935c103c56; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别出 Kubernetes/Helm 应阻塞且 Development/Docker 应继续，但因等待批准未执行任何写入或验证。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d22f5a61b9778737597225188b6c8c34747660b197372bd350dcfc64d227e5ff; fixture_sha256=1de8258a9da58346af1c991b6a49dbec33d719a345dcdc2748bb8b2eeb45a0e0; output_sha256=3b4efcc31e472300934f41bd2c997db1c4c232d456b7286c5dfe85747578106e; snapshot_sha256=688e0585d4fcc1030582b467472cd5d1dd454c62bba74a8f686092ddcd0f0c8f
- Behavior: 完成了确认范围的部署文档、导航和映射，并保留 Kubernetes/Helm 缺口说明；报告称文档测试通过。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完成要求的文档回填；所有要求继续生成或交付页面的断言均未满足。
- Next: 执行确认范围内的五个页面、导航和 change-map 更新，并运行文档测试。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-012-deployment-class-evidence-gap`
- Review context: PR #166 fifth-round P2 fresh paired validation and fresh Codex judge

## Test Set / Fixture Version

- Fixture: verified Development/Docker evidence plus an unexecuted Kubernetes plan and no cluster authority; deployment-root links are resolved semantically so directory and explicit `index.md` targets are equivalent
- Actual validation date: `2026-07-22`

## Latest Result

- Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `blocks_only_missing_class` | PASS | FAIL | with_skill 在 `deployment/index.md` 明确标记 `Kubernetes/Helm \ \| blocked`，并列出 Chart、values、模板、kubeconfig 权限、镜像来源和 rollout 结果缺失。without_skill 列出了同样缺口，但未将该类别明确标记为 `blocked`。 |
| `continues_confirmed_classes` | PASS | PASS | 两条 lane 均生成 deployment 根索引、共享环境参数、Development、Docker、镜像来源五个页面；页面链接和 `change-map.yaml` 均覆盖这些文档。 |
| `creates_no_placeholder_commands` | PASS | PASS | 两条 lane 均未创建 `kubernetes-helm/`；生成页面不含 `helm install`、namespace、values 或 `imagePullSecrets` 等占位事实，并说明所需缺失证据。 |
| `keeps_class_boundaries` | PASS | PASS | 两条 lane 的 Development 与 Docker 页面均分别包含 prerequisites、commands、success criteria、rollback、troubleshooting；未将 Kubernetes 计划或集群来源塞入 Docker 内容。 |

未满足断言（with/without 任一 FAIL）：``blocks_only_missing_class``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Used settings/tests to constrain shared environment fields to evidenced Development/Docker applicability.
- Generated the required five-page atomic scope: deployment root, shared `environment-reference.md`, Development index, Docker index and Docker `image-sources.md`.
- Linked the deployment root to both confirmed classes and the shared authority, linked both class pages back to the shared authority, linked the Docker image authority, and covered all five pages in the change map.
- Kept complete and separate prerequisites, commands, success criteria, rollback and troubleshooting for Development and Docker; no Kubernetes/Helm directory, command, map entry or success claim was created.
- Reported the missing Chart, values, template, permission, image and execution evidence, kept pages `unverified`, and preserved the `docs-agent:docs-audit` version gate.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- Source: fresh lane from the same pristine fixture and `eval_metadata.json` prompt without the target skill, Agent README, eval definition, comparisons or with-skill output.
- It passed the same 3/3 host tests after correcting a missing deployment-root change-map entry and generated all five required pages, links and final change-map paths, but the fresh judge rated it **PARTIAL (3/4 assertions)**.
- It failed `keeps_class_boundaries`: the Docker page omitted the current startup command, so it did not fully maintain the required per-class command surface.
- Its deployment root used directory-style Development and Docker links, which the repaired host test accepted after resolving them to the corresponding index pages.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- No with-skill assertion failures.
- The baseline failed one assertion even though its final 3/3 deterministic host tests passed; those tests do not cover category-level command completeness or report classification.
- Matching hashes for all 13 immutable fixture inputs prove the paired inputs. The judge intentionally did not read lane execution logs, so generation-process and prohibited-read provenance rely on workspace isolation and lane reports rather than a complete file-access audit.

## Next Steps

- Keep this PASS; the host test now resolves Markdown targets before comparison, accepts `development/`, `./development/`, `docker/`, `./docker/` and explicit `index.md` equivalents, and still rejects candidates that omit either confirmed class link, the shared authority links, or any required change-map path.
- Preserve the semantic assertion review because the deterministic host tests do not by themselves detect incomplete per-class runbooks.
- Require new evidence and a separately confirmed batch before Kubernetes/Helm documentation is created.

## Runtime Artifact Policy

- Paired lanes, reports, last-message outputs and judge verdict remain under `tmp/eval-runs/pr166-review-round5-20260722-2117/` and are not submitted.
- Only this comparison is durable.
