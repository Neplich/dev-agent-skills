# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-001-timeline`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165` from `agents/product_manager/test/roadmap-gen/workspace/eval-1-timeline`.
- Fixture SHA-256: `1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165`
- Prompt SHA-256: `ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `74b972ac8dbd7706448e20025f6995b87c544e99309b65961f70d0e86a7bd191`
- Skill overlay SHA-256: `bddee41393bca0a60880eaa8d81044ec84f2c1d751e6af66c6178450b19850d3`
- Judge schema SHA-256: `c9231138562bec2ed562cf0d8c1ec94b96debb390ee547b6815473c326c64b09`
- Eval definition SHA-256: `d6df04c011109b2d27a14aaefa7802d9d9c0af801e4acce9ed37afdc4c26a731`
- Metadata SHA-256: `c374d15583cb501346d3285d30669c9dbaf58b19f95661d07d8aeac8332d8ba1`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `phase_classification` | PASS | with_skill 的 roadmap.md 将有截止日期的 3.36.0、3.37.0、4.0.0 分为当前冲刺、近期计划和远期规划，并单列已完成 3.35.0。 |
| `undated_semantic_inference` | PASS | with_skill 对无日期的 3.38.0 基于当前版本 3.35.0 和后续 minor 版本语义暂列远期规划并要求确认；对无法匹配语义的 Rendering research 标记待维护者分类，未归入未排期且未捏造日期。 |
| `roadmap_artifacts` | PASS | with_skill 的 roadmap.md 包含 Unicode 进度条、Mermaid gantt、issue 的开放/关闭状态，以及 milestone 和 issue 的 GitHub 链接。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63; fixture_sha256=1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165; output_sha256=5c560594e26c4cfa05c89d1dd1a03fe814daaa4a847be8d35ae99c4dee6fecb5; snapshot_sha256=f357b31aa25ac18efa1a0872e49b7df378c42f2b4d4f12a7a5f0c43ef68912ca
- Behavior: 生成了符合要求的 docs/roadmap.md，正确处理日期阶段、无日期 milestone 语义和路线图证据。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63; fixture_sha256=1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165; output_sha256=f04ab3dbbb0d7f991a69f21648697629dae6320d99df6faebb389c2dd0a4fdf8; snapshot_sha256=1a1a4dbeb71a699d27ff46ed6ccb182c04f7d80952b83691d17133022c9e057f
- Behavior: 也生成了路线图，但将无日期 milestone 直接标为未排期，未提供 Mermaid Gantt，且进度汇总与原始快照计数不一致。
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
- Eval: `eval-001-timeline`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165` from `agents/product_manager/test/roadmap-gen/workspace/eval-1-timeline`.
- Fixture SHA-256: `1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165`
- Prompt SHA-256: `ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `74b972ac8dbd7706448e20025f6995b87c544e99309b65961f70d0e86a7bd191`
- Skill overlay SHA-256: `bddee41393bca0a60880eaa8d81044ec84f2c1d751e6af66c6178450b19850d3`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d6df04c011109b2d27a14aaefa7802d9d9c0af801e4acce9ed37afdc4c26a731`
- Metadata SHA-256: `c374d15583cb501346d3285d30669c9dbaf58b19f95661d07d8aeac8332d8ba1`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `phase_classification` | PASS | with_skill 的 docs/roadmap.md 将 3.36.0（2026-08-20）列为“当前冲刺”、3.37.0（2026-10-15）列为“近期计划”、4.0.0（2026-12-20）列为“远期规划”，并保留已完成的 3.35.0。 |
| `undated_semantic_inference` | PASS | with_skill 将无日期的 3.38.0 依据当前 release 3.35.0 之后的 minor 版本语义归入近期计划且明确无日历承诺；将无法仅凭语义匹配的 Rendering research 列为待维护者确认，未捏造日期或归入未排期。 |
| `roadmap_artifacts` | PASS | with_skill 交付文件包含各 milestone 进度条、Mermaid Gantt、issue 的开放/关闭状态，以及 milestone、issue 和仓库的 GitHub 链接。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63; fixture_sha256=1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165; output_sha256=264ee5ae205b984cf2d30b885ee5263be09e05db49a7382e86afa2eef541590f; snapshot_sha256=96de21e7e552cfa5969bed7821fe15f9fa3a4b53fe3dca49aeae742d17b434b7
- Behavior: 交付 docs/roadmap.md，注明数据时点，并完整覆盖日期阶段、无日期 milestone 处理及路线图证据工件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63; fixture_sha256=1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165; output_sha256=d920e9f0d146e3e75e06459dc73b78506ea66467d0154eda67dc90bf48fd283b; snapshot_sha256=0a622f9fc43a73aae14a891a1a2b67930092bf0152caf35ea876570060838b9f
- Behavior: 交付了路线图文件，但其内容未满足无日期 milestone 的语义推断与待确认要求，且未提供可见的进度条和 Mermaid Gantt。
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
- Eval: `eval-001-timeline`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165` from `agents/product_manager/test/roadmap-gen/workspace/eval-1-timeline`.
- Fixture SHA-256: `1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165`
- Prompt SHA-256: `ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a12253d9a3d1d231837468fc266a18cbef8c731ab282a55d4d464a493ca02f11`
- Skill overlay SHA-256: `c50d53c79d2138148c86c2ddaa4ea3403b46c5d6a9d3d67baf48a5203cd6d0b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d6df04c011109b2d27a14aaefa7802d9d9c0af801e4acce9ed37afdc4c26a731`
- Metadata SHA-256: `c374d15583cb501346d3285d30669c9dbaf58b19f95661d07d8aeac8332d8ba1`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `phase_classification` | PASS | with_skill 文档将有截止日期的 3.36.0、3.37.0、4.0.0 分别归入“当前冲刺”“近期计划”“远期规划”，并保留已完成版本。 |
| `undated_semantic_inference` | PASS | 3.38.0 根据当前版本 3.35.0 与 minor 版本语义归入近期计划；Rendering research 因无法可靠匹配阶段而列入待维护者确认，未自动归入未排期且未捏造日期。 |
| `roadmap_artifacts` | PASS | 文档包含各 milestone 进度条、Mermaid Gantt、issue 的 open/closed 勾选状态，以及 milestone 和 issue 的 GitHub 链接。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63; fixture_sha256=1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165; output_sha256=8f44fd9e9d310416760ccd5d39256d2959a645d65f248eca7061ed475ee10d52; snapshot_sha256=690810c71bb7783f5efce2a26351b3a4d15326ae764ac0fda7a9ab7844612f54
- Behavior: 成功写入 docs/roadmap.md，注明数据时点，完成日期阶段分类、无日期 milestone 语义推断与待确认处理，并提供所需路线图证据。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63; fixture_sha256=1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165; output_sha256=fbb3449e45cfaa3d83fab45f72f2599375ce4ecaa6506455b845daceed86bd09; snapshot_sha256=62da80af99cede28bd8757a028a34f920bf8776727c34b5e89e2f0db40d0d0d4
- Behavior: 生成了路线图并注明数据时点，包含丰富的路线、issue 和风险内容；其未提供可核验的进度条、Mermaid Gantt，且未明确展示无日期 milestone 的用户确认流程。
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
- Eval: `eval-001-timeline`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165` from `agents/product_manager/test/roadmap-gen/workspace/eval-1-timeline`.
- Fixture SHA-256: `1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165`
- Prompt SHA-256: `ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a12253d9a3d1d231837468fc266a18cbef8c731ab282a55d4d464a493ca02f11`
- Skill overlay SHA-256: `c50d53c79d2138148c86c2ddaa4ea3403b46c5d6a9d3d67baf48a5203cd6d0b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d6df04c011109b2d27a14aaefa7802d9d9c0af801e4acce9ed37afdc4c26a731`
- Metadata SHA-256: `c374d15583cb501346d3285d30669c9dbaf58b19f95661d07d8aeac8332d8ba1`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `phase_classification` | PASS | with_skill 文档将有截止日期的 3.36.0、3.37.0、4.0.0 分别归入当前冲刺、近期计划、远期规划，并保留截止日期。 |
| `undated_semantic_inference` | PASS | with_skill 按版本语义将无日期的 3.38.0 归入远期规划；将无法按版本语义推断的 Rendering research 单列并请求维护者确认，未捏造日期或自动归入未排期。 |
| `roadmap_artifacts` | PASS | with_skill 输出包含各里程碑进度条、Mermaid Gantt、Issue 的 open/closed 状态及 GitHub milestone/issue 链接。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63; fixture_sha256=1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165; output_sha256=343c54551c97283bc808cecb08e763f73249c327d55ec8b5be31cf8366c7bcc1; snapshot_sha256=aede57ebfeae0c97df17501a0db394d438d0a1693b5bae6fb5ae51307a737d2b
- Behavior: 生成 docs/roadmap.md，正确完成日期阶段分类、无日期 milestone 的语义推断与确认分流，并包含要求的路线图证据。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63; fixture_sha256=1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165; output_sha256=823a074b4ad1cc83f1d78b2975e2cf5cfdb230215e1dc87dc671225c1b8fe948; snapshot_sha256=70eee936628af919b06dbcac116fd7db0da58b83b6f2759e34eecc624b13fc7c
- Behavior: 生成了包含路线、Issue 状态、风险和链接的路线图，但未按要求明确展示无日期 milestone 的确认流程；未提供 Mermaid Gantt。
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
- Eval: `eval-001-timeline`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165` from `agents/product_manager/test/roadmap-gen/workspace/eval-1-timeline`.
- Fixture SHA-256: `1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165`
- Prompt SHA-256: `ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2b8eaa887e0089b78c69e8bf72f0824676518d33b5c372709e901a79190cd61b`
- Skill overlay SHA-256: `61c47c3293a0a8c5746d4b748abf3c5e11689bfbf0a0493a9b3beca73cbb7663`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d6df04c011109b2d27a14aaefa7802d9d9c0af801e4acce9ed37afdc4c26a731`
- Metadata SHA-256: `c374d15583cb501346d3285d30669c9dbaf58b19f95661d07d8aeac8332d8ba1`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `phase_classification` | PASS | with_skill 将有截止日期的 3.36.0、3.37.0、4.0.0 分别归入当前冲刺、近期计划和远期规划，并保留已完成的 3.35.0。 |
| `undated_semantic_inference` | PASS | with_skill 基于当前版本 3.35.0 和 minor 版本语义将无日期的 3.38.0 暂列近期计划；将无法可靠映射的 Rendering research 放入待维护者分类区，明确要求确认，未捏造日期或归入未排期。 |
| `roadmap_artifacts` | PASS | with_skill 输出包含各 milestone 进度条、Mermaid Gantt、issue 的勾选状态及 GitHub milestone/issue 链接。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63; fixture_sha256=1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165; output_sha256=4f59b033f4a614bd782c9b5b3e188646167c7c2412cbeea2ac11dde84702179e; snapshot_sha256=221841a8b4ec88d601b83beafb850a33c4b1c459b628e076b53f66fa86cbbf92
- Behavior: 按日期和版本语义完成阶段分类，显式处理无法分类的无日期 milestone，并保留进度、时间线、issue 状态和 GitHub 链接。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63; fixture_sha256=1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165; output_sha256=1d3503bfe8b419a7e346dbd8df7b248a81e0e583f62ec80ca030acff1424e42d; snapshot_sha256=7d4d6595c22a75e506c852373bc6b9b01150ce43cfcc7aa9ba0e42085b2a55ff
- Behavior: 生成了较完整的路线图并注明数据时点，包含 issue 和链接，但未提供要求的进度条及 Mermaid Gantt，也未按断言规则处理无日期 milestone。
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
- Eval: `eval-001-timeline`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/roadmap-gen/workspace/eval-1-timeline`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `468200f0078590343722139d5397a5381e11a254b11fd8f1f5d7276eda7575c7`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f225bc0cb8da89135ab8fda6545fb6caaf81067f282662f8137864aa5ba934b5`
- Skill overlay SHA-256: `6a4646ad3a1fa7bd703a7dd65466915e8af51609ca905370cd74275729cdaa61`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `cbeae06859c5325069790802206e50a82b5b23d446c019f5364c7f597eb8f474`
- Metadata SHA-256: `2881f972587a02ea67b4b7ffba2b31eb69fa71b4cf60d23781d8d9d383996c5a`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `phase_classification` | PASS | 证据显示所有开放 milestone 均无 due_on，未发现有截止日期的 milestone；输出未捏造日期。 |
| `undated_semantic_inference` | FAIL | 输出正确指出无法按 semver 推断阶段并请求维护者确认，但仍将这些 milestone 放入“未排期”区段，违反了不得自动归入未排期的要求。 |
| `roadmap_artifacts` | FAIL | 输出包含进度条、issue 状态和 GitHub 链接，但明确因无截止日期而不生成 Mermaid Gantt，缺少必需工件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=468200f0078590343722139d5397a5381e11a254b11fd8f1f5d7276eda7575c7; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=e6b544f8737d602714eb2f4ec5429155072f5e0ce8d0584779b0b21381596132; snapshot_sha256=f673eff5f537456013e5fafd947b7fef82b7d917b7e1b6bffa99729ad004a4d8
- Behavior: 基于 milestone、issue 和版本上下文整理了进度条、issue 状态及链接；识别无日期且非 semver 的 milestone 并请求确认，但将其置于未排期区段且省略 Mermaid Gantt。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=468200f0078590343722139d5397a5381e11a254b11fd8f1f5d7276eda7575c7; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=38031397ba38c47e007a6c2fe3ce04050d5b819938d3d82ff9576de10d0d651f; snapshot_sha256=3045c5dae12c123c781c79ea48b3d52accb7d146ee8b95db48385d98bdb093dc
- Behavior: 生成了主题化的规划路线图和官方链接，但未展示基于 milestone 的日期/语义分类证据，也未提供要求的结构化进度与 Gantt 工件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足无日期 milestone 不得自动归入未排期的约束。
- with_skill 缺少 Mermaid Gantt。
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

