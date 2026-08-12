# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-001-route-greenfield-product-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-1-route-greenfield-product-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81`
- Repository HEAD: `33a503192c752d6227de1bc0d8d8a2e78e31cdf5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8b87fb93cdb85ecb0436a61b1aedfcf9c8b41c4cd8f9eff41c412a3196c1d245`
- Skill overlay SHA-256: `56390e18f057b654978938889dac7daf0263eaaf39d741419b573d12bff2c198`
- Judge schema SHA-256: `8e99b873e976898a8a9714405f69dce2d81e6c553f7d4c2b0a99b8b832eee831`
- Eval definition SHA-256: `4e776e14ac2c8d3f3aa33718b92238355ee2d15eab3267a50cdada6bb3d4a1de`
- Metadata SHA-256: `98a5616a9f22e4ba7d6ed10c98a36b572ccd9f5c0bfcfaf868ea982ef672635f`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `route_to_idea_to_spec` | PASS | With-skill output explicitly selects `pm-agent:idea-to-spec`, identifies `greenfield-discovery`, and keeps the request in product discovery. |
| `pm_first_guardrail` | PASS | With-skill output identifies `project_status: empty`, requires confirmation, and explicitly limits execution to product discovery without code or technical implementation. |
| `context_to_collect` | PASS | With-skill output asks one high-information question about the target user and problem, with three concrete options and trade-offs. |
| `expected_pm_artifacts` | NOT_EXERCISED | The with-skill output is still awaiting the first discovery answer; `delivery_snapshot` is empty and no PM completion or handoff is claimed. |
| `handoff_boundary` | NOT_EXERCISED | No handoff occurs; the output remains at the first discovery question and explicitly keeps engineering work for a later stage. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c9c45e64d7e4422194457bf56a20500614625df851c86017274dd60b66664a80; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the empty-directory idea into PM greenfield discovery, asks the next product question, and avoids implementation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=2b4af7db6f65fef950a714543984faac797cbd3b88ad4ae2c0e046fe474322a5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a plausible MVP proposal and several implementation-oriented questions, but lacks explicit PM routing and focused first-step discovery control.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Obtain the user's answer to the target-user/core-problem question before producing PRD/DECISIONS or considering handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
