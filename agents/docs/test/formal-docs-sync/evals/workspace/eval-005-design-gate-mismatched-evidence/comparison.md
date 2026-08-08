# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-005-design-gate-mismatched-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-005-design-gate-mismatched-evidence`.
- Fixture SHA-256: `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f`
- Prompt SHA-256: `cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a0fd1ad6b8713d6036307d1b20788b4771cc4b6ba53645fe17625e0dd55bbb5b`
- Skill overlay SHA-256: `73e88fe8c07f988c3353f81f9b058d4f8350c48ee381f924fe8c8201b9f92bb4`
- Judge schema SHA-256: `c9b93b28ac72af6810f4752921bb72d418af8d9162ae5d66c15fe90f929562c8`
- Eval definition SHA-256: `9b46c27014c750c2c7c902ee9b735c340d6216e70bd1db10e9ac7cfe4ffa72b8`
- Metadata SHA-256: `8201495b57b213f9db3f5219d86222ff877b211b7bfe7d5c149fe15482812507`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_evidence_mismatch` | PASS | with_skill 明确识别请求/计划为 `preferences-summary`，而 PRD/TRD frontmatter 为 `account-preferences`，状态为 blocked，confirmed_batch 为无且零写入。 |
| `design_zero_change` | PASS | with_skill 的 `delivery_snapshot` 为空，git status/diff 均为空，并明确报告 design 页面与 change-map 为 zero-write。 |
| `routes_to_owner` | PASS | with_skill 将 PRD 归属冲突路由给 `pm-agent`，将 TRD feature path/impact 冲突路由给 `engineer-agent:trd-gen`，要求统一后重试。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=1696808b65841adebaec99b52d2ebfe04351b7170cb2bdf7d4e6f1121ad10653; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别证据链冲突并阻断同步，保持工作树零修改，路由给对应 owner。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=0a0dd8905267bb579e8109cdb41ed144f86b07f427320308725a8e8107b39e04; snapshot_sha256=e7a6ced1964efb2365fdc3dc91c2be0cdd930c840d1bcaa0cc5f7c8e5e293a26
- Behavior: 直接完成文档与 change-map 写入，未因 PRD/TRD feature_path 不一致而阻断。
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
- Skill: `formal-docs-sync`
- Eval: `eval-005-design-gate-mismatched-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-005-design-gate-mismatched-evidence`.
- Fixture SHA-256: `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f`
- Prompt SHA-256: `cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `c9b93b28ac72af6810f4752921bb72d418af8d9162ae5d66c15fe90f929562c8`
- Eval definition SHA-256: `9b46c27014c750c2c7c902ee9b735c340d6216e70bd1db10e9ac7cfe4ffa72b8`
- Metadata SHA-256: `8201495b57b213f9db3f5219d86222ff877b211b7bfe7d5c149fe15482812507`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_evidence_mismatch` | PASS | With-skill output explicitly compares request/plan `preferences-summary` against PRD/TRD `account-preferences`, identifies the conflict, and reports blocked with no confirmed batch or writes. |
| `design_zero_change` | PASS | With-skill git evidence shows empty status and diff; output explicitly reports both design and change-map files were not modified. |
| `routes_to_owner` | PASS | With-skill output routes the PRD conflict to `pm-agent` and TRD path/impact alignment to `engineer-agent:trd-gen`, requiring alignment before retry without guessing. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=4240495ddef735c7df44443b46ae10b5104c7016760bab923d1e72b654966c40; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Detected the feature-path evidence conflict, blocked before writing, preserved both design artifacts, and routed remediation to the appropriate owners.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=d31a1827d6b6fc6ccefed4f62f76a34877fb43faf932873233742517a2096795; snapshot_sha256=db4989e09d8bf4284f35b97e4221c147701506227a25a2afa83c41978138460e
- Behavior: Fresh baseline proceeded with both documentation changes despite the feature-path mismatch.
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
- Skill: `formal-docs-sync`
- Eval: `eval-005-design-gate-mismatched-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-005-design-gate-mismatched-evidence`.
- Fixture SHA-256: `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f`
- Prompt SHA-256: `cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `e1b96c87b6eb051a20a849fc51ca738b49866387566d5f61a7cdde4f1fc422cd`
- Skill overlay SHA-256: `44e860f93f5d468075d88a048afe986ad68fcbae84270ffdc4d5a090573d59b8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9b46c27014c750c2c7c902ee9b735c340d6216e70bd1db10e9ac7cfe4ffa72b8`
- Metadata SHA-256: `8201495b57b213f9db3f5219d86222ff877b211b7bfe7d5c149fe15482812507`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_evidence_mismatch` | PASS | With-skill output identifies the request/plan path as `preferences-summary` and PRD/TRD metadata as `account-preferences`, marks the gate blocked, confirms no batch, and states no synchronization/write occurred. |
| `design_zero_change` | PASS | With-skill locked evidence shows an empty delivery snapshot and empty git status/diff; output states no write was made. The delivered design and change-map files therefore remained unchanged. |
| `routes_to_owner` | FAIL | The output routes the PRD/TRD conflict together to `pm-agent` and separately mentions `docs-site-bootstrap`; it does not route the TRD path/impact alignment to Engineer or `trd-gen` as required. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=ccf2b41f3e53eae3a03930bf37018004c90c19b016761485f54bdeb5744ba3ea; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Blocked before synchronization and writes after detecting the feature-path mismatch, but incompletely routed the ownership correction.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=baec6f2e423bae38799807aa1be6dbdfad1d4aea241bca91eb95f1905e91f1ca; snapshot_sha256=80d7c7d2d2a0d2332c02cd1aa5e16af33bc44e49143cda4c76404419807419fd
- Behavior: Proceeding baseline: edited both design files despite acknowledging the feature-path mismatch.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill lane failed to route the TRD alignment issue to Engineer/trd-gen.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-005-design-gate-mismatched-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-005-design-gate-mismatched-evidence`.
- Fixture SHA-256: `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f`
- Prompt SHA-256: `cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a612d50c32b84c65fad3cad08aad2d416a3a33647abfa1462784c1e58022424b`
- Skill overlay SHA-256: `e55ecf59b3cd8d90a2ed4cf555bed2ad2fc2131494e0914246a868317b68f4e8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9b46c27014c750c2c7c902ee9b735c340d6216e70bd1db10e9ac7cfe4ffa72b8`
- Metadata SHA-256: `8201495b57b213f9db3f5219d86222ff877b211b7bfe7d5c149fe15482812507`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_evidence_mismatch` | PASS | With-skill output explicitly contrasts the request/plan path `preferences-summary` with PRD/TRD `account-preferences`, identifies the conflict, blocks the closeout, and states that no files were modified. |
| `design_zero_change` | PASS | With-skill output states no files were modified and reports empty git status/diff, establishing zero change to both the design page and change-map. |
| `routes_to_owner` | FAIL | The output routes metadata unification to `pm-agent` but does not route TRD path/impact-domain alignment to Engineer / `trd-gen` as required. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=87fa35658cb679bef68d64191a87eeeb73b842ec2a94975d39b263aba9e60dff; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocked before writing on the path mismatch, but incompletely routed remediation ownership.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=a26e8464caaf962087c040e3e4ac051ef55edb967fd4143c52bfa76e1b0f4476; snapshot_sha256=91e3b9866e5a5d77c12441326f5ba000ee18f19f82b909f0162727ea9316ccdf
- Behavior: Incorrectly completed and modified both design and change-map files despite the feature-path conflict.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- TRD remediation was not routed to Engineer / trd-gen; the output instead broadly assigned metadata unification to pm-agent.
- Next: Route the PRD conflict to the PM owner and the TRD path/impact alignment to Engineer / trd-gen, requiring all metadata to align before retrying.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-005-design-gate-mismatched-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-005-design-gate-mismatched-evidence`.
- Fixture SHA-256: `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f`
- Prompt SHA-256: `cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `52db6badcefada59a1d42e81de2581f06256f43c060b7699c281ab21bfb40949`
- Skill overlay SHA-256: `f896903fa1a8ae6886eb0b6365065625a2e60f6809acd0af6c7c8dc8f8f2bd40`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9b46c27014c750c2c7c902ee9b735c340d6216e70bd1db10e9ac7cfe4ffa72b8`
- Metadata SHA-256: `8201495b57b213f9db3f5219d86222ff877b211b7bfe7d5c149fe15482812507`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_evidence_mismatch` | PASS | with_skill 明确指出请求/计划使用 preferences-summary，而 PRD/TRD frontmatter 使用 account-preferences，将其判为 feature identity 未闭合，并说明在范围确认和写入前阻塞。 |
| `design_zero_change` | PASS | with_skill 输出声明未修改任何文件；其 git_status、git_diff、delivery_snapshot 均为空，符合 design 页及 change-map 原子范围零变化。 |
| `routes_to_owner` | PASS | with_skill 要求由 PM/Engineer 先将 PRD/TRD 对齐到同一 feature_path，并要求对齐后再重试，未自行猜测正确路径；这语义上覆盖 PM 与 Engineer/trd-gen 的责任分流。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=42eacb2b6b84004214f64a3b1e150509a8fcf7869797b86aab41a30d7502d4df; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别请求/计划与 PRD/TRD 的 feature_path 冲突，在写入前阻断，保持工作区无变化，并要求 PM/Engineer 先完成证据链对齐。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=d8050d4403ebda5329cd2236b7df69328e28ac1fee1437667c9d721e27029601; snapshot_sha256=7b12d0bfeff48cdac30646d4b3a78665c1f7d6fb377734f6ca23dcf8d4da9c3a
- Behavior: 错误地将 account-preferences 视为命名偏差，继续同步并修改 design 页及 change-map。
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
- Skill: `formal-docs-sync`
- Eval: `eval-005-design-gate-mismatched-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-005-design-gate-mismatched-evidence`.
- Fixture SHA-256: `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f`
- Prompt SHA-256: `cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1e290565a84b926a128928ccdd91365a2235adff18f999307c0a3553f0b41f34`
- Skill overlay SHA-256: `0c6a49eed1db242a95632eb0d142c1760f60ffc995c96026908ec8c0e6bd8d63`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9b46c27014c750c2c7c902ee9b735c340d6216e70bd1db10e9ac7cfe4ffa72b8`
- Metadata SHA-256: `8201495b57b213f9db3f5219d86222ff877b211b7bfe7d5c149fe15482812507`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_evidence_mismatch` | PASS | With_skill explicitly contrasts preferences-summary in the request/plan with account-preferences in PRD/TRD, identifies the metadata mismatch, and reports blocking before any write. |
| `design_zero_change` | PASS | With_skill reports no document writes, empty git status/diff, and explicitly states both the design page and change-map remain unchanged. |
| `routes_to_owner` | FAIL | It requests PM/Engineer alignment and retry, but does not specifically route the PRD conflict to the PM owner and the TRD path/impact-domain alignment to Engineer/trd-gen. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=f69babe8b201ddd4df748f4c29c8747ca66013a3c331e0506eaa9d8b87aa38ea; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocked the sync and preserved both design artifacts, but gave only a broad PM/Engineer routing request rather than the assertion's explicit owner routing.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=89913b5858fb968c4262198be429b334ca16408cac2127351d52106f9237e9ff; snapshot_sha256=1e91c4c0a0f9a046994648cfdc5dc55b103bec2a019396c0884dbfb260276278
- Behavior: Ignored the feature-path mismatch, treated it as non-blocking, and modified both required design artifacts.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- routes_to_owner was not fully satisfied because the required specific PM and Engineer/trd-gen routing was absent.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-005-design-gate-mismatched-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-005-design-gate-mismatched-evidence`.
- Fixture SHA-256: `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f`
- Prompt SHA-256: `cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9b46c27014c750c2c7c902ee9b735c340d6216e70bd1db10e9ac7cfe4ffa72b8`
- Metadata SHA-256: `8201495b57b213f9db3f5219d86222ff877b211b7bfe7d5c149fe15482812507`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_evidence_mismatch` | PASS | with_skill 明确对比了 handoff/计划中的 preferences-summary 与 PRD/TRD frontmatter 中的 account-preferences，判定为 feature_path 冲突，并在写入前阻塞。 |
| `design_zero_change` | PASS | with_skill 明确报告设计页和 change-map 均未写入；git_status 与 git_diff 均为空。 |
| `routes_to_owner` | FAIL | with_skill 仅笼统要求 PM/Engineer 对齐 PRD/TRD，未明确将 PRD 冲突路由给 PM owner、将 TRD 冲突路由给 Engineer / trd-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=96ad6a1ad4e196cfd84aaedd21c60d71e9458a5787528846a85e050c361b7680; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别 feature_path 冲突并在写入前阻断，保持目标文件零变化，但 owner 路由不够具体。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=8bffa1ce5864ad783ce8bc58c4b3cdb4d9fef4e599d3b9721f6ce3e5762f5ebf; snapshot_sha256=bb8fd2943cdde7f9581c093a0229154512b27022ef295f7015350cdf537b4367
- Behavior: 进行了写入并保留已知 feature_path 风险，未阻断不一致证据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未按断言要求分别明确路由 PRD 至 PM owner、TRD 至 Engineer / trd-gen。
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

- Skill: `formal-docs-sync`
- Eval: `eval-005-design-gate-mismatched-evidence`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `blocks_on_evidence_mismatch` | PASS | PASS | 两条 lane 均明确对比 handoff/计划的 `preferences-summary` 与 PRD/TRD 的 `account-preferences`，并停止同步；证据见各自 `result.txt` 与 `PRD.md`/`TRD.md`。 |
| `design_zero_change` | PASS | PASS | 两个目标文件内容均保持原样；`.eval/actual-diff.patch` 仅包含 `src/preferences_summary.py` 新增，不包含 design 文档或 change-map 修改。 |
| `routes_to_owner` | FAIL | FAIL | with_skill 仅路由给 `pm-agent`，未明确路由 Engineer / `trd-gen`；without_skill 仅要求统一 PRD/TRD，未指定 PM owner 与 Engineer / `trd-gen` 双 owner 路由。 |

未满足断言（with/without 任一 FAIL）：``routes_to_owner``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 只加载 design 模块，识别 PRD/TRD/实际路径证据不一致。
- design 页面与映射零变化，并分别指出 PM 与 Engineer/trd-gen 的修复责任。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 全新 baseline 在本 fixture 上也满足 3/3，说明该阻塞信号本身足够明显。
- with-skill 的价值主要体现在稳定的 owner 和双面门禁表达。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- with-skill 无 assertion failure。

## Next Steps

- 保留作为明显冲突的安全网回归用例。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
