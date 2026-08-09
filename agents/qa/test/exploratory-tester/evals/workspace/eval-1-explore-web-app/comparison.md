# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-001-explore-web-app`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7` from `agents/qa/test/exploratory-tester/evals/workspace/eval-1-explore-web-app`.
- Fixture SHA-256: `ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7`
- Prompt SHA-256: `b0dd5a79c80e2e161088bef46107d054902f47f9ef2205167f1eaadd760b99cd`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4e2073febaef7202820d7977feb83c73b7673e1200e4724a3f37b54a20923059`
- Skill overlay SHA-256: `bb6d955d3f1008412eca24a4e3e97d4883ccffc96444f5d6d3cd037fea0800ba`
- Judge schema SHA-256: `3783048bfb479d6e8907a0e84c4199cb646178dd63c9a58d60ddd654db2122dc`
- Eval definition SHA-256: `32b9d61e575fbee81406ffc68edbaec9418feec621754c8fca12fc2f2edd2c08`
- Metadata SHA-256: `228751d86855b3dcdb583bdc4a44c4a493c28334ed74368c030ddad805b1f314`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections were removed without rerunning candidate or judge; the executor hash reflects the current durable-format-only implementation.
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 交接报告直接包含 Surface、15 分钟 Timebox、Heuristics 和 Escalation signals。 |
| `assertion_2` | NOT_EXERCISED | 报告声称已读取相关 QA 资料并说明未新增场景或脚本，但锁定证据无法独立证明实际读取顺序。 |
| `assertion_3` | PASS | 15 分钟明确来自用户请求，并围绕 SearchPanel、FilterPills、ResultsList 及键盘焦点风险组织范围。 |
| `assertion_4` | PASS | 报告区分已确认失败、环境阻塞、风险与未探索缺口，并明确未将阻塞或未确认信号写成产品缺陷。 |
| `assertion_5` | NOT_EXERCISED | 报告采用 charter、优先路径和恢复后的探索清单；但因 QA_BASE_URL 缺失，实际页面路径与边界尚未执行。 |
| `assertion_6` | PASS | 锁定报告包含 charter、timebox、covered/gaps、证据链和后续动作，具备交接结构。 |
| `deduplicates_existing_flows` | PASS | 报告复用 TC-001，并明确未新增或修改 TC、script、FLOW_INDEX；未发现可沉淀的新流程。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0dd5a79c80e2e161088bef46107d054902f47f9ef2205167f1eaadd760b99cd; fixture_sha256=ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7; output_sha256=449dd945645863b11ef2b483a68e36f8e048438416df5e57fa82d4c21911f400; snapshot_sha256=d8573e39c0ebb16cbf0cfcff0ddec52f29c46fa068c608793a00691201f47188
- Behavior: 完成预检并交付结构完整的探索测试报告，准确标记 blocked，未虚构运行时结果。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=b0dd5a79c80e2e161088bef46107d054902f47f9ef2205167f1eaadd760b99cd; fixture_sha256=ee088defa4a7bb2cbc3d091f8817eac9fb8cc7c128c92be34adf72ee4a79f3b7; output_sha256=007805819ddbba47c04eeb05979490572e7cfdba59e3e7ee1ca7c60413c41e76; snapshot_sha256=f30d5320795192b7b776ac66fcd576daffd6ac2d410500878da06179de8481d7
- Behavior: 同样交付了 blocked 交接报告，但结构与证据链较简略。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供 QA_BASE_URL 及必要登录/种子数据。
- Next: 从 TC-001 开始执行筛选、空状态和键盘焦点路径，并保存截图、console/network 证据。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
