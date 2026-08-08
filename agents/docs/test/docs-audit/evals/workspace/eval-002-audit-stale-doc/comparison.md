# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-002-audit-stale-doc`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583` from `agents/docs/test/docs-audit/evals/workspace/eval-002-audit-stale-doc`.
- Fixture SHA-256: `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583`
- Prompt SHA-256: `a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `6c436d29e1c4d967534d387d71455397c2a958eb0e9fdd8f24d404e3a4bfc7c7`
- Eval definition SHA-256: `65171d2c00ad7205a3b92eb523639da0ae1b9b851f9b225fb39f151ac8a09d1b`
- Metadata SHA-256: `393d49433e1e9b818095a60378e27c82e27a5159f0878e57881a2872b5feee91`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | PASS | 报告的“Deterministic impact”明确说明必需页面未在 base-to-target diff 中更新，因此进入事实审查时标记为 `suspect`。 |
| `confirms_outdated_claim_stale` | PASS | 报告以目标代码 blob 为证据，确认 `locale` 必填非空并存在 `400 {"code": "invalid_locale"}`，随后将文档结论定为 `stale`。 |
| `blocks_stale_release` | PASS | 报告结果为 `blocked`，列出 stale 页面证据及更新文档后重新审计等具体待办，并明确未执行 tag 操作且未返回 `ready_for_tag`。 |
| `does_not_stamp_stale_set` | PASS | 报告明确写出“No page was stamped”，且目标树没有 `.meta/releases.json`；文档的 `last_verified_version` 保持为 `v1.0.0`。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=f548f1e435668a919e740752f08347fe8e91d96eae537e2284575c40aaa83861; snapshot_sha256=b510e4dcdd8ee892520bac506cf355a2ce699b54aa4bcbfddb54bea690de79df
- Behavior: 完成正式文档审计，识别 suspect、经事实核验确认 stale，并以 blocked 结果阻止版本盖章和发布操作。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=cd07cf3d7db5e15199afce0f99febb20947a1a5e6d3915894fb5c31ac15f5735; snapshot_sha256=c327e63cd185bf04976939bce8907b505f7cbd832509ebd95570461c80f3156e
- Behavior: 生成了审计报告并指出文档遗漏 locale、invalid_locale 和旧验证版本，但未展示确定性 suspect 到事实层 stale 的审计链路，也未明确 blocked、未盖章和具体发布阻塞控制。
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
- Eval: `eval-002-audit-stale-doc`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583` from `agents/docs/test/docs-audit/evals/workspace/eval-002-audit-stale-doc`.
- Fixture SHA-256: `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583`
- Prompt SHA-256: `a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `6c436d29e1c4d967534d387d71455397c2a958eb0e9fdd8f24d404e3a4bfc7c7`
- Eval definition SHA-256: `65171d2c00ad7205a3b92eb523639da0ae1b9b851f9b225fb39f151ac8a09d1b`
- Metadata SHA-256: `393d49433e1e9b818095a60378e27c82e27a5159f0878e57881a2872b5feee91`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | NOT_EXERCISED | with_skill 未提供可证明确定性层先标记 `suspect` 并送事实层的锁定证据；仅能看到最终文档状态为 `stale`。 |
| `confirms_outdated_claim_stale` | PASS | with_skill 以代码新增必填非空 `locale` 及 `400 invalid_locale` 为证据，并指出正式文档未同步，明确标记文档状态为 `stale`。 |
| `blocks_stale_release` | PASS | with_skill 给出 `blocked` 阶段结果，列出 stale 文档及同步文档后重新审计的待办，且未返回 `ready_for_tag`。 |
| `does_not_stamp_stale_set` | PASS | with_skill 明确未修改文档、版本元数据或 Git 历史；锁定 Git 证据显示工作区和索引均无变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=33954e4eb06eb64648933aab7efc6dc98796b5673532af2125fd493e048fc975; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别新增 locale 约束及错误响应，将文档判为 stale，并阻塞 pre-tag 审计；未执行任何写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=44596e9c57fddd810f3f3ee7492ce92b2dd4dc2924c226c528b18bd89787f8ca; snapshot_sha256=b345356b2d70a115c38d6e7b42ca5aaf29f7b17e7893583f449757f6879f5588
- Behavior: 生成了审计报告并识别文档缺少 locale 和 invalid_locale，但未呈现 suspect→事实确认流程；仅作新鲜基线对比。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补齐正式文档站基础后，更新 API 文档及验证元数据并重新运行审计。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-002-audit-stale-doc`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583` from `agents/docs/test/docs-audit/evals/workspace/eval-002-audit-stale-doc`.
- Fixture SHA-256: `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583`
- Prompt SHA-256: `a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `6c436d29e1c4d967534d387d71455397c2a958eb0e9fdd8f24d404e3a4bfc7c7`
- Eval definition SHA-256: `65171d2c00ad7205a3b92eb523639da0ae1b9b851f9b225fb39f151ac8a09d1b`
- Metadata SHA-256: `393d49433e1e9b818095a60378e27c82e27a5159f0878e57881a2872b5feee91`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | PASS | The locked audit states the change-map match, required page not changed, and classifies the page as a suspect for fact review before recording a mismatch. |
| `confirms_outdated_claim_stale` | FAIL | The report documents the required nonblank locale and invalid_locale error mismatch, but its final status is `mismatch`, not the required `stale` verdict. |
| `blocks_stale_release` | PASS | The delivered report records `phase result: blocked`, identifies the documentation evidence, gives concrete update-and-rerun work, and states no tag was created. |
| `does_not_stamp_stale_set` | PASS | The report explicitly says no pages were stamped; the delivery manifest contains only the audit file and leaves the documented version at v1.0.0 with no releases metadata update. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=fb70f8b364db2d41440017dfca7a128fa3bdcd5cf63da41d62fbcdce8b83e86e; snapshot_sha256=8e0c057aac1551d98b2f4ea03a56052835a0b981f4a48405257f61a3e8f0f9e0
- Behavior: Saved a detailed pre-tag audit, identified the undocumented locale contract, blocked release, and avoided stamping, but reported `mismatch` rather than final `stale`.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=3731d7f9cdcb3c953537bcfe1fab5144f3f8983aad3bc1feb44d3272b150ef23; snapshot_sha256=56769b47f7cb7522f6bf8f4db6e84465beeb3e1f5ab8db9467f73281705de5c6
- Behavior: Saved a shorter failed audit noting the missing locale/error documentation and unchanged last_verified_version, without the structured blocked pre-tag inventory.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill report stops at `mismatch` and does not make the required final `stale` determination.
- Next: Update the with_skill audit result to explicitly classify the confirmed documentation mismatch as `stale` while retaining the evidence and release block.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-002-audit-stale-doc`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583` from `agents/docs/test/docs-audit/evals/workspace/eval-002-audit-stale-doc`.
- Fixture SHA-256: `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583`
- Prompt SHA-256: `a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `6c436d29e1c4d967534d387d71455397c2a958eb0e9fdd8f24d404e3a4bfc7c7`
- Eval definition SHA-256: `65171d2c00ad7205a3b92eb523639da0ae1b9b851f9b225fb39f151ac8a09d1b`
- Metadata SHA-256: `393d49433e1e9b818095a60378e27c82e27a5159f0878e57881a2872b5feee91`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | PASS | With-skill report explicitly says the unchanged required page is a suspect for fact review, not automatically stale, and includes an affected-page fact review. |
| `confirms_outdated_claim_stale` | FAIL | With-skill report concludes the page is `mismatch`, explicitly stating the older verification metadata is not by itself stale; it does not ultimately classify the documentation as `stale`. |
| `blocks_stale_release` | FAIL | The report gives concrete documentation-update actions, concludes `blocked`, and states advancement to `ready_for_tag` is not permitted, but its evidence is labeled `mismatch` rather than `stale`. |
| `does_not_stamp_stale_set` | PASS | The locked delivery snapshot states unified stamp was not performed, no page was changed, and `.meta/releases.json` is missing. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=95e87f363af063175e37fbed61ae1e5b3a96fee2c603a434822a91b14f337442; snapshot_sha256=22708c8b19593df6dfb4f6c6948bd32c05e5d147d1589914e39f92483a268a8f
- Behavior: Correctly separates deterministic suspect detection from fact review, identifies the undocumented locale contract, and blocks pre-tag release without stamping; however, it stops at `mismatch` instead of confirming `stale`.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=e1757a6e5732de517c9820a0d9ae7f18c7ca6b48b7b3c5ba08726b210274bc76; snapshot_sha256=73dde36157b7f3ac30dca789952caa87ec50c8a85b70848edf0c0f34ae640b1a
- Behavior: Recognizes missing locale documentation and reports a release failure, but does not demonstrate the suspect-to-fact-layer distinction and incorrectly treats verification metadata as requiring immediate update.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- confirms_outdated_claim_stale
- blocks_stale_release
- Next: Classify the confirmed documentation mismatch as `stale` in the fact-layer result and report stale evidence explicitly while retaining the blocked pre-tag outcome.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-002-audit-stale-doc`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583` from `agents/docs/test/docs-audit/evals/workspace/eval-002-audit-stale-doc`.
- Fixture SHA-256: `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583`
- Prompt SHA-256: `a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `65171d2c00ad7205a3b92eb523639da0ae1b9b851f9b225fb39f151ac8a09d1b`
- Metadata SHA-256: `393d49433e1e9b818095a60378e27c82e27a5159f0878e57881a2872b5feee91`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | PASS | With-skill report states the change-map matched, the required page was unchanged, and it was a suspect requiring fact review. |
| `confirms_outdated_claim_stale` | FAIL | The report documents the conflicting locale facts and labels the conclusion `mismatch`, but does not ultimately classify the page as `stale`. |
| `blocks_stale_release` | PASS | The delivered report includes detailed evidence of the outdated documentation, concrete documentation-sync and rerun follow-ups, result `blocked`, and no `ready_for_tag` result. |
| `does_not_stamp_stale_set` | PASS | The locked report states no page was stamped and no release metadata was created; git evidence shows only the untracked report was added and no tracked files were changed. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=f9af684fba6b22f0d1e35b4de192138ff3633c85a409c529936a4f72ac3330e7; snapshot_sha256=80cd7d346194a9adf29401d68eb27f318e1e0c99c858b52a73cf27f0dac0e897
- Behavior: Produced a detailed blocked pre-tag audit with change-map matching, suspect review, API fact evidence, follow-up blockers, and no stamping or release mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=707a7546a784eba9a04118b5beb857b0e6ee1684687344646be8a51ebb3bb3a8; snapshot_sha256=ce02eec864b3079221a8eb9893982fcaab5b2ca0cee77bf6345c4eb7f9e6d7c9
- Behavior: Produced a shorter blocked audit identifying the missing locale/error documentation and old verification version, with an untracked report.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill report does not make the required final `stale` classification.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-002-audit-stale-doc`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583` from `agents/docs/test/docs-audit/evals/workspace/eval-002-audit-stale-doc`.
- Fixture SHA-256: `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583`
- Prompt SHA-256: `a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d339a8370a29b3fb2a69aa1879b1226165ec088d306a4e2e7a01258df2326973`
- Skill overlay SHA-256: `0bc7243cbb5cff3e77d9ba448e020a1a1f279639f8db6a365faac208b8e1dcc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `65171d2c00ad7205a3b92eb523639da0ae1b9b851f9b225fb39f151ac8a09d1b`
- Metadata SHA-256: `393d49433e1e9b818095a60378e27c82e27a5159f0878e57881a2872b5feee91`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | NOT_EXERCISED | The with_skill report proves the change-map match and documentation mismatch, but locked evidence does not prove the hidden deterministic-layer label `suspect` or its handoff to the fact layer. |
| `confirms_outdated_claim_stale` | PASS | The report cites the required nonblank `locale` and `400 invalid_locale` code evidence, and confirms the API documentation is out of sync. |
| `blocks_stale_release` | PASS | The report records the documentation mismatch, gives concrete remediation blockers, sets `phase_result: blocked`, and explicitly states no `ready_for_tag` result is valid. |
| `does_not_stamp_stale_set` | PASS | The report states the unified stamp was not performed, the page remains at `v1.0.0`, and no version metadata was changed; git evidence shows no such mutation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=33b5a37f0b396829b5a179b554e0129df759ee5fdc447dd26be29a74f1d2a31f; snapshot_sha256=59e2f0516951256d7b1abf05184f62d823254c8dcaf0efc18dbc4b13b467bd39
- Behavior: Produced a saved structured pre-tag audit report identifying the code/documentation mismatch, blocking release, and avoiding version stamping.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=eaebc592702b94714213bd6027212e4464771439ff92d623d28ca1354bd5ae69; snapshot_sha256=af86f0ef59eefd11f44269bce91e9cf6f6bb3223b96117592be99bcac9aa3def
- Behavior: Produced a saved FAIL report identifying the missing locale documentation and unchanged last_verified_version, but did not provide the structured blocked audit evidence.
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
- Eval: `eval-002-audit-stale-doc`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583` from `agents/docs/test/docs-audit/evals/workspace/eval-002-audit-stale-doc`.
- Fixture SHA-256: `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583`
- Prompt SHA-256: `a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9e9abf391c9ccd9564d35b5def50bc0374b1db0886710676c4d48422839746ae`
- Skill overlay SHA-256: `c66ac938bf9158faa694d7c3e311e913ddc4a06da11de703a881234f257c470c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `65171d2c00ad7205a3b92eb523639da0ae1b9b851f9b225fb39f151ac8a09d1b`
- Metadata SHA-256: `393d49433e1e9b818095a60378e27c82e27a5159f0878e57881a2872b5feee91`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | PASS | With-skill report explicitly says the required page was not updated in the same diff and was classified as `suspect` for fact review. |
| `confirms_outdated_claim_stale` | PASS | The report uses `mismatch` as the final status but semantically confirms the stale documentation claim, citing the required `locale` parameter and `invalid_locale` response. |
| `blocks_stale_release` | PASS | Report cites the documentation discrepancies, gives concrete synchronization and re-audit actions, sets result to `blocked`, and states `ready_for_tag` was not reached. |
| `does_not_stamp_stale_set` | PASS | Report explicitly says not to stamp `last_verified_version` and raw evidence shows only the audit report was added; no release metadata or document stamp was updated. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=7a40f3069dc106f58a03ae070df04874079afc2c95a98b6d348d966fa92cc20a; snapshot_sha256=0163df8acd4a4fbd5aae64773f9a2d7ab89c791b3745d5278923ad4bbc137fda
- Behavior: Saved a detailed audit report that classifies the missing required documentation as suspect, confirms the mismatch from code evidence, blocks release, and avoids stamping.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=0e4c6ae4c42eb8e5be3e34d5642da7d845f462df9cf352d1a53b0ea82031367b; snapshot_sha256=8c928145a85f2b000839ead54287f6c3dcef460bd8f2d0c416e49efa6ff97d44
- Behavior: Produced a saved audit report and identified the missing locale documentation, but did not expose the suspect-to-fact-review classification or the full release-audit evidence.
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
- Eval: `eval-002-audit-stale-doc`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583` from `agents/docs/test/docs-audit/evals/workspace/eval-002-audit-stale-doc`.
- Fixture SHA-256: `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583`
- Prompt SHA-256: `a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2d24da5f976a5ab2710c2c072a19015e074d314e0ebdb88f1c28831425f1b98c`
- Skill overlay SHA-256: `40330c17a3b77f25a1b1a716fa5e9355e0011db79d19014344ed516affba11c8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `65171d2c00ad7205a3b92eb523639da0ae1b9b851f9b225fb39f151ac8a09d1b`
- Metadata SHA-256: `393d49433e1e9b818095a60378e27c82e27a5159f0878e57881a2872b5feee91`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | PASS | with_skill 报告明确将未修改的受影响页面作为 suspect 页面审查，并随后进行页面事实核验，没有仅因缺少同批文档更新直接判 stale。 |
| `confirms_outdated_claim_stale` | FAIL | with_skill 报告确认代码与文档不一致并判为 mismatch，但没有最终将该页面判为 stale。 |
| `blocks_stale_release` | PASS | 报告列出 v1.0.0 验证元数据、缺失 locale 与 invalid_locale 文档等阻断证据，要求修正文档后以新的 target_ref 重审；phase_result 为 blocked，且明确不可用 ready_for_tag。 |
| `does_not_stamp_stale_set` | PASS | 报告显示 pre-stamp last_verified_version 仍为 v1.0.0，明确未执行统一 stamp，且没有更新页面或 .meta/releases.json。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=ab7b78f6885b6d4c25c74e3cc5f3bda20059325cae7e74db672355ea47d69bcb; snapshot_sha256=7e120dddbfc61d487253f0f9a241f59f59cd22a6bc313aea0be36a5ed739c74e
- Behavior: 执行了 change-map 影响分析、suspect 页面事实核验和 pre-tag 阻断审计；最终使用 mismatch 而非 stale 作为页面结论。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=142e39447a9dad691da7c97854e637b3dbda59d3cfbec9a9b522c2dc2fec5565; snapshot_sha256=f658059eff62ced8a85067e3a9787d95a14b82130261ecaf03a9b35d3be1dae2
- Behavior: 发现 locale、invalid_locale 及验证版本问题并生成 FAIL 报告，但未呈现 suspect→事实层→stale 的分层审计过程，也未列出 blocked/ready_for_tag 状态。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未将文档与新增必填 locale 参数及 invalid_locale 错误的不一致最终判为 stale。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-002-audit-stale-doc`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583` from `agents/docs/test/docs-audit/evals/workspace/eval-002-audit-stale-doc`.
- Fixture SHA-256: `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583`
- Prompt SHA-256: `a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `65171d2c00ad7205a3b92eb523639da0ae1b9b851f9b225fb39f151ac8a09d1b`
- Metadata SHA-256: `393d49433e1e9b818095a60378e27c82e27a5159f0878e57881a2872b5feee91`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | PASS | with_skill 报告明确指出同批更新缺失时页面 initially `suspect`，随后送事实核查。 |
| `confirms_outdated_claim_stale` | FAIL | with_skill 报告确认代码与文档事实冲突，但将页面标为 `mismatch`，未最终明确判为 `stale`。 |
| `blocks_stale_release` | PASS | 报告结果为 `blocked`，列出补正文档并重新审计的待办，且明确未返回或执行 `ready_for_tag`。 |
| `does_not_stamp_stale_set` | PASS | 报告明确称完整受影响集合未验证、未应用统一 stamp，并确认未创建 releases.json、候选提交或 tag。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=b030d1e86d7242d191951ae6412a140d1481c25cbfebc732e6263ec383bae6f6; snapshot_sha256=b8a26cb4406a1e570e886300425fb1c454d3fd61aba6804f31d1a8879efd36fd
- Behavior: 执行了 change-map 命中、suspect 后事实核查、blocked 发布决策及不盖章处理；未明确使用 stale 作为最终页面状态。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=09ffcb1aaf68507bf0af2f9a7d2032c6ba42864435baee8b7d7fbe5600c59890; snapshot_sha256=db5b514831063871e48e5a8bd4d595e73669725b3a3b746ffce366ba1ae78da7
- Behavior: 识别了 locale 文档缺失，但直接建议更新 last_verified_version，未体现 suspect 到事实层的确定性流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- confirms_outdated_claim_stale 未满足：with_skill 报告使用 `mismatch` 而非最终 `stale` 状态。
- Next: 将事实层确认后的页面状态明确记录为 `stale`，并保留 locale 与 invalid_locale 的代码证据。

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
- Eval: `eval-002-audit-stale-doc`

