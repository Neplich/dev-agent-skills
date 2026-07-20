# Issue #116 site Release Notes handoff

```yaml
handoff_target: "issue #117 / docs-audit pre-tag"
downstream_target: "issue #120 / github-release-generator"
handoff_status: ready
next_gate: "issue #117 pre-tag audit"
release_execution_authorized: false
target_release_version: "v1.4.0"
target_release_version_confirmation:
  status: maintainer_confirmed
  source: "maintainer-approval/release-v1.4.0@2026-07-20T09:00:00+08:00"
site_release_note_path: "docs/site/release-notes/v1.4.0.md"
confirmation_status: confirmed
confirmation_source: "maintainer-approval/site-release-notes-v1.4.0@2026-07-20T09:10:00+08:00"
docs_checks:
  - command: "npm run test:docs"
    cwd: "docs/site"
    result: passed
updated_release_surfaces:
  release_metadata:
    - "docs/site/.meta/releases.json"
  indexes:
    - "docs/site/release-notes/index.md"
  navigation: []
source_evidence:
  - source: "docs/pm/ai-search/PRD.md"
    supports: "已批准的用户搜索范围"
  - source: "docs/engineer/ai-search/TRD.md"
    supports: "GET /api/search 接口契约"
  - source: "docs/engineer/ai-search/IMPLEMENTATION_PLAN.md"
    supports: "已完成的实现与验证范围"
  - source: "src/search/routes.ts"
    supports: "当前路由、参数与响应事实"
  - source: "tests/search-api.test.ts"
    supports: "成功和非法请求测试"
  - source: "evidence/docs-checks.md"
    supports: "宿主 docs checks 通过"
required_version_sources:
  - source_id: actual_tag
    locator_kind: git-ref
    locator: refs/tags/v1.4.0
    selector: tag-name
    extractor: git-tag-name-v1
    required_raw_form: vX.Y.Z
  - source_id: target_version
    locator_kind: handoff
    locator: release-notes-handoff.md
    selector: target_release_version
    extractor: handoff-field-v1
    required_raw_form: vX.Y.Z
  - source_id: release_notes
    locator_kind: git-file
    locator: docs/site/release-notes/v1.4.0.md
    selector: heading[h1].release-version
    extractor: markdown-release-heading-v1
    required_raw_form: vX.Y.Z
  - source_id: release_index
    locator_kind: git-file
    locator: docs/site/release-notes/index.md
    selector: entry[v1.4.0].version
    extractor: markdown-release-index-v1
    required_raw_form: vX.Y.Z
  - source_id: release_metadata
    locator_kind: git-file
    locator: docs/site/.meta/releases.json
    selector: /latest
    extractor: json-pointer-rfc6901-v1
    required_raw_form: vX.Y.Z
  - source_id: host_package
    locator_kind: git-file
    locator: package.json
    selector: /version
    extractor: json-pointer-rfc6901-v1
    required_raw_form: X.Y.Z
blockers: []
```

站内页面、metadata、index、正文确认和 docs checks 由 `docs-agent:release-notes-generator` 所有。该 handoff 不是 GitHub Release 执行授权；`github-release-generator` 只能在同版本 `ready_for_tag` 后准备预览，并在实际 tag、`release_verified` 和维护者独立发布批准全部存在后发布。
