# Eval Result: eval-002-defer-bootstrap-without-spec

## Evaluation Target

- Agent: `engineer`
- Skill: `project-bootstrap`
- Eval: `eval-002-defer-bootstrap-without-spec`
- Test case: defer-bootstrap-without-spec
- Workspace: `workspace/eval-002-defer-bootstrap-without-spec`
- Classification: (a) fixture 已足够，只缺 fresh baseline。空 workspace 本身就是“无 TRD、PRD 或其他已确认 spec”的负向证据；prompt 也没有显式 skip-PM override，因此不需要添加 fixture 文件。
- Latest result: PASS (3/3 assertions) - fresh Codex paired subagent validation completed on 2026-07-26 at 15:16 CST.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: empty workspace with only eval metadata and this durable comparison; no product or engineering spec is present.
- Prompt: `这是一个空目录。我想做一个 AI 对话助手，左侧是会话列表，右侧是聊天区。`
- Expected output: identify the missing approved spec, defer scaffolding to `pm-agent:idea-to-spec`, and preserve only the explicit skip-PM override.
- Fresh run: the current Codex subagent generated a new with-skill response and a new without-skill response from the same prompt and empty workspace. No historical baseline or prior response text was reused.

## Assertions

- PASS `assertion_1`: the with-skill response explicitly says that no TRD, PRD, or other approved PM document exists and bootstrap/scaffold must not start by default.
- PASS `pm`: the with-skill response redirects requirement convergence and documentation to `pm-agent:idea-to-spec` without selecting a framework or running initialization.
- PASS `override`: the with-skill response permits bootstrap before stable PM docs only when the user explicitly asks to skip PM and scaffold directly.

## With Skill Behavior

The fresh with-skill result followed the required stop branch. It stated that the empty workspace contains no TRD, PRD, or other approved spec, declined to begin bootstrap by default, pointed to `pm-agent:idea-to-spec`, and said work can resume after PM documents stabilize or earlier only under an explicit skip-PM instruction. It did not ask stack questions, recommend a framework, provide initialization commands, or create files.

With-skill result: 3/3 assertions passed.

## Without Skill Baseline

The fresh baseline treated the prompt as an early product idea: it restated the two-panel layout and proposed clarifying technology, model/API, persistence, authentication, and deployment choices before implementation. It did not initialize files, but it also did not identify the absence of approved PRD/TRD as the reason to stop, route the request to `pm-agent:idea-to-spec`, or state the explicit skip-PM override.

Without-skill result: 0/3 assertions passed.

## Failures

- With-skill: none.
- Without-skill: `assertion_1`, `pm`, and `override` failed.

## Risks

- This is intentionally a negative empty-workspace fixture. Adding synthetic specs would invalidate the scenario rather than strengthen it.
- A generic baseline may independently choose not to scaffold an underspecified idea, but that alone does not satisfy the repository-specific PM routing and explicit override assertions.

## Next Steps

Keep the workspace empty and retain this eval as the no-spec bootstrap stop-branch regression case.

## Runtime Artifacts Policy

Only this canonical `comparison.md` is durable. Fresh response text, transcripts, verdicts, timing, outputs, and diagnostics are runtime artifacts and must not be committed.
