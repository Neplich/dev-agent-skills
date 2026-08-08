# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-010-release-notes-boundary`.
- Fixture SHA-256: `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c`
- Prompt SHA-256: `59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `b3a1a852c447e6e1ef51ed958da793390c6914ade2f68188c4962daac377d01b`
- Eval definition SHA-256: `73a1610671f9f97761837a796f3ae7908687bbe25fc17ad4582a0bb4ee5c7fae`
- Metadata SHA-256: `2352ae604513521c63a446b6d886e6c879f4a0cef5861b4ee1c9c3ee9f319eba`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `recognizes_release_communication_outcome` | PASS | with_skill 将目标识别为独立的 release-notes-gen 站内发布说明工作流，并明确不属于当前 Product 或 Ops 页面同步。 |
| `routes_complete_entry_to_site_owner` | PASS | with_skill 的交接记录包含 release-request、v1.5.0、dashboard 10→25、目标站点页面、已接受/缺失证据及站内范围，并指向负责发布说明生成与确认的 release-notes-gen。 |
| `keeps_entire_site_zero_diff` | PASS | with_skill 输出明确报告工作区零改动；git_status、git_diff 和 delivery_snapshot 均为空，docs/site 未发生写入。 |
| `preserves_external_release_boundary` | PASS | with_skill 未执行或声称执行 tag、GitHub Release 或外部发布授权；git_evidence 也显示无 ref、commit 或 reflog 变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=ee4c0704be1c0ebf38c4a861ced257d5b4ef55a2047a1e46334fbf34236d4037; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为站内发布说明交接，在证据门禁未通过时保持 docs/site 零写入，并保留站内范围与外部发布边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=9639a315ce49ce35064dd18af0d0405ef3f7dceeba83de48af8b517cc880266d; snapshot_sha256=bc547f43aa4a886d2f90ca2b86c496a089952da937a27c23de80df0e7551f995
- Behavior: 直接修改发布页面、版本列表和发布元数据，完成了用户可见产物但绕过了交接门禁与零写入要求。
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

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-010-release-notes-boundary`.
- Fixture SHA-256: `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c`
- Prompt SHA-256: `59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `b3a1a852c447e6e1ef51ed958da793390c6914ade2f68188c4962daac377d01b`
- Eval definition SHA-256: `73a1610671f9f97761837a796f3ae7908687bbe25fc17ad4582a0bb4ee5c7fae`
- Metadata SHA-256: `2352ae604513521c63a446b6d886e6c879f4a0cef5861b4ee1c9c3ee9f319eba`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `recognizes_release_communication_outcome` | PASS | 明确识别为 release 模式，列出版本页、发布列表和发布元数据，并排除 current-state Product/Ops 页面。 |
| `routes_complete_entry_to_site_owner` | PASS | 将完整 Release Notes 入口指向 `docs-agent:release-notes-gen`，列出 v1.5.0、范围、实现提交、目标站点面及支持证据。 |
| `keeps_entire_site_zero_diff` | PASS | with_skill 的 git status、git diff 和 delivery_snapshot 均显示 docs/site 零变化，并明确 gate blocked before writes。 |
| `preserves_external_release_boundary` | PASS | 明确排除 GitHub Release、tag 和发布部署；git evidence 显示无分支、提交或引用变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=e7d572d0a4a37796ca6587391ba5840914fc9d62e8420b76204f99f80ab2c1db; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为站内 Release Notes 工作流，在写入前阻塞，保留完整交接信息并保持 docs/site 零变化。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=55a4fec418f5e9c0d42c1769548a624403526442b4e8ed255c54cc1a821f893f; snapshot_sha256=ff864b63fbd2b995280123d6c03824b23490c635b0881b4139aff10edb65d800
- Behavior: 直接修改版本页、发布列表和发布元数据，并声称导航及测试已通过。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 由 pm-agent 补齐 changelog、发版流程证据和审计上下文，再交接给 docs-agent:release-notes-gen。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-010-release-notes-boundary`.
- Fixture SHA-256: `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c`
- Prompt SHA-256: `59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `b3a1a852c447e6e1ef51ed958da793390c6914ade2f68188c4962daac377d01b`
- Eval definition SHA-256: `73a1610671f9f97761837a796f3ae7908687bbe25fc17ad4582a0bb4ee5c7fae`
- Metadata SHA-256: `2352ae604513521c63a446b6d886e6c879f4a0cef5861b4ee1c9c3ee9f319eba`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `recognizes_release_communication_outcome` | PASS | With-skill output identifies a release communication workflow, naming release mode and the user-facing release-notes page, version list, metadata, and navigation surfaces. |
| `routes_complete_entry_to_site_owner` | FAIL | The output routes work to docs-agent:release-notes-gen and preserves version, scope, evidence, and target surfaces, but explicitly records target_release_version as missing and does not include the confirmed host repository in the handoff. |
| `keeps_entire_site_zero_diff` | PASS | Locked git evidence shows empty status and diff, and the output states no changes were made; delivery_snapshot is empty. |
| `preserves_external_release_boundary` | PASS | The output excludes GitHub Release/tag activity, and locked git evidence shows no ref, commit, or worktree changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=cbf7e1ffd7cd107b0d1b55f2d411fe1c432d05afa987eb6abd09cf408f0ffc61; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly recognized the release-notes workflow, preserved the zero-write and external-release boundaries, and routed to the docs owner, but the handoff omitted required confirmed entry details.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=a58f2b4a56336407f79d80c02a954c0dc6cd5c3876e626e0e0dff0de0a2926d9; snapshot_sha256=a5f25f7c75f7ca95570cec5f3aaf8e79d5348dfb498e52dcdddc724fb083168a
- Behavior: Created and modified the release page, version list, and metadata, demonstrating the fresh baseline's boundary violations.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill handoff is incomplete: it omits the confirmed host and contradicts the confirmed version by marking target_release_version as missing.
- Next: Provide the complete confirmed host, v1.5.0 version, scope, evidence boundary, and target site surfaces to docs-agent:release-notes-gen.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-010-release-notes-boundary`.
- Fixture SHA-256: `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c`
- Prompt SHA-256: `59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `b3a1a852c447e6e1ef51ed958da793390c6914ade2f68188c4962daac377d01b`
- Eval definition SHA-256: `73a1610671f9f97761837a796f3ae7908687bbe25fc17ad4582a0bb4ee5c7fae`
- Metadata SHA-256: `2352ae604513521c63a446b6d886e6c879f4a0cef5861b4ee1c9c3ee9f319eba`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `recognizes_release_communication_outcome` | PASS | with_skill 将请求识别为 release 模式，明确目标是 release-notes 页面、版本列表和元数据，并排除 Product/Ops 当前状态页面；还指定 docs-agent:release-notes-gen。 |
| `routes_complete_entry_to_site_owner` | FAIL | with_skill 没有把已确认的 host、版本和范围完整交给 Docs owner，反而将版本标为 missing，并要求先由 pm-agent 补充后再转交 docs-agent。 |
| `keeps_entire_site_zero_diff` | PASS | with_skill 输出工作区无修改；git_status、git_diff 为空，且 delivery_snapshot 为空，证明 docs/site 保持零变化。 |
| `preserves_external_release_boundary` | PASS | with_skill 的原始 git 证据显示 HEAD、branch、refs、tags 均未变化；输出也未包含外部发布执行或授权。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=2d9daa79452447cd33c851a3a9b5473f3b9fef28c9068817308851f8c615bd69; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为站内发布说明工作流，在实现证据缺失时阻止 docs/site 写入；但交接信息不完整且错误地要求先转 PM。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=1f26d79409b07ce2494f1d5e3c91b860402babe31cd4810ef7742ae1a36ed4f2; snapshot_sha256=e424917879281fb026aeeef9749b12a90b2037b02251f564fb48cf917b1bb834
- Behavior: 直接创建版本页、更新版本列表和发布元数据，产生 docs/site 写入；未体现交接或证据门禁。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完成对唯一 Docs owner 的完整交接，并错误地将已确认版本视为缺失。
- Next: 将 release-request.md 中已确认的 host、v1.5.0、dashboard 10→25、abc1500 证据边界和目标站点面完整交给 Docs owner，并明确因 abc1500 缺失而等待确认。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-010-release-notes-boundary`.
- Fixture SHA-256: `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c`
- Prompt SHA-256: `59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `73a1610671f9f97761837a796f3ae7908687bbe25fc17ad4582a0bb4ee5c7fae`
- Metadata SHA-256: `2352ae604513521c63a446b6d886e6c879f4a0cef5861b4ee1c9c3ee9f319eba`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `recognizes_release_communication_outcome` | PASS | with_skill 将请求识别为 release 站内发布说明流程，并明确路由至 docs-agent:release-notes-gen，而非 Product/Ops 当前事实同步。 |
| `routes_complete_entry_to_site_owner` | FAIL | with_skill 虽指向 Docs owner，但未交付完整的 host、版本、范围、证据边界和目标站点入口；且声称 release-request 缺少已确认版本等信息，与原始 fixture 的 scope_confirmation 及确认字段矛盾。 |
| `keeps_entire_site_zero_diff` | PASS | with_skill 声明阻塞且不写入；其 git_status、git_diff、delivery_snapshot 均为空，git evidence 也证明 docs/site 未发生变化。 |
| `preserves_external_release_boundary` | PASS | with_skill 未执行或声称执行 tag、GitHub Release 或外部发布，仅保留站内文档路由。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=dd66e18e1d168dab24823cc1381b25d37a8707a24831582be015e0545fe65068; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为 release 文档流程并阻塞写入；保持站点零变化，但未完成包含已确认入口信息的 Docs owner 交接。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=11d491cbca5217d50b6d9abf799f6a0fd29dd7b1d5368f23e7400d3bb015052c; snapshot_sha256=8cf2d42e60545b4bd208e0cac825e41a83765e5b6b99eb8f612100003a658b87
- Behavior: 直接修改并新增 v1.5.0 发布页、版本索引和发布元数据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- routes_complete_entry_to_site_owner: 未向 Docs owner 交付完整已确认入口，并对 fixture 中已有确认信息作出不实缺失判断。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-010-release-notes-boundary`.
- Fixture SHA-256: `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c`
- Prompt SHA-256: `59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a612d50c32b84c65fad3cad08aad2d416a3a33647abfa1462784c1e58022424b`
- Skill overlay SHA-256: `e55ecf59b3cd8d90a2ed4cf555bed2ad2fc2131494e0914246a868317b68f4e8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `73a1610671f9f97761837a796f3ae7908687bbe25fc17ad4582a0bb4ee5c7fae`
- Metadata SHA-256: `2b92a8a77481c502d1fcd66199a8c8461112beb365a1111e12f804f2f04909b7`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `recognizes_release_communication_outcome` | PASS | 明确识别为 Release Notes 路由，并覆盖用户版本页、版本列表、发布元数据及派生导航，不将其当作 Product/Ops 当前状态同步。 |
| `routes_complete_entry_to_site_owner` | FAIL | 明确交给 docs-agent:release-notes-gen，且保留版本、范围和目标站点，但交接内容未明确携带已确认 host，因而不是完整入口交接。 |
| `keeps_entire_site_zero_diff` | PASS | 输出声明未执行写入、工作区无文件改动；原始 git evidence 显示 docs/site 整体 status、index diff 和 worktree diff 均为空。 |
| `preserves_external_release_boundary` | PASS | 明确将 GitHub Release/tag 列为排除项，未执行或授权任何外部发布操作。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=6c08ebc65e7f0121b4407bfbde2891013f18883567c77d5089f34c569d71eedb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为站内 Release Notes 工作流，在正式入口证据不足时阻塞并保持 docs/site 零变化，交给 Docs owner。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=f82e63e3fccdfadcdedc644c7138b246402a4ae1504fa2ff8d1441a32b03dbbc; snapshot_sha256=eecf48fd57f679e383e4db0a88d639daa5c6f771912507943eb3e137142085c2
- Behavior: 直接修改版本页、版本列表和发布元数据，并声称校验通过。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 的交接明确包含版本、范围、目标站点和证据缺口，但未明确传递已确认 host，未满足完整入口交接要求。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0daa7cdcb772a6f6919dacea1ac9411135275f8c86a790e62556fe0d85f5534a` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-010-release-notes-boundary`.
- Fixture SHA-256: `0daa7cdcb772a6f6919dacea1ac9411135275f8c86a790e62556fe0d85f5534a`
- Prompt SHA-256: `59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `52db6badcefada59a1d42e81de2581f06256f43c060b7699c281ab21bfb40949`
- Skill overlay SHA-256: `f896903fa1a8ae6886eb0b6365065625a2e60f6809acd0af6c7c8dc8f8f2bd40`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `73a1610671f9f97761837a796f3ae7908687bbe25fc17ad4582a0bb4ee5c7fae`
- Metadata SHA-256: `2b92a8a77481c502d1fcd66199a8c8461112beb365a1111e12f804f2f04909b7`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `recognizes_release_communication_outcome` | PASS | With-skill output identifies a release-document workflow and names the user update page, release list, and release metadata as the produced surfaces. |
| `routes_complete_entry_to_site_owner` | FAIL | It does not hand off the confirmed host, version, scope, evidence boundary, and site surfaces to the Docs owner; instead it claims to have completed the synchronization. |
| `keeps_entire_site_zero_diff` | FAIL | Raw evidence shows docs/site mutations: metadata and index modified, and v1.5.0.md added. |
| `preserves_external_release_boundary` | PASS | The with-skill output and raw diff show no tag or GitHub Release creation or movement, and no external-release authorization is included. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=0daa7cdcb772a6f6919dacea1ac9411135275f8c86a790e62556fe0d85f5534a; output_sha256=a451b7a34dc32b8c977a55ae595bfd7d1c53ab7cdbe8f11010d942154788d93f; snapshot_sha256=4a38053a27af16600259bab9cb51a2a92d1975bb542eaeae93d81f26657ee129
- Behavior: Correctly identified the release-document surfaces and stayed within site files, but performed the forbidden site mutations and omitted the required Docs-owner handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=0daa7cdcb772a6f6919dacea1ac9411135275f8c86a790e62556fe0d85f5534a; output_sha256=fd0995f86aea25d4415a144070f93036fd4755d0fdd62fb7e64e64ad0da24fe4; snapshot_sha256=25a7959e075071547a8b4e47fdf545c6869362e948f91f0aaad6c5a2b62e92cb
- Behavior: Directly created the release page, index, metadata, and generated navigation; no handoff or zero-diff boundary.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- Missing complete handoff to the Docs owner.
- docs/site was modified despite the required zero-diff boundary.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0daa7cdcb772a6f6919dacea1ac9411135275f8c86a790e62556fe0d85f5534a` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-010-release-notes-boundary`.
- Fixture SHA-256: `0daa7cdcb772a6f6919dacea1ac9411135275f8c86a790e62556fe0d85f5534a`
- Prompt SHA-256: `59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1e290565a84b926a128928ccdd91365a2235adff18f999307c0a3553f0b41f34`
- Skill overlay SHA-256: `0c6a49eed1db242a95632eb0d142c1760f60ffc995c96026908ec8c0e6bd8d63`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `73a1610671f9f97761837a796f3ae7908687bbe25fc17ad4582a0bb4ee5c7fae`
- Metadata SHA-256: `2b92a8a77481c502d1fcd66199a8c8461112beb365a1111e12f804f2f04909b7`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `recognizes_release_communication_outcome` | PASS | With-skill output targets the version page, release list, release metadata, and generated navigation, identifying the site release-notes workflow rather than Product/Ops current-state pages. |
| `routes_complete_entry_to_site_owner` | FAIL | The output claims direct completion and does not hand off the confirmed host, version, scope, evidence boundary, and target surfaces to the Docs owner. |
| `keeps_entire_site_zero_diff` | FAIL | Raw git evidence shows modifications to docs/site/.meta/releases.json and docs/site/release-notes/index.md plus a new docs/site/release-notes/v1.5.0.md. |
| `preserves_external_release_boundary` | PASS | Raw git evidence shows no ref delta, new commits, or reflog changes, and the output mentions no tag or GitHub Release creation or publication. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=0daa7cdcb772a6f6919dacea1ac9411135275f8c86a790e62556fe0d85f5534a; output_sha256=cc23cc006ad6103e2cb48b97f3b7344a55129f0e3cc3f1bfa8614e05f933b731; snapshot_sha256=e91a1a593606b4117d2fa47fbfa162a89c28a5748b346497a13ca4dbe895072f
- Behavior: Directly modified the release metadata and index and created the version page; it avoided generated artifacts and external Git changes, but did not preserve the required handoff/zero-write boundary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=0daa7cdcb772a6f6919dacea1ac9411135275f8c86a790e62556fe0d85f5534a; output_sha256=deeeec46c1755c5adc5f965ac991e5c90103f5f520941f0793d5d045d292e940; snapshot_sha256=dcdf895e16f982800e80432e522f7718fff595dfc89409e375653f629162cd9b
- Behavior: Directly modified release metadata and index, created the version page and generated site artifacts, and reported completion.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane failed to route the complete confirmed entry to the Docs owner.
- The with_skill lane wrote three files under docs/site despite the required zero-diff handoff boundary.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0daa7cdcb772a6f6919dacea1ac9411135275f8c86a790e62556fe0d85f5534a` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-010-release-notes-boundary`.
- Fixture SHA-256: `0daa7cdcb772a6f6919dacea1ac9411135275f8c86a790e62556fe0d85f5534a`
- Prompt SHA-256: `59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `73a1610671f9f97761837a796f3ae7908687bbe25fc17ad4582a0bb4ee5c7fae`
- Metadata SHA-256: `2b92a8a77481c502d1fcd66199a8c8461112beb365a1111e12f804f2f04909b7`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `recognizes_release_communication_outcome` | FAIL | with_skill 输出宣称直接完成页面、版本列表和元数据写入，没有识别为独立的站内 Release Notes 交接工作流，也没有区分其与 Product/Ops 当前事实同步。fixture/docs/site/release-notes/README.md 明确规定这是独立的站内 Release Notes 流程。 |
| `routes_complete_entry_to_site_owner` | FAIL | with_skill 输出未交接 host_repository、confirmed_version、confirmed_scope、source_evidence、desired_site_surfaces 或 maintainer-confirmed 边界，也未路由给唯一 Docs owner；反而宣称已完成同步。 |
| `keeps_entire_site_zero_diff` | FAIL | with_skill 的 git_status 显示修改 docs/site/.meta/releases.json、docs/site/release-notes/index.md，并新增 docs/site/release-notes/v1.5.0.md 和 docs/site/.generated/；因此 docs/site 并非零变化。 |
| `preserves_external_release_boundary` | PASS | with_skill 输出和 git_evidence 未显示创建/移动 tag、创建或发布 GitHub Release，亦未混入外部发布授权；证据中的 ref_delta、new_commits 和 reflog_delta 均为空。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=0daa7cdcb772a6f6919dacea1ac9411135275f8c86a790e62556fe0d85f5534a; output_sha256=b8429c7da861f18b9b87d7ba79679c0a49ab2d3a06cef9a4eab103cb607c3eda; snapshot_sha256=bfd9a22fb265954f1f8c6e19140a164292e0cc635efee8fb31ad4f31c6250240
- Behavior: 同样直接完成站内发布材料写入，并额外生成 docs/site/.generated/；未进行交接，docs/site 非零变化，未涉及外部发布执行。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=0daa7cdcb772a6f6919dacea1ac9411135275f8c86a790e62556fe0d85f5534a; output_sha256=a346aec47dc64956c00a16528c6c18e7e2711b543e4a0a30e504716e9289e8b3; snapshot_sha256=e1ca05e5a63676d2ec8f224b2b3745a65f6b3ec81f4666fb68e73c8f63039404
- Behavior: 直接创建 v1.5.0 页面、版本列表和元数据；docs/site 发生三项变更，未完成严格影响范围检查。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未识别并执行独立 Release Notes 交接工作流。
- with_skill 未将完整已确认入口交给 Docs owner。
- with_skill 越界修改并生成了 docs/site 内容，违反零写入要求。
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

# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`
- Scenario: 从非协议化结果语义识别独立站内版本说明工作流
- Review context: issue #177 sub-batch 4c

