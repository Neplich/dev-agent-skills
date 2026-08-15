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
- target_skill_sha256: `dbf68937d134aca2f40875673b0fd0b744ad9837ea79e85af0826e2a587f5231`
- eval_definition_sha256: `ef789eef7ae75d20cd2b4f7363ad1491d04eb3cdb6114859d0ec16b9b00b6acb`
- metadata_sha256: `e4901c042b0409a9250648c22e35f5aa91c71bf1facf120010b04e53329e73e7`
- fixture_sha256: `e469c8867c3eaab395b1e2ecf769900426fc05c37fc44889d5555593c06bb9a0`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `50ba2d2012c41a93dc7606cfb865565f1a5b791f485b360a632d9cb7b9413bac`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `6501dca073ea693c3fce773a64fba0b68444a0b5dc8e1f9f199b652d00d7a920`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `dc4e9a8a891ad08c98ae67c1fa935de8b5c54b55c6249a46d7cf05f06bdbed91`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_read_only_fields` | PASS | With-skill output explicitly retains `diagnosis_only` and `allowed_mutations: none`, and states a zero-mutation boundary. |
| `routes_to_existing_debugger` | PASS | With-skill output routes the work to `debugger`; the captured engineer-agent routing material identifies debugger as the read-only diagnosis specialist, with no parallel specialist proposed. |
| `does_not_require_repair_docs_first` | PASS | With-skill output marks expectations `unaligned` due to missing PRD/TRD, preserves evidence collection, and explicitly disallows confirming implementation deviation or creating a repair plan. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6501dca073ea693c3fce773a64fba0b68444a0b5dc8e1f9f199b652d00d7a920; fixture_sha256=e469c8867c3eaab395b1e2ecf769900426fc05c37fc44889d5555593c06bb9a0; output_sha256=c95220b1c5153d7a6d4dc3f873bca1528cf7e167ab5983244c1e29bd85e49328; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Read-only diagnosis was routed to the existing debugger, preserved the handoff constraints, and treated missing PRD/TRD as unaligned without blocking evidence collection or initiating repair.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6501dca073ea693c3fce773a64fba0b68444a0b5dc8e1f9f199b652d00d7a920; fixture_sha256=e469c8867c3eaab395b1e2ecf769900426fc05c37fc44889d5555593c06bb9a0; output_sha256=6cab3c954041912db27929a178bd3da41d1d9226001a7379d55c459ed7fef2ee; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline preserved the no-change intent and reported available incident evidence, but did not explicitly preserve the required fields, route to debugger, or mark the missing-document state as unaligned.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
