# Eval Result: eval-002-empty-qa-directory-expands-cases

## Evaluation Target

- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`
- Prompt target: 对已有但无 TC 的 E2E 功能树做路由与执行协议说明。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `cdfc879` plus current working-tree assertion alignment
- Fresh run: `2026-07-30 19:56:24 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-pr-b-qa-agent-20260730-195624/eval-002-empty-qa-directory-expands-cases/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **FULL**
- 所有 assertion 场景均已触发；无 `NOT EXERCISED` assertion。
- 变更点检查：with-skill 输出识别空功能树并传递探索上下文，同时只声明 specialist 权威门禁指针，未展开协议。

Overall result: PASS

## Assertion Results

- PASS `assertion_1`: 正确识别空功能树不是现有覆盖。
- PASS `assertion_2`: 用户已授权探索，要求读取目标源文件、环境说明与仓库现有测试配置/命令，没有重复询问或直接 blocked。
- PASS `specialist_gate_pointer`: 声明 `exploratory-tester` 的 E2E memory、platform version、credential、execution entry、PRD/TRD/implementation plan 与 blocked-condition 权威门禁适用；没有展开协议。
- PASS `assertion_6`: 选择单一 `exploratory-tester` route，未进入实现修复。

## With-Skill Behavior

候选选择单一 `exploratory-tester` route，识别空目录不是覆盖，并在用户已授权的前提下传递目标代码、环境和测试命令发现任务。输出没有复制平台版本、凭据、执行入口或 blocked-condition 的具体协议。

## Fresh Without-Skill Baseline

本轮 baseline 使用同一 prompt 与 fixture 新生成，未读取或应用 skill、QA README，也未复用历史 baseline。它能识别空目录并选择单一路由，但直接展开 platform version、credential、execution entry、subagent 与报告协议，违反当前指针断言。

## Failures

- 无 with-skill assertion 失败。

## Next Steps

- 保持 router 只传递探索上下文和权威门禁指针；由 specialist 执行实际用例扩充与验证协议。

## Runtime Artifact Policy

- 新生成的 with-skill / without-skill candidate 与 verdict 均在上述 `tmp/eval-runs/` 目录。
- Runtime 产物不提交；durable 结果仅为本文件。
