# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-001-route-design-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89` from `agents/designer/test/designer-agent/evals/workspace/eval-1-route-design-handoff`.
- Fixture SHA-256: `318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89`
- Prompt SHA-256: `6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a2af40534bea6300e7542181039cc4ea7fb5bf91ca59c58d810e2ecc81053275`
- Skill overlay SHA-256: `3e0603def6ab2fd4b5f3adf5c8eae0d13b31a6e105737c16ebc52acd20d08553`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `22532d649002dfa1851fec27c554d610e1ed3e70ab860965c5b4914f96d4ccce`
- Metadata SHA-256: `b228adbda9579c0023d949fdd52d3bd090b6ff85b7c6c2610e5202c6900dbe10`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_ux_first` | NOT_EXERCISED | Locked evidence shows a UX specification and the ui-ux-design skill was visible, but does not prove the required route selection or that it occurred first. |
| `routes_visual_followup` | NOT_EXERCISED | A visual-system.md artifact exists and visual-design was visible, but locked evidence does not prove the required route selection or sequencing. |
| `uses_real_output_filenames` | PASS | With-skill delivery evidence lists docs/design/billing-notifications/ui-ux-spec.md and docs/design/billing-notifications/visual-system.md. |
| `stops_before_code` | PASS | With-skill status contains only the two design documents; the output explicitly says React implementation was not performed, and the UX document states design does not authorize application-code changes. |
| `hands_off_to_engineer` | FAIL | The output says implementation can proceed in an engineering phase, but does not state that it should be handed to engineer-agent as required. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=39cad851b3086e2903a091eaa196344245315eb8a6a763bc4e71df6bfc5a2699; snapshot_sha256=eedf15d44de242b6a9a05554b5103c4ebcb5c67a21de61f8498313d09677e348
- Behavior: Produced the required UX and visual design documents, did not write React code, and indicated a subsequent engineering handoff, but omitted the required engineer-agent designation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=b36d60cc3bcbbc7f95249ef2c04029765c610da65ff4fa8f4887bfab41873888; snapshot_sha256=950402d4dfb8357cc07d0d9104092539a71e33d38eb86385fd6951aac0302c40
- Behavior: Implemented React files and described visual behavior, without producing the required design deliverables or respecting the design-only boundary.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output does not explicitly identify engineer-agent as the implementation handoff recipient.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-001-route-design-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89` from `agents/designer/test/designer-agent/evals/workspace/eval-1-route-design-handoff`.
- Fixture SHA-256: `318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89`
- Prompt SHA-256: `6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `516410461bd0c09f36f48a72fcff5f04e02a1fd7c3d7bf7c66ee6407ed3b789c`
- Skill overlay SHA-256: `a88badd5c39e8c98568ff4259ca011c27bd894b06440948f3ff19d0b8276099f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `22532d649002dfa1851fec27c554d610e1ed3e70ab860965c5b4914f96d4ccce`
- Metadata SHA-256: `b228adbda9579c0023d949fdd52d3bd090b6ff85b7c6c2610e5202c6900dbe10`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_ux_first` | NOT_EXERCISED | With-skill evidence shows UX deliverables, but does not record selection or invocation of ui-ux-design as the first route. |
| `routes_visual_followup` | NOT_EXERCISED | With-skill evidence shows a visual-system deliverable after the UX deliverable, but does not record handoff to visual-design. |
| `uses_real_output_filenames` | PASS | With-skill output and git status show docs/design/billing-notifications/ui-ux-spec.md and docs/design/billing-notifications/visual-system.md. |
| `stops_before_code` | PASS | With-skill output explicitly says no React implementation was made; git evidence contains only the two design documents. |
| `hands_off_to_engineer` | PASS | With-skill output explicitly states that the next step can be handed to engineer-agent for implementation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=96a7b1849791e110e3025b24a91ff147b9650248a557f804b3b993bc1b9fd554; snapshot_sha256=d94eca3eac916eb0ec61eba725348b1691d3f68b8e23b59e26a158a73ec7393b
- Behavior: Produced the required UX and visual design documents, stayed within the design boundary, and identified engineer-agent as the next implementer; routing invocation/order is not evidenced.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=05ae0a152a2e6e2c2cfb6ef235e6a62e386142808783d9f52825361967fd0f2f; snapshot_sha256=24e261783f8e891bda3037f8b9e82b3ab30ba6b87cb5cc7b8c3550f68019622e
- Behavior: Implemented React application files directly and did not produce the required design workflow or design deliverables.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
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

# Eval Result: eval-001-route-design-handoff

## Evaluation Target

- Agent: `designer`
- Skill: `designer-agent`
- Eval: `eval-001-route-design-handoff`
- Workspace: `workspace/eval-1-route-design-handoff`
- Review context: issue #196 L2-4 router single-table convergence
- Latest run: fresh isolated paired Codex validation and independent judge on 2026-08-07

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt and assertions: current `agents/designer/test/designer-agent/evals/evals.json`
- Fixture: `docs/pm/billing-notifications/PRD.md`
- With-skill source: current Designer README, `designer-agent/SKILL.md`, eval definition, fixture, and the referenced PM handoff/closeout contract; historical comparison was not read before candidate generation.
- Without-skill source: the same prompt and fixture in an isolated directory, without reading or applying Designer README, `designer-agent/SKILL.md`, with-skill output, assertions, historical comparison, or an old baseline.

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL** (5/5 declared assertions exercised)
Overall result: FAIL

## Assertion Results (Current)

- routes_ux_first: **PASS** — the current final response routes first to ui-ux-design for flow and interaction work.
- routes_visual_followup: **FAIL** — visual-design is second, but the response omits the required color, typography, and copy-tone scope.
- uses_real_output_filenames: **FAIL** — neither canonical design filename is named.
- stops_before_code: **FAIL** — no code was written, but the response does not explicitly refuse React, tests, scripts, and deployment work.
- hands_off_to_engineer: **PASS** — React implementation is assigned to engineer-agent after design.

## With-Skill Behavior (Current)

The candidate honors the PM gate and selects the two design specialists, but it
does not emit the full router contract: canonical filenames and an explicit
multi-surface engineering refusal are missing.

## Fresh Without-Skill Baseline (Current)

The baseline was regenerated before the with-skill root existed, using the
same prompt and clean fixture in an independent top-level workspace with an
isolated HOME/CODEX_HOME. It implemented a React/Vite page, clearly
differentiating the router boundary, but its behavior does not affect the
with-skill verdict.

## Failures (Current)

- Missing canonical ui-ux-spec.md and visual-system.md filenames.
- Incomplete visual-design scope and no explicit refusal covering all forbidden engineering surfaces.

## Next Steps (Current)

- Fix the router response discipline, then rerun this eval with the same isolation protocol.

## Runtime Artifact Policy (Current)

- Runtime lanes and judge evidence remain in independent /tmp workspaces and are not committed.
- Only this durable comparison is updated.

## Historical Result (Superseded: pre-#234 contract)

- Behavior result: PASS
- Coverage result: FULL (5/5 declared assertions exercised)
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


The L2-4 fallback for “范围已确认但设计类型模糊” is present in the current single `Default Routes` table. This fixture asks explicitly for both flow and visual style, so it does not exercise that fallback; no fallback behavior was inferred or counted as dynamic evidence.

## Assertion Results

| Assertion | With skill | Without skill | Evidence |
| --- | --- | --- | --- |
| `routes_ux_first` | PASS | FAIL | With skill explicitly starts with `ui-ux-design`; baseline gives generic design steps without the repository specialist route. |
| `routes_visual_followup` | PASS | FAIL | With skill explicitly follows with `visual-design`; baseline describes visual work but does not name the specialist. |
| `uses_real_output_filenames` | PASS | FAIL | With skill names both canonical files; baseline names no durable design output file. |
| `stops_before_code` | PASS | PASS | Both honor the prompt's explicit no-implementation boundary. |
| `hands_off_to_engineer` | PASS | FAIL | With skill explicitly hands implementation to `engineer-agent`; baseline only stops before implementation. |

## With-Skill Behavior

The candidate preserves `billing-notifications`, routes `ui-ux-design` before
`visual-design`, names `docs/design/billing-notifications/ui-ux-spec.md` and
`docs/design/billing-notifications/visual-system.md`, refuses React, tests,
scripts, and deployment work, and hands implementation to `engineer-agent`.
All 5 assertions pass.

## Without-Skill Baseline

The fresh baseline gives a reasonable generic design sequence and obeys the
explicit request not to implement React. It does not express the repository's
specialist names, canonical artifact filenames, or named Engineer handoff.
This provides useful differentiation on router-specific behavior.

## Failures

- None in the with-skill candidate.

## Next Steps

- Keep this eval as regression coverage for the two-specialist sequence, durable artifact names, design-only boundary, and Engineer handoff.
- Add a separate fixture only if maintainers later choose to dynamically cover the confirmed-scope/ambiguous-design fallback; this run does not fabricate that scenario.

## Runtime Artifacts Policy

Paired runtime evidence is stored only under
`tmp/eval-runs/issue-196-l2-3-4/designer-agent/eval-001-route-design-handoff/`
as `with_skill/candidate-output.md` and
`without_skill/baseline-output.md`. Runtime outputs, transcripts, verdicts,
timing data, and diagnostics must not be committed. This `comparison.md` is the
durable result.
