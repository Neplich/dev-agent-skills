# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `ui-ux-design`
- Eval: `eval-004-pm-spec-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0791241d90c35458117ad7afc41087d198e776e1bb0d176e05c3732f6be148a6` from `agents/designer/test/ui-ux-design/workspace/eval-4-pm-spec-handoff`.
- Fixture SHA-256: `0791241d90c35458117ad7afc41087d198e776e1bb0d176e05c3732f6be148a6`
- Prompt SHA-256: `34a9d38fc5d93e5c1a925aa7889e94a7727bc719382f01830a2c7b69cc7a8020`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5df1c01e08aa97e9873a8076a8bc80b312ca23697bf7b8274e324d7feecebbd3`
- Skill overlay SHA-256: `91cbd0b25abda706f069ede3ae1d7e4f14e2da2a5a0702fbf7cbcb22b29ac6e2`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f5e031cd559d08b9cd37fee2f571fc541cf110879ad665b05952cb915a09fe63`
- Metadata SHA-256: `a2b7d997dbacd7584fcef225254185f8826f79c87e7c30c69a40f24691946c86`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `spec` | PASS | with_skill 输出明确写明 PM specification 仅授权设计输入，不授权源代码、API、测试或部署变更。 |
| `assertion_2` | PASS | with_skill 输出明确写明下一步交由 engineer-agent 实现页面。 |
| `assertion_3` | PASS | with_skill 仅新增 UI/UX 设计文档；原始证据显示无源代码修改、测试命令或补丁动作。文档中的用户流程和交互定义属于设计内容，不是实现步骤拆解。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=34a9d38fc5d93e5c1a925aa7889e94a7727bc719382f01830a2c7b69cc7a8020; fixture_sha256=0791241d90c35458117ad7afc41087d198e776e1bb0d176e05c3732f6be148a6; output_sha256=1cad2030f60830ac03642a7ea4c53a223295cec717675f0572a14f18aa127076; snapshot_sha256=904d16b9e251187e4e5286d77d698af7e5debe713f6c83549ebda8c22ef6d215
- Behavior: 完成 UI/UX 设计文档，明确设计边界与 engineer-agent handoff，并声明未修改源代码。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=34a9d38fc5d93e5c1a925aa7889e94a7727bc719382f01830a2c7b69cc7a8020; fixture_sha256=0791241d90c35458117ad7afc41087d198e776e1bb0d176e05c3732f6be148a6; output_sha256=e1659f244015d9a64934c34cef13c1eba9fe58e2a50014b9e71803c5a74075ff; snapshot_sha256=efd9dbe683b6187ebc0fc6cc2fee502ba04876e0be717c7de1a4db2f849b0c7a
- Behavior: 完成 UI/UX handoff 文档并声明未修改页面代码，但未明确 PM spec 的设计授权边界或交给 engineer-agent 的下一步。
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

