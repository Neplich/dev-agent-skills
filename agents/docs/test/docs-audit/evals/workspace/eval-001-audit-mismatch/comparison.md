# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-001-audit-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2` from `agents/docs/test/docs-audit/evals/workspace/eval-001-audit-mismatch`.
- Identity schema: `2`
- target_skill_sha256: `5b11b38c1c44c386fe19122dfb1ce5918b2bfbc4830ad32aa994d8a7e39f35e7`
- eval_definition_sha256: `fee749f35b3bf7110eb1c6f38c918db3407b1a46ffa3ff2613c15b835398219e`
- metadata_sha256: `23ce240f3f391bd560df8f9bbcf6e5d2ec76b8a3ffb73e38f416b3cdb2997a3a`
- fixture_sha256: `dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `218cecf9b4e5893cf80d7edfea7d7877463de8efad846bf62ba5cba015ad2ed5`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_mapped_page` | PASS | 锁定报告的 Change-map evidence 明确记录任务落点为 `src/catalog/routes.txt`，匹配 `src/catalog/**`，并将 `docs/site/api/catalog.md` 列为 required document。 |
| `classifies_direct_conflict_mismatch` | PASS | 锁定报告的受影响页面表明确记录文档声明 `POST /catalog/items`，目标代码证据路径为 `src/catalog/routes.txt` 的目标 blob，声明 `GET /catalog/items`，最终状态为 `mismatch`。 |
| `blocks_with_conflict_evidence` | PASS | 锁定报告明确给出 `phase_result: blocked`，列出文档修订、版本面确认和禁止创建 tag 等阻塞待办；报告及最终输出均未返回 `ready_for_tag`。 |
| `does_not_stamp_blocked_set` | PASS | 锁定报告明确写出 `No unified stamp was applied`，受审页面仍为 pre-stamp `v1.0.0`，且目标树不存在 `.meta/releases.json`；没有证据表明进行了局部盖章或同步。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=fb7ef2ded615d505acf383493c9ab536e582cd621b4c9a470648912b4a392e49; snapshot_sha256=94423e6ed9f809094469434d2c55980a02af36aaf2c10e1729ad556b1e1713c2
- Behavior: 保存并提交了有证据链的 pre-tag 审计报告，正确识别影响域、直接 mismatch，并以 blocked 阻止盖章和发布授权。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=c3183ce9a456eae2f06457d583f913c28bbde4040e12ce3d0527c0e3c4262e41; snapshot_sha256=54736999aba7af935ed2830968971c41892ce375e86a75ab488d3bf60db3985b
- Behavior: 新鲜基线保存了报告并识别 POST/GET 冲突及过期版本，但未明确呈现完整 change-map 影响域、blocked 阶段和阻塞集合盖章决策。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 更新 `docs/site/api/catalog.md` 为 `GET /catalog/items`，确认版本化发布面后重新执行审计。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
