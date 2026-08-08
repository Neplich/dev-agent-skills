# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-003-nested-prd-to-engineer-trd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc` from `agents/engineer/test/trd-gen/evals/workspace/eval-003-nested-prd-to-engineer-trd`.
- Fixture SHA-256: `9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc`
- Prompt SHA-256: `8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `73cec46ef0287c25bd7a41d37b6bcee4e1ea25b1101672fb45bd299ecec77b0d`
- Skill overlay SHA-256: `8f09b52303d9393824dd3e732e656dd74f7ac606a082939547181274986dfb2d`
- Judge schema SHA-256: `10a807298f91a20d6e9b68f75881e7ea6287d8afeff10727bea551d980d3535f`
- Eval definition SHA-256: `f3397b62fc4d049158e92b00f525e136ca990d6c804b1f211ce557bfaf30d03e`
- Metadata SHA-256: `de0335f1a182c8496f115f68dc77dc691a79abeae555386cc002141eada43865`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `mirrors_nested_feature_path` | PASS | with_skill TRD is delivered at docs/engineer/chat-interface/messages/history/search/TRD.md. |
| `preserves_feature_metadata` | PASS | TRD.md frontmatter contains feature_path, parent_feature, and feature_level: 4. |
| `related_prd_matches_path` | PASS | TRD.md frontmatter points related_prd to docs/pm/chat-interface/messages/history/search/PRD.md. |
| `blocks_on_missing_or_unclear_prd_path` | PASS | The fixture PRD clearly confirms the feature path and parent; with_skill records that confirmed basis and does not guess a top-level TRD. |
| `no_plan_or_code` | PASS | Locked git evidence shows only documentation files were added; candidate explicitly states no implementation plan or code was created. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4; fixture_sha256=9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc; output_sha256=c27f4993d51236b6da64c85a63baa40d807e7f20c558273b07107bc86fe6db73; snapshot_sha256=545af0a02ad1f0bf2fec28e0369225d61ad74d437e14ef21105effa825d38c31
- Behavior: Created the correctly nested Engineer TRD, API, and ADR with matching metadata and PRD linkage; downstream implementation remains blocked.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4; fixture_sha256=9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc; output_sha256=0aa203d3b339c28775caae297046c001d6c90328a37bcd8aceb8e753e91bd303; snapshot_sha256=aba096bb3d82eabcc96f1bdaa08c184a5aab33a30e70c5f469fabef979f34584
- Behavior: Created a TRD under docs/tech with the nested path, but used the wrong documentation root and source_prd metadata rather than the required Engineer output convention.
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
- Skill: `trd-gen`
- Eval: `eval-003-nested-prd-to-engineer-trd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc` from `agents/engineer/test/trd-gen/evals/workspace/eval-003-nested-prd-to-engineer-trd`.
- Fixture SHA-256: `9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc`
- Prompt SHA-256: `8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `73cec46ef0287c25bd7a41d37b6bcee4e1ea25b1101672fb45bd299ecec77b0d`
- Skill overlay SHA-256: `8f09b52303d9393824dd3e732e656dd74f7ac606a082939547181274986dfb2d`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f3397b62fc4d049158e92b00f525e136ca990d6c804b1f211ce557bfaf30d03e`
- Metadata SHA-256: `de0335f1a182c8496f115f68dc77dc691a79abeae555386cc002141eada43865`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `mirrors_nested_feature_path` | PASS | TRD.md is delivered at docs/engineer/chat-interface/messages/history/search/TRD.md. |
| `preserves_feature_metadata` | PASS | TRD.md frontmatter directly contains feature_path chat-interface/messages/history/search, parent_feature chat-interface/messages/history, and feature_level 4. |
| `related_prd_matches_path` | PASS | TRD.md frontmatter directly contains related_prd: docs/pm/chat-interface/messages/history/search/PRD.md. |
| `blocks_on_missing_or_unclear_prd_path` | PASS | The supplied PRD path is confirmed; the with_skill delivery mirrors that exact path and does not guess a top-level TRD location. |
| `no_plan_or_code` | PASS | Git evidence shows only new Engineer documentation files; no IMPLEMENTATION_PLAN.md, code changes, test files, or implementation delivery are present. The TRD explicitly gates handoff on maintainer confirmation. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4; fixture_sha256=9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc; output_sha256=dd1eccb313d4e8a011d13fbc28068a45d76fb319f6baa3598e6fadda23cc94dc; snapshot_sha256=8e748a432b56328219c92ad2acf954d3c8d10fe856e5c81db296554a067d44f0
- Behavior: Created the correctly nested TRD plus supporting API and ADR documents with matching metadata and related PRD linkage, while deferring implementation handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4; fixture_sha256=9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc; output_sha256=09973c34b5fdae838e323f53e4df1f584c06322ca5f031720b30adeca9be528a; snapshot_sha256=3752fce2d964efb9fa464e9510cb5d5432f52507f6cd0f24dd2511a4ab4bcab2
- Behavior: Created a PM Technical-Solution.md instead of the required Engineer TRD path and metadata.
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
- Skill: `trd-gen`
- Eval: `eval-003-nested-prd-to-engineer-trd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc` from `agents/engineer/test/trd-gen/evals/workspace/eval-003-nested-prd-to-engineer-trd`.
- Fixture SHA-256: `9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc`
- Prompt SHA-256: `8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bb3f875298d7fef0fcd2297b4e59b33b5c034efad4a2286dcaede91ec0863c72`
- Skill overlay SHA-256: `12aaaef0d075d133bbbdc681f598fd09807b211a4377dcfbc6cbbfcaa30909e0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f3397b62fc4d049158e92b00f525e136ca990d6c804b1f211ce557bfaf30d03e`
- Metadata SHA-256: `de0335f1a182c8496f115f68dc77dc691a79abeae555386cc002141eada43865`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `mirrors_nested_feature_path` | PASS | with_skill 交付路径为 docs/engineer/chat-interface/messages/history/search/TRD.md，完整保留四级 feature_path。 |
| `preserves_feature_metadata` | PASS | TRD frontmatter 明确包含 feature_path、parent_feature 和 feature_level: "4"。 |
| `related_prd_matches_path` | PASS | TRD frontmatter 的 related_prd 指向 docs/pm/chat-interface/messages/history/search/PRD.md。 |
| `blocks_on_missing_or_unclear_prd_path` | NOT_EXERCISED | 原始 fixture 中 PRD 路径和父功能归属明确，未提供路径缺失或不清晰的场景。 |
| `no_plan_or_code` | PASS | git 状态仅显示新增 TRD.md；未创建 IMPLEMENTATION_PLAN.md、修改代码或补测试。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4; fixture_sha256=9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc; output_sha256=c6db2650e5f4fa83a4680b86eb427e8a254c1d3a3b5082d3559a9acaf7923e6d; snapshot_sha256=08dda9e28a9c26e38bf2123ec9a70fc77b72f36ff66f9bd9bafea205985ecb7d
- Behavior: 按完整嵌套 feature path 生成 TRD，保留要求的 frontmatter 和 related_prd，且未进入实现交付。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4; fixture_sha256=9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc; output_sha256=f325009e1d79e6d6acbc59889ae4f6841cc5e74e8a0b28585d61e389d5610be6; snapshot_sha256=4a42c72b8f55220b3cc50811596d20f8f6bb8765701e7ca420937d322b5f2002
- Behavior: 生成了 PM 目录下的 TECHNICAL_DESIGN.md，未按要求生成 Engineer TRD 路径。
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
- Skill: `trd-gen`
- Eval: `eval-003-nested-prd-to-engineer-trd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc` from `agents/engineer/test/trd-gen/evals/workspace/eval-003-nested-prd-to-engineer-trd`.
- Fixture SHA-256: `9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc`
- Prompt SHA-256: `8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `bb3f875298d7fef0fcd2297b4e59b33b5c034efad4a2286dcaede91ec0863c72`
- Skill overlay SHA-256: `12aaaef0d075d133bbbdc681f598fd09807b211a4377dcfbc6cbbfcaa30909e0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f3397b62fc4d049158e92b00f525e136ca990d6c804b1f211ce557bfaf30d03e`
- Metadata SHA-256: `de0335f1a182c8496f115f68dc77dc691a79abeae555386cc002141eada43865`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `mirrors_nested_feature_path` | PASS | With-skill delivery snapshot places TRD at docs/engineer/chat-interface/messages/history/search/TRD.md. |
| `preserves_feature_metadata` | PASS | TRD frontmatter contains feature_path chat-interface/messages/history/search, parent_feature chat-interface/messages/history, and feature_level 4. |
| `related_prd_matches_path` | PASS | TRD frontmatter sets related_prd to docs/pm/chat-interface/messages/history/search/PRD.md. |
| `blocks_on_missing_or_unclear_prd_path` | PASS | Fixture clearly confirms the nested feature path and parent ownership; the candidate bases the TRD on the approved PRD and does not guess a top-level path. |
| `no_plan_or_code` | PASS | With-skill evidence shows only the TRD as an untracked output; no implementation plan, code, tests, or delivery changes were created. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4; fixture_sha256=9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc; output_sha256=b85d76951db12d277f7d71471166a48a4f4028a2f3d6c093cd924968113f433a; snapshot_sha256=71170efbd48cfe7d6a58d4c3c4677836497b39eb0ffb01d64234fc9e66457906
- Behavior: Produced the required nested engineer TRD with matching feature metadata and related PRD, without entering implementation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4; fixture_sha256=9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc; output_sha256=3d27e7a1a5a922e376063820022b55c2819aebef9ac1fd399977b1a531004492; snapshot_sha256=76458cfa6fee29178ad3a8ef8d10aedc774e85623e8773beb9fb98e38dcb0b6e
- Behavior: Produced a technical design under docs/tech/.../TechnicalDesign.md, not the required engineer TRD path, and did not preserve the required TRD metadata contract.
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
- Skill: `trd-gen`
- Eval: `eval-003-nested-prd-to-engineer-trd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc` from `agents/engineer/test/trd-gen/evals/workspace/eval-003-nested-prd-to-engineer-trd`.
- Fixture SHA-256: `9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc`
- Prompt SHA-256: `8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a696884cd8ec31e2137cab6da5326eb0f6fb0d49089fe5e32218dce4da5cdfee`
- Skill overlay SHA-256: `14328c4af5595e19e21331fb22dcc6dda56844ee6c4f2ee6382997e7ffe0af37`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f3397b62fc4d049158e92b00f525e136ca990d6c804b1f211ce557bfaf30d03e`
- Metadata SHA-256: `de0335f1a182c8496f115f68dc77dc691a79abeae555386cc002141eada43865`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `mirrors_nested_feature_path` | PASS | With_skill output creates TRD at docs/engineer/chat-interface/messages/history/search/TRD.md. |
| `preserves_feature_metadata` | PASS | Frontmatter contains feature_path chat-interface/messages/history/search, parent_feature chat-interface/messages/history, and feature_level 4. |
| `related_prd_matches_path` | PASS | Frontmatter sets related_prd to docs/pm/chat-interface/messages/history/search/PRD.md. |
| `blocks_on_missing_or_unclear_prd_path` | NOT_EXERCISED | The fixture clearly provides the PRD feature_path and parent feature, so the missing-or-unclear path is not exercised. |
| `no_plan_or_code` | PASS | With_skill output is a TRD only; git evidence shows only the TRD untracked and the document states no code implementation is included. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4; fixture_sha256=9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc; output_sha256=acbcd7ba49779b06eedbdc9784bc16d5f7012a7169ab28a4f70ee81a4fb88c63; snapshot_sha256=0a0da5347791c3c68c736a827f26a3bd0522b1f81539b324076c32f65701589e
- Behavior: Created the TRD at the correctly mirrored engineer path with required metadata and related PRD linkage, without implementation work.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4; fixture_sha256=9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc; output_sha256=822c0cfb01b06b33e1188a5f346c1e2927552767785d65df3155162cf10ef47a; snapshot_sha256=3dc741f798a472bd0825a584f12e487beee7c572316fc75a7cc892e44eee27c8
- Behavior: Created a TRD under the PM path and used prd: ./PRD.md rather than the required engineer path and related_prd field.
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
- Skill: `trd-gen`
- Eval: `eval-003-nested-prd-to-engineer-trd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc` from `agents/engineer/test/trd-gen/evals/workspace/eval-003-nested-prd-to-engineer-trd`.
- Fixture SHA-256: `9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc`
- Prompt SHA-256: `8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b66f9acea93e151819a21f82909f9a6b7d44c68fa52d2116667525e2fe8e9bd7`
- Skill overlay SHA-256: `e4cc003a0e06320ef354c6c9cdbebb2b75980ec8b23ae530ac78b0667fab31da`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f3397b62fc4d049158e92b00f525e136ca990d6c804b1f211ce557bfaf30d03e`
- Metadata SHA-256: `de0335f1a182c8496f115f68dc77dc691a79abeae555386cc002141eada43865`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `mirrors_nested_feature_path` | PASS | With-skill output targets docs/engineer/chat-interface/messages/history/search/TRD.md; manifest confirms the exact path. |
| `preserves_feature_metadata` | PASS | TRD frontmatter contains feature_path chat-interface/messages/history/search, parent_feature chat-interface/messages/history, and feature_level 4. |
| `related_prd_matches_path` | PASS | TRD frontmatter sets related_prd to docs/pm/chat-interface/messages/history/search/PRD.md. |
| `blocks_on_missing_or_unclear_prd_path` | NOT_EXERCISED | The fixture clearly confirms both the PRD feature_path and parent_feature, so the blocking condition is not triggered. |
| `no_plan_or_code` | PASS | Only the TRD is created; the document explicitly states that implementation, code, and IMPLEMENTATION_PLAN.md are outside this task. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4; fixture_sha256=9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc; output_sha256=0b1abb3876f0ee1ae4442687b2ba9c07f63c0f29897ee8ff686aabd9a7f51dee; snapshot_sha256=726037aa24b93efa6a9cca698e33ef9e71bd4a7caac4ae7b87538ee092f7572c
- Behavior: Created the mirrored Engineer TRD with required metadata and PRD traceability, while keeping implementation and code changes out of scope.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4; fixture_sha256=9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc; output_sha256=d66fc0d5f1b0164ebdf3d9b0bc5990c0fb1ba7cf20eace0692a92dcc8cdf264e; snapshot_sha256=cc0b0e8e71ff491a866ec66f49d1083310af49f3840d5a0b352f2e2e0c50413e
- Behavior: Created a TECHNICAL.md under the PM path and did not produce the required Engineer TRD path or metadata evidence.
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

