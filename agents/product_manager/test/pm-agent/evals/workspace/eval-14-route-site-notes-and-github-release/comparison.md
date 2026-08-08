# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-14-route-site-notes-and-github-release`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `0b60a8fdef1023247fb430f4647e03f742c09fbfdb17e32a3a03dc6059ae9e02`
- Skill overlay SHA-256: `7093347dda9d009dc74c5bd9b37b3d0d8b980466e82f7a4efbacd767a0e9fa19`
- Judge schema SHA-256: `0e6be21ab02e72aa076a9b774d5cc60139434feba550f781574340027908427d`
- Eval definition SHA-256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- Metadata SHA-256: `7b48bd11ada861ee54366c474d903263630fabf2c5e0d3a66c9f38056e80908e`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | PASS | with_skill 明确将站内版本说明 owner 指向 docs-agent:release-notes-gen，并说明先完成 Docs 阶段。 |
| `routes_github_release_to_pm_specialist` | PASS | with_skill 将下游 GitHub Release owner 指向 pm-agent:github-release-gen，并拒绝由 Docs 阶段执行下游预览。 |
| `preserves_release_sequence` | NOT_EXERCISED | 输出声明 site-first 顺序，但因缺少版本来源、交接证据且 specialist 不可用，尚未实际完成确认、Docs gates 或 PM 消费步骤。 |
| `does_not_use_old_pm_skill_name` | PASS | PM owner 使用 github-release-gen；release-notes-gen 仅用于 docs-agent，未将其作为 PM owner。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=4b41c94cdb1530584bf8a4a4516ac766782734e1316f290fb3be6fd04cf5f48b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别 Docs → PM 的路由和 site-first 边界；因输入与运行证据不足而安全阻塞，未创建文件或发布内容。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b6a2d85d61a704cefe02b05941740410ad9481a21b341e96ceac8415a69bf4e6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅报告仓库缺少发布事实依据，未体现专 specialist 路由或顺序控制。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供 v1.0.0 变更来源并启用所需 specialist 后，完成 Docs 确认与 gates，再生成 PM GitHub Release 预览。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-14-route-site-notes-and-github-release`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `408fcd917b4eb851c354f2de7a398f53f4466aa8f161f9110ad055ed6bc0102c`
- Skill overlay SHA-256: `e9a6397e166437c034ee8eec0fb781d11e200a5f78eb511626f627c9596e06b0`
- Judge schema SHA-256: `0e6be21ab02e72aa076a9b774d5cc60139434feba550f781574340027908427d`
- Eval definition SHA-256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- Metadata SHA-256: `7b48bd11ada861ee54366c474d903263630fabf2c5e0d3a66c9f38056e80908e`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | PASS | with_skill 明确将站内版本说明 owner 指向 docs-agent:release-notes-gen，并按站内说明先行的路径处理。 |
| `routes_github_release_to_pm_specialist` | PASS | with_skill 明确列出 pm-agent:github-release-gen 作为 GitHub Release 预览的下游 owner，未让 Docs specialist 执行发布流程。 |
| `preserves_release_sequence` | NOT_EXERCISED | 候选正确表达了先生成并确认站内说明、再准备 GitHub Release 预览，但因缺少变更证据且专项未安装，ready handoff、Docs gates 和 release audit evidence 的后续执行未发生。 |
| `does_not_use_old_pm_skill_name` | PASS | PM owner 使用 github-release-gen；release-notes-gen 仅用于 docs-agent，未将其作为 PM owner。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=23519538b79ec268f463512bc0dcc092a1f8a62dbaa26449e66d737d3a063090; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别并保留 docs → PM 的正确路由与 site-first 顺序；因证据和专项缺失而安全阻塞，未编造内容或发布。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=2e943d190fc5987613aaba0e8575875e23dfe4b3f0704596868e144928b5e6d8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅报告仓库为空并请求补充资料；没有展示专项路由或 gates/handoff 处理。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供 v1.0.0 变更证据并安装所需 Docs/PM 专项后，执行站内说明确认、ready handoff、release audit，再生成 GitHub Release 预览。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-14-route-site-notes-and-github-release`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `408fcd917b4eb851c354f2de7a398f53f4466aa8f161f9110ad055ed6bc0102c`
- Skill overlay SHA-256: `e9a6397e166437c034ee8eec0fb781d11e200a5f78eb511626f627c9596e06b0`
- Judge schema SHA-256: `0e6be21ab02e72aa076a9b774d5cc60139434feba550f781574340027908427d`
- Eval definition SHA-256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- Metadata SHA-256: `7b48bd11ada861ee54366c474d903263630fabf2c5e0d3a66c9f38056e80908e`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | FAIL | with_skill 明确表示 docs-agent:release-notes-gen 未安装且无法执行站内版本说明流程，未完成 handoff。 |
| `routes_github_release_to_pm_specialist` | NOT_EXERCISED | with_skill 在站内版本说明阶段被阻断，并明确表示不能进入 GitHub Release 预览阶段；PM 路由未执行。 |
| `preserves_release_sequence` | NOT_EXERCISED | with_skill 未执行确认、ready handoff 或 release audit evidence 流程，仅说明无法进入后续阶段。 |
| `does_not_use_old_pm_skill_name` | PASS | 输出仅将 release-notes-gen 用作 docs-agent specialist，未将其命名为 PM owner。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=767f8ed4b9ff4a2309ce5a9227b3e637109b42353edaa2e23b3bd2d7720d5960; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 因缺少版本资料并声称 docs specialist 未安装而停止，未生成交付物或进入 PM Release 阶段。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f4ec62c693549144d68dbdeb5b85540bcc7a7396c1f2f6a58539b82f0fd00ea9; snapshot_sha256=5fac923f4d2982d63e46bc090d8b314d696557d83718e8616ad5aa905d3f007d
- Behavior: 生成了待确认的站内版本说明和 GitHub Release 预览文件，未实际发布，但未体现所需 specialist 路由与 site-first handoff 流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未完成请求 A 的 docs specialist handoff，且未交付站内版本说明或 GitHub Release 预览。
- Next: 提供已确认的 v1.0.0 变更资料，并确保 docs specialist 可用后完成请求 A，再由 PM specialist 处理 Release 预览。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-14-route-site-notes-and-github-release`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `408fcd917b4eb851c354f2de7a398f53f4466aa8f161f9110ad055ed6bc0102c`
- Skill overlay SHA-256: `e9a6397e166437c034ee8eec0fb781d11e200a5f78eb511626f627c9596e06b0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- Metadata SHA-256: `7b48bd11ada861ee54366c474d903263630fabf2c5e0d3a66c9f38056e80908e`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | FAIL | with_skill 未执行站内版本说明流程，也未确认将请求 A handoff 到 docs-agent:release-notes-gen。 |
| `routes_github_release_to_pm_specialist` | FAIL | with_skill 未执行 GitHub Release 预览流程；虽提及 pm-agent:github-release-gen，但没有实际路由或交付结果。 |
| `preserves_release_sequence` | FAIL | with_skill 未生成站内版本说明、ready handoff 或 GitHub Release 预览，因此未体现站内说明先确认并通过 Docs gates 后再交由 PM 消费的顺序。 |
| `does_not_use_old_pm_skill_name` | PASS | with_skill 将 release-notes-gen 命名为 docs-agent 的 specialist，并将 GitHub Release specialist 命名为 github-release-gen，未把 PM owner 命名为 release-notes-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=86e0249981bda28a93e585bc569b4a6374a99a08aa0940584bc97ab2b2bc54b5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 未生成任何交付物，因声称缺少变更来源、确认版说明及对应插件而停止。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=4fc9920799c83605abc500a48ad2ffaf1d322edfc7c22cf87d92b4896b9637f4; snapshot_sha256=01ca40e549a828fbad615b2a40f91daf11623b9ac1ef5c39663b09d1b75e9d6c
- Behavior: 生成了站内版本说明和 GitHub Release 预览文件，明确未发布，但没有路由或 specialist 证据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完成请求要求的站内版本说明和 GitHub Release 预览工作流。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-14-route-site-notes-and-github-release`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `da17d4a3cc21b7b3406a5e9563eb0de52953132aff13ecd162bc201b422b9c60`
- Skill overlay SHA-256: `e406d715ee602cbed706c0ad23e94d5aceb1a2d88e22b51dc7fec5b6b0ff84ae`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- Metadata SHA-256: `7b48bd11ada861ee54366c474d903263630fabf2c5e0d3a66c9f38056e80908e`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | PASS | with_skill 明确将站内版本说明分配给 docs-agent:release-notes-gen。 |
| `routes_github_release_to_pm_specialist` | PASS | with_skill 明确将 GitHub Release 预览分配给 PM github-release-gen。 |
| `preserves_release_sequence` | NOT_EXERCISED | 候选输出在缺少插件和变更来源时停止，未实际执行或展示站内说明确认、ready handoff 或 release audit evidence 的顺序。 |
| `does_not_use_old_pm_skill_name` | PASS | with_skill 将 release-notes-gen 限定为 docs-agent，并使用 github-release-gen 作为 PM 路由名。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=d02d0d91b2a72e40240c8d351cd3c3db09d228f95a41e6a32dd0d6f2f92219e2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别两个 specialist 路由并声明不发布，但因插件和变更来源缺失而未继续执行。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=3131c1d1492e48939e1d83e22cedbe93a39358d45b7749fa7f1997624b657db2; snapshot_sha256=95ebf519a248cdc04e423d89e8277579e29fa8d46721508faa2b09e3e5be6259
- Behavior: 生成了站内说明和 GitHub Release 预览文件，但未提供 specialist 路由或顺序证据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 安装所需专用插件并提供或导入 v1.0.0 的变更来源后继续。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-14-route-site-notes-and-github-release`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `847ec25f3bf19681577a3386dfc21c378712f63dee7629dde5750b16901ab4e4`
- Skill overlay SHA-256: `85498141fecd6ca653a495454d16dd5a8f8fa77675af6eb45d6d223d0cab1fbd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- Metadata SHA-256: `7b48bd11ada861ee54366c474d903263630fabf2c5e0d3a66c9f38056e80908e`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | NOT_EXERCISED | with_skill 未实际执行 handoff；候选输出因缺少版本范围与变更证据而请求补充信息。 |
| `routes_github_release_to_pm_specialist` | NOT_EXERCISED | with_skill 未实际生成或路由 GitHub Release preview；该后续步骤依赖用户确认和运行时证据。 |
| `preserves_release_sequence` | NOT_EXERCISED | 候选输出仅表达“站内版本说明 → GitHub Release 预览”的计划顺序，未执行 Docs gates、ready handoff 或 release audit evidence 流程。 |
| `does_not_use_old_pm_skill_name` | PASS | with_skill 输出未将 PM owner 命名为 release-notes-gen，也未使用该旧名。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=928ef682e653c06526583f0443664f452ca734aa07f68b3fde172f508e70ae49; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 因缺少确认后的版本范围和变更证据而暂停，明确后续顺序并承诺不实际发布；未执行 specialist 路由。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f0bd05858e16fa6309272eaf0afe83a0dbd660c05880464e5439ea14dcf608a8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 因仓库无内容而请求版本变更信息；未执行路由或发布，工作区保持不变。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供已确认的 v1.0.0 变更清单或 Issue/PR/提交后，再验证实际 Docs handoff、PM 路由及 release audit evidence 消费。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-14-route-site-notes-and-github-release`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `847ec25f3bf19681577a3386dfc21c378712f63dee7629dde5750b16901ab4e4`
- Skill overlay SHA-256: `780c8f93b8e6c45b2ccd3c9782ab0565304ee40820ab216a99298b8a0a82b7f1`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- Metadata SHA-256: `7b48bd11ada861ee54366c474d903263630fabf2c5e0d3a66c9f38056e80908e`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | FAIL | with_skill 输出仅列出站内版本说明文件，未明确 handoff 到 docs-agent:release-notes-gen。 |
| `routes_github_release_to_pm_specialist` | FAIL | with_skill 输出仅列出 GitHub Release 预览文件，未路由到 PM github-release-gen。 |
| `preserves_release_sequence` | FAIL | 文档提到完成文档审计后进入 GitHub Release 流程，但未说明 ready handoff、PM github-release-gen 消费或 release audit evidence。 |
| `does_not_use_old_pm_skill_name` | PASS | with_skill 输出及两份文档均未将 PM owner 命名为 release-notes-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=19a1d0f7fdf24b545f96dc52b88151d49a71a13a694a014fcfdf7f1b06e9266a; snapshot_sha256=ffcb749898b3af7b15f2989647f493276c1f7cef577730ebaf5bb80cb0df23a1
- Behavior: 生成站内版本说明草稿和 GitHub Release 预览，并保留未确认、不可发布状态；但未明确 specialist 路由或 handoff 链路。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=307626c1214f041d67f0e6548b160132a7a3de144b49a9a4a86ccbe59a9dd126; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 因仓库为空而拒绝生成任何输出，未体现路由行为。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确 docs-agent:release-notes-gen、PM github-release-gen 及 ready handoff/release audit evidence。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-14-route-site-notes-and-github-release`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27bdda776386001cc566aec58e87a13d3b1f46246aed8961a6b1f71f6fe7164`
- Skill overlay SHA-256: `4c9723c1beabc3433045321f3b5731004dd2e67877c45ddeed6c79c96a17ba04`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `ae4335c3ea7ab2052d5988d1cbe329b872d3570826da6174d95ecdee75a8f11e`
- Metadata SHA-256: `7b48bd11ada861ee54366c474d903263630fabf2c5e0d3a66c9f38056e80908e`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `routes_site_notes_to_docs_specialist` | FAIL | with_skill 输出未创建或说明站内版本说明，也未 handoff 到 docs-agent:release-notes-gen。 |
| `routes_github_release_to_pm_specialist` | FAIL | with_skill 输出未生成 GitHub Release 预览，也未路由到 PM github-release-gen。 |
| `preserves_release_sequence` | FAIL | with_skill 输出仅说明无法完成，并未说明站内说明先经 Docs gates 确认，再由 PM 消费 ready handoff 和 audit evidence。 |
| `does_not_use_old_pm_skill_name` | PASS | with_skill 输出未将 PM owner 命名为 release-notes-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=41602464cf3b536e8dd6f911e19f41e17b121203e4556ec1d6fe620582deb79e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 因声称仓库为空而拒绝执行任务，未创建任何输出，也未展示路由或发布流程。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=aeb9d94911e2f21a05aec636eb7871f30e1f918271687f3e921766aab4cdc3f2; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=96d818fcf61ffcfb326658ca1f96896af48bb3e59c1d3e45ebc56b2f415e4152; snapshot_sha256=5bc8109740576060b8d1edcaa3723defb56d431b2c21631753a371038142ba7c
- Behavior: 创建了站内版本说明和 GitHub Release 预览，但未提供所需 specialist 路由或 site-first handoff 证据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未完成任务要求的两类输出及其 specialist 路由。
- with_skill 未证明站内版本说明确认后再生成 GitHub Release 预览的顺序。
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

