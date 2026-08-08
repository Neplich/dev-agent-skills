# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-003-mapped-search-architecture`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859` from `agents/engineer/test/codebase-analyzer/evals/workspace/eval-003-mapped-search-architecture`.
- Fixture SHA-256: `a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859`
- Prompt SHA-256: `0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4f1332611648af165a59b99f871678f4c900534d4d5d1fcedda6f815a3b3d5ed`
- Skill overlay SHA-256: `de5de93c0f76ae4be6410327fbb42d3bdbd9dfa29aa0e5edc91c3ed04528aee5`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `df0ea3b9e16f84cfa3123784feaff62e9978d327069fdb7ff40819c75c9ebde1`
- Metadata SHA-256: `c79f8b60b8eda49d60383374b0b105b8c506dcb4b757a67593ed9721a0d169df`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_change_map_to_bound_context` | PASS | with_skill 明确引用 change-map.yaml，将 src/search/** 映射到 docs/site/api/search.md，并将分析范围限定在搜索模块相关文档。 |
| `verifies_claims_against_code` | PASS | with_skill 直接引用 src/search/query.txt，核验 entrypoint: search 与 match_mode: exact，并据此限制能力结论。 |
| `reports_document_code_conflict` | PASS | with_skill 清楚对比文档默认 fuzzy matching 与代码 exact 配置，指出当前应按代码侧证据判断，并将其列为后续改造需确认的风险。 |
| `does_not_overclaim_unverified_docs` | PASS | with_skill 识别 last_verified_version: unverified，明确文档未被实现验证；将 fuzzy matching 作为文档声明而非当前事实，并对运行时能力保持保守表述。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c; fixture_sha256=a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859; output_sha256=94d2ec4e111642996ba09fdc34dd8b4c3fcec8fa09ed6df52a6df98aa600cfd5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 按 PM handoff 与 change map 限定范围，回到 query.txt 核验代码事实，报告文档冲突，并避免将未验证文档声明当作已证实能力。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c; fixture_sha256=a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859; output_sha256=ad44e78eab353b49102de2cd9d455640593f9eab4424a2f3644bda9e008a67fa; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 能基本依据代码识别 exact 配置和文档冲突，但未充分体现由 change map 约束上下文及未验证文档的信任降级。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-003-mapped-search-architecture`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859` from `agents/engineer/test/codebase-analyzer/evals/workspace/eval-003-mapped-search-architecture`.
- Fixture SHA-256: `a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859`
- Prompt SHA-256: `0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4f1332611648af165a59b99f871678f4c900534d4d5d1fcedda6f815a3b3d5ed`
- Skill overlay SHA-256: `de5de93c0f76ae4be6410327fbb42d3bdbd9dfa29aa0e5edc91c3ed04528aee5`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `df0ea3b9e16f84cfa3123784feaff62e9978d327069fdb7ff40819c75c9ebde1`
- Metadata SHA-256: `c79f8b60b8eda49d60383374b0b105b8c506dcb4b757a67593ed9721a0d169df`
- Executor SHA-256: `c5ece8c6632badb84ff79ee67e4bea96a1d1db7e8afd66de87486af43e8fdd16`
- Runtime SHA-256: `5c4532cfa9ada91c16b3ae2d69922296ddc7c2c1c61841e01bc9c804be1b85fe`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_change_map_to_bound_context` | PASS | with_skill 明确引用 change map 指向 docs/site/api/search.md，并将分析限定在 src/search/ 及其关联文档范围内。 |
| `verifies_claims_against_code` | PASS | with_skill 直接以 src/search/query.txt 中的 entrypoint: search 和 match_mode: exact 核验入口及匹配模式，并明确指出缺少实际处理代码。 |
| `reports_document_code_conflict` | PASS | with_skill 清楚对比文档的 fuzzy matching 声明与代码的 exact 声明，并说明该冲突使 fuzzy 不能作为当前能力，且构成后续改造的不确定点。 |
| `does_not_overclaim_unverified_docs` | PASS | with_skill 识别文档和 change map 的 last_verified_version: unverified，并将未经代码验证的 fuzzy matching 降级为文档声明而非当前事实。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c; fixture_sha256=a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 限定了 change-map 文档范围，回到 query.txt 核验代码事实，准确报告 exact 与 fuzzy 冲突，并避免采信未验证文档结论。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0f34452462bbb10e7f7328b054a3e1b0e6f741b40ba12100a356dcedfa512f9c; fixture_sha256=a3ef5b9cc00c15c74b103c208a46d73ff5b53e17721ec0a79184a10c02b16859; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 已较完整地依据代码和文档进行证据化分析，并识别 exact/fuzzy 冲突及 unverified 状态。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
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

# Eval Result: eval-003-mapped-search-architecture

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-003-mapped-search-architecture`
- Test case: mapped-search-architecture
- Workspace: `workspace/eval-003-mapped-search-architecture`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 请分析 `src/search/` 的模块职责、请求流程和当前接口能力。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `reads_mapped_docs_first`: with_skill transcript 中 item_2 先读取 agents/.../consumption-contract.md，再读取 docs/site/api/search.md；未满足命中 change-map 后首先读取映射 API 文档。
- PASS `verifies_against_code`: transcript item_2/item_4 实际读取并核查 src/search/query.txt；final.md 明确指出文档默认 fuzzy 与代码 match_mode: exact 的分歧及其影响（应以代码为准、文档需校准）。
- PASS `treats_unverified_as_low_trust`: 实际 docs/site/api/search.md 与 change-map.yaml 均含 last_verified_version: unverified；final.md 按最低信任处理文档，并以 query.txt 的代码事实核证职责、流程和能力。

## With Skill Behavior

with_skill 实际读取了 change-map、映射 API 文档和代码，并正确报告 fuzzy/exact 冲突；但命中 change-map 后先读取了 shared consumption-contract，未满足映射文档优先顺序。workspace hashes 与 input/output hashes 一致，未发生文件写入。

## Without Skill Baseline

without_skill 在同一 fixture 上读取了代码、API 文档和 change-map，最终也识别出 unverified 文档与 exact 代码的冲突；仅作为 baseline 对照，不影响单独 assertion 判定。其 workspace input/output hashes 一致，未发生文件写入。

## Failures / Findings

- reads_mapped_docs_first
- Root cause: with_skill 在确认 change-map 后先读取 shared consumption-contract 而非映射的 docs/site/api/search.md，导致文档优先读取断言失败。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

# Consumption Regression Comparison

## Evaluation Target

- Skill: `codebase-analyzer`
- Eval: `eval-003-mapped-search-architecture`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

**PASS** — with-skill 输出满足全部 3 条断言：命中 change-map 后以映射文档 `docs/site/api/search.md` 为地图、以 `src/search/query.txt` 为 ground truth 核证出"文档声称模糊匹配、代码只实现精确匹配"的分歧，并按 `unverified` 最低信任规则以代码为准。

## With-Skill Behavior

- 显式声明按 consumption contract 执行，只读取命中的映射文档，未做无关文档遍历。
- 产出契约要求的结构化分歧表（文档路径 / 文档声明 / 代码事实 / 影响），可直接供 `docs-audit` 消费。
- 对 `last_verified_version: unverified` 显式引用最低信任规则，全部关键能力结论以代码证据支撑，未证实项明确标注"无法确认"。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 也识别了模糊/精确匹配分歧并倾向以代码为准，但没有产出契约格式的结构化分歧证据，信任降级是临场推断而非协议行为。

## Failures

- 无。

## Next Steps

- 保留本结果；后续可在 fixture 中加入多个无关文档以放大"精准读取"与全库遍历的行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
