# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-001-analyze-test-failure`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca` from `agents/qa/test/bug-analyzer/evals/workspace/eval-1-analyze-test-failure`.
- Fixture SHA-256: `e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca`
- Prompt SHA-256: `382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0d6c4b717279e8edddeea8100d93e004d25b98b502e0ca114092a3f0c007a52f`
- Skill overlay SHA-256: `4d1289a2f580cb07efcd85d24fb079acfc635807339f9469fa7653101393ff87`
- Judge schema SHA-256: `84f20ca3637061984a451201365104813c56f53ca0b37a9fb14c70d8de0d29b1`
- Eval definition SHA-256: `35f2f99594df8382cdc242359c30a451a1bdaa89727c7071b5ec00d92699fbf8`
- Metadata SHA-256: `e96ab79b6862e4b82cb2cc5b58266d1ce1ed35caa4271d16c371f2d1b6443e6f`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 报告直接记录了失败场景、500 错误、缺失的堆栈/截图/trace、console、network、环境与构建上下文，并列出各项证据状态。 |
| `assertion_2` | PASS | 报告使用了 suspected / needs more evidence，并分别记录 Evidence status 与 Confidence；根据单次失败且缺少服务端证据，分类选择合理。 |
| `assertion_3` | PASS | 报告给出 High severity 及登录主链路阻断的 rationale，并独立给出 Low confidence 及其证据依据。 |
| `assertion_4` | PASS | 报告持久化为本地 Markdown artifact：docs/qa/login-refresh/bug-valid-login-returns-500.md，未创建 GitHub issue。 |
| `assertion_5` | NOT_EXERCISED | 当前证据仅支持一次失败，报告明确无法声称可重复触发；因此确认的 E2E 回归覆盖条件未被满足。 |
| `assertion_6` | PASS | 报告包含 User / System Impact、Implementation / Release Impact，以及指向日志和构建文件的 Evidence References。 |
| `non_e2e_report_path` | PASS | 报告路径为 docs/qa/login-refresh/bug-valid-login-returns-500.md，位于 docs/qa/{feature_path}/ 下、文件名不含日期，且未使用 docs/qa-reports/。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=e6f29d61b5cf825a8b543844613bb9019fbf8ba5ea2420b22b6ff5b7f1ec5017; snapshot_sha256=5638f1df22bf505abae3369d8428fe4fd9df535f7fe1634d83b9b378157dfebe
- Behavior: 创建了结构完整的本地缺陷报告，谨慎将单次 500 归为 suspected / needs more evidence，并分离证据状态、严重度和置信度。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=88ec1c259f97530bf7f51a95b7c822a6968eb2ed18e1989a83a7b6395a6c46ba; snapshot_sha256=da15e8b12d6fe33e48d12141ad3317e1fa0a8f56cee11fa04d3b959677c65136
- Behavior: 创建了本地缺陷报告并覆盖基础复现和日志内容，但使用了 docs/defect-report-* 路径，未采用要求的分类结构，且未单独盘点完整证据缺口。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充重复复现及服务端堆栈后，再判断是否需要创建 E2E 回归用例与脚本。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-001-analyze-test-failure`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca` from `agents/qa/test/bug-analyzer/evals/workspace/eval-1-analyze-test-failure`.
- Fixture SHA-256: `e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca`
- Prompt SHA-256: `382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0d6c4b717279e8edddeea8100d93e004d25b98b502e0ca114092a3f0c007a52f`
- Skill overlay SHA-256: `4d1289a2f580cb07efcd85d24fb079acfc635807339f9469fa7653101393ff87`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `35f2f99594df8382cdc242359c30a451a1bdaa89727c7071b5ec00d92699fbf8`
- Metadata SHA-256: `e96ab79b6862e4b82cb2cc5b58266d1ce1ed35caa4271d16c371f2d1b6443e6f`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | NOT_EXERCISED | 报告直接记录了场景、错误、堆栈、截图、trace、console、network 和环境证据的存在或缺失，但锁定证据无法证明这些信息是在分类之前收集的。 |
| `assertion_2` | PASS | 报告使用了“suspected / needs more evidence”，并将 Evidence status 与 Confidence 分开记录；同时明确说明当前证据不足以确认根因。 |
| `assertion_3` | PASS | 报告给出 High severity 及其影响理由，并单独给出 Low confidence 及证据强弱依据。 |
| `assertion_4` | PASS | 锁定交付文件为本地 Markdown artifact，路径为 docs/qa/login-refresh/bug-valid-login-returns-500.md；未创建 GitHub issue。 |
| `assertion_5` | NOT_EXERCISED | 报告将可复用测试用例标记为 blocked，并说明仓库没有可确认的 E2E 功能树或执行要求；当前场景也未被确认可沉淀为 E2E 回归覆盖。 |
| `assertion_6` | PASS | 报告包含 User/system impact、Implementation/release impact，并保留 failure log 与 build context 的 evidence references。 |
| `non_e2e_report_path` | PASS | 该场景无可确认的 E2E 用例树或版本化执行要求；报告落在 docs/qa/login-refresh/ 下，文件名无日期，且未使用 docs/qa-reports/。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=c8b14701d1c1e140e89b0abc2fc4c5d1db7a28afab766acb4b46164570431d3f; snapshot_sha256=d5d6c43de65068289a961076ce6edac9322705f31281ed32a0f2c19b20c74498
- Behavior: 生成并交付了 docs/qa/login-refresh/bug-valid-login-returns-500.md，完整记录当前证据、分类、严重度、置信度、影响、引用和缺失信息；E2E 回归用例因前置条件不足而阻塞。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=1ad9304e63bcc2de6022b46e872545aa6fd0db48e121748bb03708ac778a9a7f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了未持久化的缺陷报告文本，虽包含较多证据与影响分析，但没有交付本地 Markdown artifact。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充重复复现结果及服务端 stack trace、request ID、响应体和 trace 后，再评估 E2E 回归用例是否可创建。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-001-analyze-test-failure`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca` from `agents/qa/test/bug-analyzer/evals/workspace/eval-1-analyze-test-failure`.
- Fixture SHA-256: `e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca`
- Prompt SHA-256: `382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `41901c7a6c233e96234e49bc5924edbee83abf2f5546698275afb442ff6f1d8f`
- Skill overlay SHA-256: `57b0a87d033b766894f476e95aca86f50c66550e77c4d8ba3a998651bf9efccb`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `35f2f99594df8382cdc242359c30a451a1bdaa89727c7071b5ec00d92699fbf8`
- Metadata SHA-256: `e96ab79b6862e4b82cb2cc5b58266d1ce1ed35caa4271d16c371f2d1b6443e6f`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | FAIL | 报告记录了场景、500、console、network、trace unavailable 和环境上下文，但未记录截图是否存在/缺失，也未完整明确错误消息和堆栈跟踪缺失。 |
| `assertion_2` | PASS | 报告使用了“suspected / needs more evidence”分类，并将 Evidence status 与 Confidence 分开记录；现有证据不足以使用已确认分类。 |
| `assertion_3` | PASS | 报告给出 High 严重度及阻断验收的 rationale，并单独给出 Medium confidence 及其依据。 |
| `assertion_4` | PASS | 报告持久化为本地 Markdown artifact，路径为 docs/qa/login-refresh/bug-login-valid-credentials-500.md，未创建 GitHub issue。 |
| `assertion_5` | NOT_EXERCISED | 报告明确场景尚未二次运行验证并将可复用测试用例标记为 blocked；确认且可复现的 E2E 条件未满足。 |
| `assertion_6` | PASS | 报告包含实现影响、发布影响，并通过失败日志和构建环境链接保留 evidence references。 |
| `non_e2e_report_path` | PASS | 在无 E2E 用例树或版本化执行要求的证据下，报告落在 docs/qa/login-refresh/ 下，文件名不含日期，且未使用 docs/qa-reports/。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=034224dd78c9b799f05846c5bbfecaaa9afebf0a204b3d570b17c9b157f87fc1; snapshot_sha256=d53072129b7494158e262646246e68458368013f2c5244517370af408d3e759f
- Behavior: 生成了 docs/qa/login-refresh/bug-login-valid-credentials-500.md，进行了证据边界、分类、严重度/置信度、影响和后续取证说明；未固化 E2E 用例。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=1a27b60aac973889bca5128300d110ff15bdcf72491f97a60e8f8e43784d9e08; snapshot_sha256=192dffc9f3326f52ba4247903f3ed499583ed72feb0e165243e6259ab788b805
- Behavior: 生成了 docs/defect-report-login-500.md，包含复现、环境、日志、影响和排查建议，但未按 docs/qa/ 路径交付。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- assertion_1 未完整呈现截图以及错误消息/堆栈跟踪的证据摄取状态。
- Next: 补充截图、服务端错误消息和堆栈跟踪的存在性或缺失说明；若后续确认场景可复现，再按要求固化 E2E 用例。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-001-analyze-test-failure`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca` from `agents/qa/test/bug-analyzer/evals/workspace/eval-1-analyze-test-failure`.
- Fixture SHA-256: `e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca`
- Prompt SHA-256: `382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `41901c7a6c233e96234e49bc5924edbee83abf2f5546698275afb442ff6f1d8f`
- Skill overlay SHA-256: `57b0a87d033b766894f476e95aca86f50c66550e77c4d8ba3a998651bf9efccb`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `35f2f99594df8382cdc242359c30a451a1bdaa89727c7071b5ec00d92699fbf8`
- Metadata SHA-256: `e96ab79b6862e4b82cb2cc5b58266d1ce1ed35caa4271d16c371f2d1b6443e6f`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | NOT_EXERCISED | 报告记录了场景、500 错误、console、network、trace unavailable、环境上下文及缺失的服务端堆栈等信息；但锁定证据无法证明先收集再分类的过程顺序。 |
| `assertion_2` | PASS | 报告分别记录了证据状态“疑似/需要补充证据”和独立的中等置信度，并给出“已确认且可复现”及“已确认但环境相关”的后续分类。 |
| `assertion_3` | PASS | 报告给出高（S2）严重度及其登录阻断理由，并单独给出中等置信度及证据不足的理由。 |
| `assertion_4` | PASS | 报告持久化为本地 Markdown artifact：docs/qa/login-refresh/bug-valid-login-returns-500.md；未创建 GitHub issue。 |
| `assertion_5` | NOT_EXERCISED | 报告明确只有一次失败记录，重复复现尚未确认，因此创建 E2E 用例树和脚本的条件尚未满足。 |
| `assertion_6` | PASS | 报告包含“实现与发布影响”，并保留失败日志和构建环境的 evidence references。 |
| `non_e2e_report_path` | PASS | 在没有 E2E 用例树或版本化 E2E 执行要求的 fixture 中，报告落在 docs/qa/login-refresh/ 下，文件名无日期，且未使用 docs/qa-reports/。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=80e0613082b8dd3837017e6a2b7a837447972bbc457d58f5dd21d1e3343c3f1d; snapshot_sha256=ab370a009543815e9e9b731033b797ee691c0ee0f3500cd8931d66544b716a29
- Behavior: 生成了结构化本地缺陷报告，正确区分证据状态、严重度和置信度，记录证据缺口、影响和追踪引用，并使用正确的 docs/qa 路径。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=cf44c56b52deafb64b4276bca9d9c75c58f5ad4c35eb81f4d621daa12aabb7d7; snapshot_sha256=cb08e7bf5b04ea3382ea350adec6110c29166bd25e6109cf8e29043730c7aaff
- Behavior: 生成了根目录 Markdown 报告，包含基本复现、影响和证据，但未遵循 docs/qa fallback 路径，也未明确结构化分类和独立置信度。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补采集服务端堆栈、请求关联信息、响应体及截图等缺失证据，并重复执行场景。
- Next: 若确认可复现，再创建对应的 E2E case 和 spec 脚本。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-001-analyze-test-failure`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca` from `agents/qa/test/bug-analyzer/evals/workspace/eval-1-analyze-test-failure`.
- Fixture SHA-256: `e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca`
- Prompt SHA-256: `382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27d2fe5d8edb9052289c39964020afb301396abbc970275eb70967d32504d68`
- Skill overlay SHA-256: `bca841768a4850fe9fad50cd3d5afd91b738dda4eaad1293eea1e37d4bad841f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `35f2f99594df8382cdc242359c30a451a1bdaa89727c7071b5ec00d92699fbf8`
- Metadata SHA-256: `e96ab79b6862e4b82cb2cc5b58266d1ce1ed35caa4271d16c371f2d1b6443e6f`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 报告引用并整理了失败场景、500 错误、console output、network output、trace unavailable 和构建环境；同时明确缺失堆栈、截图等证据。 |
| `assertion_2` | FAIL | 未使用 confirmed and reproducible、confirmed but environment-sensitive、suspected / needs more evidence 三类，也未分开记录 evidence status 与 confidence。 |
| `assertion_3` | PASS | 给出了高/P1 严重度及登录验收阻塞的理由，并明确说明现有证据不足以确认具体根因。 |
| `assertion_4` | FAIL | with_skill 仅输出内联报告，没有创建 durable Markdown artifact；git_status、delivery_snapshot 和 declared_outputs 均为空。 |
| `assertion_5` | NOT_EXERCISED | 原始证据未显示存在 E2E 用例树或版本化 E2E 执行要求，因此该条件性断言未被触发。 |
| `assertion_6` | FAIL | 报告包含日志和构建文件引用，但没有明确的 implementation impact 或 release impact 部分。 |
| `non_e2e_report_path` | FAIL | 未创建 fallback Bug 报告，无法证明其落在 docs/qa/{feature_path}/ 下且未使用 docs/qa-reports/。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=c6f65cd56b1a7c98f79b2178a4048f5cde81b46b1bed94819f4946135a480117; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 内联报告正确概述了登录 500 和证据边界，但未持久化输出，缺少要求的分类、影响字段和 fallback 路径。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=382c8cd397f8f6526e011c90c1ba36354751b701fabc41ae3a4966bbcf764eb3; fixture_sha256=e52dc183368f81bf8278941735b98c8f9da85437b60c6dd9736b019d7bf6c9ca; output_sha256=89b058442bc8efbf848f4ab1bbb1d9a5acaacfe6f8ea906455c8ba426f5a2475; snapshot_sha256=89be414e2d8569c40c828e3a7fe4d9aff8a7bd24ddfda0a94135d2bb37b3c8db
- Behavior: 创建了仓库根目录 defect-report-login-500.md，包含影响评估和证据边界，但未按目标路径及分类结构交付。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未创建 durable Markdown artifact。
- with_skill 未满足证据分类与 evidence status/confidence 分离要求。
- with_skill 未明确 implementation impact 或 release impact。
- with_skill 未满足非 E2E fallback Bug 报告路径要求。
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

# Eval Result: eval-001-analyze-test-failure

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-001-analyze-test-failure`
- Test case: analyze-test-failure
- Workspace: `workspace/eval-1-analyze-test-failure`
- Natural user prompt:

