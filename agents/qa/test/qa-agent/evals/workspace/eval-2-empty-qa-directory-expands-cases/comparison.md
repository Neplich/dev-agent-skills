# Eval Result: eval-002-empty-qa-directory-expands-cases

## Evaluation Target

- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`
- Prompt target: 对已有但无 TC 的 E2E 功能树做路由与执行协议说明。

## Test Set / Fixture Version

- Eval schema: `evals.json` v1.0
- Fixture version: repository commit `c664869`
- Fresh run: `2026-07-31 08:22:36 +0800`
- Runtime directory: `tmp/eval-runs/issue-196-l2-3-4/qa-agent/eval-002-empty-qa-directory-expands-cases/`
- `eval_metadata.json` 未声明 `execution_cleanup`。

## Latest Result

- Behavior result: **FAIL**
- Coverage result: **FULL**
- 所有 assertion 场景均已触发；无 `NOT EXERCISED` assertion。
- router 单表契约已触发：with-skill 依据含「信号示例」列的 `Default Routes` 单表选择主 route；未要求或伪造独立信号列表。

Overall result: FAIL

## Assertion Results

- PASS `assertion_1`: 正确识别空功能树不是现有覆盖。
- FAIL `assertion_2`: 用户已授权探索，候选要求读取目标源文件、环境说明与现有 QA 索引，没有重复询问或直接 blocked；但没有显式要求下游发现或读取仓库测试命令，未满足该 assertion 的全部要素。
- PASS `specialist_gate_pointer`: 声明 `spec-based-tester` 的 E2E memory、platform version、credential、execution entry、PRD/TRD/implementation plan 与 blocked-condition 权威门禁适用；没有展开协议。
- PASS `assertion_6`: 选择单一 `spec-based-tester` route，未进入实现修复。

## With-Skill Behavior

候选从单张路由表选择 `spec-based-tester`，识别空目录不是覆盖，并在用户已授权的前提下传递目标代码、环境和现有 QA 索引读取任务。输出没有复制平台版本、凭据、执行入口或 blocked-condition 的具体协议，但遗漏了显式的仓库测试命令发现/读取要求。

## Fresh Without-Skill Baseline

本轮 baseline 使用同一 prompt 与 fixture 新生成，未读取或应用 skill、QA README、with-skill 候选或旧 comparison，也未复用历史 baseline。它能识别空目录并提出 TC/脚本补齐步骤，但没有命名一个受约束的 QA specialist，末尾又建议同时做 exploratory testing；它还展开 platform version、账号和执行阻塞细节，缺少 router 指针边界。

## Failures

- `assertion_2`：with-skill 未显式要求下游发现或读取仓库测试命令。

## Next Steps

- 下一轮候选在不展开 specialist 协议的前提下，把“发现并读取仓库现有测试命令”作为传递给 specialist 的上下文要求。

## Runtime Artifact Policy

- 新生成的 with-skill / without-skill candidate 与 verdict 均在上述 `tmp/eval-runs/` 目录。
- Runtime 产物不提交；durable 结果仅为本文件。
