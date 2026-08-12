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
- Identity schema: `2`
- target_skill_sha256: `500941dffb48347901d3283054321002e2a4be37cb509882170d999b6f27485f`
- eval_definition_sha256: `ef78ea6924e16ad4c29c668948468977eb007b3ff9fb4e26733caf7d332c338d`
- metadata_sha256: `aaf6d95692337cdac99edc2200f96e32a7dbdc444f3865d1a29464638703fbd4`
- fixture_sha256: `f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `82478d5bfcdfccbe67817c9bfae394096b57b2c317a4413eadf1808b946de6d0`
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
| `creates_evidence_based_rollback` | PASS | Locked deploy/ROLLBACK.md uses the Docker Compose file, release-record last-known-good immutable SemVer tag, APP_IMAGE_TAG, pull/up -d app, and post-checks for status, logs, and /health. |
| `creates_scoped_incident_response` | PASS | Locked deploy/INCIDENT_RESPONSE.md covers P1/P2 response times, #ops-incidents, incident commander and service owner, investigation, recovery, validation, and closure/post-recovery checks. |
| `avoids_unsupported_procedures` | PASS | The locked rollback document explicitly excludes database migration rollback and unsupported deployment methods; raw command events show inspection/static checks and no executed docker rollback command. |
| `omits_unrequested_playbooks` | PASS | Locked git status and delivery snapshots contain only deploy/ROLLBACK.md and deploy/INCIDENT_RESPONSE.md; neither TROUBLESHOOTING.md nor ON_CALL.md was delivered. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=8894bf2357286174c0ba23d8a9341e88c38f756d5899e18afc278dacb0f770e3; snapshot_sha256=96dc1f58a9fd14d33e1dc3587efb58cf0f4558b0aef633829f750e1846d49cf1
- Behavior: Delivered both requested evidence-based operational manuals with scoped procedures and no observed rollback execution.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=d2de1f49f2cfff688c2a75a1170e804e96ee65aab527178129a598c4eb447526; snapshot_sha256=f3f0d128cb5111430a85d25f75389e3dce47f39c334be7863819700edc5d1e39
- Behavior: Fresh baseline also delivered both requested manuals and broadly satisfied the requested behavior; comparison context only.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
