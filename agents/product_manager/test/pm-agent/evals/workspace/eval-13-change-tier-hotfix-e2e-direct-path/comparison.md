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
- target_skill_sha256: `ed93e443692bf05e76aaa38c8a5b8faff57190219ed48b9335316584424e6eb9`
- eval_definition_sha256: `44d523204e1cd35255225227815a7ce2ae5cdbcf16a8a61436277c46e50fdccc`
- metadata_sha256: `f04a4e17e46e81cdd684f89a442d6802d244bbaf82973e8aad0b9c94fc7c6e23`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6a4c53f4d8ac913c9f4214c0dc35c3bf4c2a1bd9745f539a3879966e5d7f9011`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `4b716f413649b163f4dd5dcd45dc5b4214bafbb5cb059afb757fef3a77b94653`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `057fcdbdb4862a826dd9a02a1748c655acde3dcccad3cc1b60fd26db843348ee`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `hotfix_direct_path_only` | PASS | with_skill 输出明确限定为仅修改登录页空状态文案，不改交互、接口或其他页面；在源码缺失时索取包含源码的工作区或正确分支。 |
| `evidence_still_required` | PASS | with_skill 输出明确说明缺少登录页源码及可执行测试/验证路径，并要求恢复后留下文案代码改动及验证证据。 |
| `no_full_suite_required` | PASS | with_skill 输出未要求无关的完整 E2E suite，原始 trace 也未执行此类套件。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4b716f413649b163f4dd5dcd45dc5b4214bafbb5cb059afb757fef3a77b94653; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=ece0254d8cbbc8d835e4283076d48857b40e0b7a6e6bf94666c5150d48fb5c9e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确聚焦直接影响路径，识别源码缺失并保留验证证据要求；未发生代码修改或实际验证。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4b716f413649b163f4dd5dcd45dc5b4214bafbb5cb059afb757fef3a77b94653; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=cb49c1e50e40de147bbd58979fc23d9d57b988bd013f3407c1f2db84ad3c8015; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样识别空快照并请求项目输入，作为新鲜基线对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供包含登录页源码的正确工作区或分支；恢复后完成最小文案修改并执行直接影响路径验证。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
