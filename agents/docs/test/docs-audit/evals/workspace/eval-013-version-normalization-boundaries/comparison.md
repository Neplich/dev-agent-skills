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
- Repository HEAD: `f34c1007244dc48cf04fcd5d073fc5949225f1bd`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `7ed8638f6a80000c952068f188dbfe51d8ede83a52ee0b3635f473bf2d9da41d`
- Skill overlay SHA-256: `4183c2c4191ffb5278feb2ab2a6f8ac1fed136b346aab58bc7438d627c8d7660`
- Judge schema SHA-256: `3cb4db02fceb3a963ab35cfa46d9bd95146e58bed4f92e90064a4aa2fe2f0404`
- Eval definition SHA-256: `5705e506f62200b76867ebca90e47274aa68bc0ca81a7790a3ab2ac8baafd194`
- Metadata SHA-256: `de723686d571b59f10dc657eaf98d1d9ad27c06a9381fcb0dfee19364fb401ec`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_complete_version_identity` | FAIL | with_skill 未读取 fixture，也未输出完整版本 identity；原始 fixture 明确包含 prefixed 与 unprefixed 形式及完整 `1.2.0-rc.1+Build.7` identity。 |
| `enforces_each_source_contract` | FAIL | with_skill 未逐来源检查 raw form、selector 或 extractor，且错误声称未提供 target_release_version；fixture 中已有维护者确认和每个来源契约。 |
| `reports_all_version_blockers` | FAIL | with_skill 仅报告入口凭据缺失，未报告 fixture 中的大小写/重复前缀、缺失值、非法版本、重复索引、selector 为 0、extractor 漂移及 comparison candidate 差异，也未说明其 pre-tag/post-tag 影响。 |
| `binds_pre_and_post_tag_inventory` | NOT_EXERCISED | locked delivery_snapshot 为空，with_skill 输出和 trace 均表明在生成 pre-tag inventory 前即停止；没有可供 post-tag 消费的绑定。 |
| `makes_inventory_integrity_reproducible` | NOT_EXERCISED | locked delivery_snapshot 为空且未生成 inventory，因此没有可重算的完整性证据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=5fbb958343c0775859f6187bc5f86a90f428181db85a97e2a79627e5ba1b4752; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 在入口阶段错误阻断，未读取 fixture、未生成 inventory、未给出版本来源审计。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e4e9083fe5f80e87e2a90dbd2508e2ce8a005911bcd108e280ebfcc392bef53e; fixture_sha256=1cee6041bd72db3f52d6c6c5a5cd2b2192f387347cccb99c7f5a1da1c4e1e970; output_sha256=9e65d2a62d339fc4e65d9fb9e7b72a2df28c401838f4efc9c0370919a809858a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 读取并列出了大部分发布后异常，但错误地将发布前 prefixed/unprefixed 差异视为可归一化放行。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未读取并审查版本来源 fixture。
- with_skill 未保留完整 identity、逐来源契约或全部版本 blockers。
- Next: 读取 fixture，绑定完整来源集合并分别审查 pre-tag 与 post-tag。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
