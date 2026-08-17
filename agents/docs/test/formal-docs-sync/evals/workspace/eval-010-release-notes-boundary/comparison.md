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
- Identity schema: `2`
- target_skill_sha256: `314b02febc2ef94201a8e1bf1080c874c355a0e47e6ac9a01b931425f08bfbd7`
- eval_definition_sha256: `73a1610671f9f97761837a796f3ae7908687bbe25fc17ad4582a0bb4ee5c7fae`
- metadata_sha256: `2352ae604513521c63a446b6d886e6c879f4a0cef5861b4ee1c9c3ee9f319eba`
- fixture_sha256: `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `b3a1a852c447e6e1ef51ed958da793390c6914ade2f68188c4962daac377d01b`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `84e19c3e634cfde176d2ff20ba8e9d25a4838db3ed1deb5def94a8d0f1d2ddd9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `recognizes_release_communication_outcome` | PASS | 输出将请求判定为 Release 模式，列出版本页、发布列表和元数据，并明确交由 docs-agent:release-notes-gen 处理。 |
| `routes_complete_entry_to_site_owner` | PASS | Sync decision 保留 release-request.md 中已确认的 host/version/scope/site surfaces，并将完整候选批次路由给 docs-agent:release-notes-gen，同时标明 abc1500 未解析的证据边界。 |
| `keeps_entire_site_zero_diff` | PASS | with_skill 的 delivery_snapshot 为空，git_status 和 git_diff 均为空；输出明确报告工作区零修改、未写入文件。 |
| `preserves_external_release_boundary` | PASS | 输出将 GitHub Release/tag creation 列为排除项，且 raw git evidence 显示无 ref、commit 或工作区变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=90bbb9064c664c4aeba33ac3d5d0bac1e802cdc70775971b4847000ec5759740; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为站内 Release Notes 工作流，完整保留路由信息，在门禁未通过时保持 docs/site 零写入，并排除外部发布执行。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=fd94f4ff7de8aba7815a04d44a7ab54d2dc614b24ab93771947fe6df576924e6; snapshot_sha256=14711a1c4f3550f2f3ccd570f65b514296f0d65ef9b7947ff1ede31b02cf8b34
- Behavior: 直接创建版本页、发布列表和元数据，产生 docs/site 变更，且未执行所需的交接与门禁。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 由 pm-agent 补发正式 Release handoff，并提供可解析的版本/tag 或真实提交、changelog/release-process 证据及 audit context。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
