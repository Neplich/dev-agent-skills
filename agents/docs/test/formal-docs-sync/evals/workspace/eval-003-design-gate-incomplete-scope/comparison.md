# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-003-design-gate-incomplete-scope`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 识别实施计划内 SCOPE-02 为 TODO 后原子性 blocked：设计页与 design change-map 条目哈希级零变化，指名未完成条目、owner（feature-implementor）与解锁路径，阻塞期间不写临时/部分设计。

## With-Skill Behavior

- 完成态门禁第 4 项精确触发，未采信其余证据齐全的表象。
- 未写入校验以文件哈希与 git status 双重确认，原子性证据充分。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 同样保持零变更并要求先完成 SCOPE-02，方向一致；差异在门禁编号化执行与原子范围的显式声明。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
