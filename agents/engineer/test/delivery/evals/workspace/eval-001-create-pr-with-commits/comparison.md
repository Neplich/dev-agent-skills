# Eval Result: eval-001-create-pr-with-commits

## Evaluation Target

- Agent: `engineer`
- Skill: `delivery`
- Eval: `eval-001-create-pr-with-commits`
- Test case: create-pr-with-commits
- Workspace: `workspace/eval-001-create-pr-with-commits`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: PARTIAL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 已完成工作的 scope、changed files 与验证状态见 workspace `DELIVERY_HANDOFF.md`。代码已完成，创建 PR 并关联 Issue #123
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `assertion_1`: with_skill transcript 仅记录 git 检查因 not a git repository 失败；workspace 无 .git、无分支产物。
- FAIL `assertion_2`: 未观察到成功的 git add/commit；final 明确无法提交。
- FAIL `pr`: 未观察到 PR 创建或 PR 正文；final 明确尚未创建 PR。
- NOT EXERCISED `ci`: 未创建 PR，因此 transcript 中没有可验证的 PR CI 状态检查。

## With Skill Behavior

未完成分支、提交、PR；本地 npm test 有 transcript 证据通过。workspace 哈希与 output.sha256 一致，且无 .git。

## Without Skill Baseline

同样未完成交付；额外尝试 GitHub Issue 查询但未创建 PR。workspace 哈希与记录一致；仅作对照。

## Failures / Findings

- assertion_1: 未创建符合规范的功能分支
- assertion_2: 未产生 Conventional Commit 或其他提交
- pr: 未创建包含摘要、PM 文档引用和测试状态的 PR
- Root cause: fixture workspace 没有 Git 仓库或远端，且 GitHub 未认证，导致分支、提交、PR 无法完成；因无 PR，CI 检查未执行。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-001-create-pr-with-commits

## Evaluation Target

- Agent: `engineer`
- Skill: `delivery`
- Eval: `eval-001-create-pr-with-commits`
- Test case: create-pr-with-commits
- Workspace: `workspace/eval-001-create-pr-with-commits`
- Latest result: PASS (4/4 assertions) - fresh Codex paired validation completed on 2026-07-26
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: completed-work handoff, PM reference, changed source/test, passing test command and CI workflow
- Fresh run: both isolated copies created a feature branch and Conventional Commit, ran `npm test`, pushed a remote branch, opened a real temporary GitHub PR, and waited for hosted CI.
- Hosted evidence: with_skill [PR #170](https://github.com/Neplich/dev-agent-skills/pull/170) at `129da903c5a2be7d25d53ed58ab28d7ab77459d5`; fresh without_skill [PR #169](https://github.com/Neplich/dev-agent-skills/pull/169) at `602726696738d32095ee63225837946e247b7152`.
- Cleanup: both temporary PRs were closed without merge after validation and both remote branches were deleted.

## Assertions

- PASS `assertion_1`: creates a project-conformant feature branch.
- PASS `assertion_2`: creates a Conventional Commit.
- PASS `pr`: each side created a real GitHub PR whose body includes a summary, canonical PM document, Issue #123 and passing tests.
- PASS `ci`: each side waited for hosted `repository-contract`, `eval-contract`, `doc-contract` and `python-tests`; all eight checks completed with `SUCCESS`.

## With Skill Behavior

The candidate verified scope and tests, staged only scoped files, completed branch/commit/push/PR delivery, and waited for all hosted CI checks before reporting success.

## Without Skill Baseline

The fresh baseline independently created PR #169 and waited for all four hosted CI checks, so it also satisfied 4/4 assertions. The skill adds a more explicit staged-scope review and CI evidence structure, but the assertions do not distinguish it.

## Failures

- With-skill and baseline: none.

## Next Steps

Keep the temporary-PR cleanup rule and hosted CI evidence requirement explicit in future paired runs.

## Runtime Artifacts Policy

Scratch `.git` directories, responses and diagnostics are ignored and not committed. Temporary PRs are retained only as closed GitHub evidence; their remote branches were deleted.
