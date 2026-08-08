# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-008-marketplace-historical-tag-limit-upgrade-note`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-008-marketplace-historical-tag-limit-upgrade-note`.
- Fixture SHA-256: `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933`
- Prompt SHA-256: `734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f95690411417d5e9cf66495e67ce2d96d0a51fc4ca1821536421129a950bb8f3`
- Skill overlay SHA-256: `ee4b811662f5234e9cbcc50a85629526ebcf704244484e48f81d5ce85841d93c`
- Judge schema SHA-256: `df39efd24a07751331d3b8f08b12fab041cb7e732754feb1dfc8bc4a96c5fe1a`
- Eval definition SHA-256: `ca7c0b18d751c17e3675256471abe2e22f05a84c6ec6d780c8a51c53156008f9`
- Metadata SHA-256: `a37c69100d8b09e8a32fd7ae07c266ac1aa0ef65dd08a89916726ecd29694ad7`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | 标题为“v0.9.0 - 失败消息重试与统一附件模型兼容”，符合要求。 |
| `upgrade_note_first_sentence_derived` | PASS | 「升级说明」首段以指定句开头，并使用由 manifest 推导的 6 个 role plugin 数量。 |
| `claude_section_omitted_with_platform_limit` | FAIL | 正文包含 `### Claude Code` 小节；该小节按要求应省略。 |
| `codex_section_omitted_without_target_tag_support` | FAIL | 正文包含 `### Codex` 小节；目标 INSTALL.md 不支持 TARGET_TAG，按要求应省略。 |
| `kimi_section_omitted_without_plugin_json` | FAIL | 正文包含 `### Kimi Code` 小节；目标 tag 无 plugin.json，按要求应省略。 |
| `closing_sentence_derived` | PASS | 收尾句包含 6 个 role plugin 数量，并声明无已验证固定版本安装路径、按 main 更新，未作不当承诺。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=78ceeca5ece40ef6b66fd38b11539fb3b8c001e688253560de30173ee86fb9a4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了未写入或发布的 Release 预览；标题和升级说明数量推导正确，但错误保留了应省略的 Claude Code、Codex 和 Kimi Code 小节。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=27213037a7e614431148631468ba0bb3dbf8bc8d4f135e4343eb9bdfde3c0b85; snapshot_sha256=7aac4f219319af522179782d1c0588f0eb805963ed386026d5a40ac586f321a5
- Behavior: 生成了文件型 Release 预览并保持仓库未提交；标题未采用要求的 marketplace 格式，且保留并泛化描述了三个宿主小节。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- claude_section_omitted_with_platform_limit
- codex_section_omitted_without_target_tag_support
- kimi_section_omitted_without_plugin_json
- Next: 删除升级说明中的 Claude Code、Codex 和 Kimi Code 小节，并保留平台限制及无固定版本安装路径的声明。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-008-marketplace-historical-tag-limit-upgrade-note`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-008-marketplace-historical-tag-limit-upgrade-note`.
- Fixture SHA-256: `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933`
- Prompt SHA-256: `734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f95690411417d5e9cf66495e67ce2d96d0a51fc4ca1821536421129a950bb8f3`
- Skill overlay SHA-256: `ee4b811662f5234e9cbcc50a85629526ebcf704244484e48f81d5ce85841d93c`
- Judge schema SHA-256: `df39efd24a07751331d3b8f08b12fab041cb7e732754feb1dfc8bc4a96c5fe1a`
- Eval definition SHA-256: `ca7c0b18d751c17e3675256471abe2e22f05a84c6ec6d780c8a51c53156008f9`
- Metadata SHA-256: `a37c69100d8b09e8a32fd7ae07c266ac1aa0ef65dd08a89916726ecd29694ad7`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | The with_skill preview title is `v0.9.0 - 失败消息重试与统一附件链路`, matching the required format with a non-empty, evidence-related summary. |
| `upgrade_note_first_sentence_derived` | FAIL | The upgrade section begins with the required facts and derives N=6 from the target marketplace, but the required opening sentence ends after `v0.9.0` whereas the candidate continues it with an added clause. |
| `claude_section_omitted_with_platform_limit` | PASS | The candidate omits the `### Claude Code` section and explains the missing version pin, lack of a verified fixed-version path, and main-branch fallback. |
| `codex_section_omitted_without_target_tag_support` | PASS | The candidate omits the `### Codex` section and states that the target INSTALL.md lacks TARGET_TAG support. |
| `kimi_section_omitted_without_plugin_json` | PASS | The candidate omits the `### Kimi Code` section and states that the target tag has no `.kimi-plugin/plugin.json`. |
| `closing_sentence_derived` | FAIL | The upgrade note closes by stating that the tag has no verified fixed-version installation path and to update from main, but the closing sentence does not contain the manifest-derived count of 6 role plugins. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=92c9340b36664e90c04419d34056ddf0f48c31f1d1ef0adf7e751915dcab4d16; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a preview with a correctly formatted title, platform-specific omissions, and accurate fixed-version limitations, but missed two literal sentence-level requirements.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=0f6e06f0b847212336aadcb347f2c36d376cb799aeb73165f5f4404260e8351e; snapshot_sha256=1013e9433ec76bf2bc41a647753970194521c80fcd126fa6ffd6653a286ed880
- Behavior: Produced a file-backed preview that included unsupported platform sections and did not follow the required omission and fixed-version limitations.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The upgrade-note opening does not use the required first-sentence form.
- The closing sentence omits the required count of 6 role plugins.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-008-marketplace-historical-tag-limit-upgrade-note`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-008-marketplace-historical-tag-limit-upgrade-note`.
- Fixture SHA-256: `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933`
- Prompt SHA-256: `734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `380b2fcfd0ff29b900d02472045d511ad62a16c847b128cbfdce8af3c7a60338`
- Skill overlay SHA-256: `c666691beb368144f31c0354fd118ef20d664151476cfb1c8695e6ee7c490aa7`
- Judge schema SHA-256: `df39efd24a07751331d3b8f08b12fab041cb7e732754feb1dfc8bc4a96c5fe1a`
- Eval definition SHA-256: `ca7c0b18d751c17e3675256471abe2e22f05a84c6ec6d780c8a51c53156008f9`
- Metadata SHA-256: `a37c69100d8b09e8a32fd7ae07c266ac1aa0ef65dd08a89916726ecd29694ad7`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | 标题为“v0.9.0 - 失败消息重试与统一附件模型”，概述非空且对应已确认变更。 |
| `upgrade_note_first_sentence_derived` | PASS | 升级说明首段以“无破坏性变更，也没有新增 plugin。6 个 role plugin 均更新到 `v0.9.0`。”开头。 |
| `claude_section_omitted_with_platform_limit` | PASS | 正文无 `### Claude Code` 小节，说明 `/plugin update` 无法固定到 `v0.9.0`，并声明无已验证固定版本路径。 |
| `codex_section_omitted_without_target_tag_support` | FAIL | 正文实际包含 `### Codex` 小节，违反目标 tag 不支持 TARGET_TAG 时省略该小节的要求。 |
| `kimi_section_omitted_without_plugin_json` | PASS | 正文无 `### Kimi Code` 小节，也未臆造 `/plugins install` 命令。 |
| `closing_sentence_derived` | PASS | 收尾句明确包含 6 个 plugin，并说明无已验证固定版本安装路径、按默认分支 `main` 更新，未作固定版本同步承诺。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=383c7a99e169fc5f7956eb4e07fdab5687772b3d2451f43442926888e7b229aa; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了符合大部分约束的 inline preview，但错误保留 Codex 小节。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=f88626d2cd6ca73f8140869e5ce6a72a2d93b9711bcb3c1361fedfd669cfb708; snapshot_sha256=d171384b7d402f82f6a69859fd33b343b2e12b31f130f38d069ddcd12590edda
- Behavior: 生成了文件型预览并覆盖多个宿主说明，但标题为裸版本号，且未遵循所需的升级说明和宿主小节省略约束。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出保留了不应出现的 `### Codex` 小节。
- Next: 移除 `### Codex` 小节，并仅在正文保留不臆造 TARGET_TAG 指令的限制说明。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-008-marketplace-historical-tag-limit-upgrade-note`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-008-marketplace-historical-tag-limit-upgrade-note`.
- Fixture SHA-256: `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933`
- Prompt SHA-256: `734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `380b2fcfd0ff29b900d02472045d511ad62a16c847b128cbfdce8af3c7a60338`
- Skill overlay SHA-256: `c666691beb368144f31c0354fd118ef20d664151476cfb1c8695e6ee7c490aa7`
- Judge schema SHA-256: `df39efd24a07751331d3b8f08b12fab041cb7e732754feb1dfc8bc4a96c5fe1a`
- Eval definition SHA-256: `ca7c0b18d751c17e3675256471abe2e22f05a84c6ec6d780c8a51c53156008f9`
- Metadata SHA-256: `a37c69100d8b09e8a32fd7ae07c266ac1aa0ef65dd08a89916726ecd29694ad7`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | FAIL | The locked with_skill markdown uses `# Release Notes - v0.9.0 (2026-08-08)`, not the required `v0.9.0 - {主题概述}` format. |
| `upgrade_note_first_sentence_derived` | PASS | The upgrade section begins with the required sentence and derives the count as 6 from the target marketplace manifest. |
| `claude_section_omitted_with_platform_limit` | PASS | No `### Claude Code` section is present; the body explains the `/plugin update` version-pin limitation and states there is no verified fixed-version path. |
| `codex_section_omitted_without_target_tag_support` | PASS | No `### Codex` section is present, and the content states that TARGET_TAG support is absent. |
| `kimi_section_omitted_without_plugin_json` | PASS | No `### Kimi Code` section is present, and the content states that `.kimi-plugin/plugin.json` is absent. |
| `closing_sentence_derived` | PASS | The upgrade section closes with a statement that no fixed-version path is verified and updates the default `main` branch; it does not make the forbidden synchronization promise. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=10b7c3cc120535344a945f5bca1333d2efb59d3419ba68546c5a5c4fd8618ead; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly derived the upgrade guidance and omitted unsupported Claude, Codex, and Kimi sections, but produced a nonconforming preview title.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=5a23ec08b108110bcf264b8d8a87218308058cb0940d75fc5bd047ccef39367c; snapshot_sha256=402f69fe3a7c5b19d39116533bf85feabc7df1ad4c178b88ee1fba276b655b8f
- Behavior: Fresh baseline produced a generic `Dev Agent Skills v0.9.0` title and included platform-specific bullets rather than the required structured omissions and derived guidance.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill preview title does not match the required marketplace format.
- Next: Regenerate the preview with a title in the form `v0.9.0 - {主题概述}`.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-008-marketplace-historical-tag-limit-upgrade-note`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-008-marketplace-historical-tag-limit-upgrade-note`.
- Fixture SHA-256: `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933`
- Prompt SHA-256: `734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `380b2fcfd0ff29b900d02472045d511ad62a16c847b128cbfdce8af3c7a60338`
- Skill overlay SHA-256: `c666691beb368144f31c0354fd118ef20d664151476cfb1c8695e6ee7c490aa7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ca7c0b18d751c17e3675256471abe2e22f05a84c6ec6d780c8a51c53156008f9`
- Metadata SHA-256: `a37c69100d8b09e8a32fd7ae07c266ac1aa0ef65dd08a89916726ecd29694ad7`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | with_skill 标题为“v0.9.0 - 失败消息重试与统一附件链路”，符合格式且概述非空、关联已确认事实。 |
| `upgrade_note_first_sentence_derived` | PASS | 升级说明首段以“无破坏性变更，也没有新增 plugin。6 个 role plugin 均更新到 v0.9.0。”开头。 |
| `claude_section_omitted_with_platform_limit` | FAIL | 虽未包含 Claude Code 小节，但正文未说明 Claude 的“/plugin update”无版本 pin 及无法保证固定安装到 v0.9.0 的平台限制。 |
| `codex_section_omitted_without_target_tag_support` | FAIL | 正文包含“### Codex”小节；该断言要求目标 tag 不支持 TARGET_TAG 时省略该小节。 |
| `kimi_section_omitted_without_plugin_json` | FAIL | 正文包含“### Kimi Code”小节；该断言要求无 .kimi-plugin/plugin.json 时省略该小节。 |
| `closing_sentence_derived` | PASS | 升级说明收尾包含无已验证固定版本安装路径、按默认分支 main 更新，并在前文明确 6 个 role plugin。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=078abfcba0555233f10dc2c503d9c414051e696feb8fa351e9a7e619ddd7dbf2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确推导标题、6 个 role plugin、无破坏性变更及无固定版本路径，但错误保留了 Codex/Kimi 小节，并遗漏 Claude 平台限制说明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=ece61b407c5f22e3eb18f45958afdbbb31837d0ed123fa0d10136e72e04efb6f; snapshot_sha256=88c07d11e5ed21b979406f8ae30a690399b632b60f6670ccb7c6d84603000ee6
- Behavior: 生成了内容较完整但将三种宿主安装能力混写的预览文件；标题为裸版本加项目名格式，未满足本组针对历史 tag 的精确升级约束。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出未省略 Codex 与 Kimi 小节。
- with_skill 输出未在正文说明 Claude /plugin update 无版本 pin 的限制。
- Next: 删除 Codex 与 Kimi 小节，并将相关事实改为正文中的简短平台限制说明。
- Next: 补充 Claude /plugin update 无版本 pin、无法保证固定到 v0.9.0 的说明。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-008-marketplace-historical-tag-limit-upgrade-note`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-008-marketplace-historical-tag-limit-upgrade-note`.
- Fixture SHA-256: `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933`
- Prompt SHA-256: `734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bfa553ee1e9614c42bec50e00faa33ed1a614260acdb1011ab1116e8b73db2dd`
- Skill overlay SHA-256: `0db0717c5ca83fddc3ecdfe8bf130c8885c13a22148bb9bf0d8e93c491b17294`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ca7c0b18d751c17e3675256471abe2e22f05a84c6ec6d780c8a51c53156008f9`
- Metadata SHA-256: `a37c69100d8b09e8a32fd7ae07c266ac1aa0ef65dd08a89916726ecd29694ad7`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | 标题为“v0.9.0 - 失败消息重试与统一附件模型兼容”，符合格式且概述非空、对应已确认发布事实。 |
| `upgrade_note_first_sentence_derived` | PASS | 升级说明以指定句开头，明确 6 个 role plugin 均更新到 v0.9.0，且内容与 fixture 事实一致。 |
| `claude_section_omitted_with_platform_limit` | PASS | 未生成 Claude Code 小节，说明 /plugin update 无版本 pin，并明确该 tag 无已验证固定版本安装路径。 |
| `codex_section_omitted_without_target_tag_support` | PASS | 未生成“### Codex”小节，未臆造 TARGET_TAG 或 INSTALL.md fetch 指令，并准确说明旧版安装能力限制。 |
| `kimi_section_omitted_without_plugin_json` | PASS | 未生成“### Kimi Code”小节，未臆造 /plugins install 命令，并说明目标 tag 无 plugin manifest。 |
| `closing_sentence_derived` | PASS | 收尾明确包含 6 个 role plugin，并声明无已验证固定版本安装路径、按 main 更新，未作不受证据支持的同步承诺。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=605ffe795e1ed30f993d49fa9b5bf11732d03c25be0096a53e446b301f8173d3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了符合 marketplace 格式的历史 tag Release 预览，正确推导 6 个 plugin，并按平台能力省略相关小节、说明限制及无固定版本路径。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=c794e3a1f9a0dd36981fee1af7646886fcdbcf3a84b0d2c8e9b7a6391a13a029; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了裸版本 Tag 元数据式预览，包含不应生成的 Claude、Codex、Kimi 小节，且升级说明和固定版本限制处理不符合断言。
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
- Eval: `eval-008-marketplace-historical-tag-limit-upgrade-note`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-008-marketplace-historical-tag-limit-upgrade-note`.
- Fixture SHA-256: `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933`
- Prompt SHA-256: `734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bfa553ee1e9614c42bec50e00faa33ed1a614260acdb1011ab1116e8b73db2dd`
- Skill overlay SHA-256: `0db0717c5ca83fddc3ecdfe8bf130c8885c13a22148bb9bf0d8e93c491b17294`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ca7c0b18d751c17e3675256471abe2e22f05a84c6ec6d780c8a51c53156008f9`
- Metadata SHA-256: `a37c69100d8b09e8a32fd7ae07c266ac1aa0ef65dd08a89916726ecd29694ad7`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | With-skill title is `v0.9.0 - 失败消息重试与附件链路兼容`, matching the required format with a non-empty, fact-based overview. |
| `upgrade_note_first_sentence_derived` | PASS | The upgrade section begins with the required no-breaking-change/no-new-plugin statement and correctly states 6 role plugins updated to `v0.9.0`. |
| `claude_section_omitted_with_platform_limit` | FAIL | The with-skill output includes a `### Claude Code` section, although the historical-tag rerun requirement says to omit it; it also presents Codex instructions despite the fixture confirming no fixed-version path. |
| `codex_section_omitted_without_target_tag_support` | FAIL | The with-skill output includes a `### Codex` section even though `.codex/INSTALL.md` lacks `TARGET_TAG` support; the assertion requires omitting that section. |
| `kimi_section_omitted_without_plugin_json` | PASS | No `### Kimi Code` section or `/plugins install` command is generated; Kimi is mentioned only in surrounding prose. |
| `closing_sentence_derived` | PASS | The upgrade explanation has a closing statement identifying 6 role plugins and explicitly says there is no verified fixed-version installation path, with updates performed from `main`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=e9b6143d46864eac613d1b5a4eec912843a995135629b1de2b7d20fa3cbebe6a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a semantically detailed preview with correct version/plugin-count derivation and safe no-mutation handling, but included Claude and Codex sections that the fixture-specific historical-tag constraints require omitting.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=29f78eb81c5970c6c2cfa7e57c6be4637a42ce0927d3444d89ef568389d85755; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a release preview but used an incorrect title format and included unsupported/inapplicable platform guidance.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output violates the required omission of the Claude Code section.
- The with_skill output violates the required omission of the Codex section when TARGET_TAG support is absent.
- Next: Remove the `### Claude Code` and `### Codex` sections and retain an explicit statement that the historical tag has no verified fixed-version installation path.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-008-marketplace-historical-tag-limit-upgrade-note`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-008-marketplace-historical-tag-limit-upgrade-note`.
- Fixture SHA-256: `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933`
- Prompt SHA-256: `734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `793cabc84dc1947c3d6386a1d060276eea2eb8b4e9de25fdd6c7b7a60fb82cb0`
- Skill overlay SHA-256: `ecc021af86f838c5c915ade1c1e1095fa203f789350af9aa701ad32bae876bb2`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ca7c0b18d751c17e3675256471abe2e22f05a84c6ec6d780c8a51c53156008f9`
- Metadata SHA-256: `a37c69100d8b09e8a32fd7ae07c266ac1aa0ef65dd08a89916726ecd29694ad7`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | With-skill 标题为 `v0.9.0 - 失败消息重试与附件模型兼容`，符合格式且概述非空、与事实相关。 |
| `upgrade_note_first_sentence_derived` | PASS | 升级说明首段以「无破坏性变更，也没有新增 plugin。6 个 role plugin 均更新到 `v0.9.0`。」开头。 |
| `claude_section_omitted_with_platform_limit` | FAIL | 正文包含 `Claude Code` 小节；该断言要求历史 tag 重跑时省略该小节。 |
| `codex_section_omitted_without_target_tag_support` | FAIL | 正文包含 `Codex` 小节；fixture 明确目标 tag 不支持 TARGET_TAG，断言要求省略该小节。 |
| `kimi_section_omitted_without_plugin_json` | FAIL | 正文包含 `Kimi Code` 小节；fixture 明确无 `.kimi-plugin/plugin.json`，断言要求省略该小节。 |
| `closing_sentence_derived` | FAIL | 正文有无固定版本安装路径的声明，但收尾句「该 tag 无已验证的固定版本安装路径，按默认分支（main）更新」未包含由 manifest 推导的 6 个 role plugin 数量。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=0a8fcc47f241ba629bd94e85926726560174b5cc00d29215a21cb39dbf783f08; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 标题和升级说明首段符合要求，也声明了平台限制，但未按能力缺失要求省略 Codex、Claude Code、Kimi Code 小节，且收尾句缺少 6 个 role plugin 数量。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=d28b33c02a64ba8fe257c3af8811a44ae2804e6b14fa818e67bd65c5af80a9aa; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了包含大量未由 fixture 确认事实的 Release 内容，并保留了不应生成的客户端小节。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未省略不适用的 Claude Code、Codex、Kimi Code 小节。
- with_skill 的升级说明收尾句未包含 6 个 role plugin 数量。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-008-marketplace-historical-tag-limit-upgrade-note`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-008-marketplace-historical-tag-limit-upgrade-note`.
- Fixture SHA-256: `17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933`
- Prompt SHA-256: `734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ebd2c00966a7932d251daeeef05573b0145183fe908cf102225636115f85820c`
- Skill overlay SHA-256: `2398a04c1c550bc8e45aa1564f5f42f6e629a29d1c1ed530494ae269f918d169`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ca7c0b18d751c17e3675256471abe2e22f05a84c6ec6d780c8a51c53156008f9`
- Metadata SHA-256: `a37c69100d8b09e8a32fd7ae07c266ac1aa0ef65dd08a89916726ecd29694ad7`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `title_matches_marketplace_format` | PASS | with_skill 标题为 `v0.9.0 - 失败消息重试与统一附件兼容`，概述非空且对应已确认发布事实。 |
| `upgrade_note_first_sentence_derived` | PASS | 「升级说明」首段以要求的“无破坏性变更，也没有新增 plugin。6 个 role plugin 均更新到 `v0.9.0`。”开头。 |
| `claude_section_omitted_with_platform_limit` | FAIL | 虽未生成 `### Claude Code`，但写有“需要固定版本时使用具备相应能力的安装路径”，而 fixture 明确无已验证固定版本路径；未按要求直接明确该 tag 无固定版本安装路径。 |
| `codex_section_omitted_without_target_tag_support` | FAIL | with_skill 生成了 `### Codex` 小节，尽管 `.codex/INSTALL.md` 不含 TARGET_TAG 支持。 |
| `kimi_section_omitted_without_plugin_json` | PASS | 未生成 `### Kimi Code` 小节，也未臆造 `/plugins install` 命令。 |
| `closing_sentence_derived` | FAIL | 升级说明收尾句“该 tag 无已验证的固定版本安装路径，按默认分支（main）更新。”未包含由 manifest 推导的 6 个 role plugin 数量。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=d402cefd8db978c0d6fa0c8a95730b6808ddd136a3f09e75cc22b394c59471a4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 标题和升级首句、Kimi 省略符合要求，但错误保留 Codex 小节，且对无固定版本路径的表述及收尾句不完全符合断言。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=734c4a4cb7e543db5091d9f1c4a08014e2d017a93f5c1b82e54e15f916eb8fba; fixture_sha256=17e20791a9c9288907fb214989bbc6378e7d64a98732f68a5c493285ff25f933; output_sha256=aefa6f2f023ca25cc46ec71b3f946c1494121684b0123a87eac2ba013186a8ab; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了裸版本式标题，并保留 Claude、Codex、Kimi 三个平台说明；未按历史 tag 平台限制省略相关小节。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未省略不支持 TARGET_TAG 的 Codex 小节。
- with_skill 对无已验证固定版本路径的说明不符合要求，且升级说明收尾句未包含 6 个 role plugin 数量。
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

