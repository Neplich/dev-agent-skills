# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-agent`
- Eval: `eval-005-integration-release-chain`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3` from `agents/docs/test/docs-agent/evals/workspace/eval-005-integration-release-chain`.
- Fixture SHA-256: `69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3`
- Prompt SHA-256: `62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e`
- Repository HEAD: `f34c1007244dc48cf04fcd5d073fc5949225f1bd`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `cf92649952a97be677cf5e900a4d9c793a6c0724813cf1fa3154f57e7d2c08f3`
- Skill overlay SHA-256: `ae0e9f3dff3c62a65c453e0c23d5576ecdece8af2d0329b54155f9542b7cb272`
- Judge schema SHA-256: `1f2ea17b811fce39b8e906ef0e0a70b6a6223a188a2f4a05f2f0a88c54c6aceb`
- Eval definition SHA-256: `05d8b9eb5ccf6bbc077dad850c79899562c5b4ed9bbb4187abffd82f21410ea3`
- Metadata SHA-256: `af301306a3e584e9c32987cd73e02ac298dcd98f38208af58ca0764e8b5a4154`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_release_audit_entry` | PASS | 保留 v1.4.0、ai-search 范围、维护者确认、证据来源及只读执行边界，并接受入口材料作为 docs-audit 路由基础。 |
| `evaluates_site_release_notes_gate` | PASS | 识别 handoff 的 confirmed 状态、主机检查、支持证据、更新面和外部执行边界，同时指出 unverified 页面及缺失审计凭据，未将 ready 自称视为 GitHub Release 放行。 |
| `validates_release_window_basis` | PASS | 明确核对 previous_tag/base_ref 均解析到 041b91a5，并核对 target_ref/tag-entry 为 5dc0861b；未猜测或替代锚点。 |
| `rejects_missing_pre_tag_authority` | PASS | 明确指出没有 bound pre-tag audit inventory/authority，未宣称 pre-tag 已通过。 |
| `detects_post_tag_evidence_drift` | PASS | 根据签认快照指出 release-candidate/tag-entry 树为 7c8b9b，而 v1.4.0 tag 树为 490d0b，判定 post-tag 验证受阻。 |
| `blocks_github_release_handoff` | PASS | 明确结论为不能进入 GitHub Release 准备或发布阶段，未生成 preview、draft 或 publish handoff，并将后续交给 docs-audit。 |
| `preserves_no_mutation_boundaries` | PASS | 候选输出声明未执行 tag/GitHub Release 写入；锁定 git_evidence 显示 HEAD、分支、refs、索引和工作树均未变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=81a972762542f11c5ed48be91f086675bff3cfdedcd05ca6d39591472e46db95; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确接受发布审计入口，核验版本窗口，识别缺失 pre-tag 权威及 post-tag 树漂移，阻断 GitHub Release，并保持只读边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=62a386a246bcb0c7c5b2df7096cfd60c5023a6b28473d50af8f99649d1d3480e; fixture_sha256=69659db940208abe97ba4ab195a49c736d9a7ba7e1e880c287d3bf12132c10a3; output_sha256=b55b049277b1eed0d1b3385034a109575c054258f0314aa851321bb7af41afe3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样识别主要发布阻塞和只读边界，但作为 fresh baseline comparison context，未用于否定 with_skill assertions。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
