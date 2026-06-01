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

实际执行 skill eval 或 fresh Codex subagent validation 后，必须在同一轮变更中更新对应 workspace 的 durable `comparison.md`。PR 评论或对话中的 eval 结论必须与已提交或拟提交的 `comparison.md` 一致；如果没有可更新文件，记录 blocked 或不适用原因。
