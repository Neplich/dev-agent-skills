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
- Identity schema: `2`
- target_skill_sha256: `ed93e443692bf05e76aaa38c8a5b8faff57190219ed48b9335316584424e6eb9`
- eval_definition_sha256: `47a19a6c15b443fba6827b5bff8e5f73b3367c26176898038b1822e6a445e0c6`
- metadata_sha256: `db913f77966bbc3a5f433aefe00a5e9265090f37be540fbcde62221b7046f2a4`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `bb0ee0282945f3d4f9dce339b9d8538e36a23ce40cb0cf92b33dc2be95234be0`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `c8036aad85835ee733e12f58737233d7e9bc1a90da347bec50e7094cf58797ad`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `aaa44399c1d48ca988bdeda9dcf25acf631b5b582ec64543a5cfb0c5e9b90965`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classify_hotfix` | NOT_EXERCISED | 锁定证据显示候选检查了 PM/交付技能并将请求称为交付型热修复，但该结论仅出现在 agent-message 中，原始证据不能独立证明已完成分类。 |
| `allow_fast_lane` | NOT_EXERCISED | 锁定输出未提供 fast lane 说明；由于工作区为空且交付流程在前置核对阶段被阻塞，无法从原始证据证明该步骤已发生。 |
| `preserve_evidence` | NOT_EXERCISED | 候选保留了仓库状态、未创建提交/PR及 CI 状态等交付证据，但原始证据不足以证明已执行该断言要求的 scope、source evidence 和 verification evidence 保留流程。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8036aad85835ee733e12f58737233d7e9bc1a90da347bec50e7094cf58797ad; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=18a1a69f968c2e3e68a7758dbf56b3ca8ce8919ae1cf2cca3cda843041ff6b88; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 检测到空仓库、无 README、无远程和无变更后停止交付，未执行提交、推送、PR 或 CI 回读。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8036aad85835ee733e12f58737233d7e9bc1a90da347bec50e7094cf58797ad; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=ad106e76f540896f786f363554a75828c7652eac22ee4db10dee28686af1e0c7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样检测到空仓库并停止，未执行任何交付变更。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充包含 README 修复的工作区并重新执行交付流程。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
