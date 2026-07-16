# Consumption Regression Comparison

## Evaluation Target

- Skill: `codebase-analyzer`
- Eval: `eval-003-mapped-search-architecture`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

**PASS** — with-skill 输出满足全部 3 条断言：命中 change-map 后以映射文档 `docs/site/api/search.md` 为地图、以 `src/search/query.txt` 为 ground truth 核证出"文档声称模糊匹配、代码只实现精确匹配"的分歧，并按 `unverified` 最低信任规则以代码为准。

## With-Skill Behavior

- 显式声明按 consumption contract 执行，只读取命中的映射文档，未做无关文档遍历。
- 产出契约要求的结构化分歧表（文档路径 / 文档声明 / 代码事实 / 影响），可直接供 `docs-audit` 消费。
- 对 `last_verified_version: unverified` 显式引用最低信任规则，全部关键能力结论以代码证据支撑，未证实项明确标注"无法确认"。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 也识别了模糊/精确匹配分歧并倾向以代码为准，但没有产出契约格式的结构化分歧证据，信任降级是临场推断而非协议行为。

## Failures

- 无。

## Next Steps

- 保留本结果；后续可在 fixture 中加入多个无关文档以放大"精准读取"与全库遍历的行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
