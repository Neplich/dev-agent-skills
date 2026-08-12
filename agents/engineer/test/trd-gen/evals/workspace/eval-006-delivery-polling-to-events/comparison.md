# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-006-delivery-polling-to-events`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74` from `agents/engineer/test/trd-gen/evals/workspace/eval-006-delivery-polling-to-events`.
- Fixture SHA-256: `26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74`
- Prompt SHA-256: `4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea`
- Repository HEAD: `7ac19d358ca18ef7b2d109aeec17239bc9d0f4c0`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `241887560d0522d91eee495434f78fbbe72dd8e5d7ed6c58dce70753634045ba`
- Skill overlay SHA-256: `1701eca585dc754d5c838c067ffd884a80205302462ac0a542c908fd069ff822`
- Judge schema SHA-256: `58d5f8c73c18457a8d0864b8f5e21613dc914d57c8f96acc11ce98a78c601f05`
- Eval definition SHA-256: `ec0b30178f28a00245f34e8794f34ea3d889794c5e097f45505840818ce3d657`
- Metadata SHA-256: `c58e464b2f51cbecc05208e0f4320ff2bade980227072a25840336ba048c489e`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `updates_existing_trd` | FAIL | with_skill 的 delivery_snapshot 仅更新目标 TRD，但正文第 9 节及最终输出明确将实现计划移交给 feature-implementor，违反“不把任务路由给别人”。 |
| `body_consolidation` | FAIL | with_skill 的 TRD 正文第 5 节保留“现有 TRD 中的轮询调度与批量扫描不属于当前目标架构”，属于以状态标注保留旧方案。 |
| `removal_recorded_in_changelog` | FAIL | with_skill 的 frontmatter 没有 changelog；变更记录位于正文第 8 节，而要求记录在 frontmatter。版本号已更新为 1.2.0。 |
| `no_implementation_plan_or_code` | PASS | 锁定 delivery_snapshot 仅包含 TRD.md，没有 IMPLEMENTATION_PLAN.md、代码或测试文件；验证策略仍属于 TRD 正文内容。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea; fixture_sha256=26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74; output_sha256=2adcde8d0adc262e0c52c45024540428f657933db3a8739e95f3519a421e3f91; snapshot_sha256=549ce70cb2f5c120e7484c2e5151430005b3702f9fd0878b0b6542de98f970b4
- Behavior: 更新了目标 TRD 并切换为事件驱动，但保留了不应出现的移交信息和正文旧方案状态说明，且 changelog 位置错误。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea; fixture_sha256=26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74; output_sha256=fb374e7191c9247c57c47154649cc0caf26a04ae926eade3d427d094b75b9692; snapshot_sha256=7287e564dc77138e88eebe437956ef48b2d9ec7c5c31a07591c3826759611bf7
- Behavior: 更新目标 TRD 为事件驱动，未新增其他文件；作为对照，其正文更简洁且未显示移交信息或保留旧轮询状态说明。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 违反了不得将任务路由给其他角色的要求。
- with_skill 在正文保留了带状态标注的轮询旧方案。
- with_skill 未将删除记录写入 frontmatter changelog。
- Next: 移除 TRD 正文中的实现计划移交、角色归属和 IMPLEMENTATION_PLAN.md 路由内容。
- Next: 删除正文中“不属于当前目标架构”等轮询旧方案状态说明。
- Next: 在 frontmatter 中新增 changelog 并记录轮询方案移除，同时保留版本更新。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
