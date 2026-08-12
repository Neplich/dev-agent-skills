# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `pm-agent`
- Eval: `eval-010-change-tier-hotfix-fast-lane`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/pm-agent/evals/workspace/eval-10-change-tier-hotfix-fast-lane`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `c8036aad85835ee733e12f58737233d7e9bc1a90da347bec50e7094cf58797ad`
- Repository HEAD: `715bd6b76fcd6f14f475aeabe141543063d431ba`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `be11ec63823b148323fef6c35d27c0861bd093b24d683f705e846234e98b7baa`
- Skill overlay SHA-256: `961e7aacbdec2d154ad578bc7bf54d5d734f34031af1384fb20aa67a8e2d392a`
- Judge schema SHA-256: `bb0ee0282945f3d4f9dce339b9d8538e36a23ce40cb0cf92b33dc2be95234be0`
- Eval definition SHA-256: `47a19a6c15b443fba6827b5bff8e5f73b3367c26176898038b1822e6a445e0c6`
- Metadata SHA-256: `dd7edb355d66e4505d2039e9fe3eb4eb203c3d8b2cfcc299410f099efef7e166`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `classify_hotfix` | PASS | The with_skill output explicitly sets change_tier to hotfix and explains that the README-only correction leaves functionality and expectations unchanged, with local verification evidence. |
| `allow_fast_lane` | PASS | It explicitly sets fast_lane to allowed_after_classification for the delivery request, preserving the required ordering after classification. |
| `preserve_evidence` | PASS | It records confirmed_scope, source_documents including local-link verification, and required verification of the diff; hotfix handling does not waive verification. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8036aad85835ee733e12f58737233d7e9bc1a90da347bec50e7094cf58797ad; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=e27654698638234e1f004a65309d0c5bb54739095543f891d3322ae39dfa49e6; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Correctly classifies the request as an allowed hotfix, permits fast lane after classification, preserves scope and evidence requirements, and transparently blocks delivery on missing workspace inputs.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=c8036aad85835ee733e12f58737233d7e9bc1a90da347bec50e7094cf58797ad; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=938ee222867d02b1c453a8a3ed968006fa5d381ef5836340f3407687e381f402; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Reports the empty repository and stops without making the routing classification or evidence-preservation decision.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Restore or attach the PR workspace/diff, then rerun delivery.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
