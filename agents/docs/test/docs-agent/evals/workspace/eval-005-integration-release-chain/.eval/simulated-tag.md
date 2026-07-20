# Simulated post-tag evidence

- evidence_kind: read-only simulated Git object data
- actual_tag: `v1.4.0`
- actual_tag_kind: `lightweight`
- tag_ref_target_object_id: `4444444444444444444444444444444444444444`
- peeled_tag_commit: `4444444444444444444444444444444444444444`
- peeled_tag_tree: `cccccccccccccccccccccccccccccccccccccccc`
- trusted_pre_tag_handoff_tree: `cccccccccccccccccccccccccccccccccccccccc`
- trusted_pre_tag_handoff_path: `docs/site/.meta/audit/handoffs/pre-tag-v1.4.0.md`
- candidate_record_path: `docs/site/.meta/audit/audit-v1.4.0.md`
- target_release_version: `v1.4.0`
- tag_tree_contains_same_version_inventory: true
- tag_tree_contains_same_stamped_pages: true
- tag_tree_contains_same_candidate_and_discovery_blobs: true
- tag_mutation_allowed: false
- github_release_mutation_allowed: false

post-tag 必须消费执行者在本轮 pre-tag 形成并验证的同版本锚定证据，将 peeled tag tree 与可信 handoff tree 绑定，并从 tag tree 读取同一版本来源 inventory。此模拟文件只提供 tag 读取结果，不预先授予 `release_verified`。
