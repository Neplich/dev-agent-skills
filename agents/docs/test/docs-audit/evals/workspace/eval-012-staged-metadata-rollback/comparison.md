# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-012-staged-metadata-rollback`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620` from `agents/docs/test/docs-audit/evals/workspace/eval-012-staged-metadata-rollback`.
- Fixture SHA-256: `1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620`
- Prompt SHA-256: `4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb`
- Repository HEAD: `f34c1007244dc48cf04fcd5d073fc5949225f1bd`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `7ed8638f6a80000c952068f188dbfe51d8ede83a52ee0b3635f473bf2d9da41d`
- Skill overlay SHA-256: `4183c2c4191ffb5278feb2ab2a6f8ac1fed136b346aab58bc7438d627c8d7660`
- Judge schema SHA-256: `73f9308006ffa877e1ed5f74c8eef2e3a2b3222e98dd5485cfd0ba5e210de92a`
- Eval definition SHA-256: `885108a0e0e9ce48751816455b91da0ec400a08bb7d3a722984a36e4221d1938`
- Metadata SHA-256: `86b2ab0ad4bcb3fb98728ca8ff1375ff58d1094876353cbeafc325bf7593eb63`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `detects_non_content_candidate_drift` | PASS | 引用的 staged.name-status 与 staged.patch 足以暴露普通文件、可执行位、符号链接、删除、重命名及链接目标等 Git 语义变化。 |
| `rejects_every_unauthorized_transformation` | FAIL | 输出阻塞了文件类型变更、删除、重命名和越界链接，但未逐类明确阻塞 catalog-items.md 的 100644→100755 可执行位变更。 |
| `rechecks_committed_candidate_boundaries` | NOT_EXERCISED | 后续 candidate/handoff 尚未形成，且当前捕获哈希不一致、目标版本也未确认；该后续交互步骤未被执行。 |
| `rolls_back_only_the_failed_attempt` | PASS | 输出以 host-before/host-after 证据说明未改动现有 index/worktree，并明确保留 notes/release-checklist.md 与 notes/local.txt 这两项无关用户变化；候选仅存在于隔离暂存捕获中。 |
| `proves_host_state_restoration` | PASS | 输出证明 ref 无已提交差异，并给出 index/worktree 清理与重新捕获、重新审计的阻塞处置；原始前后状态记录也覆盖相关路径身份。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb; fixture_sha256=1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620; output_sha256=d7a8cf297840918557ec800f34dcd446fb51043f20bd9ce8e785a6d9fe1bb38f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确阻塞发布并核对了主要类型、路径、删除、链接和前后宿主状态问题，但遗漏了可执行位变更这一类越界转换。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=4c059264a7527dcf6082f43bc5cacdf327f947505e6d5f9721fd10e71b64fdcb; fixture_sha256=1013313f9177f2e4b64118a15325ba0a4da0ec26b6c32604368f1f754b57e620; output_sha256=bd8aa10d5035bba4781a98998e00c9fc2ff5e7a82fcb88eb4d9e19afef3cbb25; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样阻塞发布并发现主要风险，但作为比较基线也遗漏了可执行位变更及后续 committed candidate/handoff 边界要求。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- rejects_every_unauthorized_transformation: 未明确将 catalog-items.md 的可执行位变更列为授权边界违反项。
- Next: 重新生成并校验一致的候选捕获，明确审查可执行位、类型、删除、重命名和链接目标。
- Next: 确认目标发布版本；形成 candidate 与 handoff 后重新验证相同授权边界。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
