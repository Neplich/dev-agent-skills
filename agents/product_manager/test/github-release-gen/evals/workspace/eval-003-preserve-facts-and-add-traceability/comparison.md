# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-003-preserve-facts-and-add-traceability`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-003-preserve-facts-and-add-traceability`.
- Fixture SHA-256: `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17`
- Prompt SHA-256: `1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f95690411417d5e9cf66495e67ce2d96d0a51fc4ca1821536421129a950bb8f3`
- Skill overlay SHA-256: `ee4b811662f5234e9cbcc50a85629526ebcf704244484e48f81d5ce85841d93c`
- Judge schema SHA-256: `13218ab4a7abff52fb220f782ffa27173bde4d7c9a5b1ae26ef3115112e26b3d`
- Eval definition SHA-256: `95f3370a6690706f871a83ed16fd2ea4af289f136e5af47351107d1ec6c06fc2`
- Metadata SHA-256: `9e52b1a05d9dc7bd3856fe83df9035077725f4a4387447107b2ae09c5bfbb539`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_confirmed_release_facts` | FAIL | with_skill 保留了文件卡片、失败消息重试、统一附件模型、nullable JSONB 迁移风险、部署顺序与开关、双架构资产、升级说明和旧浏览器限制，但正文新增了证据未确认的发布日期“2026-08-09”。 |
| `adds_verified_traceability_links` | FAIL | with_skill 使用了代表性 PR、commit 和最终 compare 链接，但未提供 github-evidence.md 中的贡献者链接。 |
| `curates_instead_of_dumping` | PASS | with_skill 围绕版本事实组织说明，仅列出代表性 PR/commit，并明确未粘贴 18 个维护 commit feed。 |
| `blocks_on_fact_conflict` | NOT_EXERCISED | 锁定证据未包含 GitHub 与站内事实的冲突，因此该阻塞分支未被实际触发，无法证明其是否会返回 docs-agent:release-notes-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=4b2899973f574f8ae6d359a2ee4b152511a14d01a917a147aa63b4901f9c5659; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了不执行 GitHub 写入的 Release 预览，并正确等待 tag 与发布确认；但预览含未经证实的日期且缺少贡献者链接。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=29d0179f8a9c62a86efe8306a371440a38587056aa581a19151ed62c7117eac8; snapshot_sha256=1ea865ec9c72220b04727c251c9040170fb92274b4f400bf8fef43b4ef335f15
- Behavior: 生成了文件型 Release 预览，覆盖主要事实并包含贡献者链接，但 compare 链接出现旧目标提交与最终 tag 的不一致。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 新增了未由锁定证据确认的发布日期。
- with_skill 缺少贡献者链接。
- Next: 移除未经证据确认的发布日期。
- Next: 为代表性 PR/commit 补充对应贡献者链接。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-003-preserve-facts-and-add-traceability`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-003-preserve-facts-and-add-traceability`.
- Fixture SHA-256: `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17`
- Prompt SHA-256: `1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `380b2fcfd0ff29b900d02472045d511ad62a16c847b128cbfdce8af3c7a60338`
- Skill overlay SHA-256: `c666691beb368144f31c0354fd118ef20d664151476cfb1c8695e6ee7c490aa7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `95f3370a6690706f871a83ed16fd2ea4af289f136e5af47351107d1ec6c06fc2`
- Metadata SHA-256: `9e52b1a05d9dc7bd3856fe83df9035077725f4a4387447107b2ae09c5bfbb539`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_confirmed_release_facts` | PASS | with_skill 的预览正文保留了文件卡片、失败消息原位重试、统一附件模型与旧文本兼容、nullable JSONB 迁移及删列风险、部署顺序与开关、amd64/arm64 资产、升级步骤和旧浏览器限制；未发现与 fixture 事实冲突的改写。 |
| `adds_verified_traceability_links` | PASS | 正文包含 PR #116、PR #117、commit 8b6a1f2 及 @alice/@bob/@carol 链接，并包含 github-evidence.md 中的完整 compare 链接 v0.9.0...v1.0.0；目标 tag 与 compare endpoint 一致。 |
| `curates_instead_of_dumping` | PASS | 正文围绕已确认的用户功能、架构、数据库、部署和升级事实组织，仅选择代表性 PR/commit 链接，明确未展开完整维护 feed。 |
| `blocks_on_fact_conflict` | NOT_EXERCISED | 原始 GitHub 证据未显示与站内事实冲突或新的用户版本事实，因此条件性冲突阻塞分支未被锁定证据实际触发。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=f3bb32c8a2ae1fe950fe753e7358215f7782e6dd39382b57e42fa3f4df8b41fd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了仅预览的 Release 内容、版本与 compare 证据、精选维护链接及明确的 tag 缺失阻塞；未创建或修改工作区文件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=2249419138996917cf0986b8dfefe755683d0f161d17ebea48f183f22919cc96; snapshot_sha256=178b92b4e10a673f0ef5ad62acfd85f49945a20d9708e793291f77a993a22142
- Behavior: 生成了可交付的 GitHub Release 预览文件，包含主要事实和精选链接，但使用 pre-tag target ref 作为 compare endpoint，且未呈现门禁与后续 tag 阻塞状态。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 创建 v1.0.0 tag 后重新读取 tag、release_verified 和 latest Release 证据，再进行 draft/publish 前复核。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-003-preserve-facts-and-add-traceability`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-003-preserve-facts-and-add-traceability`.
- Fixture SHA-256: `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17`
- Prompt SHA-256: `1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bfa553ee1e9614c42bec50e00faa33ed1a614260acdb1011ab1116e8b73db2dd`
- Skill overlay SHA-256: `0db0717c5ca83fddc3ecdfe8bf130c8885c13a22148bb9bf0d8e93c491b17294`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `95f3370a6690706f871a83ed16fd2ea4af289f136e5af47351107d1ec6c06fc2`
- Metadata SHA-256: `9e52b1a05d9dc7bd3856fe83df9035077725f4a4387447107b2ae09c5bfbb539`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_confirmed_release_facts` | PASS | with_skill 保留了文件卡片、原位重试、统一附件模型、nullable JSONB 迁移及删列风险、部署顺序与开关、双架构资产、升级步骤和旧浏览器限制。 |
| `adds_verified_traceability_links` | PASS | 使用了 PR #116、PR #117、commit 8b6a1f2 及对应贡献者链接，并提供了与 v1.0.0 标签一致的完整 compare 链接。 |
| `curates_instead_of_dumping` | PASS | 正文围绕已确认版本事实组织，仅选取代表性 PR/commit，并明确未粘贴其余 18 个无关维护 commit。 |
| `blocks_on_fact_conflict` | NOT_EXERCISED | 原始证据未显示 GitHub 证据与站内事实冲突或暴露新事实，无法检验冲突阻塞行为。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=f255de6073693548cf65f4e7ae3de8f1350a9dce198e0e6ba94d040b70bc5f29; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成仅预览、不发布的 Release 内容，完整保留站内事实，补充精选维护链接并明确过滤非支持性 feed。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=bcb90c3e5d29c194ad8330b3c025b19ba3b351e321ee3704b912c5ace8918388; snapshot_sha256=2415e4dbfdba408672e14d4673714868c0eeadec47d194ea319fb747a5e7a94b
- Behavior: 生成了包含主要事实和精选链接的预览，但未展示冲突阻塞决策。
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
- Skill: `github-release-gen`
- Eval: `eval-003-preserve-facts-and-add-traceability`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-003-preserve-facts-and-add-traceability`.
- Fixture SHA-256: `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17`
- Prompt SHA-256: `1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bfa553ee1e9614c42bec50e00faa33ed1a614260acdb1011ab1116e8b73db2dd`
- Skill overlay SHA-256: `0db0717c5ca83fddc3ecdfe8bf130c8885c13a22148bb9bf0d8e93c491b17294`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `95f3370a6690706f871a83ed16fd2ea4af289f136e5af47351107d1ec6c06fc2`
- Metadata SHA-256: `9e52b1a05d9dc7bd3856fe83df9035077725f4a4387447107b2ae09c5bfbb539`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_confirmed_release_facts` | PASS | with_skill 保留文件卡片、失败消息原位重试、统一附件模型、nullable JSONB 迁移与删列风险、部署顺序、功能开关、双架构资产、升级要求及旧浏览器限制。 |
| `adds_verified_traceability_links` | PASS | with_skill 提供 compare 链接、PR #116/#117、commit 8b6a1f2 及对应贡献者链接，并说明当前提交 compare 与目标 tag 建立前后的 endpoint。 |
| `curates_instead_of_dumping` | PASS | with_skill 按用户功能、架构、升级等主题组织内容，仅列代表性 PR/commit；未粘贴完整维护 feed。 |
| `blocks_on_fact_conflict` | NOT_EXERCISED | 原始证据未提供 GitHub 与站内事实冲突或新事实，因此无法验证冲突时是否阻塞并返回 docs-agent:release-notes-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=0ad189020e3cc5dbea8da0acf768625e7d389fdf9d7b21b7a6caab895459dfe0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 准备了只读 GitHub Release 预览，完整整理已确认发布事实，提供精选可追溯链接，并保留创建 tag 和复核 latest 的后续门禁。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=a9e85d8d5fa895f09e7a67cdf2fb77637926599a4bc1cfcb301f4e991316f0c3; snapshot_sha256=e021284596c3f70d88447729f65e7db596fcf1c9a487c8aff2894035aa172f6c
- Behavior: 生成了预览文件并提供精选链接，未执行 GitHub 发布；仅作基线对照。
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
- Skill: `github-release-gen`
- Eval: `eval-003-preserve-facts-and-add-traceability`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-003-preserve-facts-and-add-traceability`.
- Fixture SHA-256: `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17`
- Prompt SHA-256: `1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `793cabc84dc1947c3d6386a1d060276eea2eb8b4e9de25fdd6c7b7a60fb82cb0`
- Skill overlay SHA-256: `ecc021af86f838c5c915ade1c1e1095fa203f789350af9aa701ad32bae876bb2`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `95f3370a6690706f871a83ed16fd2ea4af289f136e5af47351107d1ec6c06fc2`
- Metadata SHA-256: `9e52b1a05d9dc7bd3856fe83df9035077725f4a4387447107b2ae09c5bfbb539`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_confirmed_release_facts` | PASS | with_skill 保留了文件卡片、原位重试、统一附件模型、迁移与删列风险、部署顺序和开关、双架构资产、升级步骤及旧浏览器限制。 |
| `adds_verified_traceability_links` | PASS | 使用了 v0.9.0...v1.0.0 完整 compare 链接、PR #116/#117、commit 8b6a1f2 及 alice、bob、carol 贡献者链接。 |
| `curates_instead_of_dumping` | PASS | 正文按用户可读主题组织，仅列出支持版本事实的代表性 PR 和 commit，明确未展开 18 个维护类 commit。 |
| `blocks_on_fact_conflict` | NOT_EXERCISED | raw evidence 未发现 GitHub 证据与站内事实冲突或暴露新事实，因此未触发阻塞路径。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=f0a42a4a3dc61d84f1ec2ef4cf06b6bb3112607bd9e1593f30ef5f1b230cb5f8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了只读、可审阅的 Release 预览，保留事实、补充维护链接并明确未执行 GitHub 写操作。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=805ffee074c4b87979a087f7e117d4ca64d18145d68a8865dfd6228f05a58329; snapshot_sha256=8b544923abb46675c52dce4d676a65d9093448e74eae0d11f72631d1a64642f9
- Behavior: 创建了 GitHub Release 预览文件，覆盖主要事实和链接，但未展示冲突阻塞协议。
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
- Skill: `github-release-gen`
- Eval: `eval-003-preserve-facts-and-add-traceability`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-003-preserve-facts-and-add-traceability`.
- Fixture SHA-256: `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17`
- Prompt SHA-256: `1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ebd2c00966a7932d251daeeef05573b0145183fe908cf102225636115f85820c`
- Skill overlay SHA-256: `2398a04c1c550bc8e45aa1564f5f42f6e629a29d1c1ed530494ae269f918d169`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `95f3370a6690706f871a83ed16fd2ea4af289f136e5af47351107d1ec6c06fc2`
- Metadata SHA-256: `9e52b1a05d9dc7bd3856fe83df9035077725f4a4387447107b2ae09c5bfbb539`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_confirmed_release_facts` | PASS | with_skill 正确保留了站内确认的用户功能、架构兼容、数据库迁移风险、部署顺序与开关、双架构资产、升级流程及旧浏览器限制。 |
| `adds_verified_traceability_links` | PASS | 包含与目标标签一致的 v0.9.0...v1.0.0 compare 链接、PR #116/#117、commit 8b6a1f2，以及对应贡献者链接；这些链接均有 github-evidence.md 支持。 |
| `curates_instead_of_dumping` | PASS | 正文围绕发布事实组织，仅引用两个代表性 PR 和一个代表性 commit，没有粘贴 18 个维护 commit 的完整 feed。 |
| `blocks_on_fact_conflict` | FAIL | with_skill 说明缺少 Latest Release 证据，但没有说明 GitHub 证据与站内事实冲突或暴露新事实时应阻塞，并返回 docs-agent:release-notes-gen 重新确认。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=4f887f6a63d8b01aa7aa70b49621823f9f68f0d639f605699aa32e79199eed89; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 以预览形式组织发布说明，保留确认事实并提供经过筛选的追踪链接；对 Latest 证据不足进行了提示，但未满足冲突阻塞要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=9ee56686ab5f68b362ca342de0f5fc08b50e5b255b7765f1ca5bc88a31b4555e; snapshot_sha256=7c8928f61c428678fffe56a1f48fcdfef3676063ac1e7c0db9e39bba5d7d9d3d
- Behavior: 生成了完整的 GitHub Release 预览文件，保留主要发布事实并加入维护链接，但未提供冲突阻塞流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足冲突不自行覆盖且返回 docs-agent:release-notes-gen 重新确认的要求。
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

