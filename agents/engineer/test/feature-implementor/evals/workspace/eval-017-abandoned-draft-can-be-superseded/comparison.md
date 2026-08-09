# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b` from `agents/engineer/test/feature-implementor/evals/workspace/eval-017-abandoned-draft-can-be-superseded`.
- Fixture SHA-256: `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b`
- Prompt SHA-256: `3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e820a1098a32d64fe76bdf4ec719cd859ebecfdb70fa28be1309b656ec71bd22`
- Skill overlay SHA-256: `226a387f9ef93d9f4c106e1f240f22e5014d390eeb37da0fd61da0c129ca36ba`
- Judge schema SHA-256: `a264d3282fcfebf29821ed24d8e702134594b3cc4be72cd72f03b0e03e92c160`
- Eval definition SHA-256: `d59f332d9689221834dd583c1a569fa62e1de4ce2c4c1d7f5aa087aed088bd53`
- Metadata SHA-256: `21a9c9ae11f8c9b8058a429c319a4f2a640a6b07fdf2d71e259bbc158caa4e24`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_unfinished_active_plan` | PASS | with_skill 明确给出 active_plan_path、原状态 Draft；归档文件内容保留 implementation_scope: refund-reason-codes。 |
| `detects_explicit_abandonment` | PASS | 归档文件的 superseded_reason 明确记录维护者放弃未完成退款原因码轮次并转向退款审核流程。 |
| `archives_as_superseded` | FAIL | 归档文件为 Superseded 且有非空 superseded_reason，并保留 implementation_scope；但缺少 archive_approved_by，且使用 archive_date/archived_from 而非要求的 archived_at/source_plan。 |
| `links_replacement_plan` | NOT_EXERCISED | with_skill 要求 TRD 更新后生成新的 IMPLEMENTATION_PLAN.md，并标记等待确认；当前快照未交付替代计划，因此该后续步骤尚未可执行。 |
| `waits_before_coding` | PASS | 快照仅修改计划文档、未修改代码；输出将实现等下游动作标为 blocked，并明确 confirmation_required。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=6b0818d0110323c05dfafdf7acc47a5488e5b4f8a2656a37d47037f33dbc610e; snapshot_sha256=5c69ebe72c6122710d815aec1c919391055e24943a81a577a3fc7c3e8191dd3c
- Behavior: 识别并归档了已放弃的 Draft 计划为 Superseded，保留了原计划主体 metadata，并在编码前等待确认；但归档 metadata 不完整，替代计划尚未交付。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=fcdd9eeaaae5cd709b1c1cc841eb38d8355b25a9b78d0a84d3437a833a484f80; snapshot_sha256=9376e94e955c4dcaedaae10925e482fc12581b8fb001b5b00e0c62070b739a50
- Behavior: 直接覆盖原 Draft 计划，将实施范围改为 refund-review；未按要求归档原计划、建立替代计划回链或等待确认。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 归档文件缺少 assertion 要求的 archive_approved_by，且未提供 archived_at/source_plan 字段。
- Next: 补齐归档文件的 archived_at、archive_approved_by、source_plan 字段。
- Next: 在 TRD 完整且获得确认后生成新的 IMPLEMENTATION_PLAN.md，并通过 previous_plan_archive 回链归档文件。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
