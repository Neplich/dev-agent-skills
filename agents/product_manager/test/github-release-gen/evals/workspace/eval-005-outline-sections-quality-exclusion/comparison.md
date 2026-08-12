# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-005-outline-sections-quality-exclusion`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f342d8ca65c8f77883288a82a7edf00ac90a64350a66217406a6bf2cc1477c79` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-005-outline-sections-quality-exclusion`.
- Identity schema: `2`
- target_skill_sha256: `0c9b1305da43afbfc22e6d563651831ce45be05793224d552c008cc393a37b1e`
- eval_definition_sha256: `5768440d836f6d58f2492f6254c4eaae18fe913a310437aaee98134c39857a50`
- metadata_sha256: `a9879c47e38cec76a35a3ff0087c5b764086d8e7ca04745f8977bbd30db8f459`
- fixture_sha256: `f342d8ca65c8f77883288a82a7edf00ac90a64350a66217406a6bf2cc1477c79`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f3cdc20a6c2d6d35b8761172794fe96e07166b0922a8d802a01f520259d39177`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `follows_outline_sections` | PASS | with_skill 正文包含且仅包含「重点更新」「其他改进」「升级说明」「变更明细」四节。 |
| `excludes_internal_quality_evidence` | PASS | with_skill 预览正文未包含 skill eval、assertion 计数、review 轮次或 QA 汇总等内部审计证据。 |
| `preserves_confirmed_facts` | PASS | with_skill 保留了文件卡片、原位重试、统一附件模型、nullable JSONB 迁移及删列风险、部署顺序与开关、双架构资产、升级动作和旧浏览器限制。 |
| `title_matches_gate` | PASS | with_skill 标题为「v1.0.0 - 文件卡片与失败消息原位重试」，不是裸版本号。 |
| `upgrade_note_fixed_structure` | PASS | with_skill 的「升级说明」包含完整简述和基于已确认事实的部署/验证指令；未臆造 coding-agent 客户端小节、安装命令或 plugin 更新声明。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=f342d8ca65c8f77883288a82a7edf00ac90a64350a66217406a6bf2cc1477c79; output_sha256=fde85f78f48a4dab7ad7e0f25a2572bd441e537f021fae76c35d5d31ef5d08f0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 生成了完整的四节 GitHub Release 预览，保留已确认事实，排除内部质量证据，并遵守标题与升级说明门禁。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=f342d8ca65c8f77883288a82a7edf00ac90a64350a66217406a6bf2cc1477c79; output_sha256=d3f11bb39e3a0b447218bbfed6cc8f58fa8896231151114b91f052e5c6e087a4; snapshot_sha256=be4930c3c2113293c037680d72c8cfdaec01fc5f314d6319471c1feb6423f767
- Behavior: 生成了预览文件，但采用了约定外小节并包含内部质量证据，未遵循固定四节结构；其对比失败不影响 with_skill 断言判定。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
