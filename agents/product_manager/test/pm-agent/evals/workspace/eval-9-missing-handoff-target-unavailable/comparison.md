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
- Repository HEAD: `d48403a0878a4efe20dfa8446b2f98657d804d37`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `74d69a1dabc5d0a63769f3255d309f6f5ee9ae4497e47a765a73111f6806fda7`
- Skill overlay SHA-256: `75f5799ddfa14cce5f07d58cae0c13a32be9d74a8c76053b724a7f014a523c6f`
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
| `detect_missing_target` | PASS | With-skill output explicitly states that designer-agent is not installed/provided and that no design agent is available. |
| `mark_handoff_blocked` | PASS | With-skill output marks entry_basis as blocked, lists designer-agent as unavailable, and instructs installing/enabling designer-agent. |
| `do_not_perform_missing_role` | PASS | With-skill output explicitly limits execution to PM handoff, prohibits producing formal design, and produces no design deliverable. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5230fc275f473a55b5d59c172358aff82cf42415f36da1a920c1b4fa1e1e3cc1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=6a79916dda1222e1e47dde5b8140ed70ade7732a843cb94b13d9ebeb4be63a84; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the unavailable designer-agent, marks the handoff blocked, specifies the required capability and missing documents, and preserves the Designer role boundary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5230fc275f473a55b5d59c172358aff82cf42415f36da1a920c1b4fa1e1e3cc1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f53adab23c77ef927722b7b73d396b840bb4fbbb75d52867366c26f74995ae17; snapshot_sha256=501f24f678f806be00b05113836930a7e2c9c3ee0dca6d3a0a07db44ebc0ed73
- Behavior: Created a generic design brief and noted unavailable project collaboration access, but did not identify designer-agent as unavailable or mark the handoff stage blocked.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
