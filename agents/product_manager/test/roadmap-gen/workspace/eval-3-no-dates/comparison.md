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
- Fixture SHA-256: `8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f`
- Prompt SHA-256: `4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `74b972ac8dbd7706448e20025f6995b87c544e99309b65961f70d0e86a7bd191`
- Skill overlay SHA-256: `bddee41393bca0a60880eaa8d81044ec84f2c1d751e6af66c6178450b19850d3`
- Judge schema SHA-256: `f6a7dabb82746a0dc0f0c5965d8e78c276cdccf3d2da25bfbb1a77e91ffeca3f`
- Eval definition SHA-256: `fbd695e0a879758e25936e89babfefc9a6cba4a52e1572a61e1da7fea0b1364b`
- Metadata SHA-256: `1dfb7bfbfed7613af8764f4385cade9d5822d1652d85a0cbb75853e0bcae7474`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
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
