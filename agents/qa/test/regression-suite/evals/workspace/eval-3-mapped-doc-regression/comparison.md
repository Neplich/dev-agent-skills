# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-003-mapped-doc-regression`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94` from `agents/qa/test/regression-suite/evals/workspace/eval-3-mapped-doc-regression`.
- Fixture SHA-256: `b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94`
- Prompt SHA-256: `ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `93e5fd0d6baa599b41823d84d9e76df4ae1d287d1ee0dc585a0fbe0d3c54e8d5`
- Skill overlay SHA-256: `e9706a0f5c60f10753664f62398d5e5d1b2198510bb7a2bd63d1c64e17ebc61f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e133160262ed184852d28136da76d373bddc3830b084351e43f62baba3d14a43`
- Metadata SHA-256: `8f1420b83ef9d543d57a760ebba7fc169b9c3d2172e7b3b1e191d47cfe76b856`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | The output references the mapped API document and change map, but locked raw evidence cannot prove document read order. |
| `verifies_against_code` | PASS | It confirms the code threshold is 3, the document says 2, records the discrepancy, and identifies the rule, search-entry, and documentation impact paths. |
| `treats_unverified_as_low_trust` | PASS | It identifies last_verified_version as unverified and states that final judgment should rely on code and runtime results, while marking execution blocked. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b; fixture_sha256=b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94; output_sha256=70983e161f7a3b23070d86c2d3781ef2d09c214a7fec034581ea5ce1c48d2d1f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly verifies the mismatch, defines focused regression paths, and treats unverified documentation as low trust while distinguishing scope from execution status.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b; fixture_sha256=b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94; output_sha256=330516c8344e6374558e4a704d73c2d1e1ab4945c9dec68e8120059bb4dabc4f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly reports the code/document threshold mismatch and proposes boundary coverage, but treats the document as the alignment target without addressing its unverified status.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-003-mapped-doc-regression`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94` from `agents/qa/test/regression-suite/evals/workspace/eval-3-mapped-doc-regression`.
- Fixture SHA-256: `b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94`
- Prompt SHA-256: `ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e0bb997f7c8683c58b155379f15e9833f91e4d2f51aece7bfcfa4974d6a1defb`
- Skill overlay SHA-256: `5380fc16efa2deba2f3d503697de616d07aef499ace1b8bbfa59e73c1e19fe13`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e133160262ed184852d28136da76d373bddc3830b084351e43f62baba3d14a43`
- Metadata SHA-256: `8f1420b83ef9d543d57a760ebba7fc169b9c3d2172e7b3b1e191d47cfe76b856`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill identifies the change map and the mapped API document, and limits direct impact to the mapped documentation and query rule path. |
| `verifies_against_code` | PASS | It confirms code threshold 3 versus documented threshold 2, treats code as authoritative, records the discrepancy, and lists direct regression paths. |
| `treats_unverified_as_low_trust` | PASS | It notes both documents are unverified, bases conclusions on code, expands verification to tests/QA, and explicitly avoids claiming regression execution is complete. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b; fixture_sha256=b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94; output_sha256=662ecf99ddd63dd85c23a5375edcdb80c73e132a8bcce586f102f716a8ca7bce; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Verified the threshold against code, identified the mapped documentation discrepancy and direct paths, treated unverified documentation as low trust, and limited claims to proposed scope rather than completed execution.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b; fixture_sha256=b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94; output_sha256=b397605e3c3e0efd48a18a22d5be3e07cfe781d80ac3dd64a3cec0df0737f9b5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly found the code/document mismatch and mapped paths, but adopted the stale documented threshold of 2 as the regression target and did not account for unverified documentation.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-003-mapped-doc-regression`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94` from `agents/qa/test/regression-suite/evals/workspace/eval-3-mapped-doc-regression`.
- Fixture SHA-256: `b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94`
- Prompt SHA-256: `ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `850108c3e4722feb1b9e0417b1554f0fb5b41d47001505d7da16c6bcd9946093`
- Skill overlay SHA-256: `3af177f0dcd9723964fdbcbf144832d8c6b68b267a850af3da918d86fe27d617`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `e133160262ed184852d28136da76d373bddc3830b084351e43f62baba3d14a43`
- Metadata SHA-256: `8f1420b83ef9d543d57a760ebba7fc169b9c3d2172e7b3b1e191d47cfe76b856`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | with_skill mentions the change map and mapped document but does not establish that docs/site/api/search-query.md was read first; its output presents code verification before the document. |
| `verifies_against_code` | PASS | It confirms src/search/query.rules sets minimum_query_length = 3, notes the document still says 2, treats code as the factual baseline, and identifies the directly affected search-validation/document paths. |
| `treats_unverified_as_low_trust` | PASS | It explicitly detects last_verified_version: unverified, uses code as the fact baseline, expands regression coverage around the boundary and side effects, and does not declare the result release-ready. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b; fixture_sha256=b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94; output_sha256=641395472f4744d2b751f10a39c1b52f3bc11f9f07a7771c883ded1290ec43ed; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Verified the code/document discrepancy, handled the unverified document as low trust, and proposed focused 2-character, adjacent-boundary, and side-effect regression coverage; document-first reading was not demonstrated.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ffcf3a2d7addddf903f6f7ab8491b7d6388aab8f8d43086a53d98c797d44a47b; fixture_sha256=b09fa431bfb2ae442891b6d53441773dfe7d31b84ffb9e7738912c1ba9a50a94; output_sha256=5fc014c352b266891927327b6ae42389a7f99b7e80754e24a8ba0fdbdbd135a9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly verified the code threshold and documented boundary cases, but did not explicitly follow the mapped-document-first order or address the document's unverified status.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output does not satisfy the assertion requiring the mapped document to be read first.
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

# Eval Result: eval-003-mapped-doc-regression

## Evaluation Target

- Agent: `qa`
- Skill: `regression-suite`
- Eval: `eval-003-mapped-doc-regression`
- Test case: mapped-doc-regression
- Workspace: `workspace/eval-3-mapped-doc-regression`
- Natural user prompt:

> 为 src/search/query.rules 的最短查询长度修复制定定向回归范围，并判断当前实际阈值。

- Expected artifact: 以映射文档缩小范围、以代码事实确定阈值的回归计划和差异说明。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/regression-suite--eval-003-mapped-doc-regression/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `3948b19dc34aa631d0b7825e8dcb94050d9b7e29c04c99b855f3f0c3f4b65a28`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **FAIL**（PASS 2 / FAIL 1 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: FAIL

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `reads_mapped_docs_first`<br>优先读取搜索规则映射文档 | FAIL | transcript.jsonl 显示先执行技能说明与文件扫描，随后命令按 query.rules → change-map.yaml → search-query.md 顺序读取；没有先读取映射要求的 docs/site/api/search-query.md。最终快照仅证明文件存在，不能推翻工具读取顺序。 | FAIL | transcript 先用 rg 扫描并命中代码及文档，随后显式按 query.rules → search-query.md → change-map.yaml 读取；未按 change-map 优先读取目标文档。 |
| `verifies_against_code`<br>回归预期由代码核证 | PASS | transcript 读取 src/search/query.rules，工具输出为 minimum_query_length = 3；同时读取文档并确认其仍写着至少 2 个字符。candidate.md 记录了 3 与 2 的差异、边界范围及文档/配置影响路径。快照内容也独立确认该差异。 | PASS | transcript 和最终快照均确认代码值为 3、文档值为 2；candidate.md 记录差异及定向回归范围。 |
| `treats_unverified_as_low_trust`<br>最低信任处理未核证文档 | PASS | change-map.yaml 与 API 文档均含 last_verified_version: unverified。transcript 随后核证代码值；candidate.md 明确报告 blocked，并说明没有运行时回归证据，未给出 pass 或 release-ready 结论。 | PASS | transcript 发现 unverified 后读取代码、映射和文档，并指出没有现成测试；candidate.md 要求新增边界用例和文档核对，没有将文档单独作为 pass 或 release-ready 依据。 |

## With-Skill Behavior

with_skill 覆盖全部断言；2 条通过，reads_mapped_docs_first 失败。最终快照未发生文件变更。

## Fresh Without-Skill Baseline

without_skill 同样覆盖全部断言；2 条通过，读取顺序断言失败，仅作 baseline 对照。两条 lane 的快照均包含相同 3 个 fixture，且哈希与 fixture-manifest.json 完全一致。

## Failures

- with_skill 的 reads_mapped_docs_first：实际工具调用顺序未先读取 docs/site/api/search-query.md。
- without_skill 的 reads_mapped_docs_first：实际工具调用顺序也未先读取映射目标文档。

## Not Exercised

- 无。

## Next Steps

- 调整 with_skill 的探索顺序：先读取 change-map，再读取其 required_docs 中的 search-query.md，最后回到 query.rules 做代码核证。
- 重新执行并保留完整 transcript/tool trace；无需修改当前 evidence 文件。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
