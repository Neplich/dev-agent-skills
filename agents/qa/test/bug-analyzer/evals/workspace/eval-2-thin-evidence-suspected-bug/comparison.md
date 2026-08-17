# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-002-thin-evidence-suspected-bug`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266` from `agents/qa/test/bug-analyzer/evals/workspace/eval-2-thin-evidence-suspected-bug`.
- Identity schema: `2`
- target_skill_sha256: `f7992d17a0646109f134e112dee5a8d92a38fd3d8cf3007564f0979ffbd3929d`
- eval_definition_sha256: `ee85b4030fea85acc8c079589b9268be5087962ef495cf3e3194580abf721432`
- metadata_sha256: `8cbc4de235b64dc94f1f26425c852e96d8c8a43534bff26146b8ba13fd8eb92c`
- fixture_sha256: `bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `086365b086fd130d9ef17a34e69f11d6786884f09ea0525a080792033b47d5cb`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `27a39b82b995acb5c798df074b3eb2e54e5b81ea6292feb84f2c09cf3d65fb1c`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `keeps_status_unconfirmed` | PASS | With-skill output and the locked delivery file explicitly classify the report as suspected / needs more evidence, with low confidence, and state it is insufficient to confirm a defect. |
| `separates_impact_from_confidence` | PASS | The delivery file separately records low confidence, unknown release impact, and potential implementation impact, while explaining that the evidence cannot distinguish the underlying cause. |
| `requests_decisive_evidence` | PASS | The output and delivery file request reproduction steps, expected/actual behavior, environment and version details, and applicable screenshot, video, console, network, server-log, and trace evidence. |
| `avoids_confirmed_bug_write` | PASS | The only persisted artifact is an unresolved QA record explicitly marked suspected, low-confidence, and not sufficient to confirm or hand off an implementation bug; no GitHub issue or confirmed bug was created. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=4e3744f5c46ed6bfa87ec2ab653c86323d4e9fef0cc31fb6d381218ad10d3b33; snapshot_sha256=cb95ac1b65957a637e1a7c398de037a737169555cd6a661c63d7d32414292861
- Behavior: Correctly kept the report unconfirmed, separated confidence from potential impact, requested decisive evidence, and persisted only an explicitly unresolved QA record.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=78696c84c936a27db0d476b9673a2b9f30099e53a98c303b4036832baf353eb7; fixture_sha256=bd09f8717eb7765700b65e2c38ca5c4dcc82c7aff0bee46b30335bbb10dcf266; output_sha256=368ffd109396616f709b67a594783b1d680e00c7a9a6a9fbab831cec2444347c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also kept the report unconfirmed and requested relevant missing evidence, but did not create a persisted artifact.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
