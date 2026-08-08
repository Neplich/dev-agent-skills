# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-003-no-dates`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f` from `agents/product_manager/test/roadmap-gen/workspace/eval-3-no-dates`.
- Fixture SHA-256: `8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f`
- Prompt SHA-256: `4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `74b972ac8dbd7706448e20025f6995b87c544e99309b65961f70d0e86a7bd191`
- Skill overlay SHA-256: `bddee41393bca0a60880eaa8d81044ec84f2c1d751e6af66c6178450b19850d3`
- Judge schema SHA-256: `f6a7dabb82746a0dc0f0c5965d8e78c276cdccf3d2da25bfbb1a77e91ffeca3f`
- Eval definition SHA-256: `fbd695e0a879758e25936e89babfefc9a6cba4a52e1572a61e1da7fea0b1364b`
- Metadata SHA-256: `1dfb7bfbfed7613af8764f4385cade9d5822d1652d85a0cbb75853e0bcae7474`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `semantic_classification` | PASS | 交付的 docs/roadmap.md 按当前版本后的补丁版 Go1.26.1、下一 minor Go1.27、远期 major Go2.0 分类，并将 Runtime experiments 标为无法仅凭名称确认阶段、待维护者确认。 |
| `no_fake_dates` | PASS | 交付文件明确记录 due_on 均为 null，未生成 Mermaid Gantt；日期仅使用证据中的抓取/更新上下文。 |
| `release_blockers` | PASS | 交付文件以“发布阻塞项”突出列出带 release-blocker 标签的 #4101。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a; fixture_sha256=8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f; output_sha256=f7b5cee9d5a79c3d436d7fcc96583c32f6014a84acf6cc89ccb158ac0bdced62; snapshot_sha256=e071008d39586820391975b638a350319b5cb46d902544287410dc3ba5f8f7bf
- Behavior: 成功写入路线图，完成语义分类、日期约束和发布阻塞项突出显示。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a; fixture_sha256=8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f; output_sha256=eb0b5db69da2c9220987703d084cd3d6df6b9f5abb267320e2841e67ddd92d21; snapshot_sha256=7dd086fbbd65d13eec0975ec73ed463e9ddcd05e9531f022cc3fe5b269f2f8e0
- Behavior: 也写入了路线图并覆盖主要版本分类与日期约束，但未明确将无法匹配的 milestone 交用户确认。
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

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-003-no-dates`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f` from `agents/product_manager/test/roadmap-gen/workspace/eval-3-no-dates`.
- Fixture SHA-256: `8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f`
- Prompt SHA-256: `4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `74b972ac8dbd7706448e20025f6995b87c544e99309b65961f70d0e86a7bd191`
- Skill overlay SHA-256: `bddee41393bca0a60880eaa8d81044ec84f2c1d751e6af66c6178450b19850d3`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `fbd695e0a879758e25936e89babfefc9a6cba4a52e1572a61e1da7fea0b1364b`
- Metadata SHA-256: `1dfb7bfbfed7613af8764f4385cade9d5822d1652d85a0cbb75853e0bcae7474`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `semantic_classification` | PASS | with_skill 的锁定 docs/roadmap.md 按当前 go1.26.0 将 Go1.26.1 归为补丁版、Go1.27 归为下一次 minor、Go2.0 归为明显远期，并将 Runtime experiments 标为待维护者分类、Backlog 标为显式未排期。 |
| `no_fake_dates` | PASS | 锁定交付文件明确记录所有 due_on 为 null，未生成 Mermaid Gantt，也未编造开始或截止日期；使用的是不表示日历排期的 Mermaid flowchart。 |
| `release_blockers` | PASS | 锁定交付文件在 Go1.26.1 下以“发布阻塞项”专门突出显示 #4101，并保留 release-blocker 标签。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a; fixture_sha256=8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f; output_sha256=0179d5b882597a858bea8e0e559f1afc7e12c97d63d1ca7016f5d3aeca97e3ed; snapshot_sha256=ba84ae0cede4873dc3c66d0b6b42d81c6090fa17c24a0c435301064e8937efbb
- Behavior: 写入 docs/roadmap.md，完成语义分类、未知分类项标注、无日期约束及发布阻塞项突出显示。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a; fixture_sha256=8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f; output_sha256=ffa61a9046e765323a7c6c9913c575deb2e411ec208df0f3d2cfe55bbe05ae4f; snapshot_sha256=c1dc501398b7c8a58f4f1927725eeadfb7137db8a2a2526d77ae09af714855dc
- Behavior: 完成路线图并按版本语义排列，声明未添加日期；未在最终内容中直接展示发布阻塞项。
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

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-003-no-dates`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f` from `agents/product_manager/test/roadmap-gen/workspace/eval-3-no-dates`.
- Fixture SHA-256: `8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f`
- Prompt SHA-256: `4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a12253d9a3d1d231837468fc266a18cbef8c731ab282a55d4d464a493ca02f11`
- Skill overlay SHA-256: `c50d53c79d2138148c86c2ddaa4ea3403b46c5d6a9d3d67baf48a5203cd6d0b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `fbd695e0a879758e25936e89babfefc9a6cba4a52e1572a61e1da7fea0b1364b`
- Metadata SHA-256: `1dfb7bfbfed7613af8764f4385cade9d5822d1652d85a0cbb75853e0bcae7474`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `semantic_classification` | PASS | with_skill 将 Go1.26.1、Go1.27、Go2.0 分别归为补丁、近期 minor 和远期主版本，并将 Runtime experiments 标为待维护者确认、Backlog 标为显式未排期。 |
| `no_fake_dates` | PASS | with_skill 明确说明 milestone 无截止日期，未生成 Mermaid Gantt，也未作日历排期承诺；使用的采集时间来自原始证据。 |
| `release_blockers` | PASS | with_skill 在 Go1.26.1 下以“发布阻塞项”标题突出列出带 release-blocker 标签的 #4101。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a; fixture_sha256=8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f; output_sha256=d274640d2d2a093696564e68eb232259f31939660bdab771c48d943f0a88a1b2; snapshot_sha256=d167d941a37d3d5589d9295ff36549c2c9ec6e7c9978ecb3b9beaa68c8bb985f
- Behavior: 写入了基于 semver 的分阶段路线图，处理了无法按版本匹配的 milestone，避免虚构排期，并突出发布阻塞项。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a; fixture_sha256=8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f; output_sha256=bd470d2de82d86b98e3ac5bc6cd01c1df6304618716219388e274cffeefaeb28; snapshot_sha256=031885dddf03e406261a0c2216a5b589a66c99242baec63001d303e3f9dc3d8b
- Behavior: 写入了路线图并避免虚构日期，基本完成版本分组和阻塞项识别。
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

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-003-no-dates`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f` from `agents/product_manager/test/roadmap-gen/workspace/eval-3-no-dates`.
- Fixture SHA-256: `8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f`
- Prompt SHA-256: `4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a12253d9a3d1d231837468fc266a18cbef8c731ab282a55d4d464a493ca02f11`
- Skill overlay SHA-256: `c50d53c79d2138148c86c2ddaa4ea3403b46c5d6a9d3d67baf48a5203cd6d0b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `fbd695e0a879758e25936e89babfefc9a6cba4a52e1572a61e1da7fea0b1364b`
- Metadata SHA-256: `1dfb7bfbfed7613af8764f4385cade9d5822d1652d85a0cbb75853e0bcae7474`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `semantic_classification` | FAIL | The with_skill output correctly classifies Go1.26.1 as the patch/current sprint, Go1.27 as the next minor, and Go2.0 as a distant major. However, unmatched milestones are only labeled “待维护者分类” or “未排期”; they are not explicitly handed to the user for confirmation as required. |
| `no_fake_dates` | PASS | The with_skill roadmap states that no dates were invented and contains no Mermaid Gantt or calendar-based schedule. Its flowchart explicitly says it represents semantic relationships, not dates. |
| `release_blockers` | PASS | The with_skill roadmap prominently displays a “发布阻塞项” section and includes issue #4101 with the release-blocker label. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a; fixture_sha256=8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f; output_sha256=9e1738093ba27047bcaca61af9ac6d7c6c6eef1c4925ee093b10d8172c6a43c7; snapshot_sha256=01ba33fec59e510671aeacd96c32e479cc8472e8233b79b1ce6b835cd27403f9
- Behavior: Created the roadmap with semantic version grouping, explicit no-date handling, incomplete-export caveats, and a prominently displayed release blocker; it did not explicitly request user confirmation for unmatched milestones.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a; fixture_sha256=8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f; output_sha256=abec560e30a0294eef9de078a9a480e4950de84ae16d1801afc64b82839e6928; snapshot_sha256=f8324a1af0a7d20c98446b09bb562a437e516f173be1a388c3ecddeb87d2c4d7
- Behavior: Created the requested roadmap, avoided fabricated dates, and presented the release-blocker issue, but used less explicit semantic classification and confirmation handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- semantic_classification is not fully satisfied because unmatched milestones are not explicitly handed to the user for confirmation.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-003-no-dates`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f` from `agents/product_manager/test/roadmap-gen/workspace/eval-3-no-dates`.
- Fixture SHA-256: `8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f`
- Prompt SHA-256: `4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2b8eaa887e0089b78c69e8bf72f0824676518d33b5c372709e901a79190cd61b`
- Skill overlay SHA-256: `61c47c3293a0a8c5746d4b748abf3c5e11689bfbf0a0493a9b3beca73cbb7663`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `fbd695e0a879758e25936e89babfefc9a6cba4a52e1572a61e1da7fea0b1364b`
- Metadata SHA-256: `1dfb7bfbfed7613af8764f4385cade9d5822d1652d85a0cbb75853e0bcae7474`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `semantic_classification` | PASS | with_skill 输出按当前 go1.26.0 将 Go1.26.1 归为补丁、Go1.27 归为次版本、Go2.0 归为主要版本；对无版本号的 Runtime experiments 明确标为待维护者确认。 |
| `no_fake_dates` | PASS | with_skill 输出明确所有 milestone 的 due_on 缺失，未生成 Mermaid Gantt，也未虚构日期或日历排期；使用的更新时间与导出时间有原始证据支持。 |
| `release_blockers` | PASS | with_skill 输出以“发布阻塞项”醒目标注 Go1.26.1 中带有 release-blocker 标签的 issue #4101。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a; fixture_sha256=8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f; output_sha256=59c6d5bcd80d5b6f20d6ee6ddee8a875e2a4c2529430113a5525fcf96403db1e; snapshot_sha256=349e02c7d6fb72f6d90ecb281231df2a8f644605027c05155a95812b143ca5c1
- Behavior: 完成路线图，正确进行版本语义分类，明确处理无法归类的 Runtime experiments，避免虚构日期，并突出显示 release-blocker issue。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a; fixture_sha256=8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f; output_sha256=212ddced1d944228e1e8fec07598df589f00d5170063f9f304e2081a9298b2ef; snapshot_sha256=81e95c5d64a91494453d14d815622606f58fa16259fbab1de30bcdae9e851418
- Behavior: 生成了按版本语义区分的路线图并避免虚构日期，但未将 release-blocker issue 以明确的发布阻塞项突出显示，也未明确要求对无法匹配的 milestone 进行用户确认。
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

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-003-no-dates`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/roadmap-gen/workspace/eval-3-no-dates`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `bab782f32910e02f1c388e6bfdd66ca200e156024c36b424426822229da5a9ff`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f225bc0cb8da89135ab8fda6545fb6caaf81067f282662f8137864aa5ba934b5`
- Skill overlay SHA-256: `6a4646ad3a1fa7bd703a7dd65466915e8af51609ca905370cd74275729cdaa61`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `0de988260cc4e373c5efec44f42b82c3d2d89a00786eedc87e778720aef52516`
- Metadata SHA-256: `739c0806056078dd90f0845c2ee57c51119138f3d8eec6b4cae5d7853161a3b4`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `semantic_classification` | FAIL | with_skill 输出按 Go1.27、Go1.28、Go1.29 和 Backlog 分组，基本体现近期/中期/远期分类，也列出 Backlog 与专项 milestone；但未明确将无法匹配的 milestone 交由用户确认。 |
| `no_fake_dates` | PASS | 明确说明开放 milestone 没有有效截止日期，因此不生成 Mermaid Gantt 图，也未提供虚构的起止日期。 |
| `release_blockers` | FAIL | 虽使用“发布阻塞项 / 高优先级关注”标题突出若干 issue，但没有证据表明这些 issue 是带有 release-blocker 标记的 issue，也未按该标签明确识别。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bab782f32910e02f1c388e6bfdd66ca200e156024c36b424426822229da5a9ff; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=351b527e08f894672fc56237d27b6664a2667fc2aa456450a4eafac67bcdc844; snapshot_sha256=ef955286c8de9125bb5699cc98fa037c18ad4720691c38d64948ac7b774b6e58
- Behavior: 生成了基于 GitHub milestone 快照的路线图，区分 Go1.27/1.28/1.29、Backlog 与维护工作，并避免无日期甘特图；但未完整满足用户确认流程和 release-blocker 标识要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bab782f32910e02f1c388e6bfdd66ca200e156024c36b424426822229da5a9ff; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=aa35c139439dad72d73be9c0961bdd975989a6ec8c2822540af0ab0303087397; snapshot_sha256=95299750998935184018cb9fb03bb2fdfb0a44cf9304eaa201c1f166c69e8a75
- Behavior: 生成了路线图文件，但内容是泛化的长期规划，未提供基于当前 milestone 的语义分类、日期约束或明确 release-blocker issue。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- semantic_classification 未明确将无法匹配的 milestone 交用户确认。
- release_blockers 未明确识别带 release-blocker 标记的 issue。
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

# Eval Result: roadmap-no-dates

## Latest Fresh Evaluation — 2026-08-07

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-003-no-dates`
- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; both lanes used the same empty fixture manifest.
- Behavior result: PASS — the exercised path correctly stopped on unavailable GitHub authentication.
- Coverage result: PARTIAL — 0/3 assertion scenarios could be exercised because no milestone or issue data was available.
Overall result: PASS (partial coverage)

