# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `test-writer`
- Eval: `eval-002-mapped-pagination-tests`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d` from `agents/engineer/test/test-writer/evals/workspace/eval-002-mapped-pagination-tests`.
- Fixture SHA-256: `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d`
- Prompt SHA-256: `868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8676e9bdfb5dcb168ade64b20ca31fd5f471aaa2778319375ec606582ddd34da`
- Skill overlay SHA-256: `3ddde57487997fd2ff39d31cb5f9f0b20bccf604d883b4e7f63c7540bbbf4537`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `dffdc1de9650924aeba7f48471eac1b4c1592e52cef441419d14a463af648ff5`
- Metadata SHA-256: `6a60b69beab2bdd4c854670cd54e7749219cde65551c8e29d984d322f4c34c88`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | The locked output claims the mapped document was read, but raw evidence cannot prove read order or that unrelated documents were not scanned. |
| `verifies_against_code` | NOT_EXERCISED | The candidate correctly reports 25 from defaults.txt and the 50-versus-25 conflict, but test expectations were not delivered because boundary semantics require confirmation. |
| `treats_unverified_as_low_trust` | PASS | The candidate explicitly treats the unverified document as conflicting low-trust evidence and does not use 50 in a test assertion. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=a279e3848dd486bfa1e3e1a5070e59e2bbd581f9d7bba81bfa659220a6fabc0a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Verified the code default, identified the unverified documentation conflict, and safely paused before inventing boundary semantics or modifying files.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=b6950a72c26d30a74e94807b92358487a4de14bb612d18430a8f2ac7b8515c23; snapshot_sha256=e4d7f770b2c2511962c84d79770af27de0bfdf76eb7008c032cc9ea1345ac0a4
- Behavior: Added boundary tests and modified the unverified documentation, while inferring boundary behavior not established by the fixture.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Confirm the intended behavior for zero, negative, and over-limit page sizes, then write tests using the code default of 25.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `test-writer`
- Eval: `eval-002-mapped-pagination-tests`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d` from `agents/engineer/test/test-writer/evals/workspace/eval-002-mapped-pagination-tests`.
- Fixture SHA-256: `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d`
- Prompt SHA-256: `868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8676e9bdfb5dcb168ade64b20ca31fd5f471aaa2778319375ec606582ddd34da`
- Skill overlay SHA-256: `3ddde57487997fd2ff39d31cb5f9f0b20bccf604d883b4e7f63c7540bbbf4537`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dffdc1de9650924aeba7f48471eac1b4c1592e52cef441419d14a463af648ff5`
- Metadata SHA-256: `6a60b69beab2bdd4c854670cd54e7749219cde65551c8e29d984d322f4c34c88`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | The locked evidence shows the mapped document was identified, but cannot prove the required read order or that unrelated documents were not scanned. |
| `verifies_against_code` | PASS | The delivered test reads src/pagination/defaults.txt and asserts default_page_size is 25; the candidate also reports the documented value 50 is inconsistent. |
| `treats_unverified_as_low_trust` | PASS | The delivered tests use the source defaults file for expectations and do not assert the unverified document value of 50 as the default. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=78de78ef9a4c98451284273c38c0c532af256a283d73f8a3157fe0152c05cf99; snapshot_sha256=ac3bc893a064b7df47773123964cfd6d5e1a2ca900835d367afc8abe26890739
- Behavior: Delivered tests grounded in defaults.txt, asserting 25, 100, and their ordering, while flagging the unverified document mismatch.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=2a08c0ca4e3b1613ec5c4c9ec94e9bd58252fe9e49748c2e5de01686db84dc1d; snapshot_sha256=5eaf5ac57d9d7fc528dd9b9b3a2984047bc06fab8373bbe282ed2132e6322af2
- Behavior: Reported correct source values and mismatch, and delivered broader boundary tests.
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
- Skill: `test-writer`
- Eval: `eval-002-mapped-pagination-tests`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d` from `agents/engineer/test/test-writer/evals/workspace/eval-002-mapped-pagination-tests`.
- Fixture SHA-256: `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d`
- Prompt SHA-256: `868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8676e9bdfb5dcb168ade64b20ca31fd5f471aaa2778319375ec606582ddd34da`
- Skill overlay SHA-256: `951d3480264b2e92c6fe060b9ff2dd8bbbbc16570bec34932e5d89da435a6181`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dffdc1de9650924aeba7f48471eac1b4c1592e52cef441419d14a463af648ff5`
- Metadata SHA-256: `6a60b69beab2bdd4c854670cd54e7749219cde65551c8e29d984d322f4c34c88`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 候选输出与锁定原始证据无法证明具体读取顺序或未扫描无关文档。 |
| `verifies_against_code` | PASS | with_skill 明确报告源码默认页大小为 25、文档为 50 且存在不一致；交付的测试直接从 src/pagination/defaults.txt 读取并断言默认值为 25。 |
| `treats_unverified_as_low_trust` | PASS | 测试未将文档中的 50 写入断言，而是以源码配置为测试事实；候选输出也将文档数值标为不一致。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=c9a0107682343fad0c8d5863d26ab9e4356eda3ea660ea48b4b7ffe20a64c506; snapshot_sha256=e04d922ef186a3d3c491ef21e7183893785dd1f0617c987cbfac84789ee9c2c0
- Behavior: 以源码 25 为测试预期，识别文档 50 的不一致，并交付 3 项通过的测试；未覆盖不存在运行时实现的超限行为。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=05364080d78f6cbf3e501e619e9b75c1a0ba87eff240e99f74d0f2a1ed44249e; snapshot_sha256=ad5876a80445efd9fb229168ad188515e5330b3dc93d16b5a71f1c503c4ab3ca
- Behavior: 报告默认值 25，识别文档中的 50 不一致，并交付测试；未提供可验证的读取顺序证据。
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
- Skill: `test-writer`
- Eval: `eval-002-mapped-pagination-tests`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d` from `agents/engineer/test/test-writer/evals/workspace/eval-002-mapped-pagination-tests`.
- Fixture SHA-256: `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d`
- Prompt SHA-256: `868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8676e9bdfb5dcb168ade64b20ca31fd5f471aaa2778319375ec606582ddd34da`
- Skill overlay SHA-256: `951d3480264b2e92c6fe060b9ff2dd8bbbbc16570bec34932e5d89da435a6181`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dffdc1de9650924aeba7f48471eac1b4c1592e52cef441419d14a463af648ff5`
- Metadata SHA-256: `6a60b69beab2bdd4c854670cd54e7749219cde65551c8e29d984d322f4c34c88`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 锁定的原始证据未能证明读取顺序或是否扫描了无关文档。 |
| `verifies_against_code` | PASS | with_skill 输出明确核对代码默认页大小为 25，识别文档中的 50 不一致，并新增测试断言默认值为 25。 |
| `treats_unverified_as_low_trust` | PASS | with_skill 输出明确指出文档为 unverified、数值与代码不一致，并未将文档的 50 写入测试预期。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=a1ff6961c917aec3cf24658bbb8f40a4932ce963f8ab07795727d1e11e2bea91; snapshot_sha256=494c427ce799f247f47b67bc6d36f299fdfe6a29a323941ae71b464d386efae7
- Behavior: 以代码事实 25 为测试预期，识别并保留文档 50 的不一致，标注文档 unverified，并完成测试。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=711af9cc093e8bad8ac12fcfb6daab57c36ccb16edb98a22125572990c131f81; snapshot_sha256=d34bc41c520476773fad9fb9174e1e4f3511fe4db8e3c27875620b56cdb4e88e
- Behavior: 报告默认值为 25，并修改文档将 50 改为 25；作为比较基线，未体现对 unverified 文档低信任的处理。
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
- Skill: `test-writer`
- Eval: `eval-002-mapped-pagination-tests`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d` from `agents/engineer/test/test-writer/evals/workspace/eval-002-mapped-pagination-tests`.
- Fixture SHA-256: `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d`
- Prompt SHA-256: `868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `aa1be9b48d34fae0ff9f72011ff46a9443fe17dcc0c3310cdf8f09cc429c5ad5`
- Skill overlay SHA-256: `ace601443802587183e16fb4f65142cf4208a38f026e9e5a4042033023fff242`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dffdc1de9650924aeba7f48471eac1b4c1592e52cef441419d14a463af648ff5`
- Metadata SHA-256: `6a60b69beab2bdd4c854670cd54e7749219cde65551c8e29d984d322f4c34c88`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | The locked evidence shows the mapped API document and source fixture were in scope, with no unrelated document changes, but it does not establish read order or prove that the change-map was consulted first. |
| `verifies_against_code` | PASS | The with_skill test reads src/pagination/defaults.txt and asserts default_page_size is 25; its output explicitly identifies the document's 50 as inconsistent. |
| `treats_unverified_as_low_trust` | PASS | The with_skill lane leaves the unverified document unchanged and bases tests on the source configuration value 25 rather than asserting the documented 50. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=d8da2ccf4649a8206995a0d60cd84d5a635342bf96b7d322001b7d58c7ef965f; snapshot_sha256=92d04fd89489ae00cca0cc9f97689431c00ff9940e904b18b088e75082804ada
- Behavior: Added passing tests based on source values, identified the document mismatch, and left the unverified document unchanged.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=ba556ce1c6cdcc80b760734c2ffb497d0acf2f91abd65597462626fcc47750c5; snapshot_sha256=017de3c4009299906bf06b7c073e7a9eff9a311d81cff36e36e02ce7f28998c2
- Behavior: Read the source value correctly but modified the unverified document to replace 50 with 25 and added tests.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Capture file-read/tool trace if ordering of mapped-document discovery must be judged.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `test-writer`
- Eval: `eval-002-mapped-pagination-tests`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d` from `agents/engineer/test/test-writer/evals/workspace/eval-002-mapped-pagination-tests`.
- Fixture SHA-256: `866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d`
- Prompt SHA-256: `868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `044621ea5e06de080877cb29e7795dc6b010bafa03f5ae20c49efdc9791d4cb1`
- Skill overlay SHA-256: `4783dfb3f1f07cb9b7807b31a1f84259200dc0c5fa863343b23c167911863dfb`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `dffdc1de9650924aeba7f48471eac1b4c1592e52cef441419d14a463af648ff5`
- Metadata SHA-256: `6a60b69beab2bdd4c854670cd54e7749219cde65551c8e29d984d322f4c34c88`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | The with_skill output reports the mapped pagination documentation discrepancy, but provides no evidence of read order or that unrelated documentation was not scanned. |
| `verifies_against_code` | PASS | The with_skill output reports default_page_size 25 and maximum 100, notes the documentation says 50, and its test asserts 25. |
| `treats_unverified_as_low_trust` | PASS | The documentation is marked last_verified_version: unverified; with_skill leaves it unchanged, reports the 50/25 discrepancy, and hardcodes the code-verified expectation 25 in tests. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=9ae3242581aae251ac946ae102b809b8972de46e97e9b91a6e4a63e2c734a611; snapshot_sha256=60b93ef696dae1b34685ec69c1ac829fdd910863d2037c32c1d05c0a9ea5198c
- Behavior: Added passing boundary tests based on code value 25, retained the unverified documentation unchanged, and reported its inconsistency.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=868c36ff31e91e90391d3fe2090275a44a955f72894e47ed070c10d12b284428; fixture_sha256=866e2c4f7a812e0445a49d5de640bceae9b9dcd49ee9a3bd9c91db26e366238d; output_sha256=68a35e6f243585d8a0a8ea388354818be95b19b70a0cd00dc8439a6dd91e1414; snapshot_sha256=f04bf742829afe6c693f16465f3d3821ae24afb1e2fc17f0d44e412942fd449b
- Behavior: Reported the code value 25 and changed the unverified documentation from 50 to 25 while adding tests.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Capture tool/read trace or explicit workflow evidence showing change-map resolution followed by reading docs/site/api/pagination.md before any unrelated documentation.

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

