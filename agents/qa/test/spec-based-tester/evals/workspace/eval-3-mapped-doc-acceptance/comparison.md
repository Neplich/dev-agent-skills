# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `spec-based-tester`
- Eval: `eval-003-mapped-doc-acceptance`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b` from `agents/qa/test/spec-based-tester/evals/workspace/eval-3-mapped-doc-acceptance`.
- Fixture SHA-256: `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b`
- Prompt SHA-256: `b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8ceb46669357c2ad2e3984067ae0ce5c97b019da23d3a0f850d2bedd7e38ab17`
- Skill overlay SHA-256: `fda3e87e887ba889a897540771dbb1fdc6d424a530b084850bba0cba716a1567`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `69ea284c249fd48ea67518dcbbbb4aff0b51c724f5aa24139bc9524759db6c7c`
- Metadata SHA-256: `dbcf12ca577304c6eedeb3847e29d69b72d051700655cd6bd5000bc1d6f7a9d9`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | Locked raw evidence contains the candidate's claimed read order but no tool trace or other proof of sequencing. |
| `verifies_against_code` | PASS | The with_skill output identifies the formal document, its 80-character declaration, the code rule `nickname_max_length = 64`, and the 65–80 character acceptance impact. |
| `treats_unverified_as_low_trust` | PASS | The with_skill output explicitly marks `last_verified_version: unverified` as low trust and bases the key conclusion on the code value 64. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=8df1c764ccf0a61b7779acdb58f6e2e0a697a9ec40b31656040b26404fc2148d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the code/document mismatch, treats the documentation as unverified, and records evidence and impact; read sequencing is not independently provable.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=0651e1aa72e5dda7a97e9cf1d8e62cb5848e26d2cfebc41372ebe2953ebde645; snapshot_sha256=c079e778f877afd1c1077460bc725705ce7e4245cab3271d165e505a99e58cd6
- Behavior: Claims to correct the documentation and add a requirements matrix, with delivery snapshots showing those artifacts.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Capture read-order/tool-trace evidence to exercise the mapped-document-first assertion.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `spec-based-tester`
- Eval: `eval-003-mapped-doc-acceptance`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b` from `agents/qa/test/spec-based-tester/evals/workspace/eval-3-mapped-doc-acceptance`.
- Fixture SHA-256: `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b`
- Prompt SHA-256: `b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8ceb46669357c2ad2e3984067ae0ce5c97b019da23d3a0f850d2bedd7e38ab17`
- Skill overlay SHA-256: `0dc6062e83cf445a1577948355ffb768c08c70474d373f09d93a3ded935ca1bb`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `69ea284c249fd48ea67518dcbbbb4aff0b51c724f5aa24139bc9524759db6c7c`
- Metadata SHA-256: `dbcf12ca577304c6eedeb3847e29d69b72d051700655cd6bd5000bc1d6f7a9d9`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 候选输出提及了映射文档和正式说明，但锁定证据无法证明实际读取顺序。 |
| `verifies_against_code` | PASS | with_skill 明确以 src/profile/validation.rules 中的 nickname_max_length = 64 核对正式说明所称 80，并记录了文档路径、代码事实及 65–80 字符被拒绝的验收影响。 |
| `treats_unverified_as_low_trust` | PASS | with_skill 明确指出 last_verified_version: unverified，将 80 字符说明视为未验证且与代码冲突，并以代码事实作为当前真实限制。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=c0d28846c8e84ed7fb056541df73e1c29a387fb9044bc949cfa3d6cb943c75bc; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别并记录了代码、正式说明、变更映射和 unverified 状态，正确以代码核证限制；未交付需求矩阵文件，并报告因缺少 handoff/规划材料而阻塞。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=26fa338498b0ad7752fcb1973b6f49024deb0375223aee1c084092628c13c3dd; snapshot_sha256=bef1189e8d53eb5ecd1906d4bf5ee746d97e82cbc8462ca2132aec758c58eff9
- Behavior: 报告了 64 与 80 的冲突及影响，并交付了需求矩阵文件；但其输出不能证明正式文档读取顺序或低信任处理过程。
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
- Skill: `spec-based-tester`
- Eval: `eval-003-mapped-doc-acceptance`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b` from `agents/qa/test/spec-based-tester/evals/workspace/eval-3-mapped-doc-acceptance`.
- Fixture SHA-256: `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b`
- Prompt SHA-256: `b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8ceb46669357c2ad2e3984067ae0ce5c97b019da23d3a0f850d2bedd7e38ab17`
- Skill overlay SHA-256: `55ae613f45225c4fd27fe7b7bb1eff99de0a24107c076461ac6a7464ef4fa3ae`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `69ea284c249fd48ea67518dcbbbb4aff0b51c724f5aa24139bc9524759db6c7c`
- Metadata SHA-256: `dbcf12ca577304c6eedeb3847e29d69b72d051700655cd6bd5000bc1d6f7a9d9`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 候选输出提及 change-map 和命中文档，但锁定原始证据无法证明读取顺序或未遍历无关文档。 |
| `verifies_against_code` | PASS | 明确引用 src/profile/validation.rules:1 的 64、正式文档的 80，并记录 65–80 字符将被实现拒绝及其契约影响。 |
| `treats_unverified_as_low_trust` | PASS | 明确识别文档的 last_verified_version 为 unverified，并以代码确认当前限制、将文档与实现的不一致作为待确认事项，而非盲信文档。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=e699d20b9ae1f72d70737274bf06b2eace0633179787b9702042a46387d0dc1f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核对代码与正式说明，记录证据、影响及未验证状态；未能由原始证据证明读取顺序。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=10daf30775fbba080cc0fc53243c1ba1944fb4b6c5870f54fd2a9a611dbe7a3a; snapshot_sha256=a2c4e07233c72e236bc167b166b87b2a1722fa0548878fe29e00e7a41fad52d7
- Behavior: 正确识别 64/80 不一致并生成需求矩阵，行为与 with_skill 基本相同。
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
- Skill: `spec-based-tester`
- Eval: `eval-003-mapped-doc-acceptance`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b` from `agents/qa/test/spec-based-tester/evals/workspace/eval-3-mapped-doc-acceptance`.
- Fixture SHA-256: `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b`
- Prompt SHA-256: `b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8ceb46669357c2ad2e3984067ae0ce5c97b019da23d3a0f850d2bedd7e38ab17`
- Skill overlay SHA-256: `61d94a4bf111e70ade2232cb9d882f35a6012c6ae7909aa0b8f48602aadf3860`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `69ea284c249fd48ea67518dcbbbb4aff0b51c724f5aa24139bc9524759db6c7c`
- Metadata SHA-256: `dbcf12ca577304c6eedeb3847e29d69b72d051700655cd6bd5000bc1d6f7a9d9`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | The locked evidence shows the mapped document was read, but cannot prove it was read first or that unrelated documents were not traversed. |
| `verifies_against_code` | PASS | The with_skill evidence records the formal document's 80-character claim, the code's nickname_max_length = 64, boundary results (64 accepted; 65 and 80 rejected), and the resulting 16-character documentation mismatch and impact. |
| `treats_unverified_as_low_trust` | PASS | The with_skill output and recorded result identify both the formal document and change map as unverified, treat the full alignment gate as blocked, and base the key limit judgment on code and targeted boundary evidence. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=0092f1c7ecb1eb9180ba651b0eaa7825b3043251ee9b2ffb9a1913785ba8f35b; snapshot_sha256=50c9fb38e0b9403de7a7007519705daca44eaf3d29d17439075edcd40069d9e0
- Behavior: Correctly identified and evidenced the mismatch, recorded boundary behavior and impact, and explicitly handled unverified documentation and blocked E2E alignment.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=cb08e18525f2507b7d69df35f763e4dee7d7b85228114d104da03453dc5bf9d1; snapshot_sha256=beef16742ece183e57f0ab982abf4d3065582d75058919d66e1ff0047570dffd
- Behavior: Correctly identified the 64-versus-80 mismatch and recorded a requirements matrix, but did not expose the unverified trust status.
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
- Skill: `spec-based-tester`
- Eval: `eval-003-mapped-doc-acceptance`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b` from `agents/qa/test/spec-based-tester/evals/workspace/eval-3-mapped-doc-acceptance`.
- Fixture SHA-256: `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b`
- Prompt SHA-256: `b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b00130d1b7a5468374704d3f87e6d53d8fc4e258a5b47d2ce1aedb6133dc481d`
- Skill overlay SHA-256: `46ffa1a74f0eaa93e8e4995713b7c67a998b633e4325098596292dae49b6afe3`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `69ea284c249fd48ea67518dcbbbb4aff0b51c724f5aa24139bc9524759db6c7c`
- Metadata SHA-256: `dbcf12ca577304c6eedeb3847e29d69b72d051700655cd6bd5000bc1d6f7a9d9`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill 明确识别 src/profile/validation.rules，读取 change-map 命中的 docs/site/api/profile-validation.md，并未报告遍历无关文档。 |
| `verifies_against_code` | PASS | with_skill 以 src/profile/validation.rules:1 的 nickname_max_length = 64 核对文档的 80 字符声明，明确记录两者差异及 65–80 字符输入可能被拒绝的影响。 |
| `treats_unverified_as_low_trust` | PASS | with_skill 识别 last_verified_version: unverified，将文档作为低信任导航，并说明最终结论以代码事实为准。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=a9d609745d2bb48f99d4c8e8b2a2d0f73837b7c5683f68136e560b324dff8e66; snapshot_sha256=b7e06e10b7cbfcc659ec65c6b62cf2c9fe4ed9b54e6f569e07f25f6be677db16
- Behavior: 针对性读取映射文档与代码，确认 64/80 不一致，按 unverified 低信任处理，并记录证据、影响和验收失败结论。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=4348d4b14691973bf909487aa92bea894a2fd7a18bbeef43ab4d8df43b266d5c; snapshot_sha256=5022061a888f109e26bf6507ea042ee9f68f318f56b45d98c7571565f3792a6e
- Behavior: 报告代码限制为 64，但修改了正式文档为 64 并新增需求矩阵；未将文档原始 80 字符声明作为当前未核证事实保留。
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
- Skill: `spec-based-tester`
- Eval: `eval-003-mapped-doc-acceptance`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b` from `agents/qa/test/spec-based-tester/evals/workspace/eval-3-mapped-doc-acceptance`.
- Fixture SHA-256: `bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b`
- Prompt SHA-256: `b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9bc7bc56a69ed03539b92f8b1b5ab784d65f1b99345268b0e2860387a93c400f`
- Skill overlay SHA-256: `5682fc1ffcb4eb879c1789588b290db4ff6dc8f83dc85473fb6c12c8ad0ebd72`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `69ea284c249fd48ea67518dcbbbb4aff0b51c724f5aa24139bc9524759db6c7c`
- Metadata SHA-256: `dbcf12ca577304c6eedeb3847e29d69b72d051700655cd6bd5000bc1d6f7a9d9`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | PASS | with_skill identifies the change-map mapping to docs/site/api/profile-validation.md and limits the stated scope to the mapped formal documentation and target rule. |
| `verifies_against_code` | PASS | It cites src/profile/validation.rules:1 as nickname_max_length = 64, contrasts it with the formal document's 80-character statement, and records the 65–80 impact. |
| `treats_unverified_as_low_trust` | FAIL | Although it uses code as the source for the 64-character conclusion, it does not explicitly identify last_verified_version: unverified or state that the mapped document is low-trust location guidance. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=c2be3e85b8042ddc5d95581bf0ee66d097f82848cb695202f7d9d2c853ed3d7d; snapshot_sha256=46a5e0057caa3ac0cba04695fc77073fdbe686e53982ead2c1b6b5d7df911874
- Behavior: Compared the mapped formal document against code, correctly preserved the 64-versus-80 discrepancy, documented its impact, and noted runtime checks were unavailable.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0800640829a83735e541e027ba4771a2f52dd5cf39982ebc89e3721cf0f1d96; fixture_sha256=bfb7b9881699180197883abe46418a65cf0676dceb7443a1b2ac7db5c3b8ae9b; output_sha256=d9777e068ab66eb8d0a8bdf5143c496938aa8783e8bc8820497e220dc98f3f6e; snapshot_sha256=0d1731ffeb77fe20a50924fd76da10ff156cc2f8b76bccbc6faf8d3b297455d5
- Behavior: Reported 64 characters and changed the formal document to match, claiming implementation and documentation consistency.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- The with_skill output does not explicitly treat last_verified_version: unverified as a low-trust locator signal.
- Next: Explicitly record the document's unverified status and explain that all acceptance conclusions are grounded in code or executable test evidence.

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

