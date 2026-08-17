# 维护 Role Skill

1. 从 `pm-agent` 进入并判定变更等级；新增或重命名 Role Skill / Agent 属于 `major`。
2. 使用仓库 `maintain-skills` Skill 作为生命周期权威流程，修改前读取其同步面 reference。
3. 只更新该流程明确列出的 Skill、路由/发现面、过程文档、lock entry 和共享契约副本。
4. 运行共享契约生成、repository/doc contract、受影响确定性测试和安装验证。
5. 审查精确 diff，按范围提交并推送 PR；未经维护者确认不得合并。

仓库架构见 [architecture.md](../architecture.md)。
