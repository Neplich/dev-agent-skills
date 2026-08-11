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
- Repository HEAD: `ae451ca624c3dfd1bb8d530c3b416d40910caf82`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `619bfdcdc189ae85f09016655828cc88fc4d95591087522dac73338147eaad17`
- Skill overlay SHA-256: `d250e0c694804c4780185b995ee5f122601fe31dbd177a9a2a0571aa28ed8dec`
- Judge schema SHA-256: `6f1f540339fe5c4c310ca6aaedc38adff3d61e4268399a40149f44e3770ac25c`
- Eval definition SHA-256: `700336d4b7193b70e468b0c4438658b25a2ebad8ec77c1b4f8af7b856ebd1494`
- Metadata SHA-256: `70b36659756bbd4d7fc0e09d0fabc7ee5ba1a168323c148fa735110fb59ec768`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routing_decision_present` | PASS | The with_skill output explicitly presents a Routing decision containing request_type, selected_owner, entry_basis, feature_path, and execution_boundary. |
| `stay_in_pm_alignment` | PASS | The with_skill output keeps the work with pm-agent:idea-to-spec, marks feature_path unresolved, requires confirmation, and explicitly says no downstream engineering handoff or code modification has occurred. |
| `blocks_engineering_without_basis` | PASS | The with_skill output identifies missing product/design/current-page/acceptance context, states that engineering handoff is not yet justified, requires confirmation before generating implementation boundaries, and raw git evidence shows no code changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=360f361c775636a211fe725ce46aa69a9246db284379c6aae71a6c438117b90f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routed the request to PM, kept it in scope-alignment, identified missing product/design/implementation context, and avoided code changes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c7125b57c6e2197a316ce5751fed7de2350fc5c12d4d43ac0642e2ff0fbd5d2b; snapshot_sha256=953232cc053d1ab5e7622c6b16d72e667c381d7f21a751ce202358bc08e91216
- Behavior: Implemented a new settings-page prototype despite the missing product/design basis and created untracked files.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