## Test Set / Fixture Version

- Fixture version: `issue-177 discrimination restore round-1`
- Validation time: `2026-07-28 23:36:25 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-release-evals/round-1/`
- 两侧使用同一 prompt 与独立 pristine fixture；baseline 不读取目标 skill、assertions、旧 comparison 或 with-skill 输出。

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| recognizes_release_communication_outcome | PASS | PASS | 两条 lane 都产出用户版本页、发布列表和 `releases.json`；with_skill 的 `result.txt` 明确列出三类站点发布材料，without_skill 也列出相同目标。 |
| routes_complete_entry_to_site_owner | FAIL | FAIL | 两条 lane 都直接执行同步并报告“已完成”，没有将 host、版本、范围、证据边界和站点面交给 Docs owner，也没有交接记录。 |
| keeps_entire_site_zero_diff | FAIL | FAIL | 两条 lane 的实际 diff 都新增 `docs/site/release-notes/v1.5.0.md`，并修改 `index.md` 与 `.meta/releases.json`；不满足 `docs/site/` 零写入。 |
| preserves_external_release_boundary | PASS | PASS | 产物和执行记录只显示 `docs/site/` 内三处文档变更；未发现创建/移动 tag、创建或发布 GitHub Release，或混入外部发布授权。 |

未满足断言（with/without 任一 FAIL）：`routes_complete_entry_to_site_owner`、`keeps_entire_site_zero_diff`



