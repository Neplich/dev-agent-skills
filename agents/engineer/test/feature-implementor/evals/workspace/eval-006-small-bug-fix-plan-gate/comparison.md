# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-006-small-bug-fix-plan-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `189adddf12b53efb048e7c5d0b3605c9ce9d7f6b01023de7e418b715817c16f4` from `agents/engineer/test/feature-implementor/evals/workspace/eval-006-small-bug-fix-plan-gate`.
- Fixture SHA-256: `189adddf12b53efb048e7c5d0b3605c9ce9d7f6b01023de7e418b715817c16f4`
- Prompt SHA-256: `3ca6a3518bdc8bcc3b18e69a3a095ab08898901d1b98a9feaebe381c01e9564a`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `31ea692709a0817bc32ab74f76490bf0edfdea6902d08e36d2b8cbddeb78aee4`
- Skill overlay SHA-256: `32c9b06579315c3f3af57ed46ca530329febcbd28b2adfca751e5c7d8b333736`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `eedd6f2658d30fa0d35d3b4c542f62bf462bc6c1940c310dab2dd6d4429a52b7`
- Metadata SHA-256: `e36d75fac31fda1c2cb2830fe86474e7378a0134e27ed358915e6d77bdb6c000`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `treats_bug_fix_as_spec_backed` | FAIL | with_skill 提到 PRD/TRD，但未说明用户已确认预期和根因可支持安排实现；反而错误地将缺少源码视为无法制定计划的阻塞。 |
| `writes_bug_fix_implementation_plan` | FAIL | 未要求产出或更新 docs/engineer/notifications/IMPLEMENTATION_PLAN.md，也未明确列出验证命令。 |
| `records_no_complex_split` | FAIL | 未说明这是可不触发复杂 implementation/validation sub-agent split 的单文件小修复，也未提及仍需实施计划。 |
| `waits_before_fixing` | PASS | 未声称已修改或验证，并明确表示会在修改前等待用户确认。 |
| `prepares_e2e_handoff_after_fix` | NOT_EXERCISED | 当前仍处于修改前、等待确认阶段，修复后的 E2E 交接尚不能发生；锁定证据不足以判定该后续步骤。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3ca6a3518bdc8bcc3b18e69a3a095ab08898901d1b98a9feaebe381c01e9564a; fixture_sha256=189adddf12b53efb048e7c5d0b3605c9ce9d7f6b01023de7e418b715817c16f4; output_sha256=c10069ebb5b4f7ae4e926fa96be78ba7e09ba33d25354b865d9240e05823a941; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 保持未修改仓库并等待确认，但错误地以缺少源码阻塞计划，且遗漏实施计划要求和轻量分工说明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=3ca6a3518bdc8bcc3b18e69a3a095ab08898901d1b98a9feaebe381c01e9564a; fixture_sha256=189adddf12b53efb048e7c5d0b3605c9ce9d7f6b01023de7e418b715817c16f4; output_sha256=2c36ac81df56a738b9cf7e6b54b9d13d1a1754351277ecb5a0916ac8899bac3c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 只确认修改范围并等待确认，未提供实施计划、轻量分工判断或后续 E2E 交接。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未按 PRD/TRD 已确认的 spec-backed bug fix 处理。
- with_skill 未要求 IMPLEMENTATION_PLAN.md 或明确完整验证命令。
- with_skill 未记录单文件小修复无需复杂 sub-agent split 的判断。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-006-small-bug-fix-plan-gate`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/engineer/test/feature-implementor/evals/workspace/eval-006-small-bug-fix-plan-gate`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `f1664e91f85e64c4e9fe007c1e9e2a615f6259259dc6ff27919727268dd7653c`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `900d75b77daf90703f13264de50f85150aabe03ed551f4aaa693123d44200b53`
- Metadata SHA-256: `f3bb80342a617a983918f51133662fd7b95a522ce42a95ab77febc2c0a0be550`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `treats_bug_fix_as_spec_backed` | FAIL | with_skill 仅说明工作区为空、未找到目标文件，并请求确认；未说明用户已确认预期和根因，也未提出实施范围与验证办法。 |
| `writes_bug_fix_implementation_plan` | FAIL | with_skill 输出未要求产出或更新 docs/engineer/notifications/IMPLEMENTATION_PLAN.md，也未列出目标文件和验证命令。 |
| `records_no_complex_split` | FAIL | with_skill 提到仅实施单文件修复，但未说明可不触发复杂 implementation/validation split，且未同时明确不得跳过实施计划。 |
| `waits_before_fixing` | PASS | 输出明确表示尚未修改任何文件，并要求用户确认后才继续。git_evidence 也显示无变更。 |
| `prepares_e2e_handoff_after_fix` | FAIL | with_skill 输出未说明修复完成后的 PRD/TRD 对齐结论、已确认实施计划、变更文件、验证命令和建议功能树目录交接，也未提及确认前不得更新 E2E TC。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f1664e91f85e64c4e9fe007c1e9e2a615f6259259dc6ff27919727268dd7653c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=05b60b4d03654adb046d45d43489abed3b70840d2f45a2ad9dbf4c8b7289393b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 等待确认后再修改这一点满足，但未提供 spec-backed 处理说明、实施计划、轻量分工判断或修复后 E2E 交接要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f1664e91f85e64c4e9fe007c1e9e2a615f6259259dc6ff27919727268dd7653c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=3c5fe66079947bda981fa14338217987296952bc0c127808e4bbba795a89e6c3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了根因并在修改前请求确认，但未覆盖实施计划、分工判断或 E2E 交接要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill lane 满足 1/5 条断言，未满足其余四条。
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

