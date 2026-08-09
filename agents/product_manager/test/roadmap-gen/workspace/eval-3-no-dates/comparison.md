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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `74b972ac8dbd7706448e20025f6995b87c544e99309b65961f70d0e86a7bd191`
- Skill overlay SHA-256: `bddee41393bca0a60880eaa8d81044ec84f2c1d751e6af66c6178450b19850d3`
- Judge schema SHA-256: `f6a7dabb82746a0dc0f0c5965d8e78c276cdccf3d2da25bfbb1a77e91ffeca3f`
- Eval definition SHA-256: `fbd695e0a879758e25936e89babfefc9a6cba4a52e1572a61e1da7fea0b1364b`
- Metadata SHA-256: `1dfb7bfbfed7613af8764f4385cade9d5822d1652d85a0cbb75853e0bcae7474`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `semantic_classification` | PASS | 交付的 docs/roadmap.md 按当前版本后的补丁版 Go1.26.1、下一 minor Go1.27、远期 major Go2.0 分类，并将 Runtime experiments 标为无法仅凭名称确认阶段、待维护者确认。 |
| `no_fake_dates` | PASS | 交付文件明确记录 due_on 均为 null，未生成 Mermaid Gantt；日期仅使用证据中的抓取/更新上下文。 |
| `release_blockers` | PASS | 交付文件以“发布阻塞项”突出列出带 release-blocker 标签的 #4101。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a; fixture_sha256=8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f; output_sha256=f7b5cee9d5a79c3d436d7fcc96583c32f6014a84acf6cc89ccb158ac0bdced62; snapshot_sha256=e071008d39586820391975b638a350319b5cb46d902544287410dc3ba5f8f7bf
- Behavior: 成功写入路线图，完成语义分类、日期约束和发布阻塞项突出显示。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a; fixture_sha256=8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f; output_sha256=eb0b5db69da2c9220987703d084cd3d6df6b9f5abb267320e2841e67ddd92d21; snapshot_sha256=7dd086fbbd65d13eec0975ec73ed463e9ddcd05e9531f022cc3fe5b269f2f8e0
- Behavior: 也写入了路线图并覆盖主要版本分类与日期约束，但未明确将无法匹配的 milestone 交用户确认。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
