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
- Repository HEAD: `5eed6bd61702fe0e1aa38eba2649b61fbdbcd5a6`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4e76801189b426dd33ce29ced16e549279e16d547ce6762d36863400f4354122`
- Skill overlay SHA-256: `77702f471e61dbfa60bd67a78323dc643acf1a23ee94c61de468a9d3da2ceccc`
- Judge schema SHA-256: `d4acd94dda2c52416ad87fb2e12177cf797b75ea923eded4095dac24f71a6a61`
- Eval definition SHA-256: `b9fa50e25ae21150a7999f6d53a6c6d8b0466463a4d2f36c8c86411a0483e826`
- Metadata SHA-256: `484b4662019ef115d32bbdc63a4fe4cffc2cd503d4cd9fc5262185023225f4ca`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routing_decision_present` | PASS | with_skill 输出明确给出 Routing decision，选择 pm-agent:idea-to-spec，并标明 entry_basis、execution_boundary 及 unresolved scope。 |
| `requires_product_and_engineering_basis` | NOT_EXERCISED | 输出确认产品范围、PRD/DECISIONS、技术约束和工程交接范围均未完成，并停留在需求发现；但 TRD/等价技术设计到实施计划之间的后续门禁尚未因用户确认而实际执行。 |
| `blocks_implementation` | PASS | with_skill 输出停留在 greenfield-discovery/idea-to-spec，明确暂不编写代码或技术设计；交付快照为空，且没有实施计划、代码或测试实现。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=17c7df6531697c7e11aac19074833f8af95924c378f0ccf81f99d8053b4a25ca; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为范围未确认的新功能，路由至 pm-agent:idea-to-spec，要求先完成需求收敛并等待用户确认，未产生实现文件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=03ba8f707e1ad80244b9a91b06f8107bed5601bb3190b7ac2bbc330a16bd52ac; snapshot_sha256=4ef727066b1b30df5535e49d30ad7062065fd5cc8217cd36a72015ca24a0b779
- Behavior: 直接假设个人资料管理并创建实施计划、页面、样式和脚本，完成了 MVP 实现。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 获得用户对功能方向和范围的确认后，再验证 PRD/DECISIONS、TRD或等价技术设计及 implementation scope 门禁。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
