# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-003-nested-feature-alignment-routing`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b` from `agents/engineer/test/engineer-agent/evals/workspace/eval-003-nested-feature-alignment-routing`.
- Fixture SHA-256: `fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b`
- Prompt SHA-256: `8df8927fae8a7a05a0bc46dd68c9ebf5573f79304565b07745939c992b9c20d9`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `cfa5a88208f1b1c899ab19782fdf4b1c4f59251e80b5c7edaead85a7f37b2ebd`
- Skill overlay SHA-256: `077bb84411e61374de4fd93945f7e775b9133b3517221140cf4b19937f8b8f70`
- Judge schema SHA-256: `2c28cd5019db4aa28a9d236d016e67174df115cef2180ca189d432ec28ba579c`
- Eval definition SHA-256: `6c7cc377f055d604b202feb40d5d2142b855d0368cb0621fa60f17937cec9872`
- Metadata SHA-256: `cc9d0ea1f23672ef6b7d553053f01b0836b8fd341a707c6f88e853c6256fb3fb`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `resolves_nested_feature_path` | PASS | With-skill output explicitly identifies feature_path as `chat-interface/history-search` and references the matching PRD/TRD paths; fixture frontmatter confirms both paths. |
| `does_not_use_sibling_or_parent_only_path` | PASS | With-skill output uses the nested feature path and does not substitute sibling or parent-only paths. |
| `routes_requirement_change_to_pm` | PASS | Because the requested ranking change affects approved expectations, with-skill output routes to `pm-agent:idea-to-spec` with `existing-project-update`, then describes subsequent TRD alignment. |
| `routes_trd_mismatch_to_trd_gen` | NOT_EXERCISED | The fixture TRD exists, is Approved, and its `feature_path` and `related_prd` match; the stale/missing/mismatch condition is not exercised. |
| `does_not_execute_directly` | PASS | With-skill output states no code changes, and locked git evidence shows no changes, commits, plans, or test execution. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8df8927fae8a7a05a0bc46dd68c9ebf5573f79304565b07745939c992b9c20d9; fixture_sha256=fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b; output_sha256=f65da846927597339f4f7dea24dccec7727684e87c4eef58b7e497a0cb2ba672; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly resolves the nested feature, routes an approved-expectation change to PM before TRD alignment, and stops without implementation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8df8927fae8a7a05a0bc46dd68c9ebf5573f79304565b07745939c992b9c20d9; fixture_sha256=fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b; output_sha256=3408558463293160b5a06abf943f70b0e947913241253e7c350b236041f94f46; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides reasonable generic planning and avoids changes, but does not resolve the nested feature path or perform the required PM routing.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: If a missing, stale, or mismatched TRD case is exercised, verify routing to `engineer-agent:trd-gen`.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-003-nested-feature-alignment-routing`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b` from `agents/engineer/test/engineer-agent/evals/workspace/eval-003-nested-feature-alignment-routing`.
- Fixture SHA-256: `fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b`
- Prompt SHA-256: `8df8927fae8a7a05a0bc46dd68c9ebf5573f79304565b07745939c992b9c20d9`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `cf5998cdd0e57fc7e288a79411dd445b8e07aa2acaa4991819873a45b9dfb293`
- Skill overlay SHA-256: `fbd54811cad37baf48c96e02cd6eda99bc6d8b886b0ce2dc848aa202c091fedd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6c7cc377f055d604b202feb40d5d2142b855d0368cb0621fa60f17937cec9872`
- Metadata SHA-256: `cc9d0ea1f23672ef6b7d553053f01b0836b8fd341a707c6f88e853c6256fb3fb`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `resolves_nested_feature_path` | PASS | with_skill 明确识别 feature_path 为 `chat-interface/history-search`，并基于锁定 manifest 中的嵌套 PRD/TRD 及输出中的两份文档内容进行推进判断。 |
| `does_not_use_sibling_or_parent_only_path` | PASS | with_skill 未使用并列路径或仅父级路径替代嵌套功能路径。 |
| `routes_requirement_change_to_pm` | PASS | 明确路由至 `pm-agent:idea-to-spec` 的 `existing-project-update`，并要求之后同步更新 TRD。 |
| `routes_trd_mismatch_to_trd_gen` | NOT_EXERCISED | 锁定 raw evidence 证明存在 TRD，但无法证明其缺失、stale 或 frontmatter/`related_prd` 不匹配。 |
| `does_not_execute_directly` | PASS | 输出明确本轮不改代码；git evidence 显示 HEAD、分支、索引和工作区均未变化，且无 delivery snapshot、实施计划或测试结果。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8df8927fae8a7a05a0bc46dd68c9ebf5573f79304565b07745939c992b9c20d9; fixture_sha256=fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b; output_sha256=6af2ae331044f2b72e1c1a7cffb82d40e9f09128c4fbfaf398e164e937946508; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别嵌套功能路径，先将排序需求变更路由回 PM，再同步 TRD，并保持只做路由、不执行实现。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8df8927fae8a7a05a0bc46dd68c9ebf5573f79304565b07745939c992b9c20d9; fixture_sha256=fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b; output_sha256=4bddd95fcb0da20911569bbdb1453fd27f8ed03fada7286fd0d5da761cc6d52f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 给出一般性的产品与技术推进建议，但未明确嵌套 feature_path 或规定的 PM 路由。
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

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-003-nested-feature-alignment-routing`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b` from `agents/engineer/test/engineer-agent/evals/workspace/eval-003-nested-feature-alignment-routing`.
- Fixture SHA-256: `fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b`
- Prompt SHA-256: `8df8927fae8a7a05a0bc46dd68c9ebf5573f79304565b07745939c992b9c20d9`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `757a4f95af830e3468b6c44e54e5901a0cc27f0a6d0aa7ecc8b703b612007d3a`
- Skill overlay SHA-256: `ed4d8f534d0e5c1c334b4a13d67b6d20c37dceb98e00e4e2ea3b6a2c0112faad`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6c7cc377f055d604b202feb40d5d2142b855d0368cb0621fa60f17937cec9872`
- Metadata SHA-256: `cc9d0ea1f23672ef6b7d553053f01b0836b8fd341a707c6f88e853c6256fb3fb`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `resolves_nested_feature_path` | PASS | with_skill 明确识别 `chat-interface/history-search`，并引用了嵌套路径下的 PRD 与 TRD。 |
| `does_not_use_sibling_or_parent_only_path` | PASS | with_skill 使用的两个文档均为 `chat-interface/history-search` 下的正确路径，未使用并列或父级替代路径。 |
| `routes_requirement_change_to_pm` | PASS | with_skill 明确将行为变更路由至 PM `existing-project-update`，先确认产品规则并增量更新 PRD，再同步 TRD。 |
| `routes_trd_mismatch_to_trd_gen` | NOT_EXERCISED | 原始 fixture 中 TRD 存在，且 frontmatter 的 `feature_path` 与 `related_prd` 均匹配；未出现缺失、过时或不匹配条件。 |
| `does_not_execute_directly` | PASS | with_skill 明确说明本轮未修改代码或文档；原始 git evidence 显示 HEAD、分支和工作区均未变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8df8927fae8a7a05a0bc46dd68c9ebf5573f79304565b07745939c992b9c20d9; fixture_sha256=fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b; output_sha256=322a3042ca956ee8791dd104bd768c199d3fc346aa8715ce8dcc98f60d1b689c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确解析功能路径，明确 PM 变更路由、文档同步和暂不实现的门禁；确认未发生代码或文档修改。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8df8927fae8a7a05a0bc46dd68c9ebf5573f79304565b07745939c992b9c20d9; fixture_sha256=fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b; output_sha256=20d7239cee10c6f33dffcecb0321795f2b02c255b83a761808d4d561fdf88bbd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确读取并概括嵌套 PRD/TRD，提出先确认排序规则再更新文档，但未明确 PM 工程路由。
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

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-003-nested-feature-alignment-routing`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b` from `agents/engineer/test/engineer-agent/evals/workspace/eval-003-nested-feature-alignment-routing`.
- Fixture SHA-256: `fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b`
- Prompt SHA-256: `8df8927fae8a7a05a0bc46dd68c9ebf5573f79304565b07745939c992b9c20d9`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `757a4f95af830e3468b6c44e54e5901a0cc27f0a6d0aa7ecc8b703b612007d3a`
- Skill overlay SHA-256: `ed4d8f534d0e5c1c334b4a13d67b6d20c37dceb98e00e4e2ea3b6a2c0112faad`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6c7cc377f055d604b202feb40d5d2142b855d0368cb0621fa60f17937cec9872`
- Metadata SHA-256: `cc9d0ea1f23672ef6b7d553053f01b0836b8fd341a707c6f88e853c6256fb3fb`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `resolves_nested_feature_path` | PASS | with_skill explicitly links both nested documents under docs/pm/chat-interface/history-search/PRD.md and docs/engineer/chat-interface/history-search/TRD.md, semantically identifying the feature path. |
| `does_not_use_sibling_or_parent_only_path` | PASS | with_skill references the required nested paths and does not substitute sibling or parent-only paths. |
| `routes_requirement_change_to_pm` | FAIL | with_skill recommends updating and confirming the PRD before synchronizing the TRD, but does not route the change to pm-agent:idea-to-spec with existing-project-update. |
| `routes_trd_mismatch_to_trd_gen` | NOT_EXERCISED | The fixture TRD exists, is Approved, and its feature_path and related_prd match; no mismatch condition occurs. |
| `does_not_execute_directly` | PASS | with_skill states not to modify code yet; locked git evidence shows no changes, no commits, and no declared outputs. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8df8927fae8a7a05a0bc46dd68c9ebf5573f79304565b07745939c992b9c20d9; fixture_sha256=fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b; output_sha256=03105e4b48ab24b4f17ae16f37eb57a26daee390fdc05336e2f49b8b99958ffa; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the nested documents, proposes PRD-then-TRD progression, and defers implementation, but omits the required explicit PM-agent route.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8df8927fae8a7a05a0bc46dd68c9ebf5573f79304565b07745939c992b9c20d9; fixture_sha256=fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b; output_sha256=abb510af72d649bad1248713349095754b36bd53209676c8dbe5e4b680d0567d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Provides a generic PRD/TRD update workflow and defers coding, but does not identify or route through the nested feature workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- resolves_nested_feature_path: PASS; does_not_use_sibling_or_parent_only_path: PASS; routes_requirement_change_to_pm: FAIL because the required pm-agent:idea-to-spec / existing-project-update route is omitted; routes_trd_mismatch_to_trd_gen: NOT_EXERCISED; does_not_execute_directly: PASS.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-003-nested-feature-alignment-routing`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b` from `agents/engineer/test/engineer-agent/evals/workspace/eval-003-nested-feature-alignment-routing`.
- Fixture SHA-256: `fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b`
- Prompt SHA-256: `8df8927fae8a7a05a0bc46dd68c9ebf5573f79304565b07745939c992b9c20d9`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `83f220b482f661eab0884cc4770c84fbb545af7bd74199e0b9f4ba499020031a`
- Skill overlay SHA-256: `94585e968fb2a0b5b29dd98429a0ee0f98e86ec73794257bcf099dd92d775e4c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6c7cc377f055d604b202feb40d5d2142b855d0368cb0621fa60f17937cec9872`
- Metadata SHA-256: `cc9d0ea1f23672ef6b7d553053f01b0836b8fd341a707c6f88e853c6256fb3fb`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `resolves_nested_feature_path` | FAIL | with_skill 输出未明确识别 `chat-interface/history-search`，也未输出两份文档的完整路径；仅泛称 PRD/TRD。 |
| `does_not_use_sibling_or_parent_only_path` | PASS | with_skill 输出未使用错误的并列路径或父级路径替代子功能文档。 |
| `routes_requirement_change_to_pm` | FAIL | with_skill 建议更新 PRD 并同步 TRD，但未路由至 `pm-agent:idea-to-spec` 的 `existing-project-update`。 |
| `routes_trd_mismatch_to_trd_gen` | NOT_EXERCISED | fixture 中 TRD 存在且为 Approved，`feature_path` 与 `related_prd` 均匹配，因此该条件未触发。 |
| `does_not_execute_directly` | PASS | with_skill 明确表示本轮不会改代码或文档，且 raw git evidence 显示无变更、无计划文件、无测试执行结果。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8df8927fae8a7a05a0bc46dd68c9ebf5573f79304565b07745939c992b9c20d9; fixture_sha256=fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b; output_sha256=22e38dcca5fa0129f746ceede862bcc6506ca22610be436ec60498142b0a6bb0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确保持只规划不执行并避免错误路径，但未在输出中给出嵌套路径，也未明确执行要求的 PM 路由。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8df8927fae8a7a05a0bc46dd68c9ebf5573f79304565b07745939c992b9c20d9; fixture_sha256=fce695dea6b3b91d6d3888c03505a121b7361b20c47f0ec1866020880becfe0b; output_sha256=a213964aff09cf4bf823bc98364680a73508a96a34958d7079219c4dd28763e6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别并列出了正确的嵌套 PRD/TRD 路径，也保持只规划不执行，但未明确要求 PM 路由。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- resolves_nested_feature_path
- routes_requirement_change_to_pm
- Next: 输出中明确 `chat-interface/history-search` 以及 PRD/TRD 的完整路径。
- Next: 在已批准排序预期发生变化时，明确路由至 `pm-agent:idea-to-spec` 的 `existing-project-update`，再同步 TRD。

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

