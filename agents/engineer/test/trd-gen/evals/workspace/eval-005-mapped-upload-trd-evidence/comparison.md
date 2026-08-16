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
- Identity schema: `2`
- target_skill_sha256: `340d804f93e6fcb990681bc077bb9f53d3744da12f12a7cfbbe7aa88f980f67e`
- eval_definition_sha256: `ed02404d14ffd40d542c29f44a74caf2fc5696740b01f75b11e50dfad6379f60`
- metadata_sha256: `c635fd02477c894e8c2d799454c0ae575efcc805f8bc3e18a331d13c47cdc0b8`
- fixture_sha256: `b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `efd5278a6dcac3b779ffc2f7bc7fbcdcc73c391218f35b1bba7e6f95759a7887`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Raw trace shows the change map was read, then its required document `docs/site/api/upload.md` and `src/upload/limits.txt` were read; no unrelated repository document contents were traversed first. |
| `verifies_against_code` | NOT_EXERCISED | The with_skill lane directly read `src/upload/limits.txt` and identified the 10 MB code limit versus the document’s 20 MB limit and its impact. However, no TRD could be produced because the required PM handoff, PRD, and feature path were missing, so the TRD-evidence portion was not exercisable. |
| `treats_unverified_as_low_trust` | PASS | The output explicitly treats both relevant documents’ `last_verified_version: unverified` status as low trust and says the document cannot independently determine the implementation; key conclusions are based on `limits.txt`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888; fixture_sha256=b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007; output_sha256=a1097ea7112482653732a312729cd0f995162af277f00f03add0922583a58a56; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Followed the mapped-document and code-verification workflow, preserved the 10 MB versus 20 MB discrepancy, applied low trust to unverified documents, and correctly stopped before creating a TRD without confirmed PM scope.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888; fixture_sha256=b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007; output_sha256=d9a4403df770c8f7e2d828fc13e8134be805414ec09528ab79825b7066409463; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a useful baseline analysis and proposed a technical design, but did not demonstrate the explicit low-trust handling or Engineer PM-entry gate seen in the with_skill lane.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain the missing PM handoff/PRD and canonical feature_path, then generate the TRD while retaining the verified discrepancy and impact.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
