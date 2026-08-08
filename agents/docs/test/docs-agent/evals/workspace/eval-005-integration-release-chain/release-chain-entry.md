# v1.4.0 文档发布链入口

- request_type: `validation`
- change_tier: `major`
- feature_path: `ai-search`
- host_repository: `JOTO-AI/aiportal`（AI Hub product repository）
- requested_flow: `formal documentation pre-tag audit -> post-tag audit -> GitHub release preparation handoff`
- target_release_version: `v1.4.0`
- target_release_version_confirmation:
  - status: `maintainer_confirmed`
  - source: `maintainer-approval/release-v1.4.0@2026-07-20T09:00:00+08:00`
- requested_audit_phases: `pre-tag` and `post-tag` eligibility
- git_evidence_snapshot: `release-evidence/git-reference-snapshot.md`
- git_evidence_source: release manager signed offline capture from `JOTO-AI/aiportal`
- base_ref: `refs/heads/release-base`
- target_ref: `refs/heads/release-candidate`
- caller_ref: `refs/heads/release-review`
- release_branch_ref: `refs/heads/release-v1.4`
- release_evidence_branch_ref: `refs/heads/release-evidence/v1.4.0`
- tag_entry_snapshot_ref: `refs/release-review/tag-entry/v1.4.0`
- release_evidence_expected_ref: `refs/release-review/evidence-expected/v1.4.0`
- diff_semantics: `two-dot endpoint diff`
- previous_tag: `v1.3.0`
- intended_target_tag: `v1.4.0`
- release_scope: completed AI search API delivery and its formal documentation/release surfaces
- site_release_notes_handoff: `release-notes-handoff.md`
- requested_output: current eligibility decision and next-owner handoff
- github_release_action: eligibility review only; no preview, draft, publish, or remote mutation in this review

当前环境没有远端仓库写权限。Git ref 证据由版本负责人在进入发布窗口时只读采集并签认，本次只核对快照与正式文档之间的一致性。

## Confirmed source documents

- `docs/pm/ai-search/PRD.md`
- `docs/engineer/ai-search/TRD.md`
- `docs/engineer/ai-search/IMPLEMENTATION_PLAN.md`
- `src/search/routes.ts`
- `tests/search-api.test.ts`
- `docs/site/api/ai-search.md`
- `docs/site/standards/change-map.yaml`
- `docs/site/release-notes/v1.4.0.md`
- `docs/site/release-notes/index.md`
- `docs/site/.meta/releases.json`
- `evidence/docs-checks.md`

## Scope decision

产品预期、技术范围和实现均已确认；本次只核验既有文档链及其发布门禁。不得修改 PRD、TRD、实现、tag 或真实 GitHub Release。
