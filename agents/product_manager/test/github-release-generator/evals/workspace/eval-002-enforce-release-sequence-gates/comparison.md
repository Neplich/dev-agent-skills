# Eval Result: github-release-generator-enforce-release-sequence-gates

## Evaluation Target

- Skill: `github-release-generator`
- Test case: site-first、draft latest 隔离、publish 最终写前漂移复查与 publication triple gate
- Latest result: PASS - 2026-07-21 issue #146 fresh paired validation 完成，with-skill 6/6 assertions 通过

## Review Context

- Review issue: #146
- Final judge: 当前会话中的 fresh Codex validation agent
- 两条 lane 分别由全新 worker 生成；judge 在两侧完成前未读取历史 `comparison.md`。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: AI Hub-shaped `v1.0.0-rc.1` confirmed page、current latest `v0.9.0`、`ready_for_tag` 与两个不完整发布场景
- Runtime evidence: `tmp/eval-runs/issue-146/{with_skill,without_skill}/eval-002-enforce-release-sequence-gates/`

## Assertions

- PASS `site_notes_before_github_release`: 明确站内 Release Notes 确认、docs audit `ready_for_tag`、PM submit-ready preview 的先后顺序。
- PASS `ready_for_tag_allows_preview_only`: `ready_for_tag` 仅允许 preview 或受限 draft 准备，不替代实际 tag、post-tag `release_verified` 或发布批准。
- PASS `draft_omits_latest_and_publish_rechecks`: 单 `v` 前缀移除后正确识别 prerelease，preview 显示 `--prerelease --latest=false`；draft 省略 latest flag；publish 内容写后、最终写前与最终写后均覆盖 target/latest/tag OID 复查，最终写原子应用 prerelease/latest 决定，漂移时停止并路由。
- PASS `blocks_missing_tag_and_post_tag_audit`: 场景 A 同时因实际 tag 与 `release_verified` 缺失而阻塞，并分别返回宿主 release owner 与 `docs-agent:docs-audit`。
- PASS `blocks_missing_independent_approval`: 场景 B 即使 tag 和 post-tag audit 齐备，仍因缺本次当前、明确、独立的维护者批准而阻塞。
- PASS `keeps_preview_or_draft`: 两个场景均只保留 preview 或既有 draft，没有调用发布操作。

## With Skill Behavior

- 给出完整 prerelease preview，并明确 pre-tag compare 与 tag 存在后的 final compare 边界。
- draft create/update 省略 `--latest` 与 `--latest=false`；publish 两阶段写入覆盖 fresh target 的 `isPrerelease`、latest 与远端 tag OID readback。
- A、B 两个请求分别在缺 tag/post-tag audit 与缺独立批准处阻塞，未虚构 fixture 未提供的 tag OID。

## Without Skill Baseline

- 2026-07-21 使用同一 prompt、assertions、expected output、metadata 与 fixture 全新生成；未读取 skill、Agent README、with-skill 证据或历史 comparison。
- baseline 同样 6/6 assertions PASS，覆盖 draft latest 隔离、publish fresh-read/漂移保护和两组 publication blockers。
- 主要差异：with-skill 更明确区分当前 pre-tag compare 与 future final compare，并强调 missing-tag 时不能创建 draft；baseline 给出同等断言结论但对远端字段全集与现有 draft 状态保留不确定性。当前 assertions 的区分度为 0/6。

## Failures

- 无 assertion failure 或 blocker。
- 非阻塞 finding：fixture、expected output 与 assertions 对完整发布写序提示很强，fresh baseline 同样全部通过，未证明 skill 相对 baseline 的断言增益。

## Next Steps

- 当 #116/#117 handoff、draft latest 限制、publish 写序、tag OID 漂移或 GitHub CLI missing-tag 行为变化时重新执行 paired validation。
- 若要提升区分度，可减少 expected output 对最终写序的直接提示，并加入 tag/draft 均不存在但请求创建 draft 的弱提示场景。

## Runtime Artifacts Policy

- 本轮 candidate、worker observations 与 manifest 仅位于 `tmp/eval-runs/issue-146/`，作为短期运行期证据。
- 不提交 transcript、candidate、worker observations、manifest、verdict、outputs、timing 或 diagnostics；长期结果仅保留本 `comparison.md`。
