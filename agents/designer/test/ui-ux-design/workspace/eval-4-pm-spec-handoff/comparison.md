# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `designer`
- Skill: `ui-ux-design`
- Eval: `eval-004-pm-spec-handoff`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `0791241d90c35458117ad7afc41087d198e776e1bb0d176e05c3732f6be148a6` from `agents/designer/test/ui-ux-design/workspace/eval-4-pm-spec-handoff`.
- Identity schema: `2`
- target_skill_sha256: `2088a9b7ee00fc1f620b92a5141c4a34a4c48ca289c4be5cea831626687d85b8`
- eval_definition_sha256: `f5e031cd559d08b9cd37fee2f571fc541cf110879ad665b05952cb915a09fe63`
- metadata_sha256: `aeaed8ffc5b8caa72862d4541461b666c1ae241b901184003afdcc4031618907`
- fixture_sha256: `0791241d90c35458117ad7afc41087d198e776e1bb0d176e05c3732f6be148a6`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `2f242e255f292a4598cb48c2bfc21dd7b56a2d6cda47e6a68b75b5c3321a2e98`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `34a9d38fc5d93e5c1a925aa7889e94a7727bc719382f01830a2c7b69cc7a8020`
- Repository HEAD: `9ea58cf4e8c46064bd1a2c1cb2ca632f0a385fa0`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `beec8510dfdfe8132ffae9f12e486d2c527ec9245f5752f40eaeb251a4d63e70`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `spec` | PASS | The delivered design file explicitly states: “The PM specification authorizes design input; it does not authorize code or implementation.” |
| `assertion_2` | PASS | The delivered file names engineer-agent as downstream owner, and the final output says subsequent page updates can be handed to engineer-agent. |
| `assertion_3` | PASS | The delivery snapshot contains only the design document; git evidence shows no source-code changes, and neither the delivered file nor final output contains test commands, patches, or implementation step instructions. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=34a9d38fc5d93e5c1a925aa7889e94a7727bc719382f01830a2c7b69cc7a8020; fixture_sha256=0791241d90c35458117ad7afc41087d198e776e1bb0d176e05c3732f6be148a6; output_sha256=5f42a45dd71859bb5f36d94f144eb5e1aa6a24cbbc62d10428ad1f6a2d5d123f; snapshot_sha256=30e7f16eb55ba9cbd0c8c014303ec4e97455c8fe41be1a3ffb3a786e017c20ac
- Behavior: Produced the requested UI/UX design document with explicit design-only boundaries and engineer handoff.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=34a9d38fc5d93e5c1a925aa7889e94a7727bc719382f01830a2c7b69cc7a8020; fixture_sha256=0791241d90c35458117ad7afc41087d198e776e1bb0d176e05c3732f6be148a6; output_sha256=1d89b901d0137e3392799c5437eb4b83f0837bb0e03c094bac0114c08543d19e; snapshot_sha256=9525cde74ef832868b6dd0133359f7991fcbd16385849129e31e6c1ffcf8362e
- Behavior: Also produced a design document, but did not explicitly state the PM-spec boundary or engineer-agent handoff.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
