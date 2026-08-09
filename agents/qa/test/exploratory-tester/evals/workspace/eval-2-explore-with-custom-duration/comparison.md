# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `qa`
- Skill: `exploratory-tester`
- Eval: `eval-002-explore-with-custom-duration`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3` from `agents/qa/test/exploratory-tester/evals/workspace/eval-2-explore-with-custom-duration`.
- Fixture SHA-256: `58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3`
- Prompt SHA-256: `95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `4e2073febaef7202820d7977feb83c73b7673e1200e4724a3f37b54a20923059`
- Skill overlay SHA-256: `bb6d955d3f1008412eca24a4e3e97d4883ccffc96444f5d6d3cd037fea0800ba`
- Judge schema SHA-256: `795b13efa8aba1d005ca8e2bf3be74790d6a011a9b79e7e9c3ef0bb4863b7e5d`
- Eval definition SHA-256: `234873760fb9d0649d16f54118fbf0383fa2955b9451730f9429892d78a6d7e0`
- Metadata SHA-256: `4befffc2e8037477b9995f3ded3869d8476cd9a66637621d7f8e8d3fc8c6fed3`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | 交付报告包含 5 分钟时长、目标功能范围、改动面、环境入口，以及保存/取消/未保存状态/toast 等未验证前提。 |
| `assertion_2` | NOT_EXERCISED | 报告记录了 feature-update 场景及既有 QA 资料清单，但锁定证据无法证明这些资料是在独立探索前按要求读取的顺序。 |
| `version_entry_and_subagent` | PASS | 报告明确因平台版本缺失而 blocked，并说明了 repo harness、浏览器连接器、Playwright 的入口顺序和原因，也记录了 subagent 默认执行规则。 |
| `assertion_3` | PASS | 报告区分了无 confirmed issue、待确认的 suspicious signals，以及未覆盖的探索区域。 |
| `assertion_4` | PASS | 报告包含实际覆盖路径、预检资料和环境等 evidence references，而非随机操作清单。 |
| `assertion_5` | PASS | 报告列出了未验证风险、阻塞原因和可执行的后续 QA 建议。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29; fixture_sha256=58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3; output_sha256=e08c791a501d2b08c9a2a66d9b5ff12f6852f645070d434d899c532298ac4840; snapshot_sha256=a8483f35b35ed86188b2aa93d01c35d4a9301073969b2ed215e9051b942f946a
- Behavior: 正确识别 feature-update 范围和阻塞条件，交付了结构化探索报告，覆盖章程、预检、入口选择、异常分层、证据、风险与下一步。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=95b19585ae663cfe50fef5d8a922d75ec357803535a13bbb323cdf9b1845fa29; fixture_sha256=58e996bab34649b23e7bf5cc00be4fa65ff65a8e7b288cba77fc10a44d715cf3; output_sha256=f016c940d2023a57be41a153fd89a31a4a6b41144914dea29fdd18fc58d0d056; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 仅报告入口不可达和无法验证功能，未交付探索报告或结构化证据。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供可访问的 QA 入口并记录浏览器/平台版本。
- Next: 重新执行 5 分钟探索，覆盖保存、取消、未保存状态、校验与 toast。
- Next: 若发现可复现问题，补充 per-TC evidence 并移交 bug 分析。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
