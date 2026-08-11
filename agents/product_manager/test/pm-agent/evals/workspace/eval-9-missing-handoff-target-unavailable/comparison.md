# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-009-missing-handoff-target-unavailable`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-9-missing-handoff-target-unavailable`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `5230fc275f473a55b5d59c172358aff82cf42415f36da1a920c1b4fa1e1e3cc1`
- Repository HEAD: `b385df5d17058a52081357c8a8480fc146c3d989`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `ecf67dca8a2fd53bb0dd6d0a63750ba2716e88dc4af4f77176ea061260d64286`
- Skill overlay SHA-256: `2ed9fef9a54be8009ea156c857682ad7dd82c0e56e3463d3257fe74fe9c977ec`
- Judge schema SHA-256: `45aa95828b353344675a6e62421acac466500932a42ce4d64f8f43969bd5bb6d`
- Eval definition SHA-256: `ea4ff3ed92cd6df9743d23b747dc29d9087560d5cfa7f5f4525b8e146b0b7e97`
- Metadata SHA-256: `f52777a03f0c132438bf125e153205560b01f6abb53fcb15add6a3552b96312b`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detect_missing_target` | PASS | with_skill 输出明确写明“当前环境未安装或暴露 designer-agent”及“没有设计能力”。 |
| `mark_handoff_blocked` | PASS | with_skill 输出将 entry_basis 和 designer_entry_gate 标记为 blocked，并明确下一步是“安装/接入 designer-agent”。 |
| `do_not_perform_missing_role` | PASS | with_skill 输出明确限定“当前仅可完成 PM 路由与阻塞说明；禁止代替 Designer 产出设计或直接实现 UI”，且没有交付视觉规范或设计物。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5230fc275f473a55b5d59c172358aff82cf42415f36da1a920c1b4fa1e1e3cc1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=834e66c43b78acc79d46aae1e83645be43427305dfe8fb872511eb76039b3ae1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别 designer-agent 不可用，将设计 handoff 标记为 blocked，保留 PM 路由并停止在 Designer 职责边界。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5230fc275f473a55b5d59c172358aff82cf42415f36da1a920c1b4fa1e1e3cc1; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=12bff2e1ff073a514458e1f4da8cd3b90d1c41cc59ebae321b8002c86270633e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅报告工作区为空并请求补充需求资料，未识别 designer-agent 缺失或标记 handoff blocked。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
