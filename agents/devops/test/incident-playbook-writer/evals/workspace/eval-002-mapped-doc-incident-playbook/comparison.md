# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `devops`
- Skill: `incident-playbook-writer`
- Eval: `eval-002-mapped-doc-incident-playbook`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7` from `agents/devops/test/incident-playbook-writer/evals/workspace/eval-002-mapped-doc-incident-playbook`.
- Fixture SHA-256: `cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7`
- Prompt SHA-256: `27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `500941dffb48347901d3283054321002e2a4be37cb509882170d999b6f27485f`
- Skill overlay SHA-256: `8bcf98d79219616ab4a2e4bf38f41850dabf91363c7e81c3766a5503c4452405`
- Judge schema SHA-256: `6eadf49a93ad15b65779f0737c549d6122220ac6abe8a01622417bb0da199cda`
- Eval definition SHA-256: `56f66c660609712980bbe29e190d00dff6d36c67cb844c6b5e1aa3d336dcd314`
- Metadata SHA-256: `d30677e1d058f7ced7ac6b80a07136e834c175a519dc8964e75c167556348374`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_mapped_docs_first` | NOT_EXERCISED | with_skill 的锁定原始证据没有提供实际文档读取顺序或工具轨迹，无法证明优先读取该映射文档。 |
| `verifies_against_code` | PASS | with_skill 明确核对了 src/runtime/health.rules 中的 5 次阈值，指出文档的 3 次说法，并说明按文档执行会提前两次触发处置。 |
| `treats_unverified_as_low_trust` | PASS | with_skill 将 last_verified_version: unverified 视为低信任，使用规则文件确认告警阈值，并因缺乏部署、恢复和回滚证据而拒绝生成未经核证的可执行步骤。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e; fixture_sha256=cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7; output_sha256=85f30731b1c2fb8dce2e02083a552cf53ddaf200969607e08ab6d4c9a2de01c6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: 正确核证了代码阈值、识别并降低未核证文档的信任度；在缺少回滚运行时证据时安全阻塞，未进行文件修改。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=27a471d4180c030327b87d22f79174352fdeffbbaace399da8cf913275d6b17e; fixture_sha256=cd9e0e84ed5447d0b5fbaab481b132d7d6de821290e56efdee5b00d1661c9bf7; output_sha256=195274b079daa5a12d8ad174bd4e547b9eaac0d47ade974c363e26d936fc9511; snapshot_sha256=ffb9cffc4080bf17c22b61b00e1cf967ee3fd5b95bdded7ed63c983967953cdc
- Behavior: 生成并修改了健康说明，修正阈值并加入处置/回滚步骤，但其锁定证据未证明读取顺序或对 unverified 文档采取最低信任。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: 补充部署方式、上一版本恢复命令和健康恢复判据后，再生成并核验可执行的处置与回滚 runbook。

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
