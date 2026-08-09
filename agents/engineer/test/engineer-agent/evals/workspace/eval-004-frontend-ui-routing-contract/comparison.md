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
- Fixture SHA-256: `ec60268c3cba621e7690e34a6ae14bc9ac52429e90275b6d4c2fdedef202a8df`
- Prompt SHA-256: `c7cb9273b0ca01f312d499d16a87d54a68980710efc17abee5e6a4600012b8c0`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `cfa5a88208f1b1c899ab19782fdf4b1c4f59251e80b5c7edaead85a7f37b2ebd`
- Skill overlay SHA-256: `077bb84411e61374de4fd93945f7e775b9133b3517221140cf4b19937f8b8f70`
- Judge schema SHA-256: `e2168c580c03f1c43acee8d4077b4a9553410b224e0542721c19d2cc8e09e39c`
- Eval definition SHA-256: `bfc10d83b8c5a5962987ac2605d966a1788bde7de31566b4d329601b6b214354`
- Metadata SHA-256: `4906971d417635b5c425ac490e57080c03cc4473b36cee23eaff89fa06fe26b0`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_frontend_update_to_engineer` | PASS | with_skill 明确指定 Owner 为 `engineer-agent`，并将前端实现列入后续工程流程。 |
| `does_not_route_to_external_ui_skill` | PASS | with_skill 输出未建议修改、调用或依赖 `ui-ux-pro-max`。 |
| `runs_feature_alignment` | NOT_EXERCISED | 输出列出 `customer-portal/profile-settings` 及对应 PRD/TRD，但锁定证据无法证明实际读取顺序。 |
| `checks_design_deliverables` | PASS | with_skill 明确说明未发现 `ui-ux-spec.md` 或 `visual-system.md`，且当前变化涉及信息层级和按钮样式。 |
| `hands_design_gap_to_designer` | PASS | with_skill 要求将信息层级、主按钮样式规则、响应式与交互状态交给 `designer-agent`。 |
| `routes_implementation_after_design` | PASS | with_skill 将设计对齐置于实现之前，并要求基于设计文档和确认后的 `IMPLEMENTATION_PLAN.md` 返回 `feature-implementor` 实现。 |
| `does_not_execute_directly` | PASS | 输出明确声明本轮不改代码；锁定 git 证据显示无状态、索引、工作区或提交变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c7cb9273b0ca01f312d499d16a87d54a68980710efc17abee5e6a4600012b8c0; fixture_sha256=ec60268c3cba621e7690e34a6ae14bc9ac52429e90275b6d4c2fdedef202a8df; output_sha256=3f1736eabda86e6631f6325cb3ccf8651fc65a22b709ea47f317d746c10fdd15; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确将前端变更路由至 engineer-agent，识别设计交付缺口并交给 designer-agent，设计完成且 IMPLEMENTATION_PLAN 确认后再实现；未执行代码变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c7cb9273b0ca01f312d499d16a87d54a68980710efc17abee5e6a4600012b8c0; fixture_sha256=ec60268c3cba621e7690e34a6ae14bc9ac52429e90275b6d4c2fdedef202a8df; output_sha256=705cb52e061923c8d10b83badcbc7ca5cc2104dda1c3382a660d92996ebf37d1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 提供了基于现状的通用推进建议，但未呈现明确的 engineer-agent 路由、feature_path 对齐或设计代理交接。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充可证明 PRD/TRD 实际读取顺序的运行证据。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
