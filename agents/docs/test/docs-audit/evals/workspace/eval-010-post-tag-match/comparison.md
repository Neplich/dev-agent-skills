# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518` from `agents/docs/test/docs-audit/evals/workspace/eval-010-post-tag-match`.
- Fixture SHA-256: `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518`
- Prompt SHA-256: `47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `f64d4542aa97d4b9bcd4bc655a5e70fec7d827a5ea9e9f63067fde8d7b819748`
- Eval definition SHA-256: `f4b575228474dd8bb2a93bb17a067f25252f9c293e1f78393d445c449385e8d2`
- Metadata SHA-256: `12f75879efa3cacf943ae19595239a747563947015e4033eed4ea7f4a51a5b47`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_pre_tag_authority_safely` | NOT_EXERCISED | 锁定 git topology 证明当前仓库有该 custom ref、tag，且 fresh clone 未取得 custom ref；但没有 delivery_snapshot/git_blob 证据证明两边实际读取了 handoff/audit 并独立重建 authority。 |
| `proves_released_tree_binding` | NOT_EXERCISED | 锁定 topology 证明 tag 的 commit/tree 及 clone 的 tag tree，但没有证明当前仓库执行了 direct package-tree 比较，或 clone 从 tag tree 核验完整发布路径。 |
| `verifies_version_surfaces_from_release` | NOT_EXERCISED | 候选输出列出四个版本面并正确区分 v1.2.0 与 package.json 的 1.2.0；但锁定证据没有 git blob 或 delivery snapshot 将这些读取绑定到实际 tag tree。 |
| `requires_durable_post_tag_evidence` | PASS | 候选输出明确指出 proposed post-release ref 没有维护者决定、目标 ref 不存在，并让当前工作区和普通新克隆均保持 blocked；fixture context 与锁定 topology 支持该结论。 |
| `preserves_upstream_release_artifacts` | PASS | 候选输出未声称重新生成、重新盖章或移动 tag；锁定 git evidence 显示 head、branch、refs、diff 与 reflog 均未变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=7c1a8a3d832e53935df5ce5bc6feca448187edb7639f34a08fc9414d1992473b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别 tag 与 custom ref 的拓扑、普通 clone 未携带 custom ref，并将两个场景保持为 blocked；但锁定原始证据不足以证明 authority 读取、tree binding 和从 tag blob 核验版本面。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=2a7663d28fe5769cbf8883e6ea6fe63775acdf384ad4fe2df99fd95852e81644; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 新克隆和 tag 身份描述基本正确，但把内容一致直接升级为可独立核对成功，遗漏了缺少 durable post-tag 结果凭据这一阻塞条件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充当前 custom ref 下 handoff/audit 的锁定 blob 证据。
- Next: 补充 tag tree 与 direct package tree、完整发布路径及四个版本面的锁定读取证据。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518` from `agents/docs/test/docs-audit/evals/workspace/eval-010-post-tag-match`.
- Fixture SHA-256: `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518`
- Prompt SHA-256: `47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f4b575228474dd8bb2a93bb17a067f25252f9c293e1f78393d445c449385e8d2`
- Metadata SHA-256: `12f75879efa3cacf943ae19595239a747563947015e4033eed4ea7f4a51a5b47`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_pre_tag_authority_safely` | PASS | with_skill 说明当前仓库解析 refs/release-evidence/v1.2.0 并检查 handoff/audit；新克隆使用默认 refspec，确认未取得 custom ref，并从自身 tag 中的已提交路径回退核验。 |
| `proves_released_tree_binding` | PASS | with_skill 实际给出 v1.2.0 的 commit/tree 解析、pre-tag ref 与 tag tree 一致，以及新克隆从自身 tag tree 核验版本面和相关 blob；未依赖 commit identity 相同作为唯一依据。 |
| `verifies_version_surfaces_from_release` | PASS | with_skill 从发布对象核验 Release Notes、index、.meta/releases.json 与 package.json，正确区分 v1.2.0 和 1.2.0，并明确未以当前工作区作为成功证据。 |
| `requires_durable_post_tag_evidence` | PASS | with_skill 识别缺少 refs/heads/release-evidence/v1.2.0 及维护者决定，明确两个场景只能核对内容、不能完成 release_verified，最终为 blocked。 |
| `preserves_upstream_release_artifacts` | PASS | with_skill 明确未修改现有 ref、tag 或发布记录；锁定 git_evidence 显示 HEAD、分支、ref_delta、提交、结果差异和 reflog 均未变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=814cbba43605675dde0a70affad2b97c7a5e30b6fdecc221273bd1dbb8bde97e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 分别核验当前仓库和默认 refspec 新克隆，确认版本面绑定，同时识别缺失持久化凭据并将两边结论保持为 blocked，且无变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=19c9e8060ea734a51e89cd9bdcb176fc25dbdceab10b0c2dfa19ed43e7b03a4b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确描述 tag/tree 和新克隆的部分核验，但错误地将内容核验直接判为通过，遗漏 durable post-tag 凭据阻断。
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
- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518` from `agents/docs/test/docs-audit/evals/workspace/eval-010-post-tag-match`.
- Fixture SHA-256: `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518`
- Prompt SHA-256: `47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d339a8370a29b3fb2a69aa1879b1226165ec088d306a4e2e7a01258df2326973`
- Skill overlay SHA-256: `0bc7243cbb5cff3e77d9ba448e020a1a1f279639f8db6a365faac208b8e1dcc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f4b575228474dd8bb2a93bb17a067f25252f9c293e1f78393d445c449385e8d2`
- Metadata SHA-256: `12f75879efa3cacf943ae19595239a747563947015e4033eed4ea7f4a51a5b47`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_pre_tag_authority_safely` | NOT_EXERCISED | 候选输出描述了当前仓库和新克隆的 ref 可见性，但锁定证据没有证明实际的解析/读取顺序或克隆确实仅使用自身 Git 对象。 |
| `proves_released_tree_binding` | NOT_EXERCISED | 输出给出了 tag commit/tree 和 blob 一致性结论，但锁定证据无法证明实际完成了要求的 tree 比较与独立内容绑定核验。 |
| `verifies_version_surfaces_from_release` | PASS | 明确从 tag 树核验四个版本面，说明 release-note 使用 v1.2.0、package.json 使用 1.2.0，并进行规范化处理；未将工作区作为成功证据。 |
| `requires_durable_post_tag_evidence` | PASS | 明确指出缺少已确认的 post-tag 记录 ref/独立持久化凭据，并将两种场景的最终状态保持为 blocked，而非 release_verified。 |
| `preserves_upstream_release_artifacts` | PASS | 明确声明未修改现有 ref、tag、发布记录，也未创建 post-tag 审计记录；锁定 git evidence 显示无 ref、提交或工作区变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=8d74b8beab8c4dd50ac418750c97cce6f6f7487887cc536a4ed69d70ffd6c513; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别版本内容可核验但 post-tag 审计凭据缺失，保持 blocked，并报告未发生发布产物或 ref/tag 变更；关键隐藏解析过程无法由锁定证据验证。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=fe8a5a78d94b6659ac7b161d0571cf1b285f760da6cb4f664fc2c697ef1c072d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 能描述 tag、tree、版本路径和默认克隆，但未识别缺少独立 post-tag 持久化凭据，错误地得出两边均可完成核对的结论。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 如需完整覆盖，请提供两种 lane 的 Git 解析、默认克隆隔离及 tree/blob 比较原始记录。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518` from `agents/docs/test/docs-audit/evals/workspace/eval-010-post-tag-match`.
- Fixture SHA-256: `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518`
- Prompt SHA-256: `47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9e9abf391c9ccd9564d35b5def50bc0374b1db0886710676c4d48422839746ae`
- Skill overlay SHA-256: `c66ac938bf9158faa694d7c3e311e913ddc4a06da11de703a881234f257c470c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f4b575228474dd8bb2a93bb17a067f25252f9c293e1f78393d445c449385e8d2`
- Metadata SHA-256: `12f75879efa3cacf943ae19595239a747563947015e4033eed4ea7f4a51a5b47`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_pre_tag_authority_safely` | PASS | With-skill identifies and compares the release-evidence ref and tag trees, confirms the default clone lacks the custom ref, and uses only tag-visible committed content for clone verification; no source-ref injection is claimed. |
| `proves_released_tree_binding` | PASS | With-skill reports the tag commit/tree, matching release-evidence tree, and verifies release files from the tag without relying on commit identity. |
| `verifies_version_surfaces_from_release` | PASS | With-skill verifies all four requested version surfaces from release content and distinguishes package.json's 1.2.0 form from v1.2.0 labels. |
| `requires_durable_post_tag_evidence` | PASS | With-skill identifies the absent post-tag evidence branch/maintainer decision and keeps both scenarios blocked rather than treating content consistency as post-tag success. |
| `preserves_upstream_release_artifacts` | PASS | With-skill reports no ref, tag, release-record, or workspace mutations; locked git evidence confirms unchanged HEAD, refs, and clean state. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=fee474ff72ea5d44e490048e650fd5733fb95da48033e6fa5e453f815e1e62f4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly treats both scenarios as blocked by missing durable post-tag authority while documenting tag/tree, version-surface, clone, and mutation evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=39e2bbf03e7288a4aecab913161907f44d0c8697dddf4be3a28146f9f5c5f35f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly verifies the tag and notes the clone lacks the custom evidence ref, but incorrectly concludes the current workspace can complete the full review.
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
- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518` from `agents/docs/test/docs-audit/evals/workspace/eval-010-post-tag-match`.
- Fixture SHA-256: `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518`
- Prompt SHA-256: `47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2d24da5f976a5ab2710c2c072a19015e074d314e0ebdb88f1c28831425f1b98c`
- Skill overlay SHA-256: `40330c17a3b77f25a1b1a716fa5e9355e0011db79d19014344ed516affba11c8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f4b575228474dd8bb2a93bb17a067f25252f9c293e1f78393d445c449385e8d2`
- Metadata SHA-256: `12f75879efa3cacf943ae19595239a747563947015e4033eed4ea7f4a51a5b47`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_pre_tag_authority_safely` | PASS | with_skill 实际解析了 refs/release-evidence/v1.2.0；说明默认 refspec 新克隆未取得该 custom ref，并从克隆自身 tag tree 读取 handoff、audit 和版本面。 |
| `proves_released_tree_binding` | PASS | with_skill 解析了 tag commit/tree，报告当前仓库 tag/package tree 无差异，并说明新克隆从 tag tree 读取已提交证据与完整发布路径。 |
| `verifies_version_surfaces_from_release` | PASS | with_skill 核验了 release notes、index、.meta/releases.json 为 v1.2.0，package.json 为 1.2.0，正确区分两种版本表示，并以 tag 内容核验。 |
| `requires_durable_post_tag_evidence` | PASS | with_skill 明确指出 proposed refs/heads/release-evidence/v1.2.0 不存在、没有 maintainer decision，且当前仓库和新克隆均为 blocked 而非 release_verified。 |
| `preserves_upstream_release_artifacts` | PASS | with_skill 明确说明未修改 ref、tag 或发布记录；raw git evidence 显示 head、branch、ref_delta、diff 和新提交均未变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=7a23812420ee7db5ee4ffaf360a40c8053620e43bd47ee231343cb0366f46298; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 独立说明当前仓库和默认新克隆的 authority、tag tree、版本面及 custom ref 缺失，并将两种场景都保持为 blocked。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=1b08da83862a09a17d0dd316dd009a3ecad10c4aca894dc2b41365f10e8cb5a1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别当前仓库与新克隆的主要 ref/tag 状态，但将两边描述为可完整核对/可确认内容，未保持 post-tag blocked 结论。
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
- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518` from `agents/docs/test/docs-audit/evals/workspace/eval-010-post-tag-match`.
- Fixture SHA-256: `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518`
- Prompt SHA-256: `47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f4b575228474dd8bb2a93bb17a067f25252f9c293e1f78393d445c449385e8d2`
- Metadata SHA-256: `12f75879efa3cacf943ae19595239a747563947015e4033eed4ea7f4a51a5b47`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_pre_tag_authority_safely` | FAIL | with_skill correctly resolves the current repository authority and detects that the fresh clone lacks the custom ref, but it stops at stating that the clone cannot independently verify or rebuild the pre-tag authority rather than satisfying the required clone-side reconstruction. |
| `proves_released_tree_binding` | PASS | with_skill resolves the tag commit and tree, reports the tag tree matching the package tree, and verifies the committed release surfaces and evidence paths in the clone without relying on matching commit identity. |
| `verifies_version_surfaces_from_release` | PASS | with_skill verifies the release surfaces from the tag tree, distinguishes package.json 1.2.0 from v1.2.0 representations, and does not treat the current worktree as success evidence. |
| `requires_durable_post_tag_evidence` | PASS | with_skill identifies the absent proposed post-release ref and keeps both environments blocked rather than upgrading content consistency to post-tag success. |
| `preserves_upstream_release_artifacts` | PASS | with_skill reports no changes to refs, tags, release records, or the workspace and preserves the pre-tag authority. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=b85e0073dd1420310b23299bf43d42831accf2d8d31fd608ca8cad1049cd8240; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Safely distinguishes tag-content verification from missing post-tag authority, keeps both scenarios blocked, and preserves repository artifacts; it does not complete the required clone-side pre-tag-authority reconstruction.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=a56cba5e5d86de0909b665922578715b0ab6c5bcc287b9ec6e6eb3656b44148b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Claims both environments passed and incorrectly upgrades content verification to a successful release review.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output does not independently rebuild or verify the pre-tag authority from only the fresh clone's visible tag tree and committed paths.
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

- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`
- Scenario: direct handoff 与 fresh clone 两种对象可达性下的 post-tag authority 与持久化门禁
- Review context: issue #177 sub-batch 4b

## Test Set / Fixture Version

- Fixture version: `issue-177 discrimination restore round-1`
- Validation time: `2026-07-28 22:48:16 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-audit/round-1/`
- Assertions: 5，全部实际触发

## Latest Result

- Behavior result: `PASS`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `selects_pre_tag_authority_safely` | PASS | FAIL | with_skill 明确区分 direct-handoff 与 fresh-clone，并在 fresh-clone 使用 tag tree 固定路径回退校验；without_skill 明确称 fresh-clone 无法重建完整审计链。 |
| `proves_released_tree_binding` | PASS | FAIL | with_skill 给出 `entry_tag_tuple` 与 `pre_result_tag_tuple` 一致、实际 tree 为 `666…666`，并解释 commit identity 不同但 tree 一致；without_skill 的 fresh-clone 仅能看到 tag tree，无法完成完整绑定复核。 |
| `verifies_version_surfaces_from_release` | PASS | PASS | 两条 lane 均核验 tag、Release Notes、索引、`releases.json` 与 `package.json`，并处理 `v1.2.0` / `1.2.0` 表示差异；证据指向 tag tree 与已提交路径。 |
| `requires_durable_post_tag_evidence` | PASS | FAIL | with_skill 明确识别 `release_evidence_branch_confirmation` 和 `release_evidence_expected_head` 缺失，并将两个场景均保持为 `blocked`；without_skill 将 direct-handoff 描述为“文档内容已验证、发布闭环待确认”，未按断言要求保持 blocked。 |
| `preserves_upstream_release_artifacts` | PASS | PASS | 两条 lane 均明确“未执行任何 tag、branch 或 release 写入”，且未重新生成、盖章或改变 pre-tag handoff。 |

未满足断言（with/without 任一 FAIL）：``selects_pre_tag_authority_safely``、``proves_released_tree_binding``、``requires_durable_post_tag_evidence``



## Leakage Surface Analysis

重做前，baseline 可直接从 prompt、assertions 与 release context 取得 package 优先级、fixed-path fallback、anchor tree 重建、tag tuple 双读、object-read 范围、版本规范化、独立记录路径、FF/CAS 和成功状态。

重做后仍可见的是原始 object identity、candidate/discovery 记录和版本表面；不再预告 locator 选择、fallback 算法或独立持久化 gate。release context 只声明 direct/fresh 对象可达性和一个未确认 branch hint。

## Redesign

- prompt 只保留 post-tag 任务、两个场景、输入指针与只读边界。
- assertions 收敛为 authority、release tree、version surfaces、durable result 和上游不可变性五个语义结果。
- 删除 fixture 中的 locator 优先级、tree equality 结论、normalization 结论和 CAS 恢复答案。
- 增加阻塞型凭据缺口：branch hint 存在，但 maintainer confirmation 与 expected head 均缺失。
- 将历史 issue 身份引用替换为 `docs-agent:release-notes-gen`，并重算 inventory digest、candidate blob、discovery blob 与 lineage digest。

## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `selects_pre_tag_authority_safely` | PASS | FAIL | skill arm 分别验证 direct handoff 与 tag-tree fixed-path fallback；baseline 将 fresh clone 判为无法建立 authority。 |
| `proves_released_tree_binding` | PASS | FAIL | skill arm 在两种可达性下都证明完整 tag tree 绑定；baseline 只完成 direct 场景。 |
| `verifies_version_surfaces_from_release` | PASS | FAIL | skill arm 从 peeled tag tree 复核完整来源；baseline 未完成 fresh 场景的发布对象复核。 |
| `requires_durable_post_tag_evidence` | PASS | FAIL | skill arm 因 evidence branch/head 未确认让两场景都 blocked；baseline 错误放行 direct 场景。 |
| `preserves_upstream_release_artifacts` | PASS | PASS | 两臂均未改 pre-tag authority、stamp、tag 或 Release。 |

## Fresh Validation Method

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

1. 两个生成 arm 只读取 `eval_metadata.json` 的 prompt 与 fixture_context；锁定前均未读取 `evals.json`、assertions、expected output 或旧 comparison。
2. with-skill arm读取 Docs README、`docs-audit/SKILL.md` 和完整内部指令；without-skill arm 不读取或应用这些内容，也不读取 with-skill 输出。
3. 两臂基于同一最终 fixture revision 生成 response 并锁定 SHA-256 后，fresh judge 才读取 assertions。
4. with-skill response SHA-256：`0605883f82aff53f7bf03dbe5a90b6e950989032fc041a169af38aaaeb81b8e4`；without-skill：`475f755dcf05f9a146e36c5f3925600165794cc0db9122574bf90db09553dfa7`。

## Failures And Limitations

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- with-skill 无失败；Coverage FULL。
- baseline 仍能从 committed records 恢复部分 authority 与版本事实，但未恢复 fresh-clone fallback 和 durable-result credential gate。
- 第一轮即达到区分度，无需第二轮。

## Runtime Artifact Policy

- responses、judge verdict 与校验和仅位于 git 忽略的 `tmp/eval-runs/issue-177/docs-audit/round-1/`，不提交。
- 本 `comparison.md` 是唯一 durable 结果。
