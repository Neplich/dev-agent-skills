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
- target_skill_sha256: `28d6bd56202068b6de6f4e41d3bc74df73f15108b0013486fcd02eaa93f991d8`
- eval_definition_sha256: `86d9727a0807549b3bf3936da079aa7238a2b14b16eed4306c9bda4eb6d7be43`
- metadata_sha256: `bc625033c4a7355e536aa9f113162cca0659e6b3b33765385304d88e087c3513`
- fixture_sha256: `ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `a3c690bb602cdac9c05191ab0581fc35b8fd034dd27825093b3b51de5926404b`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `217840028dda2eba806419edc71588064b0361d1a26fbfdbb7a47693678ccfa6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `authorization_model` | PASS | 报告列出 anonymous/authenticated-user、用户资料与账户设置资源，并描述创建、解析、退出和受保护资源访问路径。 |
| `access_control_findings` | PASS | 报告准确指出可预测会话 ID、无 30 分钟空闲过期、退出未撤销服务端会话，以及缺失登录/Cookie/端点集成证据。 |
| `evidence_and_impact` | PASS | 各项发现均提供了 session-store.js 的具体行号、影响范围、账户接管或会话重放后果及严重度。 |
| `remediation` | PASS | 报告提供了 CSPRNG opaque token、TTL/活动时间、服务端撤销、安全 Cookie 配置及单元/端到端回归验证建议。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56; fixture_sha256=ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a; output_sha256=339acdc111be851a47d99dff3f56e0cd793f72c66a2cbf45eff074eefd5e7ddb; snapshot_sha256=1c1a596d83c40aa30d58371651bd8d96ba5240e14313cc65a76bf071eb5960c7
- Behavior: 完成结构化会话授权审查，覆盖角色边界、授权路径、缺陷证据、影响、严重度和修复验证建议。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56; fixture_sha256=ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a; output_sha256=35a0ac2d23a14260e7dca061d460ba0f9db40f57949b4ff900580a78ad8ec70f; snapshot_sha256=deb02e7459da8fa3c6bafa362cc1a7f41c4a3a852bc83a87247e8e3f665d7b71
- Behavior: 完成静态会话安全审查并识别核心缺陷，但报告结构和授权模型覆盖较简略。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
