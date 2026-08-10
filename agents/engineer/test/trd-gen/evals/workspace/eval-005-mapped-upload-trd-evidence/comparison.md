# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-005-mapped-upload-trd-evidence`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007` from `agents/engineer/test/trd-gen/evals/workspace/eval-005-mapped-upload-trd-evidence`.
- Fixture SHA-256: `b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007`
- Prompt SHA-256: `415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `6b892e000764d0f52ab1e2bbfd237e12483caafd3413b84144f2d3397ea92558`
- Skill overlay SHA-256: `2811fdd3c57db7a2738883046d1d787b9d794bcfbf96919af99fd2eac7160676`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `ed02404d14ffd40d542c29f44a74caf2fc5696740b01f75b11e50dfad6379f60`
- Metadata SHA-256: `cfc84017a2f6130d5f5d58c0d09338a6a3beaaf2ead3e34eb6d3229566da0300`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **FAIL**
- Coverage result: **FULL**
Overall result: FAIL

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | FAIL | with_skill 的 trace 先扫描了 `.agents`、`docs` 及多项无关技能/文档内容，之后才读取 `docs/site/standards/change-map.yaml` 和其指向的 `docs/site/api/upload.md`。 |
| `verifies_against_code` | PASS | with_skill 直接读取 `src/upload/limits.txt`，识别出代码为 10 MB、文档为 20 MB，并明确记录该冲突及需由 PM/Engineer 确认其影响。 |
| `treats_unverified_as_low_trust` | PASS | with_skill 明确指出 `last_verified_version: unverified`，将页面视为低信任，并以配置文件作为关键限制依据。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888; fixture_sha256=b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007; output_sha256=f31f044a7f483b4d0b3f16fae036afe8c05c81ecce775bd9bf7236e9a76de224; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核对了配置与文档冲突，并正确降低未验证文档的信任级别；但在读取 change-map 前进行了无关范围扫描。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=415550072b82b1b3b236c15b45beda7e56782899611899aec658b78876563888; fixture_sha256=b9272be266caff6ac38d8060f5dbdbc6e981647729fe1530cfc53ca05b58b007; output_sha256=a8d33f80c2f42eba31d1ead20e6b9ba5a6e2cbf370ba736ed1748352174ff71b; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 识别了 10 MB/20 MB 冲突并提出方案，但未体现受控的映射文档读取流程或明确的未验证文档低信任处理。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- 未满足映射文档优先且不遍历无关文档的要求。
- Next: 从 `src/upload/` 任务落点先读取 change-map，再只读取其指向文档和必要代码证据。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
