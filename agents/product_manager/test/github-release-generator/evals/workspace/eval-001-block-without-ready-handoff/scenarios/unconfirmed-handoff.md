# 场景 B：页面存在但未确认

- request: 为 AI Hub v1.0.0 生成 GitHub Release draft
- release_version: `v1.0.0`
- intended_tag: `v1.0.0`
- previous_tag: `v0.9.0`
- target_ref: `8b6a1f2`
- site_release_note_path: `docs/site/release-notes/v1.0.0.md`
- confirmation_status: `unconfirmed`
- docs_checks:
  - command: `npm run test:docs`
    cwd: `docs/site`
    status: passed
- updated_release_surfaces:
  - `docs/site/release-notes/index.md`
  - `docs/site/.meta/releases.json`
- source_evidence: `evidence/*.md`
- issue_116_handoff_status: blocked
- blocker: 维护者尚未确认完整页面正文
