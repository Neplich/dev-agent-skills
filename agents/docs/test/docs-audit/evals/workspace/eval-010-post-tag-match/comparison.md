# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-010-post-tag-match`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518` from `agents/docs/test/docs-audit/evals/workspace/eval-010-post-tag-match`.
- Fixture SHA-256: `43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518`
- Prompt SHA-256: `47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `8588a4fc6bb55ff6a1ce485f659334cabf6f9624098f4db4f1066bdacc1fc3ec`
- Skill overlay SHA-256: `09c184e9256c59e7718f2b61600ec30436b550d1692a7c65f8b8e6c64fc491f3`
- Judge schema SHA-256: `f64d4542aa97d4b9bcd4bc655a5e70fec7d827a5ea9e9f63067fde8d7b819748`
- Eval definition SHA-256: `f4b575228474dd8bb2a93bb17a067f25252f9c293e1f78393d445c449385e8d2`
- Metadata SHA-256: `12f75879efa3cacf943ae19595239a747563947015e4033eed4ea7f4a51a5b47`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `selects_pre_tag_authority_safely` | NOT_EXERCISED | 锁定 git topology 证明当前仓库有该 custom ref、tag，且 fresh clone 未取得 custom ref；但没有 delivery_snapshot/git_blob 证据证明两边实际读取了 handoff/audit 并独立重建 authority。 |
| `proves_released_tree_binding` | NOT_EXERCISED | 锁定 topology 证明 tag 的 commit/tree 及 clone 的 tag tree，但没有证明当前仓库执行了 direct package-tree 比较，或 clone 从 tag tree 核验完整发布路径。 |
| `verifies_version_surfaces_from_release` | NOT_EXERCISED | 候选输出列出四个版本面并正确区分 v1.2.0 与 package.json 的 1.2.0；但锁定证据没有 git blob 或 delivery snapshot 将这些读取绑定到实际 tag tree。 |
| `requires_durable_post_tag_evidence` | PASS | 候选输出明确指出 proposed post-release ref 没有维护者决定、目标 ref 不存在，并让当前工作区和普通新克隆均保持 blocked；fixture context 与锁定 topology 支持该结论。 |
| `preserves_upstream_release_artifacts` | PASS | 候选输出未声称重新生成、重新盖章或移动 tag；锁定 git evidence 显示 head、branch、refs、diff 与 reflog 均未变化。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=7c1a8a3d832e53935df5ce5bc6feca448187edb7639f34a08fc9414d1992473b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别 tag 与 custom ref 的拓扑、普通 clone 未携带 custom ref，并将两个场景保持为 blocked；但锁定原始证据不足以证明 authority 读取、tree binding 和从 tag blob 核验版本面。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47c14febb101f8d485b3785bf3ac63c5d627ee1f25999068d61918f6bfa13143; fixture_sha256=43a1d01505e6c9e0f71431fdaeb75fea6b1939424f6c22775d15a970f4b73518; output_sha256=2a7663d28fe5769cbf8883e6ea6fe63775acdf384ad4fe2df99fd95852e81644; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 新克隆和 tag 身份描述基本正确，但把内容一致直接升级为可独立核对成功，遗漏了缺少 durable post-tag 结果凭据这一阻塞条件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充当前 custom ref 下 handoff/audit 的锁定 blob 证据。
- Next: 补充 tag tree 与 direct package tree、完整发布路径及四个版本面的锁定读取证据。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
