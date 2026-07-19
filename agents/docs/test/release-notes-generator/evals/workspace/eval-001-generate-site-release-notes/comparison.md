# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-001-generate-site-release-notes`

## Test Set / Fixture Version

- Fixture: `issue-116-r2-ai-hub-shaped-v2`
- 资产：完整复用 issue #122 `assets/docs/site/**` 权威骨架、package scripts、standards 与测试
- 评估基线：`a273a00` 加本轮 issue #116 R2 working tree
- Harness：`tmp/eval-runs/116-round2/`；全新 pristine、独立 git repo、fresh with-skill、fresh zero-skill baseline 与全新独立 judge

## Latest Result

**PASS（5/5 assertions）** — 页面完整保留六类证据，符合 release frontmatter，确认前派生面有独立 SHA 快照且零变化，确认后真实执行权威 #122 docs checks，74/74 tests 通过，并输出完整 #120 ready handoff。

## With-Skill Behavior

- `preserves_six_evidence_categories`：PASS。功能、架构、数据库、部署、资产、升级兼容与风险均保留具体事实、路径、顺序和风险。
- `uses_release_frontmatter_contract`：PASS。七字段完整，`doc_type: release`，owners/related_code 非空，保持 `last_verified_version: unverified`。
- `enforces_confirmation_before_derived_writes`：PASS。确认前 index、metadata 与三份 VitePress config SHA 均等于 pristine；应用明确确认后才更新 index/metadata，导航不修改。
- `runs_real_host_docs_checks`：PASS。在隔离 git repo 的 `docs/site` 执行 `GITHUB_BASE_SHA=HEAD npm run test:docs`，exit 0，74 tests 全通过；保留 raw log 与 summary。
- `returns_complete_ready_handoff`：PASS。仅在 confirmed 加 checks 成功后 ready，所需字段齐全且 `release_execution_authorized: false`。

## Without-Skill Baseline

- 来源：round2 使用同一 prompt 与 pristine fixture 全新生成，未提供 skill 或 Agent README，未复用 round1 或历史 baseline。
- baseline 过度压缩证据，缺少完整结构化 #120 handoff 和下游门禁字段。

## Failures

- 无 assertion failure；独立 judge 未发现 harness 或协议缺陷。

## Next Steps

- 保留 #122 权威资产、确认前 SHA 快照与 raw docs-check 作为后续回归基线。

## Runtime Artifact Policy

- round2 candidate、baseline、git repo、raw logs、SHA manifests 与 judge verdict 只保留在 `tmp/eval-runs/116-round2/`，不提交到 git。
