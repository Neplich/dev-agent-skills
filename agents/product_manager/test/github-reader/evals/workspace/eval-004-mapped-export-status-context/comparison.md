# Consumption Regression Comparison

## Evaluation Target

- Skill: `github-reader`
- Eval: `eval-004-mapped-export-status-context`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 输出满足全部 3 条断言：按 `src/export/` 落点聚焦读取映射文档 `docs/site/api/export.md`、以 `src/export/handler.txt` 核证出"文档声称支持 JSON 但实现声明只有 CSV"的分歧并给出交付风险，`unverified` 文档不作为已交付依据。

## With-Skill Behavior

- 显式声明按 consumption contract 执行，围绕命中文档与代码证据做聚焦核验，未做全库文档遍历。
- 以证据表结构化呈现 CSV/JSON 状态分歧与交付风险分级，结论"部分准备、尚未形成可验收交付"完全由证据支撑。
- 显式引用 `last_verified_version: unverified` 判定文档可信度最低。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 同样发现 CSV/JSON 冲突并给出风险分级，质量较高；但对文档信任度的处理是临场推断，未按契约以命中文档为地图组织读取顺序。

## Failures

- 无。

## Next Steps

- 保留本结果；可考虑在 fixture 中增加多份未映射文档以放大精准读取差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
