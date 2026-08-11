# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-017-scope-guard-unenabled-general`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-17-scope-guard-unenabled-general`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `0d80b9dec86a17116de51354d4b9cf60c96709a915b3655bf693ad2757979eb9`
- Repository HEAD: `e2d0e3e00078c297194828182b4d6445ecbb492d`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `c658e8351498435bd5246b692fbf8a3a6d40caa45d6998b37785e6522243068b`
- Skill overlay SHA-256: `2a468ab17f03f6a66d3f4083da133fc1c0904ede59404e5cd9fe19f49032d89d`
- Judge schema SHA-256: `c5629d3608d1f142562d32ed4b435e3d2c557d9aa8b1c8b5f72fce35ca63e9a2`
- Eval definition SHA-256: `77919d03beb71f1c0296e025206c5b6fb953076c10f7d13677b7bc883247a380`
- Metadata SHA-256: `2ce1f415b7c74fc286f7e511f27b1cc3bd8a9f0552bedf14bfd291205fc28318`
- Executor SHA-256: `a4bdc62ab64b81e98e050718e983a49fe8219a833420e63178b355862f4129df`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `scope_guard_stops_general_request` | PASS | with_skill 输出说明该请求是整理本机 ~/Downloads 文件、当前目录未启用项目工作流，并明确“不执行”；未输出 request_type、change_tier、selected_owner 或任何下游文档/handoff。git 与 delivery_snapshot 均无变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0d80b9dec86a17116de51354d4b9cf60c96709a915b3655bf693ad2757979eb9; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=df662982d6c7d7b7b37efdffa10a569d3f5eb0fb462fffc9236b75e247ce3a2c; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别为范围外的本机通用文件处理请求，简短说明后停止且无工作流或文件变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=0d80b9dec86a17116de51354d4b9cf60c96709a915b3655bf693ad2757979eb9; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=5097d1af9d4f085e64bf32a054d60768bfccac61352cfa4971493d83e28c1dbe; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 以权限/工作区限制为由拒绝访问，并提出后续整理建议；未进入 PM 工作流。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
