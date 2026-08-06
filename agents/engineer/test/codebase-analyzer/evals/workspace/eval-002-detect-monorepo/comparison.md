# Eval Result: eval-002-detect-monorepo

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-002-detect-monorepo`
- Test case: detect-monorepo
- Workspace: `workspace/eval-002-detect-monorepo`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: engineer-agent 已确认需要 repo-level Project Profile，入口依据见 workspace `ENGINEERING_CONTEXT.md`。这个项目是 monorepo 吗？如果是，列出所有子项目
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `assertion_1`: with_skill final.md 明确写明“是，这是一个 pnpm monorepo”；transcript 中实际读取了 ENGINEERING_CONTEXT.md、package.json 与 pnpm-workspace.yaml，并核实 workspace 配置。
- PASS `assertion_2`: with_skill final.md 列出全部三个子项目路径：apps/api、apps/web、packages/shared；实际 workspace 中对应三个 package.json，且 pnpm workspace glob 为 apps/* 与 packages/*。

## With Skill Behavior

完整触发了仓库入口检查、workspace 配置核对和三个子项目 manifest 核对；最终输出正确判断并列出全部子项目。输入/输出 hashes 与实际 workspace 文件一致，未见写入变更。

## Without Skill Baseline

同一 fixture 下完成了 ENGINEERING_CONTEXT.md、根配置和三个子项目 manifest 的读取，输出同样正确；仅作为 baseline 对照。

## Failures / Findings

- None.
- Root cause: with_skill 按 repo-level 检查路径核实了 workspace 配置及全部 manifests，因此两个要求均满足。

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-002-detect-monorepo

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-002-detect-monorepo`
- Test case: detect-monorepo
- Workspace: `workspace/eval-002-detect-monorepo`
- Latest result: PASS (2/2 assertions) - fresh Codex paired validation completed on 2026-07-26
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: repo-level Engineering context, root workspaces metadata, `pnpm-workspace.yaml`, and three package manifests
- Fresh run: isolated paired copies under `tmp/eval-runs/issue-158-round1/engineer-a/`; baseline was regenerated from the same prompt and fixture
- Source branch: `test/issue-158-round1-thin-fixtures`

## Assertions

- PASS `assertion_1`: explicitly identifies a pnpm monorepo from both workspace markers.
- PASS `assertion_2`: lists `apps/web`, `apps/api`, and `packages/shared`.

## With Skill Behavior

The candidate tied the monorepo conclusion to both root manifests and reported every discovered workspace path with package evidence.

## Without Skill Baseline

The fresh baseline also satisfied 2/2 assertions. The fixture makes the classification explicit; the skill adds evidence structure but no assertion-level gain.

## Failures

- With-skill and baseline: none.

## Next Steps

Keep the eval as a stable positive monorepo detection case.

## Runtime Artifacts Policy

Paired outputs and scratch copies are ignored runtime artifacts and are not committed.
