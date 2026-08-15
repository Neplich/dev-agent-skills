# 运行 Skill Eval

1. 使用仓库 `skill-eval-runner` Skill，并读取其 runbook。
2. 只选择真正受影响的目标；修改 eval 定义或 fixture 前先读取 authoring contract。
3. 模型执行前先运行确定性 eval contract 检查。
4. 使用仓库固定模型设置启动一个 fresh paired 进程，worker 不超过 10 个。
5. 检查场景结果，区分 eval 缺陷、Skill 缺陷和基础设施阻塞；只更新有证据支持的持久化
   `comparison.md`。
6. 交付前删除 transcript、diagnostic、timing、run status、自动 comparison 和
   `tmp/eval-runs/`。
7. 重新运行 eval contract 与运行产物检查。

本 cookbook 不复制 eval schema 或判定规则；权威仍是对应 Skill 与仓库脚本。
