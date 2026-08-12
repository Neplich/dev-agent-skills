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
- target_skill_sha256: `c5c4e1b3eeeb704a06966dee8397bc4f1df239be6ed5f5799f8d4bd382f23626`
- eval_definition_sha256: `86d9727a0807549b3bf3936da079aa7238a2b14b16eed4306c9bda4eb6d7be43`
- metadata_sha256: `f26166d912f73c7f118a1561bee3e62973123b274975fb4a17a869fba31f82a0`
- fixture_sha256: `ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `a3c690bb602cdac9c05191ab0581fc35b8fd034dd27825093b3b51de5926404b`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `authorization_model` | PASS | 报告包含 anonymous/authenticated-user 角色、已认证资源边界及登录、解析、过期、退出授权路径。 |
| `access_control_findings` | PASS | 报告以 session-store.js 行号指出可预测会话 ID、缺失 30 分钟过期、退出未撤销服务端会话，以及 Cookie/路由集成缺口。 |
| `evidence_and_impact` | PASS | 每项发现均给出代码位置、严重度、账户接管或旧会话继续访问等影响。 |
| `remediation` | PASS | 报告提供随机高熵令牌、TTL、服务端撤销、登录轮换、Cookie 属性和集成回归测试建议。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56; fixture_sha256=ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a; output_sha256=2970ac207d849d5b83742567db54f2560ac0af64d48d95ccb853db969f2c3959; snapshot_sha256=8fd3292d4752830247802fd90c5db1cfbf686c087048ac3272430c0976d374cc
- Behavior: 完成并交付结构化安全审查，覆盖全部要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=2d47191ee1ff1f15f350d3cf5e7d5d57f991913e4e2049f23f29264b335bfc56; fixture_sha256=ef54897bb21af32853256277d12077e05ab3c6d281df76ae5f08944cb67d641a; output_sha256=ec64be4e0fe7cc7d6ee7e743498ea934fb8bdda556ff46906ab391b5cb1f979e; snapshot_sha256=c5a507dedc9a8d3b6cfcfc38adf76001365ccc1a9d12cea9b53a6d68f1f8ed62
- Behavior: 同样识别主要会话缺陷并交付报告，但内容与结构较简略。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
