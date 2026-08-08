# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-001-verify-bug-fix`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308` from `agents/qa/test/regression-suite/evals/workspace/eval-1-verify-bug-fix`.
- Fixture SHA-256: `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308`
- Prompt SHA-256: `c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8289acf8e27bfd57efcbcc6d726b9bfaa4df0b2cb5c60400d61eca4c6f8c65d4`
- Skill overlay SHA-256: `a284e7eb3465da68b2d3792a2435d75549c3a3732ed503ef22754fbfde0a19d1`
- Judge schema SHA-256: `2c18050b9a27d5dccf92b0604097b9078533d47105266364099eafbf3833aad8`
- Eval definition SHA-256: `8ca6ea4c46c7a5a2c854d9ff5def7ea0ec612ddbf9888a829e50de270f1b84c4`
- Metadata SHA-256: `732278c998a10f6e6333dc13e2fc4edfbaed96da1abb806d2dc29682a3a79f75`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | NOT_EXERCISED | 报告引用 BUG-001、PR-001，并沿用原始失败、期望行为及相邻风险界定范围；但读取先后顺序无法由锁定证据证明。 |
| `qa` | NOT_EXERCISED | 报告列出 TEST_SUITE.md、FLOW_INDEX.md、TC-001 case 和 script，并说明历史 results/_reports 不存在；但执行前读取顺序无法由锁定证据证明。 |
| `assertion_3` | NOT_EXERCISED | 报告明确将修复验证、原始失败复查和期望修复行为标为 blocked，但缺少运行时证据，实际修复行为未被执行验证。 |
| `assertion_4` | PASS | 报告按 feature-update 范围覆盖原始登录、无效凭据、锁定账户及共享序列化路径，未扩展为全量 active E2E。 |
| `alignment_version_archive` | FAIL | 报告确认 PRD/TRD/IMPLEMENTATION_PLAN 对齐并将平台版本标记为 blocked；但锁定交付物写入 _reports/test-reports...md，而非要求的 results/.../result.md 和 testcase.snapshot.md。 |
| `assertion_5` | PASS | 报告同时给出 blocked/not executed、evidence_confidence: low 和 release_recommendation: needs more verification，并避免宣称已就绪。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=5198e500ae4b4a28514287628a899c53bfdec4e1fd9aa158b31d096e0d4c7201; snapshot_sha256=c39e88cdbcc366d6d1e3f05275e12ffe4cab6515926362358bf72c1c68d63a59
- Behavior: 生成了结构化的 BLOCKED 回归报告，明确范围、对齐门禁、证据置信度和发布建议，但未执行运行时验证，并产生了不符合归档要求的 _reports 文件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=631e63a478fcaa1cd01116641dcfbe9e3ec464049a5d7c560dc1de8b72d6d689; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样因缺少 package.json 和 QA_BASE_URL 无法执行验证；仅给出简要阻塞结论，未交付回归报告。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 回归报告被写入 _reports，而不是要求追加的 results/TC-NNN-<short-slug>/{platform-version}/result.md 和 testcase.snapshot.md。
- Next: 补齐可运行 harness 或配置 QA_BASE_URL。
- Next: 在声明的平台版本上执行原始登录、无效凭据和锁定账户路径。
- Next: 按要求将结果追加到 results/.../result.md 和 testcase.snapshot.md，保留历史结果。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-001-verify-bug-fix`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308` from `agents/qa/test/regression-suite/evals/workspace/eval-1-verify-bug-fix`.
- Fixture SHA-256: `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308`
- Prompt SHA-256: `c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8289acf8e27bfd57efcbcc6d726b9bfaa4df0b2cb5c60400d61eca4c6f8c65d4`
- Skill overlay SHA-256: `5963f60ead81ffc5fd7b8778d6215ec69825a76246473fc9777aee19c6576e9c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8ca6ea4c46c7a5a2c854d9ff5def7ea0ec612ddbf9888a829e50de270f1b84c4`
- Metadata SHA-256: `732278c998a10f6e6333dc13e2fc4edfbaed96da1abb806d2dc29682a3a79f75`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | NOT_EXERCISED | 报告引用了 BUG-001、PR-001 并沿用了原始期望与回归范围，但锁定证据无法证明“先读取”的顺序。 |
| `qa` | NOT_EXERCISED | 报告记录了 TEST_SUITE、FLOW_INDEX、case、script 及历史目录状态，但锁定证据无法证明这些资料是在执行前读取。 |
| `assertion_3` | NOT_EXERCISED | 报告明确记录整体 BLOCKED，但缺少运行时证据；原始失败复查和修复后行为均为 not executed。 |
| `assertion_4` | PASS | 报告将场景标为 feature-update，并覆盖原始登录、无效凭据、锁定账户及共享响应序列化等直接影响路径，未扩展为 release 全量回归。 |
| `alignment_version_archive` | PASS | 报告确认同 feature_path 下 PRD/TRD/IMPLEMENTATION_PLAN 均已对齐且 Confirmed，确认平台版本 v1.2.0-fix.1，并记录到按版本分层的 result.md 与 testcase.snapshot.md。 |
| `assertion_5` | PASS | 报告包含 release recommendation，明确 run status 为 blocked、evidence confidence 为 low，并建议 needs more verification、暂不关闭缺陷。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=1333604c65d593cbfe4255d98a8be5b5ed7ee006519e59e83227dbbb5d504c3b; snapshot_sha256=fba01951b2ea8550bce871b47fa6d8e55943584d392158e649d1b1751542d0fe
- Behavior: 完成对齐门禁、回归范围和阻塞状态记录，交付版本化结果与快照；因运行环境缺失未执行实际验证。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=632aa24d6c5fc9aa47c5710d0dde454f20890c2752c0bf5f8c27cf69fbe3c55d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到缺少 harness、package.json 和 QA_BASE_URL，结论为无法验证；未交付回归归档结果。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 在 v1.2.0-fix.1 的可运行构建或 QA 环境中重跑 TC-001，验证有效登录、无效凭据和锁定账户路径。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-001-verify-bug-fix`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308` from `agents/qa/test/regression-suite/evals/workspace/eval-1-verify-bug-fix`.
- Fixture SHA-256: `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308`
- Prompt SHA-256: `c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `93e5fd0d6baa599b41823d84d9e76df4ae1d287d1ee0dc585a0fbe0d3c54e8d5`
- Skill overlay SHA-256: `9883d5bccab96c99ea3ecc04b59f35a7f6a047a4260200cdf425c896a87f0f3e`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8ca6ea4c46c7a5a2c854d9ff5def7ea0ec612ddbf9888a829e50de270f1b84c4`
- Metadata SHA-256: `732278c998a10f6e6333dc13e2fc4edfbaed96da1abb806d2dc29682a3a79f75`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | NOT_EXERCISED | 候选报告复述了 BUG-001 的原始失败、期望行为和 PR-001 修复上下文，但锁定证据无法证明具体读取顺序。 |
| `qa` | NOT_EXERCISED | 报告列出并记录了 TEST_SUITE、FLOW_INDEX、case、script 及历史目录状态，但锁定证据无法证明实际读取过程。 |
| `assertion_3` | PASS | 报告明确给出 blocked 状态，并说明 original failure recheck 与 fixed behavior 均未执行及其阻塞原因，结论未误报为通过。 |
| `assertion_4` | PASS | 候选将范围限定为 feature-update，覆盖原始成功登录、共享响应逻辑及 invalid-credential、locked-account 两条相邻路径，未扩展到全量 release E2E。 |
| `alignment_version_archive` | FAIL | 对齐门禁、IMPLEMENTATION_PLAN 引用和平台版本均有记录，但结果写入了 _reports/v1.2.0-fix.1/test-reports-20260808-192035.md，而要求结果仅追加至 results/TC-001-login-session/{platform-version}/result.md 和 testcase.snapshot.md。 |
| `assertion_5` | PASS | 报告包含 Release Recommendation，明确建议 blocked、不得关闭缺陷或发布，并将 run status 与 evidence confidence（low）分开说明。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=c823b6ec02a42d2ae00203c3b647fe8626fde7fb03e5e13961b60019af83a29c; snapshot_sha256=15d5c8d41ee2faba47209e91bd1a4569bedc1d128f539befed3ffea23b90904c
- Behavior: 正确完成范围、对齐和阻塞式回归报告，诚实区分运行状态与证据置信度；但违反结果归档路径要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=c4dacb660bfb4c2cd005d2f452c3823fa3a74dcaadb615d79a9b0a30120fa78e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到缺少 package.json、QA_BASE_URL 和运行时 harness，结论为未验证，但未提供正式回归报告或发布建议结构。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 将回归报告写入 _reports，而不是要求的 results/TC-001-login-session/{platform-version}/result.md 和 testcase.snapshot.md。
- Next: 将报告及快照按要求追加到指定 results 路径，并在可运行 harness 或 QA 环境恢复后重新执行原始与相邻路径回归。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-001-verify-bug-fix`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308` from `agents/qa/test/regression-suite/evals/workspace/eval-1-verify-bug-fix`.
- Fixture SHA-256: `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308`
- Prompt SHA-256: `c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `93e5fd0d6baa599b41823d84d9e76df4ae1d287d1ee0dc585a0fbe0d3c54e8d5`
- Skill overlay SHA-256: `e9706a0f5c60f10753664f62398d5e5d1b2198510bb7a2bd63d1c64e17ebc61f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8ca6ea4c46c7a5a2c854d9ff5def7ea0ec612ddbf9888a829e50de270f1b84c4`
- Metadata SHA-256: `732278c998a10f6e6333dc13e2fc4edfbaed96da1abb806d2dc29682a3a79f75`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | NOT_EXERCISED | 候选输出提及并引用了 BUG、修复和回归范围，但锁定原始证据无法证明这些资料的读取顺序。 |
| `qa` | NOT_EXERCISED | 交付记录声称读取了 QA 资料及历史目录状态，但锁定证据无法证明读取发生在回归执行之前。 |
| `assertion_3` | PASS | 明确记录 original failure recheck、fixed behavior 和 verification result 均为 blocked，并说明缺少可执行环境。 |
| `assertion_4` | PASS | 按 feature-update 范围检查成功登录、无效凭据、锁定账户及共享序列化路径，未扩展到全部 active E2E。 |
| `alignment_version_archive` | FAIL | 确认了 PRD、TRD、IMPLEMENTATION_PLAN 和平台版本，也创建了正确版本目录下的 result.md；但未提供要求的 testcase.snapshot.md，且额外创建了报告文件。 |
| `assertion_5` | PASS | 回归报告包含 release recommendation，并明确区分 run status 与 evidence confidence，结论为 blocked/needs more verification，未宣称可发布。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=826cee5ef26ae6c5318e0ae682bd91d0e2956bf65162d245c01bd29eb9475ef6; snapshot_sha256=b0f4f749f5f4278106c18a2eb69291a5b65a38eb692581ae0108b06ddc89f259
- Behavior: 正确完成范围界定、阻塞式验证记录和发布建议，并产出结果与报告；归档要求未完整满足。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=92cb47cb1316ae328644dba2176b6c6f196c530a340bb331a8e9b16e76c018b0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别出运行环境缺失并给出阻塞结论，但未产出归档回归结果或正式报告。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未创建 testcase.snapshot.md，未完整满足版本归档要求。
- Next: 补充 testcase.snapshot.md 并确认归档目录符合要求。
- Next: 提供可运行修复构建或测试 harness，设置 QA_BASE_URL（如需浏览器验证），重新执行三条回归路径。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-001-verify-bug-fix`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308` from `agents/qa/test/regression-suite/evals/workspace/eval-1-verify-bug-fix`.
- Fixture SHA-256: `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308`
- Prompt SHA-256: `c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e0bb997f7c8683c58b155379f15e9833f91e4d2f51aece7bfcfa4974d6a1defb`
- Skill overlay SHA-256: `5380fc16efa2deba2f3d503697de616d07aef499ace1b8bbfa59e73c1e19fe13`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8ca6ea4c46c7a5a2c854d9ff5def7ea0ec612ddbf9888a829e50de270f1b84c4`
- Metadata SHA-256: `732278c998a10f6e6333dc13e2fc4edfbaed96da1abb806d2dc29682a3a79f75`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With-skill report records the original HTTP 500, expected session/redirect behavior, fix context, and regression scope. |
| `qa` | PASS | With-skill output confirms the required QA suite, flow index, case, script, and absence of historical results/reports were accounted for; it created versioned report and result artifacts without adding a new test case. |
| `assertion_3` | PASS | The report explicitly labels original failure recheck and expected fixed behavior as not executed, with overall verification status blocked. |
| `assertion_4` | PASS | The run is identified as feature-update and covers the original path plus shared serialization, invalid-credential, locked-account, and error-recovery adjacent paths without expanding to release scope. |
| `alignment_version_archive` | PASS | The report confirms aligned PRD/TRD and IMPLEMENTATION_PLAN, records platform version v1.2.0-fix.1, and writes versioned result.md and testcase.snapshot.md under the required paths. |
| `assertion_5` | PASS | The report includes a needs-more-verification release recommendation and separately records blocked run status and low evidence confidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=2cbeebb0adaf84596831022b057170bfcfd8354f7787f1414f1a1d424492943e; snapshot_sha256=601fda1434f85dc5ba9d4d8a60fe6a31f811b83065c14744d1f8a7bb42e7408a
- Behavior: Produced an evidence-aligned blocked regression report, versioned result artifacts, explicit per-path statuses, alignment checks, and a cautious release recommendation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=be79fb42663bebd080800ad06b8644417eec7daab66b446e10e4b5f23dd9f0f2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline recognized missing executable evidence and reported blocked, but did not produce the required structured QA regression artifacts.
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

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-001-verify-bug-fix`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308` from `agents/qa/test/regression-suite/evals/workspace/eval-1-verify-bug-fix`.
- Fixture SHA-256: `de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308`
- Prompt SHA-256: `c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `850108c3e4722feb1b9e0417b1554f0fb5b41d47001505d7da16c6bcd9946093`
- Skill overlay SHA-256: `3af177f0dcd9723964fdbcbf144832d8c6b68b267a850af3da918d86fe27d617`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8ca6ea4c46c7a5a2c854d9ff5def7ea0ec612ddbf9888a829e50de270f1b84c4`
- Metadata SHA-256: `732278c998a10f6e6333dc13e2fc4edfbaed96da1abb806d2dc29682a3a79f75`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | with_skill 报告明确引用 BUG-001 与 PR-001，并以有效登录 500、会话创建和 dashboard 跳转界定原始与修复范围。 |
| `qa` | FAIL | 报告引用了 TEST_SUITE 相关范围和 TC-001，但未提供读取 FLOW_INDEX、case、script 以及历史 results/ 和 _reports/ 的证据。 |
| `assertion_3` | PASS | 报告分别标明 Status: blocked、Original failure recheck: not executed、Expected fixed behavior: not executed，并说明运行验证结果被环境阻塞。 |
| `assertion_4` | PASS | 报告按 feature-update 限定原始成功登录、无效凭据和锁定账户等直接相邻路径，未扩展到 release 全量 E2E。 |
| `alignment_version_archive` | FAIL | 报告确认 PRD、TRD、IMPLEMENTATION_PLAN 均为 Confirmed 且平台版本为 v1.2.0-fix.1，但结果写入 _reports/test-reports-2026-08-08.md，未按要求追加 results/TC-001-login-session/{platform-version}/result.md 和 testcase.snapshot.md。 |
| `assertion_5` | PASS | 报告包含 Release Recommendation，并明确区分 Fix Verification 的 blocked run status 与 low evidence confidence。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=b5c90a74fb86fc96d16b185e8c617b295010d8781f358c81bdf9b7591af7e070; snapshot_sha256=36ea3a4d753d486f29f2cd7fef5bcdf5b064cf55ea5cea92948c12e5025c7063
- Behavior: 完成对齐门禁、定向范围和相邻路径规划，明确 blocked 状态及低证据置信度，但结果归档路径不合规且未证明完整复用 QA 资料。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c6a22bd6a4c946877c350cf1e3485fb0daa745bafdccb74f798f1fdae43d71c0; fixture_sha256=de9aee791f056463d193f05e53c9f483fe312d6ee3aeb7bb4d1f7b0eb008f308; output_sha256=b9559ec782e260e1f16c2533e144c630eacf84069027ae94bc31a13da8378071; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到缺少 package.json 和运行环境，结论为 blocked；范围和发布建议较简略。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足完整 QA 用例资料读取证据。
- with_skill 未按规定的 results/{TC}/{platform-version}/result.md 与 testcase.snapshot.md 归档结果。
- Next: 补充完整 QA 资料读取记录，并按规定路径追加 result.md 和 testcase.snapshot.md。

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

