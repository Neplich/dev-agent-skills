# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-013-implementation-plan-archive-allows-next-plan`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a2e9a2b8540bac00a2c1db6bdbe2b7cdb6e2f9b82d0dc379a0a59bc67493a95d` from `agents/engineer/test/feature-implementor/evals/workspace/eval-013-implementation-plan-archive-allows-next-plan`.
- Fixture SHA-256: `a2e9a2b8540bac00a2c1db6bdbe2b7cdb6e2f9b82d0dc379a0a59bc67493a95d`
- Prompt SHA-256: `3c8299acb745a32d6489aea810b147bccfe598f9a45f0fae92dc371d5a8af8dc`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1b3ba014c732559fe2d85e84b85c8db967bb14f4b1fc850a2267e7d4ee1cf03b`
- Skill overlay SHA-256: `7f72b0d2378eefdc164735f00c26c14522753a42e538abe02ba7accda3b0a9f5`
- Judge schema SHA-256: `92c95ee84208d5ddf7a774382e98fb939786b7da025643fcac881491d89921d5`
- Eval definition SHA-256: `a98513966bafb1dd16a4ceba24c6976614cbbf88be3adce960d3d42a72b0948c`
- Metadata SHA-256: `20785706c746be6895ed31fc2345f379cd37d1db1f0bd95d72fc9387f408aa95`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_prior_plan_archived` | PASS | With-skill output states the full-refund plan is archived and the delivered plan frontmatter points to the exact archive path; it also records no active-plan blocker. |
| `allows_new_active_plan` | PASS | The delivered file is `docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md`, and the output provides its path. |
| `records_previous_plan_archive` | PASS | The delivered file frontmatter contains `previous_plan_archive` with the exact required archive path. |
| `keeps_active_entry_fixed` | PASS | The active plan was delivered at the required `IMPLEMENTATION_PLAN.md` path, outside the archive directory. |
| `waits_for_user_confirmation` | PASS | The output explicitly requests confirmation before coding; git evidence shows only the new plan file was added and no code changes occurred. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3c8299acb745a32d6489aea810b147bccfe598f9a45f0fae92dc371d5a8af8dc; fixture_sha256=a2e9a2b8540bac00a2c1db6bdbe2b7cdb6e2f9b82d0dc379a0a59bc67493a95d; output_sha256=19b4e7cb4eb9ddd375a5671cedee4daa84e96a4913efbcffcf3bd94068b04aef; snapshot_sha256=ec3158465f1f87ca7eb9612e9c0eab6f23f08682d6f665671cd3edffa723c8f4
- Behavior: Created the proposed partial-refund implementation plan, recorded the prior archive reference, made no code changes, and gated implementation on maintainer confirmation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3c8299acb745a32d6489aea810b147bccfe598f9a45f0fae92dc371d5a8af8dc; fixture_sha256=a2e9a2b8540bac00a2c1db6bdbe2b7cdb6e2f9b82d0dc379a0a59bc67493a95d; output_sha256=d31429e14b657d84100631b433c59118942275444507048710b6e6b3c2d91178; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Recognized the archived full-refund context and absence of an active plan, but did not create or propose the required active partial-refund plan or confirmation gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
