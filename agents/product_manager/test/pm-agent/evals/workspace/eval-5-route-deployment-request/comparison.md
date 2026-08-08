# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-005-route-deployment-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-5-route-deployment-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `847ec25f3bf19681577a3386dfc21c378712f63dee7629dde5750b16901ab4e4`
- Skill overlay SHA-256: `85498141fecd6ca653a495454d16dd5a8f8fa77675af6eb45d6d223d0cab1fbd`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `73a2b58c1c65bf56a5f6d6f35f003c86e432caed7b530c34cf851322050e2633`
- Metadata SHA-256: `d17a05b229136107ac1e50142856979a9ae9f563cdb19b940e4810dadda79e1c`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **PARTIAL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_deployment` | FAIL | The with_skill output discusses 上线前检查 and DevOps but never classifies the request as `deployment`. |
| `repo_wide_scope_allowed` | NOT_EXERCISED | The locked evidence contains no scope or feature-path decision, so this hidden/process requirement cannot be proven. |
| `devops_handoff_packet` | NOT_EXERCISED | The candidate leaves DevOps handoff blocked pending user-provided project and build information; the later handoff step is not reached. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=78b7486086915c4f400ddab0770025ed4418903525681699ed61430d69ef39bf; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly identified the empty-repository blocker and requested missing project/build context, but omitted the explicit deployment classification.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=8fe2ca2af035e6220fba287078fd350aa8d7b1e222b19a25ef3c5dbcdfc5b8d3; snapshot_sha256=93ea4d185e1a05d48d8cc06e1e3dbad32c626d5cdebd29103b06a50302c8fb61
- Behavior: Created CI and launch-checklist files, but did not provide the requested workflow classifications or handoff context.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- request_type_deployment: the required `deployment` classification is absent from the with_skill result.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-005-route-deployment-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-5-route-deployment-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `847ec25f3bf19681577a3386dfc21c378712f63dee7629dde5750b16901ab4e4`
- Skill overlay SHA-256: `780c8f93b8e6c45b2ccd3c9782ab0565304ee40820ab216a99298b8a0a82b7f1`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `73a2b58c1c65bf56a5f6d6f35f003c86e432caed7b530c34cf851322050e2633`
- Metadata SHA-256: `d17a05b229136107ac1e50142856979a9ae9f563cdb19b940e4810dadda79e1c`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_deployment` | FAIL | with_skill 输出只描述 CI 配置和上线条件，未将请求分类为 `deployment`。 |
| `repo_wide_scope_allowed` | FAIL | with_skill 输出及交付快照未提及允许 `N/A` feature scope，也未提供空的 feature_path_evidence 约定。 |
| `devops_handoff_packet` | FAIL | with_skill 输出未记录 operational goal、environment、release scope、rollback needs 和 risks，且没有 DevOps handoff 记录。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=e710c6fa61464c57143399d31c9bb80d8778a7175d11cef9736e0c0770320834; snapshot_sha256=ba809490178270a55f9d2d8594542cc41ef6f32a0f2dbb766ac7c34e97d3f766
- Behavior: 仅新增基础 CI workflow，并说明空仓库不具备上线条件；未覆盖三项断言要求。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=a020ee5636afd3a32da69287b53bfecb6ca7c3d0e462cab9cb6a88aead256103; snapshot_sha256=e680d41a68905db5029c52a33c63fc73ec6e26f39b9dda049c8449d0f2ff1bfa
- Behavior: 完成较完整的仓库级 CI、预检脚本和发布清单，但未呈现三项所需的分类、scope 约定或 DevOps 交接上下文。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未识别 deployment 类型。
- with_skill 未说明仓库级非 feature 工作可使用 N/A scope 及空 feature_path_evidence。
- with_skill 未在 DevOps handoff 前补齐要求的上下文。
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-005-route-deployment-request`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-5-route-deployment-request`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `b27bdda776386001cc566aec58e87a13d3b1f46246aed8961a6b1f71f6fe7164`
- Skill overlay SHA-256: `4c9723c1beabc3433045321f3b5731004dd2e67877c45ddeed6c79c96a17ba04`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `73a2b58c1c65bf56a5f6d6f35f003c86e432caed7b530c34cf851322050e2633`
- Metadata SHA-256: `d17a05b229136107ac1e50142856979a9ae9f563cdb19b940e4810dadda79e1c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `request_type_deployment` | FAIL | with_skill 输出未将请求明确分类为 `deployment`，仅称应交由 `devops-agent`。 |
| `repo_wide_scope_allowed` | FAIL | with_skill 输出未提及 `N/A` feature scope，也未说明允许空的 feature_path_evidence。 |
| `devops_handoff_packet` | FAIL | with_skill 输出要求用户补充上线目标和检查要求，未先记录 operational goal、environment、release scope、rollback needs 与 risks 再 handoff DevOps。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=4cb4f75df26ff3b378fa1ea527cdefd631e769df7f35948841614865319f1832; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别工作区为空并要求补充仓库、CI 平台和上线信息；未满足三项断言。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=df8dd8d18e0b79f0114ea9e750efb47af7d21bc05b6ea3666cff7d6bae4802fe; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=1a17be704d3e86b6c94d3101438a5f02c8ea3c81e3f4849fadbdf0aba0080867; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别工作区为空并拒绝配置 CI；未体现所要求的分类、scope 或 DevOps 交接上下文。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未明确使用 deployment 类型。
- with_skill 未允许仓库级工作使用 N/A feature scope 和空 feature_path_evidence。
- with_skill 未在交接 DevOps 前记录完整 operational handoff packet。
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

# Eval Result: eval-005-route-deployment-request

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-005-route-deployment-request`
- Workspace: `eval-5-route-deployment-request`

