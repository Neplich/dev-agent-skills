# Immutable ref and diff evidence

- base_ref: `1111111111111111111111111111111111111111`
- target_ref: `2222222222222222222222222222222222222222`
- target_tree: `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`
- target_ref_source: committed release candidate branch
- in_scope_worktree_changes: none
- staged_changes: none
- untracked_in_scope_paths: none
- changed_files:
  - `A src/search/routes.ts`
  - `A tests/search-api.test.ts`
  - `A docs/site/api/ai-search.md`
  - `M docs/site/standards/change-map.yaml`
  - `A docs/site/release-notes/v1.4.0.md`
  - `M docs/site/release-notes/index.md`
  - `M docs/site/.meta/releases.json`
  - `M package.json`
- change_map_match: `src/search/** -> docs/site/api/ai-search.md`
- complete_affected_formal_pages:
  - `docs/site/api/ai-search.md`
  - `docs/site/release-notes/v1.4.0.md`
  - `docs/site/release-notes/index.md`
- template_pages: validate frontmatter and scaffold structure only; placeholder bodies are exempt from type-specific fact checks
- candidate_record_path: `docs/site/.meta/audit/audit-v1.4.0.md`
- discovery_handoff_path: `docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md`
- evidence_ref: `refs/heads/release-evidence/v1.4.0`
- expected_anchor_tree_after_unified_stamp: `bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb`
- expected_handoff_tree: `cccccccccccccccccccccccccccccccccccccccc`

本文件模拟从不可变 Git object 读取的 ref/diff 输入。候选记录、统一盖章、固定 discovery handoff、staged/committed 收敛和集成回读仍必须由执行者按 docs-audit 协议裁定，不得把这些 expected 值直接当作成功结论。
