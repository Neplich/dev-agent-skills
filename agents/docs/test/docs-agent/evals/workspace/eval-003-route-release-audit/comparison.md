# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-003-route-release-audit`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `bf53753`

## Latest Result

**PARTIAL** — with-skill 识别等效已确认发布链并分流到 `docs-audit`，保留 release scope、版本、changelog 与检查证据，但未显式给出 `docs-audit/SKILL.md` 及内部指令的权威路径，并带出了部分审计执行条件。

## With-Skill Behavior

- 来源：本次 fresh `codex exec` 独立子进程；读取隔离工作区内的 `docs-agent` `SKILL.md`、`_internal/**` 与 Docs Agent README，并使用本 eval fixture。
- `accepts_equivalent_chain`：通过。接受 `release-entry.md` 中的 release scope、`v0.4.0`、changelog、检查证据与审计请求。
- `routes_docs_audit`：通过。选择 `docs-audit` 并保留版本、changelog、正式站点和检查证据，未执行正式文档审计。
- `references_audit_gate_only`：未通过。输出只泛称“权威 gate”，未显式指向 `docs-audit/SKILL.md` 及其内部指令，并复述了“全部页面验证后统一版本标记”等部分审计条件。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture；隔离约束下未读取或应用 skill / Agent README。
- baseline 也识别等效 release chain 并分流到正式文档审计，但只使用通用 specialist 名称，没有权威 gate 路径指针。

## Failures

- with-skill 未满足审计 specialist gate 的显式路径指针与“不复制执行协议”断言。

## Next Steps

- 后续 docs-agent router 变更应让 handoff 仅显式指向 `docs-audit/SKILL.md` 及内部指令，不复述 specialist 执行条件；修正后重新执行本 eval。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
