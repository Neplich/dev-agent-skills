# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-003-no-dates`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f` from `agents/product_manager/test/roadmap-gen/workspace/eval-3-no-dates`.
- Identity schema: `2`
- target_skill_sha256: `74b972ac8dbd7706448e20025f6995b87c544e99309b65961f70d0e86a7bd191`
- eval_definition_sha256: `fbd695e0a879758e25936e89babfefc9a6cba4a52e1572a61e1da7fea0b1364b`
- metadata_sha256: `1dfb7bfbfed7613af8764f4385cade9d5822d1652d85a0cbb75853e0bcae7474`
- fixture_sha256: `8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f6a7dabb82746a0dc0f0c5965d8e78c276cdccf3d2da25bfbb1a77e91ffeca3f`
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
| `semantic_classification` | PASS | 交付文件按 patch、minor、major 语义将 Go1.26.1、Go1.27、Go2.0 分为近期、中期和远期；Runtime experiments 明确列为待维护者分类并请求确认。 |
| `no_fake_dates` | PASS | 交付文件没有 Mermaid Gantt 或发布日期/截止日期排期；仅包含明确标注为无日历日期的语义阶段 flowchart。 |
| `release_blockers` | PASS | Go1.26.1 部分以“发布阻塞项”标题突出列出带 release-blocker 标签的 #4101。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a; fixture_sha256=8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f; output_sha256=b4a92c682726061490a391bf408abf38a05105b02e72b98d977f375fa3557da8; snapshot_sha256=62721fdfada230a7f25de559ccda1a6a07414111f1ef08c9dc8891ad8049a64c
- Behavior: 写入完整路线图，完成语义分类、无日期处理和发布阻塞项突出显示。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a; fixture_sha256=8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f; output_sha256=2aa8804c7488f280699ef5a31b2e1419477ab16b70745c32eeeae229898a4c77; snapshot_sha256=00ceb5a98a25983606e6ee37ca74641dc5041135f6a5670e3630474cbe6a3685
- Behavior: 完成基础路线图并确认无截止日期，但最终摘要未体现语义分类细节或发布阻塞项突出处理。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
