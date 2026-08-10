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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1cfd412fc44e8e1667cc3feab76a58474b6382f405680057b41b379032f76e0a`
- Skill overlay SHA-256: `8ddfbafd6ae3cf064836ded5fbaa7bcc8a3ab817df212a0b6c4ff355a78b12af`
- Judge schema SHA-256: `6f1f540339fe5c4c310ca6aaedc38adff3d61e4268399a40149f44e3770ac25c`
- Eval definition SHA-256: `39cedbd8f4d80d0a4994293b5961329a7167770e2a14c811376cdcc3f99f53b0`
- Metadata SHA-256: `70b36659756bbd4d7fc0e09d0fabc7ee5ba1a168323c148fa735110fb59ec768`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routing_decision_present` | PASS | with_skill 输出明确给出 Routing decision，并包含 request_type、selected_owner、entry_basis、feature_path 和 execution_boundary。 |
| `stay_in_pm_alignment` | PASS | with_skill 将 owner 保持为 idea-to-spec，feature_path 为 unresolved，说明仍需 PM 需求收敛，并明确未执行代码、设计或测试修改；没有声称 Engineer handoff 已完成。 |
| `blocks_engineering_without_basis` | FAIL | with_skill 明确禁止当前修改代码并指出缺少产品、设计和实现依据，但未明确要求按布局变化补齐适用的 PRD、设计依据和技术范围。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c79b599caf92ed571529698026d612359f9682372926b9410e838e35d5c66dd6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确进行 PM 路由并停留在 idea-to-spec，阻止代码修改；但未完整列出 PRD、设计依据和技术范围要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=57e82609f413c88720ec90ed64877ede694585115e55bf0256d08e8274436d4f; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=ae868165ac2eefa894cf17f46779e832a217551acc4e79de7934adc96d78a142; snapshot_sha256=80140baa2634b0164909c7438d2756a1a2ac86521e018aeadefc017dedce8790
- Behavior: 直接创建设置页代码并声称完成实现，未进行 PM 路由或依据确认。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完整说明进入工程实现前需补齐适用的 PRD、设计依据和技术范围。
- Next: 补充明确的前置条件：确认产品范围，并补齐适用的 PRD、设计依据与技术范围后再进入工程实现。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
