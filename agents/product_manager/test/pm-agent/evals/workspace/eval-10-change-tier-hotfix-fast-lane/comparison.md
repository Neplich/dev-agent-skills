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
- target_skill_sha256: `e17c69ef6e179644f91ff00df55f141c375753f4668f30aca4e37e8247a60506`
- eval_definition_sha256: `47a19a6c15b443fba6827b5bff8e5f73b3367c26176898038b1822e6a445e0c6`
- metadata_sha256: `db913f77966bbc3a5f433aefe00a5e9265090f37be540fbcde62221b7046f2a4`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `bb0ee0282945f3d4f9dce339b9d8538e36a23ce40cb0cf92b33dc2be95234be0`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `c8036aad85835ee733e12f58737233d7e9bc1a90da347bec50e7094cf58797ad`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `e3c335a28f9d92dbe730e6d9190f098f7ac39e61749cc82d73776faa1d506ba1`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classify_hotfix` | FAIL | with_skill 的最终输出明确记录 `change_tier: standard` 和 `hotfix_disposition: not_applicable`，与必须判定为 hotfix 相矛盾。 |
| `allow_fast_lane` | FAIL | with_skill 未说明 hotfix 加 delivery/status 可在分类之后使用 fast lane；最终路由反而标为 standard。 |
| `preserve_evidence` | FAIL | with_skill 未要求保留 scope、source evidence 和 verification evidence；delivery_snapshot 为空，最终输出仅说明相关证据缺失。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8036aad85835ee733e12f58737233d7e9bc1a90da347bec50e7094cf58797ad; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=3a27d30371c80c0420971e4c1408e9232ce070197823b680dbdc87d5397634de; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到工作区为空并保持零变更，但将请求错误路由为 standard/not_applicable，未给出 hotfix fast lane 或证据保留要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8036aad85835ee733e12f58737233d7e9bc1a90da347bec50e7094cf58797ad; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=b32112e60aa0b6875d7048754d6415687a3dda048e8f4db4d13ea0d0e39a9155; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样因空工作区阻塞交付，未提供断言所需的分类、fast lane 或证据保留说明；仅作基线对比。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未满足三个用户可见断言：hotfix 分类、分类后 fast lane 说明、证据保留要求。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
