# DevOps Agent

`devops-agent` 是部署、交付自动化、配置治理和运行准备的 dispatcher skill。它负责把部署规划、CI/CD、环境审计和故障手册请求路由到合适的 DevOps specialist skill。

> [!NOTE]
> 其他语言：[English](./README.md)

> [!TIP]
> DevOps Agent 不是每个功能的必经阶段。只有当“怎么部署、怎么自动化、配置是否齐全、上线后怎么回滚”成为当前问题时才需要调用。

## 快速信息

| 项目 | 内容 |
| --- | --- |
| 入口 skill | `devops-agent` |
| Specialist skills | 4 个 |
| 主要输入 | 工程代码、PM/TRD、部署约束、环境变量、CI/CD 现状 |
| 主要输出 | `deploy/` 配置、CI/CD 文件、环境审计、runbook |
| 上下游协作 | 上游 `engineer-agent`，必要时回到 `pm-agent` 或 `security-agent` |

## Skill 清单

| Skill | 适用场景 | 主要产物 |
| --- | --- | --- |
| `devops-agent` | DevOps 请求入口与路由 | 下游 skill 选择与执行路径 |
| `deployment-planner` | 新建或扩展部署配置、容器化、K8s/Helm | `deploy/local/`、`deploy/docker/`、`deploy/helm/` |
| `cicd-bootstrap` | GitHub Actions / GitLab CI / release workflow | CI/CD 配置文件 |
| `env-config-auditor` | 环境变量、secrets、运行时配置覆盖率 | 配置审计报告、缺口清单 |
| `incident-playbook-writer` | 回滚、故障排查、on-call 准备 | runbook、incident playbook |

## 路由规则

- 新建或扩展部署资产：使用 `deployment-planner`
- 自动构建、测试、发布流程：使用 `cicd-bootstrap`
- 环境变量、secrets、配置覆盖率：使用 `env-config-auditor`
- 回滚文档、故障排查手册、值班准备：使用 `incident-playbook-writer`

默认规则：如果核心问题是“让系统可部署”，从 `deployment-planner` 开始；如果已有部署但缺自动化，从 `cicd-bootstrap` 开始。

## 部署产物模型

```text
deploy/
├── local/      # 本地开发调试
├── docker/     # Dockerfile、compose、构建脚本
└── helm/       # Helm chart、values、K8s 运行参数
```

必要时补充：

- `.github/workflows/`
- `.gitlab-ci.yml`
- `docs/devops/{feature-name}/`

## 典型工作流

```mermaid
flowchart LR
    Engineer["engineer-agent output"] --> DevOps["devops-agent"]
    DevOps --> Deploy["deployment-planner"]
    Deploy --> CI["cicd-bootstrap"]
    CI --> Audit["env-config-auditor"]
    Audit --> Runbook["incident-playbook-writer"]
```

## 协作边界

- DevOps 可以生成部署配置、CI/CD、环境审计和运维手册。
- DevOps 不替代 Engineer 修业务代码，也不替代 Security 做安全审查。
- 环境配置发现敏感风险时，应把修复或安全复审交给合适角色继续处理。

## 本地维护

```bash
# 安装某个 DevOps skill 到当前项目运行时
npx skills add ./agents/devops/skills/deployment-planner

# 运行单个 DevOps eval
uv run agents/devops/test/run_eval.py agents/devops/test/deployment-planner/evals/evals.json
```
