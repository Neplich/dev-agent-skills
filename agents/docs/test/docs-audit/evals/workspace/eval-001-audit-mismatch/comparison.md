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
- target_skill_sha256: `a5e0bb043d61dbbb218e7d7efc08374e0d16a4d7aaa3b31817f2038830c90941`
- eval_definition_sha256: `fee749f35b3bf7110eb1c6f38c918db3407b1a46ffa3ff2613c15b835398219e`
- metadata_sha256: `23ce240f3f391bd560df8f9bbcf6e5d2ec76b8a3ffb73e38f416b3cdb2997a3a`
- fixture_sha256: `dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `218cecf9b4e5893cf80d7edfea7d7877463de8efad846bf62ba5cba015ad2ed5`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **CLEAN**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_mapped_page` | PASS | with_skill 报告明确将 `src/catalog/routes.txt` 命中 change-map 的 `src/catalog/**`，并将 `docs/site/api/catalog.md` 列为受影响正式页面。 |
| `classifies_direct_conflict_mismatch` | FAIL | 报告保留了文档 `POST /catalog/items`、代码 `GET /catalog/items`、文件/行号和影响，但将页面最终分类为 `stale`，未按断言要求分类为 `mismatch`。 |
| `blocks_with_conflict_evidence` | PASS | 报告结果为 `blocked`（pre-tag），列出方法冲突及修正文档、提交后重新审计等待办，且未返回 `ready_for_tag`。 |
| `does_not_stamp_blocked_set` | PASS | 锁定报告明确写明未盖章任何页面，未创建 candidate、anchor、handoff 或 tag；并记录目标树不存在 `.meta/releases.json`，没有对阻塞集合进行局部盖章。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=e0925172e489e3fd9bbab7496e3ea8ef30123bcc3050783052fc86ff5babc340; snapshot_sha256=a5aeee4356e215326b5f683f6990071e2c147ad95eeba09d146597e9513d2d9a
- Behavior: 完成了基于 change-map 的影响域识别、代码与文档冲突证据、blocked 阶段结论及不盖章处理，但冲突分类标签不符合断言要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=957c522c4caafc6b22e13ab36b33116fd3e3d0c4519aa297e54aa0a6a2a0fa0c; snapshot_sha256=38d1eedad6fba2558ddca5a3eeaf1e150d2558d63a04f0ac16b964f5037f41ff
- Behavior: 识别出 POST/GET 冲突和过期核验版本并给出不通过结论，但未形成结构化 blocked/pre-tag 审计结果。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 将直接冲突的页面分类为 `stale`，而断言要求分类为 `mismatch`。
- Next: 将直接文档与代码冲突的最终分类改为 `mismatch`，同时保留现有冲突证据和 blocked 结论。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
