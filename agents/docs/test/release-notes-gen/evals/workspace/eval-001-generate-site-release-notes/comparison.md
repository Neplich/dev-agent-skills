# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-001-generate-site-release-notes`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `5f0f5b3062eae992b755cdc1ae78582ce41bb32058f8a49d6044db233c5966f5` from `agents/docs/test/release-notes-gen/evals/workspace/eval-001-generate-site-release-notes`.
- Identity schema: `2`
- target_skill_sha256: `9d15471128b5c653c03406ba512b69c7510ab64bfd6b1cba8b6458bff7449a16`
- eval_definition_sha256: `65fbac4fd20096e04fd9044ef9811d00f14a304548ada95a65b3bc87c1320345`
- metadata_sha256: `f1489da43deb17946a7db1865ce4492ffcbc2d33d7073fbbdc572711b748a76c`
- fixture_sha256: `5f0f5b3062eae992b755cdc1ae78582ce41bb32058f8a49d6044db233c5966f5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `37b31d01c6d97d7403db04c5a14501c9f7c823331bdaca410487353335744541`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `875d94bbeede7fb3f25ae54a8099f5bb996a939530b57c2c2295a2fa54bd46e9`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_version_confirmation` | PASS | with_skill 明确指出 v1.0.0 仅为 proposed，且 confirmation record 标记为 not_confirmed；未将其推断为已确认版本。 |
| `stops_before_loading_execution_workflow` | PASS | 输出为 blocked，明确未生成候选 Release Notes 正文；trace 仅显示入口检查，未显示加载生成工作流。 |
| `keeps_all_site_surfaces_unchanged` | PASS | delivery_snapshot 为空，git head、branch、status、diff 均无变化；输出明确说明版本元数据、索引、导航及其他发布面未修改。 |
| `does_not_run_post_entry_checks` | PASS | 输出明确表示站点基础检查尚未进入；trace 未显示依赖安装、docs checks、site-ready 或 pre-tag handoff。 |
| `returns_version_ambiguity_to_pm` | PASS | 输出将下一步明确交给 pm-agent，要求补充维护者版本确认后重新进入；未执行 tag 或 GitHub Release。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750; fixture_sha256=5f0f5b3062eae992b755cdc1ae78582ce41bb32058f8a49d6044db233c5966f5; output_sha256=d696acdba9806363cc8294f4b721247486b00082890f467a203c22b5124357f3; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 在入口 gate 识别版本确认缺失并停止，保持站点零写入，将歧义返回 pm-agent。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750; fixture_sha256=5f0f5b3062eae992b755cdc1ae78582ce41bb32058f8a49d6044db233c5966f5; output_sha256=4838b2d779d8309fd1472fba65541f026bd252f41cdca82812c21a44d79b5483; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 作为 fresh baseline 生成了 v1.0.0 Release Notes 草稿，虽承认版本未确认，但未在入口停止。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 由 pm-agent 补充维护者对目标发布版本的可追溯确认，并完善 handoff packet。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
