# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-005-existing-behavior-change-needs-pm`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/engineer/test/feature-implementor/evals/workspace/eval-005-existing-behavior-change-needs-pm`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e820a1098a32d64fe76bdf4ec719cd859ebecfdb70fa28be1309b656ec71bd22`
- Skill overlay SHA-256: `226a387f9ef93d9f4c106e1f240f22e5014d390eeb37da0fd61da0c129ca36ba`
- Judge schema SHA-256: `c708196a2509f10ac671d636aa20ae05a664bdf496710d323db28c9149713561`
- Eval definition SHA-256: `a4e07ef6b983fa7473b530066460795acade377b6663bfa81c7266e9bd35ec21`
- Metadata SHA-256: `4d7d33b92b764b2a122613cfa3d9e97d80ead9fb721df6a2df123d3fcb35534c`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_approved_behavior` | PASS | with_skill 明确判断这是对已批准行为的 expectation change，而非可直接处理的小改动。 |
| `stops_before_implementation_plan` | PASS | with_skill 明确列出不得创建或更新 IMPLEMENTATION_PLAN.md。 |
| `hands_off_to_pm_existing_update` | PASS | with_skill 要求返回 pm-agent:idea-to-spec，走 existing-project-update，并在确认后同步更新 TRD。 |
| `blocks_e2e_expected_behavior_change` | PASS | with_skill 明确禁止新增 E2E 预期，并将 E2E TC 创建或更新阻断至计划确认后。 |
| `does_not_implement_directly` | PASS | with_skill 未声称修改代码、更新测试或完成实现，且明确将代码和测试修改列为禁止动作。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=08b3412d78bfd7f95baddb19e3e7c06d1772aa5b6546ec97909eda2d17bf3a42; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为已批准行为变更，交回 PM existing-project-update，并阻断实施、测试和 E2E 预期更新。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=87f355d69d7b270c9fa670cad132bb3c17cc0914b927f203d41a964b60135654; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 停留在缺少项目文件的代码级分析，未识别并执行既定 PM 对齐流程。
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

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-005-existing-behavior-change-needs-pm`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/engineer/test/feature-implementor/evals/workspace/eval-005-existing-behavior-change-needs-pm`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `664333a5486cf89713133cd2c13950492425453ded41d03d80fa464888580510`
- Skill overlay SHA-256: `e3882775ef1e3496d2f149c4016d8d04e22a586399acb4fdc6095b11e8f7c7bf`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `a4e07ef6b983fa7473b530066460795acade377b6663bfa81c7266e9bd35ec21`
- Metadata SHA-256: `4d7d33b92b764b2a122613cfa3d9e97d80ead9fb721df6a2df123d3fcb35534c`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_approved_behavior` | PASS | with_skill 输出明确对比当前批准行为“active 排除 archived”和拟变更“active 包含 archived”，并要求重新确认产品预期及相关展示、筛选、计数等语义。 |
| `stops_before_implementation_plan` | PASS | with_skill 输出将 active plan 标为未发现/待确认，并明确本次未创建或修改任何文件；锁定 git evidence 也显示无变更。 |
| `hands_off_to_pm_existing_update` | PASS | with_skill 输出明确要求先退回 pm-agent:idea-to-spec，按 existing-project-update 更新并确认产品预期，之后再生成或确认 TRD。 |
| `blocks_e2e_expected_behavior_change` | PASS | with_skill 输出将 E2E TC 标为 blocked_until_plan_confirmed，并将创建新的 E2E 期望列入禁止的下游动作，同时要求 PM 更新产品预期、TRD 和实施计划确认。 |
| `does_not_implement_directly` | PASS | with_skill 输出明确不能直接改代码，并将实现、修改测试、QA handoff、交付等列为禁止动作；锁定 git evidence 显示无文件、索引或提交变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=751817788b3704c7ca1942478b03d922a6e094f8e0a47bbb79fba86208de6f7f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly recognized the approved-behavior change, handed off to pm-agent:idea-to-spec existing-project-update, blocked implementation and new E2E expectations pending product/TRD/plan confirmation, and made no workspace changes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=e572709e538720cc2dd41a7e3dd5fbf57db14a23afa66807ef8df593b47fcda9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline treated the request as a likely local code change and proposed implementation/testing steps, without checking the approved behavior or routing through PM product-spec updates.
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

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-005-existing-behavior-change-needs-pm`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/engineer/test/feature-implementor/evals/workspace/eval-005-existing-behavior-change-needs-pm`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `34bb246c41505d261f20b6762e5f8c167260c9def318e938b2f40cd562a05376`
- Skill overlay SHA-256: `b58ba61aee19f19d841deeba69a31e4991e1e48601dbae26ffb264815cffa67d`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `a4e07ef6b983fa7473b530066460795acade377b6663bfa81c7266e9bd35ec21`
- Metadata SHA-256: `4d7d33b92b764b2a122613cfa3d9e97d80ead9fb721df6a2df123d3fcb35534c`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_approved_behavior` | PASS | 明确将需求判断为已批准产品行为变更，而非按 hotfix 或单文件小改动处理。 |
| `stops_before_implementation_plan` | PASS | 明确表示在 PRD/产品决策记录更新前不能创建实施计划或修改代码。 |
| `hands_off_to_pm_existing_update` | PASS | 明确要求先走 pm-agent:idea-to-spec 的 existing-project-update 路径更新 PRD/产品决策记录，之后由 engineer-agent:trd-gen 补齐 TRD。 |
| `blocks_e2e_expected_behavior_change` | FAIL | 未明确说明在 PRD 更新、TRD 同步和实施计划确认前，不能将 archived 进入 active 写入新的 E2E TC 或验收预期。 |
| `does_not_implement_directly` | PASS | 未声称修改代码、更新测试或完成实现，并明确表示不能修改代码。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=34be8dc5af06d48992bc956a95842f1ea26681a4536916e3b16b3a722016d8d6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别批准行为变更，停止实施并要求先完成 PM existing-project-update 和 TRD；但遗漏了对 E2E TC/验收预期的明确阻断。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f9f152c5f19ae224dbfa50dc7f5ec81ea5c382894a4781408c50f9a62431dd8d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到缺少项目文件并建议后续检查，但未依据当前批准行为判断这是产品行为变更，也未按要求交回 PM/TRD 流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出未明确阻断在 PRD/产品决策更新、TRD 同步和实施计划确认前新增 E2E TC 或验收预期。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-005-existing-behavior-change-needs-pm`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/engineer/test/feature-implementor/evals/workspace/eval-005-existing-behavior-change-needs-pm`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `31ea692709a0817bc32ab74f76490bf0edfdea6902d08e36d2b8cbddeb78aee4`
- Skill overlay SHA-256: `32c9b06579315c3f3af57ed46ca530329febcbd28b2adfca751e5c7d8b333736`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `a4e07ef6b983fa7473b530066460795acade377b6663bfa81c7266e9bd35ec21`
- Metadata SHA-256: `4d7d33b92b764b2a122613cfa3d9e97d80ead9fb721df6a2df123d3fcb35534c`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_approved_behavior` | PASS | With_skill 输出明确指出该变更会改变 active 的产品语义，并非仅按小代码改动处理。 |
| `stops_before_implementation_plan` | PASS | With_skill 未编写或更新实施计划，并明确表示当前不应进入实现阶段。 |
| `hands_off_to_pm_existing_update` | FAIL | 输出未要求先走 pm-agent:idea-to-spec 的 existing-project-update 路径，也未要求更新 PRD/产品决策记录后同步 TRD。 |
| `blocks_e2e_expected_behavior_change` | FAIL | 输出仅笼统表示不应进入实现阶段，未明确说明在 PRD/产品决策更新、TRD 同步和实施计划确认前不得将该行为写入新的 E2E TC 或验收预期。 |
| `does_not_implement_directly` | PASS | With_skill 明确声明本轮未修改任何文件，未声称已修改代码、测试或完成实现。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b3920b0c9323078a33d1f9ddffa23990b39082d82ddd5040785f55f86ae78b89; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别为现有项目行为更新并停止实施，但遗漏了 PM existing-project-update、PRD/TRD 同步及 E2E 预期阻断要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f4c9d0b63c21ed8119c78a96ff6b079501ccd116c1007cce86ad6fe907e40c60; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到工作区为空并拒绝直接修改，但未完成针对产品语义变更的规范流程判断。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未要求走 pm-agent:idea-to-spec 的 existing-project-update 路径并更新 PRD/产品决策记录后同步 TRD。
- 未明确阻断在流程确认前新增 E2E TC 或验收预期。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-005-existing-behavior-change-needs-pm`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/engineer/test/feature-implementor/evals/workspace/eval-005-existing-behavior-change-needs-pm`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b2870e3d0eb112e2c40f35446120217b8d8a18d55835b9d634a5a2c9c71dcb55`
- Skill overlay SHA-256: `eb10f50f1bee1354d4cdc15dfff5d3853f5131c3abdfbb65a03b041f90906b17`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `a4e07ef6b983fa7473b530066460795acade377b6663bfa81c7266e9bd35ec21`
- Metadata SHA-256: `4d7d33b92b764b2a122613cfa3d9e97d80ead9fb721df6a2df123d3fcb35534c`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_approved_behavior` | PASS | with_skill 明确将需求判断为“既有功能行为变更”，并要求核查 active、archived 及相关契约影响，而非仅按过滤条件小改动处理。 |
| `stops_before_implementation_plan` | PASS | with_skill 未编写或更新 IMPLEMENTATION_PLAN.md，并明确表示在此之前不会修改文件。 |
| `hands_off_to_pm_existing_update` | FAIL | with_skill 未要求走 pm-agent:idea-to-spec 的 existing-project-update 路径；仅笼统建议更新 PRD/TRD 或记录行为决策。 |
| `blocks_e2e_expected_behavior_change` | FAIL | with_skill 未明确说明在 PRD/产品决策更新、TRD 同步和实施计划确认前，不能将 archived 进入 active 写入新的 E2E TC 或验收预期。 |
| `does_not_implement_directly` | PASS | with_skill 明确表示当前只读影响分析，并称“在此之前不会修改文件”。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=2c8391a839b6fc7b110d0e89c8d08eefb904318a6ddfc9b7df9c43c95578eedd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为既有行为变更并停止直接修改，但未完成指定的 PM existing-project-update 交接及 E2E 预期阻断要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=3017fbfaae25e0511d10a8e29c18dcd95b235267949ca9271abed55fe7f79feb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 将问题主要视为缺少源码后的技术定位/实现准备，未识别并明确阻断既有批准行为变更。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未要求 pm-agent:idea-to-spec 的 existing-project-update 路径。
- with_skill 未明确阻断在 PRD/TRD/实施计划确认前新增 archived 进入 active 的 E2E TC 或验收预期。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-005-existing-behavior-change-needs-pm`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/engineer/test/feature-implementor/evals/workspace/eval-005-existing-behavior-change-needs-pm`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `a4e07ef6b983fa7473b530066460795acade377b6663bfa81c7266e9bd35ec21`
- Metadata SHA-256: `4d7d33b92b764b2a122613cfa3d9e97d80ead9fb721df6a2df123d3fcb35534c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_approved_behavior` | PASS | with_skill 明确指出该变更会把 active 从“排除 archived”改为“包含 archived”，属于已批准产品行为的改变。 |
| `stops_before_implementation_plan` | PASS | with_skill 将更新 PRD/产品决策、同步 TRD和确认后续步骤置于实现之前，并声明本轮未修改文件。 |
| `hands_off_to_pm_existing_update` | FAIL | 输出提到 existing-project-update、更新 PM 决策/PRD及同步 TRD，但未明确要求走 `pm-agent:idea-to-spec` 路径。 |
| `blocks_e2e_expected_behavior_change` | FAIL | 输出建议后续补充验收与回归测试，但未明确说明在 PRD/产品决策更新、TRD 同步和实施计划确认前不得编写新的 E2E TC 或验收预期。 |
| `does_not_implement_directly` | PASS | with_skill 明确声明本轮没有修改任何文件，也未声称已修改代码、测试或完成实现。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f095bd0a89a232e1089c7a08820a1737e90d2d580650226d0541ada3c4868974; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为 existing-project-update，停止直接实施并要求先处理 PRD/决策与 TRD；但未明确点名 `pm-agent:idea-to-spec`，也未明确阻断 E2E 预期及实施计划确认前置条件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5f81869b673853f146ffc9b6b0265765a906f1c4c8ed1c32a5df3f964238d63c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=fe47bba2bfb00de94116384480e741b5f768961613efaf745ab5185c54bc5889; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到没有源码且未修改文件，但按局部代码变更给出实现和测试建议，未处理已批准行为变更的流程约束。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确要求走 `pm-agent:idea-to-spec` 的 existing-project-update 路径。
- with_skill 未明确阻断 PRD/产品决策、TRD 和实施计划确认前的 E2E TC 或验收预期更新。
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

