# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-006-nested-feature-path`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7` from `agents/product_manager/test/idea-to-spec/workspace/iteration-3/eval-6-nested-feature-path`.
- Fixture SHA-256: `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7`
- Prompt SHA-256: `c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c0da2e0366232678672d0c64ce9fa764d3b78f3caaaa8493348af1a7e1cd00fe`
- Skill overlay SHA-256: `8f09b52303d9393824dd3e732e656dd74f7ac606a082939547181274986dfb2d`
- Judge schema SHA-256: `4fbce5299edbfab7f3f9e314d3ad852d562878858c404b524820ab2f7613136e`
- Eval definition SHA-256: `0d6c5b2207f916945e44c4152d1df1a5456bcf63eecb7a912ef1fe1811598afa`
- Metadata SHA-256: `4835f86af8c88f61556ab924715c5dc8125d2c5616e22976f405e64c105bc13a`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `scan_existing_prds` | PASS | with_skill 输出提到读取现有 history PRD，并引用 docs/pm/chat-interface/messages/history/PRD.md。 |
| `nested_feature_path` | PASS | with_skill 的 current_feature_identity 明确给出 feature_path: chat-interface/messages/history/search。 |
| `no_parallel_top_level` | PASS | with_skill 明确建议不创建新的顶层 chat-interface 或 message-history PRD，并将搜索归入 history 子功能路径。 |
| `handoff_fields` | FAIL | handoff 中包含 feature_path、feature、parent_feature、feature_level，但使用 evidence 字段而非要求的 feature_path_evidence 字段。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=2c3864e0cae091619f20c98421e7a902c2876d902eb5eea15bb81f3f731a889d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别并规划了嵌套的消息历史搜索功能，但 handoff 字段不完整。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=2084d074434cad53a3ba3be399863b1ea46a3604f2ec16955a261eab8ddc5dea; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确建议使用嵌套 PRD 路径并避免顶层搜索文档，但未提供结构化 handoff 字段。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill handoff packet 缺少明确的 feature_path_evidence 字段。
- Next: 补充 feature_path_evidence 字段，并保留现有嵌套 feature_path。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-006-nested-feature-path`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7` from `agents/product_manager/test/idea-to-spec/workspace/iteration-3/eval-6-nested-feature-path`.
- Fixture SHA-256: `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7`
- Prompt SHA-256: `c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c0da2e0366232678672d0c64ce9fa764d3b78f3caaaa8493348af1a7e1cd00fe`
- Skill overlay SHA-256: `8f09b52303d9393824dd3e732e656dd74f7ac606a082939547181274986dfb2d`
- Judge schema SHA-256: `4fbce5299edbfab7f3f9e314d3ad852d562878858c404b524820ab2f7613136e`
- Eval definition SHA-256: `0d6c5b2207f916945e44c4152d1df1a5456bcf63eecb7a912ef1fe1811598afa`
- Metadata SHA-256: `4835f86af8c88f61556ab924715c5dc8125d2c5616e22976f405e64c105bc13a`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `5a4d229da9707c7ce22c80b66e92baafd2ef50f8fc9733b6b61f658aabf3dd17`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `scan_existing_prds` | PASS | 输出提到已检查项目文档、现有 PRD，并明确引用 history PRD。 |
| `nested_feature_path` | PASS | 明确给出 `chat-interface/messages/history/search` 及对应的 `docs/pm/.../search/PRD.md` 路径。 |
| `no_parallel_top_level` | PASS | 明确结论为不新建顶层 PM 文档，并将变更放在既有 history 子树下。 |
| `handoff_fields` | FAIL | 输出使用了 Lane checkpoint 和 current_feature_identity，但未包含 handoff packet 所要求的 feature_path、feature、parent_feature、feature_level、feature_path_evidence 字段。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=e0a76e773947c8af108b0b0824961d7b01d9083e901ae37fbaf10453044990f7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别并推荐四级嵌套搜索子特性及相关 PRD，但未提供完整 handoff 字段。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=c0ede05e064f2f648911073189e68b9d8d87b57f45771e7950020665c4beb9ac; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样识别了既有 PRD 和四级嵌套路径，提供了较简洁的文档变更建议；仅作基线对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出缺少要求的 handoff 字段。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-006-nested-feature-path`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7` from `agents/product_manager/test/idea-to-spec/workspace/iteration-3/eval-6-nested-feature-path`.
- Fixture SHA-256: `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7`
- Prompt SHA-256: `c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c0da2e0366232678672d0c64ce9fa764d3b78f3caaaa8493348af1a7e1cd00fe`
- Skill overlay SHA-256: `8f09b52303d9393824dd3e732e656dd74f7ac606a082939547181274986dfb2d`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `0d6c5b2207f916945e44c4152d1df1a5456bcf63eecb7a912ef1fe1811598afa`
- Metadata SHA-256: `4835f86af8c88f61556ab924715c5dc8125d2c5616e22976f405e64c105bc13a`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `scan_existing_prds` | PASS | with_skill 输出列出了三个 docs/pm PRD 路径，并明确提到现有 History PRD。 |
| `nested_feature_path` | PASS | with_skill 输出明确建议新增 docs/pm/chat-interface/messages/history/search/PRD.md，并给出 chat-interface/messages/history/search。 |
| `no_parallel_top_level` | PASS | with_skill 输出将搜索归入 chat-interface/messages/history/search，并说明暂不更新上层 PRD；未建议 history-search 的一级或截断路径。 |
| `handoff_fields` | FAIL | with_skill 的 YAML 未包含要求的 feature_path、feature、parent_feature、feature_level 和 feature_path_evidence 字段；仅包含 current_feature_identity、candidate_child_paths 等近似字段。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=cb68a91b2129e5856b0e50dafd6e9c39d8b4ec998050f26f8ae0ff2196d883da; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别并规划了嵌套消息历史搜索 PRD，未建议并列顶层路径，但缺少完整 handoff 字段。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=696343e72e0d865aedca27eecdc9fa2e1bf550eaf59cace265b202a3c97b6c0e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了现有 PRD 和嵌套搜索路径，但没有生成 handoff 字段或文档变更。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- handoff_fields 未满足：缺少 feature_path、feature、parent_feature、feature_level、feature_path_evidence。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-006-nested-feature-path`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7` from `agents/product_manager/test/idea-to-spec/workspace/iteration-3/eval-6-nested-feature-path`.
- Fixture SHA-256: `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7`
- Prompt SHA-256: `c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `7638558b96730ed626879bcffd4a606d3ed390013a41acf29ade725d210e3f4e`
- Skill overlay SHA-256: `12aaaef0d075d133bbbdc681f598fd09807b211a4377dcfbc6cbbfcaa30909e0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `0d6c5b2207f916945e44c4152d1df1a5456bcf63eecb7a912ef1fe1811598afa`
- Metadata SHA-256: `4835f86af8c88f61556ab924715c5dc8125d2c5616e22976f405e64c105bc13a`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `scan_existing_prds` | PASS | With-skill output references the existing history PRD and its docs/pm/chat-interface/messages/history/PRD.md path. |
| `nested_feature_path` | PASS | With-skill output explicitly states feature_path as chat-interface/messages/history/search and names the corresponding search PRD path. |
| `no_parallel_top_level` | PASS | With-skill output assigns the capability under the existing chat-interface ownership tree and does not propose a parallel top-level or truncated path. |
| `handoff_fields` | FAIL | With-skill output does not provide a handoff packet containing feature_path, feature, parent_feature, feature_level, and feature_path_evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=af7850fe6e6a5a1963102cb99c099a2b18f13ee7a15da440d537526108286bce; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the nested feature path and proposed PM documents, but omits the required handoff packet fields.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=4140c5d1ee7c1bcc8f5f11477b84ab753c46038dad2750191a125ba013696ee5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Identifies the nested search PRD path and recommends updating history plus creating the child PRD, but does not provide the required handoff fields.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output omits the required handoff packet fields: feature_path, feature, parent_feature, feature_level, and feature_path_evidence.
- Next: Add a handoff packet containing all five required feature-path fields.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-006-nested-feature-path`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7` from `agents/product_manager/test/idea-to-spec/workspace/iteration-3/eval-6-nested-feature-path`.
- Fixture SHA-256: `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7`
- Prompt SHA-256: `c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `7638558b96730ed626879bcffd4a606d3ed390013a41acf29ade725d210e3f4e`
- Skill overlay SHA-256: `12aaaef0d075d133bbbdc681f598fd09807b211a4377dcfbc6cbbfcaa30909e0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `0d6c5b2207f916945e44c4152d1df1a5456bcf63eecb7a912ef1fe1811598afa`
- Metadata SHA-256: `4835f86af8c88f61556ab924715c5dc8125d2c5616e22976f405e64c105bc13a`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `scan_existing_prds` | PASS | With-skill 输出提到已完成项目文档检查，并明确引用 Chat Interface、Message History 和 history PRD。 |
| `nested_feature_path` | PASS | 明确给出 feature path：chat-interface/messages/history/search，并给出对应 PRD 路径。 |
| `no_parallel_top_level` | PASS | 明确说明不应新建顶层 PRD，也不应创建 chat-interface/history-search 这样的平级路径。 |
| `handoff_fields` | FAIL | 输出未提供 handoff packet，且缺少 feature_path_evidence；也未以完整 handoff 字段集合呈现要求的字段。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=14da9759db17f570541aee1641e6f07f41074a73eb2fee4404b7a2e13bb03e03; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别父级 PRD、嵌套 feature path 和避免并列顶层路径，但缺少完整 handoff packet 字段。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=b41ccb1793118bbf6077e98769db7c41eb3548efc9cae220b8245fca8dfaad54; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别并读取 Message History PRD，给出嵌套 search 路径，但未提供完整 handoff 字段集合。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出缺少包含 feature_path、feature、parent_feature、feature_level 和 feature_path_evidence 的完整 handoff packet。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-006-nested-feature-path`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7` from `agents/product_manager/test/idea-to-spec/workspace/iteration-3/eval-6-nested-feature-path`.
- Fixture SHA-256: `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7`
- Prompt SHA-256: `c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a2e446c3d8d5f02d34cd5e3954e55500a6eaf296bcb868f9d3dbe27d39c64b91`
- Skill overlay SHA-256: `14328c4af5595e19e21331fb22dcc6dda56844ee6c4f2ee6382997e7ffe0af37`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `0d6c5b2207f916945e44c4152d1df1a5456bcf63eecb7a912ef1fe1811598afa`
- Metadata SHA-256: `4835f86af8c88f61556ab924715c5dc8125d2c5616e22976f405e64c105bc13a`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `scan_existing_prds` | PASS | With-skill 输出提到已完成项目文档检查，并明确引用现有 History PRD。 |
| `nested_feature_path` | PASS | 明确给出 feature_path 为 chat-interface/messages/history/search，并引用对应嵌套 PRD 路径。 |
| `no_parallel_top_level` | PASS | 明确表示不建议新增顶层 search PRD；与 fixture 中要求 history/{child} 路径一致。 |
| `handoff_fields` | FAIL | 输出仅给出 feature_path、parent_feature、feature_level，未提供 feature、feature_path_evidence，也未形成包含全部字段的 handoff packet。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=6af57991631a4edbc9da3d062638a20972d58283e611ec13c6abd91c11820f78; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确将搜索定位为 chat-interface/messages/history 的子功能并排除顶层 search，但缺少完整 handoff packet。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=8d8ed842db74674bbef437101be4c1a0396cf7885db30ee6ef544fd55bdfe079; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了现有 PRD 层级并给出嵌套 search 路径，但同样未提供完整 handoff packet 字段。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 输出未满足 handoff_fields assertion。
- Next: 补充包含 feature_path、feature、parent_feature、feature_level 和 feature_path_evidence 的 handoff packet。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-006-nested-feature-path`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7` from `agents/product_manager/test/idea-to-spec/workspace/iteration-3/eval-6-nested-feature-path`.
- Fixture SHA-256: `7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7`
- Prompt SHA-256: `c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9c3b136c6958582b2c5c3d552759bbe4fd3ef24876075804e91c5b21980a34af`
- Skill overlay SHA-256: `e4cc003a0e06320ef354c6c9cdbebb2b75980ec8b23ae530ac78b0667fab31da`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `0d6c5b2207f916945e44c4152d1df1a5456bcf63eecb7a912ef1fe1811598afa`
- Metadata SHA-256: `4835f86af8c88f61556ab924715c5dc8125d2c5616e22976f405e64c105bc13a`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `scan_existing_prds` | PASS | With-skill output references the existing Chat Interface, Messages, and Message History PRDs and their docs/pm paths. |
| `nested_feature_path` | PASS | It explicitly specifies feature_path as chat-interface/messages/history/search and the nested search PRD path. |
| `no_parallel_top_level` | PASS | It explicitly says the feature belongs under existing history as a fourth-level child and should not create a top-level feature. |
| `handoff_fields` | FAIL | The output includes feature_path, parent_feature, and feature_level, but does not provide a handoff packet containing feature, feature_path_evidence, or all required fields. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=caed880328598e205b0d2e4b3051260c661fcb49afa10632277624586fd3e112; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identified the nested fourth-level feature path and avoided parallel top-level paths, but omitted a complete handoff packet.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c1a9a695ac306d56eb35a4b41b4c84d037d6f92a7cc3a09d8d7f11f8de78d818; fixture_sha256=7749eb192d7baaaa2204b646c198e25edb560363b060536f8cc66b5b6a90c8e7; output_sha256=c80e5fddf6840b01578baff257215744d810730e2506d5be208866c6cbfaee4a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Identified the correct nested search PRD path and parent PRD updates, but did not provide the required handoff fields.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output does not contain a complete handoff packet with feature, feature_path, parent_feature, feature_level, and feature_path_evidence.
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

