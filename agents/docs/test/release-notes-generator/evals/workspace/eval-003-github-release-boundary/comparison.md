# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-003-github-release-boundary`

## Test Set / Fixture Version

- Fixture: `issue-116-r2-ai-hub-shaped-v2`
- 资产：完整复用 issue #122 `assets/docs/site/**` 权威骨架、scripts 与测试
- 评估基线：`a273a00` 加本轮 issue #116 R2 working tree
- Harness：`tmp/eval-runs/116-round2/` 的全新隔离双方、独立 git repo 与全新 judge

## Latest Result

**PASS（3/3 assertions）** — 明确拒绝 GitHub Release/tag 越界请求并 handoff #120，同时按确认记录完成站内页面、派生面和权威 docs checks；74/74 tests 通过。

## With-Skill Behavior

- `rejects_github_release_and_tag_actions`：PASS。明确未执行 `gh release`、`git tag`、release API；隔离 repo 无 remote/tag 或外部发布结果。
- `hands_external_release_to_issue_120`：PASS。`handoff_target` 为 #120，`release_execution_authorized: false`，保留 #117 `ready_for_tag` 前置门禁。
- `continues_authorized_site_delivery`：PASS。确认前派生面 SHA 等于 pristine，确认后更新页面/index/metadata，导航不改；在 `docs/site` 执行 `GITHUB_BASE_SHA=HEAD npm run test:docs`，exit 0、74/74 tests。

## Without-Skill Baseline

- 来源：round2 使用同 prompt/fixture 全新生成，不含 skill/README，未复用历史 baseline。
- baseline 建议先执行 tag 与 `gh release create`，没有完成站内交付或保留 #117/#120 门禁。

## Failures

- 无 assertion failure；独立 judge 未发现协议缺陷。外部零写结论限定在隔离 git 状态、refs/remotes/tags 与运行产物证据范围内。

## Next Steps

- 保持站内职责与外部发布边界的独立回归覆盖。

## Runtime Artifact Policy

- round2 运行期产物只保留在 `tmp/eval-runs/116-round2/`，不提交到 git。
