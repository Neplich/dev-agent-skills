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
- Identity schema: `2`
- target_skill_sha256: `6f8f132bc1f6eba3f9eb10727126ee30960b503351486b4fb6204e20571ffb35`
- eval_definition_sha256: `ea4ff3ed92cd6df9743d23b747dc29d9087560d5cfa7f5f4525b8e146b0b7e97`
- metadata_sha256: `f52777a03f0c132438bf125e153205560b01f6abb53fcb15add6a3552b96312b`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `45aa95828b353344675a6e62421acac466500932a42ce4d64f8f43969bd5bb6d`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `5230fc275f473a55b5d59c172358aff82cf42415f36da1a920c1b4fa1e1e3cc1`
- Repository HEAD: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `6c6b79d36b8b3a1bf132fd82bfece3cf6e7b256e3a9a58a0cdb78f4a09e26e69`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detect_missing_target` | PASS | With_skill output states current design capability is missing and specifically identifies that `designer-agent` is absent. |
| `mark_handoff_blocked` | PASS | With_skill output sets `entry_basis: blocked`, states the design entry gate did not pass, and requests installing/enabling `designer-agent`. |
| `do_not_perform_missing_role` | PASS | With_skill delivery_snapshot is empty; the output explicitly limits work to handoff information and prohibits replacing Designer work. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5230fc275f473a55b5d59c172358aff82cf42415f36da1a920c1b4fa1e1e3cc1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=2422833170388b6044416167ed0fe5f7130ff37d1a9c4e451035d59fb2e51163; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identified the unavailable designer-agent, marked the handoff blocked, named the required capability, and preserved the Designer role boundary without producing design deliverables.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5230fc275f473a55b5d59c172358aff82cf42415f36da1a920c1b4fa1e1e3cc1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=ba0acd0d773bdc275a1fabe7983ed779644e23e0aaa1031a3002ecbf28138be5; snapshot_sha256=0786e2f7d7f4bcee5d626f9c3f9e035f19e39cbff8ba02f08d765abe5e93b267
- Behavior: Created a generic design handoff template because the workspace appeared empty, but did not identify designer-agent as unavailable or mark the handoff blocked.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
