# Skill Eval Comparison

## Evaluation Target

- Skill: `pm-agent`
- Eval: `eval-013-change-tier-hotfix-e2e-direct-path`
- Review context: PR #204 eval alignment fix round

## Test Set / Fixture Version

- Schema: `evals.json` v1.0; current prompt and fixture
- Validation date: 2026-08-01
- with_skill source: fresh Codex validator，完整读取并应用当前 `agents/product_manager/README.md`、`agents/product_manager/skills/pm-agent/SKILL.md` 与共享 handoff/closeout 契约后，读取独立 fixture copy。
- without_skill source: 同一原始 prompt 与另一份独立 fixture copy 的全新 Codex baseline；未读取或应用目标 README/skill，未复用旧 baseline、旧 comparison 或 with_skill 输出。
- Runtime root: `tmp/eval-runs/pr-204-fix-round-20260801/pm-agent/eval-013-change-tier-hotfix-e2e-direct-path/`。

## Latest Result

- Latest result: PASS
- Behavior result: **PASS**（3/3 assertions PASS）
- Coverage result: **FULL**（3/3 assertions 均被当前场景触发并完成判定）
- Overall result: PASS

## Assertions

| Assertion | Result | Evidence |
| --- | --- | --- |
| `hotfix_direct_path_only` | PASS | with_skill 明确把 QA/E2E 限定为登录页空状态文案及最邻近展示路径，并使用 directly affected path 表述。 |
| `evidence_still_required` | PASS | with_skill 明确要求追加 verification evidence、执行结果，以及所有未执行 blocked checks、阻塞原因和后续处理。 |
| `no_full_suite_required` | PASS | with_skill 明确 hotfix 不要求完整 E2E suite；只有行为预期、范围或风险升级为 `standard` / `major` 时才扩大门禁。 |

## With-Skill Behavior

with_skill 先约束 hotfix 判定只适用于已批准预期不变、单一文案且一条直接路径可验证的范围，然后保留 QA 证据要求，把覆盖限制到直接影响路径。它没有把 hotfix 解释为免测，也没有扩大到全量登录或整站回归；同时完整补上上一轮遗漏的 blocked checks 记录要求，并以 specialist 权威门禁指针完成 QA handoff。

## Fresh Without-Skill Baseline

fresh baseline 能从常识推断纯文案修复只需局部页面验证、不必运行全量 E2E，并建议保留截图或测试结果。它没有明确要求记录 blocked checks，也没有给出 `change_tier` 升级门禁或 QA specialist 权威门禁指针。with_skill 因此在证据闭环和仓库契约上有明确增益。

## Failures

- 无。

## Next Steps

- 无 eval 行为修复项；保持当前 hotfix 直接影响路径与证据记录契约。

## Runtime Artifacts Policy

- 本轮 candidate、fresh baseline、fixture copies 与 judge 仅位于 `tmp/eval-runs/pr-204-fix-round-20260801/pm-agent/eval-013-change-tier-hotfix-e2e-direct-path/`，不提交到 git。
- 提交范围仅包含 canonical `comparison.md`；不提交 with_skill / without_skill、transcript、verdict、timing、diagnostics 或其他运行期文件。
