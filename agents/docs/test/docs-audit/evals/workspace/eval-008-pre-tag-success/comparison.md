# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`

## Test Set / Fixture Version

- Fixture version: A7 / 2026-07-19
- Assertions: 10
- Fresh pair: current A7 prompt against two pristine copies of the same fixture.

## Latest Result

**PASS — fresh with-skill 10 / 10 assertions passed.** 候选完整执行 pre-tag 两道收敛门：先在成功记录出现前校验 staged inventory 与逐文件内容差异，再把四页统一盖章和成功记录放入同一普通 commit，随后执行 commit 后确认；只有两关都通过才建立外部可信 handoff 并返回不表示已发布的 `ready_for_tag`。

Fresh without-skill baseline 为 **4 / 10**。它能识别版本、混合版本规范化、同 commit 边界和阶段结果，但未形成可审计的完整 release-surface 核验、章前字段约束、回读、精确哈希和可信 handoff 证据链，也未精确定义两道收敛门。

## Assertion Results

| Assertion | With skill | Without skill | Evidence summary |
| --- | --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | PASS | 两者均分别记录 refs 与维护者确认版本，并接受 tag 尚不存在的 pre-tag。 |
| `verifies_complete_set_and_surfaces` | PASS | FAIL | with-skill 核对两张 API 页、#116、Release Notes/索引、releases.json 与 package；baseline 未明确核对 #116 及 Release Markdown 事实。 |
| `normalizes_mixed_version_forms` | PASS | PASS | 两者均按带 `v`/不带 `v` 来源规范化为 SemVer `1.2.0`。 |
| `records_pre_stamp_values` | PASS | FAIL | baseline 列出四个旧值，但未约束不得新增 `baseline_verified_version`。 |
| `stamps_complete_set_atomically` | PASS | FAIL | baseline 提到四页盖章和只读 releases.json，但未要求完整回读证明。 |
| `commits_stamp_and_record_together` | PASS | PASS | 两者均要求四页盖章与成功记录由同一普通 commit 引入。 |
| `persists_stamp_and_content_evidence` | PASS | FAIL | baseline 缺逐页章前/章后值、精确字节 SHA-256、其他版本面哈希及 commit/tree/path/blob handoff tuple。 |
| `validates_staged_convergence_before_success_record` | PASS | FAIL | with-skill 明确成功字段前的完整 staged inventory 与逐内容 hunk 白名单；baseline 仅泛化检查意外路径。 |
| `confirms_commit_before_handoff` | PASS | FAIL | baseline 未说明 post-commit 完整内容授权复核、结果不得回写锚定 blob，以及两关通过后才 handoff。 |
| `returns_ready_for_tag_not_published` | PASS | PASS | 两者均返回 `ready_for_tag` 并明确不等于发布或 post-tag 验证。 |

## With-Skill Behavior

- 来源：本会话 A7 fresh with-skill candidate；读取当前 `docs-audit` SKILL、内部指令、Docs README、eval 定义和 pristine fixture。
- 结果：10 / 10。完整覆盖统一盖章集、来源规范化、章前基线、精确字节哈希、成功记录、同 commit 边界、pre-commit staged convergence、post-commit confirmation 与外部可信 handoff。

## Without-Skill Baseline

- 来源：本会话 A7 全新 baseline；使用相同 prompt 与独立 pristine fixture，仅基于 fixture 作答，不读取或应用 skill、Docs README、历史 comparison 或历史 baseline。
- 结果：4 / 10。能从 prompt 直接复现高层顺序，但没有把协议细化成满足证据链断言的可复核输出。
- 对比结论：本例显示 6 条断言的可量化 skill 增益，主要集中在成功记录写入时序、精确内容证据与可信锚定。

## Failures and Limitations

- With-skill 无 assertion failure；baseline 失败 6 条，均为证据完整性或执行时序缺口。
- fixture 使用合成 refs/commit/tree，仅验证协议语义；未在 fixture 中实际创建 Git commit 或 tag。
- eval-001～007 不在 A7 两阶段收敛协议变更及本轮指定验证范围内，其 prompt、assertions 与 fixture 未被本任务修改，因此未重跑也未更新其 comparison。

## Next Steps

- 保持当前 staged-before-success 与 post-commit-confirmation 两关断言；若后续引入真实 Git harness，再补实际 commit/tree/blob 执行验证。

## Runtime Artifact Policy

- 本轮 fresh with/without candidate 与 judge 诊断仅位于 gitignored `tmp/eval-runs/docs-audit-a7.*` 隔离目录，未写入 fixture、未加入 git、不得提交。
- Durable 结果仅为本 `comparison.md`；未复用历史 baseline。
