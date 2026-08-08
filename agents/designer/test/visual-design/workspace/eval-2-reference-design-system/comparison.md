# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `visual-design`
- Eval: `eval-002-playful`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `42400da86be636a5c48d6ced7acfe1114f7f3fc84e29109517e26b5a0856067c` from `agents/designer/test/visual-design/workspace/eval-2-reference-design-system`.
- Fixture SHA-256: `42400da86be636a5c48d6ced7acfe1114f7f3fc84e29109517e26b5a0856067c`
- Prompt SHA-256: `092b10f39d07502fd69cfd2b4992b956cec050d77722de8312a6a9dc94160cd6`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `da7e677bc92a70c0b2d244a02d70cdeaf6c4dea3529e1c7fd6f633e617949291`
- Skill overlay SHA-256: `f98263488d224b1b4c95d5f549311089ee5bc3eefe030032e40a15cde7e65f9d`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `1e9739265f0721cb69546820ef87da3e0b8045e92accd200c449d4a7c5bab7c5`
- Metadata SHA-256: `dea024aad09482b4b51327a960ae6e8c89fbc9764107a299297b588df52b9aa7`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `design_system_data` | FAIL | with_skill 文档包含 reference-driven design system、产品类型、推荐模式、风格、配色、字体、UX 质量规则和反模式，但未明确包含 Design System Data 查询结果或其来源证据。 |
| `assertion_2` | PASS | with_skill 输出为视觉系统文档内容，未包含 CSS、Tailwind、React、shadcn 实现代码、安装命令或工程任务拆解。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=092b10f39d07502fd69cfd2b4992b956cec050d77722de8312a6a9dc94160cd6; fixture_sha256=42400da86be636a5c48d6ced7acfe1114f7f3fc84e29109517e26b5a0856067c; output_sha256=1c3cc7305590855d976b8a51033841f0659536fffc42e7add3de228177ddb968; snapshot_sha256=a65193e8c49515d1694be1aa6bf472ed8657170667857a63e27b227bc4de70f3
- Behavior: 交付了结构完整的视觉系统文档，覆盖产品、布局、配色、字体、UX 规则和反模式，但缺少明确的 Design System Data 查询结果。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=092b10f39d07502fd69cfd2b4992b956cec050d77722de8312a6a9dc94160cd6; fixture_sha256=42400da86be636a5c48d6ced7acfe1114f7f3fc84e29109517e26b5a0856067c; output_sha256=44dc4e8a13872ba078c2cb4a2fdcc56cf50d64b61b8105212c8150dba57ce02e; snapshot_sha256=38c213b26884ec7f208a41501bd59c8162c3abcb1a79062188e444fffe4d7bef
- Behavior: 交付了详细视觉系统文档，但未明确呈现 reference-driven design system 或 Design System Data 查询结果。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- design_system_data 未满足其要求的 Design System Data 查询结果证据。
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

# Eval Result: eval-002-playful

## Evaluation Target

- Agent: `designer`
- Skill: `visual-design`
- Eval: `eval-002-playful`
- Test case: Reference-Driven Design System
- Workspace: `workspace/eval-2-reference-design-system`

## Test Set or Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`
- Fresh run time: `2026-08-07 00:04:31 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/designer/visual-design/eval-002-playful/`
- Fixture: confirmed PM handoff with `feature_path: enterprise-analytics-platform`

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL** (2/2 assertions exercised)
Overall result: PASS

## Assertion Results (Current)

- design_system_data: **PASS** — the new visual-system.md contains the reference-driven system, enterprise analytics category, Data-Dense Dashboard pattern, Data-Dense + Minimal Trust direction, colors, typography, UX rules, and anti-patterns derived from the local data helper.
- assertion_2: **PASS** — the document contains no implementation code, install command, or engineering task decomposition and ends at engineer-agent handoff.

## With-Skill Behavior (Current)

The candidate consumes the confirmed handoff, runs the local reference lookup,
reconciles it to the in-product analytics scope, and creates the canonical
visual-system artifact without leaking implementation snippets.

## Fresh Without-Skill Baseline (Current)

The baseline was completed before the with-skill root and its local reference
tree existed. It used the same prompt and clean handoff fixture in an independent
top-level workspace under isolated HOME/CODEX_HOME, and produced a generic
visual system without a real Design System Data lookup.

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


Both eval assertions were exercised on the reachable reference-driven generation path.

## Assertion Results

- `design_system_data`: **PASS** — a fresh helper lookup is reconciled into a Reference-Driven Design System with enterprise analytics category, Data-Dense Dashboard pattern, Data-Dense + Minimal Trust style, colors, typography, UX quality rules, and anti-patterns.
- `assertion_2`: **PASS** — output stops at design handoff without CSS/Tailwind/React/shadcn code, install commands, or engineering tasks.

## With-Skill Behavior

- Records the fresh helper's operations-oriented suggestions, then rejects its landing-page/dark-only mismatch in favor of the confirmed in-product data-dense dashboard scope.
- Targets `docs/design/enterprise-analytics-platform/visual-system.md`, removes raw helper implementation snippets, and hands off to Engineer.
- Uses PM handoff and local design evidence only; no BRD is required or cited, and removal causes no tested behavior difference.

## Fresh Without-Skill Baseline

- This baseline was newly generated in this run from only the same prompt and handoff; it did not apply the Designer README, skill, local references/helper, with-skill output, or old comparison.
- It offers a generic professional analytics direction and accessibility rules but cannot provide a real local database query or reference reconciliation.
- It contains no BRD reference.

## Failures

- None. The first helper attempt was blocked by the default `uv` cache path; rerunning unchanged with `UV_CACHE_DIR=/tmp/issue-198-uv-cache` succeeded.

## Next Steps

- No skill or fixture correction is required for this case.

## Runtime Artifact Policy

- Runtime candidates, fresh baseline, helper diagnostics, and judge evidence remain under the ignored runtime directory and are not committed.
- Only this durable `comparison.md` is updated.
