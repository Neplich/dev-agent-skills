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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e8c75de1d6f9996313bad1fce4ede6ed7cde9c08fd07355edd02169db57e8e68`
- Skill overlay SHA-256: `bb133a8c85c48881a2031584ba17c553a39faea708969d0cf9c8fc7668592bf7`
- Judge schema SHA-256: `463caa76fbf321564869d8651cfcd73afe8721c939c5039c5cfd81c4ab25d935`
- Eval definition SHA-256: `22532d649002dfa1851fec27c554d610e1ed3e70ab860965c5b4914f96d4ccce`
- Metadata SHA-256: `b228adbda9579c0023d949fdd52d3bd090b6ff85b7c6c2610e5202c6900dbe10`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_ux_first` | NOT_EXERCISED | Locked evidence does not prove the required route selection or ordering. |
| `routes_visual_followup` | NOT_EXERCISED | Locked evidence does not prove delegation to visual-design as a later or second route. |
| `uses_real_output_filenames` | PASS | Delivered files are exactly docs/design/billing-notifications/ui-ux-spec.md and docs/design/billing-notifications/visual-system.md. |
| `stops_before_code` | PASS | Both delivered files explicitly define the work as design-only and exclude React implementation and tests; the snapshot contains no code deliverables. |
| `hands_off_to_engineer` | PASS | Both delivered files explicitly hand remaining implementation to engineer-agent. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=2868393852ea5a4f1f9911fb881fde3111022e9d38faff25a09ff16e45f90348; snapshot_sha256=58bdc5d739570e882eec31f89ee4fbc136ce3b395ebf602bd44f8c4fe95b7d13
- Behavior: Produced the requested UX and visual design deliverables, stopped at design, and handed implementation to engineer-agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=982c1920fa1f7664c12c097b7c21d9323ff1b2e8ba4c46d5c48f200c187a2adb; snapshot_sha256=ab31f19621725ba90c2297b9a96398a29ab2b970ff8d37cdbe0c498a5dff6763
- Behavior: Implemented React/Vite files directly, providing a fresh code-first baseline.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Exercise or capture route-selection and route-order evidence for the two routing assertions.

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e8c75de1d6f9996313bad1fce4ede6ed7cde9c08fd07355edd02169db57e8e68`
- Skill overlay SHA-256: `bb133a8c85c48881a2031584ba17c553a39faea708969d0cf9c8fc7668592bf7`
- Judge schema SHA-256: `463caa76fbf321564869d8651cfcd73afe8721c939c5039c5cfd81c4ab25d935`
- Eval definition SHA-256: `22532d649002dfa1851fec27c554d610e1ed3e70ab860965c5b4914f96d4ccce`
- Metadata SHA-256: `b228adbda9579c0023d949fdd52d3bd090b6ff85b7c6c2610e5202c6900dbe10`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_ux_first` | NOT_EXERCISED | 原始证据未记录技能选择或执行顺序，无法证明该隐藏流程断言。 |
| `routes_visual_followup` | NOT_EXERCISED | 原始证据未记录视觉技能作为后续步骤的路由顺序，无法证明该隐藏流程断言。 |
| `uses_real_output_filenames` | PASS | 锁定交付快照包含 docs/design/billing-notifications/ui-ux-spec.md 和 visual-system.md。 |
| `stops_before_code` | PASS | 锁定交付仅包含两份设计文档；输出明确说明本轮未修改 React、测试或其他工程代码。 |
| `hands_off_to_engineer` | PASS | 输出明确说明后续由 engineer-agent 负责 TRD、实现和测试，视觉系统也将两份文档交给 engineer-agent。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=3db130600585f9f257731fed65bb01a7ebc5123f95195efa4ecdd44b8f8b94aa; snapshot_sha256=89cc44d1765d3d4f979ea3f78ec42b95bf962576fa76ea64cb95bf6abe381efd
- Behavior: 交付了正确命名的 UX/UI 与视觉系统设计文档，遵守设计阶段边界并完成 engineer-agent handoff。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=cd15afa7a79716a7f46921b59f4044ee00060473ca3208cd479bccb1a7de25c3; snapshot_sha256=d0c9e3764125f718c32cde8b1af215fb83c0ab1786d02e4eac08089fadbbd74d
- Behavior: 直接实现了 React 原型和工程文件，未提供设计交付文档或 engineer-agent handoff，作为鲜明的基线对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 如需完整验证路由断言，需要提供记录 ui-ux-design 先于 visual-design 的原始执行证据。

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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e8c75de1d6f9996313bad1fce4ede6ed7cde9c08fd07355edd02169db57e8e68`
- Skill overlay SHA-256: `bb133a8c85c48881a2031584ba17c553a39faea708969d0cf9c8fc7668592bf7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `22532d649002dfa1851fec27c554d610e1ed3e70ab860965c5b4914f96d4ccce`
- Metadata SHA-256: `b228adbda9579c0023d949fdd52d3bd090b6ff85b7c6c2610e5202c6900dbe10`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_ux_first` | PASS | With-skill output presents ui-ux-spec.md first; the locked file contains user journeys, information architecture, wireframes, interaction rules, and states. |
| `routes_visual_followup` | PASS | The visual-system.md delivery follows the UX spec and contains visual direction, component rules, colors, typography, and tone. |
| `uses_real_output_filenames` | PASS | Locked delivery_snapshot contains docs/design/billing-notifications/ui-ux-spec.md and docs/design/billing-notifications/visual-system.md. |
| `stops_before_code` | PASS | With-skill git status contains only the two design files; their locked contents explicitly exclude implementation, and no React, tests, scripts, or deployment configuration were delivered. |
| `hands_off_to_engineer` | PASS | With-skill output explicitly says the next step should be handed to engineer-agent; both locked design files also identify engineer-agent as the implementation owner. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=542a9fc08ac9fada7b6495427f41226c0deca91cae2c2989c1228c57d3830853; snapshot_sha256=85bb8647835b9d60c2f5fc48648629ec04b0ee9c1dad7be0ecd4b6ff33f33de3
- Behavior: Delivered the required UX and visual design artifacts, stopped at the design boundary, and handed implementation to engineer-agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=7ba65ca97735389c1359fdc91ccea71891116d8d18da367fa067a23976a838d3; snapshot_sha256=bf8b557ccbfd205b1dd422e6af858ae523b3ffbe08a67d4b9f5c048ff35d5e3e
- Behavior: Implemented a React settings page and delivered index.html, package.json, and src files, without the required design-first handoff.
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
- Skill: `designer-agent`
- Eval: `eval-001-route-design-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89` from `agents/designer/test/designer-agent/evals/workspace/eval-1-route-design-handoff`.
- Fixture SHA-256: `318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89`
- Prompt SHA-256: `6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e8c75de1d6f9996313bad1fce4ede6ed7cde9c08fd07355edd02169db57e8e68`
- Skill overlay SHA-256: `63b0ebceda55887d91c55004727587e1bea60e8f09954c557d9d72e92083bd8b`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `22532d649002dfa1851fec27c554d610e1ed3e70ab860965c5b4914f96d4ccce`
- Metadata SHA-256: `b228adbda9579c0023d949fdd52d3bd090b6ff85b7c6c2610e5202c6900dbe10`
- Executor SHA-256: `6c1c50885619c5add1ae9c7d9faf1fa39e905346d86059a01403ae742d286478`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_ux_first` | NOT_EXERCISED | Locked evidence shows UX deliverables, but cannot prove the required ui-ux-design selection or ordering. |
| `routes_visual_followup` | NOT_EXERCISED | Locked evidence shows a visual-system deliverable, but cannot prove visual-design routing as a later/second step. |
| `uses_real_output_filenames` | PASS | Delivery snapshot contains docs/design/billing-notifications/ui-ux-spec.md and docs/design/billing-notifications/visual-system.md. |
| `stops_before_code` | PASS | With-skill snapshot contains only the two design files; both explicitly state that implementation code is out of scope. |
| `hands_off_to_engineer` | PASS | Both design files explicitly hand subsequent TRD, implementation, React, and testing work to engineer-agent. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=8d39716bdfc40bffedf4df827712e5ad1b2f40ae70bec2bbf923e0c0f792052b; snapshot_sha256=bfb65b31eb3d5beb4cda8e029a17e4c333619d1783d75027175b2bb6a6c208d7
- Behavior: Delivered UX and visual design documents, stopped before implementation, and handed work to engineer-agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6928263198e744f0628528a64ad381eb51b57dfc5347279a1b5dc49c697dfc6c; fixture_sha256=318a6ed6ff151cee086f75e2b1924aa867c873c059722194e1d201fc514c9d89; output_sha256=f67d2350f7b73d4fee1f027fd4355baf9fd274d0571de6ef1f3964c8cf23e9f6; snapshot_sha256=47a5e620643957ab12428b61840d9df377419251d6757cac1ed485fbdf68b63e
- Behavior: Implemented a React prototype and supporting project files instead of stopping at design handoff.
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
