# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-015-manual-page-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad` from `agents/docs/test/docs-audit/evals/workspace/eval-015-manual-page-evidence`.
- Fixture SHA-256: `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad`
- Prompt SHA-256: `9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `cde7d254babf29e4546bfe9e69c491c81147f2f6aec782f40fd9d10a9dc4b4fd`
- Eval definition SHA-256: `aa707a4a153cd14f8630bcfdbc7593482bcfc1de05bf7582ac2eeb6f645afb7d`
- Metadata SHA-256: `2b093794d817fa1de245fdac944141cf26e940fab11bd3c871b66f71a9c40eac`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_step_screenshot_files` | PASS | with_skill 指出第 2 步引用的 step-2-save-member.png 不存在，并直接依据 SVG 内容与行号检查了 step-1-access-settings.svg；fixture 中该 SVG 结构完整可解析。 |
| `checks_caption_step_correspondence` | PASS | with_skill 明确指出第 1 步标题/图注“删除工作区确认框”与 SVG 实际显示的“工作区访问设置/保存权限”不符。 |
| `checks_manual_navigation_reachability` | PASS | with_skill 判定公共导航不可达，并引用 sidebar.public.snapshot.md；fixture 中 public 落地页、manual 根索引及生成侧边栏快照均未列出目标页面。 |
| `checks_manual_redaction` | PASS | with_skill 识别 manage-access.md 中的 test.user@example.invalid，以及 step-1-access-settings.svg 第 5 行的 token-demo-redact-me，并指出均违反脱敏要求。 |
| `blocks_manual_stamp` | PASS | with_skill 将结果判为 blocked，明确未盖章；页面仍为 last_verified_version: unverified，且未返回 ready_for_tag。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=fff9b20f40b97d7b6ad894d2b36fa64a9ddd0f84fa8e034a646407a486bff88b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完成 pre-tag 审计，识别截图缺失、图注错配、导航不可达和未脱敏内容，并阻止盖章；未见禁止性变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=c356ac753eca24b49eb4c6d57f6cad085e79cc3a49f550c1c604d136a2243500; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 基线同样识别截图缺失、导航不可达、图注错配及 token 未脱敏，并阻止发布，但未明确识别测试邮箱。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 修复缺失截图、图注错配、导航注册及邮箱/token 脱敏后重新审计。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-015-manual-page-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad` from `agents/docs/test/docs-audit/evals/workspace/eval-015-manual-page-evidence`.
- Fixture SHA-256: `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad`
- Prompt SHA-256: `9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `cde7d254babf29e4546bfe9e69c491c81147f2f6aec782f40fd9d10a9dc4b4fd`
- Eval definition SHA-256: `aa707a4a153cd14f8630bcfdbc7593482bcfc1de05bf7582ac2eeb6f645afb7d`
- Metadata SHA-256: `2b093794d817fa1de245fdac944141cf26e940fab11bd3c871b66f71a9c40eac`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_step_screenshot_files` | PASS | with_skill 明确指出 step-2-save-member.png 不存在，并引用 SVG 内容且确认其展示有效访问设置界面。 |
| `checks_caption_step_correspondence` | PASS | with_skill 指出步骤 1 的图注称“删除工作区确认框”，而 SVG 实际展示访问设置。 |
| `checks_manual_navigation_reachability` | PASS | with_skill 指出生成的公开侧边栏不包含目标手册页；原始 public 落地页、manual 根索引和快照均无该入口。 |
| `checks_manual_redaction` | PASS | with_skill 识别 manage-access.md:18 的测试邮箱及 step-1-access-settings.svg:5 的测试令牌，并要求移除。 |
| `blocks_manual_stamp` | PASS | with_skill 将页面判为 blocked，保留 last_verified_version: unverified，且明确未执行版本 stamp、未返回 ready_for_tag。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=92188746e24a4239d0aa811239c80eeade40708b1efc8243a950e1e85c0c9506; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 完整识别截图、图注、导航和脱敏缺陷，并阻止盖章。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=41e839ac61b64fccf64661e5751aa78aee9b4abdc888c6d6daa3d6cc3cdcfb5a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了截图缺失、导航、图注和令牌问题，但未完整识别邮箱脱敏及阻止盖章状态。
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
- Eval: `eval-015-manual-page-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad` from `agents/docs/test/docs-audit/evals/workspace/eval-015-manual-page-evidence`.
- Fixture SHA-256: `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad`
- Prompt SHA-256: `9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `cde7d254babf29e4546bfe9e69c491c81147f2f6aec782f40fd9d10a9dc4b4fd`
- Eval definition SHA-256: `aa707a4a153cd14f8630bcfdbc7593482bcfc1de05bf7582ac2eeb6f645afb7d`
- Metadata SHA-256: `2b093794d817fa1de245fdac944141cf26e940fab11bd3c871b66f71a9c40eac`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_step_screenshot_files` | FAIL | With_skill notes the missing `step-2-save-member.png`, but does not explicitly confirm that the referenced SVG is parseable as an image. |
| `checks_caption_step_correspondence` | PASS | With_skill identifies that step 1 is access settings while the SVG depicts access settings/save permissions and its caption says “删除工作区确认框,” establishing the mismatch. |
| `checks_manual_navigation_reachability` | FAIL | With_skill states the page is not connected to navigation and cites the sidebar snapshot, but does not establish the required basis across the public landing page, manual root index, and generated snapshot. |
| `checks_manual_redaction` | PASS | With_skill identifies the email in the manual and `token-demo-redact-me` in SVG line 5 as sensitive content requiring redaction. |
| `blocks_manual_stamp` | PASS | With_skill concludes `blocked`, says it cannot return `ready_for_tag`, and records `last_verified_version: unverified`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=7f6511a930111aa254089cdbcf1aaad6e0df3e7f51b35735f8146cadd1a36a4e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Performed a substantially complete audit, finding the missing screenshot, caption mismatch, missing navigation, redaction issues, and blocked release state, but omitted two required evidentiary details.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=f8cc4e5af3b8c6272d1b5e26ea3461034b2bba6794dd3dba0c2b734810901025; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline found the missing PNG, token, caption mismatch, and missing sidebar entry, but omitted the test-email redaction issue and did not provide the full required release audit detail.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- checks_step_screenshot_files
- checks_manual_navigation_reachability
- Next: Explicitly confirm the existing SVG is parseable as an image.
- Next: Cite the public landing page, manual root index, and generated sidebar snapshot when concluding the target page is unreachable through host navigation.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-015-manual-page-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad` from `agents/docs/test/docs-audit/evals/workspace/eval-015-manual-page-evidence`.
- Fixture SHA-256: `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad`
- Prompt SHA-256: `9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `aa707a4a153cd14f8630bcfdbc7593482bcfc1de05bf7582ac2eeb6f645afb7d`
- Metadata SHA-256: `2b093794d817fa1de245fdac944141cf26e940fab11bd3c871b66f71a9c40eac`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_step_screenshot_files` | FAIL | with_skill 指出第二步 PNG 不存在，但未确认第一步 SVG 可作为图像解析。 |
| `checks_caption_step_correspondence` | FAIL | with_skill 未指出第一步要求打开访问设置而图注却描述删除工作区确认框，二者不对应。 |
| `checks_manual_navigation_reachability` | PASS | with_skill 判定手册未出现在导航索引中，并指出 manual 根索引未链接该页面；这与落地页、根索引及生成侧边栏快照均不包含目标页面的证据一致。 |
| `checks_manual_redaction` | PASS | with_skill 识别正文测试邮箱 test.user@example.invalid（manage-access.md:18）和 SVG 中测试令牌 token-demo-redact-me（step-1-access-settings.svg:5），并要求脱敏。 |
| `blocks_manual_stamp` | PASS | with_skill 将结果判为 blocked（pre-tag），确认 last_verified_version 为 unverified，并说明未执行版本盖章。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=3743ccc87effa6ef58deff58848ad31a9cc4f589871ba5dc336bc59b8b6b869a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确阻止盖章并识别截图缺失、导航问题和两类脱敏问题，但遗漏 SVG 可解析确认及图注与步骤不对应的明确结论。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=f2dce27289280c80fe5870f945713aad3ec83720820f626641fd045f1d607c3a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了缺失 PNG、导航不可达、图注错误、令牌及未验证状态，但未识别正文测试邮箱，也未确认 SVG 可解析。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未确认第一步 SVG 可解析。
- with_skill 未指出第一步图注与操作步骤不对应。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-015-manual-page-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad` from `agents/docs/test/docs-audit/evals/workspace/eval-015-manual-page-evidence`.
- Fixture SHA-256: `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad`
- Prompt SHA-256: `9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d339a8370a29b3fb2a69aa1879b1226165ec088d306a4e2e7a01258df2326973`
- Skill overlay SHA-256: `0bc7243cbb5cff3e77d9ba448e020a1a1f279639f8db6a365faac208b8e1dcc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `aa707a4a153cd14f8630bcfdbc7593482bcfc1de05bf7582ac2eeb6f645afb7d`
- Metadata SHA-256: `2b093794d817fa1de245fdac944141cf26e940fab11bd3c871b66f71a9c40eac`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_step_screenshot_files` | FAIL | with_skill 指出 PNG 不存在，但未确认第一步引用的 SVG 可作为图像解析。 |
| `checks_caption_step_correspondence` | PASS | 明确指出第一步“访问设置”与截图标题“删除工作区确认框”不匹配。 |
| `checks_manual_navigation_reachability` | PASS | 判定页面未在导航中直接可达，并指出仅有 `/manual/` 索引入口；该结论与三个公开导航证据一致。 |
| `checks_manual_redaction` | FAIL | 识别了测试邮箱和 `token-demo-redact-me`，但未保留具体文件或行号等证据位置。 |
| `blocks_manual_stamp` | PASS | 明确判为 `blocked`（pre-tag），保留 `last_verified_version: unverified`，并说明未执行盖章；未返回 `ready_for_tag`。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=e2fdb18ab6834c5de93f08503a8ae74a698bd1feb7870805a7137e6bfd2a9e95; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确阻断手册盖章并识别多数事实缺陷，但遗漏 SVG 可解析性的确认，且敏感信息证据位置不够具体。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=f07620ce883a78866c3fb2cd8079df233d2e198858d3f090a9f453ae54f92079; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了截图缺失、敏感 token、图注不符、导航不可达和 unverified 状态，并提供了较具体的文件位置。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未确认第一步 SVG 可作为图像解析。
- with_skill 未为测试邮箱和测试 token 提供具体证据位置。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-015-manual-page-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad` from `agents/docs/test/docs-audit/evals/workspace/eval-015-manual-page-evidence`.
- Fixture SHA-256: `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad`
- Prompt SHA-256: `9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9e9abf391c9ccd9564d35b5def50bc0374b1db0886710676c4d48422839746ae`
- Skill overlay SHA-256: `c66ac938bf9158faa694d7c3e311e913ddc4a06da11de703a881234f257c470c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `aa707a4a153cd14f8630bcfdbc7593482bcfc1de05bf7582ac2eeb6f645afb7d`
- Metadata SHA-256: `2b093794d817fa1de245fdac944141cf26e940fab11bd3c871b66f71a9c40eac`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_step_screenshot_files` | PASS | With-skill output confirms the SVG is present/parseable and the referenced PNG is missing, while checking both steps. |
| `checks_caption_step_correspondence` | PASS | It states that step 1 opens access settings but the caption says “删除工作区确认框,” identifying the mismatch. |
| `checks_manual_navigation_reachability` | FAIL | It cites the generated sidebar snapshot, but does not establish the required combined evidence from the public landing page, manual root index, and sidebar snapshot. |
| `checks_manual_redaction` | PASS | It identifies test.user@example.invalid in the manual body and token-demo-redact-me in the SVG as sensitive content, with file-path evidence. |
| `blocks_manual_stamp` | PASS | It concludes blocked, explicitly says it cannot return ready_for_tag, and records last_verified_version as unverified. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=172d8898fde9a7da2ccd9c8e16faee864d25a0a996acc7a8d8fc934763695af8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks release and identifies the screenshot, caption, redaction, navigation, procedure-completeness, and release-evidence issues; it does not cite all three required navigation evidence sources.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=5c0bb797e963c317aee85a97a184d81c8d210ec2ab6a85ac7897e5309eae92e0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Identifies the missing PNG, navigation gap, caption mismatch, token exposure, and unverified version, but omits the missing third procedure step and test email.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output does not provide the required combined public landing-page, manual-root-index, and sidebar-snapshot evidence for navigation reachability.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-015-manual-page-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad` from `agents/docs/test/docs-audit/evals/workspace/eval-015-manual-page-evidence`.
- Fixture SHA-256: `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad`
- Prompt SHA-256: `9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2d24da5f976a5ab2710c2c072a19015e074d314e0ebdb88f1c28831425f1b98c`
- Skill overlay SHA-256: `40330c17a3b77f25a1b1a716fa5e9355e0011db79d19014344ed516affba11c8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `aa707a4a153cd14f8630bcfdbc7593482bcfc1de05bf7582ac2eeb6f645afb7d`
- Metadata SHA-256: `2b093794d817fa1de245fdac944141cf26e940fab11bd3c871b66f71a9c40eac`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_step_screenshot_files` | FAIL | with_skill 指出第二步 PNG 不存在，但未确认第一步 SVG 可作为图像解析。 |
| `checks_caption_step_correspondence` | PASS | with_skill 指出第一步截图标题为“删除工作区确认框”，而画面内容是“工作区访问设置”，并给出 manage-access.md:22-24。 |
| `checks_manual_navigation_reachability` | FAIL | with_skill 仅依据侧边栏快照判定未入导航，未同时指出 public 落地页和 manual 根索引均未包含目标页面。 |
| `checks_manual_redaction` | FAIL | with_skill 给出正文测试邮箱位置 manage-access.md:18，并识别截图 token-demo-redact-me，但未提供截图文件或行号等具体证据位置。 |
| `blocks_manual_stamp` | PASS | with_skill 明确结论为 blocked，说明不能返回 ready_for_tag，且页面保持 last_verified_version: unverified。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=76b60cdfc288fb641e71b9167fef9743fa11ed4b04557dda70fcb9023fc3215d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了缺失 PNG、图注不符、正文邮箱、截图令牌、导航缺项及 blocked 状态；但遗漏第一步 SVG 可解析性确认、public 落地页与 manual 根索引证据，以及令牌的具体证据位置。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=d1eaad9c37ff7ab45803f5fc8040e086f2ecbfbd6fe3796a9d339e1a6304382a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 新鲜基线识别了缺失 PNG、导航快照缺项、图注不符和截图令牌风险，并建议阻断发布；未识别正文测试邮箱，也未完成逐步 SVG 可解析性和完整导航证据链确认。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确确认第一步 SVG 可作为图像解析。
- with_skill 未完整覆盖 public 落地页、manual 根索引和生成侧边栏三处导航证据。
- with_skill 未为截图令牌提供具体证据位置。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-015-manual-page-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad` from `agents/docs/test/docs-audit/evals/workspace/eval-015-manual-page-evidence`.
- Fixture SHA-256: `1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad`
- Prompt SHA-256: `9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `aa707a4a153cd14f8630bcfdbc7593482bcfc1de05bf7582ac2eeb6f645afb7d`
- Metadata SHA-256: `2b093794d817fa1de245fdac944141cf26e940fab11bd3c871b66f71a9c40eac`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `checks_step_screenshot_files` | FAIL | 原始证据表明 SVG 结构可解析且 `step-2-save-member.png` 不存在；with_skill 仅指出 PNG 缺失，未确认 SVG 可作为图像解析。 |
| `checks_caption_step_correspondence` | PASS | with_skill 指出“删除工作区确认框”标题与“工作区访问设置/保存权限”画面不一致；正文第一步要求打开访问设置。 |
| `checks_manual_navigation_reachability` | FAIL | 原始证据显示 public 落地页、manual 根索引及生成后侧边栏均未包含目标页；with_skill 仅引用 sidebar 证据，未依据三处证据完整作出判定。 |
| `checks_manual_redaction` | FAIL | 原始证据包含正文测试邮箱 `test.user@example.invalid` 和 SVG 中的 `token-demo-redact-me`；with_skill 只识别了 token，未识别测试邮箱。 |
| `blocks_manual_stamp` | PASS | with_skill 明确判定 `blocked`、不能返回 `ready_for_tag`，并记录 `last_verified_version: unverified`。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=14ae41223a9c5d5212493b38f5f47273ad68bf459c2cd4e0864dbab2aea94d47; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确判定页面 blocked 并识别主要截图、图注、导航、token 和事实覆盖问题，但遗漏 SVG 可解析确认、测试邮箱及完整三处导航证据。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c90b10bde8bbda672daf3c3fd6d8b4bfbcd80966d8091d82aceff2f385c4210; fixture_sha256=1c27cfa2f41ff48338bb4acbfdb7cd16614fdaed5b9fc59cbb0ed2df02c327ad; output_sha256=6b77924f16d10a3f3840ab56a5ec23c70ff06416eb6d4c6485a465d0f8ea0990; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了缺失 PNG、导航缺失、图注不匹配、未验证状态和 token，但未识别测试邮箱，也未完整覆盖三处导航证据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完整满足截图可解析、三处导航证据和双重脱敏证据要求。
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
- Eval: `eval-015-manual-page-evidence`
- Review context: PR #232 third-round review remediation

## Test Set / Fixture Version

- Fixture: one changed `doc_type: manual` page with deliberate screenshot, caption, navigation, and redaction defects
- Assertions: 5
- Validation date: `2026-08-06`（#238 fresh 重跑）

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
- Overall result: FAIL

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `checks_step_screenshot_files` | FAIL | FAIL | 两侧均确认第二步 PNG 不存在；但均未明确确认第一步 SVG 可解析。文件实际为有效 SVG，且 `step-2-save-member.png` 不存在。 |
| `checks_caption_step_correspondence` | FAIL | PASS | with_skill 仅笼统要求修复对应关系；without_skill 明确指出步骤 1 是“访问设置”，图注却写“删除工作区确认框”（`manage-access.md:22-24`）。 |
| `checks_manual_navigation_reachability` | FAIL | FAIL | 两侧仅引用侧边栏快照未包含目标页；未同时依据 public 落地页与 manual 根索引完成三处导航核对。相关事实见 `index.public.md:15`、`manual/index.md:15`、`sidebar.public.snapshot.md:10-11`。 |
| `checks_manual_redaction` | FAIL | FAIL | 两侧均识别截图中的 `token-demo-redact-me`（SVG 第 5 行），但均遗漏正文测试邮箱 `test.user@example.invalid`（`manage-access.md:18`）。 |
| `blocks_manual_stamp` | PASS | PASS | with_skill 明确结论为 `blocked`、不能返回 `ready_for_tag`，并说明未修改 `last_verified_version`；without_skill 明确页面不可安全发布，且 `last_verified_version: unverified`（`manage-access.md:10`），未返回 `ready_for_tag`。 |

未满足断言（with/without 任一 FAIL）：``checks_step_screenshot_files``、``checks_caption_step_correspondence``、``checks_manual_navigation_reachability``、``checks_manual_redaction``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- Not executed. No behavior conclusion is recorded for the new manual fact-check branch.

## Fresh Without-Skill Baseline（#238）

- 来源：2026-08-06 的 #238 fresh 隔离重跑；使用与 with-skill 逐字相同的 prompt 和 pristine fixture，未加载 `docs-audit` skill，由独立 judge 对照五条断言判定。
- 行为摘要：Behavior `FAIL` / Coverage `FULL`；仅 `checks_caption_step_correspondence` 与 `blocks_manual_stamp` 通过，其余三条事实核验断言失败。

## Failures

- #238 fresh 重跑中，with-skill 未完整核验截图文件、图注与步骤对应、三处导航可达性及正文测试邮箱脱敏，Behavior 判定为 `FAIL`。

## Next Steps

- 修复 `docs-audit` 对 manual 页面证据的核验缺口后，使用相同 prompt 与 pristine fixture 重新执行 paired eval，并由独立 judge 复核五条断言。

## Runtime Artifact Policy

- Runtime candidates, transcripts, outputs, verdicts, timing, status, and diagnostics must remain in an isolated scratch workspace and must not be committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