# Eval Result: eval-001-verify-bug-fix

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-001-verify-bug-fix`
- Test case: verify-bug-fix
- Workspace: `workspace/eval-1-verify-bug-fix`
- Natural user prompt:

> 验证 Bug #001 的修复，执行回归测试

- Expected artifact: 回归验证报告，明确 original failure recheck、fixed behavior、adjacent regression checks 和 release recommendation

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/regression-suite--eval-001-verify-bug-fix/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `5923f8e6a9744051a7d093120915c47b16783a2f79be9b5e4c4bb0f0959c8c3f`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **PASS**（PASS 6 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: PASS

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>证据复用 | PASS | transcript item_3 读取 bugs/BUG-001.md、fixes/PR-001.md 及 QA 测试材料；item_9 的最终报告复用了原始失败和修复上下文。 | PASS | transcript item_2 读取了 BUG-001、PR-001 及测试文档，并据此说明无法执行回归。 |
| `qa`<br>QA 用例复用 | PASS | transcript item_3 在执行前读取 TEST_SUITE.md、FLOW_INDEX.md、cases/TC-001-login-session.md 和 scripts/TC-001-login-session.spec.md；最终快照确认这些文件均保留。初始 fixture 不存在历史 results/ 或 _reports/，因此无遗漏可读的历史结果。未新增用例，新增用例条件未触发。 | PASS | transcript item_2 读取了 TEST_SUITE、FLOW_INDEX、cases 和 scripts；没有新增用例需求。 |
| `assertion_3`<br>修复验证 | PASS | 最终快照中的 _reports/v1.2.0-fix.1/test-reports-20260807-003518.md 明确记录 Status=blocked、Original failure=not rechecked、Fixed behavior=not verified，并说明 verification evidence 不足。 | FAIL | candidate.md 只笼统说明无法验证，未将 original failure、fixed behavior 和 verification result 逐项明确标为 pass、fail 或 blocked。 |
| `assertion_4`<br>邻近回归 | PASS | TEST_SUITE.md 明确为 feature-update；最终报告只覆盖原始登录失败、直接影响的 invalid-credential 和 locked-account 路径，并明确未扩展到 release 全量 E2E。transcript 未显示执行无关全量测试。 | PASS | transcript item_2 读取了 feature-update 范围；candidate 仅讨论成功登录、无效凭据和锁定账户三条相关路径，未显示扩展到 release 全量 E2E。 |
| `alignment_version_archive`<br>对齐门禁与版本归档 | PASS | transcript item_3 检查并发现同路径 PRD/TRD/IMPLEMENTATION_PLAN 缺失；最终报告显式记录 alignment gate、platform version v1.2.0-fix.1 和下一责任方，并因门禁缺失保持 blocked。file_change trace 显示仅新增 _reports/v1.2.0-fix.1/test-reports-20260807-003518.md；最终快照无 results 覆盖或伪造归档。 | FAIL | transcript 和最终快照均未检查或引用同路径 PRD/TRD/IMPLEMENTATION_PLAN，也未生成要求的版本化回归归档。 |
| `assertion_5`<br>发布建议 | PASS | 最终报告包含 Release Recommendation=Hold release / do not close BUG-001，并在 Fix Verification 中分别记录 Status=blocked 与 Evidence confidence=low。 | FAIL | candidate.md 没有 release recommendation，也没有将 run status 与 evidence confidence 分开记录。 |

## With-Skill Behavior

with_skill 按要求读取并复用 Bug、修复说明及 QA 用例；发现 PRD/TRD/IMPLEMENTATION_PLAN、源码和测试环境缺失后，将原始失败、修复行为及邻近路径明确标为 blocked，并生成带版本归档的回归报告。

## Fresh Without-Skill Baseline

without_skill 执行了 npm 命令并识别 package.json 缺失，但未完成对齐门禁、结构化回归报告或版本归档。两条 lane 的初始 fixture 文件内容及 SHA-256 完全一致；with_skill 仅新增了 _reports 回归报告。

## Failures

- 无。

## Not Exercised

- 无。

## Next Steps

- 补齐同路径 PRD、TRD 和已确认的 IMPLEMENTATION_PLAN.md。
- 提供源码、package.json、可运行测试 harness 或 QA_BASE_URL。
- 重新执行 original failure、fixed behavior、invalid-credential 和 locked-account 检查，并追加对应版本结果。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
