# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-005-mapped-cache-debug-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d` from `agents/engineer/test/debugger/evals/workspace/eval-005-mapped-cache-debug-evidence`.
- Fixture SHA-256: `5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d`
- Prompt SHA-256: `f67ee52e742cb8b8fa4a2e4a8def50688400c24b6328050c434ae918f3f4101b`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `dcc41028443385df7286f016738f0aaf1f647d06f9da1ee3865bedd33c344afe`
- Skill overlay SHA-256: `267ff29e20f38caffb753a87229899be929d0e39edb8d8216c48698de2a99ab6`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `793c3f5cce4575964aaa387ece63f94a0f71e528641010e1ee2d932bd04007a8`
- Metadata SHA-256: `296cf62658138bf9e31e0fd2b92d8abed954cf84bd5c6bd08af68865f72fdfc1`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | With-skill output cites docs/site/api/cache.md, the change-map target for src/cache/**, and no unrelated documentation. |
| `verifies_against_code` | PASS | It cites src/cache/ttl.txt with ttl_seconds: 60, contrasts it with the documented 300 seconds, and identifies the configuration/documentation mismatch. |
| `treats_unverified_as_low_trust` | FAIL | It notes last_verified_version: unverified, but does not explicitly treat the document as the lowest-trust source; it still frames the 300-second statement as the API contract and basis for the mismatch. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f67ee52e742cb8b8fa4a2e4a8def50688400c24b6328050c434ae918f3f4101b; fixture_sha256=5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d; output_sha256=458a99ebda8c04d87b26cf6361d4278d4f9f6450476539ead48f39864c3c3cb7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Used the mapped documentation and code evidence, clearly distinguished configuration-level from runtime reproduction, and noted unverified documentation, but did not explicitly apply lowest-trust treatment.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f67ee52e742cb8b8fa4a2e4a8def50688400c24b6328050c434ae918f3f4101b; fixture_sha256=5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d; output_sha256=2a8cc7a05620605b221eb31d314db8de789f2a9596d47c3474fa762bb1ba4330; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identified the 60-second configuration and 300-second documentation discrepancy, but did not mention the change-map or unverified trust status.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output does not explicitly treat last_verified_version: unverified as the lowest-trust evidence or clearly state that its reproduction and root-cause judgment do not depend on the unverified documentation claim.
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

# Eval Result: eval-005-mapped-cache-debug-evidence

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-005-mapped-cache-debug-evidence`
- Test case: mapped-cache-debug-evidence
- Workspace: `workspace/eval-005-mapped-cache-debug-evidence`
- Evaluation date: 2026-08-07
- Overall result: PASS (partial coverage)
- Behavior result: PASS
- Coverage result: PARTIAL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 请诊断 `src/cache/` 中缓存比预期更早过期的问题，并说明复现依据和根因。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `reads_mapped_docs_first`: transcript item_2 先读取 change-map.yaml，再读取命中的 docs/site/api/cache.md，并未遍历无关文档。
- PASS `verifies_against_code`: final 明确记录 src/cache/ttl.txt 为 60 秒、API 文档声明 300 秒，并报告 240 秒分歧及静态复现限制。
- NOT EXERCISED `treats_unverified_as_low_trust`: 虽读取到 last_verified_version: unverified，final 未明确将其作为最低信任处理。

## With Skill Behavior

按映射读取 API 文档并回到 ttl.txt 核证，正确报告 60 秒与 300 秒分歧；未明确报告 unverified 的最低信任级别。

## Without Skill Baseline

读取并报告了 ttl.txt 与 API 文档的静态分歧，但未按 change-map 流程提供同等的信任模型证据。

## Failures / Findings

- None.
- Root cause: with_skill 输出遗漏了对 last_verified_version: unverified 应按最低信任处理的明确说明。

## Next Steps

- 增加可触发 NOT EXERCISED 分支的 fixture 后重跑；当前已触发路径没有行为失败。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-005-mapped-cache-debug-evidence

## Evaluation Target

- Agent: `engineer`
- Skill: `debugger`
- Eval: `eval-005-mapped-cache-debug-evidence`
- Workspace: `workspace/eval-005-mapped-cache-debug-evidence`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture：`ws1-consumption-v1`
- 日期：2026-07-30
- Fresh run：`tmp/eval-runs/issue-196-l2-2-debugger-20260730-220643/`
- paired candidates 均为本轮隔离新生成。

## Assertion Results

- PASS `reads_mapped_docs_first`：根据 `src/cache/**` 的 change-map 精准读取 `docs/site/api/cache.md`，未遍历无关文档。
- PASS `verifies_against_code`：以 `src/cache/ttl.txt` 核证实现为 fixed 60 秒，并结构化对照文档 300 秒。
- PASS `treats_unverified_as_low_trust`：明确 `last_verified_version: unverified` 为最低信任，不能单独建立批准预期。

## With-Skill Behavior

候选使用映射文档定位、代码事实定性，确认 60/300 秒分歧，同时把“应修代码还是文档”停在 `missing_docs` 的预期对齐边界。

## Without-Skill Baseline

来源为本轮隔离子代理使用相同 prompt 与 fixture 生成，未接触 skill、Engineer README 或 with-skill。baseline 同样精准读取映射文档、以代码核证 TTL，并明确 unverified 最低信任，满足 3/3 assertions。

## Failures

- With-skill：无。
- Baseline：无；本轮没有 assertion 级行为差异。

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Next Steps

保留映射消费与低信任文档覆盖；如需测量 skill 增益，可加入无关文档干扰或移除 prompt 中的明确诊断导向。

## Runtime Artifact Policy

候选、verdict 和诊断只存放于 ignored runtime 目录，不提交；本文件是 durable 结果。
