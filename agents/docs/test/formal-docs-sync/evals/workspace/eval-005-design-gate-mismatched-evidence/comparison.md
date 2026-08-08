# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-005-design-gate-mismatched-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-005-design-gate-mismatched-evidence`.
- Fixture SHA-256: `9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f`
- Prompt SHA-256: `cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `79b2ff102fa24fa224c9f24f44f3e648a1ae7eb9a7a10e639d8675db4454120a`
- Skill overlay SHA-256: `52a3ba7ee2d9485acf003417b40e0d0ca2ab263cbadde98fac58250b6c2a9778`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `9b46c27014c750c2c7c902ee9b735c340d6216e70bd1db10e9ac7cfe4ffa72b8`
- Metadata SHA-256: `8201495b57b213f9db3f5219d86222ff877b211b7bfe7d5c149fe15482812507`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocks_on_evidence_mismatch` | PASS | with_skill 明确对比了 handoff/计划中的 preferences-summary 与 PRD/TRD frontmatter 中的 account-preferences，判定为 feature_path 冲突，并在写入前阻塞。 |
| `design_zero_change` | PASS | with_skill 明确报告设计页和 change-map 均未写入；git_status 与 git_diff 均为空。 |
| `routes_to_owner` | FAIL | with_skill 仅笼统要求 PM/Engineer 对齐 PRD/TRD，未明确将 PRD 冲突路由给 PM owner、将 TRD 冲突路由给 Engineer / trd-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=96ad6a1ad4e196cfd84aaedd21c60d71e9458a5787528846a85e050c361b7680; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别 feature_path 冲突并在写入前阻断，保持目标文件零变化，但 owner 路由不够具体。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cc15a608e753e009b625973b3297598562e26547f4019135f4ff1cee37bc04f0; fixture_sha256=9ee09a35ffbbce09e9a24f1afab930b7c3820a015f0b4c8a431f51638de5592f; output_sha256=8bffa1ce5864ad783ce8bc58c4b3cdb4d9fef4e599d3b9721f6ce3e5762f5ebf; snapshot_sha256=bb8fd2943cdde7f9581c093a0229154512b27022ef295f7015350cdf537b4367
- Behavior: 进行了写入并保留已知 feature_path 风险，未阻断不一致证据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未按断言要求分别明确路由 PRD 至 PM owner、TRD 至 Engineer / trd-gen。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

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

# Skill Eval Comparison

## Evaluation Target

- Skill: `formal-docs-sync`
- Eval: `eval-005-design-gate-mismatched-evidence`

## Test Set / Fixture Version

- Fixture: `issue-121-s2-final`
- Run date: `2026-07-19`

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `blocks_on_evidence_mismatch` | PASS | PASS | 两条 lane 均明确对比 handoff/计划的 `preferences-summary` 与 PRD/TRD 的 `account-preferences`，并停止同步；证据见各自 `result.txt` 与 `PRD.md`/`TRD.md`。 |
| `design_zero_change` | PASS | PASS | 两个目标文件内容均保持原样；`.eval/actual-diff.patch` 仅包含 `src/preferences_summary.py` 新增，不包含 design 文档或 change-map 修改。 |
| `routes_to_owner` | FAIL | FAIL | with_skill 仅路由给 `pm-agent`，未明确路由 Engineer / `trd-gen`；without_skill 仅要求统一 PRD/TRD，未指定 PM owner 与 Engineer / `trd-gen` 双 owner 路由。 |

未满足断言（with/without 任一 FAIL）：``routes_to_owner``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 只加载 design 模块，识别 PRD/TRD/实际路径证据不一致。
- design 页面与映射零变化，并分别指出 PM 与 Engineer/trd-gen 的修复责任。

## Without-Skill Baseline
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- 全新 baseline 在本 fixture 上也满足 3/3，说明该阻塞信号本身足够明显。
- with-skill 的价值主要体现在稳定的 owner 和双面门禁表达。

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- with-skill 无 assertion failure。

## Next Steps

- 保留作为明显冲突的安全网回归用例。

## Runtime Artifact Policy

- 运行期证据仅保留在 `tmp/eval-runs/121/`，不提交。
