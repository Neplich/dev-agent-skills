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
- Identity schema: `2`
- target_skill_sha256: `31c42c9c81d87e424d5816b727ce29e3aa5b6dba7a54b776905197eb51df50fd`
- eval_definition_sha256: `9bebcff97f69229af9d2fc6b841c4826a4650eeb5ee2c6254e8400fa19d31afa`
- metadata_sha256: `ae0af75c7768cc5a422a172a7778c85838314f028847e67a9b64a099fa24dc99`
- fixture_sha256: `a264a565b80cdab16388e48390a97336c870c675ea266e111b6f98276cf41192`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `828832f79453e0784207e366cba87f24e08c6f3017321b257129f96f3076509d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `129b1e07f1b508c4a87a365c1e9c5e8cf169856473baee027f1d68878bcd93f2`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `348b8622cc87aa2759a4e099ebeaa2c933204e02a0dfad702e10984b10a232be`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `open_closed` | PASS | 交付快照按 open 的 August/September milestone 组织当前与近期计划，并将 closed 的 July milestone 放入“已完成”区域；状态与计数均与原始快照一致。 |
| `large_backlog` | PASS | 交付快照明确 backlog 总数为 128，仅列出有限记录，并说明其余 122 条未列出，保持路线图可读。 |
| `issue_details` | PASS | 交付快照按 issue 类型/标签分组，且每条列出的 issue 都保留了链接、标签和 assignee 或 unassigned 状态。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=129b1e07f1b508c4a87a365c1e9c5e8cf169856473baee027f1d68878bcd93f2; fixture_sha256=a264a565b80cdab16388e48390a97336c870c675ea266e111b6f98276cf41192; output_sha256=72ae4b04d189cdd6547b994ac1de777ecd9f885f8004c0ae48ca8074ee80dec7; snapshot_sha256=1a1cab0ac43d0971575e96e0c33330093eae0aed0edc8d5f21f5c704e77ce01f
- Behavior: 生成了包含数据时点、open/closed milestone 分区、压缩 backlog、Mermaid 时间线及 issue 标签、链接和 assignee 细节的 docs/roadmap.md。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=129b1e07f1b508c4a87a365c1e9c5e8cf169856473baee027f1d68878bcd93f2; fixture_sha256=a264a565b80cdab16388e48390a97336c870c675ea266e111b6f98276cf41192; output_sha256=aeb581e71b63586a15dcc784298c7d78de28750f790d26138c4234b727c4d5be; snapshot_sha256=76c3f67d508d26e764b27b79f76126bac71ef3f0940d16fe07b27a412fd43e1e
- Behavior: 也生成了可用的路线图，区分了 open/closed milestone、压缩了 128 条 backlog，并保留了 6 条 issue 的标签、链接和 assignee 信息；with_skill 版本的结构化分组与时间线更明确。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
