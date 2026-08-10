# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-008-pre-tag-success`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f` from `agents/docs/test/docs-audit/evals/workspace/eval-008-pre-tag-success`.
- Fixture SHA-256: `188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f`
- Prompt SHA-256: `c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b5823d2c0804ce3dabb1d32490f71697f4ff111cd9371ebf92d1bb1b6ad2188`
- Skill overlay SHA-256: `c7033e85898ff61111eb14edc47b25e717119ee79349d7af461390afc706db78`
- Judge schema SHA-256: `4cd14ef8cd033d31b5bb9ce50a786ad0b7d18c7ff4f682d88505eac53b634ecf`
- Eval definition SHA-256: `4d1aa7f3a07c406f7e925f931c91ea28170bd7650629aa75bcd06b4f58bba0c7`
- Metadata SHA-256: `6adbc51a2dc07674edf9fca71addc72bccaccf75ae663c41fbf3725d8c48b107`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `accepts_confirmed_version_without_tag` | PASS | 输出明确记录了 base_ref、target_ref、维护者确认的 v1.2.0，并说明同名 tag 不存在但符合 pre-tag；阻断原因是受影响路径的工作区漂移。 |
| `verifies_complete_set_and_surfaces` | NOT_EXERCISED | 锁定 trace 显示其识别了 change-map 的两张 API 页面及两张 Release Notes 页面，并读取了 handoff、版本元数据和 package.json；但在完成逐页 verified 结论前因工作区污染阻断。 |
| `normalizes_mixed_version_forms` | PASS | 输出明确说明 package.json 使用 1.2.0，Release Notes 和 releases.json 使用 v1.2.0，并归一化为同一 SemVer。 |
| `records_pre_stamp_values` | NOT_EXERCISED | 读取了 fixture 中的盖章前值，但未生成审计报告或进入可写盖章阶段。 |
| `stamps_complete_set_atomically` | NOT_EXERCISED | 候选输出明确表示未修改任何版本戳；统一盖章尚未执行。 |
| `builds_isolated_candidate_transaction` | NOT_EXERCISED | 未创建隔离 candidate worktree/branch 或 candidate 事务；流程在受影响路径存在未提交修改时阻断。 |
| `candidate_record_has_no_ready_result` | NOT_EXERCISED | 未产生 candidate record。 |
| `validates_two_complete_staged_gates` | NOT_EXERCISED | 未执行 candidate staged gate 或最终 candidate staged gate。 |
| `confirms_anchor_commit_before_discovery` | NOT_EXERCISED | 未创建或确认 post-stamp anchor commit。 |
| `persists_fixed_discovery_handoff` | NOT_EXERCISED | 未写入固定 discovery handoff；输出明确说明未创建 handoff。 |
| `returns_ready_only_after_integration` | NOT_EXERCISED | 未进行候选集成、handoff 回读或向下游返回 ready_for_tag。 |
| `returns_ready_for_tag_not_published` | NOT_EXERCISED | 输出返回 blocked，而非 ready_for_tag；由于受影响工作区存在未提交修改，成功阶段尚未到达。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=63718550d362a3d29cceb892973dd72a2a5c4f5d427588da56975d2f4b0cd21a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确锁定 pre-tag 输入，识别缺失 tag 不应阻断，并在检测到受影响路径工作区漂移后安全阻断且不执行写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c716eb0f2d2753ceb3a2258e2367701a57faeef420e346b4fa18dc3a1677c0e3; fixture_sha256=188f1d4d85d9c539fa3ce7acd636673ee316e8a8c7f692533cb806966484f84f; output_sha256=b3fc38eae644997440b021a5d3014bcb2e034cc0a59e5661e61de62a31afc80f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 新鲜基线仅进行浅层只读审计，错误地将 releases.json 发布状态视为主要问题，未执行完整 docs-audit 事务。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 维护者处理 src/catalog/routes.txt 的未提交修改并更新 release-head，然后从头重跑完整 pre-tag 审计。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
