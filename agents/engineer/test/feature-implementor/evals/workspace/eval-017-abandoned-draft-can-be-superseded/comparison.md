# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-017-abandoned-draft-can-be-superseded`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `c0e7350515f9e8f3a166039b0e6d074b044f7918d0abfcaabf64ea0fd4ef53cb` from `agents/engineer/test/feature-implementor/evals/workspace/eval-017-abandoned-draft-can-be-superseded`.
- Fixture SHA-256: `c0e7350515f9e8f3a166039b0e6d074b044f7918d0abfcaabf64ea0fd4ef53cb`
- Prompt SHA-256: `9ebe9d873c66a07a5ecd0428e103d2f74136e9e17f4f22b79640f42f218d18ee`
- Repository HEAD: `7ac19d358ca18ef7b2d109aeec17239bc9d0f4c0`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `2cef9a078b25940be2cd93c65c4193da4205d9703e5924079fcda5ac81b0dc82`
- Skill overlay SHA-256: `06e677e2d778ad6e9070a73693d2a9f47819f161c623014f6e26b508a4d8e533`
- Judge schema SHA-256: `a264d3282fcfebf29821ed24d8e702134594b3cc4be72cd72f03b0e03e92c160`
- Eval definition SHA-256: `92bf4838a78758f537ca7650dd1be190ad947406f8ab40d6ace62d644c28dc37`
- Metadata SHA-256: `21a9c9ae11f8c9b8058a429c319a4f2a640a6b07fdf2d71e259bbc158caa4e24`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `reads_unfinished_active_plan` | PASS | Raw trace shows the original plan was read and identifies status Draft, path docs/engineer/payment-refund/IMPLEMENTATION_PLAN.md, and implementation_scope refund-reason-codes. |
| `detects_explicit_abandonment` | PASS | Raw trace and delivered plan identify the maintainer’s explicit abandonment and choose the supersession path. |
| `archives_as_superseded` | PASS | Locked archive snapshot has status Superseded, non-empty superseded_reason, preserved metadata, archived_at, archive_approved_by, and source_plan. |
| `links_replacement_plan` | PASS | Locked active-plan snapshot includes previous_plan_archive pointing to the same feature_path’s Superseded archive. |
| `waits_before_coding` | PASS | Trace shows only plan/archive file changes, no code or tests; final output explicitly requests confirmation before coding. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9ebe9d873c66a07a5ecd0428e103d2f74136e9e17f4f22b79640f42f218d18ee; fixture_sha256=c0e7350515f9e8f3a166039b0e6d074b044f7918d0abfcaabf64ea0fd4ef53cb; output_sha256=ce6aa73359a7e09794b0a426c2f8c46c4d6dcad7eb0398774f40c4d7dd816fb4; snapshot_sha256=f05bc5092d80ad6dc00af86cb78b47b62a855d965a879e144475efab6ae38605
- Behavior: Read the unfinished plan, detected explicit abandonment, archived it as Superseded, linked a replacement plan, and paused before coding.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9ebe9d873c66a07a5ecd0428e103d2f74136e9e17f4f22b79640f42f218d18ee; fixture_sha256=c0e7350515f9e8f3a166039b0e6d074b044f7918d0abfcaabf64ea0fd4ef53cb; output_sha256=2c52cca74bdb51ce01855f863fa5c27db6cb0090727ff0893716694b088ae133; snapshot_sha256=9457564a7eb678c53e7ba19bd67a09ec9f942e51d8f3a1d75d940923d921e265
- Behavior: Fresh baseline modified the active plan to Abandoned and implemented code/tests without a Superseded archive, replacement-plan link, or confirmation gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
