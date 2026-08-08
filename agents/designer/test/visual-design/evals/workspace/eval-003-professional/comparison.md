# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `visual-design`
- Eval: `eval-003-professional`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `567d74ee90d360991ab613f98d8049d53202d95a2bc7caeb2b7d46b23846a5f0` from `agents/designer/test/visual-design/evals/workspace/eval-003-professional`.
- Fixture SHA-256: `567d74ee90d360991ab613f98d8049d53202d95a2bc7caeb2b7d46b23846a5f0`
- Prompt SHA-256: `fe1184ee76579ac0041ea69b2abac6b0897add864da628d5ff0192673c2c0220`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `da7e677bc92a70c0b2d244a02d70cdeaf6c4dea3529e1c7fd6f633e617949291`
- Skill overlay SHA-256: `f98263488d224b1b4c95d5f549311089ee5bc3eefe030032e40a15cde7e65f9d`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `730e4eb8de3e03b346a013a3d5577a175072336c34214d71e41ce4685c2c2ee1`
- Metadata SHA-256: `0f7ee2304f9494f523bf0e9ffeed979b5af06eb7930b9cda8b5ec89883762703`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With-skill delivery specifies WCAG AA thresholds: normal text 4.5:1 and large text/key UI boundaries 3:1. It also defines stable information hierarchy and scanning priorities for enterprise analytics users. |
| `assertion_2` | PASS | With-skill delivery explicitly states it excludes component implementation, style files, and design-token configuration. Git evidence shows only an untracked visual-system.md document and no engineering changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fe1184ee76579ac0041ea69b2abac6b0897add864da628d5ff0192673c2c0220; fixture_sha256=567d74ee90d360991ab613f98d8049d53202d95a2bc7caeb2b7d46b23846a5f0; output_sha256=2688c0d95e01fcdaf3f9b5b970dd908bc93e92d662a394cea4a413c707a3194d; snapshot_sha256=160013af585378a41e799710440199b39c9b9e50e461b0f21e433417ec26d245
- Behavior: Produced a detailed enterprise visual-system specification with explicit WCAG thresholds and no implementation artifacts.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=fe1184ee76579ac0041ea69b2abac6b0897add864da628d5ff0192673c2c0220; fixture_sha256=567d74ee90d360991ab613f98d8049d53202d95a2bc7caeb2b7d46b23846a5f0; output_sha256=9e18b7c2e67212e96565e18d99e5a6935f06e83978f1ba1d7a3a095a43a5888f; snapshot_sha256=815c1ff2508e509ec140fd49715e04325bea7abbf43c3608b7514fb194ab9336
- Behavior: Produced a visual-system document covering accessibility, hierarchy, and scope boundaries.
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

# Eval Result: eval-003-professional

## Evaluation Target

- Agent: `designer`
- Skill: `visual-design`
- Eval: `eval-003-professional`
- Test case: Professional Design System
- Workspace: `workspace/eval-003-professional`

## Test Set or Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`
- Fresh run time: `2026-08-07 00:04:31 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/designer/visual-design/eval-003-professional/`
- Fixture: confirmed PM handoff and PRD for `enterprise-analytics`

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL** (2/2 assertions exercised)
Overall result: PASS

## Assertion Results (Current)

- assertion_1: **PASS** — the fresh visual-system.md defines WCAG 4.5:1 text and 3:1 UI/large-text thresholds with clear enterprise data hierarchy.
- assertion_2: **PASS** — the new artifact is design documentation only and contains no component code, style-file change, or engineering command.

## With-Skill Behavior (Current)

The candidate consumes the confirmed PM scope, reconciles local design evidence
to a trusted data-dense product system, writes the canonical feature-path
artifact, and stops at design handoff.

## Fresh Without-Skill Baseline (Current)

The baseline ran first from the same prompt, PM handoff, and PRD in an
independent top-level workspace under isolated HOME/CODEX_HOME. It meets the
two broad assertions but lacks the current skill's local reference reasoning
and explicit design-handoff depth.

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


Both assertions were exercised on the reachable visual-system generation path.

## Assertion Results

- `assertion_1`: **PASS** — the candidate states WCAG 4.5:1 normal-text and 3:1 large-text/UI-boundary thresholds and defines a clear enterprise data hierarchy.
- `assertion_2`: **PASS** — it contains no component code, style-file change, or engineering command.

## With-Skill Behavior

- Reconciles the helper's Enterprise Gateway/Trust & Authority result with the PRD's in-product, data-dense dashboard scope.
- Targets `docs/design/enterprise-analytics/visual-system.md` with accessible colors, authoritative typography, compact spacing, dimensioned tables/charts/filters/alerts, explicit states, and Engineer handoff.
- Reads audience, product goals, and visual tone from PRD and never requests or cites BRD; removal causes no tested behavior difference.

## Fresh Without-Skill Baseline

- This baseline was newly generated in this run from only the same prompt, PM handoff, and PRD; it did not apply the Designer README, skill, local helper/references, with-skill output, or old comparison.
- It independently meets the broad accessibility and design-only assertions but lacks lookup reconciliation, canonical artifact depth, and exact role handoff.
- It contains no BRD reference.

## Failures

- None. The first helper attempt was blocked by the default `uv` cache path; rerunning unchanged with `UV_CACHE_DIR=/tmp/issue-198-uv-cache` succeeded.

## Next Steps

- No skill or fixture correction is required for this case.

## Runtime Artifact Policy

- Runtime candidates, fresh baseline, helper diagnostics, and judge evidence remain under the ignored runtime directory and are not committed.
- Only this durable `comparison.md` is updated.