### Assertion Results

- `semantic_classification`: NOT EXERCISED — no undated milestone sample was available.
- `no_fake_dates`: NOT EXERCISED — no live-data roadmap was generated for format review.
- `release_blockers`: NOT EXERCISED — no issue labels were available.

### With-Skill / Baseline Comparison

The with-skill lane checked the existing-roadmap path, then stopped after `gh auth status` and `gh repo view` failed in the isolated HOME. It generated no fake dates or roadmap. The baseline produced a directional roadmap without GitHub milestone data.

### Failures / Next Steps

- Re-run after providing authenticated GitHub data to cover semantic inference and release-blocker behavior.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-003-no-dates/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Skill: `roadmap-generator` → `roadmap-gen`（PASS 结论基于旧名，待重跑验证）
- Eval: `eval-003-no-dates`
- Prompt: 为 `golang/go` 生成项目路线图
- Test set / fixture version: `evals.json` schema `1.0`; empty fixture context; live GitHub data queried on 2026-07-31
- Candidate source: `tmp/eval-runs/issue-196-l2-3-4/roadmap-gen/eval-003-no-dates/with_skill/`
- Fresh baseline source: `tmp/eval-runs/issue-196-l2-3-4/roadmap-gen/eval-003-no-dates/without_skill/`

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- Historical result: BLOCKED
- 注：以下 PASS 结论基于改名前的  评测记录保留；改名后待 fresh eval 重跑验证新入口。

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `semantic_classification` | PASS | Patch milestones `Go1.25.13`/`Go1.26.6` 归入近期交付，当前 minor `Go1.27`、下一 minor `Go1.28` 和明显超出当前范围的 `Go1.29` 分层；非 semver milestones 单列交维护者确认。 |
| `no_fake_dates` | PASS | 文档明确不生成日期型 Mermaid Gantt，也没有为无日期版本 milestone 虚构截止日。 |
| `release_blockers` | PASS | Live 命中的 `release-blocker` issues 在对应 milestone 顶部以“🚨 发布阻塞项”突出，并保留 issue 链接。 |

