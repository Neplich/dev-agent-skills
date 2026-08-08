# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86` from `agents/docs/test/docs-audit/evals/workspace/eval-011-post-tag-mismatch`.
- Fixture SHA-256: `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86`
- Prompt SHA-256: `63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `87ef764041bed9ee9555b42ac224112964f5f9e1229cf61ab18c2da424e966e8`
- Eval definition SHA-256: `dd2f814bca5d9dce6fed31e09545467860903a50efd0252401f17372eb85d63c`
- Metadata SHA-256: `44f3e50cd86c78b14f58e8584dc26444f39390cb3ef1d6e88051fdaf94a2e89e`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_immutable_pre_tag_authority` | PASS | 明确以 refs/heads/pre-tag-handoff 作为 authority，并将 release-evidence 分支与未提交工作区副本隔离。 |
| `validates_current_attempt_history` | FAIL | 虽然保持 blocked 并识别了未提交副本，但没有明确核对同版本 attempt 2 直接 superseded attempt 1 的历史关系。 |
| `rejects_complete_release_tree_drift` | PASS | 明确比较 704d8f7..26cf729，识别新增 src/catalog/export-v2.py，并保持 blocked。 |
| `offers_safe_maintainer_recovery` | PASS | 提供了同版本修复和改用新版本两种选择，并说明维护者、docs-site-bootstrap、Docs/工程负责人的边界及重新审计前提。 |
| `persists_blocked_without_corrupting_authority` | FAIL | 说明保持 blocked、未执行写入且不产生成功状态，但未说明持久化失败后的具体恢复条件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=dc8f260ba1d782fa4cdd851e0fd56103c46ff81ba38b230bee497bc0b909f1c9; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别 pre-tag authority、完整发布树漂移并保持 blocked，且提供安全补救选择；但遗漏当前 attempt 历史核对和持久化故障恢复条件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=26dd5c84e60c0c90b1d72b0b47c41ad312d5a01d99d70bbdf4138623ea14cd61; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了 export-v2.py 漂移并拒绝 release_verified，但使用较弱的 needs_follow_up 结论，未充分隔离 immutable authority，也未覆盖完整恢复边界。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- current_attempt_history 未完整呈现。
- persistence failure recovery 未覆盖。
- Next: 补充 attempt 2、直接 superseded attempt 1 及同版本关系的核对结果。
- Next: 说明持久化失败时的恢复条件，并确认既有 authority 不被改写。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86` from `agents/docs/test/docs-audit/evals/workspace/eval-011-post-tag-mismatch`.
- Fixture SHA-256: `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86`
- Prompt SHA-256: `63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `87ef764041bed9ee9555b42ac224112964f5f9e1229cf61ab18c2da424e966e8`
- Eval definition SHA-256: `dd2f814bca5d9dce6fed31e09545467860903a50efd0252401f17372eb85d63c`
- Metadata SHA-256: `44f3e50cd86c78b14f58e8584dc26444f39390cb3ef1d6e88051fdaf94a2e89e`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_immutable_pre_tag_authority` | NOT_EXERCISED | The output preserves the pre-tag authority and rejects the modified worktree copy, but the locked evidence does not prove the required actual ref resolution and git-show read order. |
| `validates_current_attempt_history` | NOT_EXERCISED | The output remains blocked and rejects the rewritten worktree audit, but it does not explicitly establish attempt 2, its superseded attempt 1, and the same-version current-attempt relationship. |
| `rejects_complete_release_tree_drift` | PASS | It identifies the complete base-to-tag drift as the added src/catalog/export-v2.py, notes the raw patch mismatch, and keeps the result blocked instead of relying on matching version surfaces. |
| `offers_safe_maintainer_recovery` | PASS | It gives two actionable maintainer paths: repair/remove the incorrect v1.2.0 tag and rerun audits, or abandon it and confirm a new release version before auditing that target; it keeps authority changes within maintainer control. |
| `persists_blocked_without_corrupting_authority` | PASS | It reports blocked, performs no writes, preserves the existing pre-tag authority, rejects worktree backfilling of historical evidence, and requires evidence completion and renewed auditing before verification. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=ee65ebdb919b9dfe5fbd865c8cb94fb377ded1024b388523a4b3981a4e69ab46; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly keeps the release blocked, identifies the decisive complete-tree drift, separates the dirty worktree copy from authority, and provides safe recovery choices.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=95687e9f2ee88caefdde4e2de4a7d7e0c9348ee6f480b55883b1939589ad24f0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Recognizes the added source file and blocked release, but provides a less complete authority-preservation and recovery treatment for the current attempt and failed persistence context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Require explicit evidence of resolving pre-tag commit/tree refs and reading committed audit and handoff records.
- Next: Require explicit validation of attempt 2 and its direct superseded attempt 1 before claiming full coverage.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86` from `agents/docs/test/docs-audit/evals/workspace/eval-011-post-tag-mismatch`.
- Fixture SHA-256: `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86`
- Prompt SHA-256: `63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dd2f814bca5d9dce6fed31e09545467860903a50efd0252401f17372eb85d63c`
- Metadata SHA-256: `44f3e50cd86c78b14f58e8584dc26444f39390cb3ef1d6e88051fdaf94a2e89e`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_immutable_pre_tag_authority` | PASS | With-skill output identifies the pre-tag authority and explicitly isolates the uncommitted worktree release_verified copy as non-authoritative. |
| `validates_current_attempt_history` | FAIL | It does not state or reconcile attempt 2 with its directly superseded same-version attempt 1. |
| `rejects_complete_release_tree_drift` | PASS | It reports the blocked result and identifies the actual tag delta as the added src/catalog/export-v2.py, inconsistent with the audit’s claimed change scope. |
| `offers_safe_maintainer_recovery` | PASS | It offers same-version remediation and a new-valid-authority path, with complete pre-tag/post-tag verification prerequisites and an explicit prohibition on modifying the old authority. |
| `persists_blocked_without_corrupting_authority` | FAIL | It states that no post-tag result was written and existing worktree changes remain, but does not explain the recovery conditions for the failed persistence attempt. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=cb962a5d39085c27b0eec200367f64490ff98bf66bf4b282b96509518970f1b8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly concluded blocked, isolated the uncommitted drifted audit, detected the complete-tree mismatch, and proposed bounded recovery; omitted explicit attempt-history reconciliation and persistence-failure recovery conditions.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=cbdda5bcae1757453949253b1c7dedebd3107df5155c37d25b3b8777cd3c2cf8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Recognized version-surface consistency and the export-v2.py delta, but did not clearly preserve the immutable pre-tag authority or provide sufficiently bounded recovery guidance.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- validates_current_attempt_history
- persists_blocked_without_corrupting_authority
- Next: Explicitly reconcile attempt 2 and its directly superseded attempt 1 for v1.2.0.
- Next: State the persistence-failure recovery conditions, including restoring writable result persistence and rerunning post-tag verification without altering existing authority.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86` from `agents/docs/test/docs-audit/evals/workspace/eval-011-post-tag-mismatch`.
- Fixture SHA-256: `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86`
- Prompt SHA-256: `63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d339a8370a29b3fb2a69aa1879b1226165ec088d306a4e2e7a01258df2326973`
- Skill overlay SHA-256: `0bc7243cbb5cff3e77d9ba448e020a1a1f279639f8db6a365faac208b8e1dcc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dd2f814bca5d9dce6fed31e09545467860903a50efd0252401f17372eb85d63c`
- Metadata SHA-256: `44f3e50cd86c78b14f58e8584dc26444f39390cb3ef1d6e88051fdaf94a2e89e`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_immutable_pre_tag_authority` | NOT_EXERCISED | 输出正确区分了 pre-tag authority 与未提交工作区副本，但锁定证据无法证明实际执行了指定 ref 解析和 git show 读取。 |
| `validates_current_attempt_history` | FAIL | 输出确认 attempt 2、工作区副本未被采用并保持 blocked，但未核对或说明同版本且已直接 superseded 的 attempt 1。 |
| `rejects_complete_release_tree_drift` | NOT_EXERCISED | 输出指出 export-v2.py 是决定性新增差异并保持 blocked，但锁定证据无法证明实际执行了完整 commit tree 解析与差异核对。 |
| `offers_safe_maintainer_recovery` | PASS | 提供了保留/修正现有 tag 与确认新版本两类选择，要求补齐证据、change-map 和审计链路，并将决定交给维护者。 |
| `persists_blocked_without_corrupting_authority` | FAIL | 输出分离了 blocked 结果与既有 authority，且说明未执行写入；但未明确给出持久化故障恢复条件（恢复写入能力、写入并 readback 验证）。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=c89415f7171d59147f2b9e5c3c0181544834aae28f3005d147211075d8d6959e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确得出 blocked，识别 authority 漂移、完整 tree 增量和持久化限制，并给出维护者后续选择；但遗漏 attempt 1 历史核对及持久化恢复条件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=0f7aada55b49bddfce0db09b4a9609365c3fccfcdf32e6702bb758eac5046d08; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了未审计的 export-v2.py 差异并拒绝确认 release_verified，但恢复选择和 authority 保护表述较弱。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- validates_current_attempt_history: 未说明 attempt 1 已被 attempt 2 直接 supersede。
- persists_blocked_without_corrupting_authority: 未明确持久化失败后的恢复条件。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86` from `agents/docs/test/docs-audit/evals/workspace/eval-011-post-tag-mismatch`.
- Fixture SHA-256: `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86`
- Prompt SHA-256: `63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9e9abf391c9ccd9564d35b5def50bc0374b1db0886710676c4d48422839746ae`
- Skill overlay SHA-256: `c66ac938bf9158faa694d7c3e311e913ddc4a06da11de703a881234f257c470c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dd2f814bca5d9dce6fed31e09545467860903a50efd0252401f17372eb85d63c`
- Metadata SHA-256: `44f3e50cd86c78b14f58e8584dc26444f39390cb3ef1d6e88051fdaf94a2e89e`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_immutable_pre_tag_authority` | NOT_EXERCISED | 输出正确识别并隔离了 pre-tag ref、tag ref 与未提交工作区副本，但锁定证据无法证明实际使用 git show 读取记录的过程。 |
| `validates_current_attempt_history` | FAIL | with_skill 输出未核对 attempt 2、其 superseded attempt 1 及同版本关系，虽保持 blocked。 |
| `rejects_complete_release_tree_drift` | PASS | 明确报告 pre-tag 与 tag 树不匹配，指出唯一新增的 src/catalog/export-v2.py 未被审计覆盖，并保持 blocked。 |
| `offers_safe_maintainer_recovery` | PASS | 提供了纳入实际发布内容后重新审计和排除错误内容后修正发布两类选择，并要求补齐审计基础、重新生成 handoff、重跑 post-tag audit，且指出维护者与 docs-site-bootstrap 的责任边界。 |
| `persists_blocked_without_corrupting_authority` | FAIL | 输出说明保持 blocked、未写入且 post-release 记录缺失，但未明确说明持久化故障的恢复条件及失败写入不会产生成功状态或改动既有 authority。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=c7807a9482106a4532c01637766cbcf31fb5f94500e8dcc64f3f4b0bc41e62e6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确保持 blocked，识别 pre-tag authority、完整树差异、未覆盖新增文件和未提交副本，并给出恢复方向；遗漏 attempt 历史核对及持久化故障恢复条件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=7a2c5ac539aa30df53f65dbb5eeb1d7d401c3a04267f65742c000e1038387290; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了 tag 树漂移、未提交 audit 副本和审计缺口，并给出后续选择；未呈现完整 immutable authority 与 attempt 历史核对。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足当前 attempt 历史核对要求。
- with_skill 未说明持久化故障的恢复条件及失败写入的 authority 保护语义。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86` from `agents/docs/test/docs-audit/evals/workspace/eval-011-post-tag-mismatch`.
- Fixture SHA-256: `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86`
- Prompt SHA-256: `63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2d24da5f976a5ab2710c2c072a19015e074d314e0ebdb88f1c28831425f1b98c`
- Skill overlay SHA-256: `40330c17a3b77f25a1b1a716fa5e9355e0011db79d19014344ed516affba11c8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dd2f814bca5d9dce6fed31e09545467860903a50efd0252401f17372eb85d63c`
- Metadata SHA-256: `44f3e50cd86c78b14f58e8584dc26444f39390cb3ef1d6e88051fdaf94a2e89e`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_immutable_pre_tag_authority` | PASS | 明确解析并区分 refs/heads/pre-tag-handoff 与 refs/tags/v1.2.0 的 commit/tree，并拒绝未提交且指向其他 authority 的工作区副本。 |
| `validates_current_attempt_history` | PASS | 识别 pre-tag audit/handoff 为同版本 attempt 2、authority 记录不完整且当前副本已改写；最终保持 blocked。 |
| `rejects_complete_release_tree_drift` | PASS | 核对 tag/tree 证据及原始 name-status，明确新增 src/catalog/export-v2.py 未被审计覆盖，并拒绝 release_verified。 |
| `offers_safe_maintainer_recovery` | PASS | 提供保留当前 tag并补齐审计，或由维护者确认新版本后重新审计发布两种选择，明确维护者负责 tag/version 处理。 |
| `persists_blocked_without_corrupting_authority` | PASS | 明确 blocked 与 pre-tag authority 分离，仅执行只读核验；未写入结果、tag、branch 或 release，要求修复证据链后重新审计。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=9baadf764087bf75124a6a67c08648eb86b6d829289e6ede3f32dbd6dd9fd474; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 基于 committed pre-tag authority、attempt 历史和完整变更证据保持 v1.2.0 blocked，并给出维护者恢复选择。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=dc28d9e1e4e255e1c349a1183ec32e238dd872a1a74ead006cc2e7a9c790f42e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别部分发布证据缺口并保持未验证，但未充分坚持 immutable authority、attempt 历史和完整树漂移边界。
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

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86` from `agents/docs/test/docs-audit/evals/workspace/eval-011-post-tag-mismatch`.
- Fixture SHA-256: `580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86`
- Prompt SHA-256: `63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dd2f814bca5d9dce6fed31e09545467860903a50efd0252401f17372eb85d63c`
- Metadata SHA-256: `44f3e50cd86c78b14f58e8584dc26444f39390cb3ef1d6e88051fdaf94a2e89e`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_immutable_pre_tag_authority` | PASS | 明确解析 pre-tag authority 的 commit/tree，并以已提交 handoff 为依据；将未提交的 worktree audit 副本认定为不可用发布证据。 |
| `validates_current_attempt_history` | PASS | 核对 committed pre-tag handoff 的 attempt 2、superseded attempt 1 和 v1.2.0 关系，并因 worktree 改写 authority/result 而保持 blocked。 |
| `rejects_complete_release_tree_drift` | PASS | 明确指出实际 pre-tag 到 tag 的完整差异新增 src/catalog/export-v2.py，并据此保持 blocked。 |
| `offers_safe_maintainer_recovery` | PASS | 提供修复当前 v1.2.0 或确认新版本两类选择，要求重新执行 pre-tag/post-tag 审计，并将操作限定为维护者流程。 |
| `persists_blocked_without_corrupting_authority` | FAIL | 说明本次未写入或修改 authority，但未明确说明失败的 blocked 结果持久化的恢复条件，也未完整表述未完成写入不会产生成功状态。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=c2809ba2d90c1f00b857f770e3dc61c446ab411fe3caee03cd2e7ac3e1ec90ee; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 以 pre-tag authority 为准，核对提交历史和完整 tree diff，拒绝漂移副本与 release_verified，并提出安全恢复选项；未充分处理结果持久化失败条件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=580d96fbd8d2adf79b801381050e6b3b9bfc58b8f39d636b27ce9f575d873d86; output_sha256=23c711dd195f752a0c7d066ba152cdaeaeb8bece53aaf4a9e908a6569fe6a5d2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了未提交 audit 副本、tag 差异和缺失 post-tag 记录，但未按要求以 immutable pre-tag authority 和完整 tree 绑定为核心，且给出可打 tag 的倾向性结论。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足 persists_blocked_without_corrupting_authority：缺少持久化故障恢复条件及未完成写入不会产生成功状态的明确说明。
- Next: 补充 blocked 结果持久化失败时的恢复条件，并明确任何未完成写入都不会生成成功状态或修改既有 authority。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9e3866c8bd3113bab586de6d712d224d3718fa740e3b1e2887b2b51725369b40` from `agents/docs/test/docs-audit/evals/workspace/eval-011-post-tag-mismatch`.
- Fixture SHA-256: `9e3866c8bd3113bab586de6d712d224d3718fa740e3b1e2887b2b51725369b40`
- Prompt SHA-256: `63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dd2f814bca5d9dce6fed31e09545467860903a50efd0252401f17372eb85d63c`
- Metadata SHA-256: `44f3e50cd86c78b14f58e8584dc26444f39390cb3ef1d6e88051fdaf94a2e89e`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_immutable_pre_tag_authority` | FAIL | The output identifies the pre-tag commit and notes the modified worktree copy, but does not demonstrate resolving the pre-tag commit and tree refs, reading audit/handoff with git show, or explicitly isolating the M copy as non-authoritative. |
| `validates_current_attempt_history` | FAIL | It reports attempt 2 and the blocked state, but does not explicitly verify same-version attempt history or that attempt 1 was directly superseded. |
| `rejects_complete_release_tree_drift` | PASS | It keeps the result blocked and identifies the tag-versus-pre-tag added file src/catalog/export-v2.py as the decisive unreviewed tree difference. |
| `offers_safe_maintainer_recovery` | PASS | It provides same-version remediation through correcting/removing the tag and rerunning pre-tag audit, plus abandoning v1.2.0 and establishing a new version; it also states the required valid handoff/audit prerequisites and assigns documentation work to named owners. |
| `persists_blocked_without_corrupting_authority` | FAIL | It separates the blocked conclusion from the uncommitted worktree record and states no writes occurred, but does not explain recovery conditions for the failed persistence attempt or explicitly guarantee that incomplete writes cannot create success or alter existing authority. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=9e3866c8bd3113bab586de6d712d224d3718fa740e3b1e2887b2b51725369b40; output_sha256=8c3c43a30ecbe53ff86cb2bebfb63699c58d186c507ff2ca58dd97c79f1238ce; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Returns blocked, identifies the decisive tree drift and uncommitted audit copy, and offers recovery choices, but omits explicit evidence for immutable ref reads, superseded-attempt validation, and persistence-failure recovery guarantees.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=63cc630aa7fe4e8caac8407e8b4008bbc49c2b73e376868bcef067409538b2ed; fixture_sha256=9e3866c8bd3113bab586de6d712d224d3718fa740e3b1e2887b2b51725369b40; output_sha256=4db052e0d6f679b672ee6aef7e5230f7afae062cf43e5eed85c608714f8ecb94; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the added source drift and uncommitted post-tag copy, but uses a weaker tag_exists_with_evidence_gap conclusion and does not establish the full authority and attempt-history controls.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output fails the immutable authority-read requirement.
- The with_skill output fails to explicitly validate attempt 1 supersession and same-version history.
- The with_skill output fails to state persistence-failure recovery and no-corruption guarantees.
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

# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-011-post-tag-mismatch`
- Scenario: same-version history、当前副本漂移与未审计 tag 增量
- Review context: issue #177 sub-batch 4b

