# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-012-staged-metadata-rollback`
- Validation time: `2026-07-20 00:00:33 CST`
- Target behavior: staged/committed convergence 的 metadata 边界与失败事务回滚。

## Test Set / Fixture Version

- Fixture version: current working-tree fixture / 2026-07-19
- Fixture source: `evals.json` 中 eval-012 的 prompt/assertions、`eval_metadata.json`、`.eval/staged-convergence-evidence.md` 与 `.eval/prewrite-fingerprint.md`。
- Assertions: 5
- Fresh pair: 本会话先在不读取或应用 `docs-audit` skill、内部指令及 Docs Agent README 的条件下生成 baseline；随后读取完整 skill 指令，并针对同一份 pristine fixture 重新生成 with-skill 结果。

## Latest Result

**PASS — fresh with-skill 5 / 5 assertions passed.** 候选把初始与 final-record staged gate、`target_ref..anchor_commit` 及 anchor-to-handoff committed gate 统一约束为 raw mode/type/object identity、禁用 rename/copy folding 的 status、summary 与 full binary patch 检查。fixture 中 executable-bit、blob-to-symlink、rename、delete 和额外 symlink path 均使 candidate `blocked`；事务不得创建 anchor/handoff，也不得返回 `ready_for_tag`。

Fresh without-skill baseline 同为 **5 / 5**。本例 prompt、assertions 与 fixture 已直接列出所有差异维度、恢复动作和复核指纹，因此 baseline 也能完整重述预期边界；本结果证明当前 skill 没有行为回退，但该用例暂未形成 assertion-level 的差异化增益。

## Assertion Results

| Assertion | With skill | Without skill | Evidence summary |
| --- | --- | --- | --- |
| `checks_raw_metadata_not_only_content` | PASS | PASS | 两者均要求初始与最终 staged gate 检查 raw old/new mode、object identity/type、禁用 rename/copy folding 的 name-status、summary 和 full binary patch，不以白名单路径或文本行替代 metadata 检查。 |
| `rejects_mode_type_symlink_rename_delete` | PASS | PASS | 两者均拒绝 `100644→100755`、`100644 blob→120000 symlink`、R/C、D、path swap、gitlink、非 `100644` record 和额外 symlink path；同名白名单不豁免 mode/type 越界。 |
| `applies_same_gate_after_commit` | PASS | PASS | 两者均把相同 raw/status/type/mode/path/content/full-patch gate 重跑于 `target_ref..anchor_commit` 与 anchor-to-handoff delta，fixture 的假设 committed metadata delta 仍使 candidate invalid。 |
| `rolls_back_failed_candidate_transaction` | PASS | PASS | 两者均在 staged gate 失败后删除隔离 worktree/temp ref，不创建 candidate、anchor 或 handoff commit；仅按 pre-write bytes/mode/type 恢复误触授权路径/index，移除本 attempt 草稿并保留无关用户变化。 |
| `proves_no_half_stamp_residue` | PASS | PASS | 两者均使用 branch SHA、porcelain v2、staged/unstaged raw diff、相关路径 mode/type/hash 对照捕获状态；无法证明完全恢复时继续 `blocked`，列出残留和人工恢复命令，并禁止建 tag。 |

## With-Skill Behavior

- 来源：本会话 fresh with-skill 评审；读取当前 `docs-audit` SKILL、完整内部协议、Docs Agent README、eval 定义和 pristine fixture。
- 结果：5 / 5。skill 明确规定两次 staged gate、两段 committed gate 和 integration 前宿主指纹复核共享同一 metadata/content 边界。
- 裁定：fixture 在首次 staged 收敛即 `blocked`；不创建 candidate/anchor/handoff/discovery，不返回 `ready_for_tag`。清理隔离 attempt 后仅在宿主指纹完全复原时结束恢复，否则维持 blocker。

## Without-Skill Fresh Baseline

- 来源：本会话全新 baseline；只读取 eval prompt/assertions、`eval_metadata.json` 和两份 fixture evidence，未读取或应用 skill、Docs Agent README、历史 baseline 或历史 comparison。
- 结果：5 / 5。baseline 根据 fixture 显式证据逐项拒绝 mode/type/path/status 越界，并给出事务清理与指纹复核。
- 对比结论：baseline 已被高指令密度的测试输入充分引导；skill 的阶段权威性和事务顺序更明确，但未转化为额外 assertion 得分。

## Failures and Limitations

- With-skill 无失败；without-skill 无 assertion 失败。
- 当前 fixture 是合成 evidence，不执行真实 Git index/worktree、临时 ref 或 commit 操作。
- baseline 5 / 5 表明本例区分度不足：它验证协议可被 skill 正确执行，但不能单独证明这些边界只能由 skill 提供。

## Next Steps

- 后续如增强 eval 区分度，可减少 prompt/assertions 中对恢复命令和 committed gate 顺序的直接提示，并用真实 Git harness 验证 mode/type、rename/delete、隔离 ref 清理及宿主指纹恢复。

## Runtime Artifact Policy

- 本轮未创建 transcript、candidate output、subagent verdict、timing、diagnostics、with-skill/without-skill 目录或其他 runtime artifact。
- Durable 结果仅为本 `comparison.md`；未复用历史 baseline。