# Eval Result: eval-008-marketplace-historical-tag-limit-upgrade-note

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-008-marketplace-historical-tag-limit-upgrade-note`
- Test case: `marketplace 历史 tag 能力不完整时的条件省略`
- Prompt:

> 请根据 `release-package.md`、`docs/site/release-notes/v0.9.0.md` 和 `github-evidence.md` 准备 GitHub Release 预览。本仓库是 dev-agent-skills marketplace 宿主，历史 tag v0.9.0 的插件内容见 `.claude-plugin/marketplace.json` 与 `.codex/INSTALL.md`，该版本没有 `.kimi-plugin/plugin.json`。

- Expected output:

> 标题为 `v0.9.0 - {主题概述}` 强格式；升级说明按固定结构呈现：简述句按 v0.9.0 manifest 推导（6 个 role plugin 均更新到 `v0.9.0`）；`### Claude Code` 小节省略并在正文说明平台限制（/plugin update 无版本 pin，durable 正文无法承诺 v0.9.0 固定安装）；`### Codex` 小节省略（该版本 .codex/INSTALL.md 不含 TARGET_TAG 安装支持）；`### Kimi Code` 小节省略（该版本无 .kimi-plugin/plugin.json）；该 tag 无已验证固定版本安装路径，不得推荐不可用替代路径，收尾句包含由历史 manifest 推导的 6 个 plugin 并明确按默认分支（main）更新、不得承诺同步该 tag 能力；不生成空壳小节或臆造安装命令。

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `6e0fc2447801f563813c5383f41902c94ab8b2ed2718e0b1475207eeab32d777`（5 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL**
- Overall result: FAIL
- With-skill summary: github-release-gen 已实际加载（status skill_load_hits=2；transcript 首先读取 SKILL.md 及其 references）。with_skill 仅生成预览，快照无写入，但升级说明未按历史 tag 能力条件省略相关小节。未发现读取评测脚手架泄漏。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

