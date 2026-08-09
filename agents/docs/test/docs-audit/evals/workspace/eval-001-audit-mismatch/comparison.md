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
- Fixture SHA-256: `dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2`
- Prompt SHA-256: `8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `218cecf9b4e5893cf80d7edfea7d7877463de8efad846bf62ba5cba015ad2ed5`
- Eval definition SHA-256: `fee749f35b3bf7110eb1c6f38c918db3407b1a46ffa3ff2613c15b835398219e`
- Metadata SHA-256: `23ce240f3f391bd560df8f9bbcf6e5d2ec76b8a3ffb73e38f416b3cdb2997a3a`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_mapped_page` | PASS | 报告明确依据 `src/catalog/routes.txt` diff 和 `docs/site/standards/change-map.yaml`，将 `docs/site/api/catalog.md` 纳入影响范围。 |
| `classifies_direct_conflict_mismatch` | PASS | 报告保留文档 `POST /catalog/items`、代码 `src/catalog/routes.txt:1` 的 `GET /catalog/items`、证据路径及影响，并将结论标为 `mismatch`。 |
| `blocks_with_conflict_evidence` | PASS | 报告的 `phase_result` 为 `blocked`，列出 API 冲突及修正文档或代码的待办，并明确不存在 `ready_for_tag` handoff。 |
| `does_not_stamp_blocked_set` | PASS | 报告明确未应用统一版本盖章；交付快照仅新增审计报告，正式文档和元数据未被修改，且固定 candidate 路径保持缺失。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=e9fcc25a2c7649ac6a35f7fc3351c5d46223799136dc1319f75280709b95f57c; snapshot_sha256=7fc9f4c4cfdb79f3a09e796d47ea364f3887a0360f1d8472bc53955ec1afa7a8
- Behavior: 正确识别变更映射、直接文档冲突及 mismatch，阶段判定为 blocked，并保持阻塞集合未盖章。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=c906eeff03195dca2cf471e44ca4623d03e1eabc01d0cc213d3bd7dcaec86bf5; snapshot_sha256=a3b11312e73a9274413ae4733fd1cff2bea89be990dab56c1b45197058347a2f
- Behavior: 新鲜基线识别出 POST/GET 冲突并报告 FAIL，但未在交付报告中充分呈现变更映射与完整阻塞审计细节。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