# Eval Result: eval-006-small-bug-fix-plan-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-006-small-bug-fix-plan-gate`
- Test case: small-bug-fix-plan-gate
- Workspace: `workspace/eval-006-small-bug-fix-plan-gate`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 通知中心 active 列表没有排除 archived，已经确认这是实现偏离 PRD/TRD，不是需求变更；根因是 src/api/notifications.ts 的过滤条件少了 archived。请修复这个单文件问题。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `treats_bug_fix_as_spec_backed`: with_skill 错误称无法确认 PRD/TRD 已批准行为，并要求补充 PM/Engineer 文档；未按 prompt 说明 debugger 已确认这是实现偏离，且不应要求 DECISIONS.md。
- FAIL `writes_bug_fix_implementation_plan`: final 明确表示不能创建 IMPLEMENTATION_PLAN.md；workspace 中也不存在该文件。
- FAIL `records_no_complex_split`: 未说明这是单文件小修复、无需复杂 sub-agent split。
- PASS `waits_before_fixing`: transcript 明确表示计划确认前不会改代码；final 未声称已修复或验证通过，workspace 也无目标代码修改。
- FAIL `prepares_e2e_handoff_after_fix`: 未说明修复后向 QA E2E 文档流程交接所需内容，也未说明计划确认前不得更新 E2E TC。

## With Skill Behavior

with_skill 实际读取了 workspace 和 planner 规则，但将 prompt 已确认的 spec-backed bug fix 错误阻塞，未产出实施计划。hash 与 workspace 文件清单一致，未见写入目标文件。

## Without Skill Baseline

without_skill 作为对照，发现工作区为空且无目标文件，未执行修复。

## Failures / Findings

- 未将 bug fix 视为 debugger 已确认的实现偏离。
- 未创建或更新 IMPLEMENTATION_PLAN.md。
- 未记录无需复杂 sub-agent split。
- 未准备 QA E2E 文档交接说明。
- Root cause: with_skill 过度依赖 workspace 中缺失的 PM/TRD 文档链，忽略了用户 prompt 明确提供的 debugger 根因与 PRD/TRD 确认事实，导致错误阻塞。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-006-small-bug-fix-plan-gate

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-006-small-bug-fix-plan-gate`
- Test case: small-bug-fix-plan-gate
- Workspace: `workspace/eval-006-small-bug-fix-plan-gate`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture files read before skill use: `eval_metadata.json` and the `eval-006-small-bug-fix-plan-gate` item in `evals.json`.
- Fixture note: this workspace stores metadata only; the prompt declares debugger has confirmed the issue is an implementation deviation from approved PRD/TRD, not a requirements change.
- Expected output: treat the bug fix as spec-backed implementation work, produce or update `docs/engineer/notifications/IMPLEMENTATION_PLAN.md`, record `src/api/notifications.ts` and verification commands, wait for confirmation, and do not fix code yet.

## Assertions

- PASS `treats_bug_fix_as_spec_backed`: the skill allows spec-backed bug fixes after debugger or Engineer routing confirms approved PRD/TRD behavior.
- PASS `writes_bug_fix_implementation_plan`: even single-file bug fixes require `IMPLEMENTATION_PLAN.md`, file scope, and verification commands.
- PASS `records_no_complex_split`: the small-fix path can skip complex sub-agent split while still documenting that decision.
- PASS `waits_before_fixing`: implementor entry gate blocks code and test edits until the exact plan is confirmed.
- PASS `prepares_e2e_handoff_after_fix`: after implementation and self-review, QA E2E handoff needs PRD/TRD alignment, confirmed plan, changed files, verification commands/results, risks, and suggested feature tree directory.

## With Skill Behavior

Fresh with-skill validation confirmed that the small bug-fix path still runs through planner. Because the prompt says debugger already established this is a deviation from approved PRD/TRD behavior, the request may enter `feature-implementor`; it must not be sent back to PM just because there is no standalone `DECISIONS.md`. The plan should target `docs/engineer/notifications/IMPLEMENTATION_PLAN.md`, name `src/api/notifications.ts`, record deterministic verification commands, state no complex implementation/validation split is needed, and wait for confirmation before any code change or QA E2E update.

## Without Skill Baseline

The fresh without-skill baseline was summarized before reading skill docs. A generic worker is likely to honor "but first don't edit code" and produce some repair notes, but it may not create a durable implementation plan, may not distinguish spec-backed bug fix from generic debugging, may skip the split decision, and may omit the post-fix QA E2E handoff constraints.

## Failures

- None.

## Next Steps

- Keep this eval focused on spec-backed bug fixes requiring a plan and confirmation even when the code change is single-file.

## Runtime Artifacts Policy

- This validation did not create runtime artifacts.
- Runtime transcripts, verdicts, timing files, outputs, diagnostics, run status files, and `comparison.auto.md` must not be committed.
