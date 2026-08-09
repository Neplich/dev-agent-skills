# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `security`
- Skill: `privacy-surface-mapper`
- Eval: `eval-002-user-rights`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8` from `agents/security/test/privacy-surface-mapper/evals/workspace/eval-002-user-rights`.
- Fixture SHA-256: `2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8`
- Prompt SHA-256: `f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `25bd4dbed66f3625883b2a2072dcd568eef569278521e1eac012e86f61347836`
- Skill overlay SHA-256: `840e4d3e20057f4834a3b010b4142d0e7be2f66540c525231dc34075db0dbbee`
- Judge schema SHA-256: `46c6f10cb2ee094e0f2d9b8cf0d9d794ebc801a301eb97187a76e961b4e37fd0`
- Eval definition SHA-256: `ba5034d1b895bcb95cc9d848045b869189eec2c98d23c0a5d5ce381059a73047`
- Metadata SHA-256: `b655e3698222cf189fb740616c1df41fb5ccc3d4bf71526ca29a7ecf05ef368a`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `data_inventory` | PASS | 交付的 privacy-map.md 列出账号资料、订单/交易元数据、产品行为事件及账号生命周期数据，并说明 /me、/data-export、DELETE /me 的入口、处理目的和当前处理情况。 |
| `sharing_and_retention` | PASS | 报告识别了分析副本、备份、缓存、日志及第三方处理者/跨境传输的不确定性，并指出缺少保留期限、法律依据、加密和删除传播证据。 |
| `user_rights` | PASS | 报告分别评估了访问、导出、删除和更正权；准确指出导出越权且不完整、删除仅软删除且不可追踪，并提出身份绑定、异步交付、删除编排和状态查询等整改建议。 |
| `compliance_gaps` | PASS | 报告给出明确的隐私与安全合规缺口、影响、上线阻断项及分工明确的整改建议，覆盖授权、完整性、删除传播、保留例外、安全交付、审计和限流。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=cedd912f4b2e22b67f408be14767275c658a7257752f5f67d67c38961428f209; snapshot_sha256=5d014ee8694828c0ceef86ee40d2a17442cf3da876485a7437866e60ef574d8c
- Behavior: 交付了符合要求的 Security-owned 隐私处理面报告，覆盖数据范围、访问、删除、导出、共享/保留风险、影响和整改建议；未修改业务实现。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=f954f6fb2beee6f446fdaf1e7380f20a7139675884dad90e43a17db9c8bbe9d0; fixture_sha256=2a160ab6ab1065aa7d10a9502c97feefe12d13d5af072b1075181fbf932723d8; output_sha256=ff512bbd9085747910ebee2c646efaa94cb0a47f4c5fc4826d9ec850b0592085; snapshot_sha256=6dbbbbf946997fcd245284a53a849200f069de9409c98d6b5c499adab2a05eb9
- Behavior: 同样交付了结构化安全审查报告，覆盖主要越权、删除、导出和响应安全缺口；作为对比基线，其报告较少展开数据清单和用户权利映射。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
