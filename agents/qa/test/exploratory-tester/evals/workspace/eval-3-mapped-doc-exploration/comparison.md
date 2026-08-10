# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-003-mapped-doc-exploration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421` from `agents/qa/test/exploratory-tester/evals/workspace/eval-3-mapped-doc-exploration`.
- Fixture SHA-256: `5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421`
- Prompt SHA-256: `d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4e2073febaef7202820d7977feb83c73b7673e1200e4724a3f37b54a20923059`
- Skill overlay SHA-256: `d5a8b4f617bd4daeb6e78fdb531d6c6e6ec5fb1b029628fdf35a46d483c79624`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `c4de00c65a5c492d58d182077c448786bbd54172790d4519f15e143439929064`
- Metadata SHA-256: `66549bc6a4cd28361d4fb0c300ac0600f32823bbce01dba9736725e4b2d843dd`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | With-skill trace locates the change map and then reads the mapped checkout-session document; it only inspects the three relevant repository files and does not traverse unrelated docs/site content. |
| `verifies_against_code` | PASS | The with-skill output and trace explicitly identify the documentation value as 15 minutes versus the code value of 10 minutes, use 10-minute boundary points for exploration, and preserve the discrepancy for docs audit. |
| `treats_unverified_as_low_trust` | PASS | The with-skill output explicitly marks last_verified_version as unverified, treats the document as low trust, and states that code verification is complete; no executable tests exist, so behavioral questions remain exploration targets rather than asserted facts. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f; fixture_sha256=5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421; output_sha256=30e59ca5093c4db6335c3c152020dd52612158f061dfedf587c1593009431267; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a focused checkout-session timeout exploration charter grounded in the 10-minute code threshold, while identifying the stale 15-minute documentation and unverified freshness.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f; fixture_sha256=5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421; output_sha256=33ada0dd78646bb3f7ba90572e2c305bce0375496c719267da95e8be7cf92259; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also produced a valid code-grounded charter and identified the documentation discrepancy; it serves as a fresh baseline comparison only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
