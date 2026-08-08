# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-004-route-release-notes`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e` from `agents/docs/test/docs-agent/evals/workspace/eval-004-route-release-notes`.
- Fixture SHA-256: `23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e`
- Prompt SHA-256: `ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9fbb92b16f91777ce613be24ad3cd630730cfccd4cce1cf1d33c3b6c917671d6`
- Skill overlay SHA-256: `d552bdbf1aa95d384d7132b02e78e69678457f53a15c3f49ddfae00094ce8ee0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `8f5c2c38ebd9c9bb0326fa6044e4d6d7a5002b68fd540017de52e9465230113b`
- Metadata SHA-256: `5831b803b3b347d7fd4611f1c19958d707ffe3e9ced4a78ed755e71f76a2c9b8`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_notes_entry_basis` | FAIL | with_skill 仅提到版本、输出路径和站点目录阻塞，未保留或明确 host_repository、release_scope、evidence_sources 等完整入口依据。 |
| `routes_release_notes_generator` | FAIL | with_skill 将下一步错误指向 docs-site-bootstrap，未选择 release-notes-gen。 |
| `preserves_handoff_context` | FAIL | with_skill 输出仅保留目标版本和应产出路径，未保留 request_type、change_tier、feature_path、scope、仓库、来源、证据、要求及 blockers_risks。 |
| `references_release_notes_gate_only` | FAIL | with_skill 未指向 release-notes-gen/SKILL.md，反而指向 docs-site-bootstrap；虽未复制详细协议，但不满足指定 specialist gate。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=a42ff237850fa5f9c62ae2450319885070e37b5ee015ad524c4dc22711c52bf3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到版本说明目标，但因错误的站点基础门禁判断而阻塞，并错误建议 docs-site-bootstrap。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ab720b723fbaf54cc8b204eab97c1f0a7167519c350afdf3b475cf0b324862c8; fixture_sha256=23d5701fab562491dfec3455fd6eabce7f6a6cba18940861023208d40f53fc3e; output_sha256=f6e090760a361b77ac63fc96a267ef851a92226de1f49c3f9a57be022e5eb9d7; snapshot_sha256=1a93e9475aa51d959c884cec882a4095ecebf169ecffaf9413b10079f493ba38
- Behavior: 直接生成了站内版本说明文件；未体现 specialist 路由或完整 handoff 上下文。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- accepts_release_notes_entry_basis
- routes_release_notes_generator
- preserves_handoff_context
- references_release_notes_gate_only
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

# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-agent`
- Eval: `eval-004-route-release-notes`

## Test Set / Fixture Version

- Fixture version: `release-handoff.md`（fixture 身份文本 2026-07-29 更新后）
- Fresh run（2026-08-03，#188）：`tmp/eval-runs/issue-188-docs/with_skill/eval-004-route-release-notes/candidate-output.md` 与 `tmp/eval-runs/issue-188-docs/without_skill/eval-004-route-release-notes/candidate-output.md`
- Judge verdict: `tmp/eval-runs/issue-188-docs/judge/verdict.md`

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| accepts_release_notes_entry_basis | FAIL | FAIL | with_skill 仅笼统称 `release-handoff.md` 为完整交接包，未逐项保留宿主、scope、证据来源等依据；without_skill 只确认 `existing_update`、`major` 和 `v1.0.0`，并称相关证据文件不存在，未接受完整 specialist entry basis。 |
| routes_release_notes_generator | PASS | FAIL | with_skill 明确路由至 `docs-agent:release-notes-gen`；without_skill 仅写“由 Docs specialist 生成”，未选择 `release-notes-gen`。 |
| preserves_handoff_context | FAIL | FAIL | 两条 lane 均未在结果中保留完整的 `request_type`、`change_tier`、`feature_path`、`release_scope`、`host_repository`、`source_documents`、`evidence_sources`、`required_output` 和 `blockers_risks`。 |
| references_release_notes_gate_only | FAIL | FAIL | 两条 lane 均未指向 `release-notes-gen/SKILL.md` 或其内部指令；未复制详细协议，但缺少必要的 specialist gate 指针。 |

未满足断言（with/without 任一 FAIL）：`accepts_release_notes_entry_basis`、`routes_release_notes_generator`、`preserves_handoff_context`、`references_release_notes_gate_only`



## Fixture Drift Notice

fixture 身份文本已于 2026-07-29 从 issue 编号更新为 skill 名，旧 PASS 反映变更前 run。**2026-08-03（#188）已对当前 fixture 完成 fresh re-baseline**（with/without 双侧验证，judge 独立判定，证据见 `tmp/eval-runs/issue-188-docs/`），BLOCKED 状态消解；本节保留作为历史记录。

## Historical Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 2026-07-19（fixture 下游指向修正前）：**PASS（4/4 assertions）** — with-skill 接受完整 Release Notes entry basis，保留全部 handoff 上下文，选择 `release-notes-gen`，且没有复制或执行 specialist 协议。

## Assertions
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- `accepts_release_notes_entry_basis`：PASS。识别宿主、维护者确认版本、scope、证据与站内页面/下游 handoff 要求。
- `routes_release_notes_generator`：PASS。明确选择 `release-notes-gen`，排除 sync、audit、bootstrap 与 GitHub Release 当前执行。
- `preserves_handoff_context`：PASS。保留 request、tier、feature、version、scope、host、source、evidence、output 与 risk 字段。
- `references_release_notes_gate_only`：PASS。仅指向 specialist SKILL 及内部指令，没有复制七步流程或执行正文、metadata、checks、#117/#120 handoff。

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- fresh candidate 只完成 router 入口检查和分流，workspace 零写入。
- 输出明确正文确认与宿主检查仍由 specialist gate 处理，当前轮未自动继续。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：同一 prompt 与 pristine fixture 的本轮 fresh `without_skill`；不含目标 skill、Docs README、旧 comparison 或 with-skill 输出，未复用历史 baseline。
- baseline 已命名并正确路由 `docs-agent:release-notes-gen`（accepts 与 routes 两条断言 PASS），但未完整保留 handoff context（缺 `host_repository`、原始 `release_scope`），且复制了 specialist 流程、未引用权威 gate——2/4 PASS。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 with-skill assertion failure。
- Harness limitation：baseline 可通过父仓库 Git 命令看到文件名/状态，但未读取目标 skill 或 README 内容；未影响本用例的语义差异。后续应隔离 scratch Git 元数据。

## Next Steps

- 保持 Release Notes 窄路由与 specialist 单一真源；入口字段或边界变化时重跑。

## Runtime Artifact Policy

- candidate、transcript、manifest、diff 与状态文件仅保留在 `tmp/eval-runs/issue-188-docs/`，不提交到 git。
