# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-005-audit-doc-only-error`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a` from `agents/docs/test/docs-audit/evals/workspace/eval-005-audit-doc-only-error`.
- Fixture SHA-256: `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a`
- Prompt SHA-256: `59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `d804d7eed6dff47b2c8744abfb057fce66d8fde2359e03e7f21e978c34808373`
- Eval definition SHA-256: `1f7d058864bf71ce0402d8ada31c06c85782a25b93779e842d80b5a98766c9d9`
- Metadata SHA-256: `63b77017b252b389a44397720be8380b6bee7f6a85225c5d210accca792fc487`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_doc_only_change` | PASS | with_skill 将 docs/site/api/catalog.md 列为变更文件并纳入影响范围；fixture 的实际补丁也证明范围仅含该文档。 |
| `uses_related_code_for_fact_check` | PASS | with_skill 明确检查 src/catalog/routes.txt，并指出其仅提供 GET /catalog/items，没有因无代码 diff 而跳过事实核验。 |
| `classifies_doc_only_conflict_mismatch` | PASS | with_skill 保留 DELETE 声明、routes.txt 中仅有 GET 的事实及文件证据，并将文档判为 mismatch。 |
| `blocks_despite_no_code_diff` | PASS | with_skill 的 pre-tag 结果为 blocked，明确不加版本戳、不写入审计报告且不返回 ready_for_tag；其 git 证据显示无代码 diff。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=d906ce89e2a0efc833a433ed554a2cf90396bff6492a3cd4144d985c53ccde84; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别纯文档变更，使用相关路由事实核对发现 DELETE 文档与代码不一致，并在 pre-tag 阶段阻塞。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=d9309d1f16dcee6a17d035bcd2c92f96306ff0f35cc2a2d8c1f0478b3b821ce8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了文档与路由不一致，但加入了与目标断言无关或未由 fixture 支持的额外发现，未形成同等明确的 pre-tag 阻塞结果。
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
- Eval: `eval-005-audit-doc-only-error`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a` from `agents/docs/test/docs-audit/evals/workspace/eval-005-audit-doc-only-error`.
- Fixture SHA-256: `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a`
- Prompt SHA-256: `59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `a40b9426c3ece6f787614183ce8478f0aacaf94802441ebb84796853c2c8848e`
- Skill overlay SHA-256: `6cbf5a99cea4bf2bfd3e91f9b1e261a828b8b62ab73699f7ed3de43f33d01739`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `1f7d058864bf71ce0402d8ada31c06c85782a25b93779e842d80b5a98766c9d9`
- Metadata SHA-256: `63b77017b252b389a44397720be8380b6bee7f6a85225c5d210accca792fc487`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_doc_only_change` | PASS | with_skill 明确列出 docs/site/api/catalog.md 为变更文件和受影响页面，并注明无代码映射命中、无 map delta，仍将该文档纳入影响范围。 |
| `uses_related_code_for_fact_check` | PASS | with_skill 使用 src/catalog/routes.txt 核验 GET 路由及 DELETE 缺失事实，未因无代码 diff 而跳过事实核验。 |
| `classifies_doc_only_conflict_mismatch` | PASS | with_skill 保留了 DELETE 声明、代码仅有 GET 的事实、routes.txt 证据路径，并将 DELETE 判为 mismatch，同时说明其导致阻塞。 |
| `blocks_despite_no_code_diff` | PASS | with_skill 明确给出 pre-tag 结果 blocked，说明未创建报告、stamp 或提交，并要求修正文档后重新审计，未返回 ready_for_tag。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=e13b7da0eba1f09784191da0e6dd2980c6582e08646d96ee34bba0032b1ba04c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 将纯文档变更纳入影响域，按相关代码核验事实，识别 DELETE mismatch，并在 pre-tag 阶段阻塞且不盖章。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=e36ca6c347da50fbc674db8084209ddfa129193229c3621960b99c21fd5ed3e5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别出文档声明的 DELETE 路由与 routes.txt 不一致并建议暂不批准；未明确展示影响域和 related_code 的审计机制。
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
- Eval: `eval-005-audit-doc-only-error`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a` from `agents/docs/test/docs-audit/evals/workspace/eval-005-audit-doc-only-error`.
- Fixture SHA-256: `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a`
- Prompt SHA-256: `59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `d339a8370a29b3fb2a69aa1879b1226165ec088d306a4e2e7a01258df2326973`
- Skill overlay SHA-256: `0bc7243cbb5cff3e77d9ba448e020a1a1f279639f8db6a365faac208b8e1dcc7`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `1f7d058864bf71ce0402d8ada31c06c85782a25b93779e842d80b5a98766c9d9`
- Metadata SHA-256: `63b77017b252b389a44397720be8380b6bee7f6a85225c5d210accca792fc487`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_doc_only_change` | PASS | with_skill 明确说明仅有文档变更，并依据 documentation-only 规则将 catalog.md 纳入影响集。 |
| `uses_related_code_for_fact_check` | PASS | with_skill 明确核对目标提交中的 src/catalog/routes.txt，确认其仅定义 GET 路由，未因无代码 diff 而跳过事实核验。 |
| `classifies_doc_only_conflict_mismatch` | PASS | with_skill 保留 DELETE 声明，指出 routes.txt 无对应 DELETE 路由，并将结论标为 mismatch，说明该事实冲突构成阻塞。 |
| `blocks_despite_no_code_diff` | PASS | with_skill 给出 pre-tag 结果 blocked，明确不可返回 ready_for_tag，并说明未执行 stamp。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=1c247933d0ccdabace9d885ed54c497ca24e31aeb13c4ec2c1fa488b67890b37; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 明确应用文档-only 影响规则、按 related_code 核对代码事实，并在 pre-tag 阶段以 mismatch 阻塞且不盖章。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=044ea497eb0236b88a40a03848dd6d4dc30a879baee4ed8728e5e4f73a2b2484; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别文档-only 变更、DELETE 文档与代码事实冲突，并判定发布不通过。
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
- Eval: `eval-005-audit-doc-only-error`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a` from `agents/docs/test/docs-audit/evals/workspace/eval-005-audit-doc-only-error`.
- Fixture SHA-256: `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a`
- Prompt SHA-256: `59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9e9abf391c9ccd9564d35b5def50bc0374b1db0886710676c4d48422839746ae`
- Skill overlay SHA-256: `c66ac938bf9158faa694d7c3e311e913ddc4a06da11de703a881234f257c470c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `1f7d058864bf71ce0402d8ada31c06c85782a25b93779e842d80b5a98766c9d9`
- Metadata SHA-256: `63b77017b252b389a44397720be8380b6bee7f6a85225c5d210accca792fc487`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_doc_only_change` | NOT_EXERCISED | With-skill output states there was no code-file hit and identifies the page's related_code, but locked evidence does not prove the hidden deterministic impact-domain operation. |
| `uses_related_code_for_fact_check` | PASS | Output explicitly identifies related_code as src/catalog/routes.txt and compares it with the documented DELETE route. |
| `classifies_doc_only_conflict_mismatch` | PASS | Output preserves the DELETE declaration, reports routes.txt only defines GET, and classifies the page conclusion as mismatch. |
| `blocks_despite_no_code_diff` | PASS | Output explicitly reports pre-tag blocked, explains why the mismatch prevents release stamping, and does not return ready_for_tag. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=10812fcaf53f01ca04a14798db8ef52e4e390b0a8a2a37ed39443fcd5240fbf8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identifies the documentation-only scope, uses related_code to inspect the route fixture, classifies the conflict as mismatch, and blocks pre-tag release.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=cac290a8e81349fdeee10a7627703df06afa85a670f7cdc3836cfd160b0aa8a5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Detected the undocumented DELETE route and recommended failing the audit, but did not explicitly demonstrate the required related_code-based audit workflow.
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
- Eval: `eval-005-audit-doc-only-error`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a` from `agents/docs/test/docs-audit/evals/workspace/eval-005-audit-doc-only-error`.
- Fixture SHA-256: `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a`
- Prompt SHA-256: `59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2d24da5f976a5ab2710c2c072a19015e074d314e0ebdb88f1c28831425f1b98c`
- Skill overlay SHA-256: `40330c17a3b77f25a1b1a716fa5e9355e0011db79d19014344ed516affba11c8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `1f7d058864bf71ce0402d8ada31c06c85782a25b93779e842d80b5a98766c9d9`
- Metadata SHA-256: `63b77017b252b389a44397720be8380b6bee7f6a85225c5d210accca792fc487`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_doc_only_change` | PASS | with_skill 明确识别范围内仅修改 docs/site/api/catalog.md，并将该页面纳入影响审计。 |
| `uses_related_code_for_fact_check` | PASS | with_skill 使用页面 related_code 指向 src/catalog/routes.txt，并核对其仅定义 GET /catalog/items。 |
| `classifies_doc_only_conflict_mismatch` | PASS | with_skill 保留 DELETE 声明、routes.txt 事实及链接证据，说明页面声明与实现不符并判定为 mismatch。 |
| `blocks_despite_no_code_diff` | PASS | with_skill 给出 pre-tag blocked 结果，明确未执行版本戳更新或写入审计报告/handoff，未返回 ready_for_tag。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=8601ae924b52b3515f4630064e63f20cdedf4b640cdd79adffe36bd5bbccd3f7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别纯文档影响域，按 related_code 核对代码事实，将冲突判为 mismatch，并在 pre-tag 阶段阻塞。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=33850094c6e8360a2761946bdb046a27b09cb926dfa1d0e2e9280d19fd916f59; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别文档变更、核对 related_code 并发现 DELETE 不一致，结论为不通过；同时提出额外元数据和证据问题。
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
- Eval: `eval-005-audit-doc-only-error`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a` from `agents/docs/test/docs-audit/evals/workspace/eval-005-audit-doc-only-error`.
- Fixture SHA-256: `126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a`
- Prompt SHA-256: `59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `1f7d058864bf71ce0402d8ada31c06c85782a25b93779e842d80b5a98766c9d9`
- Metadata SHA-256: `63b77017b252b389a44397720be8380b6bee7f6a85225c5d210accca792fc487`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_doc_only_change` | PASS | with_skill 明确说明仅变更 docs/site/api/catalog.md，且文档因直接变更进入影响集。 |
| `uses_related_code_for_fact_check` | PASS | with_skill 明确核对页面 related_code 指向的 src/catalog/routes.txt，并以其作为实现证据。 |
| `classifies_doc_only_conflict_mismatch` | PASS | with_skill 保留 DELETE 声明、routes.txt 中仅有 GET 的事实及链接证据，并将文档结论判为 mismatch；同时说明该问题导致阻塞。 |
| `blocks_despite_no_code_diff` | PASS | with_skill 明确给出 pre-tag 结果 blocked、不能返回 ready_for_tag，并说明无代码变更不能放行错误文档。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=ca56c52d4b9298f1f3c69690cd0e7bdd90d238630dff7f4f7841f0d727a4007b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 将纯文档变更纳入影响集，按 related_code 核对代码事实，判定 mismatch，并在 pre-tag 阶段阻塞且不返回 ready_for_tag。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=4fc431d93686f31acee125c7e0d84158c0fac6ee62dfe3dc2f1919e328a0cf59; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别出文档声明与代码事实不一致，但未明确执行文档直接入影响域、related_code 核验或 mismatch/blocked 状态机结论。
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
- Eval: `eval-005-audit-doc-only-error`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9e142741ede740512aa29803d0f099c9ace27e7cbb6e032e6e183f63e2548c88` from `agents/docs/test/docs-audit/evals/workspace/eval-005-audit-doc-only-error`.
- Fixture SHA-256: `9e142741ede740512aa29803d0f099c9ace27e7cbb6e032e6e183f63e2548c88`
- Prompt SHA-256: `59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `1f7d058864bf71ce0402d8ada31c06c85782a25b93779e842d80b5a98766c9d9`
- Metadata SHA-256: `63b77017b252b389a44397720be8380b6bee7f6a85225c5d210accca792fc487`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_doc_only_change` | PASS | with_skill 明确指出仅有 docs/site/api/catalog.md 变更，并将文档页因正式 Markdown 变更直接纳入审计。 |
| `uses_related_code_for_fact_check` | PASS | with_skill 使用页面 related_code 指向的 src/catalog/routes.txt 作为实现证据，并核对其内容。 |
| `classifies_doc_only_conflict_mismatch` | PASS | with_skill 对 DELETE 声明与仅存在 GET 路由的事实进行对照，保留声明、证据和影响，并判定为 mismatch。 |
| `blocks_despite_no_code_diff` | PASS | with_skill 结果为 pre-tag blocked，明确阻止版本盖章，且未返回 ready_for_tag。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=9e142741ede740512aa29803d0f099c9ace27e7cbb6e032e6e183f63e2548c88; output_sha256=7475ffe9a754ea2b5801c1363a1248fe85380f648a0da62c4ef05fcb44769f81; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 将纯文档变更纳入审计，沿 related_code 核对实现事实，判定文档为 mismatch，并以 pre-tag blocked 阻止盖章。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=9e142741ede740512aa29803d0f099c9ace27e7cbb6e032e6e183f63e2548c88; output_sha256=5153248f6792319af54c45293977165796b44e3a6d3bb2c7e30473ad19b28654; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别出 DELETE 文档声明与代码事实不一致并判定审计不通过，但未明确说明文档变更直接进入影响域、related_code 核对机制或 blocked/pre-tag 状态。
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
- Eval: `eval-005-audit-doc-only-error`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `82ed7f212fd01d51033deeb08f3150e86fc18a56d4d92cc340644b053d415625` from `agents/docs/test/docs-audit/evals/workspace/eval-005-audit-doc-only-error`.
- Fixture SHA-256: `82ed7f212fd01d51033deeb08f3150e86fc18a56d4d92cc340644b053d415625`
- Prompt SHA-256: `59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `1f7d058864bf71ce0402d8ada31c06c85782a25b93779e842d80b5a98766c9d9`
- Metadata SHA-256: `63b77017b252b389a44397720be8380b6bee7f6a85225c5d210accca792fc487`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_doc_only_change` | PASS | with_skill identifies docs/site/api/catalog.md as affected despite no code match or change-map change. |
| `uses_related_code_for_fact_check` | PASS | with_skill checks src/catalog/routes.txt and finds only GET, while the changed file is documentation. |
| `classifies_doc_only_conflict_mismatch` | PASS | with_skill preserves the DELETE declaration, GET-only code fact, routes.txt evidence, and blocking impact, explicitly classifying the page as mismatch. |
| `blocks_despite_no_code_diff` | PASS | with_skill reports the pre-tag result as blocked, leaves version stamps unchanged, and explicitly does not return ready_for_tag. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=82ed7f212fd01d51033deeb08f3150e86fc18a56d4d92cc340644b053d415625; output_sha256=1b60f7aa98345e2509f566ec38545d43ca09eaa67c90c2d943f48fdc11143c7d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Audits the documentation-only change, follows related_code to the route fixture, classifies the conflict as mismatch, and blocks pre-tag release.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=82ed7f212fd01d51033deeb08f3150e86fc18a56d4d92cc340644b053d415625; output_sha256=d465d74d74cb973bfff0b46e928a0053256cf739dddd0d32586d71692e0ab640; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Fresh baseline detects the documentation/code mismatch and advises against approval, but does not provide the with_skill lane’s explicit pre-tag blocked result.
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

# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-005-audit-doc-only-error`

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
| `includes_doc_only_change` | PASS | FAIL | with_skill 明确写出“变更文件：`docs/site/api/catalog.md`”“影响文档：`docs/site/api/catalog.md`”；without_skill 仅说明实际差异仅修改该文件，未明确将其加入影响域。 |
| `uses_related_code_for_fact_check` | PASS | PASS | 两条 lane 均核对 `src/catalog/routes.txt`，并指出该文件仅定义 `GET /catalog/items`、没有 DELETE；没有因无代码 diff 跳过核验。 |
| `classifies_doc_only_conflict_mismatch` | PASS | FAIL | with_skill 保留 DELETE 文档声明、代码事实、证据和影响，并明确判定为 `mismatch`；without_skill 描述了冲突，但未给出 `mismatch` 分类。 |
| `blocks_despite_no_code_diff` | PASS | FAIL | with_skill 明确结论为 `blocked`、不能进入 `ready_for_tag`，且未盖章；without_skill 仅称“不通过（需修复）”，未明确阻塞或禁止 `ready_for_tag`。 |

未满足断言（with/without 任一 FAIL）：``includes_doc_only_change``、``classifies_doc_only_conflict_mismatch``、``blocks_despite_no_code_diff``



## Assertion Results
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