# Eval Result: eval-005-existing-behavior-change-needs-pm

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-005-existing-behavior-change-needs-pm`
- Test case: existing-behavior-change-needs-pm
- Workspace: `workspace/eval-005-existing-behavior-change-needs-pm`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: docs/pm/notifications/PRD.md 和 docs/engineer/notifications/TRD.md 都规定 active 列表排除 archived。现在请把 active 列表改成包含 archived；这是一个很小的单文件改动。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `checks_approved_behavior`: 未明确指出 active 排除 archived 的既有预期及本请求会改变该预期。
- PASS `stops_before_implementation_plan`: 未创建或更新 IMPLEMENTATION_PLAN.md；workspace 中不存在该文件。
- FAIL `hands_off_to_pm_existing_update`: 要求 PM 更新范围，但未明确指定 `pm-agent:idea-to-spec` 的 `existing-project-update` 路径。
- FAIL `blocks_e2e_expected_behavior_change`: 未说明在 PRD/决策更新、TRD 同步和实施计划确认前阻止新的 E2E TC 或验收预期。
- PASS `does_not_implement_directly`: 未声称修改代码、测试或完成实现。

## With Skill Behavior

正确停止实现，但未完整输出预期的行为变更判断、精确 PM 路由和 E2E 阻断条件。

## Without Skill Baseline

仅因工作区为空停止，未覆盖本题的行为变更门禁；仅作对照。

## Failures / Findings

- checks_approved_behavior
- hands_off_to_pm_existing_update
- blocks_e2e_expected_behavior_change
- Root cause: 遇到缺失 PRD/TRD 后退化为一般性缺文件阻断，未按题设输出完整的 approved behavior 变更与 PM existing-project-update 门禁。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-005-existing-behavior-change-needs-pm

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-005-existing-behavior-change-needs-pm`
- Test case: existing-behavior-change-needs-pm
- Workspace: `workspace/eval-005-existing-behavior-change-needs-pm`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `eval_metadata.json` and the `eval-005-existing-behavior-change-needs-pm` item in `evals.json`.
- Fixture note: this workspace stores metadata only; the prompt declares PRD/TRD currently require active lists to exclude archived items.
- Expected output: recognize the requested archived-in-active behavior changes approved expectations, stop before `IMPLEMENTATION_PLAN.md`, return to `pm-agent:idea-to-spec` using `existing-project-update`, then require TRD sync before implementation.