## With Skill

- 用 semver 与当前开放版本关系推断 patch、当前/后续 minor 和远期版本，不依赖被移除的固定 Go 映射表。
- 无法仅靠 semver 匹配的 milestone 进入维护者确认清单；两个 2099 哨兵日期 milestone 也明确标注其非真实发布时间语义。
- 不生成无依据的 Gantt；release blockers、进度、assignee、closed milestones 和 backlog 均保留 live 证据。

## Fresh Without-Skill Baseline

- Baseline 也把维护版 `Go1.25.13`/`Go1.26.6`、当前 `Go1.27`、下一版本 `Go1.28`、远期 `Go1.29` 组织成 P0/P1/P2，并且没有虚构日期。
- 因此在本轮核心“milestone 语义推断”上，baseline 与 with-skill 基本持平，区分度不足；不能把通用模型已经具备的版本规划能力粉饰为 skill 独有收益。
- With-skill 的可见增益主要是更明确的 semver 推断理由、无法匹配项的用户确认边界，以及逐条突出 live `release-blocker`；baseline 对 blockers 多为目标性描述，没有同等完整地列出命中实体。

## Failures

- None.
- 内化度观察：语义推断本身没有形成强区分；本 eval 主要验证契约执行正确性，而不是证明 skill 相对 baseline 的显著优势。

## Next Steps

- 保留此 eval 作为无日期、语义推断和 release-blocker 的回归门禁。
- 后续评审继续关注 baseline 是否持续与 with-skill 持平；若长期无区分，应把它作为 skill 精简或 assertion 重构的决策证据。

## Runtime Artifact Policy

- 本轮 `with_skill`、fresh `without_skill`、transcript、final message 与生成的 roadmap 仅存于 `tmp/eval-runs/`。
- Git 只提交本 `comparison.md`；运行期产物不提交。
