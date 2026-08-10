# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `feature-implementor`
- Eval: `eval-012-implementation-plan-archive-preflight`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e` from `agents/engineer/test/feature-implementor/evals/workspace/eval-012-implementation-plan-archive-preflight`.
- Fixture SHA-256: `681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e`
- Prompt SHA-256: `9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `1b3ba014c732559fe2d85e84b85c8db967bb14f4b1fc850a2267e7d4ee1cf03b`
- Skill overlay SHA-256: `7f72b0d2378eefdc164735f00c26c14522753a42e538abe02ba7accda3b0a9f5`
- Judge schema SHA-256: `097d311377d0abb4f2fcb1bfa46de1df83e6feccaa7b6f38bb1fb185a5118ab5`
- Eval definition SHA-256: `3628876acf1d52ad92b5faf79f556bf7cb6aca5a88b0bd15975a544759685f18`
- Metadata SHA-256: `158f5bafaa3ad4ac6ba561642292db5794c29432044a423049518391aa4f0dbd`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `runs_pre_plan_archive_scan` | PASS | Trace records commands reading the active plan and checking the archive directory before the final decision; output records both paths and archive state. |
| `blocks_direct_overwrite` | PASS | With-skill git evidence shows no changes, and output explicitly waits for the archive decision before writing a new plan or coding. |
| `offers_implemented_handling_options` | PASS | Output requests exactly two choices: archive then create, or archive as Superseded with a reason then create; it offers no Implemented-status update option. |
| `keeps_active_entry_fixed` | PASS | Output states the active plan path is fixed and identifies the archive directory as the only archive location. |
| `does_not_implement_directly` | PASS | Output states implementation is blocked and does not claim code changes, implementation, or completed verification; git evidence is clean. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74; fixture_sha256=681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e; output_sha256=0ada7e402cdd69639e40f216716c223cdabd73dd7e31fde86428db8808812265; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Scanned the existing completed plan and archive location, preserved the active entry, and paused for the required user archive decision.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=9c7650cd9313e12223d2a68ebc3c37905ca839128cbb6b36d20fc7541af57b74; fixture_sha256=681e197eb0a978ca201707a3d3b58dd8ed78255de8e5033ca94ef611ea90807e; output_sha256=3207c55a152cf86ee83969e077632b6f6f46a838171fa7f10becaae2c1d8d346; snapshot_sha256=19ce93611d1f23b862d248591ff905c7cd3a0e423055fea6127a7f85691e33de
- Behavior: Directly overwrote the active plan and created an archive in the wrong directory without the required decision gate.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
