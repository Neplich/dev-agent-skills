# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-003-preserve-facts-and-add-traceability`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-003-preserve-facts-and-add-traceability`.
- Fixture SHA-256: `da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17`
- Prompt SHA-256: `1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0c9b1305da43afbfc22e6d563651831ce45be05793224d552c008cc393a37b1e`
- Skill overlay SHA-256: `2f0de1beb8d9a238bffa058ef4ccfb94546f593a81b4fc6e5c1f6bcddf8dbe71`
- Judge schema SHA-256: `13218ab4a7abff52fb220f782ffa27173bde4d7c9a5b1ae26ef3115112e26b3d`
- Eval definition SHA-256: `95f3370a6690706f871a83ed16fd2ea4af289f136e5af47351107d1ec6c06fc2`
- Metadata SHA-256: `9e52b1a05d9dc7bd3856fe83df9035077725f4a4387447107b2ae09c5bfbb539`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_confirmed_release_facts` | PASS | With-skill preview preserves all confirmed release-note facts, including user features, compatibility, database migration and deletion risk, deployment order and flag, dual-architecture assets, upgrade checks, and old-browser limits. |
| `adds_verified_traceability_links` | PASS | With-skill output includes the complete intended compare URL ending in v1.0.0, representative PR links, the direct target-commit link, and contributor links consistent with the evidence. |
| `curates_instead_of_dumping` | PASS | With-skill output organizes the release around user-facing facts and includes only three curated maintenance links; it does not paste the 18-commit maintenance feed. |
| `blocks_on_fact_conflict` | NOT_EXERCISED | The locked evidence contains no GitHub-versus-site fact conflict or newly exposed conflicting fact, so the conflict-blocking behavior was not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=a23a53f3128bffaf04ea6289c84df40b9d58c743534e481da8c7f4ab465b1f60; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a fact-preserving, curated preview with verified traceability links and conservatively blocked draft/publish actions pending tag evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1f72f4ad91d022aceb74cd22a41be167aaa46a8a39f2494e69954624a58e1ac6; fixture_sha256=da29a479071012ab3bfa3af5ab47af8541f3b6d49a5ec8e88304fa50a27aed17; output_sha256=48de5a7d19cad0ac3b1c88f6cbb67c8fdf44609d51bf9f78b7aa31a43a46e915; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a broadly complete preview but claimed confirmed release readiness and could proceed to tagging without the with-skill verification gates.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
