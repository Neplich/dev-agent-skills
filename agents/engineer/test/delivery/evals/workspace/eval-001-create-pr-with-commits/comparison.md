# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `delivery`
- Eval: `eval-001-create-pr-with-commits`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a095496c94e4d4b145d5e90f01a6091f49d20133f7d6a46767163e94951ca30c` from `agents/engineer/test/delivery/evals/workspace/eval-001-create-pr-with-commits`.
- Fixture SHA-256: `a095496c94e4d4b145d5e90f01a6091f49d20133f7d6a46767163e94951ca30c`
- Prompt SHA-256: `0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d8742c44909649093ebfd76f53e0380f026aead8c232886c1d2e7539530c12ba`
- Skill overlay SHA-256: `9a91a658fe435c4f94cd090875022e1f797b535eb5aaab293c42b59f3c59e4c3`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `b5822c83e3f8caaca6208116252c535c386e189fa49ac7a53ede27f87da189e1`
- Metadata SHA-256: `42b78bc31afd3489f9b95efe4ac09505680dc657c70f69ef4c4abe87e352e812`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feature_branch_created` | FAIL | with_skill git_evidence shows branch unchanged from main to main; no feature branch was created. |
| `meaningful_commit_created` | FAIL | with_skill git_evidence shows HEAD unchanged, no new commits, and no ref delta. |
| `pr` | FAIL | with_skill output explicitly states that no PR was created; therefore it contains no summary, PM document reference, or test status. |
| `ci` | FAIL | with_skill output provides no CI run or status check and states that no PR was created. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=a095496c94e4d4b145d5e90f01a6091f49d20133f7d6a46767163e94951ca30c; output_sha256=b0b7c47e4aaacd76d143e0d47193fb752d0b92adb0a14d078958e513f0dffcde; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Ran tests and correctly identified the clean tree, missing remote, and unavailable gh; made no branch, commit, PR, or CI check.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=a095496c94e4d4b145d5e90f01a6091f49d20133f7d6a46767163e94951ca30c; output_sha256=f0c47136186cddad0398dbe5a02240862bb194231ab678c2555d6fb6326c23ab; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Ran tests, created fix/notification-status-123, and made an empty Conventional Commit; did not create a PR or check CI.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane did not create the required feature branch.
- The with_skill lane did not create a meaningful commit.
- The with_skill lane did not create a PR with the required information.
- The with_skill lane did not check CI status.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

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