## Test Set / Fixture Version

- Fixture version: `issue-177 discrimination restore round-1`
- Validation time: `2026-07-28 22:48:16 CST`
- Runtime: `tmp/eval-runs/issue-177/docs-audit/round-1/`
- Assertions: 5，全部实际触发

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `uses_immutable_pre_tag_authority` | PASS | PASS | 两者均区分 `.eval/committed-audit-v1.2.0.md` 与被篡改的 `docs/site/.meta/audit/audit-v1.2.0.md`，并引用 `.eval/release-context.md` 的可信提交记录。 |
| `validates_current_attempt_history` | FAIL | FAIL | fixture 含 `current_pre_tag_attempt: 2`、历史 attempt lineage；两者均未明确核对累计历史与当前 attempt 的一致性，仅直接采信 `candidate_verified`。 |
| `rejects_complete_release_tree_drift` | PASS | PASS | 两者均引用 `.eval/tag-tree-diff.name-status` 的 `A src/catalog/export-v2.py`，指出 tag 含未审计增量并保持 `blocked`。 |
| `offers_safe_maintainer_recovery` | PASS | FAIL | with_skill 明确针对同一 `v1.2.0` 修正 tag 或确认新版本并重新审计，且指定维护者边界；without_skill 虽提供两种路径，但未明确“同版本修复”与“改用新版本”的版本确认边界。 |
| `persists_blocked_without_corrupting_authority` | FAIL | PASS | with_skill 仅说未写入，未说明 `.eval/release-context.md` 所述 staged 后提交失败及恢复条件；without_skill 明确说明 staged 写入失败、post-tag 记录不存在、未产生成功状态且未执行写入。 |

