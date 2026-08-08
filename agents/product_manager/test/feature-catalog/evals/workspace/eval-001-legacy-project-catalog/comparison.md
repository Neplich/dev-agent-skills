# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-001-legacy-project-catalog`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-001-legacy-project-catalog`.
- Fixture SHA-256: `fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554`
- Prompt SHA-256: `35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `807b576a5130a49581d58f258e32f9a7f916850f2f335e3a48ede3a7886a942b`
- Skill overlay SHA-256: `96eaf3768827f13d232245de107b17f5e814bef969da3eb231f62d9287d9d070`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `6316196cbc0024d8a369162c20842d191078adb23f3f59cfbc5541923081da5e`
- Metadata SHA-256: `aa9b419ec00ff2ce5f9c2775fc1e620cf1eb45a8d316e5adf573b14f5b74c3e2`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `draft_before_formal_docs` | PASS | with_skill 明确标记为“功能目录草案（待确认）”，git_status 和 git_diff 均为空，且输出说明尚无正式 docs/pm 文档。 |
| `evidence_and_confidence` | PASS | 三个候选条目均在总览表中标记 high 置信度，并提供与原始 fixture 相符的 API、路由、服务、数据模型、后台任务、测试或 README 文档证据。 |
| `business_capability_naming` | PASS | 候选名称为“客户身份认证与会话续期”“订单创建与查询”“订单状态变更通知”等业务能力名称；代码路径仅作为证据出现。 |
| `open_questions_present` | PASS | 每个候选条目均包含“待确认问题”，明确指出认证、状态变更、邮件发送、通知记录及重试等未确定或未实现边界。 |
| `confirmation_gate` | PASS | 输出结尾请求维护者确认三个 feature_path，并说明确认后才写入正式目录；未提前 handoff 给 prd-gen 或 trd-gen。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=4d3eaf70234ac0964a6bd39c1fb4c0dd4ef89428de20110ed256aca210f59dc8; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 产出待确认的业务能力功能目录草案，逐项提供证据、置信度和待确认问题，并以 feature_path 确认请求收尾；未产生文件变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=35596dbabe7e81489226405d1f4c2c66e846066917c0ef619ae5a1e2332558a2; fixture_sha256=fa295db805350878180b0b5d2e6fc6d21188b2866a3c61c345e1f1875b201554; output_sha256=aca860cbc520da14670de2b6fa786b92b66ab0e8ab5a2e195c75c6feab58d851; snapshot_sha256=0538798cb2d752d059e4fc9214534c833817d714e75adb64cdcafc32e31cd466
- Behavior: 输出了未确认的正式目录文件 docs/功能目录.md，未采用待确认草案和 feature_path 确认门禁。
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

# Eval Result: eval-001-legacy-project-catalog

## Latest Fresh Evaluation — 2026-08-07

- Model: `gpt-5.6-luna`, `model_reasoning_effort="medium"`
- Fixture: HEAD `47adbbc9`; baseline and with-skill input manifests matched exactly.
- Isolation: baseline completed and its root was deleted before any with-skill root was created; the judge used a third independent root.
- Behavior result: PASS — 5/5 assertions passed.
- Coverage result: FULL — all 5 assertion scenarios were exercised.
Overall result: PASS

### Assertion Results

- `draft_before_formal_docs`: PASS — produced a visibly pending draft and wrote no formal catalog or PRD.
- `evidence_and_confidence`: PASS — used the actual route/API/service/model/job/test evidence and conservative confidence.
- `business_capability_naming`: PASS — grouped findings into user-facing authentication, order management, and status notification capabilities.
- `open_questions_present`: PASS — recorded unresolved ownership and boundary questions.
- `confirmation_gate`: PASS — stopped at maintainer confirmation before formal docs or handoff.

### With-Skill / Baseline Comparison

The with-skill lane produced an evidence-first, low-confidence draft without durable writes. The baseline wrote `docs/功能目录.md` before confirmation and lacked the same gate discipline.

### Failures / Next Steps

- No with-skill assertion failures and no coverage gaps.

### Runtime Artifact Policy

- Fresh evidence remains under `/private/tmp/pm-spec-fresh-evidence.GpQ6yO/eval-001-legacy-project-catalog/` and is not committed.

---

The sections below are historical records from earlier runs.

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-001-legacy-project-catalog`
- Workspace: `workspace/eval-001-legacy-project-catalog`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: HEAD `a452319`; Node.js commerce backend with no PM docs and shallow-scan evidence for authentication, orders, notifications, model, and tests.
- Fresh run: `2026-08-03 11:58:20 +0800`
- Runtime directory: `tmp/eval-runs/issue-198-brd/pm/eval-001-legacy-project-catalog/`

## Latest Result

- Behavior result: PASS — all 5 assertions passed.
- Coverage result: FULL — 5/5 assertion scenarios were exercised; no `NOT EXERCISED` items.
Historical result: BLOCKED
- Blocking reason: eval 定义已按 issue #234 修复泄漏（prompt/fixture 不再向 baseline 泄漏 skill 规则），本结论基于旧契约（泄漏版 eval 定义），待重跑验证。


## Assertion Results

- `draft_before_formal_docs`: PASS — produces a visibly pending draft and writes no catalog or PRD.
- `evidence_and_confidence`: PASS — each candidate includes actual evidence categories, related paths, and conservative confidence.
- `business_capability_naming`: PASS — names authentication, order management, and order status notifications as business capabilities.
- `open_questions_present`: PASS — records ownership and boundary uncertainty instead of presenting guesses as facts.
- `confirmation_gate`: PASS — stops with one maintainer confirmation request before formal docs or handoff.

## With-Skill Behavior

The response used the documented lightweight scan because no Project Profile exists, grouped evidence by business capability, capped shallow-scan candidates at low confidence, and stopped before writing `docs/pm/FEATURE_CATALOG.md`. After confirmation, the spec handoff is directly to PRD/DECISIONS and later Engineer TRD; no BRD step remains.

## Fresh Without-Skill Baseline

The baseline was newly generated in this run from the same prompt and fixture, without reading or applying the target skill, Product Manager README, internal instructions, or historical comparison. It found the same broad modules but organized them more mechanically, used inconsistent confidence, and lacked the explicit maintainer confirmation gate.

## Failures

- No assertion failures or baseline blockers.
- BRD removal caused the expected handoff-chain difference, not a regression: confirmed catalog entries now proceed directly to PRD/DECISIONS.

## Next Steps

- Keep this eval as coverage for legacy feature discovery and the BRD-free confirmation-to-spec handoff.

## Runtime Artifact Policy

- Fresh responses and judge notes remain under `tmp/eval-runs/issue-198-brd/pm/eval-001-legacy-project-catalog/` and are not committed.
