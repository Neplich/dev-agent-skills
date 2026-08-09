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
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4e2073febaef7202820d7977feb83c73b7673e1200e4724a3f37b54a20923059`
- Skill overlay SHA-256: `bb6d955d3f1008412eca24a4e3e97d4883ccffc96444f5d6d3cd037fea0800ba`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `c4de00c65a5c492d58d182077c448786bbd54172790d4519f15e143439929064`
- Metadata SHA-256: `66549bc6a4cd28361d4fb0c300ac0600f32823bbce01dba9736725e4b2d843dd`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | The with_skill output names the change-map hit and formal checkout-session document, but locked evidence does not prove read order. |
| `verifies_against_code` | PASS | It identifies the code threshold as 10 minutes, contrasts it with the document’s 15-minute claim, and explains the impact on exploration. |
| `treats_unverified_as_low_trust` | PASS | It explicitly treats `unverified` documentation as low-trust navigation and grounds the threshold in code. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f; fixture_sha256=5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421; output_sha256=bd94eb520fb8606936521c9c090961cab1c5ad2fab04d6348fb21fe5930b6a38; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produces a code-grounded exploration charter, identifies the documentation mismatch, and treats unverified documentation as low trust.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d280f60d4c43a5403f08df3395711e665a24f6defcf1e883ede2ed9c11e2a47f; fixture_sha256=5b1017edbbf8a6df86fadbd205bf7416456f615f000264cc379e5e296b079421; output_sha256=b2bd05533a470fd48dd9b3b28cc72aa061acd0e92a93bb03bb7e74f67909793d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also identifies the mismatch and proposes useful boundaries; comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Verify the document read order if process-level evidence becomes available.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
