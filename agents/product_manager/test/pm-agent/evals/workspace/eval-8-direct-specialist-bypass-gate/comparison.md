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
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167`
- Repository HEAD: `b385df5d17058a52081357c8a8480fc146c3d989`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ecf67dca8a2fd53bb0dd6d0a63750ba2716e88dc4af4f77176ea061260d64286`
- Skill overlay SHA-256: `2ed9fef9a54be8009ea156c857682ad7dd82c0e56e3463d3257fe74fe9c977ec`
- Judge schema SHA-256: `d4acd94dda2c52416ad87fb2e12177cf797b75ea923eded4095dac24f71a6a61`
- Eval definition SHA-256: `b9fa50e25ae21150a7999f6d53a6c6d8b0466463a4d2f36c8c86411a0483e826`
- Metadata SHA-256: `484b4662019ef115d32bbdc63a4fe4cffc2cd503d4cd9fc5262185023225f4ca`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routing_decision_present` | PASS | With_skill 输出以 “Routing decision” 开始，明确选择 `pm-agent:idea-to-spec`，并给出 `entry_basis: missing`、`feature_path: unresolved` 与 `execution_boundary`。 |
| `requires_product_and_engineering_basis` | PASS | With_skill 明确指出缺少目标用户、核心问题、MVP、验收标准及技术约束，标记 PRD/DECISIONS 待范围确认，并未进入实施计划阶段。 |
| `blocks_implementation` | PASS | With_skill 明确声明当前仅进行需求收敛，暂不编写代码、技术设计或测试，并停留在 `greenfield-discovery` 与 `pm-agent:idea-to-spec` 阶段。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=d40bdbccc915e6dfef359c9c6e5b4a57273689a963dd4746866286e1c87acfa0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确将范围未确认的新功能路由至 PM，并阻止实施动作，要求先完成范围确认与产品/工程依据补齐。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=89c766a65dcc92343312cb6e343947a5a49970ec3356f8ac6d388399a7861e60; snapshot_sha256=5b1ebd72e24940094342f0be5145a8063f98572e7b9e2521856b464da26b7bcd
- Behavior: 直接创建账号资料 API、存储层和测试，未执行 PM 路由或范围确认。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
