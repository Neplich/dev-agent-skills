# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-009-prd-iteration-split-proposal`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997` from `agents/product_manager/test/idea-to-spec/workspace/eval-009-prd-iteration-split-proposal`.
- Identity schema: `2`
- target_skill_sha256: `a5ef9beb8352f2c9b4cfde83ccd9caf0accd15d632ffa2d78214f3c51045041a`
- eval_definition_sha256: `8ef466ccd13d937453c02f105817ced47839fb573011ea1ee300be62facb6b71`
- metadata_sha256: `ae189abbce9ec160b22d49ab4f79a0a7a8f521d1a6e2046930669caf75d7dab0`
- fixture_sha256: `cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `9c9a733fc3c46fd3cb1cdea794218e66a7a987137063c1a3c970e8e9386d1a58`
- Identity migration: **MIGRATED_WITHOUT_MODEL_RERUN**
- Identity migration source commit: `4cca644d64c599531542e66ba5a9210c5c6bf40c`
- Identity migration audit: `docs/engineer/repository-governance/eval-scenario-isolation/eval-identity-v2-migration-audit.json`
- Repository HEAD: `7ac19d358ca18ef7b2d109aeec17239bc9d0f4c0`
- Repository worktree state: **DIRTY**
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `applies_requested_change` | NOT_EXERCISED | 未写入 PRD；候选明确说明“当前未写入文件”，且没有 delivery_snapshot。 |
| `detects_l2b_signals` | PASS | 明确列出 3 个独立领域、约 66 行、18 个 US/FR 表格行，并判定 l2b_triggered。 |
| `presents_split_proposal` | PASS | 提供了子 feature_path 树、章节迁移映射，以及 Engineer、Design、QA、DevOps、Security 影响清单。 |
| `waits_for_confirmation` | PASS | 明确要求用户确认；确认前保持当前 PRD 不变，未移动文件或创建子文档。 |
| `rejection_keeps_current_flow` | PASS | 明确说明拒绝拆分时沿用当前 feature_path，并继续写入事件驱动策略的 1.4.0 增量更新。 |
| `body_consolidation` | NOT_EXERCISED | 尚未产出更新后的 PRD 正文；该步骤等待用户确认后才能执行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ae03344941a8a5473fce84f07af68d8bb42c4c4dd8dbaf557b909886adf20c98; fixture_sha256=cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997; output_sha256=aac4f6fd624c7ab359bf49bf1c7b8279bb2007a7bc54635862275c3f189e331d; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了 L2b 信号并提出完整拆分提案，等待用户确认；尚未写入 PRD。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ae03344941a8a5473fce84f07af68d8bb42c4c4dd8dbaf557b909886adf20c98; fixture_sha256=cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997; output_sha256=65820e993f1ddb167c588a1ce747c70e111255097d0651920dae922d638ecbab; snapshot_sha256=8611ac84fd906785def520891f6fb18cb2693a0277c461a985ee398e925e1e4d
- Behavior: 直接更新了 PRD，但未处理 L2b 拆分提案与确认流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 获得用户确认后，按确认决策更新或拆分 PRD，并完成正文校验。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
