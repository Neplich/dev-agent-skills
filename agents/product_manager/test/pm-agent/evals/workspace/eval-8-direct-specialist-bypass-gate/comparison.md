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
- Repository HEAD: `33a503192c752d6227de1bc0d8d8a2e78e31cdf5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b87fb93cdb85ecb0436a61b1aedfcf9c8b41c4cd8f9eff41c412a3196c1d245`
- Skill overlay SHA-256: `56390e18f057b654978938889dac7daf0263eaaf39d741419b573d12bff2c198`
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
| `routing_decision_present` | PASS | 明确输出 Routing decision，包含 selected_owner 为 pm-agent:idea-to-spec、entry_basis: missing，以及 execution_boundary，并将请求路由到 PM 承接。 |
| `requires_product_and_engineering_basis` | PASS | 明确要求先完成需求发现、PRD/DECISIONS、技术设计和确认范围，并指出当前缺少用户目标、业务规则、技术设计及验收依据。 |
| `blocks_implementation` | PASS | 明确停留在 greenfield-discovery，声明暂不写代码、测试或技术实现计划；锁定 git 证据显示无文件、索引或提交变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=0edef3ea8623a77736974bf10f8c80835bdfa813cb5ef9cc89ed3c7968bdcd39; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 先进行 PM 路由和范围确认，停留在 greenfield-discovery，未执行实现。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=40a51f29c8ee21293d942f8bc4961d1158ef35c73a70b98cb42358fa61dc0894; snapshot_sha256=a2c623a34a7efe69b9d4841e0be754625c07524e12082b8146c9d8e6c979617d
- Behavior: 直接假设账号资料功能并创建 API、源码和测试，之后才列出待确认事项。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
