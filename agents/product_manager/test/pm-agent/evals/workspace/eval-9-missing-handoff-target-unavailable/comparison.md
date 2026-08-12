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
- Repository HEAD: `8813f864e743f7c83dc2e51e0b5add79f312e870`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0616a11ea39f978cac34906ca01c79a336316825183bb1897d900f056d8544f7`
- Skill overlay SHA-256: `4d4a580c5e7c36b9199abb80221829f90c900c96463581d7f87c6d7ccc538bd7`
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
| `detect_missing_target` | PASS | With_skill explicitly states that designer-agent or an equivalent design capability is unavailable. |
| `mark_handoff_blocked` | PASS | With_skill explicitly marks the handoff as blocked and requests installing or enabling designer-agent. |
| `do_not_perform_missing_role` | PASS | With_skill performs no design production; it keeps PM routing and states the execution boundary forbids substituting for Designer. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5230fc275f473a55b5d59c172358aff82cf42415f36da1a920c1b4fa1e1e3cc1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=bc563a308901ee513841e5193a3a1da7a5dbcf3fe077e8a724f5efb209491abd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the missing designer-agent capability, marks the handoff blocked, specifies the required enablement, and does not perform the missing design role.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5230fc275f473a55b5d59c172358aff82cf42415f36da1a920c1b4fa1e1e3cc1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f7ac53dcadcd6ca378adfe6923d6522cfaff58eb368615becaa983d793b1ae51; snapshot_sha256=eb74465208301e13b4e07b6b8b1acde0642e25d2d46d7a37f59400e1ce2e40f7
- Behavior: Fresh baseline creates a generic design handoff template but does not identify the unavailable designer-agent or explicitly mark the handoff blocked.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Install or enable designer-agent before continuing the formal design handoff.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
