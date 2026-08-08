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
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `83f220b482f661eab0884cc4770c84fbb545af7bd74199e0b9f4ba499020031a`
- Skill overlay SHA-256: `94585e968fb2a0b5b29dd98429a0ee0f98e86ec73794257bcf099dd92d775e4c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bfc10d83b8c5a5962987ac2605d966a1788bde7de31566b4d329601b6b214354`
- Metadata SHA-256: `4906971d417635b5c425ac490e57080c03cc4473b36cee23eaff89fa06fe26b0`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_frontend_update_to_engineer` | FAIL | with_skill 未将前端更新识别为 Engineering request，也未指定由 `engineer-agent` 承接。 |
| `does_not_route_to_external_ui_skill` | PASS | with_skill 输出未建议修改、调用或依赖 `ui-ux-pro-max`。 |
| `runs_feature_alignment` | FAIL | with_skill 仅泛泛提到 PRD/TRD 和链接，未解析 `customer-portal/profile-settings` feature_path，也未明确读取两份文档后再路由。 |
| `checks_design_deliverables` | FAIL | with_skill 未检查 `docs/design/customer-portal/profile-settings/ui-ux-spec.md` 或 `visual-system.md`；fixture 中也仅有 PRD.md 与 TRD.md。 |
| `hands_design_gap_to_designer` | FAIL | with_skill 未将设计交付物缺口 handoff 到 `designer-agent`，也未说明需补齐的信息层级与按钮样式设计范围。 |
| `routes_implementation_after_design` | FAIL | with_skill 未说明设计完成后回到 `engineer-agent` / `feature-implementor`，也未提及 IMPLEMENTATION_PLAN 确认门禁。 |
| `does_not_execute_directly` | PASS | with_skill 明确建议本轮先不改代码；git evidence 显示无代码、文档或其他工作区变更，且未执行测试。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c7cb9273b0ca01f312d499d16a87d54a68980710efc17abee5e6a4600012b8c0; fixture_sha256=ec60268c3cba621e7690e34a6ae14bc9ac52429e90275b6d4c2fdedef202a8df; output_sha256=c3f752a0b5c1d94f78647ce0924b99a6fc04b5af6815c5293445103400c7d1d8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 说明暂不改代码并讨论信息层级、按钮规格和后续实现，但未执行规定的 feature 对齐、设计交付物检查及 Engineer/Designer 路由。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c7cb9273b0ca01f312d499d16a87d54a68980710efc17abee5e6a4600012b8c0; fixture_sha256=ec60268c3cba621e7690e34a6ae14bc9ac52429e90275b6d4c2fdedef202a8df; output_sha256=faf8cfd4decaa824bbef7b105d4169e6fbad72f189b5ddf7de153c2dc0a9f227; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline提供一般性的产品、设计、实现步骤，但未完成规定的工程路由、设计交付物检查或 Designer handoff。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 5 项关键路由与对齐断言：未路由至 engineer-agent、未完成 PRD/TRD feature 对齐、未检查设计交付物、未 handoff 至 designer-agent、未说明设计后回到实现并遵守 IMPLEMENTATION_PLAN 门禁。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Eval Result: eval-004-frontend-ui-routing-contract

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-004-frontend-ui-routing-contract`
- Test case: frontend-ui-routing-contract
- Workspace: `workspace/eval-004-frontend-ui-routing-contract`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 用户说：Customer Portal 的 profile settings 已有 PRD/TRD，现在要更新前端代码，调整设置页的信息层级和主按钮样式。请先做工程路由，不要改代码。相关文档在 docs/pm/customer-portal/profile-settings/PRD.md 和 docs/engineer/customer-portal/profile-settings/TRD.md。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `routes_frontend_update_to_engineer`: with_skill final 仅写 `feature-implementor`，未明确由 `engineer-agent` 承接；不可据此推断满足要求。
- PASS `does_not_route_to_external_ui_skill`: final/transcript 未建议调用或依赖 `ui-ux-pro-max`。
- PASS `runs_feature_alignment`: transcript 实际读取 PRD/TRD，并确认 `feature_path` 为 `customer-portal/profile-settings`。
- PASS `checks_design_deliverables`: transcript 检查了 docs/design 下目标路径，且 final 明确指出 ui-ux-spec.md 与 visual-system.md 均未发现。
- FAIL `hands_design_gap_to_designer`: 虽 handoff 到 `designer-agent`，但未具体说明需补齐信息层级与主按钮样式的设计范围。
- FAIL `routes_implementation_after_design`: final 仅说明回到 `feature-implementor`，未说明遵守 `IMPLEMENTATION_PLAN` 确认门禁。
- PASS `does_not_execute_directly`: exit_code 为 0；workspace 实际文件哈希与输入哈希一致，未见代码、IMPLEMENTATION_PLAN 或测试执行证据。

