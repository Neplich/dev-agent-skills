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
- Identity schema: `2`
- target_skill_sha256: `a5e0bb043d61dbbb218e7d7efc08374e0d16a4d7aaa3b31817f2038830c90941`
- eval_definition_sha256: `3b49ebce5564e2973a0e2404ae2204baef9f3926736e7959e09be720ea423b90`
- metadata_sha256: `2b29c083a590a4eda139a3861e29b83daf406cc100d9a6f0e884225e104c8734`
- fixture_sha256: `02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `b484eac80dd3c83d19d6e2564672bb72616ee37e54370c5c00059bfaaa781dcf`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `d7e2242fcdf83209e6c0cb5ec9544aa009e79488a72f81ebd4bf387289fbabec`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `preserves_state_for_no_surface_change` | PASS | with_skill 正确识别 version-stamp.patch 仅更新 last_verified_version，且明确保留既有部署完整性状态。 |
| `refreshes_shared_state_for_material_change` | NOT_EXERCISED | with_skill 正确识别 internal-build-target.patch 改变构建命令、默认输出逻辑和 VitePress outDir，并要求重新核对；但缺少部署完整性证据，无法证明后续共享状态刷新已执行。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba; fixture_sha256=02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52; output_sha256=d680401b9e1b891db1dbd8e4bfcd37e8c4e82f06f2b3a8b1a120db07f184edb6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确区分纯版本标记与构建产物路径变化，保留无变化状态并识别需要复核的材料变化；未修改部署配置。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=cb27f98c195c0adaa2bc7ce90eded119c590e29ff34ec55cdd7a71187adb71ba; fixture_sha256=02024e6f0aaa0bcf6615062b3d8a31430a90f2e0a76edad7ce1044c04423eb52; output_sha256=0d52c93cf7e3e30828f19739e506a45be10bc1053bdcfe3d96d2fc27d52f058a; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 同样正确识别两类 patch 的表面影响，作为新鲜基线对照。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补齐维护者确认的 target_release_version、审计交接和部署完整性运行时证据后，复用共享检查并刷新状态。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
