# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-004-deployment-completeness-trigger`.
- Fixture SHA-256: `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842`
- Prompt SHA-256: `a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f74a445a21eabfad3f25cc38a5190833cf5fc52294bb0054a41378fe894ddd82`
- Skill overlay SHA-256: `749412be4f8f7fe24db333e412ff5013877a6c57121d621b10bbe79fa7b60b02`
- Judge schema SHA-256: `84cb88cc9e25dde2fbf0d2a0fb5349bfe630e32b333634cfdb918d30e60002a8`
- Eval definition SHA-256: `f0a0699462419947dfa64649c390cf74a3d370111b9c3ea826e84a8d4dc9f735`
- Metadata SHA-256: `abed400d8529a0bd91cc069fda9057f38aa9e64b1a632698bb6d1e29c26ae6e8`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_first_bootstrap_integrated` | NOT_EXERCISED | The locked with_skill output reports the repository states but provides no durable-commit confirmation or completed first-bootstrap integrated classification. |
| `asks_first_bootstrap_choice` | FAIL | It identifies billing-api as lacking a documentation site and suggests PM/Docs scope confirmation, but does not explicitly ask the three required choices: include all variants, independent hosting not_applicable, or defer with blocker. |
| `rechecks_rebootstrap_drift` | NOT_EXERCISED | No locked evidence shows a repeated bootstrap, re-read configuration, or Internal startup-path drift recheck. |
| `preserves_authorization_boundary` | PASS | The output explicitly states the check was read-only and no files were modified; git evidence also shows no changes, commits, pushes, releases, or deployments. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=fe4360fe69be6281e70aaea42c218c4feb3cedd3e55a9d03ba9a49c07efcb010; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Accurately performs the requested read-only repository connectivity review and preserves the authorization boundary, but omits the explicit three-way bootstrap choice.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=ebf512367cce7627977b41c253d64e86d1f61149606d857b4b3c54da7d2e487c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a comparable read-only repository review, with similar connectivity findings, but is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- asks_first_bootstrap_choice was not satisfied: the required three-way user choice was omitted.
- Next: If the bootstrap workflow is continued, explicitly ask the three required hosting/scope choices for the non-integrated documentation host.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-004-deployment-completeness-trigger`.
- Fixture SHA-256: `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842`
- Prompt SHA-256: `a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f74a445a21eabfad3f25cc38a5190833cf5fc52294bb0054a41378fe894ddd82`
- Skill overlay SHA-256: `749412be4f8f7fe24db333e412ff5013877a6c57121d621b10bbe79fa7b60b02`
- Judge schema SHA-256: `84cb88cc9e25dde2fbf0d2a0fb5349bfe630e32b333634cfdb918d30e60002a8`
- Eval definition SHA-256: `f0a0699462419947dfa64649c390cf74a3d370111b9c3ea826e84a8d4dc9f735`
- Metadata SHA-256: `abed400d8529a0bd91cc069fda9057f38aa9e64b1a632698bb6d1e29c26ae6e8`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_first_bootstrap_integrated` | NOT_EXERCISED | No bootstrap was performed, no durable-commit confirmation occurred, and no first integrated-state workflow was exercised. |
| `asks_first_bootstrap_choice` | NOT_EXERCISED | No bootstrap host-selection workflow was initiated; the output only reports repository findings and follow-up owners. |
| `rechecks_rebootstrap_drift` | NOT_EXERCISED | No repeated bootstrap or configuration re-read was performed. |
| `preserves_authorization_boundary` | PASS | The output explicitly remains read-only, and locked git evidence shows no branch, commit, index, worktree, or untracked-file changes; it does not authorize or perform push, publishing, deployment, or Docs changes to delivery files. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=3cdff511a25b3540d43e26cff08d26bda11a9b9b91c02b7b0e6c3faae05fc243; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly performed the requested read-only repository connectivity review and preserved the authorization boundary; bootstrap-specific behavior was not exercised.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=1e9d207918be4b76ca5da079a6065533ff71116bdec80ed4e111c318dbe41825; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also performed a read-only connectivity review, but is comparison context only and does not affect assertion verdicts.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain user confirmation and runtime evidence before judging first-bootstrap integration, three-way choice handling, or re-bootstrap drift detection.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-004-deployment-completeness-trigger`.
- Fixture SHA-256: `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842`
- Prompt SHA-256: `a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f74a445a21eabfad3f25cc38a5190833cf5fc52294bb0054a41378fe894ddd82`
- Skill overlay SHA-256: `749412be4f8f7fe24db333e412ff5013877a6c57121d621b10bbe79fa7b60b02`
- Judge schema SHA-256: `84cb88cc9e25dde2fbf0d2a0fb5349bfe630e32b333634cfdb918d30e60002a8`
- Eval definition SHA-256: `f0a0699462419947dfa64649c390cf74a3d370111b9c3ea826e84a8d4dc9f735`
- Metadata SHA-256: `abed400d8529a0bd91cc069fda9057f38aa9e64b1a632698bb6d1e29c26ae6e8`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_first_bootstrap_integrated` | NOT_EXERCISED | 未提供 durable commit 确认、Public/Internal 枚举后的集成交付快照或运行时证据；该交互后续步骤未发生。 |
| `asks_first_bootstrap_choice` | FAIL | with_skill 识别 support-portal 未连通并指出 internal 路径漂移，但未明确询问“全部纳入、独立托管 not_applicable、暂缓并保留 blocker”三个选择。 |
| `rechecks_rebootstrap_drift` | NOT_EXERCISED | 没有重复 bootstrap、重新读取配置或用户确认进入 PM 到 DevOps 补链路的原始证据。 |
| `preserves_authorization_boundary` | PASS | 明确说明只读检查且未修改文件；git evidence 显示无提交、分支或工作区变化，也未主张 push、镜像发布或部署授权。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=a1ee3b125900a9881ac7ee92544a91383b663430a30cc25fda1fceed5f708340; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成只读配置检查，正确识别 atlas-docs 的闭环缺口、support-portal 的 internal 路径漂移，并保持无修改边界；未继续交互式 bootstrap 选择流程。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=159523a6e0cfeb9e80e6672bed49c743f088ff38e3c2a0cbd225b0233c82c124; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样识别主要构建、路径和发布缺口，但将 billing-api 的非文档站状态及部分细节作了不同表述；仅作基线对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未提出首次未集成状态所要求的三个后续处理选项。
- Next: 补充首次未集成时的三个明确选择，并等待用户选择。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-004-deployment-completeness-trigger`.
- Fixture SHA-256: `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842`
- Prompt SHA-256: `a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f74a445a21eabfad3f25cc38a5190833cf5fc52294bb0054a41378fe894ddd82`
- Skill overlay SHA-256: `749412be4f8f7fe24db333e412ff5013877a6c57121d621b10bbe79fa7b60b02`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f0a0699462419947dfa64649c390cf74a3d370111b9c3ea826e84a8d4dc9f735`
- Metadata SHA-256: `abed400d8529a0bd91cc069fda9057f38aa9e64b1a632698bb6d1e29c26ae6e8`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_first_bootstrap_integrated` | NOT_EXERCISED | with_skill 未执行首次 bootstrap、durable commit 确认或 integrated 判定；仅完成静态快照审计。 |
| `asks_first_bootstrap_choice` | FAIL | with_skill 已识别 billing-api 不含文档站，但只要求确认是否初始化，未明确提出“全部变体纳入、独立托管 not_applicable、暂缓并保留 blocker”三个选择。 |
| `rechecks_rebootstrap_drift` | NOT_EXERCISED | with_skill 未执行重复 bootstrap、配置重读或 Internal 启动路径漂移检查，因此后续 PM 到 DevOps 询问未到可执行阶段。 |
| `preserves_authorization_boundary` | PASS | with_skill 明确声明仅做静态检查，未执行构建、推送或部署；锁定 git 证据显示无提交、分支或工作区变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=762ec8b6c5d672c94399ffb8f836a01e9943323370441ee9b60dbd0b29291d29; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成三仓库静态审计并保留只读边界；对缺少文档站的 billing-api 未提供要求的三选一 bootstrap 选项。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=374e68e626645b02f0a761f613b6ef6add03c5022f909c7f18401195a72604d2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成三仓库静态连通性审计，识别 support-portal 路径错误及 atlas-docs 的 push/部署断点，但未执行 bootstrap 交互。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- asks_first_bootstrap_choice：billing-api 被识别为无文档站，但未明确给出全部变体纳入、独立托管 not_applicable、暂缓并保留 blocker 三个选择。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-004-deployment-completeness-trigger`.
- Fixture SHA-256: `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842`
- Prompt SHA-256: `a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `94e37af2ad7f4b39032db420d30845826ffa4c408edb8ffe671f400ff7e83f83`
- Skill overlay SHA-256: `09f32081fb5da19c616e5c124981201ff10d8f1031a9890f0577b1364fa9c83c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f0a0699462419947dfa64649c390cf74a3d370111b9c3ea826e84a8d4dc9f735`
- Metadata SHA-256: `abed400d8529a0bd91cc069fda9057f38aa9e64b1a632698bb6d1e29c26ae6e8`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_first_bootstrap_integrated` | NOT_EXERCISED | 输出仅完成只读快照检查；没有用户确认 durable commit，也没有执行首次完整建站流程。 |
| `asks_first_bootstrap_choice` | NOT_EXERCISED | 输出识别了未连通仓库，但未进入首次 bootstrap 的交互选择步骤；该后续流程未被触发。 |
| `rechecks_rebootstrap_drift` | NOT_EXERCISED | 没有执行重复 bootstrap 或重新读取配置以检查漂移。 |
| `preserves_authorization_boundary` | PASS | with_skill 输出明确声明为只读检查，提出后续负责人和补齐事项但未声称执行 push、镜像发布、部署或修改 Docker、CI/CD、Compose、Helm；git evidence 也显示无变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=420a1bd6b6f10fd6d8f5b5cbfcb3b27f7204bcefd0678496ede750177cc0d6e0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了更完整的只读连通性分析和后续责任分工，识别变体、Dockerfile、Compose、CI 与 Helm 证据，但未进入 bootstrap 交互流程。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=99dc18ffcce827270d1005e05538360dab96d271f862dd04c2434bafb52e59ac; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了静态仓库连通性检查，识别 support-portal 的 internal 路径错误，但未执行交互式 bootstrap 流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 如需覆盖未 exercised 的断言，需要在后续交互中触发首次 bootstrap 并确认 durable commit，再执行重复 bootstrap 以验证漂移处理。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-004-deployment-completeness-trigger`.
- Fixture SHA-256: `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842`
- Prompt SHA-256: `a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b2f0004a415a9413ec4f04c88be670a46f49aae91bdfea7a5f5a1bd3994bc3a2`
- Skill overlay SHA-256: `e3264805b55d520c4492930be28050bfd749cd67b6530c8ad7ae5532a81dc597`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f0a0699462419947dfa64649c390cf74a3d370111b9c3ea826e84a8d4dc9f735`
- Metadata SHA-256: `abed400d8529a0bd91cc069fda9057f38aa9e64b1a632698bb6d1e29c26ae6e8`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_first_bootstrap_integrated` | NOT_EXERCISED | 候选输出提供了构建、Docker、CI、Compose/Helm 和入口配置证据，但没有 durable commit 确认后的首次 bootstrap 流程或 integrated 判定过程。 |
| `asks_first_bootstrap_choice` | NOT_EXERCISED | 输出识别了 support-portal 的未连通状态，但三选一属于后续交互步骤；当前没有用户确认或继续 bootstrap 的运行时证据。 |
| `rechecks_rebootstrap_drift` | NOT_EXERCISED | 输出正确指出 support-portal 的 .generated/private 与 .generated/internal 路径漂移，但锁定证据无法证明这是重复 bootstrap 后重新读取配置，也未进行后续询问。 |
| `preserves_authorization_boundary` | PASS | 输出保持只读检查，未执行 push、镜像发布、部署或仓库修改；git_evidence 显示分支、提交和工作树均未变化，并将后续处理交给相应 owner。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=80411edca5cc78dcb2975f54caf074aec76edf6f955a97ee7d01405edbf2bf31; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 更准确识别了 CI 中 Docker build、缺少 push、部署配置及 support-portal 路径漂移，同时保持只读边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=3e61f3c500c48bd61e6f3f7a60183289c9aed876c873049fa3ce0f977e8a855d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成了基础只读链路检查，识别 support-portal 路径断点，但未确认 CI 实际构建与推送。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 如需完整覆盖这些断言，应在用户确认 durable commit 后运行首次 bootstrap，并在后续确认后执行 re-bootstrap 流程。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-004-deployment-completeness-trigger`.
- Fixture SHA-256: `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842`
- Prompt SHA-256: `a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `152b64c666428933a1e4cc6555b5ae40ea5c3e08c7fc1320bdd861942ed3733a`
- Skill overlay SHA-256: `256eb0ac5a55ca6fadf72afd9abf599973b2fa270458596afcc043a11cc688b6`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f0a0699462419947dfa64649c390cf74a3d370111b9c3ea826e84a8d4dc9f735`
- Metadata SHA-256: `abed400d8529a0bd91cc069fda9057f38aa9e64b1a632698bb6d1e29c26ae6e8`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_first_bootstrap_integrated` | FAIL | The with_skill output does not perform or report a first-bootstrap durable-commit confirmation, real Docker/CI/Compose/Helm/入口 verification, or an integrated classification; it explicitly says real CI, registry, and cluster state were not verified. |
| `asks_first_bootstrap_choice` | FAIL | For support-portal, the output identifies a broken internal build path but asks owners to repair and connect publishing/deployment; it does not present the required three choices: include all variants, independent hosting/not_applicable, or defer with blocker. |
| `rechecks_rebootstrap_drift` | NOT_EXERCISED | Neither the with_skill output nor the read-only fixture evidence shows a repeated bootstrap, configuration reread, or a rebootstrap drift decision. |
| `preserves_authorization_boundary` | PASS | The output explicitly frames the work as read-only, reports missing push/deployment evidence rather than performing those actions, and assigns Docker/CI/CD/Compose/Helm work to engineering or platform owners without authorizing Docs to modify those systems. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=a945b9847f3a7ac347145818c3f353c223b779bbdf4bbe0556d29d7b86b89d31; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a more precise read-only repository audit, correctly identifies support-portal's internal artifact-path break and atlas-docs' missing image publication/deployment closure, while preserving the authorization boundary; bootstrap-choice and rebootstrap behaviors are absent.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=caea4f3701d93a4a3f2479e7ede065739303dc13c76c7c83c943f860cbc615ae; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a read-only connectivity audit and correctly spots missing push/deployment steps and the support-portal path mismatch, but does not follow the bootstrap-specific interaction requirements.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane does not satisfy the first-bootstrap integrated classification requirement.
- The with_skill lane does not ask the required three-way choice for an unintegrated site.
- The rebootstrap drift assertion is not exercised.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-004-deployment-completeness-trigger`.
- Fixture SHA-256: `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842`
- Prompt SHA-256: `a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4a398cfa9db1074844549bc002d7714ae1641dceb87757d5c772d45182765b8a`
- Skill overlay SHA-256: `4e5a2571a4a7180fe735bec31f7744892dd9b213e7966b85237f9d1c2b22d88a`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f0a0699462419947dfa64649c390cf74a3d370111b9c3ea826e84a8d4dc9f735`
- Metadata SHA-256: `abed400d8529a0bd91cc069fda9057f38aa9e64b1a632698bb6d1e29c26ae6e8`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_first_bootstrap_integrated` | FAIL | with_skill 输出将 atlas-docs 判为“部分连通，未完成发布闭环”，未体现 durable commit 确认后的首次 integrated 判定或不重复执行 DevOps。 |
| `asks_first_bootstrap_choice` | FAIL | with_skill 输出未将镜像化宿主判为 not_integrated，也未明确询问纳入全部变体、独立托管 not_applicable、暂缓保留 blocker 三个选择。 |
| `rechecks_rebootstrap_drift` | FAIL | with_skill 输出未体现重复 bootstrap、重新读取配置、识别 Internal 启动路径漂移并重新询问进入 PM 到 DevOps 链路。 |
| `preserves_authorization_boundary` | PASS | 输出明确为只读检查，未声称执行 push、镜像发布、部署或修改 Docker/CI/CD/Compose/Helm；仅将后续工作交给文档维护者及发布/平台团队。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=09a202e03a46b7d1b4844a04fb56af5a2d9882fc13c8f2e59623440cd28b583c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供只读仓库链路审计、证据和责任分工；未执行或描述断言要求的 bootstrap 流程。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=3d3561d7588e7d04285e9ae0be1a6978a6aa5eac4b095225cf718ce88c0fda73; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供仓库链路审计和阻断点，但未覆盖首次 bootstrap 选择、重复 bootstrap 漂移或授权边界流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足首次 integrated 判定断言。
- with_skill 未满足首次未集成三选一断言。
- with_skill 未满足重复 bootstrap 漂移复核断言。
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

- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`
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
| `classifies_first_bootstrap_integrated` | PASS | PASS | 两条 `result.txt` 均依据 `evidence.md`，列出 Public/Internal、Docker、Tag CI、Compose、Helm、健康检查、TLS 和网络认证，并说明仅做只读核验、未重复执行发布部署。 |
| `asks_first_bootstrap_choice` | FAIL | FAIL | 两条产物均仅说“补齐”缺失的 Dockerfile、CI、Compose、Helm 配置，没有明确询问三选一：全部纳入、独立托管 `not_applicable`、暂缓并保留 blocker。 |
| `rechecks_rebootstrap_drift` | FAIL | FAIL | 两条产物都识别了 `.generated/internal` → `.generated/private` 的路径漂移，但没有判为 `partial`，也没有重新询问是否进入 PM → DevOps 补齐链路。 |
| `preserves_authorization_boundary` | PASS | PASS | 两条产物均明确“仅获准只读检查和文档修改”，且未执行或授权 push、镜像发布、部署；没有让 Docs 明确修改 Docker、CI/CD、Compose 或 Helm。 |

未满足断言（with/without 任一 FAIL）：``asks_first_bootstrap_choice``、``rechecks_rebootstrap_drift``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 正确区分首次 integrated、首次 not_integrated、re-bootstrap partial 漂移，给出三选一和授权边界。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-004-deployment-completeness-trigger/candidate-output.md`.

## Fresh Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- BLOCKED (0/4)；识别事实但缺 durable commit trigger、稳定状态、完整三选一与 PM/DevOps 链路。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- baseline 缺少共享 closeout 协议。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
