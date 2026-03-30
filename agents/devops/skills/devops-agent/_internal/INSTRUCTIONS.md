# DevOps Agent Dispatcher Instructions

## Available Skills

- `deployment-planner` - Plan deployment strategy
- `cicd-bootstrap` - Setup CI/CD pipeline
- `env-config-auditor` - Audit environment configuration
- `incident-playbook-writer` - Create incident playbooks

## Intent Mapping

| User Intent | Skills to Execute |
|-------------|------------------|
| "部署规划" | deployment-planner |
| "配置 CI/CD" | cicd-bootstrap |
| "环境审计" | env-config-auditor |
| "故障手册" | incident-playbook-writer |
| "完整部署流程" | deployment-planner → cicd-bootstrap → env-config-auditor |