## Leakage Surface Analysis

重做前，prompt 与 assertions 直接写出 `formal-docs-sync` 必须拒绝、四类禁止 surface、准确 specialist 名和整个站点零 diff；fixture 还声明用户正在强迫错误 owner。baseline 因此可复述完整边界。

重做后 prompt 只用“面向用户的本次更新页面、版本列表、发布元数据”描述目标结果；fixture 只保留 host、版本、范围、来源和目标站点面，不标注正确 owner 或越界结论。

## Redesign

- 按 requested outcome 而不是协议术语判断路由。
- assertions 只检查 workflow 识别、完整入口交接、当前 specialist 零写入和外部发布边界。
- 不在 prompt/assertions 中给出 specialist 名称或精确禁止路径清单。

## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `recognizes_release_communication_outcome` | PASS | FAIL | with-skill 识别独立 Release Notes workflow；baseline 直接生成页面。 |
| `routes_complete_entry_to_site_owner` | PASS | FAIL | with-skill 将 confirmed host/version/scope/evidence/surfaces 交给 `docs-agent:release-notes-gen`；baseline 无 handoff。 |
| `keeps_entire_site_zero_diff` | PASS | FAIL | with-skill 站点零写入；baseline 新增版本页并修改 index/metadata。 |
| `preserves_external_release_boundary` | PASS | PASS | 两侧均未执行 tag 或 GitHub Release。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 未加载 Product/Ops 类型模块，也未进入 current-state 页面同步。
- 直接生成站内版本说明 specialist handoff，整个 `docs/site/` 保持 pristine。
- Response SHA-256: `3941048d7ac38a20485a8f6a0101d59fa5be1b6566b64543584c531198ee9e69`。

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- baseline 自行新增 v1.5.0 页面、更新版本索引和 release metadata，并运行宿主检查。
- 它保留外部 tag/GitHub Release 零写入，但没有识别当前 specialist 的站内职责边界。
- Response SHA-256: `5b0e0bb59cf7311e9269f8ae69bbcaf1a3d22834a76d32000e0dbc6658ed8931`。

## Failures And Iterations
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Round 1 即达到区分度，无需第二轮。
- with-skill 无 assertion failure；基础设施失败 none。

## Next Steps

- 保持本例为 outcome-based routing 回归，不把 specialist 名称重新泄漏到 prompt。

## Runtime Artifact Policy

- 两 lane workspace、responses、依赖、日志和 judge verdict 仅位于 gitignored runtime，不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
