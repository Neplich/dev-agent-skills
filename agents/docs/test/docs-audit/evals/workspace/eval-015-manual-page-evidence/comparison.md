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
