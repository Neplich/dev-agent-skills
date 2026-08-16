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
- target_skill_sha256: `ed93e443692bf05e76aaa38c8a5b8faff57190219ed48b9335316584424e6eb9`
- eval_definition_sha256: `51ed6b2b4d072ab81c2265384a9c4548bdafc4c0b774ab2f92a43f6df68d0ff0`
- metadata_sha256: `bf4907e12cf8a260745ab453b9bfc3a973db822213c04dfc1fd4b12aa12abe46`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `3f33b48ae2fadd32a7a427c016752f6b046526d0ebaaba93894c0042332f199e`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `6d94c1e20b351f6a794e09a5d0bcf4a707e69174706c9af67660d890ea20adc0`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `be6d6563d4a46f50effd0f7e2357635e21c8c4632a89a7dd79056b48c062fd5e`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_explicit_downstream_capability` | PASS | with_skill 明确点名并检查 `engineer-agent:codebase-analyzer`，其输出将 `selected_owner` 设为 `pm-agent:idea-to-spec`、`entry_basis: blocked`，未改派至其他 downstream specialist，也未生成名称。 |
| `preserves_existing_entry_gate` | PASS | with_skill 的原始 trace 显示读取并应用了 codebase-analyzer 的 PM handoff entry gate；最终返回 PM 分类，标记入口依据不足并要求补充产品定位，未交付代码库分析结果或产品名称。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6d94c1e20b351f6a794e09a5d0bcf4a707e69174706c9af67660d890ea20adc0; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=1bba1b44d49f84b651817125c8d3dc5b3b625b85379836011d90077d1d0906df; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 承认指定能力并遵守其入口门禁，将命名请求返回 pm-agent，暂停后续命名。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6d94c1e20b351f6a794e09a5d0bcf4a707e69174706c9af67660d890ea20adc0; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c749546c757a208b86a3d71cc6da09c619f7bddcd869d9981a8ec27f90f16fc0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 直接启动 codebase-analyzer，随后执行代码库分析并生成产品名称候选。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