# Eval Result: eval-003-nested-feature-alignment-routing

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-003-nested-feature-alignment-routing`
- Test case: nested-feature-alignment-routing
- Workspace: `workspace/eval-003-nested-feature-alignment-routing`
- Evaluation date: 2026-08-07
- Overall result: FAIL
- Behavior result: FAIL
- Coverage result: PARTIAL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 用户说：Chat Interface 已经有 History Search 子功能 PRD/TRD，现在想调整搜索结果排序，这是个很小的现有功能改动。请先做工程路由，不要改代码。相关文档在 docs/pm/chat-interface/history-search/PRD.md 和 docs/engineer/chat-interface/history-search/TRD.md。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `resolves_nested_feature_path`: final 明确识别 `chat-interface/history-search`；with_skill transcript 实际读取了嵌套路径下的 PRD.md 与 TRD.md。
- PASS `does_not_use_sibling_or_parent_only_path`: transcript 与 final 均使用完整嵌套路径，未读取错误的 sibling 或 parent-only 路径。
- FAIL `routes_requirement_change_to_pm`: 排序调整属于已批准行为的变更，但 final 仍将目标技能写为 `engineer-agent:feature-implementor`，没有路由到 `pm-agent:idea-to-spec` 的 `existing-project-update`。
- NOT EXERCISED `routes_trd_mismatch_to_trd_gen`: 当前 TRD 存在、状态为 Approved，feature_path 与 related_prd 均匹配，未触发该条件。
- PASS `does_not_execute_directly`: workspace hash 与输入一致；无代码、IMPLEMENTATION_PLAN 或测试变更，transcript 也未显示执行测试。

## With Skill Behavior

解析并读取了正确的嵌套 PRD/TRD，且未修改 workspace；但在 alignment gate 未通过时仍指向 feature-implementor，缺少 PM existing-project-update 路由。

## Without Skill Baseline

正确识别并引用嵌套 PRD/TRD，未修改 workspace；仅作对照，不影响 with_skill 判定。

## Failures / Findings

- routes_requirement_change_to_pm：未路由到 `pm-agent:idea-to-spec` 的 `existing-project-update`。
- Root cause: with_skill 在已批准排序行为的变更尚未完成需求对齐时错误保留了 feature-implementor 路由。

## Next Steps

- 修复上述 assertion 对应的 skill 行为或 eval 输入问题后，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-003-nested-feature-alignment-routing

## Evaluation Target

- Agent: `engineer`
- Skill: `engineer-agent`
- Eval: `eval-003-nested-feature-alignment-routing`
- Test case: nested-feature-alignment-routing
- Workspace: `workspace/eval-003-nested-feature-alignment-routing`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: approved `chat-interface/history-search` PRD/TRD with a small search-ordering change.
- Fresh validation date: 2026-08-01.
- With-skill source: current Engineer README, current `engineer-agent` SKILL, eval definition, metadata, README, and same-path PRD/TRD.
- Without-skill source: the same prompt and fixture, freshly regenerated without reading or applying the target README/SKILL, with-skill output, historical comparison, or prior baseline.

## Latest Result

- Behavior result: PASS
- Coverage result: FULL
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


All 5 assertions were exercised and passed in the with-skill run.

## Assertions

- PASS `resolves_nested_feature_path`: preserves `chat-interface/history-search` and reads its same-path PRD/TRD.
- PASS `does_not_use_sibling_or_parent_only_path`: does not collapse evidence to a sibling or parent-only path.
- PASS `routes_requirement_change_to_pm`: sends approved sorting changes to the PM `existing-project-update` lane.
- PASS `routes_trd_mismatch_to_trd_gen`: sends missing, stale, or path-mismatched TRDs to `engineer-agent:trd-gen`.
- PASS `does_not_execute_directly`: remains route-only.

## With Skill Behavior

The fresh route resolves the nested path, compares the explicit sorting contract, sends a changed expectation to PM, and sends technical freshness/path mismatches to `trd-gen`. It does not create a plan, edit code, or run tests.

## Without Skill Baseline

The fresh baseline preserves the exact nested paths, recognizes a possible product requirement change, and stays route-only. It does not name the required PM `existing-project-update` or `engineer-agent:trd-gen` routes. Baseline assertion result: 3/5.

## Failures

- None.

## Next Steps

- Keep this eval as regression coverage for nested feature-path resolution and same-path alignment.

## Runtime Artifacts Policy

- Fresh runtime evidence is under `tmp/eval-runs/issue-196-project-bootstrap-removal-20260801-131022/engineer-agent/eval-003-nested-feature-alignment-routing/`.
- `with_skill.md`, `without_skill.md`, and `verdict.md` are scratch evidence and must not be committed.
- This `comparison.md` is the only durable result.