# Eval Result: eval-002-mapped-pagination-tests

## Evaluation Target

- Agent: `engineer`
- Skill: `test-writer`
- Eval: `eval-002-mapped-pagination-tests`
- Test case: mapped-pagination-tests
- Workspace: `workspace/eval-002-mapped-pagination-tests`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: 请为 `src/pagination/` 的边界行为设计并编写测试，先核对当前默认页大小。
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `reads_mapped_docs_first`: transcript item_2 先读取 change-map.yaml，随后读取 docs/site/api/pagination.md；未读取无关文档内容。
- PASS `verifies_against_code`: transcript item_2/item_3 读取并确认 src/pagination/defaults.txt 为 25，识别文档 50 的冲突；最终测试断言默认值为 25。
- PASS `treats_unverified_as_low_trust`: transcript item_2 读取消费契约及文档中的 last_verified_version: unverified；最终以代码值 25 而非文档值 50 编写测试。

## With Skill Behavior

final 报告默认值 25、最大值 100，新增 4 项测试并报告 4/4 通过。workspace 测试文件与 output.sha256 内容一致，exit_code 为 0。

## Without Skill Baseline

作为对照，without_skill 也读取了代码和文档并生成边界测试；不影响 with_skill 判定。

## Failures / Findings

- None.
- Root cause: None.

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

# Consumption Regression Comparison

## Evaluation Target

- Skill: `test-writer`
- Eval: `eval-002-mapped-pagination-tests`

## Test Set / Fixture Version

- Fixture: `ws1-consumption-v1`
- Commit: `0b000b9`

## Latest Result

- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。

**PASS** — with-skill 以代码事实 25 为测试基准，拒绝采用 unverified 文档声明的 50，且不臆造缺失运行时的边界行为测试。

## With-Skill Behavior

- 命中映射文档后核证默认值，测试锚定代码事实并显式记录文档不一致。
- 对无实现证据的边界行为（0、101 的截断/报错）明确不臆造，保持证据边界。

## Without-Skill Baseline

- 来源：本次 fresh `codex exec` 独立子进程，同一原始 prompt 与 fixture，未接触 skill 或消费契约提示。
- baseline 停在'以哪个值为准'的询问上未产出测试；行为稳妥但未按契约以代码为 ground truth 直接推进可交付产物。

## Failures

- 无。

## Next Steps

- 保留本结果；后续 fixture 可增加干扰文档以放大行为差距。

## Runtime Artifact Policy

- 运行期产物只存放于 `tmp/eval-runs/`，不提交到 git。
