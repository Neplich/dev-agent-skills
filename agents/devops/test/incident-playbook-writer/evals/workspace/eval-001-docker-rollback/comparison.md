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
- target_skill_sha256: `dcee4cc39c2fa28ea4046f8b10ceca0528d9458efc81ffb2c28e21e284fe034f`
- eval_definition_sha256: `ef78ea6924e16ad4c29c668948468977eb007b3ff9fb4e26733caf7d332c338d`
- metadata_sha256: `fe85f6eb6336802a8ad0f9268aaeda74d6a32f5dafcd0a67b8753f30859c10b1`
- fixture_sha256: `f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `82478d5bfcdfccbe67817c9bfae394096b57b2c317a4413eadf1808b946de6d0`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `5d95ff5039100f2131c72122b091ff4a172f65d45070290345e8a658862159d4`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `creates_evidence_based_rollback` | PASS | Locked deploy/ROLLBACK.md uses a release-record known-healthy immutable SemVer tag, sets APP_IMAGE_TAG, runs compose pull and up -d for app, then checks ps, logs, and /health. |
| `creates_scoped_incident_response` | PASS | Locked deploy/INCIDENT_RESPONSE.md specifies P1/P2 response targets, #ops-incidents, incident commander and service owner roles, investigation evidence collection, restoration, and closeout checks. |
| `avoids_unsupported_procedures` | PASS | The delivered manuals explicitly exclude database migration rollback and unsupported operations; raw trace shows no executed rollback or deployment command. |
| `omits_unrequested_playbooks` | PASS | The with_skill delivery snapshot and git status contain only deploy/ROLLBACK.md and deploy/INCIDENT_RESPONSE.md; no troubleshooting or on-call playbook was created. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=ad57d84222b20be985d8333050da2af7d5ad0cbafe1672ed3e09fd35de499283; snapshot_sha256=dc9eddb4825642f9738002d6a920fac6ae524c655b7d705b6031c4455b7b3d33
- Behavior: Delivered both requested evidence-backed manuals, scoped to the confirmed Docker Compose app surface, without executing rollback.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f9cbfa543cb8f8fa6c3d3f1e68b0eaa1e627427917cfa9b9970e909922356673; fixture_sha256=f3b605dee7b400a16cee380181367beb6aef0898c3081a8e6f89abd9e2c19e1a; output_sha256=4bdb32ca27d5ebd53306ac21c83509d4964d9ddb476bb4747c2ef326de46c563; snapshot_sha256=3113709fe1afdbaf7fe25888dd5e14520e3b0996902e51cf11b59dd1b9e2d29e
- Behavior: Also delivered the two requested manuals and avoided unrequested playbooks and rollback execution; broadly similar baseline behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
