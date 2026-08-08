# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-002-detect-monorepo`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f21b114551d8be3583bc722843216a52ebb44b2de4870be6c6e960ab6597a69f` from `agents/engineer/test/codebase-analyzer/evals/workspace/eval-002-detect-monorepo`.
- Fixture SHA-256: `f21b114551d8be3583bc722843216a52ebb44b2de4870be6c6e960ab6597a69f`
- Prompt SHA-256: `4a44a53303527788f0fdde89c2cf0711930adcb2731bd7176d57421ed0f8220c`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4f1332611648af165a59b99f871678f4c900534d4d5d1fcedda6f815a3b3d5ed`
- Skill overlay SHA-256: `de5de93c0f76ae4be6410327fbb42d3bdbd9dfa29aa0e5edc91c3ed04528aee5`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9a583203eacc9eba1f7a8bc21f635feb6ed3d4608d62de30920ed955c3d1edca`
- Metadata SHA-256: `c7ae12e62e0a39a4d07a2a609b69c812f1e0369799ab62ccf27310eb616d8c85`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `monorepo_classified` | PASS | With_skill 明确输出“是，这是一个 pnpm monorepo”，且根 package.json 与 pnpm-workspace.yaml 都定义 apps/* 和 packages/* workspace。 |
| `workspace_projects_listed` | PASS | With_skill 列出了全部三个 workspace 子项目：apps/web、apps/api 和 packages/shared，并给出对应 package.json 路径及包名；与 fixture 配置和文件一致。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4a44a53303527788f0fdde89c2cf0711930adcb2731bd7176d57421ed0f8220c; fixture_sha256=f21b114551d8be3583bc722843216a52ebb44b2de4870be6c6e960ab6597a69f; output_sha256=5999d87d24936d22090b6c88371c0a8c7c6f1944f23c89ab368226de52c75eba; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确判断为 pnpm monorepo，并完整列出三个 workspace 子项目。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4a44a53303527788f0fdde89c2cf0711930adcb2731bd7176d57421ed0f8220c; fixture_sha256=f21b114551d8be3583bc722843216a52ebb44b2de4870be6c6e960ab6597a69f; output_sha256=1fbd482121f08d6a50a4a752c4055769e5d295f5f99d365ca0fbcdaedfc07493; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确判断为 monorepo，并列出三个应用/共享包。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge package, verdict, timing, and diagnostics remain under ignored `tmp/eval-runs/` or short-lived CI artifacts and are not committed.
- This durable comparison retains only the reviewable summary and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Eval Result: eval-002-detect-monorepo

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-002-detect-monorepo`
- Test case: detect-monorepo
- Workspace: `workspace/eval-002-detect-monorepo`
- Evaluation date: 2026-08-07
- Overall result: PASS
- Behavior result: PASS
- Coverage result: FULL

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Prompt: engineer-agent 已确认需要 repo-level Project Profile，入口依据见 workspace `ENGINEERING_CONTEXT.md`。这个项目是 monorepo 吗？如果是，列出所有子项目
- Paired isolation: baseline 全部完成并销毁运行根后，才创建 with-skill roots；两条 lane 使用逐字相同 prompt 与同一 fixture。
- Leak control: candidate 不可见 `evals.json`、`eval_metadata.json`、expected output、assertions、历史 comparison 或 judge；eval 脚手架 `README.md` 已从两条 lane 物理移除。
- Execution: with-skill、without-skill 与独立 judge 均为 fresh `gpt-5.6-luna`，`model_reasoning_effort="medium"`；judge 读取实际 workspace、JSONL transcript 与文件 hashes。

## Assertions

- PASS `assertion_1`: with_skill final.md 明确写明“是，这是一个 pnpm monorepo”；transcript 中实际读取了 ENGINEERING_CONTEXT.md、package.json 与 pnpm-workspace.yaml，并核实 workspace 配置。
- PASS `assertion_2`: with_skill final.md 列出全部三个子项目路径：apps/api、apps/web、packages/shared；实际 workspace 中对应三个 package.json，且 pnpm workspace glob 为 apps/* 与 packages/*。

## With Skill Behavior

完整触发了仓库入口检查、workspace 配置核对和三个子项目 manifest 核对；最终输出正确判断并列出全部子项目。输入/输出 hashes 与实际 workspace 文件一致，未见写入变更。

## Without Skill Baseline

同一 fixture 下完成了 ENGINEERING_CONTEXT.md、根配置和三个子项目 manifest 的读取，输出同样正确；仅作为 baseline 对照。

## Failures / Findings

- None.
- Root cause: with_skill 按 repo-level 检查路径核实了 workspace 配置及全部 manifests，因此两个要求均满足。

## Next Steps

- 后续修改该 skill、fixture 或 assertions 时，使用同样的 paired fresh 流程重跑。

## Runtime Artifacts Policy

- 本轮 candidates、judge、transcripts、diagnostics、workspace snapshots、timing 与 run status 只作为 ignored 运行期证据，不提交。
- 长期只保留本 `comparison.md`。

## Historical Results

### Previous comparison record: eval-002-detect-monorepo

## Evaluation Target

- Agent: `engineer`
- Skill: `codebase-analyzer`
- Eval: `eval-002-detect-monorepo`
- Test case: detect-monorepo
- Workspace: `workspace/eval-002-detect-monorepo`
- Latest result: PASS (2/2 assertions) - fresh Codex paired validation completed on 2026-07-26
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: repo-level Engineering context, root workspaces metadata, `pnpm-workspace.yaml`, and three package manifests
- Fresh run: isolated paired copies under `tmp/eval-runs/issue-158-round1/engineer-a/`; baseline was regenerated from the same prompt and fixture
- Source branch: `test/issue-158-round1-thin-fixtures`

## Assertions

- PASS `assertion_1`: explicitly identifies a pnpm monorepo from both workspace markers.
- PASS `assertion_2`: lists `apps/web`, `apps/api`, and `packages/shared`.

## With Skill Behavior

The candidate tied the monorepo conclusion to both root manifests and reported every discovered workspace path with package evidence.

## Without Skill Baseline

The fresh baseline also satisfied 2/2 assertions. The fixture makes the classification explicit; the skill adds evidence structure but no assertion-level gain.

## Failures

- With-skill and baseline: none.

## Next Steps

Keep the eval as a stable positive monorepo detection case.

## Runtime Artifacts Policy

Paired outputs and scratch copies are ignored runtime artifacts and are not committed.