# Eval Result: eval-003-preserve-facts-and-add-traceability

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-003-preserve-facts-and-add-traceability`
- Test case: `事实一致与可追溯增强`
- Prompt:

> 请根据 `release-package.md`、`docs/site/release-notes/v1.0.0.md` 和 `github-evidence.md` 准备 GitHub Release 预览。

- Expected output:

> 预览逐项保持已确认的功能、架构、数据库、部署、资产、升级与风险事实，补充可信 compare、代表性 PR/commit 和贡献者链接，不把原始维护列表当成用户说明。

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `48f64768ed5b5a87211bb5aee4d2a82f88fd01187214112795689e47210e9e9c`（3 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **PARTIAL**
- Overall result: PASS (partial coverage)
- With-skill summary: with_skill 实际加载 github-release-gen（status skill_load_hits=2；transcript item_1 读取 SKILL.md），按技能要求先读取参考规范再读取三份事实材料，未写入工作区，并生成保留事实、精选链接和最终 compare 链接的预览。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载 github-release-gen（status skill_load_hits=2；transcript item_1 读取 SKILL.md），按技能要求先读取参考规范再读取三份事实材料，未写入工作区，并生成保留事实、精选链接和最终 compare 链接的预览。

## Without-Skill Baseline

without_skill 未加载技能（skill_load_hits=0），但也生成了包含主要事实和维护链接的预览文件；仅作对照。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `preserves_confirmed_release_facts` | **PASS** | with_skill candidate 明确保留文件卡片、失败消息原位重试及其独立性、统一附件模型与旧文本兼容、nullable JSONB message_files 与回填/NOT NULL 约束、删除列丢失元数据风险、数据库→Gateway→Web 部署顺序、生产开关、amd64/arm64 资产、升级验证、备份和旧浏览器限制；transcript item_3 读取了三份事实材料，且 before/after 快照显示事实源未被修改。 | without_skill 生成的预览也包含上述主要事实。 |
| `adds_verified_traceability_links` | **PASS** | candidate 使用了 github-evidence.md 中的 PR #116、PR #117、commit 8b6a1f2 及对应贡献者链接，并给出完整 compare https://github.com/example/ai-hub/compare/v0.9.0...v1.0.0；该 endpoint 与目标 tag v1.0.0 一致。transcript item_3 读取 github-evidence.md，item_8 输出了这些链接。 | without_skill 预览文件同样包含 compare、两个 PR、direct commit 和贡献者链接。 |
| `curates_instead_of_dumping` | **PASS** | candidate 将维护链接放在重点更新、其他改进和变更明细中，只列三条代表性变更，并明确说明 18 个格式化、依赖更新和测试 commit 未原样放入正文；与 fixture 中“不得原样堆入正文”一致。 | without_skill 也排除了完整的 18 个维护性 commit feed。 |
| `blocks_on_fact_conflict` | **NOT EXERCISED** | fixture 中 github-evidence.md 仅提供与事实源相容的代表性链接和 release window，没有触发 GitHub 证据冲突或暴露新事实的条件；因此未能从实际行为判定阻塞并返回 docs-agent:release-notes-gen 的分支。 | without_skill 同样未遇到事实冲突，未触发该条件。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- blocks_on_fact_conflict：当前 fixture 没有冲突或新增事实，条件分支未触发。

## Next Steps

- 如需 FULL coverage，补充会与站内事实冲突或 materially extend 的 GitHub 证据 fixture。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `80.97s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `62.622s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `81.651s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