## Test Set / Fixture Version

- Fixture version: docs-audit A2 / 2026-07-19
- Assertions: 4

## Latest Result

- Overall result: PASS
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `PASS` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `marks_missing_doc_update_suspect` | PASS | FAIL | with_skill 报告明确写明 required page 的确定性状态为 `suspect`，随后事实层判为 `stale`；without_skill 直接判为 stale，未标记 `suspect`。 |
| `confirms_outdated_claim_stale` | PASS | PASS | 两条 lane 均核对 `src/catalog/routes.txt`：新增必填非空 `locale` 与 `400 invalid_locale`，而 `catalog.md` 未声明，均确认文档为 stale。 |
| `blocks_stale_release` | PASS | FAIL | with_skill 报告 frontmatter 为 `phase_result: blocked`，并明确“不可 `ready_for_tag`”；without_skill 仅为 `status: fail`，未形成 pre-tag `blocked` 结果。 |
| `does_not_stamp_stale_set` | PASS | PASS | 两条 lane 的 `catalog.md` 和 `change-map.yaml` 仍为 `last_verified_version: v1.0.0`，且均不存在或更新 `.meta/releases.json`；报告也明确未执行版本戳更新。 |

未满足断言（with/without 任一 FAIL）：``marks_missing_doc_update_suspect``、``blocks_stale_release``



## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | PASS | required doc 未同批更新时仅标 `suspect` 并送事实层，没有直接等同于 stale。 |
| `confirms_outdated_claim_stale` | PASS | 当前代码要求非空 `locale` 并定义 400 `invalid_locale`，文档遗漏，事实层判 `stale`。 |
| `blocks_stale_release` | PASS | 报告列出同步文档、补齐 release surfaces、重审的待办，结果 `blocked`。 |
| `does_not_stamp_stale_set` | PASS | 页面版本保持 `v1.0.0`，未创建或修改 `.meta/releases.json`。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮 fresh session `019f7a73-2dfe-7763-a3a0-e6156e81de1b`，位于 `tmp/eval-runs/117/eval-002-audit-stale-doc/with_skill/`。
- 候选持久化契约路径报告，清楚区分确定性 `suspect` 与事实层 `stale`。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮独立 fresh session `019f7a77-668b-7f93-b7db-5e4a32d4d4d0`，同一 prompt 与 pristine fixture；未复用历史 baseline。
- baseline 同样识别 stale 和 blocked，但报告位于 `.eval/audit-report.md`，未完整体现版本表面与契约化报告路径。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure。合成 refs 通过 `.eval/actual-diff.patch` 复现，属于 harness 限制，不是协议缺陷。

## Next Steps

- 保留本结果；suspect/stale 判定规则变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
