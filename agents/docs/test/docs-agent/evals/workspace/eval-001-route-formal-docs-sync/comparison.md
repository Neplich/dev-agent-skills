# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-001-route-formal-docs-sync`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `bf53753`

## Latest Result

**PARTIAL** — with-skill 正确接受 PM handoff 并分流到 `formal-docs-sync`，但最终输出未完整保留全部 packet 字段，也未显式给出 specialist gate 与共享 consumption contract 的权威路径指针。

## With-Skill Behavior

- 来源：本次 fresh `codex exec` 独立子进程；读取隔离工作区内的 `docs-agent` `SKILL.md`、`_internal/**` 与 Docs Agent README，并使用本 eval fixture。
- `routes_formal_docs_sync`：通过。接受 PM cross-role handoff，选择 `docs-agent:formal-docs-sync`，未改派 bootstrap 或 audit。
- `accepts_complete_handoff`：未通过。输出保留了 `request_type`、`change_tier`、`feature_path`、source documents、scope、required output 与风险摘要，但未显式保留 `feature`、`parent_feature`、`feature_level`、`feature_path_evidence`、`downstream_owner` 等全部字段。
- `references_specialist_gate_only`：未通过。未执行 specialist，但没有显式指向 `formal-docs-sync/SKILL.md` 及其内部指令。
- `recognizes_shared_consumption_contract`：未通过。未给出 `agents/product_manager/skills/idea-to-spec/_internal/_shared/consumption-contract.md` 权威指针。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture；隔离约束下未读取或应用 skill / Agent README。
- baseline 也接受 handoff 并选择 `formal-docs-sync`，但同样没有完整保留 packet 字段，也没有 specialist gate 或共享 consumption contract 的路径指针。

## Failures

- with-skill 未满足 3 条输出契约断言：完整 packet 字段保留、specialist gate 路径指针、共享 consumption contract 路径指针。

## Next Steps

- 后续 docs-agent router 变更应让最终 handoff 输出显式保留完整 packet 字段，并仅以权威路径指向 specialist gate 与共享 consumption contract；修正后重新执行本 eval。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
