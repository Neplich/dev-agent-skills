# Runtime-local post-tag evidence contract

- setup_command: `sh .eval/setup-git-fixture.sh`
- runtime_evidence: `.eval/runtime-git-evidence.md`
- evidence_kind: read-only synthetic Git objects in the isolated eval workspace
- actual_tag: `v1.4.0`
- actual_tag_kind: `lightweight`
- actual_tag_ref: `refs/tags/v1.4.0`
- trusted_pre_tag_handoff_path: `docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md`
- candidate_record_path: `docs/site/.meta/audit/audit-v1.4.0.md`
- release_evidence_branch_ref: `refs/heads/release-evidence/v1.4.0`
- release_evidence_expected_head: read the captured pre-integration value from `.eval/runtime-git-evidence.md`; verify post-tag result parent, branch final head and blob readback against it
- target_release_version: `v1.4.0`
- tag_mutation_allowed: false
- github_release_mutation_allowed: false

post-tag 必须消费同版本锚定证据，通过 Git object reads 独立解析 tag object/peeled commit/tree，并与可信 handoff commit/tree/path/blob 交叉验证；还必须从 tag tree 读取同一版本来源 inventory。持久化前需确认 `release_evidence_branch_ref` 仍精确等于已捕获的 `release_evidence_expected_head`，再按 CAS/fast-forward/readback 协议处理。此文件只提供输入契约，不预先授予 `release_verified`。
