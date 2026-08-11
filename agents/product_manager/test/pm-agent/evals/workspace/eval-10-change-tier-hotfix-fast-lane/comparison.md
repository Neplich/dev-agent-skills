# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-010-change-tier-hotfix-fast-lane`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-10-change-tier-hotfix-fast-lane`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `c8036aad85835ee733e12f58737233d7e9bc1a90da347bec50e7094cf58797ad`
- Repository HEAD: `5eed6bd61702fe0e1aa38eba2649b61fbdbcd5a6`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4e76801189b426dd33ce29ced16e549279e16d547ce6762d36863400f4354122`
- Skill overlay SHA-256: `77702f471e61dbfa60bd67a78323dc643acf1a23ee94c61de468a9d3da2ceccc`
- Judge schema SHA-256: `bb0ee0282945f3d4f9dce339b9d8538e36a23ce40cb0cf92b33dc2be95234be0`
- Eval definition SHA-256: `47a19a6c15b443fba6827b5bff8e5f73b3367c26176898038b1822e6a445e0c6`
- Metadata SHA-256: `dd7edb355d66e4505d2039e9fe3eb4eb203c3d8b2cfcc299410f099efef7e166`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classify_hotfix` | PASS | with_skill 输出明确将 change_tier 判定为 hotfix，并以功能预期不变及已有链接验证作为 selection_reason。 |
| `allow_fast_lane` | PASS | with_skill 输出标明 hotfix_disposition: allowed，并明确 fast_lane: allowed_after_classification；request_type 为 delivery。 |
| `preserve_evidence` | PASS | with_skill 输出保留 confirmed_scope、source_documents，并将验证证据列入 required_output，未因 hotfix 省略验证要求。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8036aad85835ee733e12f58737233d7e9bc1a90da347bec50e7094cf58797ad; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=c6192e4d4622b0974b853c17a91262781103720bc83a227b643f24971735dbb7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确完成 delivery 请求的 hotfix 分类，允许分类后的 fast lane，并保留范围、来源与验证证据要求；实际交付因空仓库和缺少 engineer-agent 被阻塞。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8036aad85835ee733e12f58737233d7e9bc1a90da347bec50e7094cf58797ad; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=5f7592ec9cec08c9d097e3fefea2ac5c25e1dadb783be45f4b9ffec44d5702c0; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅报告空仓库并请求补充内容，未完成 hotfix 分类、fast lane 判断或证据保留要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
