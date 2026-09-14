# 仓库架构

Dev Agent Skills 是按需使用的专业知识库，包含六个插件、三十七个 Skill。助手直接对用户目标负责，可在同一任务中组合产品、工程、测试、运维、安全和文档能力。

| 插件 | 导航 Skill | 专业内容 |
| --- | --- | --- |
| Product Manager | `pm-agent` | 需求、功能目录、研究、路线图、版本沟通、写作 |
| Engineer | `engineer-agent` | 代码分析、技术设计、实现、测试、调试、交付 |
| QA | `qa-agent` | 探索测试、预期验证、缺陷分析、回归 |
| DevOps | `devops-agent` | 部署、CI/CD、环境配置、故障处置 |
| Security | `security-agent` | 应用安全、授权、依赖、隐私与数据流 |
| Docs | `docs-agent` | 文档站、事实同步、操作手册、发布说明、审计 |

每个 Skill 均可直接使用。角色导航帮助选择专业方法，用户请求、issue、代码、测试和已有文档共同提供任务依据。助手在授权范围内持续完成工作，遇到关键决策缺口或需要额外权限的操作时询问用户。专业文档、实施计划、交接记录和子代理按任务价值选用。

## 内容组织

```text
agents/{role}/skills/{skill}/    Skill 入口、专业参考与工具
agents/{role}/README*.md        插件能力目录
docs/                          使用、维护与发布文档
scripts/                       安装、生成与一致性检查
```

`SKILL.md` 说明能力用途和核心方法，支持资料放在 `_internal/`、`references/`、`scripts/` 或 `assets/`。`human-writing` 可与文档能力一起使用，帮助组织面向读者的内容。

共享参考源位于 `agents/product_manager/skills/idea-to-spec/_internal/_shared/`。四份文件分别提供协作摘要、任务完成记录、安全发现和文档使用建议，五个插件内保留生成副本供安装后按需参考。`scripts/generate_shared_contracts.py` 维护副本一致性。

## 分发与验证

Claude Code 从 marketplace 安装独立插件。Codex 安装器将 Agent 树复制到隐藏镜像，再通过根目录的相对软链暴露 Skill。Kimi Code 通过原生 manifest 注册六个目录，由用户请求选择能力。

版本、注册路径、Skill 名称、lockfile 内容哈希、共享参考副本和本地链接由检查脚本验证。行为变更使用相关测试确认。

[文档说明](./AGENTS.md) · [Codex 安装](./README.codex.md) · [Skill 维护](./cookbook/maintain-skills.md) · [手动发布](./cookbook/release.md)
