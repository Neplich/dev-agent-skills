# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-003-monorepo-scope-clarification`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c414562285f1c022777b6125d75fb56cbbd795475c5bf83bc97b862a14abc6d3` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-003-monorepo-scope-clarification`.
- Fixture SHA-256: `c414562285f1c022777b6125d75fb56cbbd795475c5bf83bc97b862a14abc6d3`
- Prompt SHA-256: `592a8806afad3bd6928b7ec27d5b10ebdae9bb0b86dd82cabdc2f71dc5d37c25`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c7dc67ac03b6fbf2bf69bb7af239cc79636a61220df238e51a6c8f891a2b2bbf`
- Skill overlay SHA-256: `5fabe64a432e7077b010b055323ac846ade69c047e7f21a1ce71459e61d31a42`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `221668759d9b3f1847f350986e591b6defbd71cd5f83a296b96e5736de8e7ceb`
- Metadata SHA-256: `8aa1f1f970ba708ba203aa964e23b048bfd278c5cd0d04094602a65c55ad9476`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocked_on_scope` | PASS | With-skill 输出识别出 apps/web、apps/admin、services/api 三个 workspace，并要求先确认功能目录覆盖范围，形成待澄清状态。 |
| `minimal_clarification` | PASS | With-skill 只提出一个范围澄清问题，并用三个范围选项具体化，没有展开多问题清单或冗长问卷。 |
| `no_fabricated_catalog` | PASS | With-skill 未输出功能目录、FEATURE_CATALOG.md 或 PRD；git_status、git_diff 均为空。 |
| `no_parallel_top_level` | PASS | With-skill 仅将 workspace 路径作为范围选项列出，没有将其断言为新的并列顶层 feature_path。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=592a8806afad3bd6928b7ec27d5b10ebdae9bb0b86dd82cabdc2f71dc5d37c25; fixture_sha256=c414562285f1c022777b6125d75fb56cbbd795475c5bf83bc97b862a14abc6d3; output_sha256=482eb340816ae9518042e59e22abf9cf8daf252c1275334670bb489a669cae0a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别三个 workspace，在范围未明确时暂停并请求单一范围澄清；未产生文件变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=592a8806afad3bd6928b7ec27d5b10ebdae9bb0b86dd82cabdc2f71dc5d37c25; fixture_sha256=c414562285f1c022777b6125d75fb56cbbd795475c5bf83bc97b862a14abc6d3; output_sha256=6e5099cf95b75f0e8f5644fafb83b961f567b1a1ddfb6f7ba76629d1a6e5f030; snapshot_sha256=0aa8b8e04aa5210da35e90d8c801a73add70a481a4d791f1e0103c5fca6d7431
- Behavior: 直接声称已建立功能目录并产生 README.md 与 docs/FEATURES.md 变更。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-003-monorepo-scope-clarification`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c414562285f1c022777b6125d75fb56cbbd795475c5bf83bc97b862a14abc6d3` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-003-monorepo-scope-clarification`.
- Fixture SHA-256: `c414562285f1c022777b6125d75fb56cbbd795475c5bf83bc97b862a14abc6d3`
- Prompt SHA-256: `592a8806afad3bd6928b7ec27d5b10ebdae9bb0b86dd82cabdc2f71dc5d37c25`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `807b576a5130a49581d58f258e32f9a7f916850f2f335e3a48ede3a7886a942b`
- Skill overlay SHA-256: `96eaf3768827f13d232245de107b17f5e814bef969da3eb231f62d9287d9d070`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `221668759d9b3f1847f350986e591b6defbd71cd5f83a296b96e5736de8e7ceb`
- Metadata SHA-256: `8aa1f1f970ba708ba203aa964e23b048bfd278c5cd0d04094602a65c55ad9476`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `blocked_on_scope` | FAIL | with_skill 输出直接称“已按整个 monorepo 盘点”，列出 web、admin、api，但没有因范围未指定而 blocked 或请求先确认纳入哪些 workspace。 |
| `minimal_clarification` | FAIL | 末尾问题询问接受 customer-account 还是拆分子功能，而非先确认 workspace 范围；正文还列出两个 open_questions。 |
| `no_fabricated_catalog` | PASS | 输出明确称为“功能目录草案（待确认）”，git_status/git_diff 为空，delivery_snapshot 为空，未写 docs/pm/FEATURE_CATALOG.md 或生成 PRD。 |
| `no_parallel_top_level` | PASS | 仅为 web 候选提出 suggested_feature_path: customer-account；明确表示 admin 和 api 没有足够证据建立具体功能项，未将三者猜测为并列顶层 feature_path。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=592a8806afad3bd6928b7ec27d5b10ebdae9bb0b86dd82cabdc2f71dc5d37c25; fixture_sha256=c414562285f1c022777b6125d75fb56cbbd795475c5bf83bc97b862a14abc6d3; output_sha256=899d8a82351ed93758be9fb7a66ae7b456e8b8cd17814d9fccd928afbb0a742d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别出三个 workspace 并保留候选/低置信度标记，但假定盘点整个 monorepo，未先澄清范围，且提出了超出最小范围确认的问题。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=592a8806afad3bd6928b7ec27d5b10ebdae9bb0b86dd82cabdc2f71dc5d37c25; fixture_sha256=c414562285f1c022777b6125d75fb56cbbd795475c5bf83bc97b862a14abc6d3; output_sha256=e141ad9fa479f2a9d0203fd1a57f30e6a651d87142259694ea17ea0af0bbba6b; snapshot_sha256=47ba5c399a76724491e423ac6c6ba01022560f61aadec0d17ad4828814d8e750
- Behavior: 直接声称已建立功能目录并产生 docs/feature-catalog.md 与 README 修改，未请求范围澄清。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未因请求范围不清而 blocked 或先确认 workspace 范围。
- with_skill 的澄清问题聚焦功能拆分和路径命名，而非最小范围澄清。
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

# Eval Result: eval-003-monorepo-scope-clarification

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; fresh paired manifests matched exactly.
- Behavior result: PASS — 4/4 assertions passed.
- Coverage result: FULL — all 4 assertion scenarios were exercised.
Overall result: PASS

### Assertion Results

- `blocked_on_scope`: PASS — detected independent web, admin, and API workspaces and stopped for scope clarification.
- `minimal_clarification`: PASS — asked one scope question only.
- `no_fabricated_catalog`: PASS — wrote no formal catalog or PRD.
- `no_parallel_top_level`: PASS — did not guess workspace names as confirmed feature paths.

### With-Skill / Baseline Comparison

The with-skill response stopped at the smallest scope gate. The baseline wrote a root `FEATURES.md` despite the unresolved scope.

### Failures / Next Steps

- No with-skill assertion failures and no coverage gaps.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-003-monorepo-scope-clarification/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-003-monorepo-scope-clarification`
- Test case: monorepo-scope-clarification
- Workspace: `workspace/eval-003-monorepo-scope-clarification`
- Latest result: PASS - fresh Codex subagent validation completed on 2026-07-05
- Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture: pnpm monorepo with independently deployed `apps/web`, `apps/admin`, and `services/api`, with no PM docs
- Expected output: blocked on scope, ask exactly one minimal scope clarification question, and avoid confirmed catalog or guessed parallel top-level feature paths.

