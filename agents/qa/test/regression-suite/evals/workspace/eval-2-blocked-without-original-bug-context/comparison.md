# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-002-blocked-without-original-bug-context`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5` from `agents/qa/test/regression-suite/evals/workspace/eval-2-blocked-without-original-bug-context`.
- Fixture SHA-256: `811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5`
- Prompt SHA-256: `261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `850108c3e4722feb1b9e0417b1554f0fb5b41d47001505d7da16c6bcd9946093`
- Skill overlay SHA-256: `3af177f0dcd9723964fdbcbf144832d8c6b68b267a850af3da918d86fe27d617`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `bde407cd9167fc95a8a68436fa7745a88790341ccffae265b6e1321da5b3938f`
- Metadata SHA-256: `e69dc8ec803ebfc43eb2e4147f1b861f4b02e94afa256d86c039101ea44fff1b`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 明确指出缺少原始缺陷记录、复现/失败证据、修复提交或变更说明，以及测试环境和版本信息。 |
| `blocked` | FAIL | 仅声明总体状态为 blocked，未分别将 original failure recheck、fixed behavior、adjacent regression checks、平台版本确认及 PRD/TRD 对齐标记为 blocked 或 not executed。 |
| `assertion_3` | FAIL | 未以输出字段或清晰分节完整包含 original failure recheck、fixed behavior、adjacent regression checks、release recommendation 和 evidence confidence。 |
| `assertion_4` | FAIL | 虽表示不能得出可发布结论，但未明确给出 release recommendation 为 needs more verification 或 blocked。 |
| `no_unknown_or_unscoped_release` | PASS | 未使用 unknown 作为结论或将局部回归当作全量 E2E，并列出了版本、环境、原始 bug、修复证据及相关验证材料的补充要求。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=22f34b11dca71abdc089dde4c4f44863a85714fd099545e42de564bead900c8e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别材料不足并总体标记 blocked，补充了 PRD/TRD/实施计划和邻近场景要求，但未完整输出各项结构化回归状态、发布建议和证据置信度。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=261f550b35c9a4d84c8303c0abe4a7adbe04fbf62131aadd694155952d4db10d; fixture_sha256=811b93327e61a4a1610d2801bebd47a27e231fa7f4e1ec17fdfda144fdd986f5; output_sha256=4599e365113a983c9087eac4921d42ed3c180bd5daf7d9360af32409d19d962d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别材料不足并要求补充原始缺陷、修复、版本、环境、测试步骤和回归证据，但未提供结构化 blocked 状态或明确证据置信度。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未分别标记要求的回归维度为 blocked 或 not executed。
- with_skill 未完整提供要求的结构化输出字段。
- with_skill 未明确给出符合限定值的 release recommendation。
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

# Eval Result: eval-002-blocked-without-original-bug-context

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-002-blocked-without-original-bug-context`
- Test case: blocked-without-original-bug-context
- Workspace: `workspace/eval-2-blocked-without-original-bug-context`
- Natural user prompt:

> 复测上周修过的支付按钮问题，但仓库里找不到原始 bug 报告、失败证据、修复 PR 或可用测试环境。请给出回归验证结论。

- Expected artifact: blocked 回归验证报告，说明缺失上下文、无法复核 original failure、不能给 release ready 结论，并列出恢复验证所需证据

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/regression-suite--eval-002-blocked-without-original-bug-context/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `fcb18ed7faddb7313fd51c13f012a7fe051e13a2f764566630a63d003a998d9a`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **FAIL**（PASS 1 / FAIL 4 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `assertion_1`<br>原始证据缺失 | PASS | candidate.md 明确写出缺少 bug 报告、失败证据、修复 PR、变更说明、测试命令和测试环境；transcript 中仅执行了读取/探索命令，最终快照也只有 notes/missing-context.md，因此没有直接执行泛化回归的证据。 | PASS | candidate.md 明确列出缺少原始 Bug 报告、失败证据、修复 PR、测试命令和测试环境；transcript 仅有只读探索命令，快照无测试产物。 |
| `blocked`<br>blocked 状态 | FAIL | 原始失败、修复验证和邻近回归被描述为无法复现/未执行，且 PRD/TRD 对齐不可用；但没有明确标记 platform version confirmation 为 blocked 或 not executed，也未完整逐项给出 fixed behavior、adjacent regression checks 和对齐状态。 | FAIL | 虽然说明无法复测并列出缺失证据，但没有逐项标记 fixed behavior、adjacent regression checks、平台版本确认及 PRD/TRD 对齐为 blocked/not executed；transcript 也只有失败的 git 检查和文件读取。 |
| `assertion_3`<br>结构化输出 | FAIL | candidate.md 使用了语义近似的“原始失败/修复验证/邻近回归/发布建议”，但缺少必需的 evidence confidence 字段，且未完整按 original failure recheck、fixed behavior、adjacent regression checks 等结构化字段输出。 | FAIL | candidate.md 未包含完整的 original failure recheck、fixed behavior、adjacent regression checks、release recommendation 和 evidence confidence 五项结构化输出。 |
| `assertion_4`<br>发布边界 | FAIL | “暂缓放行”语义上表示不放行，但断言规定 release recommendation 必须是 needs more verification 或 blocked；输出没有使用规定取值。 | FAIL | candidate.md 没有 release recommendation 字段，也没有明确给出 needs more verification 或 blocked 作为发布建议。 |
| `no_unknown_or_unscoped_release`<br>不得用 unknown 或误判发版范围 | FAIL | 最终快照没有 unknown 目录或 release 全量测试产物，transcript 也无写入证据；但恢复清单虽包含原始 bug、失败证据、修复 PR、测试环境和执行入口，未明确列出缺失的测试平台版本，因此未满足“版本、环境、原始 bug 和修复证据”完整清单要求。 | FAIL | 最终快照没有 unknown 目录或 release 全量测试产物，transcript 无写入证据；但候选未明确列出测试平台版本，恢复验证所需证据清单不完整。 |

## With-Skill Behavior

with_skill 正确识别上下文缺失并阻塞回归，但未完整满足结构化字段、平台版本状态和规定的 release recommendation 取值要求。最终快照仅有 notes/missing-context.md，且 transcript 仅显示读取命令，无写入或测试执行证据。

## Fresh Without-Skill Baseline

without_skill 同样识别了缺失上下文，但缺少更多必需的结构化状态与发布建议字段；仅作为 baseline 对照，不影响当前结果。两条 lane 的最终快照树、文件内容、SHA-256 和大小均一致，符合 fixture-manifest。

## Failures

- with_skill 的 blocked 断言未明确覆盖 platform version confirmation，且未逐项完整标记所有要求的检查状态。
- with_skill 缺少 evidence confidence，结构化输出字段不完整。
- with_skill 使用“暂缓放行”而非规定的 needs more verification 或 blocked。
- 两条 lane 均未在恢复验证清单中明确列出平台版本。

## Not Exercised

- 无。

## Next Steps

- 补充逐项结构化状态：original failure recheck、fixed behavior、adjacent regression checks、platform version confirmation、PRD/TRD alignment，均标为 blocked 或 not executed。
- 增加 evidence confidence 及简短依据。
- 将 release recommendation 明确写为 blocked 或 needs more verification，并列出平台版本、测试环境、原始 bug/失败证据、修复 PR/提交及预期行为。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
