# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-014-existing-site-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-014-existing-site-deployment-recheck`.
- Fixture SHA-256: `c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79`
- Prompt SHA-256: `1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `4b8356273a26d14ecc55ebfe7a9a2e541bdc3539a06437a0f30fb3a0dc7cbd4b`
- Eval definition SHA-256: `db9d705a02de2df76d9e1b62334995eac21d110dc172ed350d92306793043708`
- Metadata SHA-256: `57de9e366e385164240069213a2870da7cd8d43f7b6ee6621d6856f237ac7e4c`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reports_existing_site_integrated` | PASS | With_skill reports Atlas public/internal builds, Docker targets, Compose services, Helm values, CI matrix, and read-only evidence paths; it also states no deployment or build execution occurred. |
| `detects_partial_variant_coverage` | PASS | With_skill enumerates Orbit public versus internal: internal has a build script but lacks internal Docker target, Compose service, Helm values, and CI matrix, so it cannot be published or deployed and is not complete. |
| `returns_gap_to_pm_read_only` | NOT_EXERCISED | With_skill records that PM handoff evidence is missing and provides a blocked audit handoff while explicitly excluding deployment and documentation changes, but it does not ask the user to confirm PM-agent handoff generation; that later interactive step is not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79; output_sha256=097ec79cedfc4ce5299d6c8772dcee00315169159bc5114cda303a191d24d09f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Accurately performs a read-only configuration review, confirms Atlas coverage, detects Orbit's partial internal coverage, and records the PM handoff gap without mutations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79; output_sha256=54650a16846996a76a1780ba76b7afa96458131ad3c1e9b323d658e2b307964a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a fresh comparison baseline that identifies Orbit's missing internal release path but is less systematic about the full deployment-chain gaps.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Ask whether pm-agent should generate the repo-wide deployment handoff when confirmation is available.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-014-existing-site-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-014-existing-site-deployment-recheck`.
- Fixture SHA-256: `c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79`
- Prompt SHA-256: `1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `4b8356273a26d14ecc55ebfe7a9a2e541bdc3539a06437a0f30fb3a0dc7cbd4b`
- Eval definition SHA-256: `db9d705a02de2df76d9e1b62334995eac21d110dc172ed350d92306793043708`
- Metadata SHA-256: `57de9e366e385164240069213a2870da7cd8d43f7b6ee6621d6856f237ac7e4c`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reports_existing_site_integrated` | PASS | With_skill reports both sites’ current build and startup/deployment configuration, identifies the relevant workflow, package, Dockerfile, Compose, Helm, and auth evidence, and states that no deployment assets were modified. |
| `detects_partial_variant_coverage` | PASS | With_skill correctly distinguishes atlas-portal’s public and internal configuration from orbit-console’s public-only publishable chain, explicitly stating that orbit-console internal is not a publishable variant. |
| `returns_gap_to_pm_read_only` | NOT_EXERCISED | The lane reports the handoff/audit gate as blocked pending confirmation, but no user confirmation is present to exercise the PM-agent handoff question or subsequent handoff generation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79; output_sha256=c08db1e97501697cfe005b878fb56caa56f93bedfdadae84db87338d07f7d7b2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Read-only, evidence-based configuration review; accurately identifies atlas public/internal coverage and orbit public-only coverage, with deployment verification and handoff blocked pending confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79; output_sha256=be64f3403c5ce9633fabcd7071f69660bff3aa01895e634596051f8ea42b5e25; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a broadly accurate comparison review but overstates atlas internal completeness and does not provide the formal blocked handoff framing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Ask whether pm-agent should generate the repo-wide deployment handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-014-existing-site-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-014-existing-site-deployment-recheck`.
- Fixture SHA-256: `c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79`
- Prompt SHA-256: `1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `db9d705a02de2df76d9e1b62334995eac21d110dc172ed350d92306793043708`
- Metadata SHA-256: `57de9e366e385164240069213a2870da7cd8d43f7b6ee6621d6856f237ac7e4c`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reports_existing_site_integrated` | FAIL | with_skill 未复核配置、未报告 integrated，也未列出证据；其自行设置的 handoff 前置条件并非用户要求。 |
| `detects_partial_variant_coverage` | FAIL | with_skill 未枚举两套站点的 Public/Internal 覆盖，也未识别 Orbit Console 为 partial。 |
| `returns_gap_to_pm_read_only` | FAIL | with_skill 未询问是否由 pm-agent 生成 repo-wide deployment handoff；虽声明未修改部署资产，但仅阻塞并要求返回 pm-agent/docs-agent。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79; output_sha256=8b4a63754dcf9ac5a5e6fdf1cc340c1bb6ca501f97d7070dfb66888c61935e37; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 因自行设定的 handoff 前置条件而阻塞，未读取或复核站点配置；声明未修改资产。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79; output_sha256=28db2f511fbabbfe18234df7f9d7a9fd8be13fb573359617273203c68b863d34; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成只读复核，列出 Atlas 的 Public/Internal 与 Orbit 的仅 Public 覆盖，并指出缺口；未修改资产。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未执行用户要求的只读配置复核，导致三个断言要求的用户可见结果均缺失。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-014-existing-site-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-014-existing-site-deployment-recheck`.
- Fixture SHA-256: `c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79`
- Prompt SHA-256: `1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a612d50c32b84c65fad3cad08aad2d416a3a33647abfa1462784c1e58022424b`
- Skill overlay SHA-256: `e55ecf59b3cd8d90a2ed4cf555bed2ad2fc2131494e0914246a868317b68f4e8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `db9d705a02de2df76d9e1b62334995eac21d110dc172ed350d92306793043708`
- Metadata SHA-256: `57de9e366e385164240069213a2870da7cd8d43f7b6ee6621d6856f237ac7e4c`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reports_existing_site_integrated` | FAIL | with_skill lists Atlas Public/Internal build, Docker, Compose, and Helm evidence and states no build or publish commands were run, but it never reports the required integrated result. |
| `detects_partial_variant_coverage` | PASS | with_skill enumerates Atlas as Public/Internal and Orbit as Public only, identifies Orbit's internal build script as lacking Docker, CI, Compose, and Helm support, and does not claim complete Internal coverage. |
| `returns_gap_to_pm_read_only` | FAIL | with_skill confirms no deployment assets were modified and no deployment commands were run, but it does not ask whether pm-agent should generate a repo-wide deployment handoff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79; output_sha256=81985d8aeaa272ac7daa9fc974bab92f47fe9f0ec876fcf947c334a069f3fd29; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a detailed read-only configuration review, correctly identifies Orbit's incomplete Internal variant, and reports no mutations or execution, but omits the integrated verdict and pm-agent handoff question.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79; output_sha256=1cab8145fd1e085b986b2da94e7f3ab97d7b17ea2c0e70b383fc65bab0584665; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reports Atlas Public/Internal coverage and Orbit Public-only coverage, with evidence and no deployment mutations.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output omits the required integrated verdict.
- The with_skill output does not ask whether pm-agent should generate a repo-wide deployment handoff.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-014-existing-site-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-014-existing-site-deployment-recheck`.
- Fixture SHA-256: `c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79`
- Prompt SHA-256: `1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `52db6badcefada59a1d42e81de2581f06256f43c060b7699c281ab21bfb40949`
- Skill overlay SHA-256: `f896903fa1a8ae6886eb0b6365065625a2e60f6809acd0af6c7c8dc8f8f2bd40`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `db9d705a02de2df76d9e1b62334995eac21d110dc172ed350d92306793043708`
- Metadata SHA-256: `57de9e366e385164240069213a2870da7cd8d43f7b6ee6621d6856f237ac7e4c`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reports_existing_site_integrated` | PASS | With_skill reports Atlas public and internal build targets, CI matrix, Docker stages, Compose services, Helm hosts, and the external OAuth2 dependency; it remains read-only and does not rerun deployment operations. |
| `detects_partial_variant_coverage` | PASS | With_skill enumerates both sites and both variants: Atlas has public/internal configuration with an external OAuth2 dependency, while Orbit has public only and internal lacks an image target, CI, domain, authentication, and private-network launch configuration. It does not claim complete coverage. |
| `returns_gap_to_pm_read_only` | FAIL | With_skill states that no deployment assets were modified, but it does not ask whether pm-agent should generate a repo-wide deployment handoff or identify formal-docs-sync in that handoff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79; output_sha256=8632b2158700e70d3082e9aab729e024476607080aedb2f0119b240976092dfd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a more detailed read-only review with variant, CI, image, authentication, network, and versioning gaps, but omits the required pm-agent handoff question.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79; output_sha256=6758e16dabd3265647b3e1cd081c386b082fa4dd1cdf3059c8806dc881b77858; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a read-only configuration review, identifies Atlas public/internal and Orbit public-only coverage, and notes deployment gaps.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output omits the required question about having pm-agent generate a repo-wide deployment handoff.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-014-existing-site-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-014-existing-site-deployment-recheck`.
- Fixture SHA-256: `c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79`
- Prompt SHA-256: `1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1e290565a84b926a128928ccdd91365a2235adff18f999307c0a3553f0b41f34`
- Skill overlay SHA-256: `0c6a49eed1db242a95632eb0d142c1760f60ffc995c96026908ec8c0e6bd8d63`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `db9d705a02de2df76d9e1b62334995eac21d110dc172ed350d92306793043708`
- Metadata SHA-256: `57de9e366e385164240069213a2870da7cd8d43f7b6ee6621d6856f237ac7e4c`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reports_existing_site_integrated` | PASS | with_skill 将 Atlas Portal 的 public/internal 构建、Docker target、Compose 服务、Helm 入口和 CI matrix 对齐列出，并明确未修改部署资产。 |
| `detects_partial_variant_coverage` | PASS | with_skill 分别枚举了 Orbit Console 的 public 变体及 internal 构建脚本，并指出 internal 缺少 Docker target、CI、Compose 和 Helm 发布/访问链路，判定其不可发布或访问。 |
| `returns_gap_to_pm_read_only` | FAIL | with_skill 明确声明只读且未修改 Dockerfile、workflow、Compose 或 Helm，但没有询问是否由 pm-agent 生成 repo-wide deployment handoff。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79; output_sha256=3d0d97dd50f2e21a723c6db73d28611340474da80ac8e8711075a4a85c14f171; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成只读配置盘点；更明确地区分 Atlas 的完整双变体与 Orbit 仅 public 可发布，并补充认证代理依赖和 CI 发布缺口，但未提出 pm-agent handoff 询问。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79; output_sha256=16371e42fbd2c1047936e86b95d00e68ccbfee00e3f3c9d4835a62eae345a0ef; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成只读配置盘点；识别 Atlas 的 public/internal 链路和 Orbit internal 的发布缺口，但未提出 pm-agent handoff 询问。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足必须询问是否由 pm-agent 生成 repo-wide deployment handoff 的要求。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-014-existing-site-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-014-existing-site-deployment-recheck`.
- Fixture SHA-256: `c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79`
- Prompt SHA-256: `1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `db9d705a02de2df76d9e1b62334995eac21d110dc172ed350d92306793043708`
- Metadata SHA-256: `57de9e366e385164240069213a2870da7cd8d43f7b6ee6621d6856f237ac7e4c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reports_existing_site_integrated` | FAIL | with_skill lists Atlas Public/Internal configurations and evidence, but does not report the existing site as integrated; it instead emphasizes unresolved workflow and external-platform gaps. |
| `detects_partial_variant_coverage` | PASS | with_skill enumerates Orbit's Public and Internal variants, states only Public is configured for CI/image/Compose/Helm, and says Internal cannot form a publishable access entry without claiming completeness. |
| `returns_gap_to_pm_read_only` | FAIL | with_skill states that deployment assets were not modified, but does not ask whether pm-agent should generate a repo-wide deployment handoff. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79; output_sha256=c0baa34eeabf6662a2be605f0b4fa4a8c05d129a15ae1ec170860165d745e37c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a read-only configuration review with evidence, distinguishes Atlas's two configured variants from Orbit's Public-only state, and notes deployment gaps.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1fa72144e806cf52f8fd8fbc5b8cac36763c1b6d96e197c5c1ebe4dd6e004c69; fixture_sha256=c3d3b07fc792c4084ace3c9b32ba907e4fcd07d875befcf6af84add997421b79; output_sha256=5649c8c3e7c5a45f4fb738148943b2fc4678ca2f209d384555c60fb35be571a4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Identifies Atlas Public/Internal and Orbit's Public-only coverage, with evidence and gaps, but does not provide the required integrated/PM handoff behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output omits an explicit integrated conclusion for the existing Atlas site.
- The with_skill output does not ask whether pm-agent should generate a repo-wide deployment handoff.
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

