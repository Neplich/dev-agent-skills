# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `feature-catalog`
- Eval: `eval-004-catalog-mapped-billing-feature`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa` from `agents/product_manager/test/feature-catalog/evals/workspace/eval-004-catalog-mapped-billing-feature`.
- Fixture SHA-256: `dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa`
- Prompt SHA-256: `18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `272c84e241c5d52534922fccf2bc6732492a0d70c9f6e2ab8dc1eff2533f7b0c`
- Skill overlay SHA-256: `c7fd56e26e53c8ea32b598e8f4e06588e28aee376ed79eb9822ecf37e3099222`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `8d7030970f6fab5f1056baaa7f97792f12e093b11e3211055d5ae790cf0d3bc2`
- Metadata SHA-256: `b6e639db89ad7dc9c01b74ff5037844027a7f93b1a684864779b0328b14ee4bc`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | 候选输出声称已读取 required doc，但锁定证据没有记录实际读取顺序或遍历范围，无法证明该隐藏过程要求。 |
| `verifies_against_code` | PASS | 明确引用 docs/site/api/billing.md，说明文档声称月付和年付；同时引用 src/billing/service.txt，指出代码仅声明支持 monthly，并将年度计划列为待核实项。 |
| `treats_unverified_as_low_trust` | PASS | 明确指出 last_verified_version: unverified，并据此将年度计划视为待核实项，且将代码复核作为实现结论依据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99; fixture_sha256=dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa; output_sha256=4194ff17fe73fb00e88225fd419432bb0f26a0c91b2c99d0c5288633bc0b5268; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 产出带证据、置信度和待确认事项的计费功能目录，正确区分代码事实与未验证文档声明。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=18727fc23cb0e6511e466aafaee8dc2b3d50aa38834ef79db9cd3a99a2690d99; fixture_sha256=dbc5593a346cec17c758e623e41d968d8b062bb60f1c6687047b79f186d5a5fa; output_sha256=54d0923311f5c574b8480cb47ae950dd7c630ce8f7dbfa9f009a52e2e41b42c4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 也识别了月付与创建订阅，并发现年付仅为未验证文档声明，但未形成同等结构化的功能目录和后续确认流程。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
