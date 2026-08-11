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
- Repository HEAD: `5eed6bd61702fe0e1aa38eba2649b61fbdbcd5a6`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4e76801189b426dd33ce29ced16e549279e16d547ce6762d36863400f4354122`
- Skill overlay SHA-256: `77702f471e61dbfa60bd67a78323dc643acf1a23ee94c61de468a9d3da2ceccc`
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
| `routing_decision_present` | PASS | With-skill output begins with a Routing decision containing request_type, selected_owner, entry_basis, feature_path, and execution_boundary. |
| `stay_in_pm_alignment` | PASS | With-skill output routes to pm-agent:idea-to-spec, states that scope and basis are unresolved, requests confirmation, and explicitly prevents downstream execution. |
| `blocks_engineering_without_basis` | PASS | With-skill output identifies missing product/design materials, undefined target layout and acceptance criteria, unresolved implementation context, and an execution boundary forbidding code changes; git evidence confirms no mutation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=608154b5f8c80dc25b970b8dd568c44b9f90e6978be085cd70f2bbcdf1fc1ee0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the request to PM discovery, keeps execution blocked, and requests the missing scope and design basis.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=eed339cc38e0708d645de175cd909574e4ea8056403ba35aaf738427f6df41c4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reports the empty workspace and no mutation but omits the required PM routing and basis-gating behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
