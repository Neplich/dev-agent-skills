# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-005-mapped-upload-trd-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007` from `agents/engineer/test/trd-gen/evals/workspace/eval-005-mapped-upload-trd-evidence`.
- Fixture SHA-256: `b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007`
- Prompt SHA-256: `415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888`
- Repository HEAD: `7ac19d358ca18ef7b2d109aeec17239bc9d0f4c0`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `241887560d0522d91eee495434f78fbbe72dd8e5d7ed6c58dce70753634045ba`
- Skill overlay SHA-256: `1701eca585dc754d5c838c067ffd884a80205302462ac0a542c908fd069ff822`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `ed02404d14ffd40d542c29f44a74caf2fc5696740b01f75b11e50dfad6379f60`
- Metadata SHA-256: `cfc84017a2f6130d5f5d58c0d09338a6a3beaaf2ead3e34eb6d3229566da0300`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill trace reads docs/site/standards/change-map.yaml, then reads its mapped docs/site/api/upload.md; the workspace-wide command only enumerates paths and does not read unrelated document contents. |
| `verifies_against_code` | NOT_EXERCISED | The with_skill output identifies src/upload/limits.txt as the 10 MB single-request configuration and records the 20 MB documentation conflict plus its impact on compatibility and the need for a product decision. A formal TRD artifact was blocked by missing PM confirmation, so the later TRD-evidence portion was not exercised. |
| `treats_unverified_as_low_trust` | PASS | The output explicitly marks last_verified_version: unverified as low-trust navigation and leaves the final limit and related design decisions for confirmation rather than treating the documentation as authoritative. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888; fixture_sha256=b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007; output_sha256=49baf75ccf690178f5438a5a76590eb239d5ab936225a58cffe980997f9cc10f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Followed the mapped-document workflow, verified the 10 MB fixture against the conflicting unverified 20 MB documentation, and produced a cautious gap assessment while blocking formal TRD work pending confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888; fixture_sha256=b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007; output_sha256=a9e0491909fada6abd92df9b0ccfbfdcceafa9edadfc38662885b2399868b135; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a useful baseline report that also found the 10 MB versus 20 MB conflict and proposed a multipart design, but did not provide the skill-specific blocked-TRD handoff context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain PM confirmation of scope, size limits, compatibility, storage, and feature path; then generate the formal TRD evidence.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