# Eval Result: eval-003-nested-prd-to-engineer-trd

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-003-nested-prd-to-engineer-trd`
- Test case: nested-prd-to-engineer-trd
- Workspace: `workspace/eval-003-nested-prd-to-engineer-trd`
- Evaluation date: 2026-08-07
- Overall result: PASS (partial coverage)
- Behavior result: PASS
- Coverage result: PARTIAL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: PM 已经确认 docs/pm/chat-interface/messages/history/search/PRD.md，其中记录的功能路径是 chat-interface/messages/history/search。请编写对应技术方案。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `mirrors_nested_feature_path`: with_skill workspace 实际仅生成 docs/engineer/chat-interface/messages/history/search/TRD.md；transcript item_7 记录同一路径。
- PASS `preserves_feature_metadata`: TRD.md frontmatter 包含 feature_path、parent_feature 和 feature_level: 4。
- PASS `related_prd_matches_path`: TRD.md 的 related_prd 为 docs/pm/chat-interface/messages/history/search/PRD.md。
- NOT EXERCISED `blocks_on_missing_or_unclear_prd_path`: 实际 PRD 路径和父功能均已确认，未触发缺失或不清晰路径的阻断分支。
- PASS `no_plan_or_code`: with_skill workspace 无 IMPLEMENTATION_PLAN.md、代码或测试文件；TRD 明确说明不授权代码实现，exit_code 为 0。

## With Skill Behavior

with_skill 成功生成嵌套路径 TRD，并额外生成同路径 API.md；frontmatter、related_prd、交接条件均符合要求。记录的输入与输出哈希均与实际文件一致。

## Without Skill Baseline

without_skill 作为对照也生成了正确嵌套路径 TRD，但未生成 API.md，且缺少本次裁决所需的完整 TRD 元数据核验依据。

## Failures / Findings

- None.
- Root cause: 无实际行为失败；仅因缺失路径阻断分支未被测试，覆盖度为 PARTIAL。

## Next Steps

- 增加可触发 NOT EXERCISED 分支的 fixture 后重跑；当前已触发路径没有行为失败。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-003-nested-prd-to-engineer-trd

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-003-nested-prd-to-engineer-trd`
- Test case: nested-prd-to-engineer-trd
- Workspace: `workspace/eval-003-nested-prd-to-engineer-trd`
- Latest result: PASS - durable comparison coverage updated on 2026-06-25 for a real 4-level PRD -> TRD mirror path; no fresh model transcript or runtime output was generated in this worker pass.
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: 4-level PRD at `docs/pm/chat-interface/messages/history/search/PRD.md` with `feature_path: chat-interface/messages/history/search`.
- 4+ fixture path: `chat-interface/messages/history/search`.
- Expected output: TRD target path is `docs/engineer/chat-interface/messages/history/search/TRD.md`, with matching feature path metadata and `related_prd`.
- Fixture files read: `README.md`, `docs/pm/chat-interface/messages/history/search/PRD.md`, workspace metadata, and this comparison.

