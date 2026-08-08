# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-002-feature-path-audit`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a481b5374544e745048b6d91a89eb4240f2b8d26afa6409ed21d0c822a29f8c9` from `agents/devops/test/env-config-auditor/workspace/eval-002-feature-path-audit`.
- Fixture SHA-256: `a481b5374544e745048b6d91a89eb4240f2b8d26afa6409ed21d0c822a29f8c9`
- Prompt SHA-256: `45dd97708d4498ba2c5e31fb882b1692d7db80756c144b5c54d249bddbdf8a4b`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `30d88474014fd1654b2afdad809dd429177b5ede44673678193420a680992fce`
- Skill overlay SHA-256: `4a296e51a1a55fbed13be81dcfbf208640c3c058625400ff291752ea55bee7b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6efcde24d7900ac81923c70a8eb454a7b5687569fc19e166e7a2702223bf20b8`
- Metadata SHA-256: `ed9d0f761d7a235166a80b0e2724cd90628f15321561b77d0b2d2233a2c87014`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_confirmed_feature_path` | PASS | with_skill 输出使用 feature_path `chat-interface/messages/history/search`，并明确关联 `docs/engineer/chat-interface/messages/history/search/TRD.md` 与 `docs/engineer/chat-interface/messages/history/search/IMPLEMENTATION_PLAN.md`；两文件在 fixture 中存在。 |
| `writes_nested_devops_report` | PASS | with_skill 的 git_status 与输出均指向 `docs/devops/chat-interface/messages/history/search/ENV_AUDIT.md`，符合要求的嵌套路径。 |
| `does_not_invent_feature_directory` | NOT_EXERCISED | fixture 中 feature_path 清晰，且同路径 TRD 与实施计划均存在，因此未触发回 PM/Engineer 对齐的条件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=45dd97708d4498ba2c5e31fb882b1692d7db80756c144b5c54d249bddbdf8a4b; fixture_sha256=a481b5374544e745048b6d91a89eb4240f2b8d26afa6409ed21d0c822a29f8c9; output_sha256=2446f0c3b3dfbd0bd9fa66ac8705a7f1250da5601832336e3bb4712b96b6d2a6; snapshot_sha256=dad1a87c5cff07ec54c6aeb955345fcd22d2b3e019bf364431de212596375b48
- Behavior: 沿用确认的功能路径，读取并关联同路径工程文档，将审计写入要求的嵌套 DevOps 路径，且未修改既有工程文档。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=45dd97708d4498ba2c5e31fb882b1692d7db80756c144b5c54d249bddbdf8a4b; fixture_sha256=a481b5374544e745048b6d91a89eb4240f2b8d26afa6409ed21d0c822a29f8c9; output_sha256=fb657a4bf1ee85cca160c575a77e345209aef5ad7c0b98403c7e301cfeb2ee81; snapshot_sha256=17994eec0b01a427aba54564150b3e594fd01792b386b9c03c1652c5c91f278b
- Behavior: 识别了配置审计问题，但将报告写入 Engineer 目录下的错误文件名，并修改实施计划。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

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

# Eval Result: eval-002-feature-path-audit

## Evaluation Target

- Agent: `devops`
- Skill: `env-config-auditor`
- Eval: `eval-002-feature-path-audit`
- Test case: `feature-path-audit`
- Workspace: `agents/devops/test/env-config-auditor/workspace/eval-002-feature-path-audit`

## Latest Result

- Fresh run: `2026-08-07`（issue #238 严格隔离重跑）
- Model: `gpt-5.6-luna`，`model_reasoning_effort=medium`
- Isolation: baseline 使用随机顶层 root；完成后仅保存在内存快照并删除 root，随后才创建 with_skill root；with_skill root 删除后才创建独立 judge root。两条 lane 的原始 prompt、fixture snapshot、`HOME` 与 `CODEX_HOME` 值相同。
- Judge: 独立 fresh `codex exec`，读取实际产物、final、status 与工具轨迹，对照当前 assertions 判定；不采信 lane 自评。
- Behavior result: PASS
- Coverage result: PARTIAL
- Without-skill comparison: FAIL（仅作对照，不参与 durable Overall 组合）

Overall result: PASS (partial coverage)

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Eval definition: `agents/devops/test/env-config-auditor/evals/evals.json`
- Metadata: `agents/devops/test/env-config-auditor/workspace/eval-002-feature-path-audit/eval_metadata.json`
- Expected output: 读取同一 feature_path 下的 PM/Engineer 文档，输出 docs/devops/chat-interface/messages/history/search/ENV_AUDIT.md，不生成 docs/devops/history-search/ENV_AUDIT.md 或 docs/devops/chat-interface/history-search/ENV_AUDIT.md。
- Fixture: `docs/pm/chat-interface/messages/history/search/PRD.md`, `docs/engineer/chat-interface/messages/history/search/TRD.md`, `docs/engineer/chat-interface/messages/history/search/IMPLEMENTATION_PLAN.md`, `src/server.ts`, `deploy/local/.env.example`

## Assertion Results

| Assertion | with_skill | without_skill | Evidence |
| --- | --- | --- | --- |
| `uses_confirmed_feature_path` | PASS | PASS | 两条 lane 均读取了同路径的 docs/engineer/chat-interface/messages/history/search/TRD.md 与 IMPLEMENTATION_PLAN.md；with-skill trace 明确记录了这些读取。 |
| `writes_nested_devops_report` | PASS | FAIL | with-skill status 显示新增 docs/devops/chat-interface/messages/history/search/ENV_AUDIT.md；without-skill status 显示新增错误路径 docs/engineer/chat-interface/messages/history/search/ENV_CONFIG_AUDIT.md。 |
| `does_not_invent_feature_directory` | NOT_EXERCISED | NOT_EXERCISED | fixture 中 feature_path 明确，且同路径 TRD 与 IMPLEMENTATION_PLAN 均存在，因此该条件分支未触发。 |

## With-Skill Behavior

- with-skill 正确使用确认的嵌套 feature_path，并输出要求的 DevOps 审计报告路径；条件分支断言因 fixture 不具备触发前提而未执行，因此 Coverage 为 PARTIAL。without-skill 输出路径错误，作为 baseline FAIL，不影响 durable Overall。
- Workspace changes: added: `docs/devops/chat-interface/messages/history/search/ENV_AUDIT.md`。

## Fresh Without-Skill Baseline

- baseline 在本轮重新生成，没有复用历史 baseline，也没有读取 target skill、with_skill 产物或旧 comparison。
- Workspace changes: added: `docs/engineer/chat-interface/messages/history/search/ENV_CONFIG_AUDIT.md`。
- assertion 结果见上表；baseline 只用于比较 skill 增益，不作为 durable Overall 的独立机器门禁。

## Failures and Coverage Gaps

- with_skill 无 assertion failure。
- NOT EXERCISED: `does_not_invent_feature_directory`；fixture 未触发对应条件分支。
- 无模型、认证、runner 或外部服务 blocker。

## Historical Result (Old Contract)

- 旧结论为 PASS，但仅做静态审查且没有 fresh baseline；issue #234 后标为 BLOCKED 等待重跑。
- 该历史结论适用旧 eval 契约；本文件顶部的 2026-08-07 fresh 结果已取代它作为 latest durable 结论。

## Next Steps

- 保留当前行为结果；若要获得 FULL coverage，需要新增能够触发 NOT EXERCISED 条件分支的独立 fixture。

## Runtime Artifact Policy

- 两条 lane、工具轨迹、状态、文件快照、judge verdict 与隔离事件只保存在 `tmp/eval-runs/issue-238-devops-strict-20260806/`，不提交 git。
- durable 结果只保留本 `comparison.md`。
