# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-005-mapped-cache-debug-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d` from `agents/engineer/test/debugger/evals/workspace/eval-005-mapped-cache-debug-evidence`.
- Fixture SHA-256: `5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d`
- Prompt SHA-256: `f67ee52e742cb8b8fa4a2e4a8def50688400c24b6328050c434ae918f3f4101b`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `acf0c5d2caeeb9edf300e1f0c7701e33bb6c45afbe3042c358a9c6ee00d796a7`
- Skill overlay SHA-256: `fe7a8ba393fe785cea7c7f8aebc226c5d2d3fa7e0ca885b983992d7f1c96a094`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `793c3f5cce4575964aaa387ece63f94a0f71e528641010e1ee2d932bd04007a8`
- Metadata SHA-256: `296cf62658138bf9e31e0fd2b92d8abed954cf84bd5c6bd08af68865f72fdfc1`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace reads the change map for `src/cache/**`, identifies `docs/site/api/cache.md` as the sole required document, then reads it; no unrelated repository document contents are read. |
| `verifies_against_code` | PASS | The delivered diagnosis cites `src/cache/ttl.txt` with `ttl_seconds: 60`, contrasts it with the document's 300 seconds, calculates the 240-second discrepancy, and structures the root-cause report around that conflict. |
| `treats_unverified_as_low_trust` | PASS | The diagnosis explicitly notes `last_verified_version: unverified`, treats the documentation as low trust, and states that the 60-second behavior is established by configuration while 300 seconds is not confirmed as an approved expectation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f67ee52e742cb8b8fa4a2e4a8def50688400c24b6328050c434ae918f3f4101b; fixture_sha256=5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d; output_sha256=5bff38cf6c84b64cf4c6fed8b95cbe4cb1d84534957f4c3f17826fa7bfc7683d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Completed the requested static diagnosis with mapped-document review, code/config verification, discrepancy analysis, and low-trust handling of unverified documentation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f67ee52e742cb8b8fa4a2e4a8def50688400c24b6328050c434ae918f3f4101b; fixture_sha256=5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d; output_sha256=06256efdfc772423d45931c133251792142c88fd1eb9f23dd28cd53c6b97ba59; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also identified the 60-second versus 300-second discrepancy but did not explicitly handle the unverified-document trust level.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
