# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-011-change-tier-standard-full-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-11-change-tier-standard-full-gate`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `2c9f63eba393d7546f89112ce3f1659145dc2f6ca60bdba6ba71df10258a35a4`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1cfd412fc44e8e1667cc3feab76a58474b6382f405680057b41b379032f76e0a`
- Skill overlay SHA-256: `8ddfbafd6ae3cf064836ded5fbaa7bcc8a3ab817df212a0b6c4ff355a78b12af`
- Judge schema SHA-256: `e0fce32f646911cc00fe0709c7d0e934a3657054c9fc5a2efda7653a3ac97ea6`
- Eval definition SHA-256: `da85ba336c757be6c6ca84ef12c1d1a20655adb3e82559a2c2234b5462387973`
- Metadata SHA-256: `6652dce9ab8a85ed09b58d853b1bdac1fd0f6f3e5ccd74f38c1d4aa6171a8cf4`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classify_standard` | PASS | with_skill 的 Routing decision 明确写出 `change_tier: standard` 且 `hotfix_disposition: rejected`。 |
| `require_prd_trd_alignment` | PASS | with_skill 将 `entry_basis` 标为 `missing`，要求完成需求对齐并更新 PRD/DECISIONS，且明确阻止代码、测试和部署执行，等待 PM 入口依据。 |
| `request_type_existing_update` | PASS | with_skill 的 Routing decision 明确写出 `request_type: existing_update`，并说明这是既有退款审批业务规则的变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9f63eba393d7546f89112ce3f1659145dc2f6ca60bdba6ba71df10258a35a4; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=fdac81b1a6b4f412606c7edf57798693b617424efb8952dacfaa5f2dc5d99f33; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别为 existing_update 和 standard，拒绝 hotfix，并在缺少项目资料时要求先完成需求/产品对齐，阻止下游实施。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2c9f63eba393d7546f89112ce3f1659145dc2f6ca60bdba6ba71df10258a35a4; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=55d4c05e130b21ebf2956fba1c91c513146399aa4cf40fb941e8613e433fb6a9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅报告空仓库并请求提供项目代码，未作出请求类型、变更分级或需求对齐门禁判断。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
