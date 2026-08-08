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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c794a9f4d25d61e50b6bf610eddf7b88ff4be58b7215ed85d280d6be8cae915f`
- Skill overlay SHA-256: `ee5b521f7d9c6fe11867036a027efeb03a84b77600d52fa7396a529de342ee2e`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `793c3f5cce4575964aaa387ece63f94a0f71e528641010e1ee2d932bd04007a8`
- Metadata SHA-256: `296cf62658138bf9e31e0fd2b92d8abed954cf84bd5c6bd08af68865f72fdfc1`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | With_skill 输出引用了映射命中的文档，但锁定证据无法证明先读 change-map 或未遍历无关文档。 |
| `verifies_against_code` | PASS | 明确报告 src/cache/ttl.txt 的 ttl_seconds 为 60、expiry_mode 为 fixed，并与文档声明的 300 秒对照，结构化说明 240 秒提前过期及证据限制。 |
| `treats_unverified_as_low_trust` | FAIL | 虽指出文档为 unverified 并要求补齐正式期望，但未明确按最低信任处理，且其偏差结论仍直接依赖未经代码验证的 300 秒文档声明。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f67ee52e742cb8b8fa4a2e4a8def50688400c24b6328050c434ae918f3f4101b; fixture_sha256=5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d; output_sha256=22d9b0234c5d0f27d28780803eecba6b9c7bbc47c6add1a39a9acc8585111d16; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核对配置与文档并报告差异，但未满足最低信任及不依赖未验证文档声明的要求；读取顺序无法由证据确认。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f67ee52e742cb8b8fa4a2e4a8def50688400c24b6328050c434ae918f3f4101b; fixture_sha256=5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d; output_sha256=a82dddca138231c5e3372e7c363184b4a5c99555e1d459b36f04b0edc67172ca; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别 60 秒配置与 300 秒文档声明的差异，并指出文档未验证；未提供可证明的 change-map 读取顺序。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确将 last_verified_version: unverified 作为最低信任，并且根因判断依赖该文档的 300 秒声明。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4d48049390ab002df61765af74d4475aee31c5bcd9182a3c09d089676dc5c67c`
- Skill overlay SHA-256: `900f3a9f7889564aa652e55c72206132dc4b2c69166314535fb3c79893f86eba`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `793c3f5cce4575964aaa387ece63f94a0f71e528641010e1ee2d932bd04007a8`
- Metadata SHA-256: `296cf62658138bf9e31e0fd2b92d8abed954cf84bd5c6bd08af68865f72fdfc1`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | with_skill 提到了 docs/site/api/cache.md，但未说明读取 change-map 或证明按映射优先读取；仅凭输出和原始证据无法确认读取顺序。 |
| `verifies_against_code` | PASS | 明确引用 src/cache/ttl.txt 的 ttl_seconds: 60，并与文档声明的 300 秒对照，计算提前 240 秒，且将根因归为配置/契约漂移。 |
| `treats_unverified_as_low_trust` | FAIL | with_skill 未提及文档 front matter 中的 last_verified_version: unverified，也未明确将该文档声明视为最低信任或说明根因判断不依赖未经验证的文档。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f67ee52e742cb8b8fa4a2e4a8def50688400c24b6328050c434ae918f3f4101b; fixture_sha256=5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d; output_sha256=8e0f168539689a2991a47c8fafad4a3b2a2655de39a14c5e6fd4e3e332e9eaea; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核对 TTL 配置与文档并给出具体复现时点和根因，但未证明映射文档优先读取，也未处理 unverified 文档信任问题。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f67ee52e742cb8b8fa4a2e4a8def50688400c24b6328050c434ae918f3f4101b; fixture_sha256=5265284c4bc9506c9aff21630151842110054255967ea23b3c9669fa67c6063d; output_sha256=6050593f87dcd94d0c29251f39690f82ca576219192ee8770408ce418a5d4818; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别 60 秒配置与 300 秒文档预期的差异并给出复现区间，但未证明通过 change-map 优先读取，也未处理 unverified 信任等级。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 reads_mapped_docs_first。
- with_skill 未满足 treats_unverified_as_low_trust。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

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
