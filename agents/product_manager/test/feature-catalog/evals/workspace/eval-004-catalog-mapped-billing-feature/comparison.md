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
- Identity schema: `2`
- target_skill_sha256: `7440f3be22fb3254e3abf20bcd1c6ebca9f2fdee2fae7f710cc03af349b94250`
- eval_definition_sha256: `8d7030970f6fab5f1056baaa7f97792f12e093b11e3211055d5ae790cf0d3bc2`
- metadata_sha256: `b6e639db89ad7dc9c01b74ff5037844027a7f93b1a684864779b0328b14ee4bc`
- fixture_sha256: `dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `855b39267bf29cb8319dc4bcf28cd88b5cba0ad0d7279c117acb672b2cd4540b`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | With-skill trace reads the change map, then the mapped billing document before code verification; no unrelated document contents are read. |
| `verifies_against_code` | PASS | The delivered draft cites docs/site/api/billing.md:13, records its monthly-and-annual claim, cites src/billing/service.txt:1-2, records monthly plus create_subscription as code facts, and identifies annual support as an unresolved discrepancy. |
| `treats_unverified_as_low_trust` | PASS | The draft explicitly treats last_verified_version: unverified as low trust and bases the implementation conclusions on src/billing/service.txt rather than accepting the annual documentation claim. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99; fixture_sha256=dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa; output_sha256=2e55931dbf297d5a37d0faa9f982419a973355fcfccd33e1782daa0c7aa33143; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a confirmation-gated feature catalog draft with mapped-document evidence, code verification, confidence, and the documentation/code discrepancy.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99; fixture_sha256=dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa; output_sha256=f8a8509968d244a1401ce7901a0263c1335207a4708c506b0bc142f1b2e1a887; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a reasonable code-grounded billing summary and identified the annual-plan discrepancy, but its trace shows a fresh direct scan without the mapped-document-first workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
