# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-005-design-gate-mismatched-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-005-design-gate-mismatched-evidence`.
- Identity schema: `2`
- target_skill_sha256: `a3e1263ac8acb74f106913f935cefb0ebe0f7f059ccc011cd16715592fd0163d`
- eval_definition_sha256: `9b46c27014c750c2c7c902ee9b735c340d6216e70bd1db10e9ac7cfe4ffa72b8`
- metadata_sha256: `8201495b57b213f9db3f5219d86222ff877b211b7bfe7d5c149fe15482812507`
- fixture_sha256: `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `c9b93b28ac72af6810f4752921bb72d418af8d9162ae5d66c15fe90f929562c8`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `b6ae3621879be63fa5b02212924eed11dd010ad027f0308f85d7666d26a57421`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_evidence_mismatch` | PASS | With-skill output explicitly identifies the `preferences-summary` versus `account-preferences` mismatch, calls it a blocking conflict, and states it stopped before Step 4 and any writes. |
| `design_zero_change` | PASS | With-skill output reports zero writes; locked git evidence shows unchanged HEAD, empty status, and empty worktree diff. |
| `routes_to_owner` | PASS | With-skill output routes the path ambiguity to `pm-agent` and the TRD alignment issue to `engineer-agent:trd-gen`, requiring unified paths before retry and stating it will not guess. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=ce5366ab7e58f25e91f54665140ffc1316d10153c1d3ae7d0406ee12b22111c5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Blocked on the evidence mismatch, preserved both design surfaces unchanged, and routed each correction to its owner.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=a6b26a10d573e9e4942e19cb5ecf858b8585d1b167a31904ad8044198334abeb; snapshot_sha256=736859f7e81a08b8217c6ef2cb8ebcddfb2e356203c7914f6ed436acfd951a3c
- Behavior: Treated the mismatch as a naming risk, proceeded with the sync, and modified both design surfaces.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
