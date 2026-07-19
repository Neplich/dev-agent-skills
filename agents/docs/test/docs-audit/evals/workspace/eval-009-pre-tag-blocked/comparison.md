# Fresh Paired Validation: eval-009-pre-tag-blocked

## Evaluation target

- Skill: `docs-audit`
- Eval: `eval-009-pre-tag-blocked`
- Validation time: `2026-07-20 00:00:33 CST`
- Fixture: 本轮工作区中的 `evals.json` prompt/assertions、`eval_metadata.json` 及其列出的 pristine fixture 文件
- Latest result: **PASS（4/4 assertions）**

## Run sources

- `without_skill`: fresh baseline；先仅读取本例 prompt、assertions、metadata 与 fixture，未读取或应用 docs-audit skill、Docs Agent README 或旧 `comparison.md`。
- `with_skill`: fresh candidate；baseline 冻结后完整读取 `docs-audit/SKILL.md`、`docs-audit/_internal/INSTRUCTIONS.md` 与 `agents/docs/README.md`，并在同 prompt/pristine fixture 下重新判断。
- 本轮没有复用历史 baseline、旧 comparison 内容或历史运行产物。

## Assertion review

| Assertion | Without skill | With skill | Evidence and behavior |
| --- | --- | --- | --- |
| `requires_exact_target_tree_blobs` | PASS | PASS | Baseline 能识别未提交 patch 不属于 `release-head`，不能作为通过证据。Skill §1 input gate 与 §4 step 2 进一步限定 passing evidence 必须是精确 target_ref tree 的 ordinary blob；工作区、index、untracked 和 later-branch bytes 仅可诊断。 |
| `blocks_every_in_scope_worktree_delta` | PASS | PASS | 两侧均逐项解析 porcelain：staged `src/catalog/routes.txt` 属事实证据，unstaged `catalog-items.md` 属 affected page，untracked candidate draft 属 authorized write path，modified `package.json` 属 required version inventory；每一项都独立阻塞。Skill 明确不需要调用方先把差异声明为 passing evidence。 |
| `performs_zero_audit_writes` | PASS | PASS | Baseline 在 dirty scope 下直接 blocked。Skill §4 step 2 和失败事务规则要求在建 candidate 前阻塞，不判页为 verified、不盖章、不建 candidate/anchor/discovery/handoff commit、不返回 `ready_for_tag`，并保持宿主 branch/worktree/index 原状。 |
| `requires_clean_commit_update_ref_and_rerun` | PASS | PASS | 两侧均要求维护者提交需保留的最终内容或移出全部 scope 内差异，再把 `target_ref` 更新到最终 commit、确认 scope/index 干净，并从输入解析开始完整重跑；Skill 明确不允许局部续跑或用补证修复本次尝试。 |

## Behavior summary

### With skill

在任何事实核对或审计写入前，完整列出四个独立 scope intersection，并将阶段判为 `blocked`。所有未提交内容仅作为诊断上下文；不会创建隔离事务或修改宿主状态。重跑条件覆盖全部差异处置、目标 ref 更新、scope 清洁确认和从头执行完整 pre-tag protocol。

### Without skill baseline

本例 prompt、release context 与 porcelain inventory 已清楚给出未提交证据和四类 scope 交集，因此 baseline 也能正确阻塞、保持零写入并要求完整重跑。Skill 的增益主要是把“任何 scope/authorized path/required inventory 差异都独立阻塞”和“只接受 target-tree ordinary blob”固化为不可绕过的协议。

## Failures

- With skill: 无 assertion failure。
- Without skill: 无 assertion failure。

## Next steps

- 无需修改 skill；保留本例验证 dirty scope 的 fail-closed 行为和完整重跑要求。

## Runtime artifact policy

本轮仅持久化此 `comparison.md`。未创建或提交 `with_skill/`、`without_skill/`、transcript、candidate output、subagent verdict、timing、run status、diagnostics 或其他临时/runtime 产物。
