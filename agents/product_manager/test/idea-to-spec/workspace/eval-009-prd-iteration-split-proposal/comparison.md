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
- target_skill_sha256: `62f7a88900be8a0aae1af9e34b28dc32abd76006ca95f89107567b68f5780813`
- eval_definition_sha256: `8ef466ccd13d937453c02f105817ced47839fb573011ea1ee300be62facb6b71`
- metadata_sha256: `ae189abbce9ec160b22d49ab4f79a0a7a8f521d1a6e2046930669caf75d7dab0`
- fixture_sha256: `cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `9c9a733fc3c46fd3cb1cdea794218e66a7a987137063c1a3c970e8e9386d1a58`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `ae03344941a8a5473fce84f07af68d8bb42c4c4dd8dbaf557b909886adf20c98`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7b19869a4835a1feeb491815cac7af7bde071247819525989c10dbfbc0acd2f7`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `applies_requested_change` | NOT_EXERCISED | 未产出更新后的 PRD；候选正确停在需要用户确认的拆分门槛，因此实际应用变更尚未可执行。 |
| `detects_l2b_signals` | PASS | 明确给出 independent_domain_count=3 和 combined US/FR rows=18，并判定 l2b_assessment=triggered。 |
| `presents_split_proposal` | PASS | 给出三个子 feature_path、章节迁移映射，以及 Engineer、Design、QA、DevOps、Security 五类下游影响清单。 |
| `waits_for_confirmation` | PASS | 明确要求确认接受或拒绝拆分，并说明确认前不能直接写入 PRD；无 git mv 或新建子路径文档证据。 |
| `rejection_keeps_current_flow` | PASS | 明确说明拒绝拆分时保持 notification-center 当前路径，直接改为事件驱动并按正常版本迭代。 |
| `body_consolidation` | NOT_EXERCISED | 未产出更新后的 PRD 正文；该后续步骤依赖用户确认，尚未执行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ae03344941a8a5473fce84f07af68d8bb42c4c4dd8dbaf557b909886adf20c98; fixture_sha256=cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997; output_sha256=096351dc619d34011011e8bd36f4dd5830a22e94e1fecb9e13fdeea548877008; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别到 L2b 信号，输出完整拆分提案并等待用户确认；未执行 PRD 更新。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=ae03344941a8a5473fce84f07af68d8bb42c4c4dd8dbaf557b909886adf20c98; fixture_sha256=cda1a0661ddb58fa697ce0a283dc50943986240370fdcd97782d5714af75a997; output_sha256=32873913c60f965f3ad771a005533c350586228564a73b0e98370e51e75a34a1; snapshot_sha256=31a4e197bc25f40bf845517ec0d0636069b31c0ee1943a849aae92836beb70a1
- Behavior: 直接更新 PRD 为事件驱动方案并产生工作区修改，但未展示拆分确认流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 等待用户确认接受或拒绝 L2b 拆分。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
