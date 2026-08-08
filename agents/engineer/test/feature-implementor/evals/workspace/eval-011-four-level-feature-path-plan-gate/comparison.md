# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-011-four-level-feature-path-plan-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `6c438d1edc9a89256655ae36e972b31a4929ddc7fe5b5f285e888975f24e8b68` from `agents/engineer/test/feature-implementor/evals/workspace/eval-011-four-level-feature-path-plan-gate`.
- Fixture SHA-256: `6c438d1edc9a89256655ae36e972b31a4929ddc7fe5b5f285e888975f24e8b68`
- Prompt SHA-256: `e0c7bd09477fcc6f52d75011fdf516c41f01082c930d49e3864459c1ec60e40b`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7d6cafded24992611b95dfc908abe3d7611f7857dadb745152c30089566b43d2`
- Metadata SHA-256: `3668a072214fe6498899f002deadbb563dcff96e3a3df4bc0dd68e0b0df02057`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_matching_four_level_docs` | PASS | With-skill output identifies PRD/TRD alignment; plan metadata references both exact four-level paths, whose fixture frontmatter confirms feature_path chat-interface/messages/history/search. |
| `writes_four_level_plan_path` | PASS | Raw git status and workspace manifest show only docs/engineer/chat-interface/messages/history/search/IMPLEMENTATION_PLAN.md created; no forbidden paths appear. |
| `preserves_feature_metadata` | PASS | Plan frontmatter contains feature_path, parent_feature, feature_level 4, related_prd, and related_trd with the required values. |
| `includes_scope_and_checks` | PASS | Plan lists the two expected implementation/test files and the deterministic targeted npm test command plus diff review. |
| `waits_for_user_confirmation` | PASS | Output explicitly asks the user to confirm the implementation plan before coding. |
| `does_not_implement_directly` | PASS | With-skill git evidence shows only an untracked implementation plan, empty diff, and no source/test modifications or implementation claims. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e0c7bd09477fcc6f52d75011fdf516c41f01082c930d49e3864459c1ec60e40b; fixture_sha256=6c438d1edc9a89256655ae36e972b31a4929ddc7fe5b5f285e888975f24e8b68; output_sha256=a83356415dc332bad9814a8834687b8b8e674e4c550805235ecfac2d744e0d9e; snapshot_sha256=9b0c163a18e54ed20536b32a2eaab6669db9b6be1ea3b7bf569323cec98a5fc4
- Behavior: Created the correctly nested implementation plan with required metadata, scope, validation, and confirmation gate; did not implement code.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e0c7bd09477fcc6f52d75011fdf516c41f01082c930d49e3864459c1ec60e40b; fixture_sha256=6c438d1edc9a89256655ae36e972b31a4929ddc7fe5b5f285e888975f24e8b68; output_sha256=5502c168fdff4b9d311eedbd7b77a7a59b14436b5aa276f42c81315382d221f6; snapshot_sha256=9e93b2821e8a707798573a40afd23660847c646cf3bc4643db820b257844dd11
- Behavior: Implemented source and test changes directly, without creating the required plan or awaiting confirmation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

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

# Eval Result: eval-011-four-level-feature-path-plan-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-011-four-level-feature-path-plan-gate`
- Test case: four-level-feature-path-plan-gate
- Workspace: `workspace/eval-011-four-level-feature-path-plan-gate`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: docs/pm/chat-interface/messages/history/search/PRD.md 和 docs/engineer/chat-interface/messages/history/search/TRD.md 已确认。请实现消息历史搜索。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `reads_matching_four_level_docs`: transcript 命令读取并列出两份精确路径文档；计划 frontmatter 也引用了对应 PRD/TRD 路径，并确认 feature_path。
- PASS `writes_four_level_plan_path`: 实际 workspace 存在 docs/engineer/chat-interface/messages/history/search/IMPLEMENTATION_PLAN.md，final 链接为该精确路径；未发现错误路径计划。
- PASS `preserves_feature_metadata`: 计划 frontmatter 包含 feature_path、parent_feature、feature_level、related_prd、related_trd。
- PASS `includes_scope_and_checks`: 计划列出 service/test 文件范围、workspace 过滤、排序、空结果和输入不变性，并列出确定性验证命令。
- PASS `waits_for_user_confirmation`: final 明确写明“请确认此计划后，我再开始实现”；计划状态为 Planned，transcript 仅记录 IMPLEMENTATION_PLAN 文件新增。
- PASS `does_not_implement_directly`: with_skill 的源代码和测试 hash 与输入一致，transcript 无代码/测试修改事件；final 未声称已实现或验证。

