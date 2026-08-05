# Eval Result: eval-005-mapped-cache-debug-evidence

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-005-mapped-cache-debug-evidence`
- Workspace: `workspace/eval-005-mapped-cache-debug-evidence`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture：`ws1-consumption-v1`
- 日期：2026-07-30
- Fresh run：`tmp/eval-runs/issue-196-l2-2-debugger-20260730-220643/`
- paired candidates 均为本轮隔离新生成。

## Assertion Results

- PASS `reads_mapped_docs_first`：根据 `src/cache/**` 的 change-map 精准读取 `docs/site/api/cache.md`，未遍历无关文档。
- PASS `verifies_against_code`：以 `src/cache/ttl.txt` 核证实现为 fixed 60 秒，并结构化对照文档 300 秒。
- PASS `treats_unverified_as_low_trust`：明确 `last_verified_version: unverified` 为最低信任，不能单独建立批准预期。

## With-Skill Behavior

候选使用映射文档定位、代码事实定性，确认 60/300 秒分歧，同时把“应修代码还是文档”停在 `missing_docs` 的预期对齐边界。

## Without-Skill Baseline

来源为本轮隔离子代理使用相同 prompt 与 fixture 生成，未接触 skill、Engineer README 或 with-skill。baseline 同样精准读取映射文档、以代码核证 TTL，并明确 unverified 最低信任，满足 3/3 assertions。

## Failures

- With-skill：无。
- Baseline：无；本轮没有 assertion 级行为差异。

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
Overall result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Next Steps

保留映射消费与低信任文档覆盖；如需测量 skill 增益，可加入无关文档干扰或移除 prompt 中的明确诊断导向。

## Runtime Artifact Policy

候选、verdict 和诊断只存放于 ignored runtime 目录，不提交；本文件是 durable 结果。