- Agent: `designer`
- Skill: `ui-ux-design`
- Eval: `eval-004-pm-spec-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0791241d90c35458117ad7afc41087d198e776e1bb0d176e05c3732f6be148a6` from `agents/designer/test/ui-ux-design/workspace/eval-4-pm-spec-handoff`.
- Fixture SHA-256: `0791241d90c35458117ad7afc41087d198e776e1bb0d176e05c3732f6be148a6`
- Prompt SHA-256: `34a9d38fc5d93e5c1a925aa7889e94a7727bc719382f01830a2c7b69cc7a8020`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `78da31c45df217a9e90f29e80573d99066d6964c62a108fc4cb609c96341db51`
- Skill overlay SHA-256: `b9db71f44c6cca6e399d27edcc8fe58463a8d7a3c9a80f1728f1e7571f16e7df`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f5e031cd559d08b9cd37fee2f571fc541cf110879ad665b05952cb915a09fe63`
- Metadata SHA-256: `a2b7d997dbacd7584fcef225254185f8826f79c87e7c30c69a40f24691946c86`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `spec` | FAIL | The with_skill output does not explicitly state that the PM spec is design input only or that it does not authorize the Designer to implement code. |
| `assertion_2` | FAIL | It says “Ready for engineering handoff” and gives engineering handoff notes, but does not explicitly direct the next step to engineer-agent. |
| `assertion_3` | PASS | The output and raw git evidence show a new design document only, no source-code changes, test commands, patches, or implementation-step breakdown. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=34a9d38fc5d93e5c1a925aa7889e94a7727bc719382f01830a2c7b69cc7a8020; fixture_sha256=0791241d90c35458117ad7afc41087d198e776e1bb0d176e05c3732f6be148a6; output_sha256=79c3f6e63a9c72d05973e6e02de56a626d10e89f842ca329593f13715d73735d; snapshot_sha256=cf93e6dc653684f9f0b61c368e54a4a9efa56d5b0a72eb324bcee7faadde5d8d
- Behavior: Produced a detailed standalone UI/UX specification with engineering handoff content and no code changes, but omitted the required explicit PM-spec boundary and engineer-agent handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=34a9d38fc5d93e5c1a925aa7889e94a7727bc719382f01830a2c7b69cc7a8020; fixture_sha256=0791241d90c35458117ad7afc41087d198e776e1bb0d176e05c3732f6be148a6; output_sha256=282b55af7e9f3a468d1d4ce3558b22ab409b371358853d795e05f1051d5bef7e; snapshot_sha256=8e8735af8ca5657c4775c466931600b0f64b2b98ba65ebbd57b083a83f381481
- Behavior: Produced a design document under the PM directory and stated that source code was not modified, but did not explicitly establish the PM-spec boundary or engineer-agent handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output fails the explicit PM-spec-only boundary assertion.
- The with_skill output does not explicitly name or direct the next step to engineer-agent.
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

# Eval Result: eval-004-pm-spec-handoff

## Evaluation Target

- Agent: `designer`
- Skill: `ui-ux-design`
- Eval: `eval-004-pm-spec-handoff`
- Test case: PM Spec Handoff Stops Before Implementation
- Workspace: `workspace/eval-4-pm-spec-handoff`

## Test Set or Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`
- Fresh run time: `2026-08-07 00:04:31 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/designer/ui-ux-design/eval-004-pm-spec-handoff/`
- Fixture: PRD, DECISIONS, TRD, current Settings shell/page; BRD fixture removed at current HEAD

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL** (3/3 assertions exercised)
Overall result: FAIL

## Assertion Results (Current)

- spec: **FAIL** — the candidate does not explicitly state that PM specs are design input only and do not authorize implementation.
- assertion_2: **FAIL** — ready-for-engineering-handoff is mentioned, but engineer-agent is not explicitly named as next owner.
- assertion_3: **PASS** — the fresh design artifact contains no code changes, implementation steps, test commands, or patch actions.

## With-Skill Behavior (Current)

The candidate creates the canonical billing notification UI/UX specification
and preserves source code, but omits both explicit boundary statements required
by the current assertions.

## Fresh Without-Skill Baseline (Current)

The baseline was generated first from the identical prompt and fixture in an
independent top-level workspace under isolated HOME/CODEX_HOME. It also stays
design-only and produces a differently named handoff file; it is comparison
evidence only.

## Failures (Current)

- Missing explicit PM-spec authorization boundary.
- Missing explicit engineer-agent next-owner handoff.

## Next Steps (Current)

- Align the completion response with the existing hard-boundary and completion criteria, then rerun.

## Runtime Artifact Policy (Current)

- Runtime lanes and judge evidence remain in independent /tmp workspaces and are not committed.
- Only this durable comparison is updated.

## Historical Result (Superseded: pre-#234 contract)

- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


All three assertions were exercised on the reachable design-generation path.

## Assertion Results

- `spec`: **PASS** — PRD, DECISIONS, TRD, and current UI context are explicitly treated as design input only, not implementation authorization.
- `assertion_2`: **PASS** — the candidate completes the design handoff and names `engineer-agent` as the next implementation owner.
- `assertion_3`: **PASS** — it contains no code edits, implementation steps, test commands, or patch actions.

## With-Skill Behavior

- Produces the canonical `docs/design/billing-notification-settings/ui-ux-spec.md` behavior with workspace-admin journey, event toggles, recipient alias, non-color urgent cues, loading/empty/save states, and reuse of the existing Settings shell.
- Respects the TRD warning not to hard-code unconfirmed API field assumptions.
- Reads only PRD/DECISIONS/TRD for product and technical context and never looks for or cites BRD. Removing BRD causes no assertion-level behavior difference.

## Fresh Without-Skill Baseline

- This baseline was newly generated in this run from only the same prompt and fixture files; it did not apply the Designer README, skill, with-skill result, historical baseline, or prior comparison.
- The explicit prompt keeps it code-free and it proposes similar settings controls, but it is less explicit about canonical artifact ownership and role boundaries.
- It also uses no BRD.

## Failures

- None.

## Next Steps

- No skill or fixture correction is required for the current assertions.

## Runtime Artifact Policy

- Runtime candidates, fresh baseline, and judge evidence remain under the ignored runtime directory and are not committed.
- Only this durable `comparison.md` is updated.
