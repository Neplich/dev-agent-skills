# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-003-missing-trd-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ab5acf9561757cd60998119f1643fd8622ced39a8046dbb107e9cf8100e1110f` from `agents/engineer/test/feature-implementor/evals/workspace/eval-003-missing-trd-handoff`.
- Fixture SHA-256: `ab5acf9561757cd60998119f1643fd8622ced39a8046dbb107e9cf8100e1110f`
- Prompt SHA-256: `b3686b3e49b5b805ba890514f93468b848aeefc3a94d03ef515571046a19d7e0`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `beeebfd4f2a4eb407e840ff01043296b9db4c0e70af2a9d7de790cf54280c082`
- Metadata SHA-256: `b646b97a67422c086871d592a86b4ef2968c69945b431fbbc93a36b8db79d701`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_engineer_trd` | PASS | 明确指出 `docs/engineer/capture-loop/TRD.md` 缺失。 |
| `hands_off_to_trd_gen` | FAIL | 要求补充 TRD，但未交给 `engineer-agent:trd-gen` 编写或确认。 |
| `does_not_write_plan_or_code` | PASS | 未编写实现计划、代码、测试或文件变更计划，也明确未修改文件。 |
| `names_required_trd_decisions` | FAIL | 列出了重试、状态、调度、持久化、可观测性和测试等决策，但未覆盖受影响组件或模块、数据流/API/集成影响、发布或回滚风险及安全策略。 |
| `keeps_finder_trd_gen_boundary` | FAIL | 未明确发现者与 `engineer-agent:trd-gen` 的职责边界，也未指明由该 agent 补完整 TRD。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b3686b3e49b5b805ba890514f93468b848aeefc3a94d03ef515571046a19d7e0; fixture_sha256=ab5acf9561757cd60998119f1643fd8622ced39a8046dbb107e9cf8100e1110f; output_sha256=9145e69ed4f2777cd47fc582c6229f6d5a2096d881cb7fe4a6e99ff5222dc2ce; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别缺失 TRD，并保持未修改 workspace；但缺少 engineer-agent:trd-gen 交接、职责边界及完整技术决策覆盖。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b3686b3e49b5b805ba890514f93468b848aeefc3a94d03ef515571046a19d7e0; fixture_sha256=ab5acf9561757cd60998119f1643fd8622ced39a8046dbb107e9cf8100e1110f; output_sha256=8db71cd312ff6d7517715da17bbbaa2dff6dee77812c769db16055ff3f5a89b9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别 workspace 缺少源码，但未明确指出 Engineer TRD 缺失，也未提出 TRD 交接或技术决策清单。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 3 项断言：TRD-gen 交接、完整技术决策清单、发现者与 trd-gen 边界。
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

# Eval Result: eval-003-missing-trd-handoff

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-003-missing-trd-handoff`
- Test case: missing-trd-handoff
- Workspace: `workspace/eval-003-missing-trd-handoff`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 请根据 docs/pm/capture-loop/PRD.md 实现 Capture Loop 队列重试能力。当前 workspace 没有 docs/engineer/capture-loop/TRD.md。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `detects_missing_engineer_trd`: final.md 明确指出缺少 `docs/engineer/capture-loop/TRD.md`。
- PASS `hands_off_to_trd_gen`: final.md 明确要求转回 `engineer-agent:trd-gen` 补齐并确认 TRD。
- PASS `does_not_write_plan_or_code`: final.md 明确写明未创建计划、未修改代码；workspace 输出 hash 与输入 hash 一致，且无 IMPLEMENTATION_PLAN、代码或测试文件。
- PASS `names_required_trd_decisions`: final.md 列出重试策略、受影响组件/API/集成、幂等并发持久化、验证命令/测试、发布迁移回滚风险等缺失决策。
- FAIL `keeps_finder_trd_gen_boundary`: 虽要求转回 `engineer-agent:trd-gen`，但未明确说明发现者只负责说明 TRD 缺口、由 trd-gen 负责补完整 TRD。

## With Skill Behavior

with_skill 正确识别缺失 TRD、停止实现并完成大部分 gap packet；但缺少明确的 finder/trd-gen 职责边界表述。transcript 仅记录该最终回复，workspace hash 未发生变化。

## Without Skill Baseline

without_skill 仅以缺少源码、测试和 TRD 为由阻止实现，未按要求交回 `engineer-agent:trd-gen`，也未列出完整 TRD gap packet；transcript 中曾出现实现计划意图，但 workspace hash 未发生变化。

## Failures / Findings

- keeps_finder_trd_gen_boundary 未满足：最终输出没有明确声明发现者仅说明缺口、trd-gen 负责补完整 TRD。
- Root cause: 最终 handoff 文案缺少 skill 要求的显式职责边界句。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-003-missing-trd-handoff

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-003-missing-trd-handoff`
- Test case: missing-trd-handoff
- Workspace: `workspace/eval-003-missing-trd-handoff`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `README.md`, `eval_metadata.json`, and `docs/pm/capture-loop/PRD.md`.
- Fixture summary: PM scope exists for Capture Loop retry behavior, but `docs/engineer/capture-loop/TRD.md` is intentionally absent.
- Expected output: stop before `IMPLEMENTATION_PLAN.md` and code, hand off to `engineer-agent:trd-gen`, and provide a complete TRD gap packet.

## Assertions

- PASS `detects_missing_engineer_trd`: the alignment gate requires `docs/engineer/{feature_path}/TRD.md` before planning.
- PASS `hands_off_to_trd_gen`: missing, stale, incomplete, path-mismatched, or conflicting TRDs return to `engineer-agent:trd-gen`.
- PASS `does_not_write_plan_or_code`: planner stops before implementation plan, code, tests, or file-change plan when TRD is missing.
- PASS `names_required_trd_decisions`: the TRD gap packet must cover technical decisions, components, data/API/integration impacts, validation commands, rollout risks, and error handling/observability/security strategy.
- PASS `keeps_finder_trd_gen_boundary`: planner states the finder only clarifies gaps and `trd-gen` completes the TRD.

## With Skill Behavior

Fresh with-skill validation confirmed that the direct specialist gate remains strict: a PRD alone is not an equivalent confirmed document chain. The current skill should resolve `feature_path: capture-loop`, detect the missing mirrored Engineer TRD, and stop before creating `docs/engineer/capture-loop/IMPLEMENTATION_PLAN.md`. It should hand the work to `engineer-agent:trd-gen` with the required TRD gap packet and boundary statement.

## Without Skill Baseline

The fresh without-skill baseline was summarized before reading skill docs. Because the prompt explicitly says the TRD is missing and says not to code, a generic response might still block direct implementation. Its likely weakness is an incomplete handoff: it may not name all missing technical decisions, may omit validation and rollout/error strategy, and may not clearly separate the finder role from `engineer-agent:trd-gen`.

## Failures

- None.

## Next Steps

- Keep this eval focused on missing-TRD blocking and full TRD gap handoff.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
