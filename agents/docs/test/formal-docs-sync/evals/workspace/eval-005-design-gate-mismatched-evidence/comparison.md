# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-005-design-gate-mismatched-evidence`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 发现 PRD/TRD 元数据（account-preferences）与请求 feature_path（preferences-summary）不一致后原子性 blocked：设计页与 change-map 零变化，回 pm-agent 确认规范路径、trd-gen 对齐 TRD；即便识别出设计页确实过期也不越权修订。

## With-Skill Behavior

- 证据归属校验优先于内容判断，不把目录位置或测试通过当作范围确认。
- blocked 输出含缺失证据、owner 与下一步，完整符合门禁协议。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 同样保持零改动并要求先对齐元数据，方向一致；差异在门禁清单的协议化执行与 blocked 输出结构。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
