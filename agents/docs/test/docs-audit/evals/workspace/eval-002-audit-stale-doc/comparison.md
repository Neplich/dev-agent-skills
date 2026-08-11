# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `docs-audit`
- Eval: `eval-002-audit-stale-doc`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583` from `agents/docs/test/docs-audit/evals/workspace/eval-002-audit-stale-doc`.
- Fixture SHA-256: `7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583`
- Prompt SHA-256: `a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4`
- Repository HEAD: `f34c1007244dc48cf04fcd5d073fc5949225f1bd`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `7ed8638f6a80000c952068f188dbfe51d8ede83a52ee0b3635f473bf2d9da41d`
- Skill overlay SHA-256: `4183c2c4191ffb5278feb2ab2a6f8ac1fed136b346aab58bc7438d627c8d7660`
- Judge schema SHA-256: `6c436d29e1c4d967534d387d71455397c2a958eb0e9fdd8f24d404e3a4bfc7c7`
- Eval definition SHA-256: `65171d2c00ad7205a3b92eb523639da0ae1b9b851f9b225fb39f151ac8a09d1b`
- Metadata SHA-256: `393d49433e1e9b818095a60378e27c82e27a5159f0878e57881a2872b5feee91`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `marks_missing_doc_update_suspect` | PASS | 交付报告明确记录“same-diff status: not updated；deterministic classification `suspect`”，随后将最终事实结论列为 `stale`。 |
| `confirms_outdated_claim_stale` | PASS | 交付报告以目标代码中的 `QUERY locale required nonblank` 和 `ERROR 400 {"code": "invalid_locale"}` 为证据，确认文档不同步并将结论列为 `stale`。 |
| `blocks_stale_release` | PASS | 报告列出 stale 证据、要求更新文档并重跑审计，明确 `phase_result: blocked`，且未返回 `ready_for_tag`。 |
| `does_not_stamp_stale_set` | PASS | 报告记录 `last_verified_version: v1.0.0` 未更新，目标树无 `.meta/releases.json`，并明确未执行版本盖章或修改释放面。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=8ec797a2b9ebdb5cdb9e24f19eaf1a43248f664e937f75081f6a37030b5f45e4; snapshot_sha256=6326e66b2dcdc58c9479c0b47112d2d7febc24bdcca60c2ba8e4b1f8f467886c
- Behavior: 完整审计并保存报告；正确识别 suspect、stale、blocked，并避免盖章。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=a0986a693a041b20341e8fc74006f156b719dab648f0efc1ee18f7a27b8849f4; fixture_sha256=7c0329b08b7d983c3fb25be26c421ff6963478e62486e2e0e75d22d246186583; output_sha256=d292b1a6fd487511ffa4b08f87540a5489cc3b039dd6a7b1f3422e09a160b21d; snapshot_sha256=1144b19413ef6019378be29cb34da20166bbce8feff90d31c039acc8d1b8afb5
- Behavior: 仅提供简要阻断结论和文档缺口概述，未展示确定性 suspect 到事实层 stale 的完整审计链。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
