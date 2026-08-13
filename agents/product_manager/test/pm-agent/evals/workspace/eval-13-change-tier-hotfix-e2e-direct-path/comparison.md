# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-013-change-tier-hotfix-e2e-direct-path`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-13-change-tier-hotfix-e2e-direct-path`.
- Identity schema: `2`
- target_skill_sha256: `28ec452f7594200030ea15ffdc8d5edc9ae2298318457884574b818964824cf6`
- eval_definition_sha256: `44d523204e1cd35255225227815a7ce2ae5cdbcf16a8a61436277c46e50fdccc`
- metadata_sha256: `385a2edb2c46d9f3ce571c34b812bf357f9247b71af061faebaf0764c87334a2`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6a4c53f4d8ac913c9f4214c0dc35c3bf4c2a1bd9745f539a3879966e5d7f9011`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `4b716f413649b163f4dd5dcd45dc5b4214bafbb5cb059afb757fef3a77b94653`
- Repository HEAD: `2f950c46c67111058957774f796ccf97ae616d36`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `8041f8266999d0ba9597ccc13e0354e28fcccb4a3b921ae9b5b9d1e08fe1da7b`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `hotfix_direct_path_only` | PASS | with_skill 明确将范围限定为“登录页空状态文案”，未修改或扩展到无关路径；空 fixture 下仅请求项目工作区和目标文案等最小输入。 |
| `evidence_still_required` | PASS | with_skill 明确说明缺少源码、目标文案和可执行验证路径，未声称已验证，并请求补齐项目工作区或目标文案。 |
| `no_full_suite_required` | PASS | with_skill 未要求无关的完整 E2E suite 作为前置条件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4b716f413649b163f4dd5dcd45dc5b4214bafbb5cb059afb757fef3a77b94653; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=58c98cdf544381d0d0b7b861da987839e4884d22458cc67aeb0a6d7d799c636b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到输入不足，保持修改与验证边界，说明阻塞项并请求最小补充输入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4b716f413649b163f4dd5dcd45dc5b4214bafbb5cb059afb757fef3a77b94653; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=234bde27287ff4e611e07c9baa2cbb427d744fd4b7709e23aa2edbfa7d49923b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样识别到空仓库并请求切换到包含登录页的项目内容；作为基线未影响 with_skill 判定。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供包含登录页源码的工作区及目标文案后，执行直接影响路径验证。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