| Assertion | Result | Evidence summary |
| --- | --- | --- |
| `includes_doc_only_change` | PASS | `catalog.md` 即使没有代码 diff 或 change-map 命中也直接进入影响域。 |
| `uses_related_code_for_fact_check` | PASS | 事实层按页面 `related_code` 核对 `src/catalog/routes.txt`。 |
| `classifies_doc_only_conflict_mismatch` | PASS | 文档 DELETE/204 与代码仅有 GET 的事实、证据和影响均保留，结论 `mismatch`。 |
| `blocks_despite_no_code_diff` | PASS | 结果 `blocked`，页面保持 `v1.0.0`，没有因无代码 diff 放行或盖章。 |

## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮 fresh session `019f7a75-30f1-7de1-9565-f18800886463`，位于 `tmp/eval-runs/117/eval-005-audit-doc-only-error/with_skill/`。
- 候选只新增契约路径报告，不修复页面或生成 release metadata。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 来源：本轮独立 fresh session `019f7a78-ed50-7d13-aa25-55b5c7407307`，同一 prompt 与 pristine fixture；未复用历史 baseline。
- baseline 同样识别 DELETE 冲突并阻塞，但报告写入 `.eval/pre-tag-audit-report.md`，影响域与协议边界证据较简略。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 无 assertion failure。合成 refs 使用 `.eval/actual-diff.patch`，属于 harness 限制，不是协议缺陷。

## Next Steps

- 保留本结果；文档-only 影响域规则变化时重跑。

## Runtime Artifact Policy

- 本轮运行期证据仅位于 `tmp/eval-runs/117/`，不提交；durable 产物仅为本 `comparison.md`。
