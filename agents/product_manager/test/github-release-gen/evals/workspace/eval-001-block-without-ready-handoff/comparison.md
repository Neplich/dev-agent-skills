# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-001-block-without-ready-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7971e90a4d24648a705271605d4ebb4560650bfee70305b5f8ad9d95d2e46900` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-001-block-without-ready-handoff`.
- Fixture SHA-256: `7971e90a4d24648a705271605d4ebb4560650bfee70305b5f8ad9d95d2e46900`
- Prompt SHA-256: `286c359d7bf7fac12beb682b18d5fbc5dfddaa2eb888069325d5cedb93a5c23c`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0c9b1305da43afbfc22e6d563651831ce45be05793224d552c008cc393a37b1e`
- Skill overlay SHA-256: `2f0de1beb8d9a238bffa058ef4ccfb94546f593a81b4fc6e5c1f6bcddf8dbe71`
- Judge schema SHA-256: `00bb3d210a5b206a0ac9f62c0fe5d7e4f8787acdaa15b33827594f02c88b5a24`
- Eval definition SHA-256: `f104e1c59d5fad76689ae01a26b19666b3049ba013ffcdc08c70032e1a95c629`
- Metadata SHA-256: `9990f4cbb2adede98186059b8ed7e0088b4cd2cc6d822272edf43193f350dfdf`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_missing_handoff` | PASS | With-skill output explicitly marks no-handoff blocked, identifies the missing site_release_notes_handoff, and says it cannot proceed or publish. |
| `blocks_unconfirmed_handoff` | PASS | With-skill output explicitly identifies confirmation_status: unconfirmed and states that docs checks passing cannot substitute for maintainer confirmation. |
| `returns_to_site_release_notes` | PASS | Both scenarios explicitly return to docs-agent:release-notes-gen for confirmation or handoff completion; no upstream evidence is invented. |
| `no_publishable_output_or_mutation` | PASS | The with-skill delivery_snapshot is empty and git evidence shows no changes; the output contains no publishable complete Release body, draft mutation, publication, docs/site mutation, or tag operation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=286c359d7bf7fac12beb682b18d5fbc5dfddaa2eb888069325d5cedb93a5c23c; fixture_sha256=7971e90a4d24648a705271605d4ebb4560650bfee70305b5f8ad9d95d2e46900; output_sha256=34ef2b765b0685008eccac52d6dc415a95100fdcf58377a227804b5e99021c10; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks both release workflows, distinguishes missing versus unconfirmed handoff, routes both back to the documentation owner, and performs no mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=286c359d7bf7fac12beb682b18d5fbc5dfddaa2eb888069325d5cedb93a5c23c; fixture_sha256=7971e90a4d24648a705271605d4ebb4560650bfee70305b5f8ad9d95d2e46900; output_sha256=45f30a89a9a71e396193d7eafa4035346f1eedc49bc6fe8f4d492296aa11afc1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also blocks both scenarios and routes them back to the documentation owner; comparison baseline only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
