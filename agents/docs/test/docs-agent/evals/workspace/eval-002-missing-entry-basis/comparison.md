# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-002-missing-entry-basis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/docs/test/docs-agent/evals/workspace/eval-002-missing-entry-basis`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b04f0f833fdfe60f19dba4258110d7f6b0a3d6a6f2afb7034b0d3d883c30f83b`
- Skill overlay SHA-256: `56a47f4293d7435d43e789574be1e08a3a03c3c8021043b25cccb472ae22b6c6`
- Judge schema SHA-256: `da898e3ecfd0169570b22be7c73cd730ef2fd22e3bf1c5b559383dc76454ff0d`
- Eval definition SHA-256: `bf1b5d8af479146ff04e48ba6dcc39176cc5d38f4f20e513ea504da5a2a472c2`
- Metadata SHA-256: `9e2c43ddcdebfd4398d2a8f32a222c29dd71f706e06b85ffb24ea4623239c500`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `guides_to_pm_agent` | PASS | with_skill 明确说明无 PM handoff、等价确认文档链，并要求先由 pm-agent 补齐和确认 handoff。 |
| `does_not_execute_bootstrap` | PASS | with_skill 声明停留在路由边界、不创建或修改文档站；git_status、workspace_manifest、delivery_snapshot 均为空，且无变更证据。 |
| `names_missing_credentials` | FAIL | with_skill 指出宿主仓库路径缺失，但未说明“显式建站请求加确认仓库路径”可构成 docs-site-bootstrap specialist entry basis。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=56c80ca31c94e3485904e29fa5cb186a358b2c204e72e7c23f3f4e313133540c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确执行 PM 路由并保持下游建站边界，但未完整说明可解锁的 specialist entry basis。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a2280a0950e4b111161e1a023cdeb5012e0a17d22c681968022175369704a9e3; snapshot_sha256=6330393a243b8b937565be05cdd389635373021b9861f37889a2a2a81f72da12
- Behavior: 直接声称已搭建正式文档站，并交付 index.html、styles.css、script.js；git_status 显示未跟踪文件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完整说明可由显式建站请求与确认仓库路径解锁 docs-site-bootstrap specialist entry basis。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-002-missing-entry-basis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/docs/test/docs-agent/evals/workspace/eval-002-missing-entry-basis`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b04f0f833fdfe60f19dba4258110d7f6b0a3d6a6f2afb7034b0d3d883c30f83b`
- Skill overlay SHA-256: `56a47f4293d7435d43e789574be1e08a3a03c3c8021043b25cccb472ae22b6c6`
- Judge schema SHA-256: `da898e3ecfd0169570b22be7c73cd730ef2fd22e3bf1c5b559383dc76454ff0d`
- Eval definition SHA-256: `bf1b5d8af479146ff04e48ba6dcc39176cc5d38f4f20e513ea504da5a2a472c2`
- Metadata SHA-256: `9e2c43ddcdebfd4398d2a8f32a222c29dd71f706e06b85ffb24ea4623239c500`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `guides_to_pm_agent` | PASS | With-skill output explicitly states that no PM handoff, confirmation chain, or specialist entry basis exists and asks the user to have pm-agent complete and confirm the Docs handoff. |
| `does_not_execute_bootstrap` | PASS | With-skill output sets the execution boundary at routing, reports no delivered files or manifest, and raw git evidence shows no changes. |
| `names_missing_credentials` | PASS | With-skill output identifies the unconfirmed host repository path as missing, while routing the explicit formal-docs request toward docs-site-bootstrap after the required repository and handoff information is confirmed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=5c9e6eb9c0422444143e9c40b1844afa1139bf48a8e0f046c8ee177492cdc60d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly stopped at the routing boundary, identified missing PM and repository context, and directed the user to pm-agent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=191d6951ebd31de5bce5b6425efac1f9ab9e14324b4ab6a26d1bebf61002f06e; snapshot_sha256=a984dd1aface0c913380e76321d0282752d94eece43ffd356fe9d4cc8137d8e2
- Behavior: Fresh baseline executed the ambiguous request, created a static documentation site with README, HTML, CSS, and JavaScript, and provided local preview instructions.
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

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-002-missing-entry-basis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/docs/test/docs-agent/evals/workspace/eval-002-missing-entry-basis`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b04f0f833fdfe60f19dba4258110d7f6b0a3d6a6f2afb7034b0d3d883c30f83b`
- Skill overlay SHA-256: `56a47f4293d7435d43e789574be1e08a3a03c3c8021043b25cccb472ae22b6c6`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bf1b5d8af479146ff04e48ba6dcc39176cc5d38f4f20e513ea504da5a2a472c2`
- Metadata SHA-256: `9e2c43ddcdebfd4398d2a8f32a222c29dd71f706e06b85ffb24ea4623239c500`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `guides_to_pm_agent` | PASS | with_skill 明确指出缺少 PM handoff，并要求通过 pm-agent 补充范围、来源文档和授权状态。 |
| `does_not_execute_bootstrap` | PASS | with_skill 仅完成路由，明确在信息齐备前不会创建或修改文档站文件；git_status、manifest 和 delivery_snapshot 均为空。 |
| `names_missing_credentials` | FAIL | with_skill 指出宿主仓库路径未确认，但未说明“显式建站请求 + 已确认仓库路径”可构成 docs-site-bootstrap 的 specialist entry basis。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=885034b2590436683cd9bd15fa39db274ff875ad40f752362bf922dc55fe4c83; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确停留在路由阶段，指出 PM handoff、宿主仓库路径和范围缺失，并引导通过 pm-agent 补充信息。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=52fb6e934d7460fe6f3d440ce9b589a69c466159776d09367b0ae50680fdc8c2; snapshot_sha256=3622d10bb8fc645d499df13e60bdf6df0863e2e65fdcebdc352bb7e21c4773ed
- Behavior: 将模糊请求直接执行为文档站建设，并交付 index.html、script.js 和 styles.css。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确说明显式建站请求与确认仓库路径可构成 specialist entry basis。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-002-missing-entry-basis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/docs/test/docs-agent/evals/workspace/eval-002-missing-entry-basis`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e64e4dc492a2ff92be09822529f9abb1fbd17f4d0148b3045e0162382c5d46d3`
- Skill overlay SHA-256: `749fef364aaabb23f2e52b059edb29be9012a21c64c9a31f0ad0b387e6a4d9e4`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bf1b5d8af479146ff04e48ba6dcc39176cc5d38f4f20e513ea504da5a2a472c2`
- Metadata SHA-256: `9e2c43ddcdebfd4398d2a8f32a222c29dd71f706e06b85ffb24ea4623239c500`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `guides_to_pm_agent` | FAIL | with_skill 明确指出缺少有效的 PM Docs 交接包及相关前置上下文，但未引导用户经 `pm-agent` 完成分类和上下文准备。 |
| `does_not_execute_bootstrap` | PASS | with_skill 明确表示暂不能执行；git_status、git_diff、workspace_manifest 和 delivery_snapshot 均为空，未见建站产物或 bootstrap 执行证据。 |
| `names_missing_credentials` | PASS | with_skill 指出缺少主机项目/仓库绝对路径，并说明补齐后将路由至 `docs-site-bootstrap`，语义上对应确认仓库路径后具备 specialist entry basis。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=764b449f318a6e9a058620118d6e13984965cb4270634831d4736187bdef701e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为 docs-site-bootstrap 请求，但因缺少 PM 交接包、仓库路径及上下文而暂停执行并请求补充信息。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=dd9c7c68f963c1d62b89f672d65d45530f0057787e971c37934d1da770bd95de; snapshot_sha256=4c5d649d4eb887f526ef236f97459fa0b897c0f8a5e9a0a40d4f3d0a4074265b
- Behavior: 直接创建并交付静态文档站文件，未进行 PM handoff 或入口条件检查。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未提及或引导用户通过 `pm-agent` 完成分类和前置上下文。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-002-missing-entry-basis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/docs/test/docs-agent/evals/workspace/eval-002-missing-entry-basis`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e64e4dc492a2ff92be09822529f9abb1fbd17f4d0148b3045e0162382c5d46d3`
- Skill overlay SHA-256: `749fef364aaabb23f2e52b059edb29be9012a21c64c9a31f0ad0b387e6a4d9e4`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bf1b5d8af479146ff04e48ba6dcc39176cc5d38f4f20e513ea504da5a2a472c2`
- Metadata SHA-256: `9e2c43ddcdebfd4398d2a8f32a222c29dd71f706e06b85ffb24ea4623239c500`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `guides_to_pm_agent` | FAIL | with_skill 明确指出缺少宿主项目或 PM 确认交接包，并要求补充上下文，但没有温和引导用户经 `pm-agent` 完成分类和前置上下文。 |
| `does_not_execute_bootstrap` | PASS | with_skill 没有创建文件、生成 manifest、加载或复述 bootstrap 模板，也没有把请求当作已确认的建站 opt-in；Git 原始证据显示工作区保持干净。 |
| `names_missing_credentials` | FAIL | with_skill 指出了缺少宿主项目目录/仓库，但没有说明“显式建站请求 + 已确认仓库路径”可构成 `docs-site-bootstrap` 的 specialist entry basis。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b0c902389a193e8a361ed83a67a6ec3186e90a0a3daec8a75c6d4e9a10a2bff3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 拒绝在缺少宿主项目或 PM 确认交接包时执行建站，并要求补充项目、技术栈、部署目标及文档范围。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=198964db65f7ad9cdf55bab97f4e9dd666b1f943e769f66edff1d60c936fac09; snapshot_sha256=08c2e672490df3182386ba06e36beeac41b34d68eedb186173d00bcdb6247340
- Behavior: 直接声称正式文档站已搭建，并在 raw evidence 中显示创建了三个未跟踪文件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未引导用户经 `pm-agent` 完成分类和前置上下文。
- 未说明确认仓库路径与显式建站请求如何构成 specialist entry basis。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-002-missing-entry-basis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/docs/test/docs-agent/evals/workspace/eval-002-missing-entry-basis`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9b5483c75770358083301bcb4f3e774af3a6e851f51536b52de7b7f0a1bd16fd`
- Skill overlay SHA-256: `320e6c30e29bfe7c756c6fe127e3b5eaa8fa87b721478809a95d374e8e5e3334`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bf1b5d8af479146ff04e48ba6dcc39176cc5d38f4f20e513ea504da5a2a472c2`
- Metadata SHA-256: `9e2c43ddcdebfd4398d2a8f32a222c29dd71f706e06b85ffb24ea4623239c500`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `guides_to_pm_agent` | FAIL | with_skill 未明确说明缺少 PM handoff packet、等效确认文档链或完整 specialist entry basis，也未引导用户经 pm-agent 完成分类和前置上下文。 |
| `does_not_execute_bootstrap` | PASS | with_skill 输出未执行建站；raw evidence 显示无文件、无 manifest、无模板内容复述，且 git 状态无变化。 |
| `names_missing_credentials` | FAIL | with_skill 提到缺少宿主项目，但未明确指出已确认的宿主仓库路径缺失，也未说明显式建站请求加确认仓库路径可构成 docs-site-bootstrap entry basis。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=e31d101f7cf6c1160d1cca32ad1389ae169681f836f7381b736127726c22d849; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 未执行建站，指出缺少宿主项目且下游 docs-site-bootstrap 未安装，但未完成 PM-agent 引导或完整 entry-basis 条件说明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=82ed36e72fbc687b49bce1cdd5e28bc5dc9a1b4a91f7bcca5913d449a3c397c7; snapshot_sha256=64c73aa79c9b9c5075783d995b6b7965a616cc380551fad38ce7e861286f7937
- Behavior: 直接声称已搭建文档站，并生成 index.html、script.js、styles.css；未进行前置路由或条件确认。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- guides_to_pm_agent 未满足。
- names_missing_credentials 未满足。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-002-missing-entry-basis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/docs/test/docs-agent/evals/workspace/eval-002-missing-entry-basis`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9fbb92b16f91777ce613be24ad3cd630730cfccd4cce1cf1d33c3b6c917671d6`
- Skill overlay SHA-256: `d217ecf7b54c3a1d88949c667de969b1871337427d1c578eeca7de0421ad0971`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bf1b5d8af479146ff04e48ba6dcc39176cc5d38f4f20e513ea504da5a2a472c2`
- Metadata SHA-256: `9e2c43ddcdebfd4398d2a8f32a222c29dd71f706e06b85ffb24ea4623239c500`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `guides_to_pm_agent` | FAIL | with_skill 指出缺少交接包/文档范围，但未明确列出缺少 PM handoff、等效确认文档链或完整 specialist entry basis，也未引导经 pm-agent 完成分类。 |
| `does_not_execute_bootstrap` | PASS | with_skill 未创建文件、docs/site、manifest，也未加载或复述 bootstrap 模板，并要求补充前置信息后再初始化。 |
| `names_missing_credentials` | FAIL | with_skill 要求提供产品代码仓库/目录路径，但未说明需确认的宿主仓库路径，也未说明显式建站请求加确认路径可构成 docs-site-bootstrap specialist entry basis。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=ee61724bee4397b3ebb47e31159d64f584f923c0ad0b368bf6bb17274c78b253; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 未执行建站，要求补充仓库路径或 PM 交接信息，但未完整遵循 PM handoff 引导和 entry-basis 说明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6cf5103ac6662b081338cd0ba18b3696b5704a9a176ed2544db6f0ed4a2a1ee6; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=cc7f1d4aae973d12c1f991346bea2c57c81cd234924fc23b7194e88abcea8ffb; snapshot_sha256=9ef4281bc2f46189e3d95e78a5b8b10be5f3d01b10f67fb4cd134e6fa11bc84e
- Behavior: 直接生成静态文档站文件，未进行前置分类或凭据核验。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 guides_to_pm_agent。
- with_skill 未满足 names_missing_credentials。
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

# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-002-missing-entry-basis`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- 评估基线：`a273a00` 加本轮 cross-doc sync R2 working tree
- Harness：完整 router harness、fresh zero-skill baseline 与独立 judge

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| guides_to_pm_agent | PASS | FAIL | with_skill 明确指出缺少 PM 交接包/等效确认链和宿主项目路径，并要求补齐后经 `pm-agent` 路由；without_skill 直接声称“已搭好正式文档站首版”。 |
| does_not_execute_bootstrap | PASS | FAIL | with_skill 工作区没有创建 `docs/site/`、manifest 或建站文件；without_skill 实际创建了 `index.html`、`styles.css`、`script.js`，并声称已搭建首版。 |
| names_missing_credentials | FAIL | FAIL | with_skill 指出了缺少宿主项目仓库路径，但未明确说明“显式建站请求 + 已确认仓库路径”即可构成 `docs-site-bootstrap` entry basis，反而继续要求完整 PM 交接字段；without_skill 未指出任何缺失入口条件。 |

未满足断言（with/without 任一 FAIL）：`guides_to_pm_agent`、`does_not_execute_bootstrap`、`names_missing_credentials`



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `guides_to_pm_agent`：PASS。明确没有 PM packet、等效链或完整 specialist entry basis。
- `does_not_execute_bootstrap`：PASS。未创建 `docs/site/`、模板或 manifest；fixture 仅新增 candidate output。
- `names_missing_credentials`：PASS。指出“显式建站请求 + 已确认宿主仓库路径”可解锁 bootstrap entry basis。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：同 prompt/fixture 的本轮全新 baseline，不含 skill/README。
- baseline 只索要一般建站信息，未识别 PM gate 或最小 specialist entry basis。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure；未发生任何下游写入。

## Next Steps

- 保留当前温和入口安全网。

## Runtime Artifact Policy

- 运行期产物仅保留在 `tmp/eval-runs/116/`，不提交到 git。
