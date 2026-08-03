# Release Package

- site_release_notes_handoff_status: ready
- release_version: `v1.0.0`
- site_release_note_path: `docs/site/release-notes/v1.0.0.md`
- confirmation_status: `confirmed`
- docs_checks: `npm run test:docs` from `docs/site`, exit 0
- updated_release_surfaces: index, releases metadata and generated navigation updated
- source_evidence: confirmed six-category evidence
- docs_audit_pre_tag_handoff:
  - phase: `pre-tag`
  - phase_result: `ready_for_tag`
- base_ref: `v0.9.0`
- target_ref: `8b6a1f2`
- intended_tag: `v1.0.0`
- requested_mode: preview only
- host: dev-agent-skills marketplace（Claude Code + Codex + Kimi Code 三宿主）
- target_content: 目标 tag 含 `.codex/INSTALL.md` 的 TARGET_TAG 安装支持与 `.kimi-plugin/plugin.json`（见工作区对应文件）
