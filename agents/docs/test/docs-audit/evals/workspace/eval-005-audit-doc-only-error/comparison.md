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
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b5823d2c0804ce3dabb1d32490f71697f4ff111cd9371ebf92d1bb1b6ad2188`
- Skill overlay SHA-256: `c7033e85898ff61111eb14edc47b25e717119ee79349d7af461390afc706db78`
- Judge schema SHA-256: `d804d7eed6dff47b2c8744abfb057fce66d8fde2359e03e7f21e978c34808373`
- Eval definition SHA-256: `1f7d058864bf71ce0402d8ada31c06c85782a25b93779e842d80b5a98766c9d9`
- Metadata SHA-256: `63b77017b252b389a44397720be8380b6bee7f6a85225c5d210accca792fc487`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `includes_doc_only_change` | PASS | with_skill 报告列出变更文件 `docs/site/api/catalog.md`、受影响正式页面，并明确纯文档页仍进入事实复核；raw trace 也记录了直接变更正式 API 页必须复核。 |
| `uses_related_code_for_fact_check` | PASS | 报告明确读取页面 `related_code` 指向的 `src/catalog/routes.txt`，并以其仅有 GET 路由作为代码事实。 |
| `classifies_doc_only_conflict_mismatch` | PASS | 报告保留 DELETE 声明、代码仅有 GET 的事实、相关路径证据及阻断影响，并将页面判为 `mismatch`。 |
| `blocks_despite_no_code_diff` | PASS | 报告明确阶段为 `pre-tag`、结果为 `blocked`，且不能盖章、不能创建候选记录或 handoff。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=c07c751dd5c087f891979bdc2aff217db34c536d207583b24e55865fa9696da0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别纯文档变更，按 related_code 核对代码事实，将冲突判为 mismatch，并在 pre-tag 阶段阻塞。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59ccd7c8df4ada989871eac608af9fe615691e1a2d925c63deac93d4d7d56264; fixture_sha256=126b82b218c4429d9a8e50c428008903893e0b48fd89e0ee4186368ab968404a; output_sha256=5b21fac3d88bda1ebf6a9944f4c7e2dcb898f4b97a96561e83acf4ccb6bd1e1b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样识别文档与代码冲突并给出不通过结论，但未提供结构化审计阶段结果。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
