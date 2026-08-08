# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-005-mapped-upload-trd-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007` from `agents/engineer/test/trd-gen/evals/workspace/eval-005-mapped-upload-trd-evidence`.
- Fixture SHA-256: `b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007`
- Prompt SHA-256: `415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b66f9acea93e151819a21f82909f9a6b7d44c68fa52d2116667525e2fe8e9bd7`
- Skill overlay SHA-256: `e4cc003a0e06320ef354c6c9cdbebb2b75980ec8b23ae530ac78b0667fab31da`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ed02404d14ffd40d542c29f44a74caf2fc5696740b01f75b11e50dfad6379f60`
- Metadata SHA-256: `cfc84017a2f6130d5f5d58c0d09338a6a3beaaf2ead3e34eb6d3229566da0300`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill identifies and uses docs/site/api/upload.md and cites change-map.yaml as the source requiring that document; its evidence is limited to the mapped API document and src/upload/limits.txt. |
| `verifies_against_code` | PASS | with_skill reports limits.txt as maximum_upload_mb: 10, contrasts it with the API document's 20 MB statement, preserves the conflict in the current-conclusion table, and flags resolving the limit as a prerequisite. |
| `treats_unverified_as_low_trust` | PASS | with_skill explicitly records last_verified_version: unverified and concludes that only declared behavior is known, leaving the actual limit and HTTP contract undetermined rather than relying on the document. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888; fixture_sha256=b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007; output_sha256=521626a02ba0097355b111893a8f0f9929a5af6678d935f71743833b4a2a54e9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Explicitly connected the task location to the mapped API document, verified it against limits.txt, retained the discrepancy and impact, and treated the unverified document as low trust.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888; fixture_sha256=b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007; output_sha256=4d3ddb0223c0be3931a799d5650e1abbc499edae07d6bff76d83180b6e6b780f; snapshot_sha256=09275c1140622f4c2b8e444654e5cb6b3508d8b27c7fbe56fae363e9ef95f8be
- Behavior: Produced a proposal and noticed the 10 MB versus 20 MB conflict, but stated the mapped-document and unverified-trust handling less explicitly.
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

# Eval Result: eval-005-mapped-upload-trd-evidence

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-005-mapped-upload-trd-evidence`
- Test case: mapped-upload-trd-evidence
- Workspace: `workspace/eval-005-mapped-upload-trd-evidence`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 请为 `src/upload/` 增加分片上传能力准备技术方案，并先确认当前接口行为与技术差距。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- FAIL `reads_mapped_docs_first`: transcript 中先读取 src/upload/limits.txt（item_3），之后才读取 change-map.yaml（item_4）及其命中文档 upload.md（item_7），不满足映射文档优先。
- PASS `verifies_against_code`: final 明确核对 limits.txt 的 10 MB 与 upload.md 的 20 MB，并保留该分歧及其技术影响；workspace 哈希与记录一致。
- PASS `treats_unverified_as_low_trust`: final 明确指出文档版本为 unverified、与代码配置冲突，并称无法据此确认真实运行时接口行为。

## With Skill Behavior

正确发现并记录 10 MB/20 MB 分歧及 unverified 低信任状态，但实际读序未先读取映射文档。

## Without Skill Baseline

作为对照，读取了上传配置、映射文档和 API 页面，并输出了分歧与技术差距；不影响 with_skill 判定。

## Failures / Findings

- reads_mapped_docs_first 未通过：代码证据读取发生在 change-map 和命中文档之前。
- Root cause: with_skill transcript 明确显示先读取 src/upload/limits.txt，后读取 change-map.yaml 与 docs/site/api/upload.md，违反“映射文档优先”的断言。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

# Consumption Regression Comparison

## Evaluation Target

- Skill: `trd-gen`
- Eval: `eval-005-mapped-upload-trd-evidence`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

**PASS** — with-skill 以接口证据核查发现代码 10 MB 与文档 20 MB 的上限冲突，按 gate 停在 PM 决策点补齐产品基线，未带着未验证预期起草 TRD。

## With-Skill Behavior

- 命中映射文档后回代码核证上传上限，识别并结构化列出 10 MB / 20 MB 冲突与待确认契约问题。
- 严格遵守协作链：PM 确认 → TRD → 维护者确认 → 实施计划，未越权产出正式 TRD。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 同样发现冲突并请求基线确认，但对文档采信边界与协作链停点的处理是临场组织，未引用契约协议。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
