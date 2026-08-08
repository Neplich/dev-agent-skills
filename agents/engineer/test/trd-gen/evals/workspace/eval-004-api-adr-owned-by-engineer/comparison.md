# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-004-api-adr-owned-by-engineer`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116` from `agents/engineer/test/trd-gen/evals/workspace/eval-004-api-adr-owned-by-engineer`.
- Fixture SHA-256: `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116`
- Prompt SHA-256: `825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `73cec46ef0287c25bd7a41d37b6bcee4e1ea25b1101672fb45bd299ecec77b0d`
- Skill overlay SHA-256: `8f09b52303d9393824dd3e732e656dd74f7ac606a082939547181274986dfb2d`
- Judge schema SHA-256: `2fb0119eb77903cfe9db053e59a3c85f9fb841609febdeb77953e7bac06ea0fe`
- Eval definition SHA-256: `c2e125b845f0cfd23a8b77d0953e79c0dfdb8a47bc09cbe45bf84d70fdf9a2db`
- Metadata SHA-256: `d32be481f3b029c028aa82a9a8adf92bda8ff5084062b1a65511dd3d764980a1`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `engineer_owns_api_and_adr` | FAIL | The Engineer documents contain `generated_by: "trd-gen"`, but neither the locked output nor file content states that API and ADR are owned by `engineer-agent:trd-gen`; the output instead says the main flow completed them because the Engineer document subagent was unavailable. |
| `writes_all_engineer_docs_under_feature_path` | PASS | The delivery snapshot contains TRD.md, API.md, and ADR-001-search-index.md under `docs/engineer/chat-interface/history-search/`. |
| `preserves_related_prd_and_metadata` | PASS | All three Engineer documents contain the required feature_path, parent_feature, feature_level, and related_prd metadata pointing to the PM PRD. |
| `does_not_use_pm_generators` | PASS | The with_skill output and snapshots contain no routing to `api-gen` or `adr-gen`; generation is identified as `trd-gen`. |
| `no_plan_or_code` | PASS | Git evidence shows only untracked Engineer documentation files, with no implementation plan or code changes. The TRD explicitly states this stage does not implement code or create an implementation plan; its testing strategy is documentation, not added tests. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=3387cb020b5b9be1f2f66d7d9986ff3330b00b08e8f6e2fa8586afa284e35982; snapshot_sha256=059d708749478013d2ffddd270bf392ac6a626da8b42e1b596589a69a634be08
- Behavior: Created the requested Engineer TRD, API, and ADR under the correct feature path, preserved metadata and PRD linkage, and avoided implementation changes; however, it did not satisfy the required explicit Engineer-agent ownership statement.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=0084f26d0297f8d5c6904ac679e7c5dba0fc665e3252806fdeeb1a10332b50de; snapshot_sha256=5888f3412bbabee943d80b4f3e8c0f9493df2b994bc343120ed0781e4bfa43c7
- Behavior: Created technical, API, and ADR files under the PM path, providing a fresh baseline that misplaced Engineer artifacts and did not demonstrate the required Engineer ownership routing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane does not establish the required `engineer-agent:trd-gen` ownership for the API and ADR, and explicitly says the main flow completed the work because the Engineer document subagent was unavailable.
- Next: Route or explicitly identify API and ADR generation as owned by `engineer-agent:trd-gen`.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-004-api-adr-owned-by-engineer`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116` from `agents/engineer/test/trd-gen/evals/workspace/eval-004-api-adr-owned-by-engineer`.
- Fixture SHA-256: `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116`
- Prompt SHA-256: `825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `73cec46ef0287c25bd7a41d37b6bcee4e1ea25b1101672fb45bd299ecec77b0d`
- Skill overlay SHA-256: `8f09b52303d9393824dd3e732e656dd74f7ac606a082939547181274986dfb2d`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `c2e125b845f0cfd23a8b77d0953e79c0dfdb8a47bc09cbe45bf84d70fdf9a2db`
- Metadata SHA-256: `d32be481f3b029c028aa82a9a8adf92bda8ff5084062b1a65511dd3d764980a1`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `engineer_owns_api_and_adr` | PASS | API.md and ADR-001 frontmatter both set generated_by to engineer-agent:trd-gen. |
| `writes_all_engineer_docs_under_feature_path` | PASS | Locked delivery evidence contains TRD.md, API.md, and ADR-001 under docs/engineer/chat-interface/history-search/. |
| `preserves_related_prd_and_metadata` | PASS | All three Engineer documents contain the required feature_path, parent_feature, feature_level, and related_prd metadata. |
| `does_not_use_pm_generators` | PASS | No PM api-gen or adr-gen routing appears; API and ADR are Engineer-generated. |
| `no_plan_or_code` | PASS | Git evidence shows only the three Engineer documentation files added; no implementation plan, code, or tests were delivered. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=da63b11697bdabd2153c0702826031ba5ed42055001d0102ea187ca63065a02b; snapshot_sha256=5122988d719f47bf6b80dfef37b085a370a1f2ef0252e46eebe50548ab708814
- Behavior: Delivered the required Engineer TRD, API, and ADR under the feature-mirrored path with metadata preserved and no implementation work.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=95daeaedbdf69012c02473d5da554f2d71f579094edc3355f272a5fe4d5b37fe; snapshot_sha256=1ef63c9a49c2aafec853be292b3b617cf6a9af70254c2b808384cffb1ae590bb
- Behavior: Created PM-path technical, API, and ADR documents and modified the PRD, without the required Engineer ownership/path metadata.
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
- Skill: `trd-gen`
- Eval: `eval-004-api-adr-owned-by-engineer`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116` from `agents/engineer/test/trd-gen/evals/workspace/eval-004-api-adr-owned-by-engineer`.
- Fixture SHA-256: `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116`
- Prompt SHA-256: `825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bb3f875298d7fef0fcd2297b4e59b33b5c034efad4a2286dcaede91ec0863c72`
- Skill overlay SHA-256: `12aaaef0d075d133bbbdc681f598fd09807b211a4377dcfbc6cbbfcaa30909e0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `c2e125b845f0cfd23a8b77d0953e79c0dfdb8a47bc09cbe45bf84d70fdf9a2db`
- Metadata SHA-256: `d32be481f3b029c028aa82a9a8adf92bda8ff5084062b1a65511dd3d764980a1`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `engineer_owns_api_and_adr` | FAIL | 文档位于 Engineer 路径且 metadata 标注 generated_by: trd-gen，但输出未明确说明由 engineer-agent:trd-gen 负责 API/ADR。 |
| `writes_all_engineer_docs_under_feature_path` | PASS | 锁定清单显示 TRD.md、API.md 和 ADR-001-postgresql-full-text-search.md 均位于 docs/engineer/chat-interface/history-search/。 |
| `preserves_related_prd_and_metadata` | FAIL | TRD.md 与 API.md 包含所需路径元数据和 related_prd；ADR 仅通过 related_docs 指向 PRD，缺少 required related_prd 字段。 |
| `does_not_use_pm_generators` | PASS | 锁定输出和文档未将 API/ADR 路由到 api-gen 或 adr-gen，且文档标注 generated_by: trd-gen。 |
| `no_plan_or_code` | PASS | git evidence 仅显示三个文档新增；输出明确说明未进入代码实现，未创建 IMPLEMENTATION_PLAN.md 或测试。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=11ae8428d99b8389367a395c4a255a62516741dc726eef0b4e5ea68f08cda2f8; snapshot_sha256=6229568ba1e0edf977926713c90d9e61cdda651a96d6381c44dd511b0b200195
- Behavior: 在 docs/engineer 对应 feature_path 生成 TRD、API 和 ADR，未进入代码实现，但遗漏了明确的 engineer-agent:trd-gen 责任说明及 ADR 的 related_prd 字段。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=fd2bdd8a3bc5a999df175eb28bb3f6878c0457888873c20290cc023fbf2290b3; snapshot_sha256=33bf8f5eab90bd47b3de0e8128ea156b31d63d7afec7435108226184ac2f7176
- Behavior: 在 docs/pm 路径生成技术方案、API 和 ADR，未满足 Engineer 产物路径要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确说明 API 和 ADR 由 engineer-agent:trd-gen 负责。
- ADR 文档缺少 related_prd 字段。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-004-api-adr-owned-by-engineer`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116` from `agents/engineer/test/trd-gen/evals/workspace/eval-004-api-adr-owned-by-engineer`.
- Fixture SHA-256: `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116`
- Prompt SHA-256: `825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bb3f875298d7fef0fcd2297b4e59b33b5c034efad4a2286dcaede91ec0863c72`
- Skill overlay SHA-256: `12aaaef0d075d133bbbdc681f598fd09807b211a4377dcfbc6cbbfcaa30909e0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `c2e125b845f0cfd23a8b77d0953e79c0dfdb8a47bc09cbe45bf84d70fdf9a2db`
- Metadata SHA-256: `d32be481f3b029c028aa82a9a8adf92bda8ff5084062b1a65511dd3d764980a1`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `engineer_owns_api_and_adr` | FAIL | with_skill 输出说明已补齐 Engineer 文档，但未说明 API 和 ADR 由 `engineer-agent:trd-gen` 负责，也未明确排除 PM 内部生成器。 |
| `writes_all_engineer_docs_under_feature_path` | PASS | 输出及 delivery_snapshot 均显示目标路径为 docs/engineer/chat-interface/history-search/TRD.md、API.md 和 ADR-001-search-index.md。 |
| `preserves_related_prd_and_metadata` | PASS | 三份 Engineer 文档 frontmatter 均包含 feature_path: chat-interface/history-search、parent_feature: chat-interface、feature_level: 2，并将 related_prd 指向 docs/pm/chat-interface/history-search/PRD.md。 |
| `does_not_use_pm_generators` | PASS | with_skill 输出和文档未将 API 或 ADR 路由到 PM 内部 api-gen 或 adr-gen。 |
| `no_plan_or_code` | PASS | git evidence 仅显示三份 Engineer 文档新增；输出明确说明未修改业务代码，未创建 IMPLEMENTATION_PLAN.md 或测试交付物。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=6533489d95d8ce6aa07b6808c619bc62a2d7be23833e67eda9f656b7af640bd1; snapshot_sha256=b30ac27fe53bccde12fa3c5d14ee26802988ddfbe31a154fc598c6769416982b
- Behavior: 正确生成 Engineer 路径下的 TRD、API 和 ADR，保留路径元数据及 PRD 关联，并未修改代码；但未明确说明 engineer-agent:trd-gen 负责 API/ADR。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=5e7f0873ce51fa99c9dc29a803e9281d1cd364f4de4185439943d2045c487ba1; snapshot_sha256=7c64add107c578ad5842a7a71f5fc73e8fe26ae3eb144020e12e85f7bd2a2b49
- Behavior: 生成了错误位于 PM 路径下的技术方案、API 和 ADR，未体现 Engineer 产物归属。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- engineer_owns_api_and_adr 未满足：缺少 API/ADR 由 `engineer-agent:trd-gen` 负责的用户可见说明。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-004-api-adr-owned-by-engineer`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116` from `agents/engineer/test/trd-gen/evals/workspace/eval-004-api-adr-owned-by-engineer`.
- Fixture SHA-256: `7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116`
- Prompt SHA-256: `825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b66f9acea93e151819a21f82909f9a6b7d44c68fa52d2116667525e2fe8e9bd7`
- Skill overlay SHA-256: `e4cc003a0e06320ef354c6c9cdbebb2b75980ec8b23ae530ac78b0667fab31da`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `c2e125b845f0cfd23a8b77d0953e79c0dfdb8a47bc09cbe45bf84d70fdf9a2db`
- Metadata SHA-256: `d32be481f3b029c028aa82a9a8adf92bda8ff5084062b1a65511dd3d764980a1`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `engineer_owns_api_and_adr` | FAIL | With-skill output creates Engineer documents and marks `generated_by: "trd-gen"`, but neither the output nor document metadata identifies `engineer-agent:trd-gen` as the responsible owner. |
| `writes_all_engineer_docs_under_feature_path` | PASS | Locked with-skill status and delivery paths show TRD.md, API.md, and ADR-001-search-index-strategy.md under `docs/engineer/chat-interface/history-search/`. |
| `preserves_related_prd_and_metadata` | PASS | All three with-skill documents contain `feature_path: "chat-interface/history-search"`, `parent_feature: "chat-interface"`, `feature_level: "2"`, and `related_prd: "docs/pm/chat-interface/history-search/PRD.md"`. |
| `does_not_use_pm_generators` | PASS | With-skill output and document contents contain no routing to `api-gen` or `adr-gen`; all documents identify `trd-gen`. |
| `no_plan_or_code` | PASS | With-skill git status contains only the three Engineer documentation files; no implementation plan, source-code changes, or test files were created. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=04dedc5fe1ea6b8327dd76d02fa0d05ac5f448b7ca8cc218a0e1c48b61a15570; snapshot_sha256=55555b0e679ee3e7559451f4dde9c39ee05f63209d46735f33c6315f0fd829c3
- Behavior: Created three Engineer documents under the mirrored feature path with required metadata and no code changes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=825205d6124cce58172b3b6756f4b557e630d638b9032e293e0df1661f6c8e2b; fixture_sha256=7b6820d67dd73e9499a1ca84c463bfc82e890640eeaf8c3154b04834d8479116; output_sha256=d81b752e256f2dd0e16e51897fdbf7548bfca49bfea3ee9bf086461bf5501a1d; snapshot_sha256=1ea94e8bcce7c201417d67538f131ee6163fefaa3a1896c3b5e8cd6d79ae38aa
- Behavior: Created PM-path technical design, API, and ADR documents.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- engineer_owns_api_and_adr failed because the required explicit owner string `engineer-agent:trd-gen` is absent.
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

# Eval Result: eval-004-api-adr-owned-by-engineer

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-004-api-adr-owned-by-engineer`
- Test case: api-adr-owned-by-engineer
- Workspace: `workspace/eval-004-api-adr-owned-by-engineer`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: PM 已确认 docs/pm/chat-interface/history-search/PRD.md。请为聊天历史搜索补技术方案、API 文档和一份搜索索引选型 ADR。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `engineer_owns_api_and_adr`: workspace 中 API.md 与 ADR 确实写在 Engineer 路径；但 final.md 和 agent_message 未明确说明由 `engineer-agent:trd-gen` 负责、且不是 PM 内部生成器负责。
- PASS `writes_all_engineer_docs_under_feature_path`: file_change 记录及 workspace 均显示三份文件位于 `docs/engineer/chat-interface/history-search/`；final.md 也列出对应路径。
- PASS `preserves_related_prd_and_metadata`: TRD.md、API.md、ADR.md 的 frontmatter 均包含 `feature_path: chat-interface/history-search`、`parent_feature: chat-interface`、`feature_level: 2` 和 `related_prd: docs/pm/chat-interface/history-search/PRD.md`。
- PASS `does_not_use_pm_generators`: with_skill transcript 未记录调用 `api-gen` 或 `adr-gen`，file_change 仅新增 Engineer TRD/API/ADR 三份文档。
- PASS `no_plan_or_code`: with_skill workspace 未产生 IMPLEMENTATION_PLAN.md 或代码/测试文件；file_change 仅涉及三份 Engineer 文档，final.md 说明实现代码尚不存在。

