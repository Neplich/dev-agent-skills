# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `test-writer`
- Eval: `eval-002-mapped-pagination-tests`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d` from `agents/engineer/test/test-writer/evals/workspace/eval-002-mapped-pagination-tests`.
- Fixture SHA-256: `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d`
- Prompt SHA-256: `868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `044621ea5e06de080877cb29e7795dc6b010bafa03f5ae20c49efdc9791d4cb1`
- Skill overlay SHA-256: `4783dfb3f1f07cb9b7807b31a1f84259200dc0c5fa863343b23c167911863dfb`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dffdc1de9650924aeba7f48471eac1b4c1592e52cef441419d14a463af648ff5`
- Metadata SHA-256: `6a60b69beab2bdd4c854670cd54e7749219cde65551c8e29d984d322f4c34c88`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | The with_skill output reports the mapped pagination documentation discrepancy, but provides no evidence of read order or that unrelated documentation was not scanned. |
| `verifies_against_code` | PASS | The with_skill output reports default_page_size 25 and maximum 100, notes the documentation says 50, and its test asserts 25. |
| `treats_unverified_as_low_trust` | PASS | The documentation is marked last_verified_version: unverified; with_skill leaves it unchanged, reports the 50/25 discrepancy, and hardcodes the code-verified expectation 25 in tests. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=9ae3242581aae251ac946ae102b809b8972de46e97e9b91a6e4a63e2c734a611; snapshot_sha256=60b93ef696dae1b34685ec69c1ac829fdd910863d2037c32c1d05c0a9ea5198c
- Behavior: Added passing boundary tests based on code value 25, retained the unverified documentation unchanged, and reported its inconsistency.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=68a35e6f243585d8a0a8ea388354818be95b19b70a0cd00dc8439a6dd91e1414; snapshot_sha256=f04bf742829afe6c693f16465f3d3821ae24afb1e2fc17f0d44e412942fd449b
- Behavior: Reported the code value 25 and changed the unverified documentation from 50 to 25 while adding tests.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Capture tool/read trace or explicit workflow evidence showing change-map resolution followed by reading docs/site/api/pagination.md before any unrelated documentation.

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

# Eval Result: eval-002-mapped-pagination-tests

## Evaluation Target

- Agent: `engineer`
- Skill: `test-writer`
- Eval: `eval-002-mapped-pagination-tests`
- Test case: mapped-pagination-tests
- Workspace: `workspace/eval-002-mapped-pagination-tests`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 请为 `src/pagination/` 的边界行为设计并编写测试，先核对当前默认页大小。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `reads_mapped_docs_first`: transcript item_2 先读取 change-map.yaml，随后读取 docs/site/api/pagination.md；未读取无关文档内容。
- PASS `verifies_against_code`: transcript item_2/item_3 读取并确认 src/pagination/defaults.txt 为 25，识别文档 50 的冲突；最终测试断言默认值为 25。
- PASS `treats_unverified_as_low_trust`: transcript item_2 读取消费契约及文档中的 last_verified_version: unverified；最终以代码值 25 而非文档值 50 编写测试。

## With Skill Behavior

final 报告默认值 25、最大值 100，新增 4 项测试并报告 4/4 通过。workspace 测试文件与 output.sha256 内容一致，exit_code 为 0。

## Without Skill Baseline

作为对照，without_skill 也读取了代码和文档并生成边界测试；不影响 with_skill 判定。

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

# Consumption Regression Comparison

## Evaluation Target

- Skill: `test-writer`
- Eval: `eval-002-mapped-pagination-tests`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

**PASS** — with-skill 以代码事实 25 为测试基准，拒绝采用 unverified 文档声明的 50，且不臆造缺失运行时的边界行为测试。

## With-Skill Behavior

- 命中映射文档后核证默认值，测试锚定代码事实并显式记录文档不一致。
- 对无实现证据的边界行为（0、101 的截断/报错）明确不臆造，保持证据边界。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 停在'以哪个值为准'的询问上未产出测试；行为稳妥但未按契约以代码为 ground truth 直接推进可交付产物。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
