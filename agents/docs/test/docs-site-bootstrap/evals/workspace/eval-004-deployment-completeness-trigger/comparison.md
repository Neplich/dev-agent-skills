# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-site-bootstrap`
- Eval: `eval-004-deployment-completeness-trigger`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842` from `agents/docs/test/docs-site-bootstrap/evals/workspace/eval-004-deployment-completeness-trigger`.
- Identity schema: `2`
- target_skill_sha256: `2846695e854af26b77f56804bd16db1050e2bacd34407999d119ed4e4a881599`
- eval_definition_sha256: `f0a0699462419947dfa64649c390cf74a3d370111b9c3ea826e84a8d4dc9f735`
- metadata_sha256: `abed400d8529a0bd91cc069fda9057f38aa9e64b1a632698bb6d1e29c26ae6e8`
- fixture_sha256: `4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `84cb88cc9e25dde2fbf0d2a0fb5349bfe630e32b333634cfdb918d30e60002a8`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `c4382a755d40b4c37cbb5843089f99a5655b439fd2c6460df6c8b5adeb479967`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classifies_first_bootstrap_integrated` | NOT_EXERCISED | With_skill stopped at the bootstrap entry gate and did not perform a first bootstrap or post-commit deployment classification. |
| `asks_first_bootstrap_choice` | NOT_EXERCISED | With_skill did not inspect a host lacking a documentation site or reach the bootstrap deployment-choice step. |
| `rechecks_rebootstrap_drift` | NOT_EXERCISED | No re-bootstrap was performed, so no drift recheck or Internal-path classification occurred. |
| `preserves_authorization_boundary` | PASS | The candidate explicitly treated the request as read-only, stated that initialization was not authorized, and locked evidence shows no branch, commit, index, worktree, or untracked-file changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=c03ac5d143898fdf7eeb3a684ac33fc4885d0e645df5bdf6b12b5f60fc449dc0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly preserved the read-only authorization boundary but stopped before repository inspection and bootstrap-specific behavior.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a857fcf2c722711dbe976f85685cf13e950a1e35983a7408a6a97bb35347ed24; fixture_sha256=4e3ac8498634ec41445a5f746933f338a50d3c3d4cae8d2f058bd619e288d842; output_sha256=91d19d0286b071f726de5e72f5f6d6b941576b45def9553d930f419d8ea65f0e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Performed the requested read-only repository inspection and reported build, image, CI, Compose/Helm, and ownership evidence, but did not exercise bootstrap workflow assertions.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the explicit bootstrap request, confirmed host repository, and required user confirmations to exercise the bootstrap assertions.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