## With Skill Behavior

成功完成四级 feature_path 门禁，写入镜像 IMPLEMENTATION_PLAN，并等待确认；未直接编码。exit_code=0，计划 hash 与 output.sha256 一致。

## Without Skill Baseline

对照组未读取/引用四级 PRD/TRD 路径，也未创建实施计划，直接修改 service/test 并声称验证通过；源文件 hash 与输入不同。

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-011-four-level-feature-path-plan-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-011-four-level-feature-path-plan-gate`
- Test case: four-level-feature-path-plan-gate
- Workspace: `workspace/eval-011-four-level-feature-path-plan-gate`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`, `docs/pm/chat-interface/messages/history/search/PRD.md`, `docs/engineer/chat-interface/messages/history/search/TRD.md`, `src/chat-interface/messages/history/search-service.ts`, and `tests/chat-interface/messages/history/search-service.test.ts`.
- Fixture summary: PRD and TRD both declare `feature_path: chat-interface/messages/history/search`, `parent_feature: chat-interface/messages/history`, and `feature_level: 4`; fixture source/test files give concrete scope for message-history search.
- Expected output: create or update `docs/engineer/chat-interface/messages/history/search/IMPLEMENTATION_PLAN.md`, preserve feature metadata, include file scope and deterministic checks, and wait for user confirmation before coding.

## Assertions

- PASS `reads_matching_four_level_docs`: PRD/TRD paths and frontmatter match at four levels.
- PASS `writes_four_level_plan_path`: the planned output path mirrors the full feature path, not a flattened or parent path.
- PASS `preserves_feature_metadata`: plan frontmatter requires `feature_path`, `parent_feature`, `feature_level`, `related_prd`, and `related_trd`.
- PASS `includes_scope_and_checks`: the plan includes `search-service.ts`, `search-service.test.ts`, and deterministic validation commands.
- PASS `waits_for_user_confirmation`: coding starts only after the exact plan is confirmed.
- PASS `does_not_implement_directly`: no source/test edits or verification claims happen during planning.

## With Skill Behavior

Fresh with-skill validation confirmed that the feature path gate supports deep feature trees. The current skill should accept the matching PRD/TRD pair, keep the direct specialist gate satisfied by the equivalent confirmed document chain, target `docs/engineer/chat-interface/messages/history/search/IMPLEMENTATION_PLAN.md`, preserve `feature_path: chat-interface/messages/history/search`, `parent_feature: chat-interface/messages/history`, `feature_level: 4`, `related_prd`, and `related_trd`, list source/test scope, and wait for confirmation.

## Without Skill Baseline

The fresh without-skill baseline was summarized before reading skill docs. A generic implementation planner might plan the code changes from the PRD/TRD, but it could collapse the path to `docs/engineer/history-search/IMPLEMENTATION_PLAN.md`, `docs/engineer/chat-interface/history-search/IMPLEMENTATION_PLAN.md`, or `docs/engineer/chat-interface/IMPLEMENTATION_PLAN.md`. It would not reliably enforce four-level metadata preservation or the exact confirmation gate.

## Failures

- None.

## Next Steps

- Keep this eval focused on successful four-level PRD/TRD alignment entering the mirrored plan gate.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
