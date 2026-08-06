# Fresh Paired Validation: eval-009-pre-tag-blocked

## Evaluation target

- Skill: `docs-audit`
- Eval: `eval-009-pre-tag-blocked`
- Validation time: `2026-08-03 22:40:00 +0800`（fresh re-baseline，issue #188）
- Fixture: 本轮工作区中的 `evals.json` prompt/assertions、`eval_metadata.json` 及其列出的 pristine fixture 文件
- Latest result: **PASS**（Behavior: PASS / Coverage: FULL）
- Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `PASS` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `requires_exact_target_tree_blobs` | PASS | PASS | 两条 lane 均指出 `release-head` 仍为 legacy dispatcher；`.eval/actual-diff.patch` 中的 table dispatcher 仅存在未提交差异，不能作为 target tree 证据。 |
| `blocks_every_in_scope_worktree_delta` | PASS | PASS | 两条 lane 均逐项识别 staged `src/catalog/routes.txt`、unstaged `docs/site/api/catalog-items.md`、untracked 审计草稿和 modified `package.json`，并判定阻塞。 |
| `performs_zero_audit_writes` | PASS | PASS | 两条 lane 均输出 `blocked`，明确不返回 `ready_for_tag`、不创建候选或修改主机文件；workspace 中也未发现候选/盖章产物。 |
| `requires_clean_commit_update_ref_and_rerun` | PASS | PASS | 两条 lane 均要求先提交或移出全部差异、更新 `target_ref`、确认范围干净，再从 pre-tag 流程第一步完整重跑，拒绝局部续跑。 |

本轮无 FAIL 断言。



## Fixture Drift Notice

fixture 身份文本已于 2026-07-29 从 issue 编号更新为 skill 名，旧 PASS 反映变更前 run。**2026-08-03（#188）已对当前 fixture 完成 fresh re-baseline**（with/without 双侧验证，judge 独立判定，证据见 `tmp/eval-runs/issue-188-docs/`），BLOCKED 状态消解；本节保留作为历史记录。

## Historical results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 2026-07-20（fixture 身份文本变更前）：**PASS（4/4 assertions）**

## Run sources

- 2026-08-03（#188）fresh re-baseline：`with_skill` 与 `without_skill` 各自在隔离目录（`tmp/eval-runs/issue-188-docs/with_skill/` 与 `tmp/eval-runs/issue-188-docs/without_skill/`）的 pristine fixture 副本中独立执行，互不读取对方输出。
- `without_skill`: fresh baseline；仅读取本例 prompt、assertions、metadata 与 fixture，未读取或应用 docs-audit skill、Docs Agent README 或旧 `comparison.md`。
- `with_skill`: fresh candidate；完整读取 `docs-audit/SKILL.md`、`docs-audit/_internal/INSTRUCTIONS.md` 与 `agents/docs/README.md`，并在同 prompt/pristine fixture 下执行。
- fresh judge 读取冻结的双侧 candidate 与 assertions 判定（`tmp/eval-runs/issue-188-docs/judge/verdict.md`）；本轮没有复用历史 baseline、旧 comparison 内容或历史运行产物。

## Assertion review
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | Without skill | With skill | Evidence and behavior |
| --- | --- | --- | --- |
| `requires_exact_target_tree_blobs` | PASS | PASS | Baseline 能识别未提交 patch 不属于 `release-head`，不能作为通过证据。Skill §1 input gate 与 §4 step 2 进一步限定 passing evidence 必须是精确 target_ref tree 的 ordinary blob；工作区、index、untracked 和 later-branch bytes 仅可诊断。 |
| `blocks_every_in_scope_worktree_delta` | PASS | PASS | 两侧均逐项解析 porcelain：staged `src/catalog/routes.txt` 属事实证据，unstaged `catalog-items.md` 属 affected page，untracked candidate draft 属 authorized write path，modified `package.json` 属 required version inventory；每一项都独立阻塞。Skill 明确不需要调用方先把差异声明为 passing evidence。 |
| `performs_zero_audit_writes` | PASS | PASS | Baseline 在 dirty scope 下直接 blocked。Skill §4 step 2 和失败事务规则要求在建 candidate 前阻塞，不判页为 verified、不盖章、不建 candidate/anchor/discovery/handoff commit、不返回 `ready_for_tag`，并保持宿主 branch/worktree/index 原状。 |
| `requires_clean_commit_update_ref_and_rerun` | PASS | PASS | 两侧均要求维护者提交需保留的最终内容或移出全部 scope 内差异，再把 `target_ref` 更新到最终 commit、确认 scope/index 干净，并从输入解析开始完整重跑；Skill 明确不允许局部续跑或用补证修复本次尝试。 |

## Behavior summary
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

### With skill

在任何事实核对或审计写入前，完整列出四个独立 scope intersection，并将阶段判为 `blocked`。所有未提交内容仅作为诊断上下文；不会创建隔离事务或修改宿主状态。重跑条件覆盖全部差异处置、目标 ref 更新、scope 清洁确认和从头执行完整 pre-tag protocol。

### Without skill baseline

本例 prompt、release context 与 porcelain inventory 已清楚给出未提交证据和四类 scope 交集，因此 baseline 也能正确阻塞、保持零写入并要求完整重跑。Skill 的增益主要是把“任何 scope/authorized path/required inventory 差异都独立阻塞”和“只接受 target-tree ordinary blob”固化为不可绕过的协议。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- With skill: 无 assertion failure。
- Without skill: 无 assertion failure。

## Next steps

- 无需修改 skill；保留本例验证 dirty scope 的 fail-closed 行为和完整重跑要求。

## Runtime artifact policy

- Runtime artifacts（双侧 candidate、judge verdict、隔离目录执行产物）在本次 fresh re-baseline 中真实生成，位于被 gitignore 覆盖的 `tmp/eval-runs/issue-188-docs/`；未提交到 git。长期 durable 产物仅为本 `comparison.md`。
