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
