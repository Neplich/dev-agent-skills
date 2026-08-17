# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `authz-reviewer`
- Eval: `eval-002-session`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a` from `agents/security/test/authz-reviewer/evals/workspace/eval-002-session`.
- Identity schema: `2`
- target_skill_sha256: `560a4230ae443905926eeddf72dec9114fbb989ca3911007bb3d55a10a342e86`
- eval_definition_sha256: `86d9727a0807549b3bf3936da079aa7238a2b14b16eed4306c9bda4eb6d7be43`
- metadata_sha256: `bc625033c4a7355e536aa9f113162cca0659e6b3b33765385304d88e087c3513`
- fixture_sha256: `ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `a3c690bb602cdac9c05191ab0581fc35b8fd034dd27825093b3b51de5926404b`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `382daaa46e228ddafa411ea49b63d6055764b79f7917bec67fcebf40d2845479`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `authorization_model` | PASS | 报告建立了 anonymous/authenticated-user 角色矩阵，覆盖用户资料和账户设置资源，并描述了创建、解析、受保护请求及退出失效路径。 |
| `access_control_findings` | PASS | 报告指出会话 ID 可预测、无 30 分钟无活动过期、退出不撤销服务端会话，并识别 Cookie 安全属性和登录后轮换缺少实现证据。 |
| `evidence_and_impact` | PASS | 各发现均提供了具体文件与代码行、严重度、攻击或账户接管等影响，以及上线阻断结论。 |
| `remediation` | PASS | 报告提供了随机会话值、服务端过期删除/吊销、退出幂等及 Cookie/轮换集成修复建议，并列出边界、重放、并发和端到端回归验证。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56; fixture_sha256=ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a; output_sha256=c3d1bf9b7443679f436222e8fc93bd60c901dd9b4c859eef156f8d95251ee3f6; snapshot_sha256=d0fae43dcd70e8e8e757070ccf8ce32dfaf30247100a2cc53c52acee4b660516
- Behavior: 交付了结构化会话授权审查，覆盖角色边界、会话缺陷、证据影响及修复验证建议。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56; fixture_sha256=ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a; output_sha256=6b07b32f54a023a6a9bba2e19e794028caabe3abcbc6d3c5a3dc44e5813a537b; snapshot_sha256=7a74c5140715e9d364173e997f305286a905fbef9a6084deb407a694228c9379
- Behavior: 同样交付了会话安全审查并识别主要缺陷，作为 fresh baseline 对比。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
