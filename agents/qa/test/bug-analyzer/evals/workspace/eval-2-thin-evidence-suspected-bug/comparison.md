# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-002-thin-evidence-suspected-bug`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266` from `agents/qa/test/bug-analyzer/evals/workspace/eval-2-thin-evidence-suspected-bug`.
- Fixture SHA-256: `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266`
- Prompt SHA-256: `78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0d6c4b717279e8edddeea8100d93e004d25b98b502e0ca114092a3f0c007a52f`
- Skill overlay SHA-256: `4d1289a2f580cb07efcd85d24fb079acfc635807339f9469fa7653101393ff87`
- Judge schema SHA-256: `086365b086fd130d9ef17a34e69f11d6786884f09ea0525a080792033b47d5cb`
- Eval definition SHA-256: `ee85b4030fea85acc8c079589b9268be5087962ef495cf3e3194580abf721432`
- Metadata SHA-256: `8fd7c615ab5c3a7f7edc961336d40be79c05d55d0c11dd967998bbb2abd4e9d7`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_status_unconfirmed` | PASS | 明确分类为 `suspected / needs more evidence`，并说明不足以确认缺陷、不可复现或判断环境敏感。 |
| `separates_impact_from_confidence` | PASS | 交付记录分别列出低置信度、证据缺口与潜在数据丢失/可用性影响，未以严重度替代确定性。 |
| `requests_decisive_evidence` | PASS | 建议补采步骤、期望/实际结果、环境版本、频率，并收集截图/录屏、控制台、网络响应和服务端日志。 |
| `avoids_confirmed_bug_write` | PASS | 创建的文件明确标为待补证调查记录，并明确不应标记为 confirmed bug；没有创建 GitHub issue 或确认缺陷记录。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=ef508896975978f43f96586ace78912e13a2b6bcbe1fc995aa66c3c7ac8f48bf; snapshot_sha256=670d133ddc39593fc8bd405d41c54b273ed82cc81ff5b9bdb9c2b6ed82d10e5c
- Behavior: 保持反馈为低置信度的待补证调查，区分影响与证据强度，提出具体补证计划，并仅交付调查记录。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=bd7322ebfc2fb8bc98f8e75fec5733ab5e820011a6dc914e72fbcfc9164e230f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样保持未确认状态并提出补证建议，但未交付持久化调查记录。
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
- Skill: `bug-analyzer`
- Eval: `eval-002-thin-evidence-suspected-bug`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266` from `agents/qa/test/bug-analyzer/evals/workspace/eval-2-thin-evidence-suspected-bug`.
- Fixture SHA-256: `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266`
- Prompt SHA-256: `78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0d6c4b717279e8edddeea8100d93e004d25b98b502e0ca114092a3f0c007a52f`
- Skill overlay SHA-256: `4d1289a2f580cb07efcd85d24fb079acfc635807339f9469fa7653101393ff87`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ee85b4030fea85acc8c079589b9268be5087962ef495cf3e3194580abf721432`
- Metadata SHA-256: `8fd7c615ab5c3a7f7edc961336d40be79c05d55d0c11dd967998bbb2abd4e9d7`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_status_unconfirmed` | PASS | with_skill 输出及 delivery_snapshot 均明确标记为 suspected / needs more evidence、低置信度，未声称已确认或可复现。 |
| `separates_impact_from_confidence` | PASS | delivery_snapshot 分别说明低置信度、证据缺口，以及若保存失败可能导致用户工作丢失的暂定影响。 |
| `requests_decisive_evidence` | PASS | 输出和 delivery_snapshot 建议补充页面与完整步骤、预期/实际结果、账号数据、版本环境，并采集持久化结果、控制台、网络请求/响应、截图或录屏等直接证据。 |
| `avoids_confirmed_bug_write` | PASS | delivery_snapshot 创建的是明确标为 suspected / needs more evidence 的调查记录，未创建 GitHub issue 或确认缺陷记录，并明确工程交接尚早。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=35e69e71173b5eeb49392aae9d318dba04f2279d6d5347d2f85d1cb3525f3524; snapshot_sha256=bfe269782a1ce06b0c6724e7606ef82ef92817f520f401868a72ad4e43109f8b
- Behavior: 保持未确认和低置信度，区分影响与证据强度，提出补证计划，并创建了明确的待补证调查记录。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=1ad1adc99b156da5a28cb5bc557d86f3d1501c99f61d3a5289b4f341009991ef; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确保持未确认状态并提出补证建议；未产生持久化交付物。
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
- Skill: `bug-analyzer`
- Eval: `eval-002-thin-evidence-suspected-bug`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266` from `agents/qa/test/bug-analyzer/evals/workspace/eval-2-thin-evidence-suspected-bug`.
- Fixture SHA-256: `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266`
- Prompt SHA-256: `78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `41901c7a6c233e96234e49bc5924edbee83abf2f5546698275afb442ff6f1d8f`
- Skill overlay SHA-256: `57b0a87d033b766894f476e95aca86f50c66550e77c4d8ba3a998651bf9efccb`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ee85b4030fea85acc8c079589b9268be5087962ef495cf3e3194580abf721432`
- Metadata SHA-256: `8fd7c615ab5c3a7f7edc961336d40be79c05d55d0c11dd967998bbb2abd4e9d7`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_status_unconfirmed` | PASS | with_skill 明确说明不足以确认缺陷，并标记为“疑似 / 需要更多证据”，未声称已确认、可复现或环境敏感。 |
| `separates_impact_from_confidence` | PASS | 分别给出证据状态、低置信度和暂定严重性，并将严重性上调与“若确认造成数据未保存”挂钩。 |
| `requests_decisive_evidence` | PASS | 建议补充产品区域、步骤、版本与环境、录屏/截图、Console、Network、服务端日志及重复复现结果。 |
| `avoids_confirmed_bug_write` | PASS | 虽创建了记录，但其内容明确标为证据收集用的 QA 调查条目而非已确认缺陷，并说明确认后再创建工程缺陷。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=da6358b7f4d012bb1e3f32c10fd45746868d7e4847f611797ab1cc8153ad3279; snapshot_sha256=96e046a06b949f34b8470bb50731c9d47d72b88258839209899ac3941bae2d98
- Behavior: 保持未确认状态，区分置信度与潜在影响，提出完整补证计划，并创建了明确标为调查用途的待补证记录。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=0d0486803cd76523e935689a787fdde5e3ce5b3de945d7339ba8c3bbd2da5328; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 保持未确认状态，提出补证建议，未产生工作区变更。
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
- Skill: `bug-analyzer`
- Eval: `eval-002-thin-evidence-suspected-bug`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266` from `agents/qa/test/bug-analyzer/evals/workspace/eval-2-thin-evidence-suspected-bug`.
- Fixture SHA-256: `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266`
- Prompt SHA-256: `78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `41901c7a6c233e96234e49bc5924edbee83abf2f5546698275afb442ff6f1d8f`
- Skill overlay SHA-256: `57b0a87d033b766894f476e95aca86f50c66550e77c4d8ba3a998651bf9efccb`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ee85b4030fea85acc8c079589b9268be5087962ef495cf3e3194580abf721432`
- Metadata SHA-256: `8fd7c615ab5c3a7f7edc961336d40be79c05d55d0c11dd967998bbb2abd4e9d7`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_status_unconfirmed` | PASS | With-skill output explicitly marks the report as suspected/needs more evidence, low confidence, and says it is insufficient to confirm a defect. |
| `separates_impact_from_confidence` | PASS | The created intake separates evidence status, tentative severity/potential impact, and low confidence, explaining unknown persistence and scope. |
| `requests_decisive_evidence` | PASS | It requests reproduction steps, expected versus actual behavior, environment/version details, screenshots or recordings, console and network evidence, request IDs, and server logs. |
| `avoids_confirmed_bug_write` | PASS | The only created artifact is an untracked investigation intake explicitly classified as not a confirmed defect; no GitHub issue or confirmed-bug record was created. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=339b11e832fa2be3387aae24478b148888ed9efa3134edc027bc849505187207; snapshot_sha256=47d1017fa07df81b6a7e3be17f8babbd23954128f2bc2fdd9ed369f22b4220d7
- Behavior: Correctly kept low confidence, separated impact from evidence strength, proposed a detailed evidence plan, and created only a clearly labeled investigation intake.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=784bd6fc5e18d472b6147a46f2d919c5ad3926463e3f6ee134004f90ff9d7dcd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly kept the report unconfirmed and proposed evidence gathering; no workspace mutation.
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
- Skill: `bug-analyzer`
- Eval: `eval-002-thin-evidence-suspected-bug`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266` from `agents/qa/test/bug-analyzer/evals/workspace/eval-2-thin-evidence-suspected-bug`.
- Fixture SHA-256: `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266`
- Prompt SHA-256: `78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4a3df9ee16d4103be1f8943282fa829f43ca07121c256afa210bba92e93b1264`
- Skill overlay SHA-256: `9d14629b58659419083ead1c924b6df5c23442d8080b433d9ff5693735eb9586`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ee85b4030fea85acc8c079589b9268be5087962ef495cf3e3194580abf721432`
- Metadata SHA-256: `8fd7c615ab5c3a7f7edc961336d40be79c05d55d0c11dd967998bbb2abd4e9d7`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_status_unconfirmed` | PASS | with_skill明确表示不足以确认缺陷，仅登记为“待核实反馈”，并说明无法判断保存失败、界面反馈缺失或网络/操作问题；未声称已确认或可复现。 |
| `separates_impact_from_confidence` | PASS | with_skill区分了证据不足与不确定性，并指出潜在影响可能是保存确实失败，同时也可能只是界面反馈或网络问题。 |
| `requests_decisive_evidence` | PASS | with_skill要求补充具体步骤、预期与实际结果、时间、账号/对象、平台浏览器及版本、频率、刷新后数据状态，并请求截图/录屏及请求日志、错误记录，覆盖最小补证计划。 |
| `avoids_confirmed_bug_write` | PASS | with_skill明确要求在确认保存失败或稳定复现前不要作为已确认缺陷升级，仅建议以“待核实问题”转给工程排查。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=836f1202f6ee64ec4286f8120bd1c1a079dc19df9f3f2fe3282cf6d9e534329f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 保持待核实状态，区分证据不足与潜在影响，提出具体补证和工程排查计划，未创建确认缺陷记录。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=f02fe90a1bdb0e3e6421fd508b3963b69bdc3598e34f4d9910637055be48abfe; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 新鲜基线同样保持疑似/待复现状态，并提出复现、环境和日志等补证建议；未创建或声明确认缺陷。
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
- Skill: `bug-analyzer`
- Eval: `eval-002-thin-evidence-suspected-bug`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266` from `agents/qa/test/bug-analyzer/evals/workspace/eval-2-thin-evidence-suspected-bug`.
- Fixture SHA-256: `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266`
- Prompt SHA-256: `78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27d2fe5d8edb9052289c39964020afb301396abbc970275eb70967d32504d68`
- Skill overlay SHA-256: `bca841768a4850fe9fad50cd3d5afd91b738dda4eaad1293eea1e37d4bad841f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ee85b4030fea85acc8c079589b9268be5087962ef495cf3e3194580abf721432`
- Metadata SHA-256: `8fd7c615ab5c3a7f7edc961336d40be79c05d55d0c11dd967998bbb2abd4e9d7`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_status_unconfirmed` | PASS | With-skill output explicitly keeps the report as an unconfirmed investigation item and says not to treat it as a confirmed defect; it does not claim reproducibility or environment sensitivity. |
| `separates_impact_from_confidence` | FAIL | It describes weak evidence and uncertainty, but does not separately state the potential user impact or distinguish impact from confidence. |
| `requests_decisive_evidence` | FAIL | It requests reproduction details, expected/actual results, environment, screenshots/recordings, network responses, and logs, but omits product/app version. |
| `avoids_confirmed_bug_write` | PASS | It recommends an unconfirmed engineering investigation item and explicitly says not to treat it as a confirmed defect; no GitHub issue or confirmed bug is created. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=8cf410eb0e8561fa7fa0f6433c38a43b6fe8a0b86dc9fe602e37a6f48faddadb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Keeps the report unconfirmed and proposes an investigation workflow, but does not explicitly separate potential impact from confidence and omits product version from the evidence plan.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=1f4585bfa6f04c070038ce93cf41f408949471c74916d81db10c2cfd33386f64; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline correctly keeps the report unconfirmed and requests substantial follow-up evidence, including product version and impact-related details.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output does not explicitly distinguish potential user impact from evidence confidence.
- The with-skill evidence plan omits product/app version.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-002-thin-evidence-suspected-bug`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266` from `agents/qa/test/bug-analyzer/evals/workspace/eval-2-thin-evidence-suspected-bug`.
- Fixture SHA-256: `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266`
- Prompt SHA-256: `78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27d2fe5d8edb9052289c39964020afb301396abbc970275eb70967d32504d68`
- Skill overlay SHA-256: `bca841768a4850fe9fad50cd3d5afd91b738dda4eaad1293eea1e37d4bad841f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ee85b4030fea85acc8c079589b9268be5087962ef495cf3e3194580abf721432`
- Metadata SHA-256: `8fd7c615ab5c3a7f7edc961336d40be79c05d55d0c11dd967998bbb2abd4e9d7`
- Executor SHA-256: `c5ece8c6632badb84ff79ee67e4bea96a1d1db7e8afd66de87486af43e8fdd16`
- Runtime SHA-256: `5c4532cfa9ada91c16b3ae2d69922296ddc7c2c1c61841e01bc9c804be1b85fe`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_status_unconfirmed` | PASS | 明确保持为“待核实的问题线索”和“待复现/未确认缺陷”，未声称已确认或可复现。 |
| `separates_impact_from_confidence` | PASS | 说明当前证据不足以确认，并区分“保存失败”与“保存成功但界面无反馈”两种潜在影响。 |
| `requests_decisive_evidence` | FAIL | 要求了步骤、预期/实际结果、环境、截图或录屏及日志/请求记录，但未明确要求版本信息或 console 证据。 |
| `avoids_confirmed_bug_write` | PASS | 明确建议不要作为已确认 Bug，未创建 GitHub issue 或 confirmed bug。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 保持未确认状态并区分潜在原因，提出补证和工程调查建议，但补证清单未明确覆盖版本和 console。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 保持未确认状态，提出较完整的补证和调查建议，未创建缺陷记录。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完整提出环境版本和 console 等要求的直接证据收集计划。
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

