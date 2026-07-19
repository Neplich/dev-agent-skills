# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-002-confirmation-gate`

## Test Set / Fixture Version

- Fixture: `issue-116-r2-ai-hub-shaped-v2`
- 资产：完整复用 issue #122 `assets/docs/site/**` 权威骨架与 package/scripts
- 评估基线：`a273a00` 加本轮 issue #116 R2 working tree
- Harness：`tmp/eval-runs/116-round2/` 的全新双方结果、独立 git repo 与全新 judge

## Latest Result

**PASS（3/3 assertions）** — 未确认时只生成完整候选页，index、metadata 与导航保持零变化；handoff 明确 blocked/unconfirmed 并等待确认。权威 #122 checks 的 74/74 结果仅作为 harness preflight，不是 release-ready 证据。

## With-Skill Behavior

- `keeps_derived_surfaces_unchanged`：PASS。未确认 SHA 记录与当前复算均证明 index、metadata、三份 VitePress config 等于 pristine；无派生面 diff。
- `reports_unconfirmed_not_ready`：PASS。`confirmation_status: unconfirmed`、`handoff_status: blocked`、正式 `docs_checks: not_run`，updated surfaces 全为空。
- `waits_for_explicit_confirmation`：PASS。展示完整六类正文、来源、风险与确认后路径，fixture 无确认记录，候选没有模拟确认。
- Harness preflight：在隔离 git repo 执行 `GITHUB_BASE_SHA=HEAD npm run test:docs`，exit 0、74/74；单列为 `release_ready_evidence: false`。

## Without-Skill Baseline

- 来源：round2 同 prompt/fixture 全新生成，零 skill/README，未复用 round1。
- baseline 在正文未确认时先行写入 index 与 metadata，也没有 blocked/unconfirmed handoff。

## Failures

- 无 assertion failure；独立 judge 未发现 harness 或协议缺陷。

## Next Steps

- 保持正式 docs checks 与 harness preflight 分离，防止未确认候选被误报 ready。

## Runtime Artifact Policy

- round2 运行期文件只保留在 `tmp/eval-runs/116-round2/`，不提交到 git。