> 分析测试失败：登录表单提交后返回 500 错误，生成 Bug 报告

- Expected artifact: 详细 Bug 报告，明确 evidence status、confidence statement 和 severity rationale，并包含 impact framing、复现步骤、环境信息和 evidence references

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/bug-analyzer--eval-001-analyze-test-failure/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `33e2cd10d9a244693e762c92b4220b0af0e494fc45e57646a727891c662e3a32`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **PASS**（PASS 6 / FAIL 0 / NOT EXERCISED 1）
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>证据摄取 | PASS | transcript item_4 读取了失败场景、500 错误、console、trace 状态和构建上下文；item_5 及报告明确记录服务端堆栈、响应体、重复复现等证据缺口，未凭空补全不存在的证据。fixture 中没有截图、独立 trace 或 network 文件。 | PASS | transcript item_2 读取失败日志和环境上下文，记录了 console 与 trace unavailable；报告明确列出缺失的服务端堆栈、响应体和 HAR/trace。 |
| `assertion_2`<br>分类分离 | PASS | 快照报告 Classification 明确写出 Evidence status: suspected / needs more evidence，并单独写出 Confidence: Medium；transcript item_5 也采用该分类。 | FAIL | 报告仅写“状态：待调查”和“当前证据不足”，没有使用 confirmed and reproducible、confirmed but environment-sensitive、suspected / needs more evidence 分类，也没有独立的 evidence status 与 confidence 字段。 |
| `assertion_3`<br>严重度与置信度 | PASS | 快照报告给出 Severity: High，并解释登录可能被整体阻断；同时给出独立的 Confidence: Medium 及其证据依据。 | FAIL | 报告给出高严重程度及影响理由，但没有明确 confidence statement，也未将证据强度作为独立置信度记录。 |
| `assertion_4`<br>持久输出路径 | PASS | transcript item_6 执行 mkdir -p docs/qa/auth，item_7 增加报告；最终快照实际存在 docs/qa/auth/bug-login-submit-500.md，且 status 显示正常完成。 | PASS | transcript item_5 增加本地 Markdown 报告，最终快照确认 bug-report-login-500.md 存在；满足本地 durable artifact 要求。 |
| `assertion_5`<br>可复用回归用例 | NOT EXERCISED | 该断言仅在确认的 E2E 复现场景需要沉淀回归覆盖时触发；报告分类为 suspected / needs more evidence，fixture 只有一次失败日志，没有 E2E 用例树或版本化执行要求。 | NOT EXERCISED | 同样没有确认的 E2E 复现场景或 E2E 用例树；报告中的验收标准建议不足以触发该条件。 |
| `assertion_6`<br>影响说明 | PASS | 快照报告包含明确的 Impact 段落，并引用 logs/test-failure.log 与 environment/build.md；transcript item_9 核验报告内容成功。 | FAIL | 报告有“影响范围”和 evidence 来源，但没有明确的 implementation impact 或 release impact 段落/表述，未完全满足断言。 |
| `non_e2e_report_path`<br>非 E2E 报告路径 | PASS | fixture 未提供 E2E 用例树或版本化 E2E 执行要求；最终快照路径为 docs/qa/auth/bug-login-submit-500.md，位于 docs/qa/{feature_path}/ 下，文件名无日期，也未使用 docs/qa-reports/。 | FAIL | 最终快照中的报告位于工作区根目录 bug-report-login-500.md，不在 docs/qa/{feature_path}/ 下。 |

## With-Skill Behavior

with_skill 生成了 durable Markdown 报告，包含分类、置信度、严重度理由、影响说明、复现步骤、环境信息和证据引用；最终快照确认文件确实存在。

## Fresh Without-Skill Baseline

without_skill 也生成了报告并收集了基础日志，但缺少独立的 evidence status/confidence，且输出路径不符合非 E2E fallback 约定。

## Failures

- 无。

## Not Exercised

- with_skill assertion_5：未确认 E2E 复现场景，且 fixture 不含 E2E 用例树或版本化执行要求。
- without_skill assertion_5：未确认 E2E 复现场景，且 fixture 不含 E2E 用例树或版本化执行要求。

## Next Steps

- 如需 FULL coverage，补充可确认/可重复的 E2E 复现场景或明确的 E2E 执行要求，再核验 cases/TC-NNN-*.md 与 scripts/TC-NNN-*.spec.md。
- 如修正 baseline，应补充独立 evidence status/confidence，并将报告移至 docs/qa/auth/ 下。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
