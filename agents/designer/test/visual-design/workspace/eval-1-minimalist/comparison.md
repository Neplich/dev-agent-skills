# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `visual-design`
- Eval: `eval-001-minimalist`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `89d144dafb490a68dbf1ec05d2336c43c874c81e51496b945ac9140ca757080a` from `agents/designer/test/visual-design/workspace/eval-1-minimalist`.
- Fixture SHA-256: `89d144dafb490a68dbf1ec05d2336c43c874c81e51496b945ac9140ca757080a`
- Prompt SHA-256: `c3c36cd66b9231c6a2156abc32bf00fb490f5264858737980fadf81d3240530f`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `da7e677bc92a70c0b2d244a02d70cdeaf6c4dea3529e1c7fd6f633e617949291`
- Skill overlay SHA-256: `f98263488d224b1b4c95d5f549311089ee5bc3eefe030032e40a15cde7e65f9d`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `2ec4f897729f0820b0a7830a10f3f0348db98fac1c3a94d29404427ccb404465`
- Metadata SHA-256: `a8c3886c0203449f24edc77c5c3e77a82c91f7ce462169d6c62325194a234222`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 的 delivery_snapshot 写入 docs/design/minimalist-productivity-app/visual-system.md；文档包含 Color System、Typography、Spacing 和 Component Styles，且 minimalist-productivity-app 与已确认 feature_path 一致。 |
| `assertion_2` | PASS | with_skill 文档是视觉规范，明确未生成代码或工程配置；原始内容未包含 CSS、组件实现、设计 token 落地代码、工程任务拆解或测试命令。 |
| `assertion_3` | PASS | 文档 Design Handoff 明确写明交由 engineer-agent 负责实现。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c3c36cd66b9231c6a2156abc32bf00fb490f5264858737980fadf81d3240530f; fixture_sha256=89d144dafb490a68dbf1ec05d2336c43c874c81e51496b945ac9140ca757080a; output_sha256=ec7286f014164f68e78e7ee636e72d433d71dc5b79e9fe35b8aacd6addc2029b; snapshot_sha256=b244e9636b2a151e5b92a78e65f031a6b9b1e23409a7658089faca261fc5c68d
- Behavior: 产出了指定路径的视觉系统文档，覆盖颜色、字体、间距和组件规则；保持设计交接范围，并明确交由 engineer-agent 实现。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c3c36cd66b9231c6a2156abc32bf00fb490f5264858737980fadf81d3240530f; fixture_sha256=89d144dafb490a68dbf1ec05d2336c43c874c81e51496b945ac9140ca757080a; output_sha256=b68048a3179c40389a76c94281dcdd73c0c17bc065b8c543f7147f2298270f8e; snapshot_sha256=64f9736113f3b772cf917c8702d47e7920f5c7fe03005540f6c204ac55668fea
- Behavior: 产出了完整视觉系统文档，路径和内容范围基本符合要求，但未明确提示由 engineer-agent 接手实现。
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

# Eval Result: eval-001-minimalist

## Evaluation Target

- Agent: `designer`
- Skill: `visual-design`
- Eval: `eval-001-minimalist`
- Test case: Minimalist Design System
- Workspace: `workspace/eval-1-minimalist`

## Test Set or Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`
- Fresh run time: `2026-08-07 00:04:31 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/designer/visual-design/eval-001-minimalist/`
- Fixture: confirmed PM handoff with `feature_path: minimalist-productivity-app`

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL** (3/3 assertions exercised)
Overall result: FAIL

## Assertion Results (Current)

- assertion_1: **FAIL** — no docs/design/minimalist-productivity-app/visual-system.md is generated despite the confirmed PM_HANDOFF fixture.
- assertion_2: **PASS** — no token code, CSS/component implementation, engineering task decomposition, or test command is emitted.
- assertion_3: **FAIL** — the candidate redirects to PM instead of naming engineer-agent as the implementation owner after design.

## With-Skill Behavior (Current)

The candidate applies the PM gate without inspecting the fixture's existing
confirmed handoff, so it incorrectly blocks before producing the required
visual system or Engineer handoff.

## Fresh Without-Skill Baseline (Current)

The baseline ran before the with-skill root existed, from the identical prompt
and clean PM_HANDOFF fixture in an independent top-level workspace under
isolated HOME/CODEX_HOME. It generated a detailed visual-system.md, but its
behavior remains comparison input only.

## Failures (Current)

- Confirmed fixture handoff was not consumed.
- Required visual-system artifact and engineer-agent handoff are absent.

## Next Steps (Current)

- Fix handoff discovery before applying the PM gate, then rerun.

## Runtime Artifact Policy (Current)

- Runtime lanes and judge evidence remain in independent /tmp workspaces and are not committed.
- Only this durable comparison is updated.

## Historical Result (Superseded: pre-#234 contract)

- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


All three assertions were exercised on the reachable visual-system generation path.

## Assertion Results

- `assertion_1`: **PASS** — the candidate targets `docs/design/minimalist-productivity-app/visual-system.md` and covers color, typography, spacing, and dimensioned components.
- `assertion_2`: **PASS** — it includes no token code, CSS/component implementation, engineering task decomposition, or test command.
- `assertion_3`: **PASS** — implementation is explicitly handed to `engineer-agent`.

## With-Skill Behavior

- Runs the local Design System Data helper, keeps useful flat/low-noise cues, and rejects its unconfirmed App Store landing framing for this productivity product.
- Produces a restrained, accessible, density-derived visual system and strips raw helper CSS/imports from the design artifact.
- Uses confirmed audience and goals from the PM handoff; it neither requires nor cites BRD, so removal causes no tested behavior difference.

## Fresh Without-Skill Baseline

- This baseline was newly generated in this run from only the same prompt and PM handoff; it did not apply the Designer README, skill, local references, with-skill output, or old comparison.
- It gives plausible minimalist visual notes and remains code-free, but does not perform the local reference lookup or consistently produce the canonical artifact and role handoff.
- It contains no BRD reference.

## Failures

- None. The first helper attempt was blocked by the default `uv` cache path; rerunning unchanged with `UV_CACHE_DIR=/tmp/issue-198-uv-cache` succeeded and produced fresh lookup evidence.

## Next Steps

- No skill or fixture correction is required for this case.

## Runtime Artifact Policy

- Runtime candidates, fresh baseline, helper diagnostics, and judge evidence remain under the ignored runtime directory and are not committed.
- Only this durable `comparison.md` is updated.
