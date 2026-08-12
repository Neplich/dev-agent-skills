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
- Repository HEAD: `8813f864e743f7c83dc2e51e0b5add79f312e870`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0616a11ea39f978cac34906ca01c79a336316825183bb1897d900f056d8544f7`
- Skill overlay SHA-256: `4d4a580c5e7c36b9199abb80221829f90c900c96463581d7f87c6d7ccc538bd7`
- Judge schema SHA-256: `d4acd94dda2c52416ad87fb2e12177cf797b75ea923eded4095dac24f71a6a61`
- Eval definition SHA-256: `cd9751a8b092fc6d7d98d6022afbbb3ec1c871d784270dc60d0af08525fe28a3`
- Metadata SHA-256: `484b4662019ef115d32bbdc63a4fe4cffc2cd503d4cd9fc5262185023225f4ca`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routing_decision_present` | PASS | With_skill output provides a Routing decision naming `selected_owner: idea-to-spec`, `entry_basis: missing`, unresolved scope, and an explicit execution boundary prohibiting planning, design, coding, and testing; it keeps the request in PM discovery. |
| `requires_product_and_engineering_basis` | NOT_EXERCISED | The candidate correctly states that PRD, technical design, and confirmed scope are missing and refuses to produce a credible implementation plan, but the later confirmation and TRD stages cannot be exercised before user input. |
| `blocks_implementation` | PASS | With_skill output explicitly prohibits implementation and the locked workspace evidence shows no delivered files, git changes, or implementation/testing actions. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=86560df66be1336515f9ab483dfbdd8e34e8b488fc0c61c0fd518fcacdafd8ae; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Routes the vague feature request to PM discovery, records missing entry basis and unresolved scope, asks one narrowing question, and blocks implementation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=827e1eab57730473669ffa6562263ebb5fcf35595b38ae224272aca2a629a167; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a743fdc5612fce5601d3a16cd313cfe99ba8c8f806e1b63716a20a56b0ccd2ee; snapshot_sha256=5af0294f1e38bb2b97f3261212ce12cfa1be58009dec51da143c1bb94a32edf8
- Behavior: Fresh baseline immediately created and delivered an account-center code skeleton despite missing product and technical basis.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: After the user confirms the feature direction, complete PM scope and PRD/decision artifacts, then obtain technical design and confirmed implementation scope before planning implementation.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
