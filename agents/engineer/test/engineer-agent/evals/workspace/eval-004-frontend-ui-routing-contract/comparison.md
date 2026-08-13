# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-004-frontend-ui-routing-contract`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ec60268c3cba621e7690e34a6ae14bc9ac52429e90275b6d4c2fdedef202a8df` from `agents/engineer/test/engineer-agent/evals/workspace/eval-004-frontend-ui-routing-contract`.
- Identity schema: `2`
- target_skill_sha256: `4bbafb4fd1b263bfdfde7c9e30fb901fcf24822b1fff3e0e99c5d830d36c45cc`
- eval_definition_sha256: `fd025b1cc76de7ba27bf5663c5ab9fb0198c4654dd23e4362935403d06d0381e`
- metadata_sha256: `4906971d417635b5c425ac490e57080c03cc4473b36cee23eaff89fa06fe26b0`
- fixture_sha256: `ec60268c3cba621e7690e34a6ae14bc9ac52429e90275b6d4c2fdedef202a8df`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `e2168c580c03f1c43acee8d4077b4a9553410b224e0542721c19d2cc8e09e39c`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `c7cb9273b0ca01f312d499d16a87d54a68980710efc17abee5e6a4600012b8c0`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `93852e7b81da4b65a2f6e7e6b552fb8fc2585f12fb1990e01ea0c8684431a23e`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_frontend_update_to_engineer` | PASS | With-skill output classifies the change as a frontend UI update, preserves Engineer ownership, and routes `designer-agent` → `engineer-agent`; the trace also records the engineer routing decision. |
| `does_not_route_to_external_ui_skill` | PASS | Neither the with-skill output nor its locked trace recommends or invokes `ui-ux-pro-max`; it uses the internal `designer-agent` and Engineer flow. |
| `runs_feature_alignment` | PASS | The output states `feature_path: customer-portal/profile-settings` and an approved PRD/TRD basis. The trace shows both specified documents were read before the routing decision. |
| `checks_design_deliverables` | PASS | The output explicitly checks and reports both design deliverables as missing: `ui-ux-spec.md` and `visual-system.md`. |
| `hands_design_gap_to_designer` | PASS | The output hands the missing design work to `designer-agent` and specifies page hierarchy, grouping, primary-button states, and visual rules as the required scope. |
| `routes_implementation_after_design` | PASS | The output explicitly routes back to `engineer-agent` and `feature-implementor` after design confirmation, requiring TRD alignment and confirmed `IMPLEMENTATION_PLAN.md` before implementation. |
| `does_not_execute_directly` | PASS | The output says this round does not modify code. Locked git evidence shows unchanged HEAD, branch, status, index, worktree, and no delivery snapshot; the trace contains read-only inspection commands and no tests or plan creation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c7cb9273b0ca01f312d499d16a87d54a68980710efc17abee5e6a4600012b8c0; fixture_sha256=ec60268c3cba621e7690e34a6ae14bc9ac52429e90275b6d4c2fdedef202a8df; output_sha256=28fc887633b6be85c49dee969fe8c8c9a9c2c911dabaaada8f17d9ca0ca75b68; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly routes the frontend UI change through Engineer, performs PRD/TRD and design-deliverable alignment, hands the design gap to Designer, preserves the post-design implementation gate, and remains read-only.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c7cb9273b0ca01f312d499d16a87d54a68980710efc17abee5e6a4600012b8c0; fixture_sha256=ec60268c3cba621e7690e34a6ae14bc9ac52429e90275b6d4c2fdedef202a8df; output_sha256=d7e4c31cc4c250c2d8579896b9e813f4bdc2e7474d770ca781b38ef3ea3a1aa6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline gives a generic planning response and preserves the clean workspace, but does not establish the required Engineer routing, feature alignment, design-gap handoff, or gated workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