# Eval Result: eval-003-mapped-doc-acceptance

## Evaluation Target

- Agent: `qa`
- Skill: `spec-based-tester`
- Eval: `eval-003-mapped-doc-acceptance`
- Test case: mapped-doc-acceptance
- Workspace: `workspace/eval-3-mapped-doc-acceptance`
- Natural user prompt:

> 请对 src/profile/validation.rules 中的昵称长度规则执行规范验收，给出需求矩阵和证据结论。

- Expected artifact: 基于映射文档定位、以代码事实核证的规范验收报告，并明确记录文档与代码的分歧。

## Test Set / Fixture Version

- Schema: `evals.json` v1.0，使用 source HEAD `47adbbc9` 的当前 prompt、assertions 与 fixture。
- Fresh run window: 2026-08-07 00:26:03 至 00:42:04（Asia/Shanghai）。
- Runtime root: `/tmp/qa-fresh-evals-20260807-002603-9bd07750/spec-based-tester--eval-003-mapped-doc-acceptance/`。
- Fixture identity: 两条 lane 的初始可见 fixture manifest 完全相同，SHA-256 为 `d1727ff5d50443ad4c264da470cb603d79901dea16aa93d2189a0984f3434bd8`。
- Lane isolation: 先完成并销毁全部 15 个 `without_skill` 独立随机顶层临时 root，再创建任何 `with_skill` root；`with_skill` 按 target skill 分组执行，每条 lane 都使用独立顶层 workspace、`HOME`、`CODEX_HOME` 和 temp 目录，不存在 candidate 可读取的 sibling lane。
- Controlled variable: 两条 lane 使用逐字相同 prompt、相同 fixture manifest、相同隔离配置和同一份认证材料；唯一显式变量是 `with_skill` 的隔离 `CODEX_HOME` 安装并加载目标 QA skill，`without_skill` 的目标 skill 加载次数为 0。
- Evidence isolation: 30 个 candidate 全部结束且临时 root 全部销毁后，才将内存中的 candidate、tool trace 和最终 workspace 快照持久化到 runtime root。
- Candidate leakage audit: 两条 lane 均未命中 `eval_metadata.json`、`evals/evals.json`、`comparison.md`、expected output、assertions 或 judge schema。
- Judge: candidate 全部结束后，第三个独立随机顶层、只读 fresh Codex 会话实际检查两条 candidate 输出、JSONL tool trace、status 和最终 workspace 快照，再按当前 assertions 判定。
- Runtime health: candidate 与 judge 均 `rc=0`、无 timeout；judge root 已销毁。

