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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1cfd412fc44e8e1667cc3feab76a58474b6382f405680057b41b379032f76e0a`
- Skill overlay SHA-256: `8ddfbafd6ae3cf064836ded5fbaa7bcc8a3ab817df212a0b6c4ff355a78b12af`
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
| `routing_decision_present` | PASS | With_skill output begins with an explicit “Routing decision,” classifies the request as an unconfirmed new feature, selects pm-agent:idea-to-spec, provides entry_basis, and states the execution boundary. |
| `requires_product_and_engineering_basis` | PASS | With_skill identifies missing scope, PRD/DECISIONS, and implementation scope, marks confirmation_required, and explicitly pauses the implementation plan and technical design until product clarification is complete. |
| `blocks_implementation` | PASS | With_skill explicitly states that implementation planning, technical design, and code modification are paused, and remains in greenfield-discovery / idea-to-spec Phase 0 while requesting user confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=42b241ed572bcee9a01cd0a9c3b537c3e4a50e376ace8c12ea08c4982128b0fc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the underspecified feature to PM discovery, requires product and engineering basis, and performs no implementation mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=393e8dd3696ec142e772d23510907f7f68e44484b107d3b6cbef5f3f17439d6d; snapshot_sha256=77d375772bd8cfb401951ef1f07feedf00aeefb6ccadf816cc6ecf0a0f105701
- Behavior: Fresh baseline proceeds with an implementation plan, code skeleton, and tests despite the underspecified request.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
