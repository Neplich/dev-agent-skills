# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-004-route-release-notes`

## Test Set / Fixture Version

- Fixture: `issue-116-r2-router-v1`
- 评估基线：`a273a00` 加本轮 issue #116 R2 working tree
- Harness：完整 `agents/docs/` 与 PM 共享契约；without-skill 零 skill/README；独立 fresh judge

## Latest Result

**PASS（4/4 assertions）** — router 接受完整站内 Release Notes entry basis，保留 handoff 上下文，正确选择新 specialist，并只指向其权威 gate。

## With-Skill Behavior

- `accepts_release_notes_entry_basis`：PASS。识别宿主、版本、scope、source/evidence 与站内页面加 #120 handoff 要求。
- `routes_release_notes_generator`：PASS。选择 `release-notes-generator`，排除 sync/audit/bootstrap 与 GitHub Release 执行。
- `preserves_handoff_context`：PASS。完整保留 request/change/feature/version/scope/host/source/evidence/output/risk 字段。
- `references_release_notes_gate_only`：PASS。只引用 specialist SKILL 及内部指令，不复制七步流程或执行正文生成。

## Without-Skill Baseline

- 来源：同一 prompt 与 pristine fixture 的全新 baseline；没有任何 skill/README，未复用历史结果。
- baseline 遗漏多个 handoff 字段，并把 specialist 生成步骤与 GitHub Release 混入 router 输出。

## Failures

- 无 assertion failure；router 运行只新增 candidate output，没有 specialist 执行产物。

## Next Steps

- 保留新 specialist 的窄路由和 gate 指针，后续变更继续全量刷新 router eval。

## Runtime Artifact Policy

- 运行期产物仅保留在 `tmp/eval-runs/116/`，不提交到 git。
