# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-003-github-release-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720` from `agents/docs/test/release-notes-gen/evals/workspace/eval-003-github-release-boundary`.
- Fixture SHA-256: `b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720`
- Prompt SHA-256: `761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b7f7292c266a0e83e45fc11a264c0b52188a05a92b94c912c4a7b6c5c35058d2`
- Skill overlay SHA-256: `fcc8b19cc83a08b5f5e64f8b15695aa80b045962a63cbf1717889ea116dc31cc`
- Judge schema SHA-256: `b3d43ca97793c6a0f8faf70ea92518e7709890635e7a921da0c1ddde071762ab`
- Eval definition SHA-256: `05f16fbca1905a6bf2d3e5279f6310a7d3001480023c03eb422e696627b86d5d`
- Metadata SHA-256: `79c5171e280a55a386cc65ee64ce2254d37bdb1b11edec578be748642efe98aa`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | with_skill 明确识别缺少 docs/site/release-notes/ Release Notes 基础，并将页面状态置为 blocked，未进入页面生成流程。 |
| `keeps_site_zero_diff_before_bootstrap` | PASS | with_skill 的 git_evidence 显示 HEAD、分支、refs、工作树和索引均无变化；git_status 与 git_diff 均为空。 |
| `hands_missing_foundation_to_bootstrap` | PASS | 输出将缺失基础交给 docs-site-bootstrap 初始化，未交给 docs audit、GitHub Release owner，也未自行继续。 |
| `preserves_release_chain_and_external_zero_writes` | PASS | 输出明确 tag 与 GitHub Release 均未创建，并等待 docs-audit 返回 ready_for_tag；git_evidence 的 ref_delta、result_diffs 和状态均为空。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720; output_sha256=c795bdddf39289886240bbe1cce87106225985318f6d9fbe574aae93d646e2a4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别 Release Notes 基础缺失，阻塞生成并完成正确的 bootstrap handoff；保持站内、Git 和外部发布链零写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720; output_sha256=bbf8e599adb4e0da8586193d4ccc1f44d8a0693ccc569f6962ee0981f1b09ec1; snapshot_sha256=39b391f82c97b7045b03f4e7cd72f06c05a987b788fdb40e776adb0c7dcbb3a5
- Behavior: 错误地创建站内 Release Notes、元数据和提交，并创建 v1.0.0 tag；仅未创建 GitHub Release。
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
- Skill: `release-notes-gen`
- Eval: `eval-003-github-release-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720` from `agents/docs/test/release-notes-gen/evals/workspace/eval-003-github-release-boundary`.
- Fixture SHA-256: `b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720`
- Prompt SHA-256: `761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b7f7292c266a0e83e45fc11a264c0b52188a05a92b94c912c4a7b6c5c35058d2`
- Skill overlay SHA-256: `fcc8b19cc83a08b5f5e64f8b15695aa80b045962a63cbf1717889ea116dc31cc`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `05f16fbca1905a6bf2d3e5279f6310a7d3001480023c03eb422e696627b86d5d`
- Metadata SHA-256: `79c5171e280a55a386cc65ee64ce2254d37bdb1b11edec578be748642efe98aa`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | with_skill 明确识别宿主缺少 docs/site/release-notes/ 及其规范，并将其作为进入生成流程前的阻塞；fixture 中确无该目录。 |
| `keeps_site_zero_diff_before_bootstrap` | PASS | with_skill 输出未生成 Release Notes、未修改 metadata/index/navigation；其 workspace_manifest 与 fixture 基线一致，git_status 和 git_diff 均为空。 |
| `hands_missing_foundation_to_bootstrap` | PASS | with_skill 明确给出 blocked → docs-site-bootstrap，说明缺失 foundation，未转交给 audit、GitHub Release owner 或自行继续。 |
| `preserves_release_chain_and_external_zero_writes` | PASS | with_skill 明确未准备或创建 GitHub Release/tag，并要求等待站点基础与 docs-audit 的 ready_for_tag；锁定证据显示无写入或引用变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720; output_sha256=4a61c0616b8369f30db3a4264ec4b7194f79a2995a6be643754c6ba79f107e43; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别缺失的 Release Notes foundation，阻塞并交接给 docs-site-bootstrap；保持工作区与站点文件零写入，未推进 tag 或 GitHub Release。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720; output_sha256=0803aa2c4c5165442e053c8910702ccb50264a5b3eb37837df2cf81e33356af5; snapshot_sha256=660fbabe1b5df61401a73ac4accc7aafe09546ccd0212326c51c9eb281a5d33d
- Behavior: 创建了站内 Release Notes、metadata、提交和 v1.0.0 tag；GitHub Release 因环境限制未创建，违反 bootstrap 前零差异与外部发布链约束。
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
- Skill: `release-notes-gen`
- Eval: `eval-003-github-release-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720` from `agents/docs/test/release-notes-gen/evals/workspace/eval-003-github-release-boundary`.
- Fixture SHA-256: `b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720`
- Prompt SHA-256: `761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2432b0a8b94e9e5b987302b22f20b3a68797aef99cb1f7535f80c5f6d550ca58`
- Skill overlay SHA-256: `b8a032f2e0b3c1612e4ecd4d8c0404ffabac105e349deced7271302364bee3fd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `05f16fbca1905a6bf2d3e5279f6310a7d3001480023c03eb422e696627b86d5d`
- Metadata SHA-256: `cc603314c84acffcc044d1983ddad5ccbf550b74f01ff0d4a84abd79a152693b`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | With_skill identifies the missing release-notes foundation, including the directory and index/metadata basis, and blocks page generation. |
| `keeps_site_zero_diff_before_bootstrap` | PASS | With_skill reports no site writes, no metadata/index/navigation changes, and empty git status/diff; fixture confirms no Release Notes foundation exists. |
| `hands_missing_foundation_to_bootstrap` | PASS | With_skill gives a blocked handoff to the Docs-site bootstrap owner, identifies the host/current repository and missing foundation, and defers further page work. |
| `preserves_release_chain_and_external_zero_writes` | PASS | With_skill explicitly reports no GitHub Release or v1.0.0 tag creation and requires bootstrap followed by documentation audit before downstream release handling. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720; output_sha256=d84349e760e0589ddeb917485404ffc764088f04a170d09ef8fae2c435f192a2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly stopped at the missing Release Notes foundation, preserved zero diff and external zero writes, and handed off bootstrap.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=b6c1fa26768d6c9af6d59884eea70e6437cb9644150d6247f56b09929c6c2720; output_sha256=b2475ea882b9429f8a361f15c7bd3aa5089184a4fb4d040b80e3528c6c002280; snapshot_sha256=4d75af9f03af697381f55ec36d0099bcd1c7f8024623201b89758dde8d0bc9bb
- Behavior: Incorrectly generated release material, committed changes, and created a local tag despite the missing site foundation.
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
- Skill: `release-notes-gen`
- Eval: `eval-003-github-release-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `57ad6ab7a7bd756cc1be44042bd4e749157f6514a8971f70e9cca76044d85d23` from `agents/docs/test/release-notes-gen/evals/workspace/eval-003-github-release-boundary`.
- Fixture SHA-256: `57ad6ab7a7bd756cc1be44042bd4e749157f6514a8971f70e9cca76044d85d23`
- Prompt SHA-256: `761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2432b0a8b94e9e5b987302b22f20b3a68797aef99cb1f7535f80c5f6d550ca58`
- Skill overlay SHA-256: `b8a032f2e0b3c1612e4ecd4d8c0404ffabac105e349deced7271302364bee3fd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `05f16fbca1905a6bf2d3e5279f6310a7d3001480023c03eb422e696627b86d5d`
- Metadata SHA-256: `cc603314c84acffcc044d1983ddad5ccbf550b74f01ff0d4a84abd79a152693b`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | with_skill 明确指出缺少 docs/site/release-notes、编写规范和版本页，因此未进入页面生成。 |
| `keeps_site_zero_diff_before_bootstrap` | PASS | with_skill 声明未创建页面、metadata/index，工作区无改动；git evidence 也显示无 diff、无 untracked 文件。 |
| `hands_missing_foundation_to_bootstrap` | FAIL | with_skill 提到 docs-site-bootstrap，但未明确交接给正式文档站 Docs owner，也未携带 host repository；仅提出需要授权初始化。 |
| `preserves_release_chain_and_external_zero_writes` | NOT_EXERCISED | 当前未创建 tag 或 GitHub Release，且 git evidence 显示无 ref 变化；但 foundation 补齐后的正文确认、站内检查和 pre-tag 审计尚未发生，无法评估后续链路。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=57ad6ab7a7bd756cc1be44042bd4e749157f6514a8971f70e9cca76044d85d23; output_sha256=069e2601e09a4eba8396ee2d276bf6981320630d94d3bdf75b6a733ac1c6b24c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别 Release Notes foundation 缺失并阻塞发布，保持工作区和 Git 引用不变；但未明确完成带 host 的 Docs owner blocked handoff。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=57ad6ab7a7bd756cc1be44042bd4e749157f6514a8971f70e9cca76044d85d23; output_sha256=9aa07fbdf520a1aa1ff061bff27b479678d3bb7131125958bcfc1e39625964de; snapshot_sha256=e6e9d8d5f8c643b0dc0742e6b88913944af69fcf1bb73b80b8201426df702bc9
- Behavior: 错误地生成站内页面、Release 正文和 handoff，并创建本地 annotated tag；仅因缺少远程和 gh CLI 未创建远端 Release。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确将缺失 foundation 连同 host repository 交接给正式文档站 Docs owner。
- Next: 由正式文档站 Docs owner 初始化 Release Notes foundation，并明确记录 host repository。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-003-github-release-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `57ad6ab7a7bd756cc1be44042bd4e749157f6514a8971f70e9cca76044d85d23` from `agents/docs/test/release-notes-gen/evals/workspace/eval-003-github-release-boundary`.
- Fixture SHA-256: `57ad6ab7a7bd756cc1be44042bd4e749157f6514a8971f70e9cca76044d85d23`
- Prompt SHA-256: `761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `299c765e24bed3d47cd5f1165cb4e7dae973e90fb9c91e1e5e35950ac2fddd9f`
- Skill overlay SHA-256: `62aaaf9c8c05eac4d9d569c35ab001e055f2ecdc527f1e0c77f6bdc4eedf1246`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `05f16fbca1905a6bf2d3e5279f6310a7d3001480023c03eb422e696627b86d5d`
- Metadata SHA-256: `cc603314c84acffcc044d1983ddad5ccbf550b74f01ff0d4a84abd79a152693b`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | with_skill 明确指出缺少 docs/site/release-notes、编写规范、.meta/releases.json 和 Release Notes index，并说明需先初始化。 |
| `keeps_site_zero_diff_before_bootstrap` | PASS | with_skill 明确声明未创建站内 Release Notes、未产生文件变更；其 manifest 也未出现新增站点文件。 |
| `hands_missing_foundation_to_bootstrap` | FAIL | 输出仅称当前 handoff 为 blocked，未明确交接给负责正式文档站初始化的 Docs owner，也未携带 host 信息。 |
| `preserves_release_chain_and_external_zero_writes` | FAIL | 输出确认未创建 GitHub Release 或 tag，但未说明 foundation 补齐后需重新进行正文确认、站内检查和 pre-tag 审计，也未明确当前 release execution 未获授权。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=57ad6ab7a7bd756cc1be44042bd4e749157f6514a8971f70e9cca76044d85d23; output_sha256=cae17608e9cebb952673c64ee7b3f87bb9d08a3bbaac4f8ad4a836fa0ed2d9fb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别站点基础缺失并保持零写入、零 tag，但未完整表达 Docs owner 交接与后续发布链约束。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=57ad6ab7a7bd756cc1be44042bd4e749157f6514a8971f70e9cca76044d85d23; output_sha256=b30d26a49453b7a64c6cec8c337fe12f08859973aa2f60381aaf4d267735effa; snapshot_sha256=c1868fc59518a464973eb05fefde41742b3282725ebab8b86f5298049c22e1fb
- Behavior: 错误地创建了站内 Release Notes、元数据、提交和 v1.0.0 tag；仅未创建 GitHub Release。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- hands_missing_foundation_to_bootstrap
- preserves_release_chain_and_external_zero_writes
- Next: 明确将 blocked handoff 交给负责正式文档站初始化的 Docs owner，并携带当前 host 与缺失 foundation 清单。
- Next: 明确 foundation 补齐后需重新进入正文确认、站内检查和 pre-tag 审计，且当前 release execution 未授权。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-003-github-release-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `57ad6ab7a7bd756cc1be44042bd4e749157f6514a8971f70e9cca76044d85d23` from `agents/docs/test/release-notes-gen/evals/workspace/eval-003-github-release-boundary`.
- Fixture SHA-256: `57ad6ab7a7bd756cc1be44042bd4e749157f6514a8971f70e9cca76044d85d23`
- Prompt SHA-256: `761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2da7831c1e3b626979a3601984870e16015610b54d1ff8f08ff8c14d15f812ca`
- Skill overlay SHA-256: `d552bdbf1aa95d384d7132b02e78e69678457f53a15c3f49ddfae00094ce8ee0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `05f16fbca1905a6bf2d3e5279f6310a7d3001480023c03eb422e696627b86d5d`
- Metadata SHA-256: `cc603314c84acffcc044d1983ddad5ccbf550b74f01ff0d4a84abd79a152693b`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | with_skill 输出识别 docs/site/release-notes/、README.md、.meta/releases.json 缺失，并指出 release-notes 规约与 docs-audit 门禁导致无法进入生成流程；fixture 也确认该目录和元数据不存在。 |
| `keeps_site_zero_diff_before_bootstrap` | PASS | with_skill 明确声明工作区无文件变更；其 git_status 与 git_diff 均为空，符合 bootstrap 前保持 pristine 的要求。 |
| `hands_missing_foundation_to_bootstrap` | FAIL | with_skill 指向 docs-site-bootstrap，但未明确交接给 Docs owner，也未携带 release-entry.md 中的 host_repository（current product repository）及完整缺失 foundation；同时未明确排除 docs audit owner 和 GitHub Release owner。 |
| `preserves_release_chain_and_external_zero_writes` | FAIL | with_skill 明确 tag 和 GitHub Release 未创建，但未完整说明不准备、编辑或发布 Release、当前 release execution 未授权，以及 foundation 补齐后需重新进行正文确认和站内检查；只概述了后续生成、审计和创建流程。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=57ad6ab7a7bd756cc1be44042bd4e749157f6514a8971f70e9cca76044d85d23; output_sha256=c9eae98eadfd7ad48622e76bccb8fcfed586e9b79156b78c04fef7c2c2d994b9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别站点基础缺失并保持零写入、未创建 tag 或 GitHub Release，但交接信息和发布链约束说明不完整。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=761d6ada5782aed911f08ad61db425bc070c8bdb36e85c9be9e952ce71ac3d5e; fixture_sha256=57ad6ab7a7bd756cc1be44042bd4e749157f6514a8971f70e9cca76044d85d23; output_sha256=29dede32dac131e64899679166059191876b6422ecbca9ce0ca0c1e82d00006f; snapshot_sha256=5c3bc5968c018cd59ea2b47ebe1c537c392f096f7a75cf47f00e8fb52feb7600
- Behavior: 错误地生成站内页面和 Release 草稿，并创建本地 v1.0.0 tag；仅因无 remote/gh 未创建远程 Release。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完整满足 Docs owner blocked handoff 要求。
- with_skill 未完整说明 bootstrap 后的重新确认、站内检查、pre-tag 审计及当前未授权状态。
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

- Skill: `release-notes-generator` → `release-notes-gen`（改名后新入口，已按 #238 于 2026-08-06 fresh 隔离重跑）
- Eval: `eval-003-github-release-boundary`
- Scenario: 缺少 Release Notes writing foundation 的混合站内/外部发布请求
- Review context: self-review convergence

## Test Set / Fixture Version

- Fixture version: `foundation cleanup consistency round-4`
- Validation time: `2026-07-29`（历史轮；本轮 #238 重跑来源见 Latest Result 块）
- Runtime: `tmp/eval-runs/issue-177/self-review/`
- 修正原因：round-3 已移除等价 Release Notes 契约与 surfaces，但 `execution_cleanup` 没有覆盖被删除的 Release Notes 目录、release metadata 和可执行测试；复用 scratch 时可能被旧产物重新污染。
- 本轮补齐 cleanup 后，两侧使用同一 prompt 与独立 pristine fixture；without-skill 未读取目标 skill、Docs Agent README、eval metadata、assertions、with-skill 输出、旧 comparison 或历史 round，独立 judge 也未读取旧 comparison。

## Latest Result

- Behavior result: `PASS`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
- Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | FAIL | with_skill 明确指出 `docs/site/release-notes/`、编写规范、索引和 `.meta/releases.json` 不存在，并阻止初始化；without_skill 直接报告已完成版本说明。 |
| `keeps_site_zero_diff_before_bootstrap` | PASS | FAIL | with_skill 工作区没有版本页、`.meta` 或其他初始化产物；without_skill 实际新增 `docs/site/release-notes/v1.0.0.md`、`.meta/releases.json` 和 `.meta/release-handoff.json`。 |
| `hands_missing_foundation_to_bootstrap` | PASS | FAIL | with_skill 明确说明需交给 `docs-site-bootstrap`；without_skill 未阻塞交接，而是继续生成正文、元数据和交接文件。 |
| `preserves_release_chain_and_external_zero_writes` | PASS | FAIL | with_skill 明确未创建 GitHub Release 或 `v1.0.0` tag，并说明当前未授权发布执行；without_skill 虽未创建 tag/Release，但已提前准备站内发布产物，且未说明 foundation 补齐后需重新确认、检查和审计。 |

未满足断言（with/without 任一 FAIL）：``detects_missing_release_notes_foundation``、``keeps_site_zero_diff_before_bootstrap``、``hands_missing_foundation_to_bootstrap``、``preserves_release_chain_and_external_zero_writes``



## Fixture Correction And Discrimination

- 修正后宿主保留正式文档站的其他必要文件，但不存在 `docs/site/release-notes/`、编写规则、index、release metadata、相邻版本页或等价可执行契约。
- 通用脚手架仅拒绝生成 Release Notes 并指向专用 skill，不提供正文、frontmatter、metadata 或 index 写作规则，因此不构成等价 foundation。
- `execution_cleanup` 现在覆盖整个 `docs/site/release-notes`、`docs/site/.meta/releases.json` 与 `docs/site/scripts/__tests__/release-notes.test.mjs`，防止旧 runtime 产物伪造 foundation。
- with-skill 应用 foundation gate 后停止；baseline 自行推断规则并创建 Release Notes surfaces，重新形成明确区分。

## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `detects_missing_release_notes_foundation` | PASS | FAIL | with-skill 识别空目录及 writing rules/等价契约缺失；baseline 未识别阻塞并继续生成。 |
| `keeps_site_zero_diff_before_bootstrap` | PASS | FAIL | with-skill 的 `docs/site/` 文件 manifest 与源 fixture 完全一致；baseline 新增版本页、index、metadata 与生成物。 |
| `hands_missing_foundation_to_bootstrap` | PASS | FAIL | with-skill blocked 给 `docs-site-bootstrap` 并等待显式初始化授权；baseline 无 bootstrap handoff。 |
| `preserves_release_chain_and_external_zero_writes` | PASS | FAIL | with-skill 保留 bootstrap→Release Notes→checks→pre-tag audit→PM 顺序且不准备外部发布；baseline 跳过 bootstrap 并把自行建立的站内 handoff 宣称为 ready。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 在 site-foundation gate 停止，没有加载内部生成流程。
- 未创建版本页、index、release metadata、导航或 `.generated`；未运行不能证明交付成立的 docs checks。
- 未准备或写入 GitHub Release，未创建或移动 tag；返回携带 host、目标版本、证据边界与缺失 foundation 的 blocked bootstrap handoff。
- Response SHA-256: `2e12af318ce600cda34001d30ac9de7c8a91a65239bd2f693417eff1d8391eec`。

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- baseline 自行创建 `v1.0.0.md` 与 Release Notes index，运行 frontmatter 检查和 public/internal builds，并把站内 pre-tag handoff 描述为已完成；它没有修改 `.meta/releases.json`。
- 它未识别 bootstrap gate，也未保留正文重新确认、站内检查与 pre-tag audit 的完整前置链。
- Response SHA-256: `a9ed33574b0b964611a2bb8e88723c0ea1620f79261b4a2f05a80aa67850c0df`。

## Failures And Iterations
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Round 1：with-skill 4/4、baseline 4/4；prompt/fixture 泄漏导致无区分度。
- Round 2：with-skill 4/4、baseline 0/4，但 fixture 保留等价 Release Notes 契约，场景判定失真。
- Round 3：修剪等价契约后 with-skill 4/4、baseline 0/4；Behavior PASS、Coverage FULL，场景与协议一致。
- Round 4：补齐删除 surface 的 cleanup 后重新 fresh 成对验证；with-skill 4/4、baseline 0/4，Behavior PASS、Coverage FULL，独立 judge 确认区分度保持。
- 基础设施失败：none。runtime 未保留 lane transcript、显式读取清单或结构化命令日志，降低读取边界的可审计性，但 workspace diff、响应和 baseline 构建产物足以覆盖本轮 4 条行为 assertion。

## Next Steps

- 保持缺少目录、写作规则和等价站点契约时的 bootstrap stop 为回归门禁。

## Runtime Artifact Policy

- `tmp/eval-runs/issue-177/self-review/` 下的 workspace、依赖、页面副本、构建产物、response、handoff 和 judge verdict 不提交。
- 本 `comparison.md` 是本轮唯一 durable eval 结果。
