# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-008-deployment-ops-upgrade`.
- Fixture SHA-256: `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845`
- Prompt SHA-256: `47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `f5d562d8581b8e42e3d9fc6fee3e3cf82b682235e3b52ce9b9c4f91a22e1e752`
- Eval definition SHA-256: `7fe3c7ecf4038349101f98fb6f2ef19330f01c150bee2276a165994129650157`
- Metadata SHA-256: `2f78367477eb99dc045585689bae85fd3302b30aa534650ea910cd64f9bdfbbe`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_executed_deployment_evidence` | PASS | The delivered pages identify deploy/compose.yaml and deployment-evidence/deployment-results.md as sources, and accurately record the executed Compose results, health response, and environment differences. |
| `writes_current_ops_upgrade_rollback` | PASS | Docker pages record Compose startup and upgrade commands, HTTP 200 /healthz success criteria, rollback to v1.4.1 with post-rollback health verification, and the v1.4.2 AI_HUB_IMAGE default with Compose evidence. |
| `does_not_promote_plan_to_current_state` | PASS | The deployment index explicitly states Kubernetes/Helm migration is planned, unexecuted, and unsupported as a current deployment path. |
| `writes_current_deployment_tree_atomically` | PASS | All four required pages are delivered with unverified front matter; links are present across Ops, deployment, and Docker indexes. The fixture change map contains all four deploy/** mappings and preserves deploy/examples/** exclusion; unrelated sections are untouched in the locked status. |
| `runs_ops_host_checks_and_handoffs` | NOT_EXERCISED | The candidate reports npm run test:docs and an audit handoff, but the locked raw evidence does not independently prove real command execution or a completed docs-agent:docs-audit handoff; the handoff is explicitly blocked pending release context. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=1b6260557181edb8fb286e5e1c25274097a1085012092e59498e2ea1d0a2a5b2; snapshot_sha256=a78cd5fadae9950ce201fbc6f0c5936c8647c082b40cbff09c0aa33dd3550503
- Behavior: Delivered the requested Docker deployment documentation coherently, preserved the Kubernetes/Helm boundary, and reported the missing release context that blocks audit handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=afb649dbe205dd9f48a12a3d1c473c9685e73f8f09089570238c7710d7f7f5d6; snapshot_sha256=32aeabcde050854e4febe70c7a3cb2905f15f3142733cf43fbc1a60ee31acc43
- Behavior: Delivered broadly similar deployment pages and checks, but provided less explicit gating and process context; comparison only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide confirmed release context and independently capture the docs audit handoff and host-check results.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-008-deployment-ops-upgrade`.
- Fixture SHA-256: `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845`
- Prompt SHA-256: `47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `f5d562d8581b8e42e3d9fc6fee3e3cf82b682235e3b52ce9b9c4f91a22e1e752`
- Eval definition SHA-256: `7fe3c7ecf4038349101f98fb6f2ef19330f01c150bee2276a165994129650157`
- Metadata SHA-256: `2f78367477eb99dc045585689bae85fd3302b30aa534650ea910cd64f9bdfbbe`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_executed_deployment_evidence` | PASS | Delivered pages cite `.env.example`, `deploy/compose.yaml`, and executed deployment results; content reflects actual Compose commands, exit 0 results, health status, and environment ports. |
| `writes_current_ops_upgrade_rollback` | PASS | Docker pages document Compose startup, upgrade to `registry.example/ai-hub:v1.4.2`, `/healthz` HTTP 200 with body `ok`, rollback to `v1.4.1`, and post-rollback health verification. |
| `does_not_promote_plan_to_current_state` | PASS | The deployment index explicitly marks Kubernetes/Helm as unsupported and describes `deployment-plan.md` as an unexecuted plan. |
| `writes_current_deployment_tree_atomically` | NOT_EXERCISED | All four required pages are delivered with `last_verified_version: unverified`; the existing navigation and `deploy/**` change-map content covers the pages and preserves the exclude. The locked evidence does not prove the hidden atomic-write operation itself. |
| `runs_ops_host_checks_and_handoffs` | NOT_EXERCISED | The candidate reports `npm run test:docs` exit 0 and all checks passed, but provides no locked raw execution log; the audit handoff is explicitly blocked pending release context rather than completed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=a358f68ffcd8059e35667ca2e6c5cd3344bd51f3ddfe76615568e331361413fc; snapshot_sha256=6943589fa2b4649957ecc3ce4e2212a9594ffc119f9e9f9446ec0334c7316d92
- Behavior: Correctly produced evidence-grounded deployment documentation and kept planned Kubernetes/Helm work out of current state; hidden atomicity and runtime handoff execution are not proven.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=0004782355c2ce262bb5fcf7062577fccce6523792c2bb5d5d033bb32a221ba6; snapshot_sha256=85be96a571c65d656ee4d1887a9620e1a31657fdaa5f5ee3fa86cd149a6db73f
- Behavior: Produced similar four-page documentation and claimed checks, but used verified version metadata and is retained only as baseline comparison context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide raw proof of the real `npm run test:docs` execution and complete the `docs-agent:docs-audit` handoff after release context is confirmed.
- Next: Provide evidence of the atomic write operation if that process-level assertion must be exercised.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-008-deployment-ops-upgrade`.
- Fixture SHA-256: `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845`
- Prompt SHA-256: `47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7fe3c7ecf4038349101f98fb6f2ef19330f01c150bee2276a165994129650157`
- Metadata SHA-256: `2f78367477eb99dc045585689bae85fd3302b30aa534650ea910cd64f9bdfbbe`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_executed_deployment_evidence` | PASS | with_skill 页面明确以 Compose、环境示例和 deployment-results 为事实源，并将未执行的 Kubernetes/Helm 计划排除；交付内容中的命令、退出状态和健康结果与原始证据一致。 |
| `writes_current_ops_upgrade_rollback` | PASS | Docker 页面记录启动、升级、/healthz HTTP 200 标准及回滚到 v1.4.1 后的 HTTP 200；image-sources 页面记录 AI_HUB_IMAGE 默认值和 Compose 执行结果。 |
| `does_not_promote_plan_to_current_state` | PASS | 部署根页明确 Kubernetes/Helm 仅为未执行计划、不属于当前支持路径；Docker 页面也明确当前证据不覆盖 Kubernetes/Helm。 |
| `writes_current_deployment_tree_atomically` | NOT_EXERCISED | 四个部署页面、Ops 索引链接和页面 frontmatter 可由 locked snapshot 验证，但交付证据未包含 change-map 文件内容或 git_blob，无法独立验证四页映射及既有 exclude。 |
| `runs_ops_host_checks_and_handoffs` | FAIL | with_skill 输出声称 test:docs exit 0，但锁定证据不能证明实际执行；更重要的是 handoff 明确转回 pm-agent，并未 handoff docs-agent:docs-audit，且状态仍为 blocked。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=fbc300ac993b108b7bc9444227cbb7ed573eb1c13552098c1d58a0e7b37b5d39; snapshot_sha256=5eafe1bd6e2b284ad6f37b6d1fbbe1f42eaf65a33b66520cf0b29bf9f1f821d8
- Behavior: 准确同步了基于 Compose 执行证据的 Docker 部署页面，保留 Kubernetes/Helm 边界并更新 Ops 链接；但未完成要求的 docs-agent:docs-audit handoff，change-map 覆盖无法由锁定原始证据核验。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=11b563d38b2578ae3d87ebdcecbf879a88507722530693240ccf23d5d54ede78; snapshot_sha256=43da90105ce6cb530f7c6933979ab002e5332d0134853c5fddb1567ddb366bb1
- Behavior: 创建四个部署页面并声称测试通过，但未更新 Ops 索引，页面 frontmatter 使用已验证版本值，且缺少可核验的升级/健康/回滚细节。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- runs_ops_host_checks_and_handoffs 未满足指定 handoff 目标。
- Next: 完成并明确 handoff 至 docs-agent:docs-audit；提供 change-map 的锁定文件内容或 git_blob 以完成 assertion writes_current_deployment_tree_atomically 的核验。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-008-deployment-ops-upgrade`.
- Fixture SHA-256: `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845`
- Prompt SHA-256: `47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7fe3c7ecf4038349101f98fb6f2ef19330f01c150bee2276a165994129650157`
- Metadata SHA-256: `2f78367477eb99dc045585689bae85fd3302b30aa534650ea910cd64f9bdfbbe`
- Executor SHA-256: `6c1c50885619c5add1ae9c7d9faf1fa39e905346d86059a01403ae742d286478`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_executed_deployment_evidence` | PASS | with_skill 文档明确以 Compose、.env.example 和 deployment-evidence 为依据，记录了已执行命令及结果。 |
| `writes_current_ops_upgrade_rollback` | PASS | Docker 页面记录启动、升级、健康检查 HTTP 200、回滚 v1.4.1 及回滚后健康检查；镜像页记录 v1.4.2 默认镜像和 Compose 证据。 |
| `does_not_promote_plan_to_current_state` | PASS | 部署根页明确 Kubernetes/Helm 仅为未执行计划且当前不支持，并排除 Development 源码部署。 |
| `writes_current_deployment_tree_atomically` | PASS | 锁定快照包含四个要求页面及 Ops 索引链接；change-map 已覆盖四页并保留 deploy/examples/** exclude；页面均为 unverified，git 证据显示未修改其他类别或 Release Notes。 |
| `runs_ops_host_checks_and_handoffs` | NOT_EXERCISED | 候选输出报告 npm run test:docs exit 0 并给出 audit_handoff，但锁定原始证据无法证明真实执行或已完成 docs-agent:docs-audit handoff；handoff 还标记为等待 release version 确认。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=bb744377bde0b607f5eae4a77cfc887ad0183d46b1b87558c4accb423edfb908; snapshot_sha256=5bfed455d2a3542435b69bd06f1a1c60d9856390f789db45db6a1382e60b2f91
- Behavior: 正确完成部署文档内容与索引更新，准确排除未执行 Kubernetes/Helm 范围；host-check/handoff 的真实过程无法由锁定证据核验。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=627681f12380fd138fb586b0eda57f55c0b6b0fd2cef76cc2096c72d85a8fcdf; snapshot_sha256=f682d9c12277c3d62fbd7a2ccbd5ce80652e1f21eedac19c5df3f8f93dc91b92
- Behavior: 交付了四个部署页面，但未修改 Ops 索引，且未提供可核验的 handoff 细节。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供 npm run test:docs 的原始执行证据及发往 docs-agent:docs-audit 的 handoff 记录。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-008-deployment-ops-upgrade`.
- Fixture SHA-256: `214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845`
- Prompt SHA-256: `47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a612d50c32b84c65fad3cad08aad2d416a3a33647abfa1462784c1e58022424b`
- Skill overlay SHA-256: `e55ecf59b3cd8d90a2ed4cf555bed2ad2fc2131494e0914246a868317b68f4e8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7fe3c7ecf4038349101f98fb6f2ef19330f01c150bee2276a165994129650157`
- Metadata SHA-256: `77c250a8dd394ec8e7b47c067343be0f3108a736b624b4ce31343031983a7685`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_executed_deployment_evidence` | PASS | With-skill pages cite and reflect .env.example, deploy/compose.yaml, deployment-results.md, and handoff scope; executed commands, exit statuses, health results, and environment differences are accurately represented. |
| `writes_current_ops_upgrade_rollback` | PASS | Docker pages document Compose startup, v1.4.2 upgrade, /healthz HTTP 200 with body ok, v1.4.1 rollback, and the v1.4.2 image default with Compose evidence. |
| `does_not_promote_plan_to_current_state` | PASS | The with-skill deployment index explicitly marks Kubernetes/Helm unsupported and the production migration as unexecuted, with no chart or rollout evidence. |
| `writes_current_deployment_tree_atomically` | PASS | All four required deployment pages are present with unverified frontmatter, links form the required Ops/deployment/Docker navigation, the deploy/** map is reported complete with its existing exclude, and unrelated sections are unchanged. |
| `runs_ops_host_checks_and_handoffs` | FAIL | The with-skill output explicitly reports npm run test:docs failed because the snapshot repository could not determine a committed base, contrary to the requirement that it execute and pass; the audit handoff is described as blocked. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=e381d66386b460b58796519753af5b12b68ba0a3810bc92718b9481dd0638ffe; snapshot_sha256=e939338493eb9b26f4c35c41ea6fd486e06820cdbbe940777dc5d89926737cc6
- Behavior: Produced the requested evidence-bounded deployment documentation, preserved Kubernetes/Helm as unsupported, and supplied an audit handoff, but reported the required npm run test:docs check failed.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=214f53e3513d921f93697a6af50dd22ab635d80910879e93ccbc5d847195e845; output_sha256=b946d6b9d74750f4ed46eaf3a68c7d8b698f862802a4da8432558aae7edc4f0a; snapshot_sha256=9d76f26574493449637168d2dd59a24e8c9a1957ede2e15f237a1323fbcd7660
- Behavior: Produced the requested deployment documentation and claimed 76/76 tests passed, but did not provide the required audit handoff and reported strict affected checking could not run.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane did not satisfy the required passing npm run test:docs host check.
- Next: Resolve the committed-base/snapshot repository issue and rerun npm run test:docs successfully before completing the docs-audit handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `79929cac2d8a0cd7566617f637009899090f1d90d4639070d26aca346f9cfe79` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-008-deployment-ops-upgrade`.
- Fixture SHA-256: `79929cac2d8a0cd7566617f637009899090f1d90d4639070d26aca346f9cfe79`
- Prompt SHA-256: `47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `52db6badcefada59a1d42e81de2581f06256f43c060b7699c281ab21bfb40949`
- Skill overlay SHA-256: `f896903fa1a8ae6886eb0b6365065625a2e60f6809acd0af6c7c8dc8f8f2bd40`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7fe3c7ecf4038349101f98fb6f2ef19330f01c150bee2276a165994129650157`
- Metadata SHA-256: `77c250a8dd394ec8e7b47c067343be0f3108a736b624b4ce31343031983a7685`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_executed_deployment_evidence` | PASS | With-skill documents use Compose, .env, execution results, health checks, and environment differences; they explicitly limit claims to verified evidence. |
| `writes_current_ops_upgrade_rollback` | PASS | Docker pages record Compose startup and upgrade, v1.4.2, /healthz HTTP 200 with body ok, and v1.4.1 rollback with a repeated health check. |
| `does_not_promote_plan_to_current_state` | PASS | The deployment overview explicitly labels Kubernetes/Helm as an unexecuted plan and unsupported current path. |
| `writes_current_deployment_tree_atomically` | PASS | All four required deployment pages are present with unverified frontmatter, links map the Ops/deployment/Docker hierarchy, the deploy/** map covers all four pages, and existing exclude is preserved; unrelated pages are unchanged. |
| `runs_ops_host_checks_and_handoffs` | FAIL | The with-skill output reports strict affected checking blocked by sandbox Git restrictions rather than npm run test:docs passing, and provides no evidence of the required docs-agent:docs-audit handoff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=79929cac2d8a0cd7566617f637009899090f1d90d4639070d26aca346f9cfe79; output_sha256=0649d26ced24098eef83a331d812d400e11974d3bddc8fbf493f76781f10cf7b; snapshot_sha256=35693bc63c30270df312298e3f27e4a646e9da104eb169c8a4498d4e72938628
- Behavior: Produced the required deployment documentation and evidence-bound content, while reporting strict affected checking as blocked and omitting the required handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=79929cac2d8a0cd7566617f637009899090f1d90d4639070d26aca346f9cfe79; output_sha256=7fcc044d00bf5c55aae0b06cb45aaf7854c833a6231ccf29ac800a5d235f2866; snapshot_sha256=91159ea255f1d5449d676e0a3e87b486ff6c9c85d2e0d7dfdfea6596ff6392aa
- Behavior: Produced the deployment pages and reported equivalent checks, but modified the Ops index and reported a sandbox workaround for affected checking.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane did not demonstrate a passing npm run test:docs and did not demonstrate the required docs-agent:docs-audit handoff.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `79929cac2d8a0cd7566617f637009899090f1d90d4639070d26aca346f9cfe79` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-008-deployment-ops-upgrade`.
- Fixture SHA-256: `79929cac2d8a0cd7566617f637009899090f1d90d4639070d26aca346f9cfe79`
- Prompt SHA-256: `47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1e290565a84b926a128928ccdd91365a2235adff18f999307c0a3553f0b41f34`
- Skill overlay SHA-256: `0c6a49eed1db242a95632eb0d142c1760f60ffc995c96026908ec8c0e6bd8d63`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7fe3c7ecf4038349101f98fb6f2ef19330f01c150bee2276a165994129650157`
- Metadata SHA-256: `77c250a8dd394ec8e7b47c067343be0f3108a736b624b4ce31343031983a7685`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_executed_deployment_evidence` | PASS | with_skill 文档内容与交接输出引用 Compose 配置、执行结果、健康检查及环境差异，并明确未验证的镜像元数据缺口。 |
| `writes_current_ops_upgrade_rollback` | PASS | 记录了 Compose 启动、升级、HTTP 200/healthy 成功标准、回滚至 v1.4.1 后的 /healthz 检查，并记录 AI_HUB_IMAGE 默认值及 Compose 证据。 |
| `does_not_promote_plan_to_current_state` | PASS | 明确 Kubernetes/Helm 仅为未执行计划，不属于当前支持路径，未写成已部署或可执行现状。 |
| `writes_current_deployment_tree_atomically` | PASS | with_skill 交付快照包含四个要求页面，均为 last_verified_version: unverified；现有 Ops、部署及 Docker 链接和 deploy/** change-map 覆盖符合要求，未修改无关页面。 |
| `runs_ops_host_checks_and_handoffs` | FAIL | 虽声称文档测试 76/76 通过，但同时说明严格 affected 检查未完成；且输出没有证据表明已 handoff 给 docs-agent:docs-audit。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=79929cac2d8a0cd7566617f637009899090f1d90d4639070d26aca346f9cfe79; output_sha256=83ed3756b7d1f10163934afb772c652a7cc36265a14eafef8d7c36389c38abe4; snapshot_sha256=596d8b5b2de4150a75f00858c5fd6b53ba2f6378f6a916bd0bf05c562fa34528
- Behavior: 基于执行证据生成了边界清晰、链接和元数据完整的四页部署文档；测试记录与要求的完整 test:docs 及 handoff 不足。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=79929cac2d8a0cd7566617f637009899090f1d90d4639070d26aca346f9cfe79; output_sha256=01a4576efc04c612fb33b58d97da486bff21c72052f19816cee1afdba1242330; snapshot_sha256=48d6f5e62a22386a8d4a28f723a4da5001ab65e5e9172177eb000654b762eff1
- Behavior: 生成了四个部署页面并记录了核心部署事实，但完整 npm run test:docs 未通过/未完成，未证明 handoff。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足真实通过完整 npm run test:docs 并 handoff docs-agent:docs-audit 的要求。
- Next: 补充并记录完整 npm run test:docs 成功结果，完成 docs-agent:docs-audit handoff。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-008-deployment-ops-upgrade`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `79929cac2d8a0cd7566617f637009899090f1d90d4639070d26aca346f9cfe79` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-008-deployment-ops-upgrade`.
- Fixture SHA-256: `79929cac2d8a0cd7566617f637009899090f1d90d4639070d26aca346f9cfe79`
- Prompt SHA-256: `47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7fe3c7ecf4038349101f98fb6f2ef19330f01c150bee2276a165994129650157`
- Metadata SHA-256: `77c250a8dd394ec8e7b47c067343be0f3108a736b624b4ce31343031983a7685`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_executed_deployment_evidence` | PASS | with_skill 文档以 Compose、执行结果和环境差异为依据，记录 exit 0、healthy、HTTP 200/ok，并明确未执行 Kubernetes/Helm。 |
| `writes_current_ops_upgrade_rollback` | PASS | Docker 页面记录启动、v1.4.2 升级、/healthz HTTP 200/ok 标准及 v1.4.1 回滚后检查；镜像页记录默认镜像和 pull 证据。 |
| `does_not_promote_plan_to_current_state` | PASS | 明确 Kubernetes/Helm 仅为未执行计划、当前不支持，未提供可执行现状命令。 |
| `writes_current_deployment_tree_atomically` | PASS | 四个新页面均为 last_verified_version: unverified；链接、change-map 四页覆盖及既有 exclude 均存在，git 状态显示未修改无关页面。 |
| `runs_ops_host_checks_and_handoffs` | FAIL | 输出仅称文档测试 76/76 通过，同时明确 strict affected check 因 committed base 不确定而阻塞；未提供真实 npm run test:docs 全量通过证据，也未记录 handoff docs-agent:docs-audit。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=79929cac2d8a0cd7566617f637009899090f1d90d4639070d26aca346f9cfe79; output_sha256=9019016a19653f70cb0818aeb5e6f3cc93ebaf6db66cb471f86a75ad35c0adba; snapshot_sha256=9f689dddc4182913439d236cbbca27832d0c3bc43d265ebab1272a9c8c7ce287
- Behavior: 部署文档内容、证据边界、链接和未支持范围处理正确；测试链存在 strict check 阻塞，且缺少要求的 docs-agent handoff。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47aecb4a312eb41566bd1acc858dd108cbb65075c955dc6992e37865198bfec5; fixture_sha256=79929cac2d8a0cd7566617f637009899090f1d90d4639070d26aca346f9cfe79; output_sha256=9768149d6b06621cf21cc988d9ca817dbd59dcc5e065d9c8b58fc93f69ba3c3f; snapshot_sha256=a16dd31eb47aa5618662b03b7fe95dd8688c6fb88834581c0e166daead3572b4
- Behavior: 正确概述了部署文档内容和范围，但未提供宿主检查或 handoff 证据，且页面版本元数据为 v1.4.2。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未证明 npm run test:docs 全量通过，并未执行或记录 docs-agent:docs-audit handoff。
- Next: 完成并记录 npm run test:docs 通过结果，再执行 docs-agent:docs-audit handoff。

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
- Eval: `eval-008-deployment-ops-upgrade`
- Review context: PR #166 second-round P2 fresh paired validation and fresh Codex judge

## Test Set / Fixture Version

- Fixture: current deployment-verification evidence set with confirmed `ops/deployment/` Docker page tree, shared environment reference, Ops navigation, and `deploy/**` change-map scope
- Evidence set: confirmed deployment handoff, TRD surface, `.env.example`, Compose configuration, executed deployment results, environment differences, and future-only Kubernetes/Helm plan
- Actual validation date: `2026-07-22`

## Latest Result

- Behavior result: `PASS`（with）/ `PASS`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `PARTIAL`（with）/ `PARTIAL`（without）— 依赖缺失导致宿主检查与 handoff 未执行
- Overall result: BLOCKED
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `PARTIAL`
- without_skill：Behavior `PASS` / Coverage `PARTIAL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| uses_executed_deployment_evidence | PASS | PASS | 两条 lane 均以 `deploy/compose.yaml` 和 `.eval/deployment-results.md` 为依据，记录 development/staging 启动 exit 0、healthy、`/healthz` HTTP 200 及回滚结果；页面正文明确引用这些文件（with：`deployment/index.md:39-49`；without：`deployment/index.md:28-30`）。 |
| writes_current_ops_upgrade_rollback | PASS | PASS | 两条 lane 均记录 Compose 启动/升级、`/healthz` 200、回滚到 `v1.4.1` 并复查健康状态；镜像页记录默认 `registry.example/ai-hub:v1.4.2`（with：`docker/image-sources.md:21-44`；without：`docker/image-sources.md:16-27`）。 |
| does_not_promote_plan_to_current_state | PASS | PASS | 两条 lane 都明确 Kubernetes/Helm 只有未执行计划，不作为当前支持路径（with：`deployment/index.md:21-24`；without：`deployment/index.md:24-26`）。 |
| writes_current_deployment_tree_atomically | PASS | PASS | 两条 lane 均生成四个要求页面，Ops、部署根页和 Docker 页有对应链接；`deploy/**` change-map 覆盖四页并保留 `deploy/examples/**` exclude；新页面均为 `last_verified_version: unverified`，未新增 product/design/database/release-notes 文件。 |
| runs_ops_host_checks_and_handoffs | NOT_EXERCISED | NOT_EXERCISED | 两条 lane 的 `npm run test:docs` 都因缺少 `fast-glob` 未启动完成，后置 handoff 因而未执行；这是 runner 依赖阻塞，不是 skill 行为失败。 |

未触发断言：`runs_ops_host_checks_and_handoffs`。

基础设施阻塞说明：依赖缺失（fast-glob 等）；对应断言不构成 skill 行为回归。



## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `uses_executed_deployment_evidence`: PASS. Current claims came from `deploy/compose.yaml`, `.env.example`, recorded command exits and health results, and confirmed environment differences rather than the TRD or plan alone.
- `writes_current_ops_upgrade_rollback`: PASS. The Docker runbook records development/staging startup, the `v1.4.2` pull and upgrade, `/healthz` HTTP 200 success, and rollback to `v1.4.1`; `docker/image-sources.md` owns the image coordinates and evidence boundary.
- `does_not_promote_plan_to_current_state`: PASS. Kubernetes/Helm remains an unsupported, unexecuted plan with no page or placeholder command.
- `writes_current_deployment_tree_atomically`: PASS. All four required pages exist and link to their authorities; the existing Ops navigation and `deploy/**` mapping cover them while preserving `deploy/examples/**`; all new pages remain `unverified`, and unrelated sections are unchanged.
- `runs_ops_host_checks_and_handoffs`: PASS. The judge reran `npm run test:docs` in both lanes, each exiting `0` with 76/76 tests; the with-skill report hands off to `docs-agent:docs-audit` without executing deployment and blocks version stamping until a maintainer confirms `target_release_version`.

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Used `doc_type: ops` throughout the deployment tree and produced the full environment-reference contract: type, requiredness, default, constraints, applicable class, safe example, sensitivity, activation timing, and evidence.
- Classified Development as out-of-scope, Docker as supported, and Kubernetes/Helm as unsupported; it also named missing image provenance, architecture, authentication, offline-source, logging, and data-check evidence without inventing commands.
- Kept the legacy single-page shape absent and treated the four pages, internal links, Ops navigation, and change map as one confirmed atomic scope.
- Preserved the formal `docs-agent:docs-audit` gate: missing confirmed release context leaves the handoff blocked and all pages `last_verified_version: unverified`.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- Source: a fresh lane copied from the same pristine input and run with the same `eval_metadata.json` prompt; it was instructed not to read the target skill, Agent README, eval definitions, comparison, with-skill output, or historical runs.
- The baseline also generated the four-page tree, recorded the executed Docker upgrade and rollback, excluded Kubernetes/Helm, and passed 76/76 tests.
- It was weaker than the skill lane: the root used `doc_type: landing`, the environment table omitted the complete ops contract fields, deployment-class and missing-evidence reporting was unstructured, and the `docs-agent:docs-audit` handoff did not explicitly enforce the maintainer-confirmed-version blocked state.

## Positioning Against Eval-011/012/013

- Eval-008 remains the deployment-verification regression for synchronizing already executed Docker upgrade facts into the current page tree; it no longer accepts `docs/site/ops/ai-hub-upgrade.md`.
- Eval-011 covers a full three-class existing-system backfill, eval-012 covers class-local blocking when Kubernetes/Helm evidence is missing, and eval-013 covers atomic migration from an existing aggregate deployment page.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- No with-skill assertion failures.
- The `codex exec` lane streams and reports were generated and judged, but the with-skill last-message transcript path was resolved outside its intended lane and was overwritten by the baseline run. This reduces transcript-level provenance but does not change the file-level same-input proof, independent test reruns, or assertion result.
- The strong confirmed fixture lets the baseline satisfy the five core assertions, so this eval demonstrates correctness more strongly than skill-versus-baseline discrimination.

## Next Steps

- 安装锁定依赖后重新执行 paired eval 与独立 judge；宿主检查和 handoff 成功前保持 `BLOCKED`。
- On a future rerun, use absolute `--output-last-message` paths per lane so both transcript summaries remain available to the judge.

## Runtime Artifact Policy

- Pristine input, paired lane outputs, reports, dependencies, CLI streams, transcript summary, and judge verdict remain under `tmp/eval-runs/issue-161-review-round2-20260722-2002/` and are not submitted.
- Only this comparison is durable; no generated formal page, report, transcript, verdict, `node_modules`, or diagnostics file is committed.
