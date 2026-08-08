# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `release-notes-gen`
- Eval: `eval-004-conditional-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31` from `agents/docs/test/release-notes-gen/evals/workspace/eval-004-conditional-deployment-recheck`.
- Fixture SHA-256: `1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31`
- Prompt SHA-256: `5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2da7831c1e3b626979a3601984870e16015610b54d1ff8f08ff8c14d15f812ca`
- Skill overlay SHA-256: `d552bdbf1aa95d384d7132b02e78e69678457f53a15c3f49ddfae00094ce8ee0`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `34ab52326e403178b3c65c89903f9ce3ed937721059a083b8dcd35f212e12e18`
- Metadata SHA-256: `026d3644999635bf9397130063cb1f65e3467ff790b1fe892aa83df25be7904c`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `skips_content_only_recheck` | PASS | With_skill correctly identifies editorial.patch as a wording-only change with no impact on build, deployment artifacts, or routes, so the existing deployment conclusion remains valid. |
| `rechecks_material_release_surface` | PASS | With_skill correctly identifies internal-entry.patch as changing the internal output directory and Dockerfile copy path, requiring revalidation of the internal build/container chain; it does not introduce a separate checklist. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=4625e5f92e5571bd6647d1526b3ccdb87ea9e3299c04bd686a4d67fd8af289e5; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classified the patch impacts and appropriately declined unsafe version-note completion because the documentation host structure was absent and the patches were corrupt.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=5b0a2bb08468867270b5e33622f2c669d7709f2935d65084fe81cdc7c550d3b1; fixture_sha256=1d05a5ef6eacf2734acacac9c7f138205eacee50a9bb44893b96aa9bb0d64d31; output_sha256=dee79b9a68003b286a2e9031df6e760ae8c6262aa9000d934af202da6ce9c32b; snapshot_sha256=c00960013e1ff6240e05a6af420c08a5f9d68ef56aa347528e579d03b5a39525
- Behavior: Correctly classified both patches, but claimed version-note completion by creating an unsupported release-note file.
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

# Skill Eval Comparison

## Evaluation Target

- Skill: `release-notes-generator` → `release-notes-gen`（改名后新入口，已按 #238 于 2026-08-06 fresh 隔离重跑）
- Eval: `eval-004-conditional-deployment-recheck`
- Review context: issue #162 fresh paired validation

## Test Set / Fixture Version

- Fixture: issue #162 scenario evidence in this workspace
- Validation date: 2026-07-22
- Execution cleanup: all declared runtime paths were absent from pristine scratch fixtures

## Latest Result

- Overall result: FAIL
- Blocking reason: 已按 #238 完成 fresh 隔离重跑（2026-08-06，gpt-5.6-luna + effort medium，独立 judge 判定），结论基于新契约；历史行为描述保留于下方段落（适用旧契约）。

## #238 Fresh Rerun Result（2026-08-06）

- 执行：with/without 两条 lane（独立 codex exec，gpt-5.6-luna + effort medium，仓库外 workspace 物化，逐字同 prompt）；判定：独立 judge（fresh 会话，read-only，对照断言逐条核对产物事实，不采信 lane 自述）
- with_skill：Behavior `FAIL` / Coverage `FULL`
- without_skill：Behavior `FAIL` / Coverage `FULL`

### 逐断言判定

| 断言 | with_skill | without_skill | 判定依据 |
| --- | --- | --- | --- |
| `skips_content_only_recheck` | PASS | PASS | with_skill 明确写出“Content-only…不触发部署级复核”；without_skill 写出“纯文案/错字变更：不影响运行时，无需部署”。 |
| `rechecks_material_release_surface` | FAIL | FAIL | 两条 lane 都识别出新增 Internal 导航会改变生成输出和启动路径；但 with_skill 仅说“需重新验证”，没有产出共享状态/检查复用证据；without_skill 仅分类为需要部署，也没有证明复用共享检查。两者均未复制新清单。 |

未满足断言（with/without 任一 FAIL）：``rechecks_material_release_surface``



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- content-only 保留状态；runtime change 复用唯一共享协议且不复制 checklist。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-004-conditional-deployment-recheck/candidate-output.md`.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- PARTIAL (1/2)；识别触发差异，但未声明共享状态/协议复用。
- The same prompt and pristine fixture were used; no historical baseline, target skill, Agent README, shared skill-map, old comparison, or with-skill output was used to compose it.

## Failures
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- baseline 缺共享协议复用语义。
- No with-skill assertion failure or runner/credential blocker.

## Next Steps

- Keep this regression case; strengthen fixture ambiguity later where the baseline already passes.

## Runtime Artifact Policy

- Runtime candidates, copied fixtures, verdict, status, and diagnostics remain under `tmp/eval-runs/issue-162/` and are not committed.
- Only this durable comparison, eval definition, metadata, and fixture evidence are submitted.