## Latest Result

- Behavior result: **PASS**（PASS 3 / FAIL 0 / NOT EXERCISED 0）
- Coverage result: **FULL**
Overall result: PASS

## Invalidated Prior Run

上一轮 QA paired run 将 `with_skill` 与 `without_skill` 放在可交叉读取的 sibling 路径，物理隔离不合格；该轮 candidate、baseline、judge 与结论全部作废，未作为本轮输入，也不保留为当前结果。本文件的当前结论仅来自 `qa-fresh-evals-20260807-002603-9bd07750`。

## Assertions

| Assertion | With skill | With-skill evidence | Without skill | Baseline evidence |
| --- | --- | --- | --- | --- |
| `reads_mapped_docs_first`<br>优先读取 change-map 命中的正式文档 | PASS | transcript item_2 的命令顺序为读取 change-map.yaml、profile-validation.md，再读取 validation.rules；快照仅含相关 fixture 与生成报告，没有遍历无关文档。 | FAIL | transcript item_2 先读取 validation.rules 和 API 文档，item_3 才读取 change-map.yaml，未满足 mapped docs first。 |
| `verifies_against_code`<br>用代码证据核证文档声明 | PASS | transcript item_2 读取代码；快照中的 validation.rules 明确为 nickname_max_length = 64，API 文档明确为 at most 80 characters；candidate.md 和生成的 spec-validation.md 均记录了文档路径、声明、代码事实及 65–80 字符欠接受影响。 | PASS | transcript item_2 读取代码和文档；candidate.md 明确记录文档要求 80、代码为 64、存在 65–80 字符不一致及验收影响。 |
| `treats_unverified_as_low_trust`<br>未核证文档按最低信任处理 | PASS | 两份映射文档快照均含 last_verified_version: unverified；transcript item_3 与生成报告将运行时检查列为未执行，并指出缺少 PRD/TRD/实现计划、无法确认权威边界，关键不一致结论回到代码与静态证据核证。 | FAIL | 虽然读取并提及 unverified，但 candidate.md 直接将文档作为规范基线，未明确按低信任定位线索处理，也未充分记录权威性不确定性。 |

## With-Skill Behavior

with_skill 三条断言均有 transcript 与最终快照证据支持。按 change-map → API 文档 → 代码顺序核验，并确认文档标记为 unverified、代码实际为 64、文档声明为 80。

## Fresh Without-Skill Baseline

without_skill 作为 baseline：未先读取 change-map，先读取代码和 API 文档；但能识别 64/80 分歧并记录影响。

## Failures

- 无。

## Not Exercised

- 无。

## Next Steps

- 如需运行时覆盖，应补充 64、65、80、81 字符边界测试，并先确认 64 或 80 的权威需求。

## Runtime Artifacts Policy

- Candidate command: `codex exec --skip-git-repo-check -C <isolated-workspace> -s workspace-write --ephemeral --ignore-user-config --ignore-rules -m gpt-5.6-luna -c 'model_reasoning_effort="medium"' --json -o <runtime-output> -`。
- Judge 使用同一模型与 reasoning effort，在独立 `read-only` root 中按结构化 output schema 判定。
- candidate、baseline、transcript、verdict、fixture snapshots、status、timing 与 diagnostics 仅保留于上述 `/tmp` runtime root，不提交到 git；仓库只更新 canonical `comparison.md`。
