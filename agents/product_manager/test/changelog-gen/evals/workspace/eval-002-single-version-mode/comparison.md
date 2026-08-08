# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-002-single-version-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-002-single-version-mode`.
- Fixture SHA-256: `835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88`
- Prompt SHA-256: `d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `53f035563de038125d09b7a8997f87e900d099e00223f427a7c690e11ebbe449`
- Skill overlay SHA-256: `9534a5bf71391ac48cfd6a48ca8f80e93da520d6ea9d2026741fd864da0cb720`
- Judge schema SHA-256: `609660421781976ec561327c947a31da6f7d421bc63e99d2f3f00692dcdf763a`
- Eval definition SHA-256: `e34f2dddfabba5be49382d984bac6785776f7fb5fa22e37126ed32d1f44a81df`
- Metadata SHA-256: `814184c8bd7a959b3f0695c85bef4dd34c73bd316a08d00ccc354207f37fabc9`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `v_version_yyyy_mm_dd` | PASS | with_skill 文件包含 `## [v0.120.2] - 2026-08-05`。 |
| `release_tag` | PASS | with_skill 文件版本号为 `v0.120.2`，与 fixture 的 target_release.tagName 一致。 |
| `pr_conventional_commit` | PASS | PR #300、#301、#302 的标题均已去除 `fix(client):`、`docs:`、`feat!:` 前缀。 |
| `breaking_change_breaking` | PASS | PR #302 条目带有 `⚠️ **BREAKING**` 标记。 |
| `section` | PASS | 输出仅包含有内容的 `Changed` 和 `Fixed` sections。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031; fixture_sha256=835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88; output_sha256=fe04769f803c1ba7bfd404232032681cfca22f7ec0ad5f0c3af897bbc37afabc; snapshot_sha256=c165a4a9a2c9ccd41858db324fda5280162727a78e510a626368977497b6a8d3
- Behavior: 成功写入包含正确版本、日期、全部 PR、清洗后标题和 breaking 标记的 changelog 文件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031; fixture_sha256=835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88; output_sha256=88091684ce05bada07c92db609134c52fff730aff45a278b21afb8ac4c523a71; snapshot_sha256=e78bf12223329d28baed7861f0bd439c62c987071972ce91e1da976d23751b60
- Behavior: 也写入了 changelog，但版本标题缺少 v 前缀，breaking change 未使用要求的 ⚠️ BREAKING 前缀。
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
- Skill: `changelog-gen`
- Eval: `eval-002-single-version-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-002-single-version-mode`.
- Fixture SHA-256: `835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88`
- Prompt SHA-256: `d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `53f035563de038125d09b7a8997f87e900d099e00223f427a7c690e11ebbe449`
- Skill overlay SHA-256: `9534a5bf71391ac48cfd6a48ca8f80e93da520d6ea9d2026741fd864da0cb720`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e34f2dddfabba5be49382d984bac6785776f7fb5fa22e37126ed32d1f44a81df`
- Metadata SHA-256: `814184c8bd7a959b3f0695c85bef4dd34c73bd316a08d00ccc354207f37fabc9`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `v_version_yyyy_mm_dd` | PASS | with_skill 文件包含 `## [v0.120.2] - 2026-08-05`。 |
| `release_tag` | PASS | 文件版本 `v0.120.2` 与原始证据中的 target_release.tagName `v0.120.2` 匹配。 |
| `pr_conventional_commit` | PASS | 3 个 PR 条目均已去除 conventional commit 前缀，保留了清洗后的可读标题。 |
| `breaking_change_breaking` | PASS | #302 条目以 `⚠️ BREAKING` 标识，且原始证据确认其为 breaking change。 |
| `section` | PASS | 输出仅包含有内容的 Changed 和 Fixed section，且两者均包含条目。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031; fixture_sha256=835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88; output_sha256=f0c21d961231647b838a20290b41f5fe8ccaab0b9e7852a065d0166d95cf00ef; snapshot_sha256=1352f6a5df9976e5b3d3fea7469342d8de4709c675e65dfc26744aeadfe012a6
- Behavior: 生成了符合版本格式、release tag、PR 标题清洗、Breaking 标识和非空 section 要求的 changelog 文件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031; fixture_sha256=835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88; output_sha256=d0d1234f432162fa4b95ca74b97baa24595bef4e0ba8efbe9d35683e770acef3; snapshot_sha256=4d3daf0515be15c244f52f69803b48d14458d5d77c26dfa9b0c5a0bba20550b4
- Behavior: 生成了文件并包含 3 个 PR，但版本标题缺少 v 前缀，Breaking 标识也未使用要求的格式。
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
- Skill: `changelog-gen`
- Eval: `eval-002-single-version-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-002-single-version-mode`.
- Fixture SHA-256: `835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88`
- Prompt SHA-256: `d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `fd6202eb001e4fcc8e818cb01c9c27ec290ab3c4edabd757735bf984bab469a4`
- Skill overlay SHA-256: `b53e1261ebb5c959b0bf29a37559e89f454013b911c855fd491809032b43b267`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e34f2dddfabba5be49382d984bac6785776f7fb5fa22e37126ed32d1f44a81df`
- Metadata SHA-256: `814184c8bd7a959b3f0695c85bef4dd34c73bd316a08d00ccc354207f37fabc9`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `v_version_yyyy_mm_dd` | PASS | With-skill output contains `## [v0.120.2] - 2026-08-05`, matching the required format. |
| `release_tag` | PASS | The output version `v0.120.2` matches the fixture's target release tag `v0.120.2`. |
| `pr_conventional_commit` | PASS | With-skill entries remove conventional-commit prefixes while retaining the meaningful scope in `client:`, and include PR references #300–#302. |
| `breaking_change_breaking` | PASS | PR #302 is rendered with the visible `⚠️ BREAKING` marker, matching the fixture's breaking-change evidence. |
| `section` | PASS | Only populated sections—Added, Changed, and Fixed—are present in the with-skill output. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031; fixture_sha256=835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88; output_sha256=2aa25c2261ba46762630da4a5099430b8121b5a3dabd177bad5f4bebf8cd4daa; snapshot_sha256=e36ba5ceb504c99036333c486ed2f855257d6027ccabeab1fb72c8829738e9bb
- Behavior: Generated the requested changelog with the matching version/date, cleaned PR titles, all three PR references, a breaking-change marker, and only populated sections.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031; fixture_sha256=835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88; output_sha256=c967f6bcaa3efe5c7f44cd9891459d5f66dba189f916feddfaeb473587ade7df; snapshot_sha256=7c0092eb15d8578f2063fe363e0c1232b4f474981c5ff58416f190fb31041657
- Behavior: Generated the requested file and included all three PRs, but omitted the required v prefix, used a generic breaking-change label, and did not visibly apply the requested section format.
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
- Skill: `changelog-gen`
- Eval: `eval-002-single-version-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-002-single-version-mode`.
- Fixture SHA-256: `835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88`
- Prompt SHA-256: `d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `fd6202eb001e4fcc8e818cb01c9c27ec290ab3c4edabd757735bf984bab469a4`
- Skill overlay SHA-256: `b53e1261ebb5c959b0bf29a37559e89f454013b911c855fd491809032b43b267`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e34f2dddfabba5be49382d984bac6785776f7fb5fa22e37126ed32d1f44a81df`
- Metadata SHA-256: `814184c8bd7a959b3f0695c85bef4dd34c73bd316a08d00ccc354207f37fabc9`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `v_version_yyyy_mm_dd` | PASS | with_skill 文件包含 `## [v0.120.2] - 2026-08-05`。 |
| `release_tag` | PASS | 版本号 `v0.120.2` 与 fixture 的实际 release tag `v0.120.2` 匹配。 |
| `pr_conventional_commit` | FAIL | PR #300 条目仍显示 `**client:** Handle streaming reconnect`，未完全去掉 conventional commit 的 scope 前缀；#301 和 #302 已清洗。 |
| `breaking_change_breaking` | PASS | PR #302 条目带有 `⚠️ BREAKING` 前缀。 |
| `section` | PASS | 输出中的 Added、Changed、Fixed 均有内容，未输出空 section。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031; fixture_sha256=835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88; output_sha256=8918eeff11ee9c1e12a66f46bb469afd99896b60e169e8e0a219f3dab631d0e0; snapshot_sha256=c7abcd23ff8ada6652e7b20cece2dfc9c938e9defe5147bfb24d64f9213468c6
- Behavior: 生成并写入目标文件，版本和日期正确，包含全部 3 个 PR，标注 breaking change；PR #300 保留了 client scope 前缀。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031; fixture_sha256=835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88; output_sha256=1db3d79a3d52672068755102b15cd5ddeb0c6c88eacb73334f9d57147188e7f6; snapshot_sha256=5aad754f2b0e07bff4f3362e14b4ea0a51e4eea82384254f3c4261a670c71b6a
- Behavior: 生成了目标文件并包含全部 PR 引用，但版本标题缺少 v 前缀，breaking 标记未使用要求的格式。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 的 PR #300 标题未完全去掉 conventional commit 前缀中的 scope。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-002-single-version-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-002-single-version-mode`.
- Fixture SHA-256: `835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88`
- Prompt SHA-256: `d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `281e1b5c19a67eed1e87d8548e15e7ab23a90d7de9e0bd112a29df45200426a3`
- Skill overlay SHA-256: `f4e3f318f95aeaf018d947cb5144bbc03198d0d62d802018a4946522adbf8065`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e34f2dddfabba5be49382d984bac6785776f7fb5fa22e37126ed32d1f44a81df`
- Metadata SHA-256: `814184c8bd7a959b3f0695c85bef4dd34c73bd316a08d00ccc354207f37fabc9`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `v_version_yyyy_mm_dd` | PASS | With-skill output contains `## [v0.120.2] - 2026-08-05`, matching the required format. |
| `release_tag` | PASS | With-skill version `v0.120.2` matches the fixture's target release tag. |
| `pr_conventional_commit` | PASS | All three PR titles are cleaned of conventional-commit prefixes while retaining their meaningful titles/scopes. |
| `breaking_change_breaking` | PASS | PR #302 is marked with the required `⚠️ BREAKING:` prefix. |
| `section` | PASS | The output includes only populated sections: Added, Changed, and Fixed; all correspond to fixture PRs. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031; fixture_sha256=835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88; output_sha256=6c6a610ca1200baaea43ac11b6db2ddf55550067022e8acc26154bb6a37f56a8; snapshot_sha256=6356441170f8c5b437fe910294dbd7cc97c9ab08ed63a4901eae87bc15670346
- Behavior: Generated the expected changelog file with the correct version/date, cleaned PR titles, breaking-change marker, and populated sections.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d5b776b3a900ef058dd8e13d5ff0673d61e60850257603b59fa1902a93991031; fixture_sha256=835e6d91014bb254ac4027a75b2b94fcac8cc02efcf4ee8832fb73ee44824c88; output_sha256=e05bab249e4233429a0ca970266f94a7d6cce466f0873385f33e306290fa5b16; snapshot_sha256=e1d9814563db2bea61ac4bc462a9e971934011ff8b0aea714184dc1b0122b905
- Behavior: Generated the changelog file and included PRs #300–#302, but omitted the required v-prefixed header and breaking-change marker.
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
- Skill: `changelog-gen`
- Eval: `eval-002-single-version-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-002-single-version-mode`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `bd018ad305c5f305a6daed7fd9f17ae486593c50dc80e5c2aa3a74b95671bf30`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3dfcf246dc4057e8231ee4e2380b4525eeecf840a484daf60bd4e990283d5e5e`
- Skill overlay SHA-256: `5c214a0a2c2365016d6b3bafaa3e6cd9bb33067b007f4407a0b78fe50c4ba935`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `4fbc72fdf98154f7c2dd882f093beffcc404677e79487aa94518bc287dcc4e70`
- Metadata SHA-256: `0261b537a122aab27112048b46542c55dcea0510f7dd974807fe61e039d9308d`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `v_version_yyyy_mm_dd` | PASS | with_skill 文件包含 `## [v0.120.2] - 2026-07-28`。 |
| `release_tag` | PASS | 版本 `v0.120.2` 与输出引用的 release tag `v0.120.2` 一致。 |
| `pr_conventional_commit` | FAIL | PR 条目仍包含 `**mcp:**` 前缀，未完全清洗 conventional commit 前缀。 |
| `breaking_change_breaking` | PASS | with_skill 输出无 breaking change 条目，因此不存在未添加 `⚠️ BREAKING` 前缀的 breaking change。 |
| `section` | PASS | 输出仅包含有内容的 `Fixed` section。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bd018ad305c5f305a6daed7fd9f17ae486593c50dc80e5c2aa3a74b95671bf30; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=365a478a03d030917ae289e7ab726f76beff21cae225eb3fcf216c9607a272c1; snapshot_sha256=a86142e53d5eff63397b9cb820f5913caeda80df11fe6805954bc08638d2b3db
- Behavior: 生成了 v0.120.2 changelog，包含日期、release 引用、Fixed section 和 PR #300。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=bd018ad305c5f305a6daed7fd9f17ae486593c50dc80e5c2aa3a74b95671bf30; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=6d51e35c792280ae79e5f62b8004db6c1d8e045584eb547358ec51ca0b85155b; snapshot_sha256=0992d862f20d10fec88966111d8644e16cf1e120c774033712380dba84fe08e8
- Behavior: 生成了 changelog 文件并包含 Fixed 条目和 PR #300，但版本标题缺少 v 前缀。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- pr_conventional_commit：PR 条目保留了 `**mcp:**` 前缀。
- Next: 移除 PR 条目中的 `**mcp:**` conventional commit 前缀。

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

