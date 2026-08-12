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
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `4b716f413649b163f4dd5dcd45dc5b4214bafbb5cb059afb757fef3a77b94653`
- Repository HEAD: `715bd6b76fcd6f14f475aeabe141543063d431ba`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `be11ec63823b148323fef6c35d27c0861bd093b24d683f705e846234e98b7baa`
- Skill overlay SHA-256: `961e7aacbdec2d154ad578bc7bf54d5d734f34031af1384fb20aa67a8e2d392a`
- Judge schema SHA-256: `6a4c53f4d8ac913c9f4214c0dc35c3bf4c2a1bd9745f539a3879966e5d7f9011`
- Eval definition SHA-256: `0e4e9687500855bbb8cac580183d47bafa14e53a69d5477185a5ceacddfe1857`
- Metadata SHA-256: `385a2edb2c46d9f3ce571c34b812bf357f9247b71af061faebaf0764c87334a2`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `hotfix_direct_path_only` | NOT_EXERCISED | with_skill 明确将 hotfix_disposition 设为 rejected、change_tier 设为 standard，且工作流因缺少业务源码而停止；未进入 hotfix QA 覆盖决策。 |
| `evidence_still_required` | NOT_EXERCISED | with_skill 要求验证结果并明确无法执行验证、禁止伪造验证结果，但由于缺少源码未进入记录 verification evidence、结果及 blocked checks 的验证步骤。 |
| `no_full_suite_required` | NOT_EXERCISED | with_skill 将变更判定为 standard 且 hotfix 被拒绝；工作流在源码缺失处阻断，未进入 E2E 套件范围决策。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4b716f413649b163f4dd5dcd45dc5b4214bafbb5cb059afb757fef3a77b94653; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=fcc072f94b45257f5e67663f0db7af4b8723be7920d6df3c77c2c6ad8711bbcf; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 诚实识别空工作区和缺失文案，未修改文件或伪造验证，并输出了 standard/rejected 的路由与阻断边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4b716f413649b163f4dd5dcd45dc5b4214bafbb5cb059afb757fef3a77b94653; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=ec062499e6be5fefcbce169334e139932c4ae23bb1446700af242a8c455cd9af; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到空 Git 仓库后直接阻断，未提供结构化路由或验证要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供正确的项目工作区和目标新文案后，再执行最小范围修改与验证。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
