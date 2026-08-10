# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `competitive-brief`
- Eval: `eval-002-battlecard-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `580131b9961f88dece682fec7455c21af018b400a3742eb37ae40114374aeae0` from `agents/product_manager/test/competitive-brief/evals/workspace/eval-002-battlecard-mode`.
- Fixture SHA-256: `580131b9961f88dece682fec7455c21af018b400a3742eb37ae40114374aeae0`
- Prompt SHA-256: `e54579ea27411964e085efe779b45a83156d8efbd3908b273d472904914675a2`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `64a375a1a490fa251e9b252ef3a7787f55ca6a4fd08e5d401228a899b274ed39`
- Skill overlay SHA-256: `c1341cebf983202b3c2101489252c70818305b548c111af4817c833b2dd4164f`
- Judge schema SHA-256: `e42897afb6931d7065c6aa9ac71e607d574f057396cd3a30a0419c210f3be3cb`
- Eval definition SHA-256: `a7454ae2eccc665064a08c31fc99de3b8f0a596f72811f2e5035b12f267e9fe8`
- Metadata SHA-256: `be38b1b419460352b11de0cc1468d57c031f7575d697be3bf617760a456d47f3`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `battlecard_fields` | PASS | Locked delivery_snapshot contains Linear and Jira battlecards with Quick Overview, Their Pitch, Strengths, Weaknesses, Objection Handling, Landmines to Set/Defuse, and Win/Loss Themes. |
| `no_full_brief` | PASS | The locked output is structured as battlecards and does not include a full competitor-brief chapter structure. |
| `evidence_boundary` | PASS | The locked file states the research date and evidence boundary, identifies source categories, and marks unavailable details as 假设 or 待验证. |
| `no_battlecard_offer` | PASS | The locked final response delivers the battlecard and does not ask whether to create one later. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e54579ea27411964e085efe779b45a83156d8efbd3908b273d472904914675a2; fixture_sha256=580131b9961f88dece682fec7455c21af018b400a3742eb37ae40114374aeae0; output_sha256=631fd284e19e45e698d2667fd059bd21b2c78fb2d6595650d9e2f779ccbf9f4d; snapshot_sha256=f3c72f2af5a822ea88f36c6ada3aa4125155dcdb1f2d7692d21c92b7082dc8f7
- Behavior: Produced a consolidated Linear/Jira battlecard with the required fields and explicit evidence-boundary markings.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=e54579ea27411964e085efe779b45a83156d8efbd3908b273d472904914675a2; fixture_sha256=580131b9961f88dece682fec7455c21af018b400a3742eb37ae40114374aeae0; output_sha256=7ae60d198f1deaec6fee87630cbc9593f285ff58fb4a94371e42612f4c8b49d4; snapshot_sha256=bb33aadcdaea49ca0db679925408bb7b2c7c50923699816b2f4486459f04ba20
- Behavior: Produced two sales one-pagers with useful research summaries, but without the required battlecard field structure.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