github-release-gen 已实际加载（status skill_load_hits=2；transcript 首先读取 SKILL.md 及其 references）。with_skill 仅生成预览，快照无写入，但升级说明未按历史 tag 能力条件省略相关小节。未发现读取评测脚手架泄漏。

## Without-Skill Baseline

without_skill 未加载 skill（skill_load_hits=0），仅作为对照；其 candidate.md 只报告已生成预览及包含三宿主限制，未改变 with_skill 判定。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `title_matches_marketplace_format` | **PASS** | with_skill candidate 的预览标题为 `v0.9.0 - 失败消息重试与统一附件模型兼容`，符合非空主题概述格式。 | without_skill candidate.md 仅报告生成预览，未提供可核验的标题正文。 |
| `upgrade_note_first_sentence_derived` | **PASS** | with_skill 正文 `## 升级说明` 后首段为“无破坏性变更，也没有新增 plugin。6 个 role plugin 均更新到 `v0.9.0`。”；fixture 的 marketplace.json 注册了 6 个 plugin，且 release note 明确为 6 个 role plugin。 | without_skill candidate.md 仅声称包含六个 plugin 清单，未提供首句以供核验。 |
| `claude_section_omitted_with_platform_limit` | **FAIL** | with_skill 正文实际包含 `### Claude Code` 小节；该 assertion 要求历史 tag 重跑时省略该小节，并在正文说明限制。虽然正文提到 `/plugin update` 无版本 pin，也声明无已验证固定版本路径，但小节未省略。 | without_skill candidate.md 报告包含 Claude 历史版本升级限制，但未提供正文结构细节。 |
| `codex_section_omitted_without_target_tag_support` | **FAIL** | with_skill 正文实际包含 `### Codex` 小节，且加入了 `Fetch and follow instructions from https://raw.githubusercontent.com/.../refs/tags/v0.9.0/.codex/INSTALL.md` 指令；fixture 与 trace 已确认目标 `.codex/INSTALL.md` 不含 TARGET_TAG 支持，断言要求省略小节且不得臆造该安装指令。 | without_skill candidate.md 报告包含 Codex 历史版本限制，但未提供正文结构细节。 |
| `kimi_section_omitted_without_plugin_json` | **FAIL** | with_skill 正文实际包含 `### Kimi Code` 小节。虽然其中如实说明无 `.kimi-plugin/plugin.json`、无 Kimi plugin 入口，但断言要求目标 tag 缺少 manifest 时省略该小节，不生成空壳小节。trace 第 15 行也显示 Kimi 文件 absent。 | without_skill candidate.md 报告包含 Kimi 历史版本限制，但未提供正文结构细节。 |
| `closing_sentence_derived` | **FAIL** | with_skill 正文虽写有“该 tag 无已验证的固定版本安装路径”，但收尾句未包含由 manifest 推导的 6 个 role plugin 数量，也未明确按默认分支 `main` 更新；因此没有满足要求的 closing sentence。 | without_skill candidate.md 仅报告包含六个 plugin 清单，未提供收尾句正文。 |

## Failures

- with_skill 实际加载了目标 skill，但违反了历史 marketplace 能力不完整时的条件省略要求：Claude、Codex、Kimi 三个小节均被保留。
- with_skill 臆造了目标 tag 的 Codex fetch 安装指令，尽管 trace 与 fixture 已确认该版本仅有不支持 TARGET_TAG 的普通安装文件。
- with_skill 缺少要求的、包含 6 个 plugin 且明确按默认分支 main 更新的收尾句。

## Not Exercised

- 无；本轮覆盖全部 assertions。

## Next Steps

- 重生成升级说明：省略 Claude Code、Codex、Kimi 三个小节；正文集中说明无已验证固定版本安装路径，并以 6 个 role plugin 和默认分支 main 完成收尾。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `141.175s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `112.661s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `78.547s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
