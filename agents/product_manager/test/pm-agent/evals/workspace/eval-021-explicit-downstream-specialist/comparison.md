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
- target_skill_sha256: `cec475406cc49b4c9cebbfe9c62f8f1a19fc3e7ced9282825f8f2930bab1478a`
- eval_definition_sha256: `a25ca20a1c90e90d338261e574dc858caafd71ea93ffab13ce3ee97baade4f6a`
- metadata_sha256: `bf4907e12cf8a260745ab453b9bfc3a973db822213c04dfc1fd4b12aa12abe46`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3f33b48ae2fadd32a7a427c016752f6b046526d0ebaaba93894c0042332f199e`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `6d94c1e20b351f6a794e09a5d0bcf4a707e69174706c9af67660d890ea20adc0`
- Repository HEAD: `133a65e3c3b501be88257e9d3a557af4d5ccd242`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `1a82254c5c5bfa1d7e697ff009c645ec152b12fd65cded8beca63e20954b94ec`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_explicit_downstream_capability` | PASS | with_skill 输出明确点名 engineer-agent:codebase-analyzer；trace 中读取并依据 pm-agent 与 codebase-analyzer 的入口规则，selected_owner 保持为该能力。 |
| `preserves_existing_entry_gate` | PASS | with_skill 输出将 entry_basis 判为 missing，返回 pm-agent:idea-to-spec，并明确禁止代码库分析、工程规划和实现，未生成产品名称；这符合 codebase-analyzer 的既有 gate。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6d94c1e20b351f6a794e09a5d0bcf4a707e69174706c9af67660d890ea20adc0; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=4cbc69bf42623c3e9c7882b10774a5fefafeea6eb29454216dd66516e404150a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 显式使用并检查被点名能力的既有入口 gate；因缺少项目上下文而返回 PM 分类，未执行代码分析或命名。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6d94c1e20b351f6a794e09a5d0bcf4a707e69174706c9af67660d890ea20adc0; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=33465e8758ca9b4e82a624a9582ce0bb80e0fa25b77ef1314716927fec72fb86; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 声称调用 codebase-analyzer 并继续分析空仓库，随后直接生成产品名称，未保留既有门禁行为。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