# Eval Result: eval-006-nested-feature-path

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; fresh paired manifests matched exactly.
- Behavior result: FAIL — 3/4 assertions passed.
- Coverage result: FULL — all 4 assertion scenarios were exercised.
Overall result: FAIL

### Assertion Results

- `scan_existing_prds`: PASS — the trace shows the existing PM PRDs were scanned and read before choosing a path.
- `nested_feature_path`: PASS — resolved `chat-interface/messages/history/search`.
- `no_parallel_top_level`: PASS — did not choose a truncated or top-level sibling path.
- `handoff_fields`: FAIL — no complete handoff packet was produced, and `feature_path_evidence` was missing.

### With-Skill / Baseline Comparison

The with-skill candidate correctly resolved the four-level path and stayed read-only. The baseline also found the nested path; it is comparison evidence only.

### Failures / Next Steps

- Include `feature_path`, `feature`, `parent_feature`, `feature_level`, and evidence-backed `feature_path_evidence` in an explicit handoff packet.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-006-nested-feature-path/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-006-nested-feature-path`
- Workspace: `workspace/iteration-3/eval-6-nested-feature-path`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; approved three-level PRD chain with all candidate stale child paths excluded by `execution_cleanup`.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-006-nested-feature-path/`

## Latest Result

- Behavior result: PASS — all 4 assertions passed.
- Coverage result: FULL — 4/4 assertion scenarios were exercised; no `NOT EXERCISED` items.
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `scan_existing_prds`: PASS — reads the complete `chat-interface/messages/history` PRD ancestry.
- `nested_feature_path`: PASS — resolves `chat-interface/messages/history/search` with parent and level metadata.
- `no_parallel_top_level`: PASS — rejects all parallel and truncated candidate directories.
- `handoff_fields`: PASS — includes `feature_path`, `feature`, `parent_feature`, `feature_level`, and structured `feature_path_evidence`.

## With-Skill Behavior

The response uses the existing PRD chain as the authoritative ownership evidence, proposes a child PRD and DECISIONS directory only under the confirmed parent, and keeps the handoff not ready until search scope is confirmed. No BRD context is required or emitted.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and cleaned fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It found the correct four-level path but used weaker path-only evidence and did not consistently preserve the not-ready PM gate.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused no feature-path or handoff regression; ownership is fully established by PRDs.

## Next Steps

- Keep this eval as coverage for PRD-based nested feature ownership after BRD removal.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-006-nested-feature-path/` and are not committed.