## Assertions

- `blocked_on_scope`: identify multiple workspaces and unresolved scope
- `minimal_clarification`: ask one smallest clarification question
- `no_fabricated_catalog`: do not fabricate a confirmed catalog or PRD
- `no_parallel_top_level`: do not guess each workspace as a settled top-level feature path

## With Skill

- The `feature-catalog` edge-case rule treats undetermined monorepo scope as `blocked`.
- The fixture clearly exposes three independently deployed surfaces: `apps/web`, `apps/admin`, and `services/api`.
- The correct with-skill behavior is to ask one minimal question, such as whether to catalog `apps/web`, `apps/admin`, `services/api`, or all of them, and stop.
- It does not create `docs/pm/FEATURE_CATALOG.md`, generate PRDs, or present guessed top-level feature paths as confirmed conclusions.

## Without Skill / without_skill Baseline

- The baseline read the eval item and fixture before target skill docs. A generic response could eagerly inventory all packages and produce a catalog despite unresolved scope.
- It may ask several discovery questions or treat each workspace name as a confirmed top-level feature path.

## Failures

- None. The current `feature-catalog` protocol satisfies the blocked, single-question, no-fabrication, and no-parallel-top-level assertions.

## Next Steps

- Keep this eval as coverage for monorepo scope clarification.
- Re-run fresh validation if monorepo scope or blocked-state rules change.

## Runtime Artifacts Policy

- No runtime artifacts were created or committed. Transcripts, verdicts, outputs, timing, and diagnostics must remain outside git; the durable result is this `comparison.md`.
