# Security Agent Dispatcher Instructions

## Available Skills

- `appsec-checklist` - Application security checklist
- `authz-reviewer` - Authorization review
- `dependency-risk-auditor` - Dependency audit
- `privacy-surface-mapper` - Privacy mapping

## Intent Mapping

| User Intent | Skills to Execute |
|-------------|------------------|
| "应用安全检查" | appsec-checklist |
| "认证授权审查" | authz-reviewer |
| "依赖审计" | dependency-risk-auditor |
| "隐私合规" | privacy-surface-mapper |
| "完整安全审查" | appsec-checklist → authz-reviewer → dependency-risk-auditor → privacy-surface-mapper |
