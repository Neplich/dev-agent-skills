# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-009-pre-tag-blocked`

## Test Set / Fixture Version

- Fixture version: A7 / 2026-07-19
- Assertions: 3
- Fresh pair: current A7 prompt against two pristine copies of the same fixture.

## Latest Result

**PASS — fresh with-skill 3 / 3 assertions passed.** 候选明确区分 `target_ref` 可达提交内容与未提交工作区 patch；后者只能作诊断，不能把页面判为 verified。结果直接 `blocked`，要求先提交、更新 `target_ref` 并完整重跑 pre-tag。

Fresh without-skill baseline 同样为 **3 / 3**。本例没有断言级 skill 增益，因为 prompt、expected output 与 release context 已直接陈述未提交证据边界和完整重跑要求。

## Assertion Results

| Assertion | With skill | Without skill | Evidence summary |
| --- | --- | --- | --- |
| `requires_target_ref_reachable_evidence` | PASS | PASS | 两者均区分 target commit 与工作区修改，并只把未提交 patch 当诊断。 |
| `blocks_uncommitted_workspace_evidence` | PASS | PASS | 两者均拒绝 verified、盖章、`ready_for_tag` 与可信 handoff，结果 `blocked`。 |
| `requires_commit_update_ref_and_rerun` | PASS | PASS | 两者均要求提交实现、更新 `target_ref` 到包含证据的 commit，并完整重跑 pre-tag。 |

## With-Skill Behavior

- 来源：本会话 A7 fresh with-skill candidate；读取当前 skill/内部协议、Docs README、eval 定义和 pristine fixture。
- 结果：3 / 3。严格执行“通过证据必须 target_ref 可达”的 pre-tag 边界。

## Without-Skill Baseline

- 来源：本会话 A7 全新 baseline；相同 prompt、独立 pristine fixture，不读取或应用 skill、Docs README、历史 comparison 或 baseline。
- 结果：3 / 3。直接依据 fixture 明示边界得出相同结论。
- 对比结论：本例区分度为零；它验证阻塞回归，而不测独立推导能力。

## Failures and Limitations

- 两个候选均无 assertion failure。
- 这是合成 ref 的只读协议验证，没有真实宿主 commit 可达性检查。
- eval-001～007 不在 A7 两阶段收敛协议变更及本轮指定验证范围内，其 prompt、assertions 与 fixture 未被本任务修改，因此未重跑也未更新其 comparison。

## Next Steps

- 若要提高区分度，可让 fixture 只提供 raw target tree 与 worktree diff，减少对结论和下一步的直接陈述。

## Runtime Artifact Policy

- fresh candidates 与 judge 诊断仅位于 gitignored `tmp/eval-runs/docs-audit-a7.*`，未写入 fixture、未加入 git、不得提交。
- Durable 结果仅为本 `comparison.md`；未复用历史 baseline。
