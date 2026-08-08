# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `delivery`
- Eval: `eval-001-create-pr-with-commits`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e` from `agents/engineer/test/delivery/evals/workspace/eval-001-create-pr-with-commits`.
- Fixture SHA-256: `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e`
- Prompt SHA-256: `0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3291b3bf29fbba656cfab581113b3724f453df2f593ee385dae5e746a6649c65`
- Skill overlay SHA-256: `67f626d08e11b0e8b9b347a8746142889487e1229a1dc34e7b49ca498c9a191d`
- Judge schema SHA-256: `eaac8d5ec4179daca7a6c1c98e4847ae0114d9d33168a84593f70ca6474abe10`
- Eval definition SHA-256: `7e02d3842aadb84c2bf63d29c927cc522ebed52b96eed1878122982c38563924`
- Metadata SHA-256: `ddad21037c097d13ee42c91b495c2c2326e53dc9044ae9a3b160a51decc6ffbb`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feature_branch_created` | PASS | git_evidence shows branch changed from main to fix/notification-status, with a new reachable branch ref. |
| `meaningful_commit_created` | PASS | The new commit subject is `fix: support archived notification status`, which follows Conventional Commits. |
| `pr` | FAIL | PR creation was correctly blocked and a preview was provided, but it incorrectly states `PM/PRD: 未提供` even though docs/pm/notifications/PRD.md exists; the required PM document reference is missing. |
| `ci` | PASS | No PR was created; the output reports CI unavailable, explains the remote/gh blockers, and provides a `gh pr checks <pr-number> --watch` recovery command without claiming CI results. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=281d70f06ea6b27502fbdd0f8641181b4b0e71dc1a0c07c2c640febb1063a040; snapshot_sha256=f0a9567b9f3ce3a4b5807827e70497510104912c63c94dd2369e71d511624ac8
- Behavior: Created a compliant feature branch and meaningful commit, passed tests, and accurately blocked PR/CI operations, but produced an incomplete and inaccurate PR preview by omitting the existing PM/PRD.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=b113a55c2c44a825438bb7abddb0c60611107f54b987a22a2d9d612804b82634; snapshot_sha256=81d39d912af6a09f9968c5f2d1bbfffbee4780dc5e0180b61b4fc1364d31578e
- Behavior: Created a compliant feature branch and meaningful commit and reported the remote/Issue blocker, but did not provide the required PR preview or explicit CI handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The PR preview omits the existing PM/PRD reference and falsely says it was not provided.
- Next: Update the PR preview to reference docs/pm/notifications/PRD.md, then create the PR once a remote and gh are available.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `delivery`
- Eval: `eval-001-create-pr-with-commits`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e` from `agents/engineer/test/delivery/evals/workspace/eval-001-create-pr-with-commits`.
- Fixture SHA-256: `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e`
- Prompt SHA-256: `0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3291b3bf29fbba656cfab581113b3724f453df2f593ee385dae5e746a6649c65`
- Skill overlay SHA-256: `67f626d08e11b0e8b9b347a8746142889487e1229a1dc34e7b49ca498c9a191d`
- Judge schema SHA-256: `eaac8d5ec4179daca7a6c1c98e4847ae0114d9d33168a84593f70ca6474abe10`
- Eval definition SHA-256: `7e02d3842aadb84c2bf63d29c927cc522ebed52b96eed1878122982c38563924`
- Metadata SHA-256: `ddad21037c097d13ee42c91b495c2c2326e53dc9044ae9a3b160a51decc6ffbb`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feature_branch_created` | PASS | with_skill 的 git_evidence 显示分支从 main 创建为 fix/notification-status。 |
| `meaningful_commit_created` | PASS | with_skill 创建了 commit，消息为 `fix: support archived notification status`，符合 Conventional Commits。 |
| `pr` | PASS | with_skill 明确说明 remote 和 gh 不可用、PR 尚未创建，并提供包含摘要、Closes #123、PRD 引用和测试状态的 PR 预览。 |
| `ci` | PASS | with_skill 未声称 PR 或 CI 已存在，说明 CI unavailable 及阻塞原因，并提供恢复后的 `gh pr checks <pr-number> --watch` 命令。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=012324204aab411d4fe3cae8ba3bdc467e24ef7cdbc427ac6ed78e1ef7a42c8b; snapshot_sha256=d0ff950256ab415c67bae31bd56abd2e79db8d3e83e619be62ac02bfa6970824
- Behavior: 完成分支创建、规范提交和本地测试；在 remote/gh 不可用时如实提供 PR 预览并说明 CI 不可用。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=54339ba8f03bd0c294b11db2e1c118c15e5b9dcecd6a7ab1e75e7d0575525b71; snapshot_sha256=b29c586532524c2daa13467c8aff824702de9596b15c58439bfffa8555ba7df7
- Behavior: 完成提交和本地测试，但仍在 main 分支，且仅说明 PR 阻塞，未提供完整 PR 预览或 CI 恢复信息。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `delivery`
- Eval: `eval-001-create-pr-with-commits`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e` from `agents/engineer/test/delivery/evals/workspace/eval-001-create-pr-with-commits`.
- Fixture SHA-256: `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e`
- Prompt SHA-256: `0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3291b3bf29fbba656cfab581113b3724f453df2f593ee385dae5e746a6649c65`
- Skill overlay SHA-256: `67f626d08e11b0e8b9b347a8746142889487e1229a1dc34e7b49ca498c9a191d`
- Judge schema SHA-256: `eaac8d5ec4179daca7a6c1c98e4847ae0114d9d33168a84593f70ca6474abe10`
- Eval definition SHA-256: `7e02d3842aadb84c2bf63d29c927cc522ebed52b96eed1878122982c38563924`
- Metadata SHA-256: `ddad21037c097d13ee42c91b495c2c2326e53dc9044ae9a3b160a51decc6ffbb`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feature_branch_created` | PASS | Git evidence shows branch changed from main to fix/notification-status, with a new branch ref. |
| `meaningful_commit_created` | PASS | Commit subject `fix: support archived notification status` follows Conventional Commits. |
| `pr` | FAIL | With_skill correctly reports no remote/gh blocker and does not claim a PR exists, but its PR preview omits the required PM document reference. |
| `ci` | PASS | No PR exists; the output states CI was not run, explains the blocker, and provides `gh pr checks <pr-number> --watch` for recovery. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=82715278a666775ce9e1265f4b0e9635aa459d67cf56e24fd289e08dbca32c4f; snapshot_sha256=d8a300f37c850d8e6aa2963a8787428476dbedd8ad97fa5469dcd48051b0c67a
- Behavior: Created a feature branch and Conventional Commit, verified tests, and accurately reported PR/CI blockage; PR preview was incomplete.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=c594452166bdb10f10fce2b3b622be022cecd856098414f7241aa68119579af0; snapshot_sha256=0b94c7e6f8d167c6a6daacef079921d50578b6e14c533e4f188913806b34bae2
- Behavior: Created a feature branch and commit and reported the missing remote, but provided less complete PR-blockage details.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The PR preview does not include a PM documentation reference as required.
- Next: Include the PM document reference and test status explicitly in the blocked PR preview.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `delivery`
- Eval: `eval-001-create-pr-with-commits`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e` from `agents/engineer/test/delivery/evals/workspace/eval-001-create-pr-with-commits`.
- Fixture SHA-256: `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e`
- Prompt SHA-256: `0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3291b3bf29fbba656cfab581113b3724f453df2f593ee385dae5e746a6649c65`
- Skill overlay SHA-256: `67f626d08e11b0e8b9b347a8746142889487e1229a1dc34e7b49ca498c9a191d`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7e02d3842aadb84c2bf63d29c927cc522ebed52b96eed1878122982c38563924`
- Metadata SHA-256: `ddad21037c097d13ee42c91b495c2c2326e53dc9044ae9a3b160a51decc6ffbb`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feature_branch_created` | PASS | with_skill 的 git_evidence 显示从 main 创建并切换到 fix/archived-notification-status，符合功能分支命名规范。 |
| `meaningful_commit_created` | PASS | with_skill 创建了提交 b51458a，message 为 fix: support archived notification status，符合 Conventional Commits。 |
| `pr` | FAIL | 正确说明远程和 gh 不可用且未声称 PR 已创建，并提供了预览；但预览未包含 PM 文档引用，未满足要求的同等字段。 |
| `ci` | FAIL | 正确说明 PR 不存在且 CI 未运行，但未提供恢复后用于检查 CI 状态的命令；恢复命令仅包含添加远程、推送和创建 PR。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=6edffcb5aaf10618654bf2ed5e120460e66350d1603fe786279c0b6a8ad36fa1; snapshot_sha256=c7406f2a869f9fb8c60732f257f294d28c65d46ed11f26ff14aec44b8053b677
- Behavior: 创建了规范功能分支和提交，正确识别 PR/CI 阻塞并提供预览，但缺少 PM 文档引用和 CI 恢复后的检查命令。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=40eff5779b72fbb846ed434a11bb645ed359e241cb4f5d8404092382a1d79ab9; snapshot_sha256=374014e9a2583dcb83ae1db018ca31a5da48330fb5b8583edd07333b8cbdcf46
- Behavior: 完成提交和本地测试，但停留在 main，未提供 PR 预览或 CI 状态说明。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- PR 预览缺少 PM 文档引用。
- 未提供恢复后检查 CI 状态的命令。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `delivery`
- Eval: `eval-001-create-pr-with-commits`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e` from `agents/engineer/test/delivery/evals/workspace/eval-001-create-pr-with-commits`.
- Fixture SHA-256: `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e`
- Prompt SHA-256: `0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2f50028ba86c6f445df96f26b38139e690cf6231ad89fac0774b234a0c5dc4e1`
- Skill overlay SHA-256: `127b8414687cc98a6277b223b3da3a183d31df3a096ba31b6f0085951eea2cb0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7e02d3842aadb84c2bf63d29c927cc522ebed52b96eed1878122982c38563924`
- Metadata SHA-256: `ddad21037c097d13ee42c91b495c2c2326e53dc9044ae9a3b160a51decc6ffbb`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feature_branch_created` | PASS | With-skill git evidence shows a new branch, fix/notification-status-archived, created from main; this is a conventional feature/fix branch name. |
| `meaningful_commit_created` | PASS | With-skill evidence shows commit cb91d95 with message "fix: support archived notification status", which follows Conventional Commits. |
| `pr` | FAIL | The with-skill output correctly states that no remote is configured and does not claim a PR exists, but it omits the required equivalent PR preview containing a summary, PM document reference, and test status. |
| `ci` | FAIL | The with-skill output does not fabricate CI results and explains that CI cannot be read without a remote/PR, but it does not clearly state CI has not run or provide the recovery check command. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=93614ae236a3b99bb2ab4b262e5fe799579182f9b68aa174731d974a20a4e9d0; snapshot_sha256=c9853f1b2ac021262786d97ce56fd5daf79c2cb47f3d4cfcbfd8df0f56ac4b76
- Behavior: Created a conventional branch and commit, verified tests, and accurately reported the missing remote without claiming PR or CI success; it omitted the required PR preview and explicit CI-not-run recovery command.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=0cf1d08c6ba0536acdf9211a45c40f19349a2a3098f6ad2258884a6e0863c677; snapshot_sha256=a5c53293f01c0465635a468b5d10319a8d9c44b0790ecbd22b68c9389781e833
- Behavior: Created a conventional branch and commit, verified tests, and accurately reported that PR creation was blocked by the missing remote; it did not provide a PR preview or CI recovery guidance.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill lane omits the required fallback PR preview when remote/PR creation is blocked.
- The with-skill lane omits an explicit CI-not-run statement and recovery check command.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `delivery`
- Eval: `eval-001-create-pr-with-commits`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e` from `agents/engineer/test/delivery/evals/workspace/eval-001-create-pr-with-commits`.
- Fixture SHA-256: `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e`
- Prompt SHA-256: `0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2f50028ba86c6f445df96f26b38139e690cf6231ad89fac0774b234a0c5dc4e1`
- Skill overlay SHA-256: `127b8414687cc98a6277b223b3da3a183d31df3a096ba31b6f0085951eea2cb0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7e02d3842aadb84c2bf63d29c927cc522ebed52b96eed1878122982c38563924`
- Metadata SHA-256: `ddad21037c097d13ee42c91b495c2c2326e53dc9044ae9a3b160a51decc6ffbb`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feature_branch_created` | PASS | With-skill git evidence shows branch changed from main to fix/notification-status and the new ref was created. |
| `meaningful_commit_created` | FAIL | The commit message is 'Fix notification status labels', which is meaningful but does not follow Conventional Commits, and no project-specific convention evidence is provided. |
| `pr` | FAIL | The candidate correctly reports that no remote and no gh command prevent PR creation, but it does not provide the required equivalent PR preview containing summary, PM document reference, and test status. |
| `ci` | FAIL | Because no PR exists, CI should be reported as not run with the blocking reason and a recovery check command; the candidate omits this CI status and command. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=83bafe40d6d3dc1eb7f9ad9fe77d7860d9937564f6796893a597c1e6232fcae6; snapshot_sha256=1c3e1f9d7e663f41231d261de35de1a7ee99b4f2f8cce451085f9b5052abe2d7
- Behavior: Created a feature branch, committed the change, ran tests, and reported a clean worktree and PR blocking, but used a non-Conventional commit message and omitted the required PR preview and CI-not-run details.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=308028c695aa88aa0e0310701a038df0251e185ccd13a2861cab3f84ea5f62ff; snapshot_sha256=d4f21218fa65fdb625ce789d421e60b468e50554e83edcf96eb8f5140d6a3e88
- Behavior: Created a feature branch and Conventional Commit, ran tests, and truthfully reported PR blocking due to no configured remote, but did not provide the required PR preview or CI status.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill commit message does not satisfy the stated commit convention.
- The with_skill output omits the required fallback PR preview.
- The with_skill output omits explicit CI-not-run status, blocking reason, and recovery command.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `delivery`
- Eval: `eval-001-create-pr-with-commits`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e` from `agents/engineer/test/delivery/evals/workspace/eval-001-create-pr-with-commits`.
- Fixture SHA-256: `415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e`
- Prompt SHA-256: `0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `29c61c58a2652bd07f18ba26bb25b18563fce087002096b0bb5e8a06424417c0`
- Skill overlay SHA-256: `32d24578ed344a6ae666c9852e0b693b2f910e584a7849849063e01d95ab66e2`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `7e02d3842aadb84c2bf63d29c927cc522ebed52b96eed1878122982c38563924`
- Metadata SHA-256: `ddad21037c097d13ee42c91b495c2c2326e53dc9044ae9a3b160a51decc6ffbb`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `feature_branch_created` | PASS | With-skill git evidence shows branch changed from main to fix/notification-status-archived, matching the project naming convention. |
| `meaningful_commit_created` | PASS | With-skill git evidence shows commit subject "fix: support archived notification status", following Conventional Commits. |
| `pr` | FAIL | The with-skill lane correctly says no PR was created because origin and gh were unavailable, but it does not provide the required equivalent PR preview containing a summary and PM document reference. |
| `ci` | FAIL | No PR exists, but the with-skill output does not explicitly state that CI did not run or provide the required recovery check command. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=1d359072460cdae68a5885ef00b47037bbad3380ffbb6c17592277a5ec320759; snapshot_sha256=c269de167a1757b1af1a25742753ad3f86b03d7ce9a6a881ef3c91aa16ee840f
- Behavior: Created the correctly named branch and a Conventional Commit; accurately avoided claiming a PR, but omitted required PR preview fields and explicit CI-not-run recovery guidance.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0b44a24f8cc1cd09df29f861e75c80120390e6bd31b5f661fccd1e0a1e7be7a5; fixture_sha256=415df27ebd271a5c6f0949b6abe147a826b07a65acc211cf3185fa0d7f9c490e; output_sha256=f7d3fd4032a759cd17b085bbfcfb62d2c84b7564d484796ff7cdfaecd79823b8; snapshot_sha256=2b3d763c9cb60b526e29c4d4eff2b193f6a83c16a0ef04fa67dbd12b12b9beae
- Behavior: Created the correctly named branch and a Conventional Commit; reported PR blockage but did not provide the required PR preview or CI blockage details.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output lacks a complete PR preview with summary and PM document reference.
- The with-skill output does not explicitly state CI was not run and omit a recovery check command.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
