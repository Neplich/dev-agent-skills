# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b` from `agents/engineer/test/feature-implementor/evals/workspace/eval-017-abandoned-draft-can-be-superseded`.
- Fixture SHA-256: `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b`
- Prompt SHA-256: `3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e820a1098a32d64fe76bdf4ec719cd859ebecfdb70fa28be1309b656ec71bd22`
- Skill overlay SHA-256: `226a387f9ef93d9f4c106e1f240f22e5014d390eeb37da0fd61da0c129ca36ba`
- Judge schema SHA-256: `a264d3282fcfebf29821ed24d8e702134594b3cc4be72cd72f03b0e03e92c160`
- Eval definition SHA-256: `d59f332d9689221834dd583c1a569fa62e1de4ce2c4c1d7f5aa087aed088bd53`
- Metadata SHA-256: `21a9c9ae11f8c9b8058a429c319a4f2a640a6b07fdf2d71e259bbc158caa4e24`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_unfinished_active_plan` | PASS | with_skill 明确给出 active_plan_path、原状态 Draft；归档文件内容保留 implementation_scope: refund-reason-codes。 |
| `detects_explicit_abandonment` | PASS | 归档文件的 superseded_reason 明确记录维护者放弃未完成退款原因码轮次并转向退款审核流程。 |
| `archives_as_superseded` | FAIL | 归档文件为 Superseded 且有非空 superseded_reason，并保留 implementation_scope；但缺少 archive_approved_by，且使用 archive_date/archived_from 而非要求的 archived_at/source_plan。 |
| `links_replacement_plan` | NOT_EXERCISED | with_skill 要求 TRD 更新后生成新的 IMPLEMENTATION_PLAN.md，并标记等待确认；当前快照未交付替代计划，因此该后续步骤尚未可执行。 |
| `waits_before_coding` | PASS | 快照仅修改计划文档、未修改代码；输出将实现等下游动作标为 blocked，并明确 confirmation_required。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=6b0818d0110323c05dfafdf7acc47a5488e5b4f8a2656a37d47037f33dbc610e; snapshot_sha256=5c69ebe72c6122710d815aec1c919391055e24943a81a577a3fc7c3e8191dd3c
- Behavior: 识别并归档了已放弃的 Draft 计划为 Superseded，保留了原计划主体 metadata，并在编码前等待确认；但归档 metadata 不完整，替代计划尚未交付。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=fcdd9eeaaae5cd709b1c1cc841eb38d8355b25a9b78d0a84d3437a833a484f80; snapshot_sha256=9376e94e955c4dcaedaae10925e482fc12581b8fb001b5b00e0c62070b739a50
- Behavior: 直接覆盖原 Draft 计划，将实施范围改为 refund-review；未按要求归档原计划、建立替代计划回链或等待确认。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 归档文件缺少 assertion 要求的 archive_approved_by，且未提供 archived_at/source_plan 字段。
- Next: 补齐归档文件的 archived_at、archive_approved_by、source_plan 字段。
- Next: 在 TRD 完整且获得确认后生成新的 IMPLEMENTATION_PLAN.md，并通过 previous_plan_archive 回链归档文件。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b` from `agents/engineer/test/feature-implementor/evals/workspace/eval-017-abandoned-draft-can-be-superseded`.
- Fixture SHA-256: `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b`
- Prompt SHA-256: `3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e820a1098a32d64fe76bdf4ec719cd859ebecfdb70fa28be1309b656ec71bd22`
- Skill overlay SHA-256: `226a387f9ef93d9f4c106e1f240f22e5014d390eeb37da0fd61da0c129ca36ba`
- Judge schema SHA-256: `a264d3282fcfebf29821ed24d8e702134594b3cc4be72cd72f03b0e03e92c160`
- Eval definition SHA-256: `d59f332d9689221834dd583c1a569fa62e1de4ce2c4c1d7f5aa087aed088bd53`
- Metadata SHA-256: `21a9c9ae11f8c9b8058a429c319a4f2a640a6b07fdf2d71e259bbc158caa4e24`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_unfinished_active_plan` | PASS | The delivered active plan is at the required path with status Draft, and the archived snapshot preserves implementation_scope: refund-reason-codes. |
| `detects_explicit_abandonment` | PASS | The plan and archive explicitly state that the maintainer abandoned the unfinished refund reason-code round. |
| `archives_as_superseded` | FAIL | The archive is Superseded with a non-empty superseded_reason and preserved scope/metadata, but it omits archived_at, archive_approved_by, and source_plan. |
| `links_replacement_plan` | PASS | The new active plan links through previous_plan_archive to the Superseded archive under the same payment-refund feature path. |
| `waits_before_coding` | PASS | Only plan documents were modified; the output states coding is blocked until explicit confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=53811b8a57a18d325cd415cb42237e112e51e175e74045ce29286e5b81a27008; snapshot_sha256=8c50219367a177fa56b27ecc2d5e823e4998593b33e536833109e6829cc84ecd
- Behavior: Created a replacement Draft plan, a Superseded archive, and a confirmation gate before coding, but omitted required archive fields.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=e3021ad4883949df890fea69fd1794494f84a0f2af5cf0928d4cf8cbfd84d479; snapshot_sha256=cd6a1d7988036b9433e10ee881de100cab6cba1a18ccfeb29ccf3ca64f33ba97
- Behavior: Changed the existing plan to Abandoned and switched scope without creating the required Superseded archive or replacement-plan link.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- archives_as_superseded: required archived_at, archive_approved_by, and source_plan fields are missing.
- Next: Add non-empty archived_at, archive_approved_by, and source_plan to the Superseded archive.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b` from `agents/engineer/test/feature-implementor/evals/workspace/eval-017-abandoned-draft-can-be-superseded`.
- Fixture SHA-256: `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b`
- Prompt SHA-256: `3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `664333a5486cf89713133cd2c13950492425453ded41d03d80fa464888580510`
- Skill overlay SHA-256: `e3882775ef1e3496d2f149c4016d8d04e22a586399acb4fdc6095b11e8f7c7bf`
- Judge schema SHA-256: `a264d3282fcfebf29821ed24d8e702134594b3cc4be72cd72f03b0e03e92c160`
- Eval definition SHA-256: `d59f332d9689221834dd583c1a569fa62e1de4ce2c4c1d7f5aa087aed088bd53`
- Metadata SHA-256: `21a9c9ae11f8c9b8058a429c319a4f2a640a6b07fdf2d71e259bbc158caa4e24`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_unfinished_active_plan` | FAIL | with_skill 输出列出了当前路径和 implementation_scope，但未识别原计划的 status: Draft。 |
| `detects_explicit_abandonment` | PASS | 输出明确说明旧轮次已废弃、维护者要求归档，并停止继续该计划。 |
| `archives_as_superseded` | PASS | 归档快照直接显示 status: Superseded、非空 superseded_reason，以及保留的 implementation_scope、archived_at、archive_approved_by、source_plan 和原 metadata。 |
| `links_replacement_plan` | NOT_EXERCISED | 输出要求新计划回链 previous_plan_archive，但由于 TRD 缺口未创建替换计划，无法验证实际回链；按交互式工作流规则暂不行使。 |
| `waits_before_coding` | PASS | 输出明确停止编码，并要求新 TRD 和精确实施计划确认后再开始编码；git 证据显示未修改代码。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=dd9f388e6596129990b36da97f497147ed2c09e6aa9af42e42858ca35dd7ff5b; snapshot_sha256=60e7d90fb7cf63cf114ab5e74753d74232568bb61eff8609a2733385201a2b38
- Behavior: 正确识别废弃路径并完成 Superseded 归档，保留编码前确认门槛；但遗漏了原计划 Draft 状态，且替换计划尚未创建。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=c00480eb196dff3d6de7c1616173e31b8f4524f122b3e62052fe296626a9ba28; snapshot_sha256=71f7ef39b6a778ef6f159cf1fb3c12ef2c5bc1602b81e6198715d772da2b5efc
- Behavior: 将原 Draft 计划错误更新为 In Progress 并改写为新范围，未执行 Superseded 归档流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未识别未完成活跃计划的 status: Draft。
- Next: 在输出中明确指出原 IMPLEMENTATION_PLAN.md 的 status: Draft。
- Next: 待 TRD 补全并确认新计划后，创建 active IMPLEMENTATION_PLAN.md 并验证 previous_plan_archive 回链。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b` from `agents/engineer/test/feature-implementor/evals/workspace/eval-017-abandoned-draft-can-be-superseded`.
- Fixture SHA-256: `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b`
- Prompt SHA-256: `3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `664333a5486cf89713133cd2c13950492425453ded41d03d80fa464888580510`
- Skill overlay SHA-256: `e3882775ef1e3496d2f149c4016d8d04e22a586399acb4fdc6095b11e8f7c7bf`
- Judge schema SHA-256: `a264d3282fcfebf29821ed24d8e702134594b3cc4be72cd72f03b0e03e92c160`
- Eval definition SHA-256: `d59f332d9689221834dd583c1a569fa62e1de4ce2c4c1d7f5aa087aed088bd53`
- Metadata SHA-256: `21a9c9ae11f8c9b8058a429c319a4f2a640a6b07fdf2d71e259bbc158caa4e24`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_unfinished_active_plan` | NOT_EXERCISED | 锁定证据包含原计划的 Draft、路径和 implementation_scope，但无法证明具体读取过程或顺序。 |
| `detects_explicit_abandonment` | PASS | 输出明确称维护者已放弃退款原因码轮次，并转向新的退款审核流程。 |
| `archives_as_superseded` | FAIL | 归档文件为 Superseded 且有非空 superseded_reason，并保留 implementation_scope；但缺少 archived_at、archive_approved_by、source_plan，且使用了不同字段名 archived_date、archived_from。 |
| `links_replacement_plan` | FAIL | 锁定交付中没有新的 active IMPLEMENTATION_PLAN.md，也没有 previous_plan_archive 回链；输出仅表示未来重新生成计划。 |
| `waits_before_coding` | PASS | 输出明确阻塞实现、测试、交付和 PR，并要求计划生成后等待确认；锁定 git 证据未显示代码修改。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=836ec1341b366526b5ca2b96eef87bd4d9ee8b9f2fe120e014dd91f5e4d9cbc1; snapshot_sha256=4284109d5509319516ecebc16903398888ad3f99fe9b341a927a547b7e7a0c18
- Behavior: 识别了明确废弃信号，创建了 Superseded 归档并阻止编码，但归档字段不完整且未交付回链新计划。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=31dbd1fab7884c4bb4c6c86bd0e6f29da65c9ec2eba4ddf96694789600004c33; snapshot_sha256=0a6a7f4fdaf9b87c4eb77381588486ccde0538f031f9c2dd36b44470fffea9a3
- Behavior: 仅将原 Draft 计划改为 Deprecated，未创建符合要求的 Superseded 归档或替代计划。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 归档 metadata 不满足要求，缺少 archived_at、archive_approved_by 和 source_plan。
- 未创建通过 previous_plan_archive 指向 Superseded 归档的新实施计划。
- Next: 补齐归档字段 archived_at、archive_approved_by、source_plan。
- Next: 创建新的 implementation plan，并以 previous_plan_archive 指向同 feature_path 的 Superseded 归档。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b` from `agents/engineer/test/feature-implementor/evals/workspace/eval-017-abandoned-draft-can-be-superseded`.
- Fixture SHA-256: `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b`
- Prompt SHA-256: `3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `664333a5486cf89713133cd2c13950492425453ded41d03d80fa464888580510`
- Skill overlay SHA-256: `e3882775ef1e3496d2f149c4016d8d04e22a586399acb4fdc6095b11e8f7c7bf`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d59f332d9689221834dd583c1a569fa62e1de4ce2c4c1d7f5aa087aed088bd53`
- Metadata SHA-256: `21a9c9ae11f8c9b8058a429c319a4f2a640a6b07fdf2d71e259bbc158caa4e24`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_unfinished_active_plan` | PASS | with_skill 输出明确给出 active_plan_path，并识别旧计划为 Draft、implementation_scope 为 refund-reason-codes。 |
| `detects_explicit_abandonment` | PASS | 归档文件中的 superseded_reason 明确记录维护者已放弃未完成的退款原因码轮次，输出也采取了归档而非继续更新 Draft 的路径。 |
| `archives_as_superseded` | FAIL | 归档文件确实为 Superseded 且 superseded_reason 非空，并保留了 implementation_scope 与原 metadata；但缺少要求的 archived_at、archive_approved_by、source_plan 字段。 |
| `links_replacement_plan` | NOT_EXERCISED | with_skill 正确指出 TRD 内容不足并暂不创建新计划；因此在当前运行中尚未到达需要验证 previous_plan_archive 回链的步骤。 |
| `waits_before_coding` | PASS | 输出明确未修改代码，并要求 TRD 补齐、生成新计划后再次确认，且禁止实现代码。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=3ed43120f33f13e6736ecb8f78e3c905d2bdeb1f7e970f91c55488669a010e12; snapshot_sha256=beede0a3073439130aeab77d2d28fafac2ce1f4e58435245b1936af4dc4f2f28
- Behavior: 识别并归档了被废弃的 Draft 计划，未修改代码并等待后续确认；但归档 metadata 不完整，且新计划回链步骤未执行。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=67e5dcc12335e2b0682b7319e716862aa76def15da57a3699932472133f32dcf; snapshot_sha256=75306b963a4467809edb9513032dd36cccc762f0c817082df023c335fe44e929
- Behavior: 修改了原计划为 Deprecated，但未归档为 Superseded，也未创建新计划或等待确认。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- archives_as_superseded 失败：归档缺少 archived_at、archive_approved_by、source_plan。
- Next: 补充归档文件中的 archived_at、archive_approved_by 和 source_plan。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b` from `agents/engineer/test/feature-implementor/evals/workspace/eval-017-abandoned-draft-can-be-superseded`.
- Fixture SHA-256: `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b`
- Prompt SHA-256: `3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `34bb246c41505d261f20b6762e5f8c167260c9def318e938b2f40cd562a05376`
- Skill overlay SHA-256: `b58ba61aee19f19d841deeba69a31e4991e1e48601dbae26ffb264815cffa67d`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d59f332d9689221834dd583c1a569fa62e1de4ce2c4c1d7f5aa087aed088bd53`
- Metadata SHA-256: `21a9c9ae11f8c9b8058a429c319a4f2a640a6b07fdf2d71e259bbc158caa4e24`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_unfinished_active_plan` | NOT_EXERCISED | The locked artifact preserves the original plan metadata, including Draft context, path, and refund-reason-codes scope, but the raw evidence cannot prove the candidate's read operation or read order. |
| `detects_explicit_abandonment` | PASS | The output explicitly states that the maintainer abandoned the refund reason-code round and that work is moving to the refund review workflow. |
| `archives_as_superseded` | PASS | The archived file is marked Superseded and includes a non-empty superseded_reason, implementation_scope, archived_at, archive_approved_by, source_plan, and original metadata. |
| `links_replacement_plan` | NOT_EXERCISED | The candidate correctly stopped after archiving because the available TRD lacks required implementation detail; no replacement plan was created, so this later linkage step could not yet occur. |
| `waits_before_coding` | PASS | The output states that code was not modified and requests TRD completion before continuing; git evidence shows no code changes or commits. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=2409dd745eb3f3babcb5a2b92ffcb32ddccb80ab8388f9b907cb909e6aadf7ab; snapshot_sha256=ed48437d065b4d6e5762aeacee22476b4bd1eec89c4212fd0f20a6bad582781c
- Behavior: Archived the abandoned plan correctly as Superseded, preserved required metadata, made no code changes, and paused pending missing TRD details.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=5ef220034df4715539458c6107ac2eada0e6f139cebd18ebea61fba7643d85e1; snapshot_sha256=ae526a402bc888e5c2f863b3d8211487212c4e6f8a397a4cc7f05ff23c398ec2
- Behavior: Changed the active plan to Deprecated and created a replacement plan, but did not archive it as Superseded with the required archive metadata or establish the required archive linkage.
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
- Eval: `eval-017-abandoned-draft-can-be-superseded`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b` from `agents/engineer/test/feature-implementor/evals/workspace/eval-017-abandoned-draft-can-be-superseded`.
- Fixture SHA-256: `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b`
- Prompt SHA-256: `3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `31ea692709a0817bc32ab74f76490bf0edfdea6902d08e36d2b8cbddeb78aee4`
- Skill overlay SHA-256: `32c9b06579315c3f3af57ed46ca530329febcbd28b2adfca751e5c7d8b333736`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d59f332d9689221834dd583c1a569fa62e1de4ce2c4c1d7f5aa087aed088bd53`
- Metadata SHA-256: `21a9c9ae11f8c9b8058a429c319a4f2a640a6b07fdf2d71e259bbc158caa4e24`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_unfinished_active_plan` | PASS | Raw evidence shows the original plan at the required path was deleted and its Draft status, feature path, and implementation_scope are preserved in the diff/archive metadata. |
| `detects_explicit_abandonment` | PASS | The output identifies the maintainer's abandonment through the recorded superseded reason. |
| `archives_as_superseded` | PASS | The archive snapshot has status Superseded, a non-empty superseded_reason, archived_at, archive_approved_by, source_plan, implementation_scope, and preserved original metadata. |
| `links_replacement_plan` | NOT_EXERCISED | The candidate correctly completed archival but reported that no new active plan was created because required TRD details were missing. |
| `waits_before_coding` | NOT_EXERCISED | No code was modified, but the replacement plan was not yet written, so the later confirmation-before-coding step was not reached. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=d2cc1bdc9f0715a27c0d9f5d7db556edaa88b2d6b4c53470ef92e4f93a2c92a3; snapshot_sha256=7294352b52d88cff4789d32dae8ebd74ca21a50792b64a470f297182baba50a2
- Behavior: Archived the unfinished plan as Superseded with required metadata, made no code changes, and paused before creating the replacement plan due to missing TRD details.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=76d493db17979402db1b65663dbf56d08f758635d44357e8d85a822fa4868261; snapshot_sha256=549bc8acb06f68ccd075fcd229a6860a90684a39f6df0bd0ac865ad2213934b7
- Behavior: Marked the old plan Deprecated and created an In Progress replacement, but did not use the required Superseded archive workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Complete the TRD details, create the replacement implementation plan with a previous_plan_archive link, then obtain user confirmation before coding.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b` from `agents/engineer/test/feature-implementor/evals/workspace/eval-017-abandoned-draft-can-be-superseded`.
- Fixture SHA-256: `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b`
- Prompt SHA-256: `3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b2870e3d0eb112e2c40f35446120217b8d8a18d55835b9d634a5a2c9c71dcb55`
- Skill overlay SHA-256: `eb10f50f1bee1354d4cdc15dfff5d3853f5131c3abdfbb65a03b041f90906b17`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d59f332d9689221834dd583c1a569fa62e1de4ce2c4c1d7f5aa087aed088bd53`
- Metadata SHA-256: `21a9c9ae11f8c9b8058a429c319a4f2a640a6b07fdf2d71e259bbc158caa4e24`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_unfinished_active_plan` | FAIL | with_skill 输出未明确识别 Draft 状态、当前路径 docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md 和精确 implementation_scope: refund-reason-codes。 |
| `detects_explicit_abandonment` | PASS | with_skill 输出明确表示已废弃旧退款原因码实施计划，并说明维护者明确放弃该轮。 |
| `archives_as_superseded` | FAIL | 虽归档为 Superseded 且有非空 superseded_reason，但归档原始证据缺少 archived_at、archive_approved_by、source_plan，且未完整保留要求的元数据。 |
| `links_replacement_plan` | FAIL | with_skill 删除了活动 IMPLEMENTATION_PLAN.md，且明确表示暂不能生成新实施计划；没有通过 previous_plan_archive 回链同 feature_path 的 Superseded 归档。 |
| `waits_before_coding` | PASS | git_diff 仅涉及计划文件归档/删除，未修改业务代码；输出明确表示暂不能开始编码。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=29e0d1e1eb8ee217da8ec0a1dcd0eeb8ffd81d7929d5209a32b38a085a74584f; snapshot_sha256=18bff28ccab4596c44ebca0f5829e83fd0ddbfbc64d79f6191fec5e3fcbaaaa7
- Behavior: 识别并归档了废弃计划为 Superseded，未修改业务代码，但遗漏必需归档字段和替代计划回链。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=32b6a4b4d786236f5e3756471f07fff5cea648747c40be94122a677eab3be70b; snapshot_sha256=6995bf9c25a12866dbab1af2906dacd7066fe6950387f174e7942935038d3a94
- Behavior: 将原计划直接改为 Abandoned，未创建符合要求的归档或替代计划。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足读取并明确识别原 Draft 计划字段的断言。
- 归档缺少 archived_at、archive_approved_by、source_plan。
- 未创建带 previous_plan_archive 的新活动实施计划。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b` from `agents/engineer/test/feature-implementor/evals/workspace/eval-017-abandoned-draft-can-be-superseded`.
- Fixture SHA-256: `1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b`
- Prompt SHA-256: `3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d59f332d9689221834dd583c1a569fa62e1de4ce2c4c1d7f5aa087aed088bd53`
- Metadata SHA-256: `21a9c9ae11f8c9b8058a429c319a4f2a640a6b07fdf2d71e259bbc158caa4e24`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_unfinished_active_plan` | PASS | With-skill raw diff shows the original plan was Draft with implementation_scope `refund-reason-codes`, and the output identifies the current and archived plan paths. |
| `detects_explicit_abandonment` | PASS | The output and archived plan identify explicit maintainer abandonment/supersession of the unfinished refund reason-code round. |
| `archives_as_superseded` | FAIL | The archive has status `Superseded`, a non-empty `superseded_reason`, `implementation_scope`, and original metadata, but lacks required `archived_at`, `archive_approved_by`, and `source_plan` fields. |
| `links_replacement_plan` | PASS | The replacement plan contains `previous_plan_archive` pointing to the archive, and both plans use feature_path `payment-refund`; the archive is Superseded. |
| `waits_before_coding` | FAIL | No code was modified and implementation is blocked pending TRD completion, but the output does not state that user confirmation is still required before coding. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=731014c63ba572543fe9cc77e423296677c5b171bc58c71be5c2486d7c421b1d; snapshot_sha256=04af1cb114eeb6b1d70ff70399d7bd15510a5c366ab97b81c93e8754d8b2cb44
- Behavior: Created a Superseded archive and linked replacement Draft plan, but omitted required archive metadata and did not explicitly wait for user confirmation before coding.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3023c99f87e425cf1e709e4a173f62dfa04ac1cedece451c8d3671923093f7ca; fixture_sha256=1f669b72548a150607fd615bf909a1c365d5c49a031676d6fa71132017e8642b; output_sha256=30677428babdc786852d112acf37bb5500311d1bfa25c6769f020aec31a01927; snapshot_sha256=25d73571d5f509474c20bb300783df84a2868dab0fcde25480a77493dd0f2b89
- Behavior: Updated the existing plan in place, marked it Superseded, changed scope, and claimed continuation, without creating a compliant archive or replacement-plan link.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The archive omits `archived_at`, `archive_approved_by`, and `source_plan`.
- The output does not explicitly require user confirmation before coding.
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

