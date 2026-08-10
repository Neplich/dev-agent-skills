# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c0e7350515f9e8f3a166039b0e6d074b044f7918d0abfcaabf64ea0fd4ef53cb` from `agents/engineer/test/feature-implementor/evals/workspace/eval-017-abandoned-draft-can-be-superseded`.
- Fixture SHA-256: `c0e7350515f9e8f3a166039b0e6d074b044f7918d0abfcaabf64ea0fd4ef53cb`
- Prompt SHA-256: `9ebe9d873c66a07a5ecd0428e103d2f74136e9e17f4f22b79640f42f218d18ee`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1b3ba014c732559fe2d85e84b85c8db967bb14f4b1fc850a2267e7d4ee1cf03b`
- Skill overlay SHA-256: `7f72b0d2378eefdc164735f00c26c14522753a42e538abe02ba7accda3b0a9f5`
- Judge schema SHA-256: `a264d3282fcfebf29821ed24d8e702134594b3cc4be72cd72f03b0e03e92c160`
- Eval definition SHA-256: `92bf4838a78758f537ca7650dd1be190ad947406f8ab40d6ace62d644c28dc37`
- Metadata SHA-256: `21a9c9ae11f8c9b8058a429c319a4f2a640a6b07fdf2d71e259bbc158caa4e24`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_unfinished_active_plan` | PASS | with_skill 的锁定命令事件读取了 `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`，输出包含原始 `status: "Draft"`、路径及 `implementation_scope: "refund-reason-codes"`。 |
| `detects_explicit_abandonment` | PASS | 归档快照的 `superseded_reason` 明确记录维护者放弃未完成退款原因码计划，且新计划 Alignment 说明该计划已明确 abandoned 并改走 Superseded 路径。 |
| `archives_as_superseded` | PASS | 归档快照包含 `status: "Superseded"`、非空 `superseded_reason`、`implementation_scope`、`archived_at`、`archive_approved_by`、`source_plan` 及 `preserved_original_metadata`。 |
| `links_replacement_plan` | PASS | 新 active plan 的 `previous_plan_archive` 指向同 `payment-refund` feature_path 下的 Superseded 归档文件。 |
| `waits_before_coding` | PASS | 锁定交付快照仅包含计划与归档文档；git 状态无代码变更。计划明确写明 awaiting explicit user confirmation，确认前禁止 implementation、QA handoff、delivery 等后续动作。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9ebe9d873c66a07a5ecd0428e103d2f74136e9e17f4f22b79640f42f218d18ee; fixture_sha256=c0e7350515f9e8f3a166039b0e6d074b044f7918d0abfcaabf64ea0fd4ef53cb; output_sha256=99df502a86666ee800d5c546e388f8e78236098a75b662568cd89f3f1b709cdf; snapshot_sha256=f0629dff30e1e097e2544b30489ea0aac667602f4fedaae5968269c990915989
- Behavior: 读取原 Draft 计划后，识别显式废弃，归档为 Superseded，创建回链归档的新审核流程计划，并停在用户确认门禁前。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9ebe9d873c66a07a5ecd0428e103d2f74136e9e17f4f22b79640f42f218d18ee; fixture_sha256=c0e7350515f9e8f3a166039b0e6d074b044f7918d0abfcaabf64ea0fd4ef53cb; output_sha256=d008401c09531582abbae6e3b11e549b012444c900bab2e2cb1f3c523614add6; snapshot_sha256=bda9a06a7066bd276a46ada0d72f32d4dee328982f45622b99318286fb8219d3
- Behavior: 作为 fresh baseline 直接修改 active 计划为 Superseded、创建新计划并实现代码，未完成要求的独立归档元数据与确认门禁。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
