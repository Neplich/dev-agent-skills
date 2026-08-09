# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-002-empty-qa-directory-expands-cases`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100` from `agents/qa/test/qa-agent/evals/workspace/eval-2-empty-qa-directory-expands-cases`.
- Fixture SHA-256: `870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100`
- Prompt SHA-256: `068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d70112827b0542d867a7689306d190b9c9a901f0d16faf502ff69330466e810c`
- Skill overlay SHA-256: `3673b22dfa628fadf9c4bb5597b7b2a2e950ec87dc67f02d57318ceb09cf90cb`
- Judge schema SHA-256: `d61853152f0f59bd847f0aa3394c1f282e4bb9275d56c9fb66462de58118346d`
- Eval definition SHA-256: `1252f49c3e393535dba5cc481c5c3100fe9a709aa3de1773196b4edb5900ada3`
- Metadata SHA-256: `bf12045623474ece32b13073fc8cb963c9b4f673ab0fe9f0cf0dc0ad649d4ef6`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With-skill output recognizes no executable QA cases and does not fall back to the legacy directory. |
| `assertion_2` | FAIL | The output passes the target directory, environment, source files, and selected specialist downstream, but explicitly returns blocked at the qa-agent gate. |
| `specialist_gate_pointer` | PASS | It selects spec-based-tester as the execution owner and states qa-agent will not execute directly, while passing the relevant context. |
| `assertion_6` | PASS | It selects one narrow route, spec-based-tester, without running multiple QA skills or expanding into implementation repair. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=77f53f79057977d0fccd55e14bed9df0d24b4a74a27a5b94f18831882f3365fe; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Selected spec-based-tester and identified the supplied QA context, but stopped with a blocked result.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=068467ca9228748a58aa1065f9a150e3f5b012d5ddc3cefa3e5b130984c9cc4a; fixture_sha256=870f233236f82c3cf594816a5771878c8e388e11eeb3846cf269bf436f0fb100; output_sha256=b907d2da1749f2a1beaae0c0d15e2d9148539967424df0971f1382f5d354c9f0; snapshot_sha256=e0fb63a7f356855fac72d9a0a511899838f76d7bfa05db92939fa8dcfd422793
- Behavior: Created a five-case QA suite and flow index, but performed the work directly without specialist routing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- assertion_2 is contradicted by the explicit blocked-at-entry-gate outcome, despite the required downstream context and specialist selection.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
