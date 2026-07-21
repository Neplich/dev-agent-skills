# Eval Result: eval-003-python

## Evaluation Target

- Agent: `security`
- Skill: `dependency-risk-auditor`
- Eval: `eval-003-python`
- Test case: Python Dependency Audit
- Workspace: `workspace/eval-003-python`
- Review context: PR #149 review 修复轮，保留 issue #143 上下文
- Latest result: PASS（4/4 assertions）- fresh paired validation completed on 2026-07-21

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt/fixture: PR #149 review 修复后的 fixture；包含 `PM_HANDOFF.md`、`docs/pm/dependency-inventory/PRD.md` 与 `requirements.txt`，其中版本为 `requests==2.19.1`、`urllib3==1.23`、`Jinja2==2.10.1`
- Fixture evidence: 本轮 `uv` resolver dry-run 成功解析 7 个包，确认 `urllib3==1.23` 满足 requests 2.19.1 的 `>=1.21.1,<1.24` 约束；精确 pin 审计报告 3 个直接依赖共 24 条已知漏洞记录
- Fresh run: `tmp/eval-runs/issue-143-r2`；with_skill 读取当前 Security Agent README 与 `dependency-risk-auditor`，without_skill 基于同一 prompt/fixture 在本轮重新生成，未读取或应用 skill/Agent README、历史 comparison、with_skill 输出或 assertions
- Audit execution note: 常规 `pip-audit -r` 因临时环境 `ensurepip` SIGABRT 失败；候选改用 `pip-audit --no-deps --disable-pip` 审计精确 pin，并以独立 `uv` dry-run 验证依赖可解析性，未把工具故障当成安全结论
- Source head: `test/issue-143-security-thin-fixtures` (`1a91659`，fixture 修复提交前工作树)
- Validation date: 2026-07-21

## Assertions

- PASS `dependency_inventory`：识别 Python/PyPI 生态及 `requests==2.19.1`、`urllib3==1.23`、`Jinja2==2.10.1` 三个直接依赖，并说明 HTTP/TLS、模板、无 hash pin 与未审计传递依赖等风险来源
- PASS `risk_classification`：区分已知漏洞、过期 pin、完整性风险和 fixture 无法证实的废弃/所有权变化风险，以利用条件为边界将总体及三个直接依赖的主要问题判为 High
- PASS `evidence`：引用 `requirements.txt` 精确版本、resolver 成功结果和本轮精确 pin 审计结果，并明确 `--no-deps` 及缺少调用代码的证据边界
- PASS `upgrade_plan`：给出 requests 2.33.0+、urllib3 2.7.0+、Jinja2 3.1.6+ 的协调升级方向、重新解析与全依赖扫描、HTTP/TLS/代理/模板回归，以及无法立即升级时的临时缓解

## With Skill Behavior

本轮候选先验证修复后的依赖集可以解析，再以精确 pin 和实际审计结果形成结构化证据，消除了旧 fixture 自相冲突对风险结论的干扰。它区分“可安装”与“安全”，也没有把版本陈旧直接推导为整个包已废弃；报告包含严重度、利用条件、升级顺序、临时缓解、验证范围及 Engineer、DevOps、PM 的协作边界。

## Without Skill Baseline

本轮 fresh baseline 识别三项精确 pin、Requests/urllib3/Jinja2 的主要风险来源，把三个问题列为高优先级，并给出联合升级、扫描、回归和临时缓解，因此满足 4/4 assertions。其证据精度和边界控制弱于 with_skill：没有列出实际 advisory/CVE 或扫描结果、没有精确安全目标版本，并把 `urllib3==1.23` 表述为“已停止维护的老版本”，但 fixture 本身没有维护状态证据；该无证据断言记录为 baseline 质量差异，不影响 with_skill 的 PASS。

## Failures

- with_skill 无 assertion failure。
- fresh without_skill baseline 无 assertion failure；存在一处未由 fixture 支撑的维护状态断言。
- 常规 pip-audit 临时环境失败已由精确 pin 审计和独立 resolver 检查补足证据，不构成本轮判断阻塞。

## Next Steps

- 当前 eval 无需修改 skill、assertions 或 fixture；后续依赖 fixture 或审计行为变化时，继续执行同 prompt/fixture 的 fresh paired run，并重新生成 without_skill baseline。

## Runtime Artifacts Policy

- 本轮 paired 输出、解析和审计临时证据仅位于 `tmp/eval-runs/issue-143-r2`，不提交到 git。
- `with_skill/`、`without_skill/`、transcript、verdict、timing、diagnostics 及其他运行期产物均不得提交；durable 结果仅为本 `comparison.md`。