# Eval Result: eval-017-abandoned-draft-can-be-superseded

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`
- Test case: abandoned-draft-can-be-superseded
- Workspace: `workspace/eval-017-abandoned-draft-can-be-superseded`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: docs/pm/payment-refund/PRD.md 和 docs/engineer/payment-refund/TRD.md 已确认。现有退款原因码实施计划不再继续，维护者明确要求废弃这一轮并为新的退款审核流程继续工作。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `reads_unfinished_active_plan`: with_skill transcript item_2 实际读取 active IMPLEMENTATION_PLAN.md，并输出 status: Draft、路径及 implementation_scope: refund-reason-codes。
- PASS `detects_explicit_abandonment`: transcript item_4 明确记录维护者已放弃该轮，并选择 Superseded 分支，而非继续更新 Draft。
- PASS `archives_as_superseded`: 实际归档文件 status 为 Superseded，包含非空 superseded_reason、implementation_scope、archived_at、archive_approved_by、source_plan，并保留原计划 metadata。
- PASS `links_replacement_plan`: 新 active IMPLEMENTATION_PLAN.md 包含 previous_plan_archive，指向同 feature_path 的 Superseded 归档文件。
- PASS `waits_before_coding`: transcript 无代码修改；workspace 仅新增/更新计划文档，最终输出请求确认后再开始实现。

## With Skill Behavior

with_skill 完成了读取、Superseded 归档、回链新计划，并等待确认；实际 workspace 哈希与 output.sha256 一致。

## Without Skill Baseline

without_skill 作为对照将旧计划标记为 Abandoned 并新增独立计划，未满足 Superseded 归档及 previous_plan_archive 回链要求。

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-017-abandoned-draft-can-be-superseded

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`
- Test case: abandoned-draft-can-be-superseded
- Workspace: `workspace/eval-017-abandoned-draft-can-be-superseded`
- Latest result: PASS - fresh Codex validation completed on 2026-07-27 with
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

  5/5 assertions passing for both with-skill and zero-exposure without-skill
  runs.

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill validation: `README.md`, `eval_metadata.json`,
  `docs/pm/payment-refund/PRD.md`, `docs/engineer/payment-refund/TRD.md`, and
  `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`.
