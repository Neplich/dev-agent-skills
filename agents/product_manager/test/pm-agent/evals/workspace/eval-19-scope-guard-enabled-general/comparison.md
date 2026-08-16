# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-019-scope-guard-enabled-general`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5` from `agents/product_manager/test/pm-agent/evals/workspace/eval-19-scope-guard-enabled-general`.
- Identity schema: `2`
- target_skill_sha256: `ed93e443692bf05e76aaa38c8a5b8faff57190219ed48b9335316584424e6eb9`
- eval_definition_sha256: `ee3671589f95fa8a892847eb388a153411b54b14444f1f7420faa0785c1aa02b`
- metadata_sha256: `b685d83a8e82816d2f4d521a041ae8452f619db60e5a55ebbccd97b0160d2ffb`
- fixture_sha256: `fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `6b0ff1b76e8b03f7712d3dcd168848aec48a65be2655318b04e40fdedd5925d2`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `9d2abe6f2d9f34e08ce206e7be1d9f6dca54aa3a23552cb1626522bb6c0a068c`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `23c155dfbbdaf3bf6fdaf16d337c16031340e19bffd6d7bb539e43bdc034b2af`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marker_does_not_trigger_pm` | PASS | with_skill 的锁定输出仅说明无法访问或修改 ~/Downloads，并请求用户上传/复制文件；未进入 PM 分类、未产出 PM 文档链或 handoff。其 delivery_snapshot、git_diff 和 git_status 均为空，runner trace 也未显示 PM 行为。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9d2abe6f2d9f34e08ce206e7be1d9f6dca54aa3a23552cb1626522bb6c0a068c; fixture_sha256=fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5; output_sha256=2d7ac7147a7ff1b9a5e28da2baab3684b875b5871c2538b30dcf2de2352549cb; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确将普通文件整理请求作为非 PM 请求处理；在缺少可访问 Downloads 时请求用户提供目录，未被 marker 触发 PM 流程。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9d2abe6f2d9f34e08ce206e7be1d9f6dca54aa3a23552cb1626522bb6c0a068c; fixture_sha256=fe6bcb3f9a810e8ec07d6cd151b927dd0790270b275bdd2a0170bbc91573f2d5; output_sha256=d4d5be6b8e0d2038c7431a77913b53a7211a0685648bb8791fd4f1ccc87cfd18; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 新鲜基线同样未进入 PM 流程；尝试检查 Downloads 后发现目录不可用，并请求用户提供文件。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