# Eval Result: eval-014-route-site-notes-and-github-release

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-014-route-site-notes-and-github-release`
- Workspace: `eval-14-route-site-notes-and-github-release`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-014-route-site-notes-and-github-release/`.

## Latest result:

- Behavior result: PASS — determined only from the with-skill lane by an independent judge.
- Coverage result: PARTIAL — 0/4 with-skill assertion scenarios were exercised.
Overall result: PASS (partial coverage)

## Assertion Results

- `routes_site_notes_to_docs_specialist`: with-skill **NOT_EXERCISED**; without-skill **NOT_EXERCISED** — 两份最终回复均未执行或承诺具体 handoff；v1.0.0 的确认范围/实体不存在，无法实际触发 A 路由。
- `routes_github_release_to_pm_specialist`: with-skill **NOT_EXERCISED**; without-skill **NOT_EXERCISED** — 两份最终回复均未生成 GitHub Release preview，也未展示 PM github-release-gen 路由；v1.0.0 来源不足。
- `preserves_release_sequence`: with-skill **NOT_EXERCISED**; without-skill **NOT_EXERCISED** — 未进入站内说明确认或 Release audit gates 阶段，因此无法核对 site-first 顺序。
- `does_not_use_old_pm_skill_name`: with-skill **NOT_EXERCISED**; without-skill **NOT_EXERCISED** — 最终回复和工具轨迹未发生实际 PM owner 命名或路由，无法核对旧名回退。

