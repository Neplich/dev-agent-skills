# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `docs`
- Skill: `formal-docs-sync`
- Eval: `eval-010-release-notes-boundary`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c` from `agents/docs/test/formal-docs-sync/evals/workspace/eval-010-release-notes-boundary`.
- Fixture SHA-256: `f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c`
- Prompt SHA-256: `59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f`
- Repository HEAD: `750d3d7432a4dcfde7dde2624f081fbf388f85f3`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `f24bfeb12dba77a74fcf3f0161749ae4671b83762eac08484e7ae08621d9bacb`
- Skill overlay SHA-256: `5dbb8d8559bfab3926047aa028e19f362490751247c2142101cfd687fff5239e`
- Judge schema SHA-256: `b3a1a852c447e6e1ef51ed958da793390c6914ade2f68188c4962daac377d01b`
- Eval definition SHA-256: `73a1610671f9f97761837a796f3ae7908687bbe25fc17ad4582a0bb4ee5c7fae`
- Metadata SHA-256: `2352ae604513521c63a446b6d886e6c879f4a0cef5861b4ee1c9c3ee9f319eba`
- Executor SHA-256: `321fdc8a67ccc7fd6265fadebaa8db97593c38dcd8d7842f8aea59909966bd54`
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `recognizes_release_communication_outcome` | PASS | `mode: release` and the proposed batch explicitly identify the release-notes page, version list, metadata, and host-required navigation as release-communication surfaces. |
| `routes_complete_entry_to_site_owner` | PASS | The handoff records the confirmed host, v1.5.0, scope, evidence bindings and target surfaces, and assigns follow-up generation to `release-notes-gen`. |
| `keeps_entire_site_zero_diff` | PASS | The candidate states writes were blocked; git status, diff, and delivery snapshot show no changes anywhere under `docs/site/`. |
| `preserves_external_release_boundary` | PASS | The output explicitly excludes GitHub tag/release activity, and git evidence shows no ref, commit, branch, or worktree changes. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=9484f4cf3484156d337a7697f8ac4b6affec5a6e168492674d62d82158785be2; snapshot_sha256=4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
- Behavior: Blocked the release-document write gate on missing implementation and base-reference evidence, preserved the site unchanged, and routed the work to the Docs release-notes owner.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=59f3f4b07b3e4d027f3b554bec6c0d7c22a2923908783529642641c26634e91f; fixture_sha256=f62e3d002a3d849e5b28b313abce4433afd4885459572da3c6552b50d7fc432c; output_sha256=71542463b5e2df00fcf3330b71479b32630d53d0ac302b4a29be04588ad2881e; snapshot_sha256=221673634388bc18df01f647983eb8cd256516c591fbcc054b7cf604c4c8074f
- Behavior: Directly created the v1.5.0 release page, version-list entry, and release metadata, producing site changes.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
