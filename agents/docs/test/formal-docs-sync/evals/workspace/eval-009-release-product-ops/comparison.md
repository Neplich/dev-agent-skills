# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-009-release-product-ops`
- Review context: issue #150

## Test Set / Fixture Version

- Fixture version: `issue-150 fresh-paired group-b v1`
- Actual validation date: `2026-07-21`
- Fresh run: `tmp/eval-runs/issue-150/group-b/eval-009-release-product-ops/`
- Both lanes started from independent copies of the same pristine fixture.

## Latest Result

**PASS（with-skill 5/5；fresh without-skill 5/5）** — with-skill 仅同步 v1.5.0 受影响的 product/ops 页面，既有两个 change-map entries 保持准确，Release Notes surfaces 零变化，两页保持 `unverified`，并在真实宿主检查通过后向 #117 输出维护者确认版本 handoff。fresh baseline 也满足全部 assertions，因此本用例证明协议可执行，但未显示相对 uplift。

## Assertions

- `limits_release_to_affected_product_ops`: PASS。只修改 `product/dashboard-limits.md` 与 `ops/dashboard-runtime.md`；对应两个既有映射已准确，无 API、database、design 或无关页面扩张。
- `reconciles_confirmed_version_facts`: PASS。代码、配置和 release tests 共同证明上限 25、镜像 `registry.example/ai-hub:v1.5.0`，并排除 10、v1.4.0 与未确认 v1.5.1。
- `preserves_release_notes_surfaces`: PASS。Release Notes 正文、index、metadata、navigation 与 pristine fixture 字节一致，并明确指向 `docs-agent:release-notes-generator` #116。
- `keeps_release_pages_unverified`: PASS。两页均回读为 `last_verified_version: unverified`。
- `runs_release_host_checks_and_handoffs`: PASS。在 `docs/site` 执行 `RELEASE_VERSION=v1.4.0 npm run test:docs`，退出 0、74/74 tests；handoff 包含完整 affected set、`target_release_version: v1.5.0` 与 `release-handoff.md` 维护者确认来源。

## With-Skill Behavior

- 读取公共八步 contract 及 product/ops 两个类型模块；未加载无关类型模块。
- 先使用 lockfile 执行 `npm ci --ignore-scripts`，再运行宿主检查；版本参数只用于校验当前未改动 release metadata，不用 Git ref 推测目标版本。
- 不操作 Release Notes、tag、GitHub Release 或部署。

## Fresh Without-Skill Baseline

- 来源：同一 prompt/assertions 与独立 pristine fixture 的本轮 fresh `without_skill`；在生成期间未读取目标 SKILL、Docs README、internal/shared 指令、旧 comparison 或历史输出。
- baseline 也只更新两页、保留准确映射和 Release Notes 零变化，页面保持 `unverified`，并真实通过相同 74 tests；其结构化响应包含 #117 affected set、维护者确认来源与 #116 边界。
- 结果：5/5 PASS；未复用历史 baseline。

## Failures

- With-skill assertion failures: none。
- Without-skill assertion failures: none。
- Comparative limitation: prompt/assertions 与 fixture 已充分显式给出范围、版本事实和 handoff 字段，fresh baseline 也能完整执行。

## Next Steps

- 保持 release mode 的 product/ops 窄范围、Release Notes 零写入、`unverified` 和明确版本确认来源作为回归门禁。
- 如需衡量 uplift，另增缺失或冲突 release evidence 的阻塞型 eval。

## Runtime Artifact Policy

- 两 lane workspace、依赖、页面副本、响应与测试日志仅位于 `tmp/eval-runs/issue-150/group-b/eval-009-release-product-ops/`，不提交。
- 本 `comparison.md` 是唯一 durable eval 结果。
