# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-014-mapped-session-plan-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927` from `agents/engineer/test/feature-implementor/evals/workspace/eval-014-mapped-session-plan-evidence`.
- Fixture SHA-256: `ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927`
- Prompt SHA-256: `2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5a3403ec360f8aca06dd1301fa3bfe0f2bd967f54afc7bad9b5691a78697b0ca`
- Skill overlay SHA-256: `5c74cbf7ab5eef845bc8c3f0d81a775b1feca5810a9a615f9b35865026f3e841`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `51a5d5a4f671b1df617b81a97fb84c601259cd9a8d3901d74d7d41b70d44d966`
- Metadata SHA-256: `85958a0c5140b007348a2041b6f7a9c97d73f65f93f4fafa12ba3e42d03d7a13`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | With-skill output and raw evidence show the mapped document and config, but provide no access/order trace proving the change-map was used first or that full-document traversal was avoided. |
| `verifies_against_code` | FAIL | The 30-minute config value and 60-minute document discrepancy are reflected in the output and diff, but there is no plan or evidence that the discrepancy's impact was incorporated into a plan. |
| `treats_unverified_as_low_trust` | NOT_EXERCISED | The output resolves the 60-minute documentation discrepancy in favor of the 30-minute config and notes no test framework, but does not establish that unverified documentation was explicitly treated as lowest trust or that all scope judgments were verified. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=e1f90c50ec385dd13119d5a5870340d5184e469277b163d5255b69dd575b89d7; snapshot_sha256=b1fbfc1f2d9143b1a8ccf4d98655cc1caec58885595501f78c84379c331a8897
- Behavior: Implemented renewal, reconciled the documentation to the 30-minute config, and reported consistency validation; process assertions are not fully evidenced.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2f129ddb28e1f1e80d9edd6a2ff9482f3bf6168c9099228d14be2ebcaee2b61a; fixture_sha256=ebf98490e96d51646bb08c2897d26dd073cad98267ddc69d86f17d77581f2927; output_sha256=588f64a9e4d36b2c94eee5d94487bf33f9911c503ce75f3450a7c533f47f3c16; snapshot_sha256=0c4505e88fc23552662559dd8d2ca97f6f7d01e3dc764b584f56418a23d875d2
- Behavior: Implemented the same config and documentation changes, without evidence of mapped-document-first review or trust handling.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- verifies_against_code is not fully satisfied because the discrepancy was corrected but its impact was not shown as incorporated into a plan.なく
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

# Eval Result: eval-014-mapped-session-plan-evidence

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-014-mapped-session-plan-evidence`
- Test case: mapped-session-plan-evidence
- Workspace: `workspace/eval-014-mapped-session-plan-evidence`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 请为 `src/session/` 增加会话续期，并先核对当前超时行为。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `reads_mapped_docs_first`: Transcript item_4 reads change-map.yaml, then mapped docs/site/api/session.md and src/session/config.txt; no full site-document traversal is evidenced.
- PASS `verifies_against_code`: Transcript and final identify config.txt as 30 minutes with renewal disabled, contrast it with the document's 60 minutes, and retain the conflict as an implementation blocker. With-skill workspace hashes match input hashes.
- PASS `treats_unverified_as_low_trust`: Both mapping and API documents state last_verified_version: unverified; the agent relies on config/code evidence, reports the discrepancy, and does not implement based on the document alone.

## With Skill Behavior

按映射读取 API 文档并回读代码配置，识别 30/60 分钟冲突；因缺少 PM/TRD 链未实施或写入计划。workspace 未变更，hash 与输入一致。

## Without Skill Baseline

未使用映射消费协议，直接修改 config.txt 与 API 文档，启用 renewal 并统一为 30 分钟；output hash 反映两文件变更。

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

- Skill: `feature-implementor`
- Eval: `eval-014-mapped-session-plan-evidence`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

**PASS** — with-skill 以代码事实（30 分钟、续期禁用）核证出文档 60 分钟声明的分歧，PRD/TRD 前置门禁正确触发暂停，未在预期未对齐时编写实施计划。

## With-Skill Behavior

- 命中映射文档后回代码核证会话行为，结构化区分代码事实与文档声明。
- 变更按 standard 分级，正确停在 PM → trd-gen → 实施计划的协作链前置，未越权编码。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 同样停在门禁前请求预期确认，行为合规但对文档分歧的证据组织与契约引用较弱。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
