# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-002-confirmation-gate`

## Test Set / Fixture Version

- Fixture: `issue-126-r3-lockfile-v1`
- 评估基线：PR #126 R3 working tree
- Harness：`tmp/eval-runs/126-r3-docs-release/eval-002-confirmation-gate/`
- Fresh validation：当前会话全新 subagent 先执行 with-skill，再以同一 prompt 和 pristine fixture 作 fresh zero-skill 对照判断；未复用历史 baseline。

## Latest Result

**PASS（3/3 assertions）** — 未确认时只生成完整候选页，index、metadata 与导航保持零变化，handoff 明确 blocked/unconfirmed 并等待维护者确认。

## With-Skill Behavior

- `keeps_derived_surfaces_unchanged`：PASS。scratch git 仅出现候选 `v1.0.0.md` 与运行期依赖，`release-notes/index.md`、`.meta/releases.json` 和导航配置无 diff。
- `reports_unconfirmed_not_ready`：PASS。候选正文没有被描述为 #120 ready；状态停在 `confirmation_status: unconfirmed` / blocked。
- `waits_for_explicit_confirmation`：PASS。候选页完整覆盖六类证据并列出来源；fixture 没有确认记录，没有模拟确认或执行确认后的派生写入。
- 确定性入口：在干净依赖状态执行 `npm ci --ignore-scripts` 成功。未确认流程不把 docs check 当作 release-ready 证据；一次 harness preflight 在候选页生成前因专用测试找不到 `v1.0.0.md` 为 73/74，此结果不改变确认门禁判定。

## Without-Skill Baseline

- 来源：当前 fresh subagent 对同 prompt/pristine fixture 的 zero-skill control 直接判断；control 不读取或应用目标 skill 与 Docs Agent README。
- 宿主 README 明示未确认不得改 index/metadata/navigation，因此对照可发现基本门禁；但没有目标 skill 的结构化 blocked handoff 与 #120/#117 边界，输出稳定性较弱。

## Failures

- 无 assertion failure。preflight 的缺候选页失败发生在候选生成前，只作为 harness 时序诊断保留，不作为 release-ready check。

## Next Steps

- 未确认 eval 的 fixture preflight 应在候选页面物化后运行，或明确排除依赖目标页面的专用测试。

## Runtime Artifact Policy

- 候选页、依赖目录、命令输出和 scratch git 仅保留在 `tmp/eval-runs/126-r3-docs-release/`，不提交到 git。
