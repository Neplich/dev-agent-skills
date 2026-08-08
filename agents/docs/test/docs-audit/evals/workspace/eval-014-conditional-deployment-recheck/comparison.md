# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-014-conditional-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52` from `agents/docs/test/docs-audit/evals/workspace/eval-014-conditional-deployment-recheck`.
- Fixture SHA-256: `02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52`
- Prompt SHA-256: `cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `9e9abf391c9ccd9564d35b5def50bc0374b1db0886710676c4d48422839746ae`
- Skill overlay SHA-256: `c66ac938bf9158faa694d7c3e311e913ddc4a06da11de703a881234f257c470c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `3b49ebce5564e2973a0e2404ae2204baef9f3926736e7959e09be720ea423b90`
- Metadata SHA-256: `2b29c083a590a4eda139a3861e29b83daf406cc100d9a6f0e884225e104c8734`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_state_for_no_surface_change` | PASS | with_skill 正确识别 version-stamp.patch 仅更新 last_verified_version，未改变构建目标、输出目录或发布面，因此判断不需重新核对部署完整性。 |
| `refreshes_shared_state_for_material_change` | NOT_EXERCISED | with_skill 正确识别 internal-build-target.patch 改变构建输出目标并判断需要重新核对，也明确未修改部署配置；但仅有 patch、没有实际部署配置或运行时证据，无法证明后续复用共享检查并刷新状态。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba; fixture_sha256=02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52; output_sha256=c196a1abaa8d7d18f8698367537dfd3d6dc3c7c52d5d0533edc1c246412ac0dd; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确区分两类变更，准确判断是否需要重新核对，并声明无法验证不存在的实际部署链路且未修改文件。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba; fixture_sha256=02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52; output_sha256=e3587c5ef85c249b095b7441fba5a447aaeb9425c8fa17eb2258f15e4dfdf6a1; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确区分版本戳变更与构建输出目标变更，并报告未修改部署配置。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 提供实际部署配置及运行时检查证据，以验证 internal-build-target.patch 后的共享完整性检查和状态刷新。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-014-conditional-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52` from `agents/docs/test/docs-audit/evals/workspace/eval-014-conditional-deployment-recheck`.
- Fixture SHA-256: `02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52`
- Prompt SHA-256: `cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2d24da5f976a5ab2710c2c072a19015e074d314e0ebdb88f1c28831425f1b98c`
- Skill overlay SHA-256: `40330c17a3b77f25a1b1a716fa5e9355e0011db79d19014344ed516affba11c8`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `3b49ebce5564e2973a0e2404ae2204baef9f3926736e7959e09be720ea423b90`
- Metadata SHA-256: `2b29c083a590a4eda139a3861e29b83daf406cc100d9a6f0e884225e104c8734`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_state_for_no_surface_change` | FAIL | with_skill 错误地将 version-stamp.patch 视为仅版本元数据变更；原始补丁还修改了 internal 构建脚本默认输出、build:internal 输出目录及 VitePress outDir，因此不能保留既有完整性状态。 |
| `refreshes_shared_state_for_material_change` | PASS | with_skill 正确识别 internal-build-target.patch 的构建目标变化，并要求复核部署消费路径、旧目录引用、发布结果及公共目标，同时未提出新协议或修改部署资产。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba; fixture_sha256=02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52; output_sha256=3864f88097185f80a4cd20db73775790e8e38f3c1ab80fd3e6861b413e2b1986; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 对 internal-build-target.patch 的处理符合要求，但错误遗漏 version-stamp.patch 的实质性构建面变化。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba; fixture_sha256=02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52; output_sha256=9bb0374ebce8a5fa43a04400e3b195b26fa34d1b6f8d2991458a4f33c25fa49b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确识别 internal-build-target.patch 的构建面变化，但同样漏判 version-stamp.patch 中附带的构建与发布路径变更。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- with_skill 未发现 version-stamp.patch 同时修改 internal 构建输出路径及 VitePress outDir，导致错误判断为无需重新核对。
- Next: 重新评估 version-stamp.patch，并核对其 internal 构建与部署路径影响。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-014-conditional-deployment-recheck`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52` from `agents/docs/test/docs-audit/evals/workspace/eval-014-conditional-deployment-recheck`.
- Fixture SHA-256: `02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52`
- Prompt SHA-256: `cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2baee6e542351d5b0c46e79c685dd29ff93f0fee4a45cf4485afee7656248cf7`
- Skill overlay SHA-256: `a2871f547194089c5425585467f9bee6e3c85ea103d77933d85a4c4cf246fa7c`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `3b49ebce5564e2973a0e2404ae2204baef9f3926736e7959e09be720ea423b90`
- Metadata SHA-256: `2b29c083a590a4eda139a3861e29b83daf406cc100d9a6f0e884225e104c8734`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_state_for_no_surface_change` | PASS | with_skill correctly classifies version-stamp.patch as not requiring a deployment-integrity recheck because it only changes last_verified_version and leaves build/deployment surfaces unchanged. |
| `refreshes_shared_state_for_material_change` | PASS | with_skill correctly classifies internal-build-target.patch as requiring revalidation because it changes internal build output paths in package.json, build.mjs, and VitePress config; it proposes checking consumers and states no deployment configuration was modified. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba; fixture_sha256=02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52; output_sha256=0b7c94f2217e161a2830271d77d7fca7d10eb4f05080a940647fb83b3389bb03; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly distinguishes both patches, identifies the changed internal output surface and relevant consumers, and preserves the no-deployment-config-change constraint.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba; fixture_sha256=02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52; output_sha256=812ea126fd6457339cba2ac2ad4d441f559f15f83c805d75a7aa4c7544326a52; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly distinguishes the metadata-only version stamp from the internal build-target change; notes that external deployment consumers cannot be verified from the fixture.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
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

# Skill Eval Comparison

## Evaluation Target

- Skill: `docs-audit`
- Eval: `eval-014-conditional-deployment-recheck`
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
| preserves_state_for_no_surface_change | FAIL | FAIL | 两条 lane 的 `evidence.md` 仅说明 `version-only` 只改 verification metadata、无构建或发布面变化；没有记录既有完整性状态被保留或重新检查后的状态。 |
| refreshes_shared_state_for_material_change | FAIL | FAIL | 两条 lane 仅记录 `build-target-change` 改变 `build:internal` 的生成产物和 runtime entry；没有共享检查复用、状态刷新、第二协议或部署资产未修改的实际产物证据。 |

未满足断言（with/without 任一 FAIL）：`preserves_state_for_no_surface_change`、`refreshes_shared_state_for_material_change`



## With-Skill Behavior
> ⚠️ 本节为该文件历史轮结论（适用旧契约/旧 fixture），本轮 #238 结论见上方「#238 Fresh Rerun Result」。

- version-only 保持状态；build/runtime change 刷新共享状态，不建第二协议、不改部署资产。
- Candidate source: fresh `tmp/eval-runs/issue-162/with_skill/eval-014-conditional-deployment-recheck/candidate-output.md`.

## Fresh Without-Skill Baseline

> ⚠️ 本节为历史轮执行证据（适用旧 run）；当前结论以本文件上方「#238 Fresh Rerun Result」为准。

- PARTIAL (1/2)；识别是否重检，但未声明共享协议与状态刷新契约。
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
