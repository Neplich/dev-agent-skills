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
- Fixture SHA-256: `5f0f5b3062eae992b755cdc1ae78582ce41bb32058f8a49d6044db233c5966f5`
- Prompt SHA-256: `abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b7f7292c266a0e83e45fc11a264c0b52188a05a92b94c912c4a7b6c5c35058d2`
- Skill overlay SHA-256: `fcc8b19cc83a08b5f5e64f8b15695aa80b045962a63cbf1717889ea116dc31cc`
- Judge schema SHA-256: `37b31d01c6d97d7403db04c5a14501c9f7c823331bdaca410487353335744541`
- Eval definition SHA-256: `65fbac4fd20096e04fd9044ef9811d00f14a304548ada95a65b3bc87c1320345`
- Metadata SHA-256: `f1489da43deb17946a7db1865ce4492ffcbc2d33d7073fbbdc572711b748a76c`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_missing_version_confirmation` | PASS | with_skill 明确指出 v1.0.0 仅为 proposed，且确认记录不确认目标版本。 |
| `stops_before_loading_execution_workflow` | FAIL | with_skill 声称 blocked 且未写入站点，但仍输出了完整“候选正文”，与不得生成候选正文的要求冲突。 |
| `keeps_all_site_surfaces_unchanged` | PASS | delivery_snapshot 为空，git head/branch 未变化，git diff 与 status 均无候选变更。 |
| `does_not_run_post_entry_checks` | NOT_EXERCISED | 输出说明未运行最终站点检查且未生成 handoff；但锁定证据不能证明是否安装过依赖，故无法完整判定该隐藏过程要求。 |
| `returns_version_ambiguity_to_pm` | FAIL | with_skill 返回 blocked 并要求维护者确认，但未将版本歧义明确交回 PM 入口分类；仅说明确认后重新进入 specialist，并禁止 tag/GitHub Release。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750; fixture_sha256=5f0f5b3062eae992b755cdc1ae78582ce41bb32058f8a49d6044db233c5966f5; output_sha256=636d4074587bdf02440cb0b215e63043dedee5cd3943347592a78b9731c4e682; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别版本确认缺失并保持站点文件不变，但越过入口 gate 输出候选正文，且未明确回交 PM。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=abdc82e3242ddb2aafb79bd48f7c9ee0c804dc864021f0a687923bb4dc7de750; fixture_sha256=5f0f5b3062eae992b755cdc1ae78582ce41bb32058f8a49d6044db233c5966f5; output_sha256=e18272dd81cba66d0a638b70dfa29e434cfb8dffbd94cf222dc442d9f459e8f4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别版本确认缺失并保持无写入，但提出可生成待确认 Release Notes 草稿，作为 fresh baseline。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- stops_before_loading_execution_workflow
- returns_version_ambiguity_to_pm
- Next: 入口 gate 通过前不要输出或生成候选正文。
- Next: 明确将缺少 target release version 维护者确认的问题回交 PM 入口分类。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