## With Skill Behavior

三份 Engineer 文档已正确写入目标目录，frontmatter 和 hash 均与实际 workspace 内容一致；但最终输出未明确声明 API/ADR 的 `engineer-agent:trd-gen` 归属。exit_code 为 0。

## Without Skill Baseline

without_skill 生成了 PM 路径下的 TECHNICAL-SPEC.md、API.md 和 ADR，未满足 Engineer-owned 产物边界；仅作对照，不影响逐条判定。其记录的 hash 与 workspace 文件一致，exit_code 为 0。

## Failures / Findings

- engineer_owns_api_and_adr：缺少明确的 `engineer-agent:trd-gen` ownership 声明及对 PM 内部生成器的排除说明。
- Root cause: 实现产物和路径边界正确，但 final/transcript 的责任归属表述不完整，未提供该 assertion 要求的明确 ownership 证据。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-004-api-adr-owned-by-engineer

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-004-api-adr-owned-by-engineer`
- Test case: api-adr-owned-by-engineer
- Workspace: `workspace/eval-004-api-adr-owned-by-engineer`
- Evaluation date: 2026-07-26
- Latest result: PASS - 本轮由当前会话中同一个 fresh Codex subagent 按 no-answer-key 顺序重新生成并锁定 `with_skill` 与新的 `without_skill` baseline；fresh judge 判定 `with_skill` 满足 5/5 assertions，baseline 满足 3/5。skill 的增益体现在明确的 Engineer ownership、完整路径元数据与 `related_prd` 契约。
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture classification: (a) fixture 已经足够，只缺可信的 fresh baseline，不需要补文件。
- Fixture evidence: `docs/pm/chat-interface/history-search/PRD.md` 为 `status: Approved` 的嵌套 PRD，已提供 `feature_path: chat-interface/history-search`、`parent_feature: chat-interface`、`feature_level: 2`、API 上下文和搜索索引选型的决策上下文；`README.md` 明确要求 Engineer 文档集且不进入实现。
- 本轮没有修改 fixture、`eval_metadata.json`、skill 或 assertions。

## No-Answer-Key Fresh Pair Protocol

1. `with_skill` 生成前只读取 workspace `eval_metadata.json` 中的原 prompt、fixture `README.md`、Approved PRD，以及 `agents/engineer/README.md` 和 `agents/engineer/skills/trd-gen/SKILL.md`。
2. 在未读取 `evals.json`、expected output、assertions 或旧 `comparison.md` 的条件下生成并锁定 `with_skill` 候选。
3. 同一个 fresh Codex subagent 随后仅依据已经锁定的原 prompt、fixture `README.md` 和 Approved PRD 生成新的 `without_skill` baseline；此阶段明确不应用 Engineer Agent README 或 `trd-gen` SKILL，仍未读取 `evals.json`、expected output、assertions 或旧 comparison。
4. 两份候选锁定后，judge 才首次读取 `evals.json` assertions 和旧 comparison，逐项判定。

本轮不复用任何历史候选、baseline 或判断。

## With Skill

- Fresh run source: 当前会话中的 fresh Codex subagent 按上述隔离顺序生成并锁定；未复用历史输出。
- Entry gate: 识别 Approved PRD 已提供稳定 PM scope 与明确 `feature_path`，进入 Engineer TRD 阶段。
- Ownership: 明确 TRD、API 和 ADR 都是 `engineer-agent:trd-gen` 负责的 Engineer 产物，不路由到 PM 内部生成器。
- Paths: 列出 `docs/engineer/chat-interface/history-search/TRD.md`、`docs/engineer/chat-interface/history-search/API.md` 和 `docs/engineer/chat-interface/history-search/ADR-001-search-index-strategy.md`。
- Metadata: 要求三份 Engineer 文档一致保留 `feature_path: chat-interface/history-search`、`parent_feature: chat-interface`、`feature_level: 2`，并以 `related_prd: docs/pm/chat-interface/history-search/PRD.md` 追溯已批准 PRD。
- Boundary: 明确本阶段只处理 TRD、API 和 ADR，不创建 `IMPLEMENTATION_PLAN.md`，不编写代码；Engineer 文档确认后才移交 `feature-implementor`。

## Without Skill / Baseline

- Fresh baseline source: 同一个 fresh Codex subagent 在锁定 `with_skill` 后，只使用原 prompt、fixture `README.md` 和 Approved PRD；不应用 Engineer Agent README 或 `trd-gen` SKILL，且生成时仍未读取 `evals.json`、expected output、assertions 或旧 comparison。
- Baseline 独立推断出三个 `docs/engineer/chat-interface/history-search/` 目标路径，生成 TRD、API 和 Proposed ADR，并明确不进入实施计划或代码。
- Baseline 的三个文档 frontmatter 均保留 `feature_path`、`parent_feature` 和 `feature_level`，但未设置 `related_prd`。
- Baseline 没有把工作路由给 PM `api-gen` / `adr-gen`，但也没有明确声明 API / ADR 由 `engineer-agent:trd-gen` 负责。

## Assertion Results

| Assertion | With skill | Without skill | Fresh judge conclusion |
| --- | --- | --- | --- |
| `engineer_owns_api_and_adr` | PASS | FAIL | with-skill 明确声明 API / ADR 由 `engineer-agent:trd-gen` 负责且不路由至 PM 内部生成器；baseline 仅按一般任务生成文档，没有给出该角色归属契约。 |
| `writes_all_engineer_docs_under_feature_path` | PASS | PASS | 两者均给出 TRD、API 和 ADR 的 `docs/engineer/chat-interface/history-search/` 路径。 |
| `preserves_related_prd_and_metadata` | PASS | FAIL | with-skill 完整声明三项路径 metadata 与 `related_prd`；baseline 保留三项路径 metadata，但缺少 `related_prd: docs/pm/chat-interface/history-search/PRD.md`。 |
| `does_not_use_pm_generators` | PASS | PASS | 两者均未调用或路由至 PM `api-gen` / `adr-gen`。 |
| `no_plan_or_code` | PASS | PASS | 两者都明确停在 Engineer 文档阶段，没有进入实现计划、代码、测试或交付。 |

## Failures

- baseline 没有明确写出 `engineer-agent:trd-gen` 对 API / ADR 的 ownership。
- baseline 虽写出三项路径 metadata，但遗漏 `related_prd`。
- with-skill 没有 assertion failure；本轮可信 fresh pair 的结论是 with-skill 5/5、baseline 3/5。

## Risks

- Fixture 足以支持本 eval，不需要补造额外证据。
- Prompt 和 fixture 已直接给出 Engineer 阶段、三个文档类型及嵌套 PRD 路径，因此 baseline 也能通过路径和边界 assertions；本 eval 对 skill 增益的区分度有限。
- 本轮 PASS 依赖 skill 对 ownership 和完整文档元数据的明确约束；后续若这些契约变化，应重新执行同样隔离的 fresh pair。
- 本轮只更新 durable evidence，不修改 `trd-gen` 行为或放宽 assertions。

## Next Steps

- 保留本轮 PASS 作为当前可信 no-answer-key 结果；任何后续重跑仍须先锁定成对候选，再读取 assertions 进行判断。

## Runtime Artifacts Policy

- 本轮仅把 fresh judge 的持久结论汇总到此 canonical `comparison.md`。
- Runtime transcripts、candidate outputs、verdicts、timing、diagnostics 和其他运行期 outputs 不提交到 git。
