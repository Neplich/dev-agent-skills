# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator`
- Eval: `eval-001-generate-site-release-notes`
- Review context: issue #150

## Test Set / Fixture Version

- Fixture version: `issue-150 fresh-paired group-b v1`
- Actual validation date: `2026-07-21`
- Fresh run: `tmp/eval-runs/issue-150/group-b/eval-001-generate-site-release-notes/`
- Both lanes started from independent copies of the same pristine fixture.

## Latest Result

**PASS（with-skill 5/5；fresh without-skill 5/5）** — with-skill 完整保留六类发布证据，应用七字段 release frontmatter，先候选回读再应用确认并更新派生面，真实通过宿主检查后输出字段完整的 #117 pre-tag ready handoff。fresh baseline 也通过全部 assertions，本用例未显示相对 uplift。

## Assertions

- `preserves_six_evidence_categories`: PASS。用户功能、架构、数据库迁移、部署配置、交付资产、升级兼容与风险均保留关键事实和来源。
- `uses_release_frontmatter_contract`: PASS。七字段完整，`doc_type: release`，owners/related_code 非空，`last_verified_version: unverified`。
- `enforces_confirmation_before_derived_writes`: PASS。候选页先生成、展示并回读，之后才应用 `confirmation-record.md`；确认后更新 index/metadata，navigation 由宿主脚本生成且未手工改 sidebar。
- `runs_real_host_docs_checks`: PASS。在 `docs/site` 执行 `npm ci --ignore-scripts` 和 `RELEASE_VERSION=v1.0.0 npm run test:docs`，退出 0、75/75 tests。
- `returns_complete_ready_handoff`: PASS。版本确认、正文确认和宿主检查三门禁满足后才 ready；handoff 包含 downstream/next gate、授权 false、确认来源、path、checks、surfaces、evidence 与 blockers。

## With-Skill Behavior

- 保留 `.meta/releases.json` 的未知 `manualNote` 与旧版本，按宿主排序追加 v1.0.0。
- 页面保持 `unverified`，等待 #117 统一盖章；#120 仅是 downstream owner，未执行 tag、GitHub Release 或部署。

## Fresh Without-Skill Baseline

- 来源：同一 prompt/assertions 与独立 pristine fixture 的本轮 fresh `without_skill`；生成期间未读取目标 SKILL、Docs README、internal/shared 指令、旧 comparison 或历史输出。
- baseline 也生成证据完整页面、保持 `unverified`、在明确确认后更新 index/metadata，并通过 75 tests；其响应包含规定 ready handoff 字段和外部发布边界。
- 结果：5/5 PASS；未复用历史 baseline。

## Failures

- With-skill assertion failures: none。
- Without-skill assertion failures: none。
- Comparative limitation: fixture 的 Release Notes README、六份 evidence、confirmation record 与 assertions 已充分显式化正确执行顺序和输出字段。

## Next Steps

- 保持 `unverified`、确认后派生写入与完整 #117 handoff 回归。
- 如需测 uplift，增加证据冲突、缺失类别或 host metadata 未知字段的阻塞/保留型 case。

## Runtime Artifact Policy

- 页面副本、依赖、响应与检查日志仅位于 `tmp/eval-runs/issue-150/group-b/eval-001-generate-site-release-notes/`，不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