未满足断言（with/without 任一 FAIL）：``validates_current_attempt_history``、``offers_safe_maintainer_recovery``、``persists_blocked_without_corrupting_authority``



## Leakage Surface Analysis

重做前，prompt、assertions 和 release context 直接提供 immutable record 选择、strict tree equality、lineage digest 算法、两条 remedy、re-entry 条件、blocked record 事务和 rollback 清单。

重做后，fixture 只保留两份 repository-state bytes、raw tag tuple、raw tree diff、committed candidate/discovery 和一次 staged 写入失败事件。显眼 tree delta 仍对 baseline 可见，但维护者版本选择契约不再出现在生成输入中。

## Redesign

- prompt 只要求给出结论、决定性差异、可持久化结果和维护者后续选择。
- assertions 改为 immutable authority、attempt history、complete tree、maintainer recovery 和 blocked persistence 五个语义结果。
- 删除 equality、active attempt、lineage rule、CAS policy 与标准答案 prose。
- 在 committed discovery 的 current tuple 中引入单字符 `previous_lineage_digest` 冲突，与 visible code-tree drift 形成两个独立 blocker。
- 清理历史 issue 身份引用，并重算 inventory/candidate/discovery object identities；只保留刻意的 lineage 冲突。

## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | With skill | Without skill | Fresh judgment |
| --- | --- | --- | --- |
| `uses_immutable_pre_tag_authority` | PASS | PASS | 两臂均使用 committed evidence 并隔离 checkout 副本。 |
| `validates_current_attempt_history` | PASS | PASS | 两臂均识别 `33adb` / `03adb` lineage 冲突。 |
| `rejects_complete_release_tree_drift` | PASS | PASS | 两臂均以完整 tree mismatch 和新增源文件阻塞。 |
| `offers_safe_maintainer_recovery` | PASS | FAIL | baseline 未明确提供同版本重跑与维护者确认新版本两类路径及完整重入前置。 |
| `persists_blocked_without_corrupting_authority` | PASS | PASS | 两臂均分离 blocked 结果与 pre-tag authority，并确认 staged 故障未形成持久成功。 |

## Fresh Validation Method

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- 两臂锁定前只读取同一 prompt/fixture，未读取 assertions、expected output 或旧 comparison。
- with-skill arm读取完整 Docs/docs-audit 指令；without-skill arm隔离这些内容和 with-skill 输出。
- fresh judge 在 response SHA-256 锁定后才读取 assertions。
- with-skill SHA-256：`2412c4e8a8e2e5bd31127afebcf852a0efb175da33596b35b084deec73e3aa9e`；without-skill：`f572067d3b6d05c6b55803129c2ceaaadcb5c4f1f8d941e180eeea0f0adfbc89`。

## Failures And Limitations

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- with-skill 无失败；Coverage FULL。
- raw tree diff 与 committed records 仍让 baseline 恢复 4/5；可测量差距集中在 specialist 的维护者救济边界。
- 第一轮即达到区分度，无需第二轮。

## Runtime Artifact Policy

- runtime responses 和 judge verdict 仅保存在 `tmp/eval-runs/issue-177/docs-audit/round-1/`，不提交。
- 本 `comparison.md` 是唯一 durable 结果。

## Next Steps

- 本 assertion 措辞在本轮 review 后做了澄清性对齐，判定语义与已记录的 fresh run 一致，未重新执行 eval。
