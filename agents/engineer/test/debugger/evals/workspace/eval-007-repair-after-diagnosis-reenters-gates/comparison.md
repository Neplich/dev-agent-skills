# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-007-repair-after-diagnosis-reenters-gates`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `80eecca81db5b48ef73374c03765192f3e14ba18339bc165760fe445d84e1dd9` from `agents/engineer/test/debugger/evals/workspace/eval-007-repair-after-diagnosis-reenters-gates`.
- Identity schema: `2`
- target_skill_sha256: `3f5fc52f5119888b420cf0815200bcffd4eec82b0638977ef69f000383c62d4a`
- eval_definition_sha256: `cdefa12a92ecb2beee7369f1d92f05bc587cd3aef8373c00d4358a500c3356d3`
- metadata_sha256: `59ea0e1c9cd38f15c9d35a377b87f90fc618ab8c609e85366f509054f3971a8b`
- fixture_sha256: `80eecca81db5b48ef73374c03765192f3e14ba18339bc165760fe445d84e1dd9`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `2d0d2df478964bd20584fbf2d57270fb046340d3fbfa14b7bcbeaa75eba39af4`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `b1efa4ccc5e8229c27460fcde3c036e13caad4098dac3db8bfef42b6ee6792c0`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `05db5d59515a04b12b590113c0f1e4b380c2726c0fb5b5aaa6e7524f0d28fe70`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `exits_diagnosis_only_mode` | PASS | With-skill output states this is a new repair entry and that the diagnosis report cannot authorize repair; it does not treat diagnosis_only or allowed_mutations:none as modification authorization. |
| `reenters_pm_engineer_repair_gate` | PASS | With-skill output routes through PM alignment via idea-to-spec, then Engineer TRD completion, and requires a confirmed engineering handoff before repair planning. |
| `classifies_missing_docs` | PASS | With-skill output explicitly classifies the case as missing_docs, identifies absent PRD/TRD/decision records, and says it cannot confirm implementation_deviation. |
| `does_not_plan_or_fix` | PASS | With-skill output refuses repair planning and modification; locked git evidence is clean, delivery_snapshot is empty, and the trace shows only read-only inspection commands. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b1efa4ccc5e8229c27460fcde3c036e13caad4098dac3db8bfef42b6ee6792c0; fixture_sha256=80eecca81db5b48ef73374c03765192f3e14ba18339bc165760fe445d84e1dd9; output_sha256=9d33124d479fb9511f79dd5d857f592c8547d67946c07b2a95ca26c67a08e43c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly exits diagnosis-only handling, re-enters PM/Engineer repair gates, classifies missing documentation, and makes no repair or mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b1efa4ccc5e8229c27460fcde3c036e13caad4098dac3db8bfef42b6ee6792c0; fixture_sha256=80eecca81db5b48ef73374c03765192f3e14ba18339bc165760fe445d84e1dd9; output_sha256=eef75c7de06a1d6d4639f785ff6b4e87f374589a4d195ace6781054c667cb89e; snapshot_sha256=be34e6f71d65bb2a2d276f0457e569d07db6a9de6ba3540913ef621d5e43af2e
- Behavior: Fresh baseline incorrectly treats the diagnosis as sufficient authorization, implements a schema change, and leaves src/session-store.ts modified.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
