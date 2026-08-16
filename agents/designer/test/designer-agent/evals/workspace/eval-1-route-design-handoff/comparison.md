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
- Identity schema: `2`
- target_skill_sha256: `1d67d4772843dc0275749d693d7415791b7459f5d948588a69fb240bcfd7f02b`
- eval_definition_sha256: `81da08302867bb0360b62db9057e07b009cd93243321e4fb904ab779192971e2`
- metadata_sha256: `b228adbda9579c0023d949fdd52d3bd090b6ff85b7c6c2610e5202c6900dbe10`
- fixture_sha256: `318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `463caa76fbf321564869d8651cfcd73afe8721c939c5039c5cfd81c4ab25d935`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `902f97074f6d958600dd8079608539a38bff227cb03726b9ab277705b1b8ded7`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_ux_first` | PASS | 锁定 trace 明确记录路由为 `ui-ux-design → visual-design`，且交付的 UI/UX 规范包含流程、信息架构、线框和交互状态。 |
| `routes_visual_followup` | PASS | 锁定 trace 明确将 `visual-design` 作为 `ui-ux-design` 后续步骤；`visual-system.md` 直接交付视觉系统内容。 |
| `uses_real_output_filenames` | PASS | delivery_snapshot 直接包含 `docs/design/billing-notifications/ui-ux-spec.md` 与 `docs/design/billing-notifications/visual-system.md`。 |
| `stops_before_code` | PASS | 锁定 git evidence 仅显示两个设计文档新增，未修改 React、测试、脚本或部署配置；候选输出也明确说明设计阶段未修改 React 或测试。 |
| `hands_off_to_engineer` | PASS | 候选输出明确说明下一步交给 `engineer-agent`，负责后续 TRD、实现和测试。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=4ea9cda6e65004528c54889cc0c7058f484fbb22ee308bff96d98037a11ca74b; snapshot_sha256=2f78acb346714aa76ba8ebf727ef82099a10f9f2faa598f368f0ae6d72505ee0
- Behavior: 完成 UX→视觉设计路由，交付两个指定设计文档，停在设计边界并移交 engineer-agent。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=e890661bb0c7224d380a6e8acc360d35ab925138135e9dc64b4288672d05d7b5; snapshot_sha256=e86274135b5aa5e53c079d654a1bd0556b887130a91d0fff912f7d4d3e2b1c3f
- Behavior: 直接实现 React 设置页并新增应用代码，未按设计路由交付指定设计文档或执行设计阶段 handoff。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
