# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-004-catalog-mapped-billing-feature`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-004-catalog-mapped-billing-feature`.
- Fixture SHA-256: `dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa`
- Prompt SHA-256: `18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `272c84e241c5d52534922fccf2bc6732492a0d70c9f6e2ab8dc1eff2533f7b0c`
- Skill overlay SHA-256: `9fb06b39d6c186c13ce243a925511364a66cb0da19ef72dd5c8e3b46dd2b75b8`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `8d7030970f6fab5f1056baaa7f97792f12e093b11e3211055d5ae790cf0d3bc2`
- Metadata SHA-256: `b6e639db89ad7dc9c01b74ff5037844027a7f93b1a684864779b0328b14ee4bc`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | with_skill trace reads the change-map, then reads the internal consumption contract before docs/site/api/billing.md; this contradicts the required immediate mapped-doc read order. |
| `verifies_against_code` | PASS | The output cites docs/site/api/billing.md, states its monthly-and-annual claim, cites src/billing/service.txt showing only monthly and create_subscription, and explains the annual-support impact. |
| `treats_unverified_as_low_trust` | PASS | The output explicitly treats last_verified_version: unverified as low-trust and bases the confirmed conclusion on src/billing/service.txt rather than the document alone. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99; fixture_sha256=dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa; output_sha256=d9894565b1cc0494f88e43e0d55666d74b57138cc08f9bdb9672fb1196d4d1b5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced an evidence-backed pending feature-catalog draft, verified the billing source, and correctly downgraded the unverified annual-plan documentation, but violated the required mapped-document read order.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99; fixture_sha256=dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa; output_sha256=ba2b0525f1623dc381d163d66ae8afe78d8953bef386bc4ae963d26e5f1f83d4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provided a broadly correct source-vs-document comparison and low-confidence treatment, but is comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane did not read docs/site/api/billing.md immediately after identifying the change-map entry; it read another document first.
- Next: Read docs/site/api/billing.md immediately after resolving the change-map entry, before reading other non-code documents.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
