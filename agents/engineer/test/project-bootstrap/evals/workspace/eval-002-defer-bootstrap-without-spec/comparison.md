# Eval Result: eval-002-defer-bootstrap-without-spec

## Evaluation Target

- Agent: `engineer`
- Skill: `project-bootstrap`
- Eval: `eval-002-defer-bootstrap-without-spec`
- Test case: defer-bootstrap-without-spec
- Workspace: `workspace/eval-002-defer-bootstrap-without-spec`
- Classification: (a) fixture 已足够，只缺 fresh baseline。空 workspace 本身就是“无 TRD、PRD 或其他已确认 spec”的负向证据；prompt 也没有显式 skip-PM override，因此不需要添加 fixture 文件。
- Latest result: PASS (3/3 assertions) - no-answer-key fresh Codex paired validation completed on 2026-07-26 at 15:33 CST.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: empty workspace with only eval metadata and this durable comparison; no product or engineering spec is present.
- Prompt: `这是一个空目录。我想做一个 AI 对话助手，左侧是会话列表，右侧是聊天区。`
- Expected output: identify the missing approved spec, defer scaffolding to `pm-agent:idea-to-spec`, and preserve only the explicit skip-PM override.
- Fresh run: two isolated fresh Codex generation contexts produced a new with-skill response and a new without-skill response from the same prompt and empty workspace. No historical baseline or prior response text was reused.

## No-Answer-Key Method

1. Before generation, the runner read only this workspace's `eval_metadata.json` to obtain the original prompt and enumerated the workspace to confirm that, apart from metadata and this durable comparison, it contained no fixture evidence.
2. The with-skill generator received only the original prompt, the empty-fixture fact, `agents/engineer/README.md`, and `project-bootstrap/SKILL.md`. It was explicitly denied `evals.json`, expected output, assertions, this comparison, network access, and repository search. Its response was locked before baseline generation.
3. A separate fresh baseline generator received only the same original prompt and an independently empty directory. It did not read or apply any Agent README, skill, eval definition, expected output, assertion, or comparison. Its response was locked independently.
4. Only after both candidates were locked did the judge read `evals.json` and the existing canonical comparison, then assess both candidates against the three assertions below.

No candidate response, transcript, verdict, timing file, output directory, or diagnostic was written into the repository.

## Assertions

- PASS `assertion_1`: the with-skill response explicitly says that no TRD, PRD, or other approved PM document exists and bootstrap/scaffold must not start by default.
- PASS `pm`: the with-skill response redirects requirement convergence and documentation to `pm-agent:idea-to-spec` without selecting a framework or running initialization.
- PASS `override`: the with-skill response permits bootstrap before stable PM docs only when the user explicitly asks to skip PM and scaffold directly.

## With Skill Behavior

The newly locked with-skill candidate followed the required stop branch. It stated that the empty workspace contains no TRD, PRD, or other approved PM document, declined to begin bootstrap/scaffold by default, pointed to `pm-agent:idea-to-spec`, and said work can resume after PM documents stabilize or earlier only under an explicit skip-PM instruction. It did not ask stack questions, recommend a framework, provide initialization commands, or create files.

With-skill result: 3/3 assertions passed.

## Without Skill Baseline

The independently locked baseline treated the request as authorization to build from scratch. It restated the two-panel layout, offered React, Vue, and native web choices, recommended React + TypeScript, and proposed proceeding with mock responses by default. It did not initialize files during the response, but it did not identify missing approved PRD/TRD as a bootstrap gate, route the request to `pm-agent:idea-to-spec`, or preserve an explicit skip-PM-only override.

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
