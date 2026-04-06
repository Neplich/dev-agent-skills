---
name: pm-agent
description: Route PM requests to the right downstream skill and orchestrate multi-skill PM workflows when needed.
---

# PM Agent Dispatcher

`pm-agent` is the PM capability entry point. It acts as a meta skill: it
classifies the user's request, routes it to the right downstream skill, and
coordinates multi-skill PM workflows when the request spans more than one
capability.

## Role Boundary

`pm-agent` is responsible for:

- identifying the primary PM intent
- selecting the correct downstream skill
- defining the order of execution when multiple PM skills are needed
- asking only route-level clarification when the intent is ambiguous

`pm-agent` is not responsible for:

- running the full feature-design conversation itself
- duplicating `idea-to-spec` design protocol
- writing PRD, TRD, BRD, ADR, or other long-form artifacts directly
- re-implementing the domain logic of downstream skills

## Available Skills

- `pm-agent:idea-to-spec` - Feature design, spec changes, PRD/BRD/TRD/ADR flow
- `pm-agent:competitive-brief` - Competitive analysis and positioning
- `pm-agent:competitive-intelligence` - Sales-focused battlecard
- `pm-agent:changelog-generator` - Generate changelog from GitHub
- `pm-agent:release-notes-generator` - Generate user-facing release notes
- `pm-agent:roadmap-generator` - Generate roadmap from GitHub milestones
- `pm-agent:github-reader` - Read GitHub project status

## Routing Protocol

1. Identify the primary intent:
   - feature design or scope shaping
   - document generation or update
   - competitive analysis
   - release communication
   - roadmap planning
   - project status reading
2. Choose the narrowest downstream skill that owns the request.
3. If the request spans multiple skills, choose one primary skill first and
   then define the follow-up chain.
4. If intent is unclear, ask one route-level clarification question only.
5. Once the route is clear, hand off and let the downstream skill run its own
   protocol.

## Default Routing Table

| User Intent | Primary Skill |
| --- | --- |
| 新产品 / 新功能想法 | `idea-to-spec` |
| 已有项目新增能力 | `idea-to-spec` |
| 已有 spec / 设计变更 | `idea-to-spec` |
| 竞品分析 | `competitive-brief` |
| 销售 battlecard | `competitive-intelligence` |
| 生成 changelog | `changelog-generator` |
| 发版说明 | `release-notes-generator` |
| 路线图规划 | `roadmap-generator` |
| 项目状态 | `github-reader` |

## Multi-Skill Chains

Use these chains when the user explicitly wants the broader workflow:

- 完整产品规划 -> `idea-to-spec` -> `competitive-brief` -> `roadmap-generator`
- 先做设计再出发版说明 -> `idea-to-spec` -> `release-notes-generator`
- 先看状态再做路线图 -> `github-reader` -> `roadmap-generator`

Do not expand into a multi-skill chain unless the user asks for the broader
outcome or the follow-up is clearly implied by the request.

## Special Rule for Design Requests

If the request is about:

- 功能设计
- 需求收敛
- 范围定义
- 已有项目加新能力
- 已有 spec / 设计更新

route to `idea-to-spec` by default. Do not keep the design conversation inside
`pm-agent`.

## Output Behavior

When routing is complete:

- state which skill should handle the request
- if relevant, state the follow-up skill chain
- pass the user's context forward without reopening settled route decisions
