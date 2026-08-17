# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `roadmap-gen`
- Eval: `eval-001-timeline`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165` from `agents/product_manager/test/roadmap-gen/workspace/eval-1-timeline`.
- Identity schema: `2`
- target_skill_sha256: `31c42c9c81d87e424d5816b727ce29e3aa5b6dba7a54b776905197eb51df50fd`
- eval_definition_sha256: `d6df04c011109b2d27a14aaefa7802d9d9c0af801e4acce9ed37afdc4c26a731`
- metadata_sha256: `c374d15583cb501346d3285d30669c9dbaf58b19f95661d07d8aeac8332d8ba1`
- fixture_sha256: `1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `c9231138562bec2ed562cf0d8c1ec94b96debb390ee547b6815473c326c64b09`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `348b8622cc87aa2759a4e099ebeaa2c933204e02a0dfad702e10984b10a232be`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `phase_classification` | PASS | with_skill 的 docs/roadmap.md 将 3.36.0、3.37.0、4.0.0 分别归入当前冲刺、近期计划、远期规划，并标出已完成的 3.35.0。 |
| `undated_semantic_inference` | PASS | with_skill 将无日期的 3.38.0 按当前 release 3.35.0 的 minor 版本语义归入近期计划；将无法匹配语义的 Rendering research 列为待维护者确认阶段，未捏造日期或归入未排期。 |
| `roadmap_artifacts` | PASS | with_skill 的路线图包含各 milestone 进度条、Mermaid gantt、issue 状态字段及 GitHub milestone/issue 链接。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63; fixture_sha256=1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165; output_sha256=3cab4d9719662d21e98baba88cb39b4db8db0ea72c735c2bbd48598fff76128e; snapshot_sha256=09295eec45976179867edabc4848df2006b3755b7c4d1808461b28bdceb007be
- Behavior: 生成并交付 docs/roadmap.md，满足全部用户可见路线图要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ccc64c80301839b5d15a311cba6ab8a69fb955dea99cdfd947a735556c9d9e63; fixture_sha256=1114e9e115cfb91a2f09d56b7563aa8c7433df316dc5fe8c86e2dd3614f9d165; output_sha256=cdcca850603a340c5765913db929294a3e9ed31fba6f809eab38871f57e1bfc6; snapshot_sha256=08cbf8a61e6edcabe91eb03dc781845a9dedd812bd11087436985b883ef979d8
- Behavior: 同样生成路线图，但未按要求保留 Mermaid Gantt、进度条和对无法匹配 milestone 的明确待确认分类。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
