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
- target_skill_sha256: `e17c69ef6e179644f91ff00df55f141c375753f4668f30aca4e37e8247a60506`
- eval_definition_sha256: `8a82a9f209d1a183092f0d4416072c9a81f83d51dc3e54ad21c9aa1a4db84c97`
- metadata_sha256: `2863415ed2f417f781064860e7cfabcfbd9a9995e8d831c6cb07097f6b82501a`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `049b196f8151e781cd3892a636ec145a437d1dcd4e2c9a7ed5826e9f1d8c5e14`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `690c63b15147f7227b0c742f032d49a25a05b14c43f0e100b18b5ece461a7e43`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_unready_execution` | PASS | With-skill output explicitly refuses direct coding, identifies the request as an unconfirmed new feature, routes it to PM / idea-to-spec, and requests scope clarification. |
| `requires_product_and_engineering_basis` | PASS | With-skill output states that confirmed scope, PRD/DECISIONS, and Engineer implementation handoff are required, and records that no approved product or technical basis exists. |
| `blocks_implementation` | PASS | With-skill delivery has no files or git changes; the output remains in PM classification and scope-confirmation, explicitly saying it cannot directly write code. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=118aaa3c87096bdae0c78d815648ac9f1c2485dc9e268b8436831a5cc47cace1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks implementation and keeps the request in PM scope clarification pending product and engineering basis.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=e8ac5fc46ddbf0363378c93e58fd800288af4f21127f3309b7f6894b8f5b5fb7; snapshot_sha256=278153ed622edd3c38e7e7d1be2a83b7225bd9eccb777d87f2fd7164ac64b426
- Behavior: Fresh baseline directly implemented a profile-management slice, added tests and documentation, and reported completion despite missing product and technical requirements.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