# Eval Result: eval-002-thin-evidence-suspected-bug

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-002-thin-evidence-suspected-bug`
- Test case: thin-evidence-suspected-bug
- Workspace: `workspace/eval-2-thin-evidence-suspected-bug`
- Natural user prompt:

> 用户只提供一句反馈：偶尔点击保存后页面好像没反应，没有截图、日志、复现步骤、环境信息或版本号。请分析是否能生成 Bug 报告。

- Expected artifact: 证据不足的缺陷分析，明确 suspected / needs more evidence、缺失证据、下一步收集计划，并避免创建 confirmed bug

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/bug-analyzer--eval-002-thin-evidence-suspected-bug/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `10fdf1909715a6b1da7d96cc3c254a697af93b4cc9a6354268fbce4960a8ceb1`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **PASS**（PASS 4 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: PASS

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>薄证据分类 | PASS | candidate 明确写出“疑似问题 / 待补证据”和“suspected / needs more evidence”，并明确不能生成已确认 Bug；transcript 与快照无相反证据。 | PASS | candidate 明确称只能作为疑似问题，不能标记为已确认 Bug。 |
| `assertion_2`<br>缺失证据 | PASS | candidate 列出复现步骤、实际/期望结果、截图或录屏、日志、环境、版本、权限、数据状态、发生频率，并建议收集控制台、网络请求、错误日志等。 | FAIL | 列出了复现步骤、期望/实际结果、截图或录屏、日志、环境和版本，但未明确列出 console output、network output 或 trace 等关键缺口；“网络环境”不等于网络请求输出。 |
| `assertion_3`<br>结构化输出 | PASS | 输出包含分类（疑似问题/待补证据）、证据状态、低置信度陈述、缺失信息和建议补充证据等结构化内容。 | FAIL | 虽有当前证据、缺失信息和建议追问，但没有明确的 confidence statement，结构化段落不完整。 |
| `assertion_4`<br>持久化边界 | PASS | with_skill transcript 仅有读取技能文件和输出消息；最终 workspace-snapshot 只有 feedback/customer-note.md，未见 GitHub issue、confirmed bug artifact 或其他新文件。 | PASS | transcript 无写入/外部工具调用，最终快照同样只有原始 customer-note.md，candidate 仅建议登记疑似问题。 |

## With-Skill Behavior

with_skill 将反馈分类为 suspected / needs more evidence，明确列出证据缺口和下一步收集计划；最终快照仅保留原始 fixture，未创建确认缺陷或 GitHub artifact。

## Fresh Without-Skill Baseline

without_skill 同样避免确认 Bug，但结构化证据缺口不完整，且缺少明确的 confidence statement。

## Failures

- 无。

## Not Exercised

- 无。

## Next Steps

- 无。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
