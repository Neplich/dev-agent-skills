# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `ui-ux-design`
- Eval: `eval-003-with-reference`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `816b980f73797aa0bb179996356d70da27810eb91a7ac7c665a793e71da22e00` from `agents/designer/test/ui-ux-design/evals/workspace/eval-003-with-reference`.
- Fixture SHA-256: `816b980f73797aa0bb179996356d70da27810eb91a7ac7c665a793e71da22e00`
- Prompt SHA-256: `1d07d7029ac6afd6bdd8b3a0c089a71197a6e0caee2ba8f44e93457b9bde08dd`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `78da31c45df217a9e90f29e80573d99066d6964c62a108fc4cb609c96341db51`
- Skill overlay SHA-256: `b9db71f44c6cca6e399d27edcc8fe58463a8d7a3c9a80f1728f1e7571f16e7df`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `36f115852952f11f54a62c4ef547a3782cf81881da967b1b9e5b272fbfbef0f5`
- Metadata SHA-256: `1297d3b18067ef541e85c715177821c621d61aa5e828ddc8a5fd239236e4a6ab`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 文档明确提炼了参考模式：克制导航、单一首屏主张、产品证明、编号章节、深层锚点和移动端纵向阅读，并说明了原创转译方式。 |
| `assertion_2` | PASS | with_skill 输出声明仅完成设计文档；git 状态仅有 docs/design/ 下的新文档，git diff 为空，未见前端工程或编码改动。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1d07d7029ac6afd6bdd8b3a0c089a71197a6e0caee2ba8f44e93457b9bde08dd; fixture_sha256=816b980f73797aa0bb179996356d70da27810eb91a7ac7c665a793e71da22e00; output_sha256=68cb0bfc14e7e27abf8bebbc93957f75131bae689f131c652934b796417addfc; snapshot_sha256=f7ecdf5aebdb008049396681946a189d35ccc870941e53aa5c3762b0b4ebe101
- Behavior: 完成更明确的原创设计交接，包含参考模式转译说明、用户旅程、原型、组件和交互规范；明确停止于设计文档阶段，未修改前端代码。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1d07d7029ac6afd6bdd8b3a0c089a71197a6e0caee2ba8f44e93457b9bde08dd; fixture_sha256=816b980f73797aa0bb179996356d70da27810eb91a7ac7c665a793e71da22e00; output_sha256=082d2958ee3a0d3a81a6d8dfd77c61d570d8fcd348956daaa01afc78666b81bf; snapshot_sha256=71aeded60b1c74fb7ea51b2760a66027f45f1d8237490008903674ddd67cd54c
- Behavior: 完成原创 UI/UX 设计文档，包含参考模式相关的信息架构与交互规格；仅产生设计文档，未见前端实现。
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

# Eval Result: eval-003-with-reference

## Evaluation Target

- Agent: `designer`
- Skill: `ui-ux-design`
- Eval: `eval-003-with-reference`
- Test case: Design with Reference Website
- Workspace: `workspace/eval-003-with-reference`

## Test Set or Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`
- Fresh run time: `2026-08-07 00:04:31 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/designer/ui-ux-design/eval-003-with-reference/`
- Fixture: confirmed PM handoff, PRD, and stable Linear reference-pattern record

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL** (2/2 assertions exercised)
Overall result: PASS

## Assertion Results (Current)

- assertion_1: **PASS** — the fresh ui-ux-spec.md extracts Linear navigation, hero, workflow, CTA, and motion patterns with an explicit adaptation boundary.
- assertion_2: **PASS** — the output stops at UI/UX specification and creates no frontend implementation artifacts.

## With-Skill Behavior (Current)

The candidate uses the confirmed PM scope and stable reference record, verifies
the live reference, produces the canonical artifact, and remains in design-only
scope.

## Fresh Without-Skill Baseline (Current)

The baseline was generated before the with-skill root existed, using the same
prompt and fixture in an independent top-level workspace under isolated
HOME/CODEX_HOME. It also meets the broad assertions but is less disciplined
about canonical structure and confirmed-source use.

## Failures (Current)

- None.

## Next Steps (Current)

- No corrective change is indicated by the current assertions.

## Runtime Artifact Policy (Current)

- Runtime lanes and judge evidence remain in independent /tmp workspaces and are not committed.
- Only this durable comparison is updated.

## Historical Result (Superseded: pre-#234 contract)

- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


Both assertions were exercised on the reachable reference-backed design path.

## Assertion Results

- `assertion_1`: **PASS** — the candidate extracts restrained navigation, hero hierarchy, progressive workflow sections, product proof, CTA rhythm, purposeful motion, and mobile stacking from the stable reference record.
- `assertion_2`: **PASS** — it stops after the design artifact and does not enter frontend implementation.

## With-Skill Behavior

- Produces `docs/design/productivity-app-landing/ui-ux-spec.md` with reference analysis, user journey, inventory, ASCII layouts, CTA states, and responsive behavior.
- Explicitly forbids copying Linear branding, copy, screenshots, icons, product names, or feature scope.
- Uses PRD, handoff, and the stable reference note only; no BRD is requested or cited, so BRD removal causes no tested behavior difference.

## Fresh Without-Skill Baseline

- This baseline was newly generated in this run from only the same prompt, fixture handoff, PRD, and stable reference note; it did not apply the skill/README or reuse historical output.
- It satisfies the two broad assertions but gives less explicit repository artifact structure, adaptation boundary, and handoff discipline.
- It contains no BRD reference.

## Failures

- None.

## Next Steps

- No skill or fixture correction is required for this case.

## Runtime Artifact Policy

- Runtime candidates, fresh baseline, and judge evidence remain under the ignored runtime directory and are not committed.
- Only this durable `comparison.md` is updated.
