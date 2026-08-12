# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-009-missing-handoff-target-unavailable`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-9-missing-handoff-target-unavailable`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `5230fc275f473a55b5d59c172358aff82cf42415f36da1a920c1b4fa1e1e3cc1`
- Repository HEAD: `715bd6b76fcd6f14f475aeabe141543063d431ba`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `be11ec63823b148323fef6c35d27c0861bd093b24d683f705e846234e98b7baa`
- Skill overlay SHA-256: `961e7aacbdec2d154ad578bc7bf54d5d734f34031af1384fb20aa67a8e2d392a`
- Judge schema SHA-256: `45aa95828b353344675a6e62421acac466500932a42ce4d64f8f43969bd5bb6d`
- Eval definition SHA-256: `ea4ff3ed92cd6df9743d23b747dc29d9087560d5cfa7f5f4525b8e146b0b7e97`
- Metadata SHA-256: `f52777a03f0c132438bf125e153205560b01f6abb53fcb15add6a3552b96312b`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detect_missing_target` | PASS | With-skill output explicitly states that `designer-agent` is not installed and design capability is unavailable. |
| `mark_handoff_blocked` | PASS | With-skill routing sets `entry_basis: blocked`, lists the unavailable capability, and states that `designer-agent` must be installed. |
| `do_not_perform_missing_role` | PASS | With-skill output preserves PM classification and blocked handoff only; no design artifact or visual specification was delivered. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5230fc275f473a55b5d59c172358aff82cf42415f36da1a920c1b4fa1e1e3cc1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b8996b5dae0fb073e4d395ac26bc8599f20db997c392874de6a8316298c1c02d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly detects the unavailable designer-agent, marks the handoff blocked, identifies installation as the required next step, and does not perform Designer work.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5230fc275f473a55b5d59c172358aff82cf42415f36da1a920c1b4fa1e1e3cc1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=08ee042f682981fa76a827f06ca187dd34fd2da353ecc61906efd56dc501b18e; snapshot_sha256=3e5d261135862c81a81f5c6da62cbe44145317d3dd6ad02007ab85a16defb312
- Behavior: Produced a design handoff document without identifying the unavailable designer-agent or blocking the handoff, illustrating the fresh baseline failure.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
