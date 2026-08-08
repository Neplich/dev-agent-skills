# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-004-feature-path-report`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c` from `agents/security/test/appsec-checklist/evals/workspace/eval-004-feature-path-report`.
- Fixture SHA-256: `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c`
- Prompt SHA-256: `05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `33e7e73c99fb4e7a6f2d6ab5104b8298fc067235a29614a6e32ee61035051666`
- Judge schema SHA-256: `a8797f637904fc863710b298fe2fad8220a05aa0d79e70ed8997096bddf38e6c`
- Eval definition SHA-256: `cea867306caa7c154c38a57a7085c1f3dc292e28eb28f571e99034334c62710c`
- Metadata SHA-256: `8529cb6cbe6ab9523b4f7cf3b65440375e54cbaab5ce6a8376eb7a3bc4427f65`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_same_path_pm_engineer_docs` | PASS | Locked report lists the PRD, TRD, and IMPLEMENTATION_PLAN under the required feature path. |
| `writes_nested_security_report` | PASS | Delivery snapshot contains docs/security/chat-interface/messages/history/search/appsec-checklist.md. |
| `includes_feature_path_frontmatter` | PASS | Report frontmatter contains the required feature_path, parent_feature, and feature_level values. |
| `does_not_invent_feature_directory` | PASS | The report uses the existing nested feature directory and does not invent a top-level synonym. |
| `escalates_fact_changing_conclusion_to_pm` | PASS | Report includes a PM escalation payload, assigns classification and issue filing to pm-agent, and excludes direct Security issue filing. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=6b7262db05e1cca1463380d76b3675fa6a2d9fcfca23607a98b5f346fe1c6ae1; snapshot_sha256=89badf4bee0864d9005220165ddc48bbdbb8f3aa39ed1e4b484e9bd2be1df3dc
- Behavior: Created the correctly nested Security report with required frontmatter, documented the security findings, and included PM escalation evidence.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=d3ccb6fc325c212284af035ff05da713930c3aecc54fb8cf6bce0a1f695706ad; snapshot_sha256=7078a4a1bc6e57b28363079a63cc42fc5f9b39910d51e8c20da66bf8f9f161d8
- Behavior: Created an engineer-path SECURITY_REVIEW.md instead of the required nested Security report and did not provide the required PM escalation handoff.
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

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-004-feature-path-report`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c` from `agents/security/test/appsec-checklist/evals/workspace/eval-004-feature-path-report`.
- Fixture SHA-256: `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c`
- Prompt SHA-256: `05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `33e7e73c99fb4e7a6f2d6ab5104b8298fc067235a29614a6e32ee61035051666`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `cea867306caa7c154c38a57a7085c1f3dc292e28eb28f571e99034334c62710c`
- Metadata SHA-256: `8529cb6cbe6ab9523b4f7cf3b65440375e54cbaab5ce6a8376eb7a3bc4427f65`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_same_path_pm_engineer_docs` | NOT_EXERCISED | The delivered report references the required PRD, TRD, and implementation plan and states they were in scope, but the locked evidence cannot prove the hidden act of reading them. |
| `writes_nested_security_report` | PASS | The with_skill delivery snapshot contains docs/security/chat-interface/messages/history/search/appsec-checklist.md, matching the required nested path. |
| `includes_feature_path_frontmatter` | PASS | The delivered file frontmatter contains feature_path: chat-interface/messages/history/search, parent_feature: chat-interface/messages/history, and feature_level: 4. |
| `does_not_invent_feature_directory` | PASS | The feature path is aligned with the PM/Engineer documentation paths, and the report was written under the corresponding nested Security path rather than an invented top-level synonym. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The report recommends PM-agent classification and PM-owned issue filing, but the locked evidence does not prove that the handoff and issue creation occurred. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=7eb57478fb318098a63d74bbec4dde1dc962eed8f09ec22048aceb9e8afa25ce; snapshot_sha256=363f23bb57ef91f850ec502ed1dceb366cef23150c4cabf3db48d709436e42a0
- Behavior: Produced the required nested Security report with matching feature frontmatter, documented the SQL injection and authorization concerns, and recommended PM-agent escalation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=62854786896fcf45b450aab15796621fe9359db87efc6b4baf2784e06b44e8eb; snapshot_sha256=86e37802041d7561a463eba960b54edb81e1e2fc103d175914d13b6e725356ef
- Behavior: Produced a security report under the incorrect engineer documentation path and did not use the required nested Security report path.
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

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-004-feature-path-report`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c` from `agents/security/test/appsec-checklist/evals/workspace/eval-004-feature-path-report`.
- Fixture SHA-256: `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c`
- Prompt SHA-256: `05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `5b2b2b7a3b96eded32c11959c382e7fa8aafb204f59c1c353154bae2cdaf9c71`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `cea867306caa7c154c38a57a7085c1f3dc292e28eb28f571e99034334c62710c`
- Metadata SHA-256: `8529cb6cbe6ab9523b4f7cf3b65440375e54cbaab5ce6a8376eb7a3bc4427f65`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_same_path_pm_engineer_docs` | PASS | The with_skill report explicitly lists and cites the PRD, TRD, and IMPLEMENTATION_PLAN at the required paths. |
| `writes_nested_security_report` | PASS | Raw delivery evidence shows the report at docs/security/chat-interface/messages/history/search/appsec-checklist.md; no forbidden alternative path was used. |
| `includes_feature_path_frontmatter` | PASS | The report frontmatter contains feature_path: chat-interface/messages/history/search, parent_feature: chat-interface/messages/history, and feature_level: 4. |
| `does_not_invent_feature_directory` | PASS | The required same-path fixture documents exist, and the with_skill output used the established nested feature path. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The locked evidence shows a recommendation to return the conclusion to pm-agent and create a fix item, but does not prove an actual fact-changing conclusion requiring issue creation or the subsequent issue action. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=c7f34abb4e1ae2f4f346b5185589e1efd898ddbf54fe5783fed4e77440a03d39; snapshot_sha256=7cdc1ec3f7edb7ab7c56b2662cffd9198b0b5684d31a3af8f3e6fdf4f6e6edd4
- Behavior: Produced the correctly nested appsec checklist with required frontmatter, cited all three feature documents, documented the SQL injection and authorization risks, and recommended PM escalation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=960272fbd912ff7c97332395ec46ab565df732132213d2591bacf8eac33601b7; snapshot_sha256=ab7b695d301555302a6a7a62fbdba504257b3f96fca756baa0056aeef1f4a486
- Behavior: Produced an engineer-directory SECURITY_REVIEW.md, omitted the required security report location and required escalation wording, while identifying key security risks.
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

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-004-feature-path-report`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c` from `agents/security/test/appsec-checklist/evals/workspace/eval-004-feature-path-report`.
- Fixture SHA-256: `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c`
- Prompt SHA-256: `05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `812b371fc30792cb2b0cf8d96079b3244c95b93efab7638e085d4e955d6ea42c`
- Skill overlay SHA-256: `5b2b2b7a3b96eded32c11959c382e7fa8aafb204f59c1c353154bae2cdaf9c71`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `cea867306caa7c154c38a57a7085c1f3dc292e28eb28f571e99034334c62710c`
- Metadata SHA-256: `8529cb6cbe6ab9523b4f7cf3b65440375e54cbaab5ce6a8376eb7a3bc4427f65`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_same_path_pm_engineer_docs` | PASS | 报告明确列出并引用 PRD、TRD 和 IMPLEMENTATION_PLAN，且 with_skill workspace_manifest 包含三份原始文档。 |
| `writes_nested_security_report` | PASS | delivery_snapshot 和 git_status 均证明写入了 docs/security/chat-interface/messages/history/search/appsec-checklist.md。 |
| `includes_feature_path_frontmatter` | PASS | 报告 frontmatter 包含 feature_path、parent_feature 和 feature_level: 4，值与要求一致。 |
| `does_not_invent_feature_directory` | NOT_EXERCISED | 原始 fixture 已提供清晰且完整的同路径文档，因此未触发路径不清或文档缺失时的回 PM/Engineer 流程。 |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | 报告指出应回交 PM 并建立修复事项，但锁定证据未证明实际完成 pm-agent 分类或 issue 创建；按交互流程规则不判 FAIL。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=942be0853407561c6b1d1ac2e301174e0aef9734f7ac5b8c25e1a1009fb8b93e; snapshot_sha256=a076e2d5b649bef34139a3d965944b4908a7a58d9735e6b50c1fef51b667540f
- Behavior: 正确完成安全审查，写入嵌套 Security 报告并包含正确 feature 路径元数据，且提出了基于证据的发布阻断与 PM 升级建议。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=a34d4561adee3d6a35337018c540971d12e071034f05f6263d48c07d551b73d1; snapshot_sha256=0b602373657b41e9c86c0957c3c6da96bdb90e3e368f2100631abfcaf5532497
- Behavior: 将报告错误写入 engineer 功能目录，未提供要求的嵌套 Security 报告路径或 frontmatter。
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

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-004-feature-path-report`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c` from `agents/security/test/appsec-checklist/evals/workspace/eval-004-feature-path-report`.
- Fixture SHA-256: `258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c`
- Prompt SHA-256: `05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `095129ad5c17fd8974fdea44f1054ac02e7fa8f954b0e4a1a1d1a0ef185f9ce5`
- Skill overlay SHA-256: `5839d5cfe31d4e5dc5e9520f24a99b1147c97570ef1cc156eb90972408a49170`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `cea867306caa7c154c38a57a7085c1f3dc292e28eb28f571e99034334c62710c`
- Metadata SHA-256: `8529cb6cbe6ab9523b4f7cf3b65440375e54cbaab5ce6a8376eb7a3bc4427f65`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `uses_same_path_pm_engineer_docs` | PASS | with_skill workspace_manifest includes the PRD, TRD, and IMPLEMENTATION_PLAN at the exact required nested paths; the report also names them as review context. |
| `writes_nested_security_report` | PASS | with_skill output and delivery_snapshot show docs/security/chat-interface/messages/history/search/appsec-checklist.md. |
| `includes_feature_path_frontmatter` | PASS | The report frontmatter contains feature_path, parent_feature, and numeric feature_level 4 with the required values. |
| `does_not_invent_feature_directory` | PASS | The feature path is clear and all three same-path PM/Engineer documents exist; with_skill uses the established path and does not create a synonym directory. |
| `escalates_fact_changing_conclusion_to_pm` | NOT_EXERCISED | The evidence shows a security assessment of implementation risks, but no conclusion that changes a formal-document fact; therefore the conditional PM escalation requirement is not triggered. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=c96550f98083768a10bdeb089717d665de6862738d73b4cde3ec74db5b61791c; snapshot_sha256=b9396df19f2b611fb99b3b3d60b6da35acc93ce57bfb88d94203bd998b68fa9c
- Behavior: Reviewed the code and all three same-path feature documents, produced the required nested Security report with correct frontmatter, and documented the observed security risks.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=05538871e356a1820db883bcff8e90f4208bc94ba8410156f5ef306f19d4ce21; fixture_sha256=258d12e924889cdd6b9d64d5ae077ef75e65139845669b9a81854ba9fc13621c; output_sha256=0ffe5b1c8fdea11b438766c54c512bc283eee8087192ffc9a04b578daf8abf83; snapshot_sha256=9631b8621b81870395b2f7a88ea398dcdc18582816f3cdce893c82a0fbe76466
- Behavior: Reviewed the code and feature documents but wrote SECURITY_REVIEW.md under the Engineer feature directory; did not produce the required nested Security report or required frontmatter.
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

# Eval Result: eval-004-feature-path-report

## Evaluation Target

- Agent: `security`
- Skill: `appsec-checklist`
- Eval: `eval-004-feature-path-report`
- Test case: Feature Path Security Report
- Workspace: `workspace/eval-004-feature-path-report`
- Natural user prompt:

> 对 chat-interface/messages/history/search 做发布前应用安全检查。仓库中已有 docs/pm/chat-interface/messages/history/search/PRD.md、docs/engineer/chat-interface/messages/history/search/TRD.md 和 docs/engineer/chat-interface/messages/history/search/IMPLEMENTATION_PLAN.md。

- Expected artifact: 读取同一 feature_path 下的 PM/Engineer 文档，输出 docs/security/chat-interface/messages/history/search/appsec-checklist.md，frontmatter 包含 feature_path，不生成 docs/security/history-search/appsec-checklist.md 或 docs/security/chat-interface/history-search/appsec-checklist.md。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-06 23:45:35 至 2026-08-07 00:13:31（Asia/Shanghai）。
- Runtime root: `/tmp/security-fresh-evals-20260806-n3l1anp1/appsec-checklist--eval-004-feature-path-report/`。
- Fixture identity: 两条 lane 的初始 fixture manifest 完全相同，SHA-256 为 `c7233a79d75e848f621326abec96afbba234cf0071a3c7333681db1dbb0d397a`。
- Lane isolation: 先完成并销毁全部 `without_skill` 独立顶层临时目录，再创建任何 `with_skill` 目录；每条 lane 使用独立的顶层临时 workspace、`HOME` 与 `CODEX_HOME`，不存在可供另一条 candidate 读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt 与相同初始 fixture；仅 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 skill，`without_skill` 未安装任何目标 skill。
- Evidence isolation: 所有 candidate 会话结束并删除各自临时根后，才将内存中的最终 workspace 快照与 transcript 持久化到 runtime root；candidate transcript 泄漏扫描未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、judge/verdict 或 expected output/assertion 脚手架。
- Judge: candidate 全部结束后，由第三个独立、只读的 fresh Codex 会话依据当前 assertions、两条 candidate 输出、transcript 与最终 workspace 快照判定。

## Latest Result

- Behavior result: **FAIL**（PASS 3 / FAIL 1 / NOT EXERCISED 1）
- Coverage result: **PARTIAL**
Overall result: FAIL

## Historical Contract Note

上一份 durable comparison 基于 issue #234 修复前会向 baseline 泄漏规则的旧契约，因此标记为 `BLOCKED`。本轮使用当前无泄漏 prompt/fixture 重新生成两条 lane，未复用旧 baseline 或旧结论。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `uses_same_path_pm_engineer_docs`<br>读取 chat-interface/messages/history/search 的 PRD、TRD 和 IMPLEMENTATION_PLAN | PASS | with-skill transcript 明确读取了 docs/pm/chat-interface/messages/history/search/PRD.md、docs/engineer/chat-interface/messages/history/search/TRD.md 和 IMPLEMENTATION_PLAN.md；最终快照中的对应文件也存在。 | PASS | without-skill transcript 明确读取了同一 PRD、TRD 和 IMPLEMENTATION_PLAN。 |
| `writes_nested_security_report`<br>输出嵌套 Security appsec 报告路径 | PASS | 最终快照存在 docs/security/chat-interface/messages/history/search/appsec-checklist.md，未发现错误的顶层替代路径。 | FAIL | without-skill 最终快照没有生成任何 docs/security 下的 appsec-checklist 报告。 |
| `includes_feature_path_frontmatter`<br>报告 frontmatter 包含 feature path 字段 | PASS | 报告 frontmatter 明确包含 feature_path: chat-interface/messages/history/search、parent_feature: chat-interface/messages/history、feature_level: 4。 | FAIL | without-skill 没有报告，因此没有满足要求的 frontmatter。 |
| `does_not_invent_feature_directory`<br>路径不清时回 PM/Engineer | NOT EXERCISED | fixture 中 feature_path 清晰，且三份同路径文档均存在；未触发回 PM/Engineer 的条件。 | NOT EXERCISED | 同一客观 fixture 未触发路径不清或文档缺失分支。 |
| `escalates_fact_changing_conclusion_to_pm`<br>改变正式文档事实的结论升级 | FAIL | 报告和最终结论确认实现未满足 TRD 的工作区授权要求，属于改变正式文档事实的安全结论；transcript 没有回交 pm-agent 分类或创建 issue 的证据，且直接结束在报告/结论输出。 | FAIL | without-skill transcript 也确认实现与 PRD/TRD 要求不一致，但没有回交 pm-agent 分类并创建 issue的证据。 |

## With-Skill Behavior

with-skill 正确读取了三份同路径文档，并在最终快照生成了正确嵌套路径的报告及所需 frontmatter；但确认实现与 TRD/PRD 存在安全事实偏差后，没有按契约回交 pm-agent 分类并创建 issue。

## Fresh Without-Skill Baseline

without-skill 读取了三份文档并识别出主要风险，但未生成 Security 报告，也未执行所需的 PM 升级。

## Failures

- with-skill 未执行触发条件已满足的 Security Conclusion Escalation to PM。

## Not Exercised

- does_not_invent_feature_directory：feature_path 清晰且 PRD、TRD、IMPLEMENTATION_PLAN 均存在。

## Next Steps

- 应将安全结论与 src/search.ts 及 PRD/TRD 要求的证据回交 pm-agent 分类并创建 issue；Security 报告可保留在当前嵌套 docs/security 路径。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` workspace 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
