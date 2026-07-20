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

post-tag 必须消费同版本锚定证据，通过 Git object reads 独立解析 tag object/peeled commit/tree，并与可信 handoff commit/tree/path/blob 交叉验证；还必须从 tag tree 读取同一版本来源 inventory。结果记录只能在独立临时 worktree 中原子构造，并通过 staged/committed 单路径、mode/type、schema 与完整 patch gate；caller worktree/index 必须保持不变。持久化前需确认 `release_evidence_branch_ref` 仍精确等于已捕获的 `release_evidence_expected_head`，再按 CAS/fast-forward/readback 协议处理。此文件只提供输入契约，不预先授予 `release_verified`。

成功路径必须先计算并验证第二次 tag tuple 与 observed/expected-head 证据，再渲染含 `release_verified` 的记录；记录中证据节先于结论节。失败路径样例位于 `.eval/git-posttag/audit-v1.4.0-post-tag-blocked.md.in`，只能形成 `blocked`，不得出现成功结论。candidate、discovery 与 post-tag 记录必须复用同一 source binding 并显式互指，由 setup 末尾 self-check 核对。
