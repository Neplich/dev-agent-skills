# DevOps Skill Evals

DevOps eval 基线目录。

`env-config-auditor` eval 用于验证：

- skill 是否把环境审计结果写到 durable artifact，而不是 `tmp/`
- 报告是否能同时检查 `deploy/` 和 CI/CD 配置
- 断言是否与当前 DevOps canonical model 一致

运行方式：

```bash
uv run agents/devops/test/run_eval.py \
  agents/devops/test/env-config-auditor/workspace/iteration-1/eval-1-missing-variables/eval_metadata.json
```

自动报告会作为运行期临时产物生成到 `tmp/eval-runs/devops/`；长期提交的最新结果只保留 `comparison.md`。

没有 deterministic 产物或机器可检查断言的 metadata 不属于当前 helper 的
runner 流程。直接运行这类 metadata 时 helper 会写入 skip report；语义验证
仍通过 fresh subagent validation 执行，并把 durable 结论写回 `comparison.md`。
`subagent-verdict.md` 只是运行期诊断产物，不作为 metadata output 或提交产物。

实际执行 skill eval 或 fresh Codex subagent validation 后，必须在同一轮变更中更新对应 workspace 的 durable `comparison.md`。PR 评论或对话中的 eval 结论必须与已提交或拟提交的 `comparison.md` 一致；如果没有可更新文件，记录 blocked 或不适用原因。

fresh Codex subagent validation 应基于同一份 eval prompt 和 fixture 同时运行 `with_skill` 与 `without_skill`。`without_skill` 运行结果是写入 `comparison.md` 的 baseline 输入；如果 baseline 无法生成或无法评审，在 comparison 结论中说明影响，不把 baseline 文案当作独立机器判定结果。
