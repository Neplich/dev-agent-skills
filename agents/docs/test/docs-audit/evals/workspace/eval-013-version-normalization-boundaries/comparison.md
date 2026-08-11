# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-013-version-normalization-boundaries`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970` from `agents/docs/test/docs-audit/evals/workspace/eval-013-version-normalization-boundaries`.
- Fixture SHA-256: `1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970`
- Prompt SHA-256: `e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e`
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b11b38c1c44c386fe19122dfb1ce5918b2bfbc4830ad32aa994d8a7e39f35e7`
- Skill overlay SHA-256: `85c4ae0a1d58505c4a23c34e6f9116aed81a09b4b6270e3ce148424084f6c7e0`
- Judge schema SHA-256: `3cb4db02fceb3a963ab35cfa46d9bd95146e58bed4f92e90064a4aa2fe2f0404`
- Eval definition SHA-256: `5705e506f62200b76867ebca90e47274aa68bc0ca81a7790a3ab2ac8baafd194`
- Metadata SHA-256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | PASS | with_skill 输出保留 `v1.2.0-rc.1+Build.7` 与 `1.2.0-rc.1+Build.7` 的前缀差异，并明确保留大小写、预发布标识和 build metadata 后归一化判等。 |
| `enforces_each_source_contract` | PASS | with_skill 输出逐项列出观察集 B 的前缀、缺失、空值和非法 SemVer 问题，并指出 selector resolution 为 0、索引匹配数为 2 及 extractor identity 不一致；同时拒绝以观察集 A 或其他来源替代缺失正式来源。 |
| `reports_all_version_blockers` | PASS | with_skill 输出覆盖了大小写/重复前缀、缺少 v、索引缺失与重复、空 releases 值、marketplace 缺失、非法 package 版本、候选版本不精确及 extractor 不一致，并分别判定 pre-tag 与 post-tag blocked。 |
| `binds_pre_and_post_tag_inventory` | NOT_EXERCISED | 原始 fixture 显示正式来源和审计 handoff 在当前树中不存在，且 with_skill 输出确认 pre-tag 无法建立可信 inventory，post-tag 无法绑定同一 inventory；按判定规则该后续消费场景未被实际行使。 |
| `makes_inventory_integrity_reproducible` | NOT_EXERCISED | 原始 fixture 与 locked trace 仅能证明来源树不完整、inventory 未建立；with_skill 输出报告 `invalid / unbound`，但确定性完整性证据在 pre-tag 阻断前尚不可产生。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=793cfbbf2bcfbd62af7559f21f4b4a7e695184f4922b9a65dcd301682dfced04; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 准确识别完整版本 identity、逐来源阻断非法观测并报告全部 blocker；因 pre-tag 已阻断，inventory 绑定与完整性重算未实际行使。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=9c4d30afdef83d9273214911dd4d47ad44b919789ba0004962ae0d4f5fbce7ea; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 能识别部分发布后版本问题，但发布前仅给出有条件通过，未完整执行逐来源审计，也未建立后续 inventory 语义。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补齐正式版本来源与 pre-tag audit handoff 后，重新执行 inventory 绑定和完整性重算。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
