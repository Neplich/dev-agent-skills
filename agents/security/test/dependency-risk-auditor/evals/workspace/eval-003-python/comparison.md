# Eval Result: eval-003-python

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-003-python`
- Test case: Python Dependency Audit
- Workspace: `workspace/eval-003-python`
- Review context: issue #143
- Latest result: PASS（4/4 assertions）- fresh Codex paired validation completed on 2026-07-21

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt/fixture: issue #143 当前 fixture；包含 `PM_HANDOFF.md`、`docs/pm/dependency-inventory/PRD.md` 与固定版本的 `requirements.txt`
- Fresh run: 当前会话中新启动的 fresh Codex validator 在 `tmp/eval-runs/issue-143/batch-c/eval-003-python/` 的隔离副本中成对运行；with-skill 读取当前 specialist SKILL.md、Security README 与共享 closeout 契约，without-skill 仅以同一 prompt/fixture 重新生成 baseline，未读取历史 comparison，未复用历史 baseline
- Audit evidence: `uvx pip-audit -r requirements.txt --no-deps --disable-pip -f json`；返回码 1，检出 3 个直接依赖中的 25 条已知漏洞记录
- Source head: `test/issue-143-security-thin-fixtures`
- Validation date: 2026-07-21

## Assertions

- PASS `dependency_inventory`：识别 Python 生态及 `requests==2.19.1`、`urllib3==1.24.1`、`Jinja2==2.10.1` 三个直接依赖，并指出 HTTP/TLS、模板、未哈希固定版本及未覆盖传递依赖等风险来源
- PASS `risk_classification`：区分已知漏洞、明显过期、供应链完整性与未能由 fixture 证实的废弃风险；按利用条件说明凭据泄漏、TLS/重定向、CRLF、解压资源消耗、XSS/沙箱逃逸等高优先级风险
- PASS `evidence`：引用 `requirements.txt` 精确版本及本轮 pip-audit 的包级 advisory 结果，并明确 `--no-deps` 的证据边界
- PASS `upgrade_plan`：给出 Requests 2.33.0、urllib3 2.7.0、Jinja2 3.1.6 的协调升级目标、兼容性验证项及无法立即升级时的重定向、TLS、代理、解压和模板缓解措施

## With Skill Behavior

with-skill 输出先验证 PM handoff 与 `feature_path=dependency-inventory`，再以 PRD、精确版本清单和实际审计命令形成结构化证据。它没有把“旧版本”直接等同于“已废弃”，而是区分已证实漏洞、过期、供应链和待核实的可利用性/维护状态；同时给出升级顺序、临时缓解、测试范围以及 Engineer、DevOps、PM 的边界。由于结论影响 release readiness，输出也正确保留 Security 报告并回交 PM 分类，而不是自行修改依赖或正式文档。

## Without Skill Baseline

本轮 baseline 在独立 `without_skill` 副本中，仅依据相同 prompt、PM handoff、PRD 与 `requirements.txt` 新生成。它识别了三个固定依赖、主要漏洞类型、版本证据、升级/缓解与传递依赖扫描需求，但只给出优先顺序，没有明确的严重度等级，故 baseline 为 3/4（`risk_classification` 未完全满足）。baseline 也未形成 Security 报告落点、角色 handoff 或 Security→PM closeout 语义。

## Failures

- with-skill 无 assertion failure。
- without-skill 对照缺口：未明确严重度等级，`risk_classification` 不完全满足；这不影响 with-skill 的 PASS 结论。

## Next Steps

- 本 eval 无需修改 assertions 或 expected_output；后续依赖审计 fixture 或 skill 行为变化时继续执行新的 fresh Codex paired run，并重新生成 baseline。

## Runtime Artifacts Policy

- 本轮 paired 输出、pip-audit 输出与临时隔离副本仅用于判定，完成后删除 `tmp/eval-runs/issue-143/batch-c`。
- 不提交 with_skill、without_skill、transcript、verdict、timing、output、diagnostics 或其他运行期产物；durable result 仅为本 `comparison.md`。
