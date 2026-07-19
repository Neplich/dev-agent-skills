# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-003-route-release-audit`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- 评估基线：`a273a00` 加本轮 issue #116 R2 working tree
- Harness：完整 router harness、fresh zero-skill baseline 与独立 judge

## Latest Result

**PASS（3/3 assertions）** — router 接受等效确认 release chain，保留版本和 release 证据，正确选择 `docs-audit`，且只引用 specialist gate。

## With-Skill Behavior

- `accepts_equivalent_chain`：PASS。保留 release scope、v0.4.0 tag、reviewed changelog、contract/CI 证据和既有站点。
- `routes_docs_audit`：PASS。选择 `docs-audit` 并排除 bootstrap、sync、Release Notes。
- `references_audit_gate_only`：PASS。只指向 `docs-audit/SKILL.md` 及内部指令，不复制或执行审计协议。

## Without-Skill Baseline

- 来源：同 prompt/fixture 的 fresh baseline，不含 skill/README，未复用历史结果。
- baseline 路由方向正确，但开始复述并承诺执行审计与盖章，越过 router 边界。

## Failures

- 无 assertion failure；fixture 到 with_skill 仅新增 candidate output。

## Next Steps

- 继续以路径指针保持 router 与 specialist gate 单一真源。

## Runtime Artifact Policy

- 运行期产物仅保留在 `tmp/eval-runs/116/`，不提交到 git。
