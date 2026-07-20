# v1.4.0 文档发布链入口

- request_type: `validation`
- change_tier: `major`
- feature_path: `ai-search`
- host_repository: `JOTO-AI/aiportal`（AI Hub-shaped fixture）
- requested_flow: `docs-audit pre-tag -> docs-audit post-tag -> github-release-generator handoff`
- target_release_version: `v1.4.0`
- target_release_version_confirmation:
  - status: `maintainer_confirmed`
  - source: `maintainer-approval/release-v1.4.0@2026-07-20T09:00:00+08:00`
- audit_phase_sequence: `pre-tag`, then consume `.eval/simulated-tag.md` for `post-tag`
- git_fixture_setup: `sh .eval/setup-git-fixture.sh`
- git_fixture_evidence: `.eval/runtime-git-evidence.md`
- base_ref: `refs/heads/fixture-base`
- target_ref: `refs/heads/fixture-target`
- release_evidence_branch_ref: `refs/heads/release-evidence/v1.4.0`
- release_evidence_expected_head: 从 `.eval/runtime-git-evidence.md` 读取 setup 在写入前捕获的 caller-confirmed head，并验证结果 commit 父节点、最终分支 head 与 blob readback
- diff_semantics: `two-dot endpoint diff`
- previous_tag: `v1.3.0`
- intended_target_tag: `v1.4.0`
- release_scope: completed AI search API delivery and its formal documentation/release surfaces
- site_release_notes_handoff: `release-notes-handoff.md`
- pre_tag_output: fixed discovery handoff for `ready_for_tag`
- post_tag_output: independent persisted result for `release_verified`
- github_release_action: handoff only; no preview, draft, publish, or remote mutation in this eval

`git_fixture_setup` 只能在 runner 复制出的隔离 workspace 执行。它创建的 tag 和 refs 均为本地 synthetic Git 对象，用于审计 object/tree/CAS 语义；不得在本仓库工作树或任何远端执行。

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
