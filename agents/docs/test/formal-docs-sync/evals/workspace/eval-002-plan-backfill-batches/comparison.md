# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-002-plan-backfill-batches`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 以 feature-catalog 为地图产出 Accounts 候选批次（路由/schema/契约测试核验），严格停在维护者确认门禁，未确认不生成页面、不写 change-map，并给出无 catalog 时的有界发现协议。

## With-Skill Behavior

- 批次粒度符合计划落定的默认值（一个业务模块、约 5 个 API 页面上限）。
- 未决事实（鉴权）明确不断言，写入时保持 unverified。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 同样提出首批范围并停在确认门禁，方向一致；差异在批次协议与 change-map 种子语义的协议化程度。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
