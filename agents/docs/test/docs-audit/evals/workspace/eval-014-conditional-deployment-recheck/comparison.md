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
- Repository HEAD: `fecf485e8e3dcaf191b2b221d9cccbddfdea0b72`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `5b11b38c1c44c386fe19122dfb1ce5918b2bfbc4830ad32aa994d8a7e39f35e7`
- Skill overlay SHA-256: `85c4ae0a1d58505c4a23c34e6f9116aed81a09b4b6270e3ce148424084f6c7e0`
- Judge schema SHA-256: `b484eac80dd3c83d19d6e2564672bb72616ee37e54370c5c00059bfaaa781dcf`
- Eval definition SHA-256: `3b49ebce5564e2973a0e2404ae2204baef9f3926736e7959e09be720ea423b90`
- Metadata SHA-256: `2b29c083a590a4eda139a3861e29b83daf406cc100d9a6f0e884225e104c8734`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_state_for_no_surface_change` | PASS | with_skill 将 version-stamp.patch 识别为仅修改 last_verified_version 元数据，并判断不影响构建目标、导航、资源或运行入口，因此保留既有完整性状态。 |
| `refreshes_shared_state_for_material_change` | NOT_EXERCISED | with_skill 正确识别 internal-build-target.patch 改变内部输出目录和构建默认逻辑，并提出重新核对；但因缺少正式 docs site、部署状态、交接证据及确认的 target_release_version 而 blocked，未实际证明共享检查刷新或后续状态更新。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba; fixture_sha256=02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52; output_sha256=c1bb64b4f7291618b068b79d1e5f321f9e6b906ba31a6e2430e96b6d81b0e14f; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确区分无发布面变化与构建面变化，识别需重检的部署影响，保持只读并在缺少运行时/审计基础证据时阻止完整审计。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba; fixture_sha256=02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52; output_sha256=8e43bc98392d3cae7ed1d7ee86ef415bc1ced1d6c99ebd56f3cfa78d7d2bf3a4; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 新鲜基线也正确区分两类补丁并指出工作区缺少站点和部署配置；仅作对比，不用于判定 with_skill 断言。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充正式 docs site、部署完整性状态、审计交接证据和维护者确认的 target_release_version 后，复用共享检查并刷新状态。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
