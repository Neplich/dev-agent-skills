# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3` from `agents/docs/test/docs-agent/evals/workspace/eval-005-integration-release-chain`.
- Identity schema: `2`
- target_skill_sha256: `af94ca4b38768885230f6271f3d4ae9e1b1be30fcd2f5bdf1098250b4ded0306`
- eval_definition_sha256: `05d8b9eb5ccf6bbc077dad850c79899562c5b4ed9bbb4187abffd82f21410ea3`
- metadata_sha256: `af301306a3e584e9c32987cd73e02ac298dcd98f38208af58ca0764e8b5a4154`
- fixture_sha256: `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `1f2ea17b811fce39b8e906ef0e0a70b6a6223a188a2f4a05f2f0a88c54c6aceb`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `e710f507db19462d482cc0a7c6de3ea1d17c9f7caf25c7c65d0a74377ce36ba1`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_audit_entry` | PASS | With-skill output identifies release-chain-entry.md, confirmed v1.4.0 scope, signed snapshot, evidence sources, and the no-mutation boundary. |
| `evaluates_site_release_notes_gate` | PASS | It recognizes the handoff as a pre-tag audit entry, notes missing ready_for_tag/release_verified results, and routes work to docs-audit before GitHub Release preparation. |
| `validates_release_window_basis` | PASS | It correctly states v1.3.0 and release-base both resolve to 041b91a..., establishing a parseable previous-tag/base comparison anchor. |
| `rejects_missing_pre_tag_authority` | PASS | It does not claim pre-tag success and explicitly reports that no ready_for_tag audit conclusion exists. |
| `detects_post_tag_evidence_drift` | FAIL | It detects that release-candidate/tag-entry resolve to 5dc0861... while v1.4.0 resolves to 9ae0a8..., but its opening conclusion says the release chain can continue instead of returning the current chain as blocked on this drift. |
| `blocks_github_release_handoff` | PASS | It concludes that GitHub Release preparation/publishing cannot proceed, provides no preview/draft/publish handoff, and routes the next step to docs-audit. |
| `preserves_no_mutation_boundaries` | PASS | Locked git evidence shows unchanged HEAD, branch, refs, diffs, and worktree; the output also explicitly limits execution to audit handoff without tag or GitHub Release mutation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=3b216a9033993b7f317309ac8d4fc6938d4002b3a46807d7969a1f59283f6c3d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Accurately accepted the audit entry, validated the release-window anchor, rejected unproven pre-tag readiness, and blocked GitHub Release handoff, but undercalled the detected post-tag tree drift.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=b34d66b1018363a3f4fd7f3fb97fb431248450a74e4bef063df957c8957d807c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identified the post-tag tree mismatch and state inconsistency, blocked GitHub Release progression, assigned remediation to the release manager/tag owner, and preserved read-only boundaries.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- detects_post_tag_evidence_drift
- Next: Return the current post-tag audit state as blocked because the signed snapshot shows the actual tag and release-evidence branch differ from the audited candidate tree.
- Next: Require a fresh signed reference snapshot and a successful release_verified audit before any GitHub Release preparation.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
