# Eval Result: eval-002-mapped-doc-incident-playbook

## Evaluation Target

- Agent: `devops`
- Skill: `incident-playbook-writer`
- Eval: `eval-002-mapped-doc-incident-playbook`
- Test case: mapped-doc-incident-playbook
- Workspace: `workspace/eval-002-mapped-doc-incident-playbook`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: issue #196 L2-3；`src/runtime/health.rules`、change-map 与 unverified 健康检查文档
- Expected output: 以代码事实确定告警阈值的最小故障处置步骤，并记录映射文档差异

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**（3/3 assertions exercised）
- Overall result: PASS
- 运行日期：2026-07-31

## Assertions

- PASS `reads_mapped_docs_first`: 任务落点命中 change-map 后先读取唯一 required doc，未遍历
  其他站点文档。
- PASS `verifies_against_code`: 识别文档阈值 3 与代码阈值 5 的差异，以代码值为准并说明处置
  时机影响。
- PASS `treats_unverified_as_low_trust`: 将 `last_verified_version: unverified` 按最低信任
  处理，关键阈值回到代码核证。

## With-Skill Behavior

- 来源：当前会话 fresh Codex validator；先读取 DevOps Agent README、skill、消费契约、
  同一原始 prompt 与 fixture，在 baseline 生成前写入并以 SHA-256 锁定。
- 从 `src/runtime/health.rules` 任务落点反查 change-map，先读唯一映射文档，再回到代码核证。
- 以代码阈值 5 为准，明确指出文档值 3 会让处置提前两个检查周期；无部署证据时不臆造命令。

## Without-Skill Baseline

- 来源：with-skill 候选锁定后，使用同一原始 prompt 与 fixture fresh 生成；生成时不读取或
  应用 skill、Agent README、with-skill 输出、历史 comparison 或旧 baseline。
- baseline 同样识别文档值 3、代码值 5 与 `unverified` 信任问题，但其读取顺序是先检查
  任务直接指向的代码，再对照 change-map 与映射文档。
- baseline 满足 2/3 assertions；差异集中在 mapped-doc-first 消费顺序。

## Failures

- with-skill 无 assertion failure。
- baseline 失败：`reads_mapped_docs_first`，未先以 change-map 定位并读取 required doc。

## Next Steps

- 保留 mapped-doc-first 与代码核证断言；本轮不新增干扰 fixture。

## Runtime Artifact Policy

- with-skill、fresh without-skill、锁定清单与 judge 只写入
  `tmp/eval-runs/issue-196-l2-3-4/incident-playbook-writer/eval-002-mapped-doc-incident-playbook/`。
- 运行期 candidates、verdicts、timing、outputs 与 diagnostics 不提交；只提交本
  `comparison.md`。
