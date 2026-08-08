# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-002-existing-project-update`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `4a0c4f24287b030b034f66b2e9e0787c5b6e4b2e4a40435cb46ef2275f03923a` from `agents/product_manager/test/idea-to-spec/workspace/iteration-1/eval-2-existing-project-update`.
- Fixture SHA-256: `4a0c4f24287b030b034f66b2e9e0787c5b6e4b2e4a40435cb46ef2275f03923a`
- Prompt SHA-256: `6aaa57677f60fb06006df08dac712b315ee95015f718fd4450b32d594a455441`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9c3b136c6958582b2c5c3d552759bbe4fd3ef24876075804e91c5b21980a34af`
- Skill overlay SHA-256: `e4cc003a0e06320ef354c6c9cdbebb2b75980ec8b23ae530ac78b0667fab31da`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `2eb26345c0320238f13795dd231ba4c205d452d230de64d35bcf4cc4acb002f8`
- Metadata SHA-256: `705e055f0c1e2ecaf46061084a80e87ae854a0054e6c7225c7ef5f20736382be`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `update` | PASS | with_skill 明确称“更新现有三份文档”，并把 PRD、DECISIONS、TRD 从 Approved 更新为 Proposed，符合已有设计迭代场景。 |
| `delta_blast_radius` | PASS | with_skill 在更新建议前概括了通知写入链路、服务端、客户端、API、未读状态、运维和发布流程等影响范围；其 git_diff 也显示这些内容被写入三份文档。 |
| `assertion_3` | FAIL | with_skill 实际采用了增量更新现有三份文档，但输出没有推荐 change-impactor 或对应 iteration 技能；只提出了文档更新和新增文档建议。 |
| `assertion_4` | PASS | with_skill 明确指出需更新 docs/pm/notification-center/PRD.md、docs/pm/notification-center/DECISIONS.md 和 docs/engineer/notification-center/TRD.md，并列出事件契约、ADR、Runbook、测试计划等新增文档类型。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6aaa57677f60fb06006df08dac712b315ee95015f718fd4450b32d594a455441; fixture_sha256=4a0c4f24287b030b034f66b2e9e0787c5b6e4b2e4a40435cb46ef2275f03923a; output_sha256=b64bee7d9e36c2153c906b0b7890c4d55a252b4b76046dab4860cfdd0087b8f6; snapshot_sha256=8c18b60cbe2b8d635e7bf4577e63372706444f2bd88df37208a12c6d0ad6bce5
- Behavior: 实际增量修改了 PRD、TRD、DECISIONS 三份现有文档，补充事件驱动架构、可靠性、回滚和验收内容；未明确推荐 iteration 技能。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=6aaa57677f60fb06006df08dac712b315ee95015f718fd4450b32d594a455441; fixture_sha256=4a0c4f24287b030b034f66b2e9e0787c5b6e4b2e4a40435cb46ef2275f03923a; output_sha256=b1c3e5f876b32b452c6021afa31da1caab60c5f6a9616f87ebcbd8caf689b87e; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 基线输出分析了影响范围并建议修改 PRD.md、TRD.md、DECISIONS.md，但未呈现对应实际文档变更。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未推荐 change-impactor 或对应 iteration 技能，未满足 assertion_3。
- Next: 在输出中明确推荐 change-impactor 或对应 iteration 技能，并说明应基于现有文档做增量更新。

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

# Eval Result: eval-002-existing-project-update

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; fresh paired manifests matched exactly.
- Behavior result: PASS — 4/4 assertions passed.
- Coverage result: FULL — all 4 assertion scenarios were exercised.
Overall result: PASS

### Assertion Results

- `update`: PASS — identified the request as `existing-project-update` against approved PRD/TRD/DECISIONS.
- `delta_blast_radius`: PASS — described the delivery delta and affected behavior/documents first.
- `assertion_3`: PASS — recommended `change-impactor` plus targeted iteration, not regeneration.
- `assertion_4`: PASS — named the notification-center PRD, DECISIONS, and Engineer TRD paths.

### With-Skill / Baseline Comparison

The with-skill response stayed read-only and produced a delta-oriented update sequence. The baseline also produced a useful impact analysis but directly rewrote the three documents; it remained comparison evidence only.

### Failures / Next Steps

- No with-skill assertion failures and no coverage gaps.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-002-existing-project-update/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-002-existing-project-update`
- Workspace: `workspace/iteration-1/eval-2-existing-project-update`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; approved notification-center PRD, DECISIONS, and Engineer TRD covering polling and the confirmed event-driven migration direction.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-002-existing-project-update/`

## Latest Result

- Behavior result: PASS — all 4 assertions passed.
- Coverage result: FULL — 4/4 assertion scenarios were exercised; no `NOT EXERCISED` items.
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `update`: PASS — classifies the request as `existing-project-update`.
- `delta_blast_radius`: PASS — states the delivery-model delta, affected behaviors, compatibility, rollback, tests, and documents before updates.
- `assertion_3`: PASS — prefers `change-impactor` and targeted iteration instead of regeneration.
- `assertion_4`: PASS — names the affected DECISIONS, PRD, Engineer TRD, and later QA paths.

## With-Skill Behavior

The response preserved the confirmed hybrid transition and rejected permanent polling-only history, then routed PM changes to targeted PRD/DECISIONS iteration and Engineer-owned TRD changes to `engineer-agent:trd-gen`. The retired BRD layer was absent; business delta and decisions flow directly into PRD and DECISIONS.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It identified the main documents and preferred incremental edits, but did not consistently apply `change-impactor`, `prd-iteration`, Engineer ownership, or decision-history preservation.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused no behavioral regression.

## Next Steps

- Keep this eval as coverage for delta-first impact analysis and targeted PRD/DECISIONS updates.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-002-existing-project-update/` and are not committed.
