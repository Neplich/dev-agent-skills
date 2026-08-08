# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `devops-agent`
- Eval: `eval-002-route-docs-site-completeness-chain`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3` from `agents/devops/test/devops-agent/evals/workspace/eval-002-route-docs-site-completeness-chain`.
- Fixture SHA-256: `db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3`
- Prompt SHA-256: `520c4aa6ac767af388d73d9adeec0eb6b05a688f692c19decf65da48e498c67e`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4c5e2e817a46aa6aa63d1e8786af2b82affbb324db7f825fe732309004758885`
- Skill overlay SHA-256: `368c3d513c6ac8a75b6ccb6f1f8a38f74c7645a2abce8dac81ffc9712870c0a6`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dc1b04424607a1675278b8e310c3f7b0da94f3cf1e857f037b9a6a8dbbf9482f`
- Metadata SHA-256: `2718def12280e05b73752266e8d3b39d6929d0781f7ca1aa2088b55bd4e38e9c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_repo_wide_docs_handoff` | PASS | With-skill output accepts deployment scope, treats feature path as N/A, and plans all documentation variants without requesting feature_path clarification. |
| `routes_dependency_order` | PASS | It explicitly states deployment-planner → cicd-bootstrap → env-config-auditor → docs-agent:formal-docs-sync. |
| `preserves_role_and_authority_boundaries` | FAIL | It preserves Docs as the final consumer of verified facts and notes missing publication/permission evidence, but does not explicitly state that DevOps must not modify formal docs or that the handoff does not authorize commit, push, image publication, or deployment. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=520c4aa6ac767af388d73d9adeec0eb6b05a688f692c19decf65da48e498c67e; fixture_sha256=db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3; output_sha256=9986482e82ddff5205bba9100aa1e1c1d65ad4b7adcfe71c6d4a9c7ca5613f5b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Names the required dependency chain, handles the repo-wide deployment handoff, and defines evidence-based stage outputs; authority boundaries are incomplete.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=520c4aa6ac767af388d73d9adeec0eb6b05a688f692c19decf65da48e498c67e; fixture_sha256=db76812ee462c1a8d89decf8e6fae581930c1406d7c6f72f3847172ed0bb02f3; output_sha256=33636eeec80e0bc7212d18b87e4b2af3517e00f29abd42fd6d1bcff602e9244c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a generic repository-wide deployment sequence and evidence handoffs, but does not name the required agent chain.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- preserves_role_and_authority_boundaries failed because the with_skill output omits explicit no-modification and no-authorization constraints.
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

# Eval Result: eval-002-route-docs-site-completeness-chain

## Evaluation Target

- Agent: `devops`
- Skill: `devops-agent`
- Eval: `eval-002-route-docs-site-completeness-chain`
- Test case: `route-docs-site-completeness-chain`
- Workspace: `agents/devops/test/devops-agent/evals/workspace/eval-002-route-docs-site-completeness-chain`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: PASS
- Coverage result: FULL
- Without-skill comparison: FAIL（仅作对照，不参与 durable Overall 组合）

Overall result: PASS

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/devops-agent/evals/evals.json`
- Metadata: `agents/devops/test/devops-agent/evals/workspace/eval-002-route-docs-site-completeness-chain/eval_metadata.json`
- Expected output: 按 deployment-planner 到 cicd-bootstrap 到 env-config-auditor 再回 formal-docs-sync 的顺序路由。
- Fixture: `pm-handoff.md`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `accepts_repo_wide_docs_handoff` | PASS | PASS | with_skill 接受 deployment、feature_path=N/A 的 repo-wide handoff，未退回 feature_path 澄清；without_skill 也未退回澄清。 |
| `routes_dependency_order` | PASS | FAIL | with_skill-final 明确给出 deployment-planner → cicd-bootstrap → env-config-auditor → docs-agent:formal-docs-sync；without_skill-final 未给出该依赖顺序。 |
| `preserves_role_and_authority_boundaries` | PASS | PASS | with_skill-final 明确未修改文件并停止于不可验证资产，未执行部署或文档修改；符合 fixture 中未预授权交付的边界。 |

## With-Skill Behavior

- with_skill 三项断言均满足，Coverage 为 FULL，因此 durable Overall 为 PASS。without_skill 缺少所要求的依赖顺序，判为 baseline FAIL；不影响 durable Overall。
- Workspace changes: 无文件变更。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: 无文件变更。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill 无 assertion failure。
- 所有当前 assertions 均已实际覆盖。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS（3/3）；issue #234 修复 eval 泄漏后，该结论被标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 保留当前回归用例；后续 skill、fixture 或断言变化时继续执行同等严格的 fresh paired run。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