- Fixture summary: the active plan is `status: Draft`, and the maintainer
  explicitly abandons the `refund-reason-codes` round before requesting a
  replacement refund-review plan.

## Assertions

- PASS `reads_unfinished_active_plan`: the response reads the fixed active path
  and identifies `status: Draft` and
  `implementation_scope: refund-reason-codes`.
- PASS `detects_explicit_abandonment`: it treats the maintainer's instruction
  as the explicit-abandonment exception instead of applying the default Draft
  continuation path.
- PASS `archives_as_superseded`: it selects a same-feature-path Superseded
  archive, requires a non-empty `superseded_reason`, and preserves
  `implementation_scope`, `archived_at`, `archive_approved_by`, `source_plan`,
  and the original plan metadata.
- PASS `links_replacement_plan`: it requires the replacement active plan at
  `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md` to set
  `previous_plan_archive` to the Superseded archive.
- PASS `waits_before_coding`: it makes no code change and keeps implementation
  blocked until the replacement plan is confirmed.

## With Skill Behavior

The fresh with-skill validator read the Engineer README, the
`feature-implementor` entry, and its planner, reviewer, coding, and output
instructions before inspecting the complete fixture. It confirmed that PRD and
TRD metadata align, read the active Draft plan, and chose the explicit
abandonment path permitted by the archive gate. The expected handling archives
the existing plan as
`implementation-plans/archive/IMPLEMENTATION_PLAN-refund-reason-codes.md` with
`status: Superseded`, a non-empty reason, required archive metadata, and
preserved original metadata. It then creates the replacement plan at the fixed
active path with `previous_plan_archive` pointing to that archive and waits for
confirmation before coding.

