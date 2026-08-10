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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `6b892e000764d0f52ab1e2bbfd237e12483caafd3413b84144f2d3397ea92558`
- Skill overlay SHA-256: `2811fdd3c57db7a2738883046d1d787b9d794bcfbf96919af99fd2eac7160676`
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
| `updates_existing_trd` | FAIL | 更新了目标 TRD 并提升版本，但正文和交接说明将后续任务路由给 feature-implementor。 |
| `body_consolidation` | FAIL | TRD 正文仍包含“定时轮询”及固定间隔扫描等旧方案引用，未将旧方案仅留在 changelog。 |
| `removal_recorded_in_changelog` | PASS | frontmatter 新增 changelog，记录轮询架构移除，并将版本从 1.1.0 更新为 2.0.0。 |
| `no_implementation_plan_or_code` | PASS | 锁定交付快照仅修改 TRD；没有新增 IMPLEMENTATION_PLAN.md、代码或测试文件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea; fixture_sha256=26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74; output_sha256=995575cf288647ae9264256d2b25a7b345f3af67e539159cf39c4075adba8a42; snapshot_sha256=6e00306ef44807451b572c6825fe5016d492d7f7cef48fe7adc6b31dbe0ca79c
- Behavior: 更新了 TRD、事件驱动正文和 changelog，但保留旧方案正文引用并包含后续任务交接路由。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4d55ba6ecaf12e0a768970bba911c34982402774916977cdba5d537398d0d4ea; fixture_sha256=26621a90d557560b63afa9dd1b1ebe2dbb9f05568b574efca78ec5babe092c74; output_sha256=821c19e9bd266f3fcc19c5ac2d57606b8ed3481203f4776665ab086bf8e0641b; snapshot_sha256=0349c3510bb90c79366c3ebcb8c77a19d6bab3d0935ee0038800c4f3ac09dcc3
- Behavior: 更新了目标 TRD 为事件驱动方案并移除正文中的轮询引用，但未提供 changelog 记录。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill lane retains legacy polling references in the TRD body.
- with_skill lane explicitly routes the next task to feature-implementor.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
