# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-002-repeat-bootstrap-idempotent`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 重复执行零内容变更：4 个代表性目标 skipped-identical、createdAt 与 manifest SHA 保持不变，change-map 与 releases.json 未被重置。

## With-Skill Behavior

- 逐项字节比较后不重写任何文件，Git 层面 zero-diff 有明确证据。
- 既有正式页面与数据文件全部保留。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 同样实现幂等零改动，行为一致；差异在 manifest 持久状态语义（createdAt 保留、状态机）的协议化表述。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
