# Immutable ref and diff evidence contract

- setup_command: `sh .eval/setup-git-fixture.sh`
- runtime_evidence: `.eval/runtime-git-evidence.md`
- base_ref: `refs/heads/fixture-base`
- target_ref: `refs/heads/fixture-target`
- pre_tag_anchor_ref: `refs/heads/fixture-pre-tag-anchor`
- pre_tag_handoff_ref: `refs/heads/fixture-pre-tag-handoff`
- actual_tag_ref: `refs/tags/v1.4.0`
- release_evidence_branch_ref: `refs/heads/release-evidence/v1.4.0`
- release_evidence_expected_head: read the caller-confirmed pre-integration commit from `.eval/runtime-git-evidence.md`; independently prove it is the parent of the post-tag result and that the exact branch now equals the recorded final head
- target_ref_source: runtime-local committed release candidate branch
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
运行前必须在隔离的 eval workspace 执行 setup command。脚本只在该 runtime copy 内初始化本地 Git 仓库，并生成可由 `git rev-parse`、`git cat-file`、`git diff`、`git show` 和 `git ls-tree` 复核的 base、target、统一盖章、discovery handoff、lightweight tag 与 evidence branch。`.eval/runtime-git-evidence.md` 记录本轮实际 object ids；不得把 ref 名或脚本声明直接当作成功结论。

候选记录、统一盖章、固定 discovery handoff、staged/committed 收敛、tag-tree 绑定和 evidence branch expected-head CAS 仍必须由执行者按 docs-audit 协议从真实对象复核。该本地 synthetic tag 仅属于隔离 fixture，不得对宿主或远端仓库执行任何 tag/Release 写入。
