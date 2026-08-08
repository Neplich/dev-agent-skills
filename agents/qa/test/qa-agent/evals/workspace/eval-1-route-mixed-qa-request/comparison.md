# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5` from `agents/qa/test/qa-agent/evals/workspace/eval-1-route-mixed-qa-request`.
- Fixture SHA-256: `c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5`
- Prompt SHA-256: `d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `fce4a3d76c9b69c96fdd86c3a44479dd8a12dd392536b124aa25210a7efca146`
- Skill overlay SHA-256: `02078f32eed1000178bae7f378d81856a077951dbb061b6ea461010744428cde`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `df4278b098e7470d5c41718341478d7c82c0968178c0b46c4b2f1526aa5b9366`
- Metadata SHA-256: `4be0f47d4261e8c4b656f6ffc80cff8a92794168034f2231da1ec209e3d5f4fd`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With_skill selects spec-based-tester as the main route, frames the work as feature-update scope acceptance, and contrasts it with full regression and immediate bug analysis. |
| `assertion_2` | FAIL | It names PRD/TRD/implementation plan and QA materials, plus platform/browser version, but does not explicitly require downstream reading of environment instructions and a concrete test command; the CI failure input is discussed rather than listed as required context to read. |
| `specialist_gate_pointer` | FAIL | It selects spec-based-tester and mentions platform version plus PRD/TRD/implementation plan, but does not point to authoritative E2E memory, credentials, execution entry, or blocked-condition gate applicability. |
| `assertion_4` | PASS | It specifies requirement matrices, feature paths, evidence references, per-TC result directories, a feature-update report, and risk/blocked-item treatment. |
| `assertion_5` | PASS | It uses spec-based-tester as the single main route, defers bug-analyzer to a stable reproduction, and explicitly says the intermittent symptom must not be marked a confirmed bug. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=46abced89ee013ee28226b77ce8e2935c16ca291baf14edc8ee16e1e9d70e04d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Selects spec-based-tester, preserves the intermittent-failure risk distinction, and defines structured artifacts, but omits required downstream context details and the specialist authority gate pointer.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=d32b34f557a9af42827fae115c24f25ec47fe1e0fcda62e092dc3afa3789c767; fixture_sha256=c9268123afd7a11d5bd4ac6d14865261ea2db8883ff6a745cea96f843ec5dbd5; output_sha256=6b7986914c4a65bdcb3f55a996fa36de4a267edc12cee141a31d96962479994c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a reasonable conditional-acceptance recommendation and evidence suggestions, but does not select a QA specialist route or satisfy the required routing and handoff structure.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- assertion_2: missing explicit environment-instructions and concrete test-command context requirements.
- specialist_gate_pointer: missing authoritative E2E memory, credential, execution-entry, and blocked-condition gate pointers.
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

# Eval Result: eval-001-route-mixed-qa-request

## Evaluation Target

- Agent: `qa`
- Skill: `qa-agent`
- Eval: `eval-001-route-mixed-qa-request`
- Test case: route-mixed-qa-request
- Workspace: `workspace/eval-1-route-mixed-qa-request`
- Natural user prompt:

> 用户说：这个登录重构已经按 docs/pm/login-refresh/PRD.md 实现了，但 CI 里有一个 intermittent 失败，同时 PM 想知道是否可以进入验收。请处理这个 QA 请求。

- Expected artifact: QA 路由决策，明确选择最窄的下游 QA skill、选择理由、需要读取的上下文和预期 evidence artifact

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/qa-agent--eval-001-route-mixed-qa-request/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `483b12548bcebdb174340d9db79ae8cf525be3c084f49f4d2adec731730ab5bc`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **FAIL**（PASS 0 / FAIL 5 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>路由选择 | FAIL | candidate.md 与 transcript item_2 明确写成“主路由应为 spec-based-tester， 并联动 bug-analyzer”，没有只选择一个主 route，也没有说明该 route 为什么比其他 QA skill 更窄、更适合 evidence outcome。 | FAIL | candidate.md 没有选择 spec-based-tester、exploratory-tester、bug-analyzer 或 regression-suite 中的主 route，也没有比较适配性。 |
| `assertion_2`<br>上下文传递 | FAIL | candidate 只列出 PRD、TEST_SUITE 和 CI log；未列出实现变更、TRD/环境说明和测试命令。虽然 transcript item_3 实际读取了这些文件，但输出没有完整传递下游所需上下文。 | FAIL | candidate 没有完整列出 PM/spec、实现变更、CI 信息、环境说明和测试命令；transcript item_2 读取了相关文档，但 item_5 仅输出无 package.json，未形成完整下游上下文清单。 |
| `specialist_gate_pointer`<br>Specialist 权威门禁指针 | FAIL | candidate 没有声明选中的单一 specialist，也没有指出其权威 E2E memory、platform version、credential、execution entry、PRD/TRD/implementation plan 与 blocked-condition 门禁适用；仅泛称“启用相应 QA specialist”。 | FAIL | baseline 没有路由 specialist，也没有任何 required specialist gate pointer。 |
| `assertion_4`<br>结构化产物 | FAIL | candidate 只列出三项后续结果（路径证据、失败复现/根因/回归、可验收结论），没有声明 requirement matrix、execution path、evidence references、risk notes 或 defect handoff notes 等结构化 artifact 结构。 | FAIL | candidate 仅给出 No-Go 和建议，没有声明结构化预期 artifact。 |
| `assertion_5`<br>边界控制 | FAIL | CI fixture 已触发该边界条件。candidate/transcript item_2 明确提出同时联动两个下游 skill；这违反“不能同时执行多个下游 skill”。虽未把 CI 直接写成 confirmed bug，但仍不足以抵消并行路由违规。 | PASS | baseline 没有同时执行或并联多个下游 skill，也没有把 intermittent CI 直接定性为 confirmed bug；其结论是先确认等待条件、重跑并补证据。 |

## With-Skill Behavior

with_skill 未满足路由器要求：同时列出 spec-based-tester 与 bug-analyzer，且缺少 specialist 权威门禁指针、完整上下文清单和结构化 artifact 说明。快照与 transcript 证实没有执行下游 specialist。

## Fresh Without-Skill Baseline

without_skill 未完成 QA 路由输出，但其边界结论未把 intermittent CI 直接定性为 confirmed bug。两条 lane 的最终快照文件树、文件内容及 fixture 哈希完全一致。

## Failures

- with_skill 的 assertion_1：选择了两个下游方向，且未说明单一主 route 相对其他 route 的窄适配理由。
- with_skill 的 assertion_2：未完整传递实现变更、环境说明和测试命令等下游上下文。
- 两条 lane 的 specialist_gate_pointer 均缺失权威门禁指针。
- 两条 lane 的 assertion_4 均未声明结构化 evidence artifact。
- with_skill 的 assertion_5：明确并联 spec-based-tester 与 bug-analyzer。

## Not Exercised

- 无。

## Next Steps

- 将主 route 明确限定为 spec-based-tester；把 CI intermittent 作为 risk note 或后续 handoff，不并行执行 bug-analyzer。
- 补充下游读取清单：PRD/spec、TRD、implementation changes、CI log、平台/环境说明和 npm test -- login；不得预设固定端口或浏览器。
- 加入 specialist 权威门禁指针，并声明 requirement matrix、execution path、evidence references、risk notes/defect handoff 等 artifact 结构。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