## Test Set / Fixture Version

- Schema: `evals.json` v1.0
- Fixture version: current tracked fixture at the start of the 2026-08-07 run.
- Fresh run: 2026-08-07 (Asia/Shanghai).
- Candidate and independent judge: `gpt-5.6-luna`, `model_reasoning_effort="medium"`.
- Isolation: identical raw prompt and fixture snapshot; all baseline roots were snapshotted in memory and destroyed before any with-skill root; all with-skill roots were destroyed before judging; HOME/CODEX_HOME values matched per eval and were reset for every lane; only `auth.json` was copied into CODEX_HOME.
- Runtime evidence: `tmp/eval-runs/issue-238-pm/fresh-20260807/pm-agent/eval-005-route-deployment-request/`.

## Latest result:

- Behavior result: PASS — determined only from the with-skill lane by an independent judge.
- Coverage result: FULL — 3/3 with-skill assertion scenarios were exercised.
Overall result: PASS

## Assertion Results

- `request_type_deployment`: with-skill **PASS**; without-skill **PASS** — with_skill 最终回复明确 request_type: deployment；without_skill 虽未使用稳定枚举，但语义明确为仓库级 CI/CD 与发布 DevOps。
- `repo_wide_scope_allowed`: with-skill **PASS**; without-skill **FAIL** — with_skill 明确使用 feature_path/feature/parent_feature: N/A、feature_level: repository，且 feature_path_evidence: []；without_skill 未记录 N/A feature fields。
- `devops_handoff_packet`: with-skill **PASS**; without-skill **FAIL** — with_skill 在交接 DevOps 前记录了 CI/发布就绪目标、仓库级 scope、未确定的环境/发布范围/回滚要求及 blockers_risks，并指定 downstream_owner: DevOps；without_skill 未完整记录 operational goal 与 release scope。

## With-Skill Behavior

三项断言均满足。最终回复包含 deployment 分类、仓库级 N/A scope、空证据列表，以及补齐运维上下文后交接 DevOps 的结构化 packet。

## Fresh Without-Skill Baseline

正确识别为仓库级 DevOps/CI/CD 请求，也指出环境和回滚等信息，但未遵循 N/A feature-scope 契约，且交接上下文不完整。

The baseline is comparison evidence only; its outcome does not affect `Overall result`.

## Failures

- without_skill 未使用仓库级非 feature 工作要求的 N/A feature fields。
- without_skill 未完整补齐 operational goal 和 release scope 后再形成 DevOps handoff packet。

## Coverage Gaps

- None.

## Blockers

- None.

## Historical Result (Pre-#234)

- The previous durable result recorded Behavior **PASS**, Coverage **FULL**, and Overall **BLOCKED** after issue #234 identified prompt/fixture leakage.
- That pre-remediation result is retained only as history and is superseded by this strict fresh run.

## Next Steps

- Keep this case as a regression gate and rerun it after changes to `pm-agent`, its routing contract, or this fixture.

## Runtime Artifacts Policy

- Candidate responses, traces, status manifests, isolation records, and judge evidence remain under the gitignored runtime path above and are not committed.
