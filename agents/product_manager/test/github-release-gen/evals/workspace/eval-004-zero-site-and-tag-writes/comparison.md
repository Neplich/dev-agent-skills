# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `github-release-gen`
- Eval: `eval-004-zero-site-and-tag-writes`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `a74185c0f265c7463444aa160a9976a1ef120533a9280afc72706076cc5c1626` from `agents/product_manager/test/github-release-gen/evals/workspace/eval-004-zero-site-and-tag-writes`.
- Identity schema: `2`
- target_skill_sha256: `ed7c0a44968df88c4831e9abe2b9be4922e4fa2cd6bcbd8dc6dd7e927ff9c87a`
- eval_definition_sha256: `266baf4d19e4ef318c97a6eab3bf8e029fbe8357edfa824c6d453c40e91b2d33`
- metadata_sha256: `12fc2cb8802eb1dba2db5f0429fdb4322d489582597f6f44ee10596dc46d8d26`
- fixture_sha256: `a74185c0f265c7463444aa160a9976a1ef120533a9280afc72706076cc5c1626`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `80b618e955757ddc076d881c72f5f8be648700b5dd3e7c6b222dd59ecfccd495`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `1db93b427a92207a25326b835a99580d099361beaf054fde25062b79bf7ca135`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `41bf9818330e1ae365d336932a5653b591537342874ba68ae701f1478bc7b159`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `does_not_write_docs_site` | PASS | with_skill 明确表示未执行任何站内文件写入；delivery_snapshot 为空，git_evidence 显示 HEAD、refs、index 和 worktree 均无变化。 |
| `does_not_mutate_tags` | PASS | with_skill 明确将 v1.0.0 tag 创建交给 release-owner；git_evidence.ref_delta 为空且无新提交或 reflog 变化。 |
| `avoids_gh_release_create_without_tag` | PASS | with_skill 明确说明目标 tag 缺失时禁止执行 draft command，因为 gh release create 可能自动创建 tag；未执行 GitHub Release 写入。 |
| `reports_zero_mutation_boundary` | PASS | with_skill 明确报告未执行站内文件、测试、tag 或 GitHub 写入，并报告 actual_tag 缺失、draft 未创建；锁定 git 证据确认零变更。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1db93b427a92207a25326b835a99580d099361beaf054fde25062b79bf7ca135; fixture_sha256=a74185c0f265c7463444aa160a9976a1ef120533a9280afc72706076cc5c1626; output_sha256=7e4cdcf6e2aae6770041773c3b17bad19e553f18506d241a591ea165a4a5e0cf; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 保留完整 inline preview，识别缺少实际 tag 和远端证据的门禁，未执行站点、tag 或 GitHub Release 写入。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=1db93b427a92207a25326b835a99580d099361beaf054fde25062b79bf7ca135; fixture_sha256=a74185c0f265c7463444aa160a9976a1ef120533a9280afc72706076cc5c1626; output_sha256=fd4d1078553aaf2f2df1d4962dc58051125d534441616e8d730c8545a186b294; snapshot_sha256=5992467a0f39a2ecb03eb499187ea9231ffb885c4ab91e3ff96485b581aac4a5
- Behavior: 修改 docs/site、提交变更并创建本地 annotated tag；未创建 GitHub draft。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
