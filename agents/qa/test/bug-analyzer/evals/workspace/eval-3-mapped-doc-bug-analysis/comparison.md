# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-003-mapped-doc-bug-analysis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf` from `agents/qa/test/bug-analyzer/evals/workspace/eval-3-mapped-doc-bug-analysis`.
- Fixture SHA-256: `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf`
- Prompt SHA-256: `42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0d6c4b717279e8edddeea8100d93e004d25b98b502e0ca114092a3f0c007a52f`
- Skill overlay SHA-256: `4d1289a2f580cb07efcd85d24fb079acfc635807339f9469fa7653101393ff87`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `5055f21aa292e91a955bc3aa635c808239336415cf083aba532e9d19a7985220`
- Metadata SHA-256: `6e065f47b93dd01060b700c2c7836503fb5797f7c0c1bb375677811fe6fa6d5f`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | The locked report records the matched change-map entry and required document, but the locked evidence cannot prove the actual read order or absence of an unrelated full-site traversal. |
| `verifies_against_code` | PASS | The delivered report records code value 2, documentation value 3, their separate evidence roles, and the impact on defect classification; the fixture confirms max_retry_attempts = 2. |
| `treats_unverified_as_low_trust` | PASS | The delivered report identifies last_verified_version: unverified as low-trust and keeps runtime defect confidence low pending code, test, and execution evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=8b5e84a2f379b9d9cc1f1e5e73c05e09d78cc6cfd0f7eadc0e2484e1b0e69ff3; snapshot_sha256=c73eff7510c1ef2210bd4a1e6f062ba5b2b87af96eb15aee849b6dcc96954f18
- Behavior: Produced a structured evidence report with correct code/document discrepancy analysis, low-trust handling, uncertainty boundaries, and requested follow-up evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=256b0e2e3603ec817b5b5916e3d5f8d0583794410ee41f57aca20425536ce2ce; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provided accurate comparison analysis in prose but no delivered report file; it also treated the discrepancy as unconfirmed runtime behavior.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Use an observable read trace or equivalent raw process evidence to evaluate the mapped-document read-order assertion.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-003-mapped-doc-bug-analysis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf` from `agents/qa/test/bug-analyzer/evals/workspace/eval-3-mapped-doc-bug-analysis`.
- Fixture SHA-256: `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf`
- Prompt SHA-256: `42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0d6c4b717279e8edddeea8100d93e004d25b98b502e0ca114092a3f0c007a52f`
- Skill overlay SHA-256: `4d1289a2f580cb07efcd85d24fb079acfc635807339f9469fa7653101393ff87`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5055f21aa292e91a955bc3aa635c808239336415cf083aba532e9d19a7985220`
- Metadata SHA-256: `6e065f47b93dd01060b700c2c7836503fb5797f7c0c1bb375677811fe6fa6d5f`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 交付报告引用了 change-map 和正式说明，但锁定原始证据无法证明读取顺序或是否遍历了无关站点文档。 |
| `verifies_against_code` | PASS | 交付文件明确记录代码为 max_retry_attempts = 2、正式说明为最多重试 3 次，并将其分类为 suspected / needs more evidence，说明未仅凭文档确认缺陷。 |
| `treats_unverified_as_low_trust` | PASS | 交付文件明确识别 last_verified_version: unverified，并说明文档不足以单独建立产品契约；结论和置信度依据代码与缺失的运行时、测试证据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=23781830324bc9e569fbc90257a8440ab5ed4033dd7c76f1f4cdd1d8a45eb782; snapshot_sha256=b2241fc8ae8cb5acc93d1a094c9ded77752737a2766b1a9020567a3f7440a1f0
- Behavior: 交付了证据化分析文件，准确记录代码/文档差异、未核证状态、当前分类、置信度及待补证据；读取顺序无法由锁定证据证明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=a41a1a634bdb502bdced4e771ffbeef3f16fd1ee326e32c1f589f6b25e4fb16d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 基线输出识别了代码与文档的 2/3 差异，并谨慎指出语义和运行时证据不足；未交付文件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 如需完整覆盖，提供带读取事件或工具调用顺序的原始证据。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-003-mapped-doc-bug-analysis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf` from `agents/qa/test/bug-analyzer/evals/workspace/eval-3-mapped-doc-bug-analysis`.
- Fixture SHA-256: `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf`
- Prompt SHA-256: `42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `41901c7a6c233e96234e49bc5924edbee83abf2f5546698275afb442ff6f1d8f`
- Skill overlay SHA-256: `57b0a87d033b766894f476e95aca86f50c66550e77c4d8ba3a998651bf9efccb`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5055f21aa292e91a955bc3aa635c808239336415cf083aba532e9d19a7985220`
- Metadata SHA-256: `6e065f47b93dd01060b700c2c7836503fb5797f7c0c1bb375677811fe6fa6d5f`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | The with_skill report identifies the mapped document and records a change-map trace, but the locked evidence cannot prove the required read order or absence of an unrelated full-site traversal. |
| `verifies_against_code` | PASS | The report explicitly contrasts `max_retry_attempts = 2` in code with the documented 3 retries, distinguishes confirmed facts from inference, and explains that runtime semantics and the actual defect remain unconfirmed. |
| `treats_unverified_as_low_trust` | PASS | The report identifies `last_verified_version: unverified`, states the document cannot independently establish current behavior, and bases its medium-confidence conclusion on the deterministic code/document mismatch while requesting runtime or test evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=be2953ab121dcbfc756cded64f87da61fe882e22089db1e06136fd60aab42224; snapshot_sha256=e63cd0b602b517b75e5a3368edc480683544d7cb579eab58fb1cc367326eb321
- Behavior: Delivered a structured QA analysis artifact with mapped-document context, explicit code-versus-document comparison, unverified-document qualification, and missing-evidence guidance.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=c98c446e77acb337fda6370b22685c6efdd7a19bae7a8fddf6232b4e1b10a4da; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Produced a useful evidence summary and identified the code/document mismatch, but did not provide a delivered QA analysis artifact.
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
- Skill: `bug-analyzer`
- Eval: `eval-003-mapped-doc-bug-analysis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf` from `agents/qa/test/bug-analyzer/evals/workspace/eval-3-mapped-doc-bug-analysis`.
- Fixture SHA-256: `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf`
- Prompt SHA-256: `42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `41901c7a6c233e96234e49bc5924edbee83abf2f5546698275afb442ff6f1d8f`
- Skill overlay SHA-256: `57b0a87d033b766894f476e95aca86f50c66550e77c4d8ba3a998651bf9efccb`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5055f21aa292e91a955bc3aa635c808239336415cf083aba532e9d19a7985220`
- Metadata SHA-256: `6e065f47b93dd01060b700c2c7836503fb5797f7c0c1bb375677811fe6fa6d5f`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | with_skill 报告正确识别并引用 change-map 指向的文档，但锁定的原始证据无法证明实际读取顺序或未遍历无关文档。 |
| `verifies_against_code` | PASS | 报告分别记录了 retry.rules 的 max_retry_attempts = 2、正式说明的最多重试 3 次，并明确说明仅凭文本/配置不能确认实际运行时语义及缺陷是否成立。 |
| `treats_unverified_as_low_trust` | PASS | 报告识别 change map 和正式文档的 last_verified_version: unverified，并将其作为不能独立证明版本化产品契约的限制；分类为 suspected / needs more evidence，要求代码消费方、测试或运行轨迹补证。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=f711e15e87246269fc4fecfc7ad00bb5836d58b70ef9acf5d446351ca5c76b8b; snapshot_sha256=b09a4b3d8649b80406730e44bf92fcfca6ef093de13a0a98f52265b302d93c6d
- Behavior: 生成了证据化报告，明确记录代码/文档冲突、变更映射、未核验状态和后续所需运行时证据，并避免将其直接认定为已确认线上缺陷。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=84e51f1d5bbd4fd07a6d9a1abf4eb2209e4e9e76b63814d7ff557274ef95a275; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了代码与文档的数值不一致及未核验状态，提供了较完整的证据和待补信息。
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
- Skill: `bug-analyzer`
- Eval: `eval-003-mapped-doc-bug-analysis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf` from `agents/qa/test/bug-analyzer/evals/workspace/eval-3-mapped-doc-bug-analysis`.
- Fixture SHA-256: `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf`
- Prompt SHA-256: `42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4a3df9ee16d4103be1f8943282fa829f43ca07121c256afa210bba92e93b1264`
- Skill overlay SHA-256: `9d14629b58659419083ead1c924b6df5c23442d8080b433d9ff5693735eb9586`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5055f21aa292e91a955bc3aa635c808239336415cf083aba532e9d19a7985220`
- Metadata SHA-256: `6e065f47b93dd01060b700c2c7836503fb5797f7c0c1bb375677811fe6fa6d5f`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill identifies the change-map entry and the mapped document docs/site/api/notification-retry.md, with no unrelated site-wide document traversal. |
| `verifies_against_code` | PASS | with_skill cites src/notifications/retry.rules as max_retry_attempts = 2, contrasts it with the document’s claim of 3 retries, and separately discusses document wording, code value, and the resulting unresolved defect classification. |
| `treats_unverified_as_low_trust` | PASS | with_skill explicitly identifies last_verified_version: unverified, treats the documentation as non-authoritative, and bases the confirmed conflict on the code/document evidence while withholding a production-behavior conclusion pending runtime or test evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=c8e70f360fd17170ed812472320d0e1db7a3ce016fb461e68b82db180a1d4336; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: With_skill mapped the code change to the formal document, verified the code/document mismatch, distinguished retry-count semantics, and downgraded unverified metadata while identifying missing runtime and test evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=3273adbab200332d2666f89b38f7d1028b7c840cb81ca761e2d65fc89ebcfce8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also found the 2-versus-3 discrepancy and cited the mapped documentation, but provided less explicit treatment of retry-count semantics and verification confidence.
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
- Skill: `bug-analyzer`
- Eval: `eval-003-mapped-doc-bug-analysis`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf` from `agents/qa/test/bug-analyzer/evals/workspace/eval-3-mapped-doc-bug-analysis`.
- Fixture SHA-256: `7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf`
- Prompt SHA-256: `42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27d2fe5d8edb9052289c39964020afb301396abbc970275eb70967d32504d68`
- Skill overlay SHA-256: `bca841768a4850fe9fad50cd3d5afd91b738dda4eaad1293eea1e37d4bad841f`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `5055f21aa292e91a955bc3aa635c808239336415cf083aba532e9d19a7985220`
- Metadata SHA-256: `6e065f47b93dd01060b700c2c7836503fb5797f7c0c1bb375677811fe6fa6d5f`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | With-skill output identifies the change map, its mapping to notification-retry.md, and the mapped document; it cites no irrelevant site-document traversal. |
| `verifies_against_code` | PASS | It separately states the documentation says 3 retries and retry.rules sets max_retry_attempts = 2, while correctly withholding a definitive code-bug classification pending execution semantics. |
| `treats_unverified_as_low_trust` | PASS | It identifies last_verified_version: unverified and internal/dev metadata, treats the material as an unverified contract, and bases its conclusion on the code/document discrepancy while noting missing tests and runtime evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=6ebaf946f4437e13fe221c0db0e50a5c990eb9032036cfe7a4859d4944fde2f1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identified the mapped documentation, independently compared documentation and code, downgraded unverified material, and limited the conclusion to a documented drift risk.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=42efa66a3d947aa438db6985ea7344decf5267623091f1d47b29acd454584b1d; fixture_sha256=7d279cf3b0905050d0b65ec93cd3a19c763df01dd02f4eaadd2d86c46d0a38cf; output_sha256=634dc76d56960459590fe01c7adab939246ca88e61861e0dcbf123eecd154c86; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identified the mapped documentation, the 2-versus-3 discrepancy, unverified metadata, and missing runtime/test evidence.
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

# Eval Result: eval-003-mapped-doc-bug-analysis

## Evaluation Target

- Agent: `qa`
- Skill: `bug-analyzer`
- Eval: `eval-003-mapped-doc-bug-analysis`
- Test case: mapped-doc-bug-analysis
- Workspace: `workspace/eval-3-mapped-doc-bug-analysis`
- Natural user prompt:

> 分析 src/notifications/retry.rules 中通知重试次数可能与预期不一致的问题，形成证据化缺陷分析。

- Expected artifact: 区分文档声明与代码事实的缺陷分析，并说明证据置信度和影响。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/bug-analyzer--eval-003-mapped-doc-bug-analysis/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `86705991ace13eac6c0d350b99408298f65b0e28353532852c7102d1e8b2d9b9`。
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
| `reads_mapped_docs_first`<br>从映射文档获取缺陷上下文 | FAIL | transcript 中首次探索命令先执行全库 rg --files；随后 item_3 的读取顺序也是 retry.rules、notification-retry.md、change-map.yaml，未在命中 change-map 后先读取 docs/site/api/notification-retry.md，且存在对无关文件的全库枚举。 | FAIL | transcript 先读取 retry.rules，并执行全库 rg --files/引用搜索；没有先读取 change-map 再精准读取 notification-retry.md。 |
| `verifies_against_code`<br>缺陷判断回到代码证据 | PASS | transcript item_3 读取 retry.rules、notification-retry.md 和 change-map.yaml；最终快照中 retry.rules 为 max_retry_attempts = 2，文档第 13 行声明最多重试 3 次。缺陷文档明确区分文档声明、代码事实，并说明缺少消费者实现时只能判为疑似。 | PASS | transcript item_1、item_3 读取代码和文档；candidate 明确记录代码值 2、文档值 3，并分别讨论 retries/total attempts 两种语义及其对缺陷结论的影响。 |
| `treats_unverified_as_low_trust`<br>降低未核证文档的证据权重 | PASS | 最终快照中的缺陷文档第 19 行识别 notification-retry.md 与 change-map.yaml 的 last_verified_version: unverified，并将报告分类为 suspected / needs more evidence；第 7、41、47-52 行以代码冲突为依据，同时明确要求消费者、批准的产品预期和运行时/单元测试来确认。 | FAIL | transcript 虽读取到文档中的 unverified 字段，但 candidate 未识别其为最低信任线索，且没有明确置信度；结论主要基于文档与配置冲突，未按该断言要求处理 unverified 状态。 |

## With-Skill Behavior

with_skill 成功核对代码、映射文档和未核证状态，并在最终快照中创建了缺陷文档；但读取顺序未满足 mapped docs first，因此有一条已触发断言失败。

## Fresh Without-Skill Baseline

without_skill 识别了代码与文档的数值冲突并讨论了字段语义不确定性，但未将 unverified 作为最低信任线索，也未明确置信度。

## Failures

- with_skill 的 reads_mapped_docs_first 已触发但失败：读取顺序和探索范围不符合要求。
- without_skill 的 treats_unverified_as_low_trust 已触发但失败；baseline 结果不改变 with_skill 的最终判定。

## Not Exercised

- 无。

## Next Steps

- 修正 with_skill 的探索顺序：先读取 change-map.yaml，确认映射后立即读取 docs/site/api/notification-retry.md，再回到代码验证，并避免无关全库遍历。
- 在分析中明确写出 unverified 仅为最低信任线索，并给出独立的证据置信度。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