# Eval Result: eval-002-single-version-mode

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-002-single-version-mode`
- Test case: `single-version-mode`
- Prompt:

> 在 https://github.com/anthropics/anthropic-sdk-python 仓库，帮我生成最新 release 版本的 changelog 条目，使用 Keep a Changelog 格式，包含该版本对应的所有 PR 引用，并写入 docs/changelog/changelog-v{version}.md。

- Expected output:

> 生成最新 release tag 的版本块，格式为 ## [v{VERSION}] - YYYY-MM-DD，包含该版本窗口内的 PR，分组写入，每条带 PR 链接，并写入 docs/changelog/changelog-v{version}.md

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`（0 个可见文件；两侧逐字节一致）。
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
- With-skill summary: changelog-gen 实际加载（skill_load_hits=2，transcript item_1 读取 SKILL.md），成功写入目标版本文件；GitHub 实时数据查询受认证/网络失败影响。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

changelog-gen 实际加载（skill_load_hits=2，transcript item_1 读取 SKILL.md），成功写入目标版本文件；GitHub 实时数据查询受认证/网络失败影响。

## Without-Skill Baseline

对照侧未加载 skill（skill_load_hits=0），但也写入了目标文件；仅作基线，不影响 with_skill 判定。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `v_version_yyyy_mm_dd` | **PASS** | trace item_16 显示文件内容含 `## [v0.120.2] - 2026-07-28`，candidate.md 也报告相同版本和日期。 | without_skill 文件为 `## [0.120.2] - 2026-07-28`，缺少 v 前缀。 |
| `release_tag` | **NOT EXERCISED** | with_skill 尝试了 `gh release list`（trace item_4），但因未认证失败；随后 `git ls-remote` 因无法解析 github.com 失败（item_5）。candidate 的 release 声明没有可用实时证据或 fixture 支撑。 | without_skill 也报告 v0.120.2，但其外部 release 查询没有可用结果。 |
| `pr_conventional_commit` | **NOT EXERCISED** | PR #300 的实时元数据/原始标题不可用：trace item_4 认证失败、item_5 网络失败，web_search 项无返回内容；因此无法验证是否确实清除了 conventional commit 前缀。 | without_skill 输出 `Support MCP SDK v2 alongside v1`，表面上已清洗前缀，但无可验证原始 PR 标题。 |
| `breaking_change_breaking` | **NOT EXERCISED** | 无法取得 PR 标题和 body，不能判断该版本是否存在 breaking change；trace 中没有可用的 PR 元数据结果。 | without_skill 未添加 `⚠️ BREAKING`，但同样无法确认条件是否触发。 |
| `section` | **PASS** | trace item_16 展示写入内容仅包含有条目的 `### Fixed` section，且该 section 下有 PR #300 条目，没有空 section；after-snapshot 证明目标文件已写入。 | without_skill 也只输出有内容的 `### Fixed` section。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- release_tag
- pr_conventional_commit
- breaking_change_breaking

## Next Steps

- 保留当前回归覆盖；目标 skill、fixture 或 assertion 契约变化时重新执行 fresh paired validation。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `100.176s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `62.473s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `62.677s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
