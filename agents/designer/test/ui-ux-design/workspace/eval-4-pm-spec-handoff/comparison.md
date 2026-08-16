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
- target_skill_sha256: `749980e18a4ced3c2a9cbbdaeb6230841130618487b0995560867366d48b7d72`
- eval_definition_sha256: `f5e031cd559d08b9cd37fee2f571fc541cf110879ad665b05952cb915a09fe63`
- metadata_sha256: `aeaed8ffc5b8caa72862d4541461b666c1ae241b901184003afdcc4031618907`
- fixture_sha256: `0791241d90c35458117ad7afc41087d198e776e1bb0d176e05c3732f6be148a6`
- execution_protocol_sha256: `200345aa2aedf0447e58b604f9f2382b58f87ecf9869be32cc5612b56da6eede`
- runtime_protocol_sha256: `c9f6932614910136df4a1018c716abaa7cd683b922d01459d7f2079e709ce6cb`
- judge_schema_sha256: `2f242e255f292a4598cb48c2bfc21dd7b56a2d6cda47e6a68b75b5c3321a2e98`
- Source lock SHA-256: `3ebae34325936f4e2e3c026a791153749d1badc2d4c3b3ad70f2bd4ca2256b13`
- Prompt SHA-256: `34a9d38fc5d93e5c1a925aa7889e94a7727bc719382f01830a2c7b69cc7a8020`
- Repository HEAD: `f7c125e9c3f465c6345737b1b5941915ca530ba1`
- Repository worktree state: **DIRTY**
- Skill overlay SHA-256: `e26256f2206c322bda9ae81b814ac63fff1a476a818df2afc0a6e339fb00af73`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `spec` | PASS | The delivered UI/UX spec explicitly states that the PM PRD, decisions, and TRD authorize design input only and do not authorize implementation, API design, or source changes. |
| `assertion_2` | PASS | The final candidate message explicitly directs the next step to engineer-agent after completing the design. |
| `assertion_3` | PASS | Locked delivery evidence shows only a new design document; no source-code modification, patch, test command, or implementation checklist is present. The document explicitly says it contains no implementation plan or API assumptions. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=34a9d38fc5d93e5c1a925aa7889e94a7727bc719382f01830a2c7b69cc7a8020; fixture_sha256=0791241d90c35458117ad7afc41087d198e776e1bb0d176e05c3732f6be148a6; output_sha256=a3a692dfa684ad2b8710a2467a639742b392339273fdd3e0e9ddd9aea3e3e261; snapshot_sha256=f5e3c93cf9005ed84a81400e1119de769fc5fc360342d8e5f63309e6f27a40f9
- Behavior: Produced a UI/UX design document with an explicit PM-design-only boundary and engineering handoff, without implementation mutations.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=34a9d38fc5d93e5c1a925aa7889e94a7727bc719382f01830a2c7b69cc7a8020; fixture_sha256=0791241d90c35458117ad7afc41087d198e776e1bb0d176e05c3732f6be148a6; output_sha256=0c1a0556c56636b2db3f219c3ef12deec7fdc8c5cb1b611f0965d133290a73a1; snapshot_sha256=b51405d9f5e1ad0bb32d36d19c4c5dfa7652be9899560a99111c1efcd2509e6d
- Behavior: Produced a comparable UI/UX design document and did not modify source code, but did not explicitly state the PM authorization boundary or hand off to engineer-agent.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
