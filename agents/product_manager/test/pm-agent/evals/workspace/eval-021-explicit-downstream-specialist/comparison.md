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
- target_skill_sha256: `e17c69ef6e179644f91ff00df55f141c375753f4668f30aca4e37e8247a60506`
- eval_definition_sha256: `51ed6b2b4d072ab81c2265384a9c4548bdafc4c0b774ab2f92a43f6df68d0ff0`
- metadata_sha256: `bf4907e12cf8a260745ab453b9bfc3a973db822213c04dfc1fd4b12aa12abe46`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3f33b48ae2fadd32a7a427c016752f6b046526d0ebaaba93894c0042332f199e`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `6d94c1e20b351f6a794e09a5d0bcf4a707e69174706c9af67660d890ea20adc0`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7e78554af92e560e1f9a15ef287d0ea9688d8bc36991af32a0c3f0de95657557`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_explicit_downstream_capability` | PASS | with_skill 明确点名并执行 `engineer-agent:codebase-analyzer` 的入口判断，依据其既有 gate 将产品命名请求返回 `pm-agent`，未直接命名或改选其他 downstream specialist。 |
| `preserves_existing_entry_gate` | PASS | with_skill 明确说明该请求不满足 codebase-analyzer 的进入条件，并返回 `pm-agent` 分类；未执行代码库分析，也未直接生成产品名称。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6d94c1e20b351f6a794e09a5d0bcf4a707e69174706c9af67660d890ea20adc0; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=e92f164860bea44179dae3368d928784c78d81cedf352063f216b2cc3f90b1d8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确应用被点名能力的入口 gate，将产品命名请求返回 pm-agent，并报告后续命名能力不可用而阻塞。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6d94c1e20b351f6a794e09a5d0bcf4a707e69174706c9af67660d890ea20adc0; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=1a18125b744279ad50e3660f58c257cebf465a9b3ca4f919cdc422b690580d44; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 作为 fresh baseline，直接执行 codebase-analyzer 分析并因空代码库请求补充产品信息，未遵循命名请求的既有入口 gate。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
