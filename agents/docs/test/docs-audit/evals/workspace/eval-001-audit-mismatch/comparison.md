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
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_mapped_page` | PASS | with_skill 输出明确写明 change-map 命中 `src/catalog/**` → `docs/site/api/catalog.md`，并列出影响页面。 |
| `classifies_direct_conflict_mismatch` | FAIL | with_skill 保留了文档 `POST`、代码 `GET` 及影响，但最终将页面标为 `stale`，不是断言要求的字面状态 `mismatch`。 |
| `blocks_with_conflict_evidence` | FAIL | with_skill 返回 `blocked` 并列出冲突证据，但待办仅要求修正文档，没有明确提出确认修文档还是修代码。 |
| `does_not_stamp_blocked_set` | PASS | with_skill 明确报告未写入；原始 trace 仅显示读取命令，没有文件变更、版本盖章或 `.meta/releases.json` 同步事件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=7bca237baf686ce37996b88eb0d514c57b8b826e0cb7d27106d6415f9a8666fd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了 change-map 影响页面、POST/GET 冲突并阻断 pre-tag，且未盖章；但分类和冲突修复待办不完全符合断言。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d4dbdcc2ce0268c7dd2fa59f4c946f0acad002c9675a3357ceee8b115ffded1; fixture_sha256=dc67ea3252d72d2cb1006bd586833469bce9e6071957244105d8c4e3b86358a2; output_sha256=5137b6df2bd3507ab326d15368a06539bdf9b44b36a4fbf1a1000955b060bd83; snapshot_sha256=17dbfa812c6103318bfc92a2497947d0b84e774b593de57a5256bcccc533ab77
- Behavior: 保存了审计报告并以 POST/GET 冲突阻断发布，但未明确呈现完整影响域和规范化阻塞流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 直接冲突的最终分类为 `stale` 而非断言要求的 `mismatch`。
- 阻塞待办未明确要求确认修正文档还是修代码。
- Next: 将直接冲突页面的最终状态按要求明确标为 `mismatch`。
- Next: 在阻塞待办中明确要求维护者确认修正文档还是修代码后再复审。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
