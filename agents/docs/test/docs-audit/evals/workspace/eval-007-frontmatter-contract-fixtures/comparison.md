# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-007-frontmatter-contract-fixtures`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f` from `agents/docs/test/docs-audit/evals/workspace/eval-007-frontmatter-contract-fixtures`.
- Fixture SHA-256: `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f`
- Prompt SHA-256: `49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `216827bc3e07bc68d228647a6fadcd479f48a986964f70c0c40f48052e42886f`
- Eval definition SHA-256: `6bde344495a08502946e81bb93f2ae1c40e1aff64c95e853b673dd5a307e9ade`
- Metadata SHA-256: `ac5c625c3b447eed92814a4915de66331bf3c2449cbef00676c3c687ad5d80de`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | The with_skill output accepts v0.4.0, the maintainer confirmation, both refs, the pre-tag phase, requested action, and evidence inventory as the audit basis. |
| `rejects_standard_doc_type` | PASS | It classifies catalog-search.md as stale because doc_type: standard is invalid. |
| `rejects_empty_related_code` | PASS | It classifies catalog-export.md as stale because related_code is empty. |
| `rejects_missing_last_verified_version` | PASS | It classifies catalog-status.md as stale because last_verified_version is missing. |
| `rejects_empty_owners` | PASS | It classifies catalog-bulk-update.md as stale because owners: [] is invalid. |
| `accepts_valid_api_page` | PASS | It does not classify catalog-items.md as stale, and records its route evidence and resulting unverified fact-layer conclusion. |
| `blocks_release_for_invalid_frontmatter` | PASS | It returns blocked, retains all four invalid pages as stale, and explicitly states that no partial stamp is permitted. |
| `uses_shared_contract_source` | NOT_EXERCISED | The output mentions docs-agent/docs-site-bootstrap generally, but the locked evidence does not prove explicit use and consistency of frontmatter-contract.md and check-frontmatter.mjs. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=5115736f566770d4823dc1522e47cc1cb3fa67be662e5cecd898245b3299741d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepts the confirmed audit entry, classifies each invalid page, accepts catalog-items into fact-layer review, and blocks release.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=29fe8fb32399c63a7bd82966b8e1a43c75a5fda1b1eb3d4a5473349aa900f7f2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline also reaches a no-go conclusion and spots several invalid pages, but provides less structured audit reasoning and does not establish the same complete blocked workflow.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide direct evidence of the shared frontmatter contract and check-frontmatter.mjs consistency if that assertion must be exercised.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-007-frontmatter-contract-fixtures`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f` from `agents/docs/test/docs-audit/evals/workspace/eval-007-frontmatter-contract-fixtures`.
- Fixture SHA-256: `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f`
- Prompt SHA-256: `49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6bde344495a08502946e81bb93f2ae1c40e1aff64c95e853b673dd5a307e9ade`
- Metadata SHA-256: `ac5c625c3b447eed92814a4915de66331bf3c2449cbef00676c3c687ad5d80de`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | With-skill output accepts the pre-tag scope, v0.4.0, and bounded 4a1b2c3..7c9e2af refs. |
| `rejects_standard_doc_type` | PASS | Correctly classifies catalog-search.md as stale/mismatch because doc_type is standard. |
| `rejects_empty_related_code` | PASS | Correctly classifies catalog-export.md as stale/mismatch because related_code is empty. |
| `rejects_missing_last_verified_version` | PASS | Correctly classifies catalog-status.md as stale/mismatch because last_verified_version is missing. |
| `rejects_empty_owners` | PASS | Correctly classifies catalog-bulk-update.md as stale/mismatch because owners is empty. |
| `accepts_valid_api_page` | PASS | The locked fixture shows catalog-items.md has valid API frontmatter and its declared route matches routes.txt; the output records that consistency while separately marking factual verification unverified. |
| `blocks_release_for_invalid_frontmatter` | PASS | Reports blocked, retains all four invalid pages as stale, and does not return ready_for_tag or claim partial stamping. |
| `uses_shared_contract_source` | NOT_EXERCISED | The locked output does not identify the shared frontmatter contract or generator checker, and raw evidence cannot prove the hidden source/logic relationship. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=1cac81383e0279294b0a2bc19809b7e3c110015f32321e2ac18b269e22fa3534; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepts the audit entry, classifies the four invalid pages, cross-checks catalog-items against the route evidence, and blocks the pre-tag audit.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=c4b4977452197fc388aa708b9c1a7ca73ca17f13a79c43a7e630d8b3ed83a5cf; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Baseline incorrectly treats the refs as an empty diff and reports broad verification failures, without applying the specified frontmatter classifications.
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
- Eval: `eval-007-frontmatter-contract-fixtures`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f` from `agents/docs/test/docs-audit/evals/workspace/eval-007-frontmatter-contract-fixtures`.
- Fixture SHA-256: `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f`
- Prompt SHA-256: `49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d339a8370a29b3fb2a69aa1879b1226165ec088d306a4e2e7a01258df2326973`
- Skill overlay SHA-256: `0bc7243cbb5cff3e77d9ba448e020a1a1f279639f8db6a365faac208b8e1dcc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6bde344495a08502946e81bb93f2ae1c40e1aff64c95e853b673dd5a307e9ade`
- Metadata SHA-256: `ac5c625c3b447eed92814a4915de66331bf3c2449cbef00676c3c687ad5d80de`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | with_skill accepts the maintainer-confirmed v0.4.0, base_ref 4a1b2c3, target_ref 7c9e2af, pre-tag phase, and evidence inventory. |
| `rejects_standard_doc_type` | PASS | catalog-search.md is classified stale because doc_type standard is invalid. |
| `rejects_empty_related_code` | PASS | catalog-export.md is classified stale because related_code is empty. |
| `rejects_missing_last_verified_version` | PASS | catalog-status.md is classified stale because last_verified_version is missing. |
| `rejects_empty_owners` | PASS | catalog-bulk-update.md is classified stale because owners is empty. |
| `accepts_valid_api_page` | PASS | catalog-items.md is classified verified and its declared route is confirmed against src/catalog/routes.txt. |
| `blocks_release_for_invalid_frontmatter` | PASS | The four invalid pages are retained as stale, the phase result is blocked, ready_for_tag is not returned, and no stamping or repair is performed. |
| `uses_shared_contract_source` | NOT_EXERCISED | The locked candidate output does not identify docs-agent's frontmatter-contract.md or confirm consistency with check-frontmatter.mjs; raw evidence cannot prove this process/source assertion. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=f288ecb0f162d2bf67978ab1b8078c60f9bff27c2e1ef39d15911b2a7bb40b8e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepts the confirmed audit entry, classifies the four invalid pages as stale, verifies catalog-items.md against route evidence, and blocks the pre-tag audit without mutation.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=c642a0e476b603f5151dcbb7845421e27a0ec8b11cb0cd1f3b76c12b741e6915; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reaches a NO-GO/blocking conclusion and identifies the invalid pages, but incorrectly treats catalog-items.md as blocked due to unverified version and does not clearly apply the required stale classification contract.
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
- Eval: `eval-007-frontmatter-contract-fixtures`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f` from `agents/docs/test/docs-audit/evals/workspace/eval-007-frontmatter-contract-fixtures`.
- Fixture SHA-256: `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f`
- Prompt SHA-256: `49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9e9abf391c9ccd9564d35b5def50bc0374b1db0886710676c4d48422839746ae`
- Skill overlay SHA-256: `c66ac938bf9158faa694d7c3e311e913ddc4a06da11de703a881234f257c470c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6bde344495a08502946e81bb93f2ae1c40e1aff64c95e853b673dd5a307e9ade`
- Metadata SHA-256: `ac5c625c3b447eed92814a4915de66331bf3c2449cbef00676c3c687ad5d80de`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | With-skill output accepts v0.4.0, the confirmed base/target refs, pre-tag phase, and audit scope. |
| `rejects_standard_doc_type` | PASS | Classifies catalog-search.md as stale because doc_type: standard is invalid. |
| `rejects_empty_related_code` | PASS | Classifies catalog-export.md as stale because related_code: [] is invalid. |
| `rejects_missing_last_verified_version` | PASS | Classifies catalog-status.md as stale because last_verified_version is missing. |
| `rejects_empty_owners` | PASS | Classifies catalog-bulk-update.md as stale because owners: [] is invalid. |
| `accepts_valid_api_page` | PASS | Marks catalog-items.md verified, states its frontmatter is valid, and matches it to GET /catalog/items. |
| `blocks_release_for_invalid_frontmatter` | FAIL | Although the output blocks release and identifies four stale pages, it marks catalog-items.md verified, contradicting the requirement not to locally seal a valid page while invalid pages remain in scope. |
| `uses_shared_contract_source` | FAIL | The output says the shared contract and generator files are missing, but does not identify docs-agent/frontmatter-contract.md as the source of truth or confirm consistency with docs-site-bootstrap/check-frontmatter.mjs. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=69253a43f76b6bade86fc55fec1ef871ea874fd1d8c2c19e6c172581bcaa9154; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly accepts the audit entry, classifies the four invalid pages, and blocks release, but incorrectly locally verifies catalog-items.md and does not establish the shared contract source/logic consistency.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=bc8c0069f558bc43e7bebdaa9594495d3a12cfe7fec64d91d27097453f53296c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly blocks the release and identifies several issues, but incorrectly treats catalog-items.md as having an invalid last_verified_version and misses the required per-field classifications.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with-skill output locally verifies catalog-items.md despite invalid pages remaining in the affected set.
- The with-skill output omits the required shared-contract source and validation-logic consistency conclusion.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-007-frontmatter-contract-fixtures`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f` from `agents/docs/test/docs-audit/evals/workspace/eval-007-frontmatter-contract-fixtures`.
- Fixture SHA-256: `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f`
- Prompt SHA-256: `49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2d24da5f976a5ab2710c2c072a19015e074d314e0ebdb88f1c28831425f1b98c`
- Skill overlay SHA-256: `40330c17a3b77f25a1b1a716fa5e9355e0011db79d19014344ed516affba11c8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6bde344495a08502946e81bb93f2ae1c40e1aff64c95e853b673dd5a307e9ade`
- Metadata SHA-256: `ac5c625c3b447eed92814a4915de66331bf3c2449cbef00676c3c687ad5d80de`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | 明确接受 v0.4.0、4a1b2c3..7c9e2af、pre-tag 阶段及维护者确认的入口。 |
| `rejects_standard_doc_type` | PASS | 将 catalog-search.md 的 doc_type: standard 判为 stale。 |
| `rejects_empty_related_code` | PASS | 将 catalog-export.md 的 related_code: [] 判为 stale。 |
| `rejects_missing_last_verified_version` | PASS | 将缺少 last_verified_version 的 catalog-status.md 判为 stale。 |
| `rejects_empty_owners` | PASS | 将 owners: [] 的 catalog-bulk-update.md 判为 stale。 |
| `accepts_valid_api_page` | FAIL | catalog-items.md 的七个 frontmatter 字段在原始 fixture 中合法，且 routes.txt 提供对应 endpoint；with_skill 却将其判为 unverified，未确认其通过 frontmatter 校验并进入事实层。 |
| `blocks_release_for_invalid_frontmatter` | PASS | 识别四个非法页面为 stale，阶段结果为 blocked，未返回 ready_for_tag，也未局部盖章。 |
| `uses_shared_contract_source` | FAIL | 未明确以 docs-agent 的 frontmatter-contract.md 为判定真源，也未确认与 docs-site-bootstrap 的 check-frontmatter.mjs 逻辑一致。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=03eba3f3f0336391562ba56963eb0119a91d5fdce2aded556326ba990e39db42; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确接受审计入口、识别四个非法页面并阻塞发布；但误判合法 API 页面，且未提供共享 contract source 一致性确认。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=7d72dcc2c223230bcf75a2932f5e74aa9b05857eec51a7e244d233916fb40003; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确给出 No-Go，但错误地将合法的 catalog-items.md 判为不通过，并以未验证版本等额外理由泛化页面失败。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未接受 fixture 中 frontmatter 合法且有 routes 证据的 catalog-items.md。
- with_skill 未明确验证 docs-agent contract 与 check-frontmatter.mjs 同源一致。
- Next: 修正 catalog-items.md 的 frontmatter 判定并将其纳入事实层核对。
- Next: 明确引用 frontmatter-contract.md，并确认其与 check-frontmatter.mjs 的校验逻辑一致。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-007-frontmatter-contract-fixtures`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f` from `agents/docs/test/docs-audit/evals/workspace/eval-007-frontmatter-contract-fixtures`.
- Fixture SHA-256: `1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f`
- Prompt SHA-256: `49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6bde344495a08502946e81bb93f2ae1c40e1aff64c95e853b673dd5a307e9ade`
- Metadata SHA-256: `ac5c625c3b447eed92814a4915de66331bf3c2449cbef00676c3c687ad5d80de`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | 接受 release-entry.md 中确认的 v0.4.0、base_ref 4a1b2c3、target_ref 7c9e2af、pre-tag 阶段和证据清单。 |
| `rejects_standard_doc_type` | PASS | 将 catalog-search.md 因 doc_type: standard 不在允许枚举中判为 stale。 |
| `rejects_empty_related_code` | PASS | 将 catalog-export.md 因 related_code: [] 判为 stale。 |
| `rejects_missing_last_verified_version` | PASS | 将 catalog-status.md 因缺少必需的 last_verified_version 判为 stale。 |
| `rejects_empty_owners` | PASS | 将 catalog-bulk-update.md 因 owners: [] 判为 stale。 |
| `accepts_valid_api_page` | FAIL | 虽核对了 catalog-items.md 和 routes.txt，但将该页面判为“未完成验证，阻塞”，未确认其七个必填字段和值合法并通过 frontmatter 校验进入事实层。 |
| `blocks_release_for_invalid_frontmatter` | PASS | 将四个非法页面保留为 stale，结论为 blocked，并明确不能返回 ready_for_tag 或执行统一版本戳更新。 |
| `uses_shared_contract_source` | FAIL | 未明确以 docs-agent 的 frontmatter-contract.md 为判定真源，也未确认与 docs-site-bootstrap 的 check-frontmatter.mjs 逻辑一致。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=9607fb23554bb8d43dd7f789eb88039da2a4a8b25caf7d564eb5391a6212b8fd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确接受审计入口并识别四个非法页面、代码证据缺口及 blocked 结果，但未接受合法 catalog-items 页面进入事实层，也未明确共享合同真源。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=49a9f020c04120ad8bdb6f9b036cf5ce5bd9266f99e431e7e0059400223b90de; fixture_sha256=1219a80a8f97201ae3cdd929f2d631a2ba100cf6ab153bec6afe2b6d163ff59f; output_sha256=7e6b2e61a131daca2632073a9ad425c5fc8d2168db9ff5638039c64152b3a294; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别出 NO-GO、若干 frontmatter 和证据问题，但未给出 blocked 阶段结论，也未完整执行合同层审计。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- accepts_valid_api_page 未满足对 catalog-items.md 七个必填字段合法性、frontmatter 通过及进入事实层的确认。
- uses_shared_contract_source 未提及 frontmatter-contract.md 或 check-frontmatter.mjs 的同源一致性。
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
- Eval: `eval-007-frontmatter-contract-fixtures`

## Test Set / Fixture Version

- Fixture version: docs-audit A3 / 2026-08-05
- Assertions: 8

## Latest Result

- Behavior result: `FAIL`（with）/ `FAIL`（without）— 本轮 #238 fresh 隔离重跑（2026-08-06）
- Coverage result: `FULL`（with）/ `FULL`（without）— 本轮重跑实际触发的断言场景
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

Overall result: FAIL

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | PASS | 两条 lane 均读取并采用 `release-entry.md` 中维护者确认的 `v0.4.0`、`4a1b2c3`、`7c9e2af`、pre-tag 请求及证据清单。 |
| `rejects_standard_doc_type` | PASS | PASS | 两条报告均将 `invalid-standard-doc-type.md` 判为 stale/失败；文件含 `doc_type: standard`。 |
| `rejects_empty_related_code` | PASS | PASS | 两条报告均将 `invalid-empty-related-code.md` 判为 stale/失败；文件含 `related_code: []`。 |
| `rejects_missing_last_verified_version` | PASS | PASS | 两条报告均将 `invalid-missing-last-verified-version.md` 判为 stale/失败；文件缺少 `last_verified_version`。 |
| `rejects_empty_owners` | PASS | PASS | 两条报告均将 `invalid-empty-owners.md` 判为 stale/失败；文件含 `owners: []`。 |
| `accepts_valid_api_page` | PASS | PASS | `valid-catalog.md` 七个必填字段均合法；其 API 声明与 `src/catalog/routes.txt` 的 `GET /catalog/items -> 200 {"items":[]}` 一致，两条报告均确认该页有效。 |
| `blocks_release_for_invalid_frontmatter` | PASS | FAIL | with_skill 明确结果为 `blocked`、不得 `ready_for_tag`，且未写入 stamp；without_skill 虽给出整体 NO-GO，但把合法页单独标为“通过”，构成断言禁止的局部盖章。 |
| `uses_shared_contract_source` | FAIL | FAIL | 两条 lane 都未能确认 `docs-agent` 的 `frontmatter-contract.md` 与 `check-frontmatter.mjs` 存在或同源一致；with_skill 明确报告“版本面证据缺失”。 |

未满足断言（with/without 任一 FAIL）：``blocks_release_for_invalid_frontmatter``、``uses_shared_contract_source``



## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `accepts_confirmed_audit_entry` | PASS | 从 `release-entry.md` 分别解析 `v0.4.0`、base `4a1b2c3`、target `7c9e2af`、pre-tag 请求和证据清单，未从 ref 推断版本。 |
| `rejects_standard_doc_type` | PASS | 在旧七项合法枚举契约下，`doc_type: standard` 不在合法枚举中，页面判 `stale`。 |
| `rejects_empty_related_code` | PASS | `related_code: []` 违反非空字符串数组契约，页面判 `stale`。 |
| `rejects_missing_last_verified_version` | PASS | 缺少无条件必填的 `last_verified_version`，页面判 `stale`。 |
| `rejects_empty_owners` | PASS | `owners: []` 违反非空字符串数组契约，页面判 `stale`。 |
| `accepts_valid_api_page` | PASS | 合法页七字段通过，并以 `routes.txt` 核对 GET/200/items 后判 `verified`。 |
| `blocks_release_for_invalid_frontmatter` | PASS | 完整集合含 4 个 stale，阶段 `blocked`，合法页保持 `unverified`，没有局部盖章。 |
| `uses_shared_contract_source` | PASS | 报告明确以 `frontmatter-contract.md` 为真源，并说明判定与 bootstrap 宿主 validator 应实现的共享契约一致；fixture 不含脚本，未虚构执行。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮成功 fresh rerun，证据位于 `tmp/eval-runs/117/eval-007-frontmatter-contract-fixtures/with_skill/`；首次并发尝试未产出最终候选，已从判定证据中排除。
- 候选只新增 `audit-v0.4.0.md`，未修复 fixture、修改页面 stamp 或创建 metadata。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮独立 fresh baseline，使用同一 prompt 与 pristine fixture，证据位于 `tmp/eval-runs/117/eval-007-frontmatter-contract-fixtures/without_skill/`；未复用历史 baseline。
- baseline 也得到 1 合法/4 stale 与 blocked，但零写入，且无法提供 docs-audit 入口 gate、共享契约真源和契约报告持久化的同等证据。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure。fixture 的合成 refs 不可解析且未附 patch；候选按维护者确认的 evidence inventory 复现影响集合并明确限制。本 eval 核心是入口与 frontmatter 契约，故为 harness 限制而非协议缺陷。

## Next Steps

- 使用当前包含 `manual` 的八项枚举契约重跑 fresh with-skill lane、同轮 fresh without-skill baseline 与独立 judge；验证后再替换 `BLOCKED`。

## Runtime Artifact Policy

- 本轮候选、transcripts、workspace 副本与失败尝试诊断仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
