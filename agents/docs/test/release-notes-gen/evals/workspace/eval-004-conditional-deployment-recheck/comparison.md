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
- Identity schema: `2`
- target_skill_sha256: `9d15471128b5c653c03406ba512b69c7510ab64bfd6b1cba8b6458bff7449a16`
- eval_definition_sha256: `34ab52326e403178b3c65c89903f9ce3ed937721059a083b8dcd35f212e12e18`
- metadata_sha256: `026d3644999635bf9397130063cb1f65e3467ff790b1fe892aa83df25be7904c`
- fixture_sha256: `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `f6ca8293d29d78d2f2b85bd613e1f25b3aa93a647c64e21ca6731d5a228a1284`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `875d94bbeede7fb3f25ae54a8099f5bb996a939530b57c2c2295a2fa54bd46e9`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `skips_content_only_recheck` | PASS | with_skill 正确识别 editorial.patch 仅修改 Release Notes 正文，不改变构建产物、导航或运行入口，并判定不会使既有部署结论失效；这等价于保留既有状态。 |
| `rechecks_material_release_surface` | NOT_EXERCISED | with_skill 正确识别 internal-entry.patch 改变内部构建输出目录、Dockerfile 复制路径及导航入口，并指出必须重新验证 Internal 变体；但因缺少主机站点与确认入口，实际共享检查未运行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=2135b15702300b375bef0d2e9dd7710f3e50499f5b81684f3783b3ded7d1cc76; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确区分正文变更与发布面变更；在缺少入口证据和主机运行时证据时阻断版本说明收尾，未修改文件或部署配置。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=cfa942ec34d6a8c023b1df1b4b0bcb34acbf43e2dd372a3eea19bff8ee37a88a; snapshot_sha256=c351c62c576411bd39d457753a27d9880ebbcbe72a6ef40b3c416d6a9bc4f4c7
- Behavior: 完成静态比较并交付 decision.md；作为对照，其识别结果与 with_skill 的变更分类一致。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补齐已确认的版本、主机、发布范围和证据交接后运行共享文档部署检查。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