# Eval Result: roadmap-timeline

## Latest Fresh Evaluation — 2026-08-07

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-001-timeline`
- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; both lanes used the same empty fixture manifest.
- Behavior result: PASS — the exercised path correctly stopped on unavailable GitHub authentication.
- Coverage result: PARTIAL — 0/3 assertion scenarios could be exercised because no milestone/issue data was available.
Overall result: PASS (partial coverage)

### Assertion Results

- `phase_classification`: NOT EXERCISED — no milestone data was available.
- `undated_semantic_inference`: NOT EXERCISED — no undated milestones were available.
- `roadmap_artifacts`: NOT EXERCISED — no live-data roadmap could be generated.

### With-Skill / Baseline Comparison

The trace first checked for an existing roadmap, then `gh auth status` and `gh repo view` failed in the intentionally isolated HOME. The with-skill lane surfaced the authentication blocker and wrote no synthetic roadmap. The baseline wrote a roadmap, but it is comparison evidence only.

### Failures / Next Steps

- Re-run with a separately authorized GitHub fixture or authenticated isolated `gh` context; do not reuse historical live data.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-001-timeline/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Skill: `roadmap-generator` → `roadmap-gen`（PASS 结论基于旧名，待重跑验证）
- Eval: `eval-001-timeline`
- Prompt: 为 `flutter/flutter` 生成完整项目路线图
- Test set / fixture version: `evals.json` schema `1.0`; empty fixture context; live GitHub data queried on 2026-07-31
- Candidate source: `tmp/eval-runs/issue-196-l2-3-4/roadmap-gen/eval-001-timeline/with_skill/`
- Fresh baseline source: `tmp/eval-runs/issue-196-l2-3-4/roadmap-gen/eval-001-timeline/without_skill/`

## Latest Result

- Behavior result: **PASS**
- Coverage result: **PARTIAL**
- Historical result: BLOCKED
- 注：以下 PASS 结论基于改名前的  评测记录保留；改名后待 fresh eval 重跑验证新入口。

未覆盖场景：

- `phase_classification` 的 90 天以上 open dated milestone 分支未触发；live 数据只有逾期/30 天内与 31–90 天 milestone。
- `undated_semantic_inference` 的“无日期 milestone 可按 semver 匹配”分支未触发；6 个无日期 open milestone 都是非 semver 名称。无法匹配后列出并交用户确认的分支已触发。

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `phase_classification` | PASS | Q2/Q3 cutoff 按逾期或 30 天内归入当前冲刺，Q4 cutoff 按 31–90 天归入近期计划；没有捏造远期 milestone。 |
| `undated_semantic_inference` | PASS | 6 个非 semver、无日期 milestone 单列为“需维护者确认阶段”，没有自动归入“未排期”或虚构日期。 |
| `roadmap_artifacts` | PASS | 输出含 16 字符进度条、dated milestone Mermaid Gantt、issue checkbox 与 GitHub 链接。 |

## With Skill

- 严格用 `due_on` 分类有日期 milestone，并对无日期 milestone 进入语义推断路径。
- 对无法可靠匹配 semver 的 6 个 milestone 保留证据、逐项提出确认问题，没有使用固定“未排期”兜底。
- Backlog 截断为 20 条并保留总数；空 milestone、无 assignee、最近关闭 milestone 和未触发场景均显式说明。

## Fresh Without-Skill Baseline

- 同样正确处理了 dated milestone、进度、issue 链接和 Mermaid Gantt，基础路线图质量与 with-skill 接近。
- 但把 6 个无日期工程 milestone 直接归入“⚪ 未排期工程主题”，没有先按版本语义尝试匹配并把无法匹配项交用户确认，不满足新契约。
- Milestone 语义推断的区分度在本样本上主要来自“未匹配处理”：with-skill 遵守确认边界，baseline 使用了固定未排期兜底。由于 live 数据没有可匹配的无日期 semver milestone，本轮不能证明两者在成功语义匹配分支上的差异。

## Failures

- Behavior failure: none.
- Coverage gap: 90 天以上 dated milestone 与可匹配的无日期 semver milestone 均未出现。

## Next Steps

- 保留此 eval，后续 live 数据出现可匹配的无日期 semver milestone 时再观察成功推断分支。
- 不为补齐 coverage 人工制造 GitHub milestone 或日期。

## Runtime Artifact Policy

- 本轮 `with_skill`、fresh `without_skill`、transcript、final message 与生成的 roadmap 仅存于 `tmp/eval-runs/`。
- Git 只提交本 `comparison.md`；运行期产物不提交。
