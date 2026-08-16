# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-008-direct-specialist-bypass-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-8-direct-specialist-bypass-gate`.
- Identity schema: `2`
- target_skill_sha256: `ed93e443692bf05e76aaa38c8a5b8faff57190219ed48b9335316584424e6eb9`
- eval_definition_sha256: `8a82a9f209d1a183092f0d4416072c9a81f83d51dc3e54ad21c9aa1a4db84c97`
- metadata_sha256: `2863415ed2f417f781064860e7cfabcfbd9a9995e8d831c6cb07097f6b82501a`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `049b196f8151e781cd3892a636ec145a437d1dcd4e2c9a7ed5826e9f1d8c5e14`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `329dfda7786ff3523b5c346349f47cd85abc8fd7cdc5970863dfe15fe67a5f26`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_unready_execution` | PASS | with_skill 输出识别范围未确认，指定 PM / idea-to-spec，明确暂不能安全开始写代码；runner trace 显示无文件变更事件。 |
| `requires_product_and_engineering_basis` | PASS | with_skill 输出明确要求先确认范围并产出 PRD/DECISIONS，再由 Engineer 生成 TRD；未从单句需求生成实施计划。 |
| `blocks_implementation` | PASS | with_skill 输出明确保持在 greenfield-discovery、产品发现和范围确认阶段；锁定工作区状态为空，runner trace 未显示写代码或测试实现。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=85bf166a1e8dd533c098e0c118f47cfa7462e16ca518191346fde9bdf6063fd6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确阻止未就绪的新功能执行，停留在 PM 范围确认，并要求后续 PRD、DECISIONS 与 TRD 依据。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=fa7e776b77a3734608544486827ea12f13ec8c45d3f34eb5461c3579c4632ff1; snapshot_sha256=331de0921a276039c2acb4c2d92e9c6cb77d4748d6260ea54a9fc30d3c9434e0
- Behavior: 在需求未定义时仍创建实施计划、代码骨架和测试，作为失败的基线对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
