# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-003-audit-pure-refactor`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677` from `agents/docs/test/docs-audit/evals/workspace/eval-003-audit-pure-refactor`.
- Fixture SHA-256: `a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677`
- Prompt SHA-256: `20617e4b8714b5129b537177e8c463822eec4083d7fdd0d6520c27013f94489f`
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b11b38c1c44c386fe19122dfb1ce5918b2bfbc4830ad32aa994d8a7e39f35e7`
- Skill overlay SHA-256: `85c4ae0a1d58505c4a23c34e6f9116aed81a09b4b6270e3ce148424084f6c7e0`
- Judge schema SHA-256: `3e58dae2a34edb25f9589f7bddb4e3282cd1f66e3b0c3f35187db4ed16fd5f23`
- Eval definition SHA-256: `a7212e3282f2eaaa660e0675fb965d5050f366a07c153f3821d78fdab8976de5`
- Metadata SHA-256: `1e20c97bb5ffc477023f6bbbd217e71d747297cb0b8f52652660b6b2d10adc7a`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `sends_refactor_suspect_to_fact_layer` | NOT_EXERCISED | 锁定 trace 中仅有 agent-message 声称进入 suspect；无独立命令/工具结果证明该隐藏流程。 |
| `classifies_accurate_refactor_verified` | PASS | 目标 routes.txt 与锁定 diff 显示 GET /catalog/items、可选 limit、200 响应和 400 invalid_limit 均准确；with_skill 最终明确判为 verified。 |
| `does_not_force_noop_doc_edit` | PASS | with_skill 明确说明纯实现重构、无需文档改动，并给出 documentation_change_required: false。 |
| `does_not_block_for_unchanged_accurate_doc` | PASS | with_skill 将阶段判为 blocked，原因是缺少版本化审计交接/候选记录及 Release Notes 版本面，并明确不能返回 ready_for_tag；未将页面判为 stale。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=20617e4b8714b5129b537177e8c463822eec4083d7fdd0d6520c27013f94489f; fixture_sha256=a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677; output_sha256=ed9550f1e22cb041c724d665f3a8892c3fb51ebe2c67a249d1ba940bedd78a86; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确完成事实核对，确认文档准确且无需无意义编辑，并因缺少完整 release-version surface 证据而阻塞；隐藏 suspect 交接流程无法由独立原始证据确认。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=20617e4b8714b5129b537177e8c463822eec4083d7fdd0d6520c27013f94489f; fixture_sha256=a0071569c74867aaacfda16310f9f4a06e50a375aa0e6b62ee25e801db096677; output_sha256=5a7da353578a4cac7cd8a3c685b0cee1f2d36c22449b50c2d70f05f36c5a856a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 新鲜基线直接放行准确文档，未展示 suspect→事实层流程，也未识别完整 pre-tag release surface 阻塞。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
