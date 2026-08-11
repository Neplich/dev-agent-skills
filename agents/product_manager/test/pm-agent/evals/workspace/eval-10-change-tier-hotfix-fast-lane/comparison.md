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
- Repository HEAD: `d96f213470acb77cb92c1af637626260d3e55b45`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c978d115fb1b50ceb3f80a0d77c450574e05667bd8252ef5b6e8b67105206fa2`
- Skill overlay SHA-256: `5b89d6a3c235a107cde8314b908b32dbfa76d6dc330906b48f74091d88e9019d`
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
| `classify_hotfix` | PASS | with_skill 输出明确将 change_tier 判定为 hotfix，并以功能预期不变及用户已验证新链接为理由。 |
| `allow_fast_lane` | PASS | with_skill 输出明确声明 request_type 为 delivery，且 fast_lane 为 allowed_after_classification。 |
| `preserve_evidence` | PASS | with_skill 输出保留 confirmed_scope、source_documents、用户本地验证来源及 required_output 中的验证要求，且未因 hotfix 省略验证。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8036aad85835ee733e12f58737233d7e9bc1a90da347bec50e7094cf58797ad; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=3febb02a1288bbc242c7c43b3b66d851ff4ef66d4bdbf5f58ae18c4697147776; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确完成 hotfix 分类、分类后 fast lane 判定，并保留范围、来源和验证要求；因工作区为空而安全阻塞后续交付。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8036aad85835ee733e12f58737233d7e9bc1a90da347bec50e7094cf58797ad; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=1d094619ac42df821353208fdac3191aa3fa9cb622f17320e28fca72d16306fe; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 新鲜基线仅发现空仓库并停止，未完成路由分类或证据保留。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
