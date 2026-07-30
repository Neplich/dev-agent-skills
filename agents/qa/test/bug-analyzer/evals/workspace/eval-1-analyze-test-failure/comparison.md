# Eval Result: eval-001-analyze-test-failure

## Evaluation Target

- Skill: `bug-analyzer`
- Eval: `eval-001-analyze-test-failure`
- Prompt target: 从登录 500 测试失败形成证据化 Bug 报告。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `778b042`
- Fresh run: `2026-07-30 19:26:38 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-20260730-192638/qa/agents/qa/test/bug-analyzer/evals/workspace/eval-1-analyze-test-failure/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL**
- 所有 assertion 场景均已判定；无外部实时样本缺口。
- 非 E2E 路径变更检查：`assertion_4` 已触发 durable output 选择，但候选只给出报告正文，没有声明 `docs/qa/{feature_path}/bug-<short-slug>.md`；因此本轮未证明新路径行为。

Overall result: FAIL

## Assertion Results

- FAIL `assertion_1`: 已读取 failing scenario、500、console 与 build context，并注明 trace 不可用；但未明确记录截图、服务端 stack、完整 network output 等证据的存在/缺失，摄取清单不完整。
- PASS `assertion_2`: 使用 `confirmed but environment-sensitive`，并将 evidence status 与 confidence 分开。
- PASS `assertion_3`: severity 有影响理由，confidence 独立陈述。
- FAIL `assertion_4`: 正确避免 GitHub-first，但没有给出可审计的本地 durable 文件路径，未覆盖 PR-B 新的非 E2E 路径。
- FAIL `assertion_5`: 当前 feature_path 与 plan 对齐材料不足时，应明确把 reusable E2E TC 沉淀标为 blocked；候选既未创建/引用 TC+script，也未记录该 blocker。
- PASS `assertion_6`: 包含 release impact 与 evidence references。

## With-Skill Behavior

候选对分类、严重度、置信度和发布影响处理正确，但证据缺口、durable 路径和 reusable E2E coverage blocker 不完整，故 Behavior FAIL。

## Fresh Without-Skill Baseline

同一 prompt/fixture 的全新 baseline 已在隔离目录生成，未读取 skill、QA README 或历史 baseline。candidate/verdict 均成功；baseline 过度判断为 `confirmed and reproducible`，且同样未处理 reusable TC，semantic verdict 为 FAIL。

## Failures

- 未给出 `docs/qa/{feature_path}/bug-<short-slug>.md`。
- 未完整记录证据缺口与 reusable E2E coverage blocker。

## Next Steps

- 后续 fixture 应提供明确 `feature_path` 并把非 E2E 路径设为显式 assertion，以直接覆盖 PR-B 路径变更。

## Runtime Artifact Policy

- 两条 candidate、两条 verdict、diagnostics 与 `comparison.auto.md` 均在上述 `tmp/eval-runs/`，返回码均为 0、无 timeout。
- Runtime 不提交；durable 结果仅为本文件。
