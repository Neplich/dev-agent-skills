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
- Repository HEAD: `715bd6b76fcd6f14f475aeabe141543063d431ba`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `be11ec63823b148323fef6c35d27c0861bd093b24d683f705e846234e98b7baa`
- Skill overlay SHA-256: `961e7aacbdec2d154ad578bc7bf54d5d734f34031af1384fb20aa67a8e2d392a`
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
| `route_to_idea_to_spec` | PASS | With-skill output explicitly selects `idea-to-spec`, identifies `greenfield-discovery`, and keeps responsibility in product discovery without engineering execution. |
| `pm_first_guardrail` | PASS | With-skill output identifies an empty project, marks scope and tech stack pending, requires confirmation, and states it will not write formal documents or enter implementation yet; git evidence shows no changes. |
| `context_to_collect` | PASS | With-skill output asks the highest-information first discovery question about the primary target user and requests a reply before proceeding. |
| `expected_pm_artifacts` | NOT_EXERCISED | The output is explicitly waiting for the user's answer and marks PRD/DECISIONS as pending, so this assertion is not yet exercised. |
| `handoff_boundary` | NOT_EXERCISED | Only the initial discovery question has been asked; no handoff has occurred. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=480b3b908106630afa0e4b5974a4e658dd73b0d6673437bca3a05996c5bb5359; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the empty-directory product idea through PM-first greenfield discovery, asks one focused user question, and makes no workspace changes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=acfb6edf3aff0b94988c5e9a7ff435967801458a79c851afd902400163536b81; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=781017dc3e41abb4cb634c447ef9c29c72f8b34562c60ebd76ea10248c454a70; snapshot_sha256=7034f2b3505bf6f75c216e16b6213a311413e969cb9e2bdc1367dfdce06a93fe
- Behavior: Fresh baseline produced a PRODUCT_BRIEF and proposed defaults before user discovery was resolved, while still avoiding code and asking several follow-up questions.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Wait for the user's target-user answer, then produce the PM PRD and decision record before any handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
