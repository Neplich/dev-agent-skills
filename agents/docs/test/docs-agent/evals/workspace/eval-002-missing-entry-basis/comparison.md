# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-002-missing-entry-basis`

## Test Set / Fixture Version

- Fixture: `ws2-docs-v1`
- Commit: `c05f689`

## Latest Result

**PASS** — with-skill 对模糊建站请求准确指名缺失凭据（已确认宿主仓库路径），不执行 bootstrap、不写任何文件，温和引导经 pm-agent 补齐分类与前置上下文。

## With-Skill Behavior

- 部分满足的 entry basis 按协议视同缺失，未先分流再让 specialist 收集凭据。
- 本 eval 首轮运行暴露了 router 对部分凭据场景的表述缺口，已通过 SKILL.md 补丁（partially satisfied basis 规则）修复后复跑通过。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 文档。
- baseline 以 PM 澄清三选项响应，方向合理但未指名 specialist entry basis 的具体构成。

## Failures

- 无。

## Next Steps

- 保留本结果。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
