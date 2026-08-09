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
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
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
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
