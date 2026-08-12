# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `ui-ux-design`
- Eval: `eval-005-mapped-notification-ui`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a` from `agents/designer/test/ui-ux-design/evals/workspace/eval-005-mapped-notification-ui`.
- Identity schema: `2`
- target_skill_sha256: `a26ada6a2ba843cfb4e657c89ce7c3b76b2095d2b006f263e49042916f04185f`
- eval_definition_sha256: `25a9beaf5037d128f11073d7bdad29e775b60a170f80ba9b4b2cd556e1ef1469`
- metadata_sha256: `10998afd499537d318b7152b7f04f522887c53c432e959ff9a023e23e13617cb`
- fixture_sha256: `cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | Trace shows the task path was mapped to the single required document, docs/site/api/notification-preferences.md, and no unrelated formal documents were read. |
| `verifies_against_code` | PASS | Trace and final response inspect src/ui/notification-preferences.html, note the missing checked attribute, and correctly conclude the checkbox defaults off despite the document claiming on. |
| `treats_unverified_as_low_trust` | PASS | Trace and final response identify last_verified_version: unverified, treat the document as low trust, and verify the default against the HTML. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2797a1f8eaaa6ec1663895e21733e03c38b2053355b7534ad87b60c49209372a; fixture_sha256=cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a; output_sha256=b9e10953269afd6793ae91e03a6aea2c321a1beb713c51d1f71fea19902955d1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly followed the mapped-doc and code-verification process, but blocked on the handoff gate and produced no design deliverable.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2797a1f8eaaa6ec1663895e21733e03c38b2053355b7534ad87b60c49209372a; fixture_sha256=cc899f673f7067e0f23d4e43273fcee59ea0d49ecc2127d06d0f6831a3eb4d0a; output_sha256=0c23d69c880448c1f023c0010de8068768794ec0c114d1e79375ff99efbc195c; snapshot_sha256=371d676555c845bac1b164ae91215b1f2f2316888ce3adb140b8df69f44ec19d
- Behavior: Delivered and updated the notification-preferences specification, including the default-state discrepancy and interaction guidance.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- No UI/UX specification or frontend handoff artifact was delivered in the with_skill lane.
- Next: Obtain or confirm the PM/design handoff and feature path, then produce the UI/UX specification artifact.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
