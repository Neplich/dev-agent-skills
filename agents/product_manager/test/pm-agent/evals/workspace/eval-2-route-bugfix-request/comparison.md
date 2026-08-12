# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-002-route-bugfix-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-2-route-bugfix-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `3622b3dfdb9bef50766ff22e70a5639483865b84fa39f8a64f027bc492debda1`
- Repository HEAD: `715bd6b76fcd6f14f475aeabe141543063d431ba`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `be11ec63823b148323fef6c35d27c0861bd093b24d683f705e846234e98b7baa`
- Skill overlay SHA-256: `961e7aacbdec2d154ad578bc7bf54d5d734f34031af1384fb20aa67a8e2d392a`
- Judge schema SHA-256: `00a01c5f9432a18e723abe9a7b1a555e5a2a41dc2c36a101ed91497434d1c7f4`
- Eval definition SHA-256: `fe6d213ce4edb254dae39c5fefca87002824c8356e6ca05dfa6b8b92c57d378d`
- Metadata SHA-256: `163386e80d321ea48ddfd244853e278bc70ea13a08cdc68ac01f85bf3ba7240f`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_bug_report` | PASS | With-skill output explicitly classifies the request as `request_type: bug_report`. |
| `expectation_first` | PASS | With-skill output routes to PM/idea-to-spec, requires comparison with approved expectations, and asks for the expected token-expiry behavior before repair; no approved PRD/TRD or equivalent evidence is available in the fixture, so the confirmation step is only partially exercised. |
| `debugger_handoff_after_confirmation` | NOT_EXERCISED | The output explicitly requires confirmation before generating an Engineer debugging package and does not hand off yet; confirmation is unavailable, so this later assertion is not exercised. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3622b3dfdb9bef50766ff22e70a5639483865b84fa39f8a64f027bc492debda1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=3a358f898be11bdc7d82d403429bec68a9657dcde0dd06f222e33cf681bc5b09; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified the report, routed it through PM expectation-first discovery, and stopped before implementation or debugger handoff pending confirmation and missing evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3622b3dfdb9bef50766ff22e70a5639483865b84fa39f8a64f027bc492debda1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=1efc8e96a59aab20b6a74d23021e4801b0a07a81f5926960222bccf955cd1370; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reported the empty repository and requested source, but did not classify the request or establish an expectation-first handoff gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the application source, approved expected behavior, and relevant logs; then confirm the implementation deviation before Engineer/debugger handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
