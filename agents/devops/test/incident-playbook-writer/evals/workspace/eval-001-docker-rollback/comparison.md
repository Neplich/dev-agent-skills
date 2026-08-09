# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `incident-playbook-writer`
- Eval: `eval-001-docker-rollback`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a` from `agents/devops/test/incident-playbook-writer/evals/workspace/eval-001-docker-rollback`.
- Fixture SHA-256: `f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a`
- Prompt SHA-256: `f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `500941dffb48347901d3283054321002e2a4be37cb509882170d999b6f27485f`
- Skill overlay SHA-256: `8bcf98d79219616ab4a2e4bf38f41850dabf91363c7e81c3766a5503c4452405`
- Judge schema SHA-256: `82478d5bfcdfccbe67817c9bfae394096b57b2c317a4413eadf1808b946de6d0`
- Eval definition SHA-256: `ef78ea6924e16ad4c29c668948468977eb007b3ff9fb4e26733caf7d332c338d`
- Metadata SHA-256: `aaf6d95692337cdac99edc2200f96e32a7dbdc444f3865d1a29464638703fbd4`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_evidence_based_rollback` | PASS | Locked deploy/ROLLBACK.md selects the last known healthy immutable SemVer tag from the release record, changes APP_IMAGE_TAG, pulls and recreates app with the repository Compose file, then checks status, logs, and /health. |
| `creates_scoped_incident_response` | PASS | Locked deploy/INCIDENT_RESPONSE.md specifies P1/15-minute and P2/30-minute response, #ops-incidents, incident commander and service owner roles, investigation, recovery, and post-recovery checks. |
| `avoids_unsupported_procedures` | PASS | The locked documents explicitly exclude database migration rollback, floating or guessed tags, unsupported runtime changes, and destructive actions; git evidence shows no rollback execution or commits. |
| `omits_unrequested_playbooks` | PASS | Locked git status shows only deploy/ROLLBACK.md and deploy/INCIDENT_RESPONSE.md as new files; no troubleshooting or on-call playbooks were delivered. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=e731b4de4056836c4162933fc7988c67f038676cd0997278848a8b0e9b96c7e8; snapshot_sha256=06810d04a9a51339888e42bc042341dd8319dac6ac33e7ab1f7ad1e51aa78190
- Behavior: Delivered both requested evidence-grounded Docker Compose handbooks with explicit operational boundaries and verification steps.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=18d38285572cda2a473a79904f01f995f4b6132457312dc446ee505aa91bac2b; snapshot_sha256=943403b7824dda0ddcf2a921c39a770b196b90ba77a07eec0e47fa0ba250ee25
- Behavior: Also delivered the two requested handbooks, serving as a comparison baseline; its behavior does not alter the with_skill verdicts.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
