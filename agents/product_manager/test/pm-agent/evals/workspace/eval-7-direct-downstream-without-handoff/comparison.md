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
- Repository HEAD: `d96f213470acb77cb92c1af637626260d3e55b45`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c978d115fb1b50ceb3f80a0d77c450574e05667bd8252ef5b6e8b67105206fa2`
- Skill overlay SHA-256: `5b89d6a3c235a107cde8314b908b32dbfa76d6dc330906b48f74091d88e9019d`
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
| `routing_decision_present` | PASS | The with_skill output begins with “Routing decision” and explicitly includes request_type, selected_owner, entry_basis, feature_path, and execution_boundary. |
| `stay_in_pm_alignment` | PASS | It routes to “pm-agent:idea-to-spec,” marks feature_path unresolved, requires confirmation, and states that no downstream handoff or implementation can proceed. |
| `blocks_engineering_without_basis` | PASS | It identifies missing product/design materials and implementation context, requests scope/target-layout evidence, and states “暂不修改代码” and “无法安全开始代码实现”; git evidence confirms no changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=741ce3121e7909ecaf0348622f37e3318ce904828f3651d082c0a247fa12a218; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the request into PM idea-to-spec, keeps it out of downstream execution, and blocks code changes pending product, design, and implementation basis.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=0091bde13c97215d2b8cc0b1efb476d27acfe5645bd6e01ba412690ef4c64f2c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline only reports the empty repository and asks for project files; it does not provide the required PM routing decision or scope-alignment protocol.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
