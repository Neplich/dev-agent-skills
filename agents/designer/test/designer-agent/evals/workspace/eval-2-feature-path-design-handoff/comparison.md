# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-002-feature-path-design-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f51ab76601713bed8d87e8e33016aaf394374041676e06644b8b383a6a3f1ef6` from `agents/designer/test/designer-agent/evals/workspace/eval-2-feature-path-design-handoff`.
- Fixture SHA-256: `f51ab76601713bed8d87e8e33016aaf394374041676e06644b8b383a6a3f1ef6`
- Prompt SHA-256: `e85929c91fa7ac5d9cb93339a38a992d155e1c545a4c3e5f4af6c78a44404dd1`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `516410461bd0c09f36f48a72fcff5f04e02a1fd7c3d7bf7c66ee6407ed3b789c`
- Skill overlay SHA-256: `a88badd5c39e8c98568ff4259ca011c27bd894b06440948f3ff19d0b8276099f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `53f91ea5792318b5883984b62004cc098b15b6389da8f0c2233bdab77fbf2aa6`
- Metadata SHA-256: `e6f9e581a9240bd876422c7ab0f1f1ca860fda8f563a8f02f87555323c8c7b30`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_confirmed_feature_path` | PASS | with_skill 的两份设计文档均声明 feature_path 为 chat-interface/messages/history/search，并分别引用同路径的 PRD.md 与 TRD.md。 |
| `mirrors_design_outputs` | PASS | with_skill workspace_manifest 与 git_status 显示产物位于 docs/design/chat-interface/messages/history/search/ui-ux-spec.md 和 visual-system.md。 |
| `no_synonym_top_level` | PASS | with_skill 仅创建确认路径下的两个设计文件，未创建或建议任何同义/截断目录。 |
| `stops_before_code` | PASS | with_skill 输出为 UI/UX 与视觉系统设计文档，并明确设计交付结束；未输出代码、实现步骤、测试命令或补丁。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e85929c91fa7ac5d9cb93339a38a992d155e1c545a4c3e5f4af6c78a44404dd1; fixture_sha256=f51ab76601713bed8d87e8e33016aaf394374041676e06644b8b383a6a3f1ef6; output_sha256=37841a69397b5af8e1beb8639a27f6242afac4af4fb3dbbd8885410629ef003d; snapshot_sha256=9cbef1a0e6dbf848660da5743acf82736770f1b99ea436fae10b6363e76294bb
- Behavior: 生成了确认 feature_path 下的 ui-ux-spec.md 与 visual-system.md，引用对应 PRD/TRD，覆盖界面、视觉和设计交接内容。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e85929c91fa7ac5d9cb93339a38a992d155e1c545a4c3e5f4af6c78a44404dd1; fixture_sha256=f51ab76601713bed8d87e8e33016aaf394374041676e06644b8b383a6a3f1ef6; output_sha256=3499837a80a27e52b2f9cec99f0683494918ef54b22d27bcec6b7ca1f1196a7d; snapshot_sha256=388ba2eb4757225122387453c315eafbed15377e91a402f97aa8887419b50b71
- Behavior: 生成了 app.js、index.html、styles.css，实现了搜索界面并运行 node --check；未生成要求的设计交付文档。
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

# Eval Result: eval-002-feature-path-design-handoff

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-002-feature-path-design-handoff`
- Workspace: `workspace/eval-2-feature-path-design-handoff`
- Review context: issue #196 L2-4 router single-table convergence
- Latest run: fresh isolated paired Codex validation and independent judge on 2026-08-07

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt and assertions: current `agents/designer/test/designer-agent/evals/evals.json`
- Fixture documents: same-path PRD and TRD for `chat-interface/messages/history/search`
- With-skill source: current Designer README, `designer-agent/SKILL.md`, eval definition, fixture, and the referenced PM handoff/closeout contract; historical comparison was not read before candidate generation.
- Without-skill source: the same prompt and fixture in an isolated directory, without reading or applying Designer README, `designer-agent/SKILL.md`, with-skill output, assertions, historical comparison, or an old baseline.

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL** (4/4 declared assertions exercised)
Overall result: FAIL

## Assertion Results (Current)

- uses_confirmed_feature_path: **PASS** — the full four-level path and same-path PRD/TRD are preserved.
- mirrors_design_outputs: **FAIL** — ui-ux-spec.md is generated, but visual-system.md is absent.
- no_synonym_top_level: **PASS** — no synonym or truncated design directory is created.
- stops_before_code: **PASS** — the candidate stops at design handoff and routes implementation to engineer-agent.

## With-Skill Behavior (Current)

The candidate correctly preserves the canonical feature path and design-only
boundary, but narrows the request to UI/UX and omits the required visual-system
artifact.

## Fresh Without-Skill Baseline (Current)

The baseline was regenerated before the with-skill root existed, from the same
prompt and clean fixture under an isolated HOME/CODEX_HOME. It produced a
non-canonical design/code-style deliverable; this is comparison evidence only.

## Failures (Current)

- Missing docs/design/chat-interface/messages/history/search/visual-system.md.

## Next Steps (Current)

- Align router behavior with the two-artifact assertion, then rerun.

## Runtime Artifact Policy (Current)

- Runtime lanes and judge evidence remain in independent /tmp workspaces and are not committed.
- Only this durable comparison is updated.

## Historical Result (Superseded: pre-#234 contract)

- Behavior result: PASS
- Coverage result: FULL (4/4 declared assertions exercised)
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


The current prompt supplies a precise four-level feature path and asks for UI/UX and visual artifacts. It therefore does not exercise the L2-4 “范围已确认但设计类型模糊” fallback; no fallback result is inferred from this fixture.

## Assertion Results

| Assertion | With skill | Without skill | Evidence |
| --- | --- | --- | --- |
| `uses_confirmed_feature_path` | PASS | PASS | Both preserve the full path and use the same-path PRD/TRD as design inputs. |
| `mirrors_design_outputs` | PASS | FAIL | With skill uses canonical `ui-ux-spec.md` and `visual-system.md`; baseline invents `UI_UX_SPEC.md` and `VISUAL_SPEC.md`. |
| `no_synonym_top_level` | PASS | PASS | Neither candidate creates a synonym or truncated top-level directory. |
| `stops_before_code` | PASS | PASS | Both stop at design delivery without code, commands, tests, or patches. |

## With-Skill Behavior

The candidate treats `chat-interface/messages/history/search` as the only
feature path, references its exact PRD/TRD, mirrors the complete path under
`docs/design/`, names both canonical design files, and stops before
implementation. All 4 assertions pass.

## Without-Skill Baseline

The fresh baseline preserves the multi-level path and respects the explicit
no-implementation instruction, so it is strong on facts already stated in the
prompt. It fails the repository artifact-name contract by inventing
`UI_UX_SPEC.md` and `VISUAL_SPEC.md`. The skill's differentiating value in this
case is exact durable naming rather than path preservation.

## Failures

- None in the with-skill candidate.

## Next Steps

- Keep this eval as regression coverage for full feature-path mirroring and canonical design artifact names.
- Do not reinterpret the explicit design layers in this fixture as coverage of the ambiguous-design fallback.

## Runtime Artifacts Policy

Paired runtime evidence is stored only under
`tmp/eval-runs/issue-196-l2-3-4/designer-agent/eval-002-feature-path-design-handoff/`
as `with_skill/candidate-output.md` and
`without_skill/baseline-output.md`. Runtime outputs, transcripts, verdicts,
timing data, and diagnostics must not be committed. This `comparison.md` is the
durable result.
