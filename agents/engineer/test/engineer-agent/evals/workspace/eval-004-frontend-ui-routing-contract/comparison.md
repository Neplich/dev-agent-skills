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
- target_skill_sha256: `4844b5e075259765184f2662312a91c5cdcb5ff00686044034ea15af2e50c5ac`
- eval_definition_sha256: `fd025b1cc76de7ba27bf5663c5ab9fb0198c4654dd23e4362935403d06d0381e`
- metadata_sha256: `5acb354c4f47f4e19cc0056b621672e97a9a1363620b5c47ee3aaa253b38e1da`
- fixture_sha256: `ec60268c3cba621e7690e34a6ae14bc9ac52429e90275b6d4c2fdedef202a8df`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `e2168c580c03f1c43acee8d4077b4a9553410b224e0542721c19d2cc8e09e39c`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `c7cb9273b0ca01f312d499d16a87d54a68980710efc17abee5e6a4600012b8c0`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `9edb63200b93f23958ca16aced6e6863b40fef177b2732db6ffeeb96c8c0a359`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_frontend_update_to_engineer` | FAIL | With-skill output routes through codebase-analyzer, trd-gen, and feature-implementor, but does not identify the request as Engineering work owned by engineer-agent. |
| `does_not_route_to_external_ui_skill` | PASS | With-skill output does not suggest or mention external ui-ux-pro-max. |
| `runs_feature_alignment` | PASS | It states feature_path customer-portal/profile-settings and names the PRD and TRD; the trace shows both documents were read before later routing checks. |
| `checks_design_deliverables` | PASS | It explicitly checks both requested design paths and reports that they are absent; the trace confirms the read-only file listing found only PRD and TRD. |
| `hands_design_gap_to_designer` | PASS | It identifies the missing design materials as a gap and hands the work to designer-agent for clarification and return. |
| `routes_implementation_after_design` | PASS | It states that after design confirmation the flow returns to implementation through feature-implementor and requires a confirmed IMPLEMENTATION_PLAN before implementation. |
| `does_not_execute_directly` | PASS | The output says this is plan confirmation only and does not modify code; locked git evidence shows no changes, and the trace contains only read commands. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c7cb9273b0ca01f312d499d16a87d54a68980710efc17abee5e6a4600012b8c0; fixture_sha256=ec60268c3cba621e7690e34a6ae14bc9ac52429e90275b6d4c2fdedef202a8df; output_sha256=8047c6cecb9baec35c06868107138a84d940f7101305b51439766a4741307d43; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly performs feature alignment, checks for missing design deliverables, hands the gap to Designer, preserves the implementation-plan gate, and does not mutate the repository, but omits explicit engineer-agent ownership.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c7cb9273b0ca01f312d499d16a87d54a68980710efc17abee5e6a4600012b8c0; fixture_sha256=ec60268c3cba621e7690e34a6ae14bc9ac52429e90275b6d4c2fdedef202a8df; output_sha256=1f00f91d5a30e93c267cd6b94ca62d45aa8271f0121d75f19c330cb4fa3e6663; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a generic phased implementation plan and correctly reports no mutations, but does not perform the required role routing, design-deliverable check, or Designer handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill lane omits the required explicit Engineering classification and engineer-agent ownership for the frontend implementation request.
- Next: Explicitly classify the request as an Engineering request owned by engineer-agent, while preserving the Designer handoff for the missing design inputs.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
