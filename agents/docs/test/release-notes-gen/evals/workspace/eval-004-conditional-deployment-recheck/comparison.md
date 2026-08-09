# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-004-conditional-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31` from `agents/docs/test/release-notes-gen/evals/workspace/eval-004-conditional-deployment-recheck`.
- Fixture SHA-256: `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31`
- Prompt SHA-256: `5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b7f7292c266a0e83e45fc11a264c0b52188a05a92b94c912c4a7b6c5c35058d2`
- Skill overlay SHA-256: `fcc8b19cc83a08b5f5e64f8b15695aa80b045962a63cbf1717889ea116dc31cc`
- Judge schema SHA-256: `f6ca8293d29d78d2f2b85bd613e1f25b3aa93a647c64e21ca6731d5a228a1284`
- Eval definition SHA-256: `34ab52326e403178b3c65c89903f9ce3ed937721059a083b8dcd35f212e12e18`
- Metadata SHA-256: `026d3644999635bf9397130063cb1f65e3467ff790b1fe892aa83df25be7904c`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `skips_content_only_recheck` | PASS | with_skill 正确识别 editorial.patch 仅为正文措辞变化，并保留其不影响现有部署结论的状态。 |
| `rechecks_material_release_surface` | NOT_EXERCISED | with_skill 正确识别 internal-entry.patch 修改 internal 构建输出目录和 Docker COPY 路径，并要求重新进行部署完整性审查；但锁定证据无法证明是否复用了 skill-map 共享检查或避免复制清单。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=86199450813edfd305850baa10a0b4d7b2e4b608b272075731925c275397ae24; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确区分纯正文变化与发布面变化，并阻止在缺少主机仓库和确认信息时完成版本说明交接。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=8f9f196f9f02e624204209cc18afcab66ba42caffbe09ee10aa408c1dad821dc; snapshot_sha256=713fe3832b81918f3ee4ef3502c1588b5d24f8611e15c9c881967438462b655f
- Behavior: 将 internal-entry.patch 误判为不影响部署结论，未触发共享部署完整性复查。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充主机仓库、发布范围、证据来源和维护者确认后完成版本说明收尾。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
