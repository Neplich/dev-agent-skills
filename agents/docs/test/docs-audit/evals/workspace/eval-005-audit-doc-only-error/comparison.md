# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-005-audit-doc-only-error`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a` from `agents/docs/test/docs-audit/evals/workspace/eval-005-audit-doc-only-error`.
- Identity schema: `2`
- target_skill_sha256: `a5e0bb043d61dbbb218e7d7efc08374e0d16a4d7aaa3b31817f2038830c90941`
- eval_definition_sha256: `1f7d058864bf71ce0402d8ada31c06c85782a25b93779e842d80b5a98766c9d9`
- metadata_sha256: `63b77017b252b389a44397720be8380b6bee7f6a85225c5d210accca792fc487`
- fixture_sha256: `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `d804d7eed6dff47b2c8744abfb057fce66d8fde2359e03e7f21e978c34808373`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_doc_only_change` | PASS | The with_skill report says the changed formal page was included in the affected set despite no code-file change-map match. |
| `uses_related_code_for_fact_check` | PASS | The with_skill report fact-checks the page against the target-tree `src/catalog/routes.txt`, the page’s declared related-code path, despite no code diff. |
| `classifies_doc_only_conflict_mismatch` | PASS | The with_skill report preserves the DELETE declaration, identifies only GET in the route evidence, cites the evidence path, describes the release impact, and classifies the page as `mismatch`. |
| `blocks_despite_no_code_diff` | PASS | The with_skill report explicitly identifies the phase as `pre-tag`, returns `blocked`, states no audit metadata was written, and does not return `ready_for_tag`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=37ecd7fb1675a1b82c0e04598a4461b9a7ee9eae72bdc0de3f745332d140b0ca; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly audited the documentation-only change, used the related code for factual verification, classified the API claim as mismatch, and blocked pre-tag release.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=90ebaa3018a96d56d3381678e0cd7d3ecd4d642b1d4471471373455bc4b7f5f2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Also identified the mismatch and recommended blocking, but did not provide the full docs-audit protocol result or explicit pre-tag audit state.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
