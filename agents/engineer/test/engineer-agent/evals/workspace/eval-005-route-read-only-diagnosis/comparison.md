# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-005-route-read-only-diagnosis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `e469c8867c3eaab395b1e2ecf769900426fc05c37fc44889d5555593c06bb9a0` from `agents/engineer/test/engineer-agent/evals/workspace/eval-005-route-read-only-diagnosis`.
- Identity schema: `2`
- target_skill_sha256: `567599e3469192896a31cdff4fe4fd18d5213c866e89288582d2212d150b33af`
- eval_definition_sha256: `ef789eef7ae75d20cd2b4f7363ad1491d04eb3cdb6114859d0ec16b9b00b6acb`
- metadata_sha256: `48a05f29fee0a106e78e2786488d2a57e30800d3511c0e6a27dab7a0cee8b2d5`
- fixture_sha256: `e469c8867c3eaab395b1e2ecf769900426fc05c37fc44889d5555593c06bb9a0`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `50ba2d2012c41a93dc7606cfb865565f1a5b791f485b360a632d9cb7b9413bac`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `6501dca073ea693c3fce773a64fba0b68444a0b5dc8e1f9f199b652d00d7a920`
- Repository HEAD: `2ac10136f4ed18048058361915e66c52b4e038c5`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `e0e827b7bd294609981357aae7bd81aabdea2aff56e900333dafe8d646c2d3e3`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_read_only_fields` | PASS | With-skill output explicitly preserves `mode: diagnosis_only` and `allowed_mutations: none`, and reports no workspace modifications. |
| `routes_to_existing_debugger` | PASS | With-skill output names `engineer-agent` as owner and selects `engineer-agent:debugger` as the specialist route; no parallel diagnosis specialist is proposed. |
| `does_not_require_repair_docs_first` | PASS | With-skill output states PRD/TRD are unavailable, does not confirm implementation deviation, repair, status changes, or mutation, and proceeds with the read-only diagnosis boundary. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6501dca073ea693c3fce773a64fba0b68444a0b5dc8e1f9f199b652d00d7a920; fixture_sha256=e469c8867c3eaab395b1e2ecf769900426fc05c37fc44889d5555593c06bb9a0; output_sha256=b77300fbf208c864b811adacd565a8a24e29175f8fc506b1303f8e1e115c52c9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Preserves the read-only diagnosis boundary, routes through engineer-agent to debugger, and treats missing PRD/TRD as an alignment limitation rather than a repair prerequisite.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6501dca073ea693c3fce773a64fba0b68444a0b5dc8e1f9f199b652d00d7a920; fixture_sha256=e469c8867c3eaab395b1e2ecf769900426fc05c37fc44889d5555593c06bb9a0; output_sha256=5577e409c388488eb7ddbf2a0ed2bca440ac649152170f76e4ca117e0820bf4f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a cautious read-only investigation summary and avoids mutation, but does not explicitly route through engineer-agent to the existing debugger or preserve the required routing fields.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
