# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-007-direct-downstream-without-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-7-direct-downstream-without-handoff`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f`
- Repository HEAD: `715bd6b76fcd6f14f475aeabe141543063d431ba`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `be11ec63823b148323fef6c35d27c0861bd093b24d683f705e846234e98b7baa`
- Skill overlay SHA-256: `961e7aacbdec2d154ad578bc7bf54d5d734f34031af1384fb20aa67a8e2d392a`
- Judge schema SHA-256: `6f1f540339fe5c4c310ca6aaedc38adff3d61e4268399a40149f44e3770ac25c`
- Eval definition SHA-256: `13771c6d0b126a3ca1ee1723ee43dcbca8cef0bbfd3ed1a8c42651bbd42a7c19`
- Metadata SHA-256: `70b36659756bbd4d7fc0e09d0fabc7ee5ba1a168323c148fa735110fb59ec768`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routing_decision_present` | PASS | With_skill output provides a routing decision with request type, selected_owner `idea-to-spec`, entry_basis, feature_path, source documents, and execution boundary. |
| `stay_in_pm_alignment` | PASS | With_skill keeps the work in the PM/idea-to-spec path, marks the entry blocked, and explicitly says no downstream execution or Engineer handoff has occurred. |
| `blocks_engineering_without_basis` | PASS | With_skill identifies missing product/design basis, unresolved scope and acceptance criteria, missing implementation context, requires confirmation, and states that code modification is not allowed; locked git evidence shows no changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=999d14f336cf0f8d7653d1b8918c08b1970186af864a746479880406ea6081fb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routed the request to PM scope alignment, blocked downstream implementation, and preserved the read-only boundary.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a61e159bfab77c22fcaf14b3184217c41205fa0610d3753eab9bab9cd0b737ae; snapshot_sha256=64c2d9a61ca4f7c80ec2811854a5fa9eed4bbdb28f39cfa28c6b781afe741f6d
- Behavior: Implemented a new settings page despite missing product/design basis and created untracked files.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
