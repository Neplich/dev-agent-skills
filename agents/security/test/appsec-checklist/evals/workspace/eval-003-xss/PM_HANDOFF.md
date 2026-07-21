# PM Handoff Packet

pm-agent 已完成入口分类，并将评论展示功能的应用安全审查路由至 appsec-checklist。

```yaml
request_type: security
change_tier: standard
feature_path: comment-display
feature: comment-display
parent_feature: N/A
feature_level: 1
feature_path_evidence:
  - source: docs/pm/comment-display/PRD.md
    reason: 该 PRD 已确认用户评论内容的展示流程和安全边界，是 comment-display 的正式产品依据。
source_documents:
  - docs/pm/comment-display/PRD.md
  - src/ui/comment-display.js
scope_decision:
  summary: 审查用户提交的评论内容进入浏览器 DOM 的路径，识别可执行脚本注入风险并给出分级和修复建议。
  expectation_changed: false
  non_goals:
    - 增加富文本编辑能力
    - 修改评论排序
downstream_owner: Security
required_output: 按 feature_path 输出 docs/security/comment-display/appsec-checklist.md，包含可定位证据、影响、严重度依据和可执行修复建议，不直接修改应用代码。
risk_surface:
  - 评论正文渲染
  - 浏览器 DOM 更新
assets:
  - 用户会话
  - 页面内容完整性
permissions:
  - viewer
  - commenter
data_categories:
  - 用户生成内容
remediation_expectations:
  - 输出编码与渲染修复项交回 engineer-agent
  - 修复后使用脚本载荷执行浏览器回归验证
blockers_risks:
  - 未转义评论内容可能在其他用户浏览器中执行攻击者脚本
```
