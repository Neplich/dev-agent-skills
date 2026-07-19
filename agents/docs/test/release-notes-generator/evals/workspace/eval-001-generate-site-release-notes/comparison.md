# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-001-generate-site-release-notes`

## Test Set / Fixture Version

- Fixture: `issue-126-r3-lockfile-v1`
- 评估基线：PR #126 R3 working tree
- Harness：`tmp/eval-runs/126-r3-docs-release/eval-001-generate-site-release-notes/`
- Fresh validation：当前会话全新 subagent 先执行 with-skill，再以同一 prompt 和 pristine fixture 作 fresh zero-skill 对照判断；未复用历史 baseline。

## Latest Result

**PASS（5/5 assertions）** — with-skill 完整生成六类证据页面，保持 release frontmatter 与确认顺序，按新增 lockfile 完成确定性安装，并在显式 fixture base 下通过 74/74 宿主测试后输出完整 #120 ready handoff。

## With-Skill Behavior

- `preserves_six_evidence_categories`：PASS。页面分别保留功能、架构、数据库、部署、资产、升级兼容与风险事实和来源。
- `uses_release_frontmatter_contract`：PASS。七字段完整，`doc_type: release`，owners/related_code 非空，`last_verified_version: unverified`。
- `enforces_confirmation_before_derived_writes`：PASS。候选页回读时 index、metadata 零变化；应用 `confirmation-record.md` 后才更新两者，自动导航配置未修改。
- `runs_real_host_docs_checks`：PASS。干净依赖状态执行 `npm ci --ignore-scripts`，exit 0；默认 `npm run test:docs` 因单提交 fixture 无 committed base 退出 1，随后使用宿主原生支持的 `GITHUB_BASE_SHA=HEAD npm run test:docs` 重跑，exit 0、74/74。
- `returns_complete_ready_handoff`：PASS。`handoff.yaml` 仅在 confirmed 和 checks 通过后 ready，包含全部规定字段，且 `release_execution_authorized: false`、下一门禁为 #117。

## Without-Skill Baseline

- 来源：当前 fresh subagent 对同 prompt/pristine fixture 的 zero-skill control 直接判断；control 不读取或应用目标 skill 与 Docs Agent README。
- 宿主 README 足以提示六类正文、确认顺序和 docs check，但没有定义完整 #120 handoff 字段、#117 next gate 或 `release_execution_authorized` 语义；对照最多满足页面与宿主校验，无法稳定满足完整 ready handoff assertion。

## Failures

- 无 assertion failure。首次无 base 的 docs check 失败被保留为真实 harness 证据，不作为最终成功结果隐藏。

## Next Steps

- 后续 fixture runner 应预置 committed base 或显式设置 `GITHUB_BASE_SHA=HEAD`，避免将单提交 harness 限制误判为文档失败。

## Runtime Artifact Policy

- 页面、handoff、依赖目录、命令输出和 scratch git 仅保留在 `tmp/eval-runs/126-r3-docs-release/`，不提交到 git。
