# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-021-explicit-downstream-specialist`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-021-explicit-downstream-specialist`.
- Identity schema: `2`
- target_skill_sha256: `28ec452f7594200030ea15ffdc8d5edc9ae2298318457884574b818964824cf6`
- eval_definition_sha256: `a25ca20a1c90e90d338261e574dc858caafd71ea93ffab13ce3ee97baade4f6a`
- metadata_sha256: `bf4907e12cf8a260745ab453b9bfc3a973db822213c04dfc1fd4b12aa12abe46`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3f33b48ae2fadd32a7a427c016752f6b046526d0ebaaba93894c0042332f199e`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `6d94c1e20b351f6a794e09a5d0bcf4a707e69174706c9af67660d890ea20adc0`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7d53e861c15cad4cd024a9dabd716a69caec88b381a3a1cc15ff7acaa0596028`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_explicit_downstream_capability` | PASS | with_skill 保留并使用用户点名的 engineer-agent:codebase-analyzer，且通过其既有入口门禁处理请求；未改派其他 specialist。 |
| `preserves_existing_entry_gate` | PASS | with_skill 根据 codebase-analyzer 的门禁将命名请求返回 pm-agent，标记 entry_basis=blocked、next_action=返回 pm-agent，并未生成产品名称；只读检查且无文件变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6d94c1e20b351f6a794e09a5d0bcf4a707e69174706c9af67660d890ea20adc0; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=5052e71c5d6bbc230bbf73c6737f6718b64330a82abd51238d8a17c00540039a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 显式识别并检查 codebase-analyzer 入口，遵守门禁将请求返回 pm-agent，要求补充产品定位后再继续。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6d94c1e20b351f6a794e09a5d0bcf4a707e69174706c9af67660d890ea20adc0; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=2fc536e8a43880c798ea8046e8ab34e71cb5ada5a987b385abc47e6ebd0c859a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 显式调用 codebase-analyzer 后直接分析空仓库并生成产品名称，未遵守其既有 PM 入口门禁。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