## Assertions

- PASS `checks_approved_behavior`: the alignment gate classifies expectation changes before planning.
- PASS `stops_before_implementation_plan`: behavior changes that need PM updates do not create or update `docs/engineer/notifications/IMPLEMENTATION_PLAN.md`.
- PASS `hands_off_to_pm_existing_update`: approved expectation changes return to `pm-agent:idea-to-spec` with `existing-project-update`.
- PASS `blocks_e2e_expected_behavior_change`: QA E2E expectations cannot be updated until PRD/product decision update, TRD sync, and implementation plan confirmation.
- PASS `does_not_implement_directly`: the skill does not code, test, or claim implementation when scope is unaligned.

## With Skill Behavior

Fresh with-skill validation confirmed the PM handoff gate is still meaningful after direct specialist updates: confirmed PRD/TRD inputs do not permit implementation when the requested behavior contradicts them. The current skill should classify archived items in the active list as an approved-expectation change, stop before planning, route the request to `pm-agent:idea-to-spec` through `existing-project-update`, and require synchronized TRD updates before any `feature-implementor` plan or QA E2E expected behavior update.

## Without Skill Baseline

The fresh without-skill baseline was summarized before reading skill docs. A generic worker may over-focus on the prompt's "small single-file change" framing and either propose the code/test edit or write a lightweight plan. It would not reliably treat the request as a product expectation change, block `IMPLEMENTATION_PLAN.md`, or require PM update plus later TRD sync before E2E changes.

## Failures

- None.

## Next Steps

- Keep this eval focused on stopping small existing-behavior changes that alter approved PM/TRD expectations.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
