# Dev Agent Skills

按需使用的专业知识库：七个插件、四十个 Skill，覆盖产品、设计、工程、测试、运维、安全和文档。助手根据用户目标选择专业方法，持续完成任务。

[English](./README.md) · [中文](./README_zh.md)

## 安装

### Claude Code

按需安装一个或多个插件：

```text
/plugin marketplace add Neplich/dev-agent-skills
/plugin install pm-agent@dev-agent-skills
/plugin install engineer-agent@dev-agent-skills
/plugin install qa-agent@dev-agent-skills
/plugin install devops-agent@dev-agent-skills
/plugin install designer-agent@dev-agent-skills
/plugin install security-agent@dev-agent-skills
/plugin install docs-agent@dev-agent-skills
```

### Codex

```text
Fetch and follow instructions from https://raw.githubusercontent.com/Neplich/dev-agent-skills/refs/heads/main/.codex/INSTALL.md
```

[Codex 安装指南](./docs/README.codex.md)

### Kimi Code

```text
/plugins install https://github.com/Neplich/dev-agent-skills/tree/main
```

README 描述当前源码的能力。固定版本安装使用对应发布 tag，该版本行为见版本记录。

## 使用

每个 Skill 都可直接使用，也可通过角色导航选择方法。用户请求、issue、代码、测试与已有文档提供工作依据；计划和正式文档按任务需要选用。已有授权随任务延续，关键决策缺口或额外权限需求由助手向用户确认。

```text
/debugger "定位并修复登录失败，验证正常与失败路径。"
/feature-implementor "为任务列表增加按状态筛选。"
/human-writing "根据当前代码更新安装说明。"
```

## 插件

| 插件 | Skills |
| --- | ---: |
| [`pm-agent`](./agents/product_manager/README_zh.md) | 9 |
| [`engineer-agent`](./agents/engineer/README_zh.md) | 7 |
| [`qa-agent`](./agents/qa/README_zh.md) | 5 |
| [`devops-agent`](./agents/devops/README_zh.md) | 5 |
| [`designer-agent`](./agents/designer/README_zh.md) | 3 |
| [`security-agent`](./agents/security/README_zh.md) | 5 |
| [`docs-agent`](./agents/docs/README_zh.md) | 6 |

## 文档

- [Architecture](./docs/architecture.md)
- [Documentation guide](./docs/AGENTS.md)
- [Skill maintenance](./docs/cookbook/maintain-skills.md)
- [Manual release](./docs/cookbook/release.md)
- [Contributing](./CONTRIBUTING.md)
- [Changelog](./CHANGELOG.md)

[Apache License 2.0](./LICENSE)
