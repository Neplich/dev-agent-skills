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
- target_skill_sha256: `a37bf10fca64a8e15e6213ecdd45b65783814d307c78fd8d8ce6ab45b20effef`
- eval_definition_sha256: `8a82a9f209d1a183092f0d4416072c9a81f83d51dc3e54ad21c9aa1a4db84c97`
- metadata_sha256: `484b4662019ef115d32bbdc63a4fe4cffc2cd503d4cd9fc5262185023225f4ca`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `049b196f8151e781cd3892a636ec145a437d1dcd4e2c9a7ed5826e9f1d8c5e14`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167`
- Repository HEAD: `3f5e81c4837ef85284a7d5381575e40267796c92`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6f4abf80e411dc3e6124c51093f07046c341195b1b2f0e9981a535c9960cb623`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_unready_execution` | PASS | With_skill output classifies the request as a new feature with missing entry basis, routes it to pm-agent:idea-to-spec, keeps feature_path unresolved, and explicitly says implementation cannot begin. Git evidence shows no workspace changes. |
| `requires_product_and_engineering_basis` | NOT_EXERCISED | No implementation plan or technical design was entered; the candidate correctly asks for product-scope confirmation first and states that PRD/DECISIONS and later technical design are prerequisites. The engineering-basis gate before a future implementation plan could not yet be exercised because user confirmation is pending. |
| `blocks_implementation` | PASS | The candidate explicitly prohibits code, technical design, and tests, remains in greenfield-discovery/product-discovery, and requests the missing product clarification. Locked git evidence shows no files, commits, or diffs. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=16ba383367945f0c3ca2203460d82caa7fe9b8533b95ed90d2b6f7d5a2e30e3f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks execution and keeps the request in PM scope discovery pending user clarification; no mutations are evidenced.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b05adf08dcfd55a0069561e08250366df7fc91ba380f516b03a99d4e07e43764; snapshot_sha256=12e291d5fa4ccf79abd5ddbf542dc0ecb7a2c42c2950e65d3c894441b04b2423
- Behavior: Fresh baseline immediately invented an account profile/password scope, created an implementation plan and code/tests, and reported passing tests.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Await user confirmation of the product scope before evaluating downstream PRD, TRD, and implementation-plan gates.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
