# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-002-missing-entry-basis`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `bf53753`

## Latest Result

**PASS** — with-skill 对模糊建站请求准确指名缺失凭据（已确认宿主仓库路径），不执行 bootstrap、不写任何文件，温和引导经 `pm-agent` 补齐分类与前置上下文。

## With-Skill Behavior

- 来源：本次 fresh `codex exec` 独立子进程；读取隔离工作区内的 `docs-agent` `SKILL.md`、`_internal/**` 与 Docs Agent README，并使用本 eval fixture。
- `guides_to_pm_agent`：通过。明确没有 PM handoff packet 或等效确认文档链，并引导先经 `pm-agent` 分类。
- `does_not_execute_bootstrap`：通过。未创建 `docs/site/`、未加载或复述 bootstrap 模板、未生成 manifest，也未修改 fixture。
- `names_missing_credentials`：通过。明确缺少已确认的宿主仓库路径，并说明补齐路径后才能路由到 `docs-site-bootstrap`。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture；隔离约束下未读取或应用 skill / Agent README。
- baseline 也返回 PM 前置门禁且未建站，但把缺口扩展为受众、信息架构和验收标准，没有准确指出“显式建站请求 + 已确认宿主仓库路径”即可构成该 specialist entry basis。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
