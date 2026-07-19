# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-site-bootstrap`
- Eval: `eval-003-block-bootstrap-conflict`

## Test Set / Fixture Version

- Fixture: `issue-122-assets-conflict-v1`
- Branch fixture commit: `a2a30a3`
- Fresh validation date: `2026-07-19`

## Latest Result

**PASS** — fresh judge 对 3 条 assertions 全部判定 PASS。with-skill 完整分类 38 个静态目标，将宿主定制的 `standards/index.md` 识别为唯一冲突并 blocked，用户选择前未覆盖、合并、格式化或登记成功状态。

## With-Skill Behavior

- 完整分类为 35 个缺失、2 个 `skipped-identical`、1 个冲突；缺失路径清单与 packaged inventory 完全对应。
- 冲突文件执行前后 SHA-256 均为 `e5d8cccfa9cebeb2a16d191b58b709b67fd3b7b9fa412d4a7789e8e03cfbadfa`。
- Manifest 前后字节一致，只保留 package 与 releases 的两个 `skipped-identical` 状态，没有为冲突路径制造成功或 `kept-as-is` 状态。
- 明确提供 overwrite、显式 merge、keep 三类逐文件选择，并说明只有用户选择 keep 后才登记 `kept-as-is`。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，使用相同原始 prompt 与 fixture，新生成且未提供任何 skill 文档或 Agent README。
- baseline 同样阻断冲突、保持文件和 manifest 不变，并给出三类选择；但只把其余 35 项概括为“缺失或字节一致”，没有给出逐文件完整分类。
- baseline 结果仅作为对照输入，不影响 with-skill 的 PASS 判定。

## Failures

- 无 assertion failure。with-skill 的一次只读检查命令使用了 zsh 保留变量名，重试后完成分类且未造成文件变化。

## Next Steps

- 真实 bootstrap 遇到同类冲突时继续等待用户逐文件选择；选择前不得补写缺失资产或更新 manifest。

## Runtime Artifact Policy

- 本次 transcripts、workspace 副本、baseline 和 judge verdict 仅位于 `tmp/eval-runs/122/eval-003-block-bootstrap-conflict/`，不提交到 git。
