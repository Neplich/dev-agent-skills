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
- target_skill_sha256: `31c42c9c81d87e424d5816b727ce29e3aa5b6dba7a54b776905197eb51df50fd`
- eval_definition_sha256: `fbd695e0a879758e25936e89babfefc9a6cba4a52e1572a61e1da7fea0b1364b`
- metadata_sha256: `1dfb7bfbfed7613af8764f4385cade9d5822d1652d85a0cbb75853e0bcae7474`
- fixture_sha256: `8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f6a7dabb82746a0dc0f0c5965d8e78c276cdccf3d2da25bfbb1a77e91ffeca3f`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `348b8622cc87aa2759a4e099ebeaa2c933204e02a0dfad702e10984b10a232be`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `semantic_classification` | PASS | 锁定的 docs/roadmap.md 将 Go1.26.1 分类为近期补丁、Go1.27 分类为中期计划、Go2.0 分类为远期规划，并将 Runtime experiments 列为待维护者确认。 |
| `no_fake_dates` | PASS | 锁定文件未生成 Mermaid Gantt，仅生成不含日历日期的阶段 flowchart，并明确说明没有可靠日期、不生成 Gantt 图。 |
| `release_blockers` | PASS | 锁定文件以“发布阻塞项”独立加粗区段突出展示带有 release-blocker 标签的 #4101。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a; fixture_sha256=8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f; output_sha256=a6a765ec441c2b3d5b71478694d72889d59af14ed7907c17a3b7536c328aa02c; snapshot_sha256=11cdfb2be75d23e4a75f2ebc2090b262cbc5fdc46d1729175490c62642a8b104
- Behavior: 生成了按语义分层的路线图，明确处理待确认 milestone，避免 Gantt 和虚构排期，并突出 release-blocker。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4165caadd548c6b8d1d9df4c0aa9c054ed9c0f0a71e88ab4aefd0c18bb92400a; fixture_sha256=8ed1c517c0f0999b8177c14728f4f1837cf8c41c83a93a8766a4e6fd07e1d14f; output_sha256=bd15c868d2dce6dbe2a6278af8829d074f001ce66dffa2033d14736f68556fcb; snapshot_sha256=eccce1d86d2d05bf7a512e447905a28fce172dbd6ae7b3c6ed52e8a8c5966e87
- Behavior: 也生成了基础版本分类和无日期说明，但未明确将无法匹配的 Runtime experiments 交由用户或维护者确认。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
