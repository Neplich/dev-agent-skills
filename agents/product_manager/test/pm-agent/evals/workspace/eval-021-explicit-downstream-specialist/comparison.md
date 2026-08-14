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
- target_skill_sha256: `a37bf10fca64a8e15e6213ecdd45b65783814d307c78fd8d8ce6ab45b20effef`
- eval_definition_sha256: `a25ca20a1c90e90d338261e574dc858caafd71ea93ffab13ce3ee97baade4f6a`
- metadata_sha256: `bf4907e12cf8a260745ab453b9bfc3a973db822213c04dfc1fd4b12aa12abe46`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3f33b48ae2fadd32a7a427c016752f6b046526d0ebaaba93894c0042332f199e`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `6d94c1e20b351f6a794e09a5d0bcf4a707e69174706c9af67660d890ea20adc0`
- Repository HEAD: `3f5e81c4837ef85284a7d5381575e40267796c92`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `85b3dc3a707d3ddd63729c1517ef95f0e7bebc3e7da84a79200204d57f127d26`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_explicit_downstream_capability` | PASS | with_skill 输出明确检查并进入 engineer-agent:codebase-analyzer；原始 trace 显示读取 pm-agent、engineer-agent 与 analyzer 的入口规则，并据此完成路由。 |
| `preserves_existing_entry_gate` | PASS | with_skill 输出将 selected_owner 设为 pm-agent:idea-to-spec、entry_basis 设为 blocked，未生成产品名称，而是提出 PM 产品发现所需的澄清问题；这符合 codebase-analyzer 的既有入口门禁。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6d94c1e20b351f6a794e09a5d0bcf4a707e69174706c9af67660d890ea20adc0; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a25aea8eae1ed767f52af59d50b8e268c837f97612057a701e642d044c9027b8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 显式进入 engineer-agent:codebase-analyzer 并遵守其入口门禁，将产品命名请求返回 PM 分类，未直接命名。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6d94c1e20b351f6a794e09a5d0bcf4a707e69174706c9af67660d890ea20adc0; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b62171bba0c2ab845efc19ed9c40213f5a476373d097a324fc7cb7923c7c58c9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 声称使用 codebase-analyzer，但实际继续执行代码库分析并直接给出产品名称，未保留 PM 入口门禁。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