- Skill: `formal-docs-sync`
- Eval: `eval-014-existing-site-deployment-recheck`
- Review context: issue #162 fresh paired validation

## Test Set / Fixture Version

- Fixture: issue #162 scenario evidence in this workspace
- Validation date: 2026-07-22
- Execution cleanup: all declared runtime paths were absent from pristine scratch fixtures

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| reports_existing_site_integrated | PASS | PASS | with_skill 的 `result.txt` 报告 Site A Public/Internal 构建、镜像、Compose/Helm、健康检查和访问控制“证据显示完整”；without_skill 报告 Site A“部署完整”，均列出证据且未重复执行 DevOps。 |
| detects_partial_variant_coverage | PASS | PASS | 两条 lane 均明确列出 Site B：Public 有 Docker/tag workflow/Compose/Helm，Internal 缺少镜像任务、启动拓扑等，并判定为部分完整。 |
| returns_gap_to_pm_read_only | FAIL | FAIL | 两条 lane 均声明只读且未修改 Dockerfile、workflow、Compose 或 Helm；但均未询问或明确返回“由 pm-agent 生成 repo-wide deployment handoff”。 |

未满足断言（with/without 任一 FAIL）：`returns_gap_to_pm_read_only`



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 老站完整时保持 integrated 且不重放 DevOps；仅 Public 覆盖时判 partial 并只读返回 PM。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-014-existing-site-deployment-recheck/candidate-output.md`.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- PARTIAL (2/3)；识别完整/部分覆盖，但直接建议 DevOps，未形成 PM repo-wide 回流。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- baseline 未满足 PM 回流和完整角色边界。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