## With Skill Behavior

完成了 PRD/TRD 读取、feature_path 对齐和设计交付物存在性检查，并进行了 Designer → feature-implementor 路由；但缺少明确的 engineer-agent 承接表述、具体设计缺口范围及 IMPLEMENTATION_PLAN 门禁。

## Without Skill Baseline

without_skill 仅作对照：读取 PRD/TRD 后错误地转向 URL/路由注册分析，未检查设计交付物，也未形成 Designer handoff。

## Failures / Findings

- routes_frontend_update_to_engineer
- hands_design_gap_to_designer
- routes_implementation_after_design
- Root cause: with_skill 的路由结论不完整，遗漏了 engineer-agent 明确承接、设计缺口具体范围和 IMPLEMENTATION_PLAN 确认门禁。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-004-frontend-ui-routing-contract

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-004-frontend-ui-routing-contract`
- Test case: frontend-ui-routing-contract
- Workspace: `workspace/eval-004-frontend-ui-routing-contract`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: frontend UI request for `customer-portal/profile-settings` with same-path PRD/TRD and intentionally absent design deliverables.
- Fresh validation date: 2026-08-01.
- With-skill source: current Engineer README, current `engineer-agent` SKILL, eval definition, metadata, README, and same-path PRD/TRD.
- Without-skill source: the same prompt and fixture, freshly regenerated without reading or applying the target README/SKILL, with-skill output, historical comparison, or prior baseline.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


All 7 assertions were exercised and passed in the with-skill run.

## Assertions

- PASS `routes_frontend_update_to_engineer`: treats local frontend/UI implementation as Engineering work.
- PASS `does_not_route_to_external_ui_skill`: does not use external `ui-ux-pro-max`.
- PASS `runs_feature_alignment`: preserves `customer-portal/profile-settings` and reads its PRD/TRD.
- PASS `checks_design_deliverables`: checks the same-path UI/UX and visual-system files.
- PASS `hands_design_gap_to_designer`: hands the missing information hierarchy and button-style design scope to `designer-agent`.
- PASS `routes_implementation_after_design`: returns to `feature-implementor` only after design completion and plan confirmation.
- PASS `does_not_execute_directly`: remains route-only.

## With Skill Behavior

The fresh route keeps frontend implementation in Engineer, aligns the same feature path, checks both repository-native design deliverables, hands the fixture's design gap to `designer-agent`, and returns to `feature-implementor` behind the confirmed-plan gate.

## Without Skill Baseline

The fresh baseline identifies frontend engineering, avoids the external skill, generically recommends a designer for missing specifications, and remains route-only. It omits the exact same-path alignment, repository design-file checks, named agent handoff, and `feature-implementor` implementation-plan gate. Baseline assertion result: 4/7.

## Failures

- None.

## Next Steps

- Keep this eval as regression coverage for frontend/UI implementation routing and repository-native design handoff.

## Runtime Artifacts Policy

- Fresh runtime evidence is under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/engineer-agent/eval-004-frontend-ui-routing-contract/`.
- `with_skill.md`, `without_skill.md`, and `verdict.md` are scratch evidence and must not be committed.
- This `comparison.md` is the only durable result.
