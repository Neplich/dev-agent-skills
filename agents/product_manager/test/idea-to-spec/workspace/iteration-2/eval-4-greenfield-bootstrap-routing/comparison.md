# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `idea-to-spec`
- Eval: `eval-004-greenfield-bootstrap-routing`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/idea-to-spec/workspace/iteration-2/eval-4-greenfield-bootstrap-routing`.
- Identity schema: `2`
- target_skill_sha256: `62f7a88900be8a0aae1af9e34b28dc32abd76006ca95f89107567b68f5780813`
- eval_definition_sha256: `8e113c060d578c3d672e422d3214efcf8ef5f3dc4a4d591f825ce19450902064`
- metadata_sha256: `af73e5b9a9192eb83b6e3ca2d5cae73fe4fd2b14b49ac401fa1a5f606db4bd6c`
- fixture_sha256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `333e583cf4bb11484925925c3c083e2f295eb8670599a3d04a51d2b749c8668a`
- Source lock SHA-256: `c58f04d32c2ca3a22aec96f7ee027af648da5971453d2a5553d7ab2cd9272551`
- Prompt SHA-256: `47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c`
- Repository HEAD: `60a4b3602dc07f3f6683a8873529bbdba6f8d27d`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `7b19869a4835a1feeb491815cac7af7bde071247819525989c10dbfbc0acd2f7`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `assertion_1` | PASS | With_skill 明确列出 project_status=empty、tech_stack=pending、existing_docs=[]，且没有给出初始化命令。 |
| `pm_first_lane` | PASS | With_skill 明确给出 lane=greenfield-discovery。 |
| `pm_first` | PASS | With_skill 进入需求确认与 PRD/DECISIONS 收敛路径，并明确不初始化项目；未执行脚手架命令。 |
| `assertion_4` | PASS | With_skill 明确列出 PRD/DECISIONS 为待落地文档，并将整理 PRD 骨架作为下一步。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=720b2ab185e9174b5698a0211e0c7db43ba367274fc7924364cce118b062d0b7; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 先盘点空工作区并选择 greenfield-discovery，保持 PM-first，提出产品定位决策点，等待确认后继续形成 PRD/DECISIONS 文档。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=47f636262c26b6b99c860d59ef8342eebebbd60397f192a193020f82c13fa42c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=cbd3f812d65fdf226f19f9a3809bb277955bf4676100e36e7deac6e77aad3f6a; snapshot_sha256=01347cab9c5d5dc29c8967774a129fde936c28b20736ee4ac1a18dd25c9e739b
- Behavior: 未先展示空工作区检测或 PM lane，直接交付了 PRD.md；虽未初始化项目，但跳过了需求确认阶段。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