## Assertions

- PASS `mirrors_nested_feature_path`: TRD path mirrors the 4-level PM path.
- PASS `preserves_feature_metadata`: TRD frontmatter includes matching feature path fields.
- PASS `related_prd_matches_path`: `related_prd` points to the 4-level PRD.
- PASS `blocks_on_missing_or_unclear_prd_path`: unclear PRD path returns to PM instead of guessing.
- PASS `no_plan_or_code`: TRD generation does not write implementation plans or code.

## With Skill

- Expected with-skill behavior is to read `docs/pm/chat-interface/messages/history/search/PRD.md`, preserve `feature_path: chat-interface/messages/history/search`, and write the mirrored Engineer TRD to `docs/engineer/chat-interface/messages/history/search/TRD.md`.
- The generated TRD frontmatter must include `feature: search`, `parent_feature: chat-interface/messages/history`, `feature_level: 4`, and `related_prd: docs/pm/chat-interface/messages/history/search/PRD.md`.
- The TRD request must stop before `IMPLEMENTATION_PLAN.md`, code, tests, or delivery.

## Without Skill / Baseline
- Not run in this worker pass.
- High-level baseline contrast: a generic Engineer response may generate `docs/engineer/history-search/TRD.md` or reuse the older 2-level `docs/engineer/chat-interface/history-search/TRD.md`, losing `messages/history` and producing a mismatched `related_prd`.

## Failures

- None in the durable eval definition, fixture, and assertion alignment reviewed on 2026-06-25.

## Next Steps

- Keep this eval focused on the 4-level PRD -> TRD mirror regression surface covered by the fixture.

## Runtime Artifacts Policy

- Runtime transcripts, verdicts, timing, outputs, and diagnostics should not be committed.