The fixture identifies the approver only as the maintainer, without a
traceable name or account. The validator therefore required a real, non-empty
`archive_approved_by` value before persistence instead of inventing one; this
does not weaken the archive-field assertion.

## Without Skill Baseline

A separate fresh Codex subagent was spawned with no inherited turns. It
received only the eval prompt, the five assertions, and an allowlist of fixture
files; it was explicitly forbidden to read the Engineer README,
`feature-implementor` instructions, `evals.json`, or any historical
`comparison.md`, and it did not modify files.

The baseline independently read `status: Draft` and
`implementation_scope: refund-reason-codes`, recognized explicit abandonment,
selected a Superseded archive with the full required metadata, linked the
replacement active plan through `previous_plan_archive`, and waited before
coding. It passed 5/5 assertions and likewise declined to invent the missing
approver identity.

## Failures

- None.
- The paired run showed no assertion-level difference. The prompt and
  assertions expose the explicit-abandonment boundary and archive fields, so
  this eval confirms protocol correctness but has limited with-skill
  differentiation.

## Next Steps

- Keep the case focused on distinguishing explicit abandonment from the
  default behavior of continuing an unfinished Draft plan.
- If stronger differentiation is needed later, reduce rule-level hints in the
  assertions without removing the fixture evidence needed to audit archive
  metadata and linkage.

## Runtime Artifacts Policy

- The paired validation returned results in agent responses and did not create
  repository runtime files or modify fixture inputs.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status
  files, and `comparison.auto.md` must not be committed.