## With-Skill Behavior

行为未触发断言失败；轨迹识别为 release_notes 工作流并先检查资料，但因缺少 v1.0.0 的项目内容、Git 历史和确认范围而停止澄清。status 显示零新增、零删除、零修改。

## Fresh Without-Skill Baseline

行为未触发断言失败；轨迹通过只读 GitHub 查询确认目标仓库当前为 v0.5.7-fix1、没有 v1.0.0 依据后停止澄清。status 显示零文件变更，未见外部写入或发布调用。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- None.

## Coverage Gaps

- 四项 with_skill assertions 均未实际执行，无法验证具体 specialist handoff、顺序或旧名约束。
- 缺少 v1.0.0 的确认版本范围、变更依据或可消费的 release handoff。

## Blockers

- 实时数据中不存在断言所需的 v1.0.0 版本实体/确认范围。

## Historical Result (Pre-#234)

- The previous durable result recorded Behavior **PASS**, Coverage **FULL**, and Overall **BLOCKED** after issue #234 identified prompt/fixture leakage.
- That pre-remediation result is retained only as history and is superseded by this strict fresh run.

## Next Steps

- Keep the passing behavior result, and rerun when the missing live entities or fixture conditions can exercise the listed coverage gaps.

## Runtime Artifacts Policy

- Candidate responses, traces, status manifests, isolation records, and judge evidence remain under the gitignored runtime path above and are not committed.
