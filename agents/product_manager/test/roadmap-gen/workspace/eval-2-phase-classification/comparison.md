# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-002-phase-classification`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a264a565b80cdab16388e48390a97336c870c675ea266e111b6f98276cf41192` from `agents/product_manager/test/roadmap-gen/workspace/eval-2-phase-classification`.
- Fixture SHA-256: `a264a565b80cdab16388e48390a97336c870c675ea266e111b6f98276cf41192`
- Prompt SHA-256: `129b1e07f1b508c4a87a365c1e9c5e8cf169856473baee027f1d68878bcd93f2`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `74b972ac8dbd7706448e20025f6995b87c544e99309b65961f70d0e86a7bd191`
- Skill overlay SHA-256: `bddee41393bca0a60880eaa8d81044ec84f2c1d751e6af66c6178450b19850d3`
- Judge schema SHA-256: `828832f79453e0784207e366cba87f24e08c6f3017321b257129f96f3076509d`
- Eval definition SHA-256: `9bebcff97f69229af9d2fc6b841c4826a4650eeb5ee2c6254e8400fa19d31afa`
- Metadata SHA-256: `ae0af75c7768cc5a422a172a7778c85838314f028847e67a9b64a099fa24dc99`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `open_closed` | PASS | with_skill 文档将 August/September 标为当前冲刺与近期计划，并将 closed 的 July milestone 放入“已完成”区域。 |
| `large_backlog` | PASS | with_skill 文档明确 backlog 总数 128、实际获取 6 条，仅列出 3 条，其余 122 条未列出，保持摘要可读。 |
| `issue_details` | PASS | with_skill 文档按标签/类型分组展示 issue，并为各 issue 保留 GitHub 链接、标签和 assignee/unassigned 状态。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=129b1e07f1b508c4a87a365c1e9c5e8cf169856473baee027f1d68878bcd93f2; fixture_sha256=a264a565b80cdab16388e48390a97336c870c675ea266e111b6f98276cf41192; output_sha256=aafa4138e6d96f306c9e5ea32c5eb643eb7b6dd32647a7d5b37333e03db79c8c; snapshot_sha256=8d42f15c91d81bbee8814012ce6e14b59931f65e54e82ad2b4b8cc18a2bf1503
- Behavior: 完整生成并交付路线图，满足全部三项断言。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=129b1e07f1b508c4a87a365c1e9c5e8cf169856473baee027f1d68878bcd93f2; fixture_sha256=a264a565b80cdab16388e48390a97336c870c675ea266e111b6f98276cf41192; output_sha256=6dcc72ef9a96a0def639ce1d93d84adfacac5b8afd783476d9e4996657ecce60; snapshot_sha256=bf58ec5257f4abb6d6f56c4a92df7274d0ca5715c712aa7adc4da2bd6356ef42
- Behavior: 也生成了可用路线图并满足全部三项断言；作为比较基线记录。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
