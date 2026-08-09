# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `engineer`
- Skill: `trd-gen`
- Eval: `eval-003-nested-prd-to-engineer-trd`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc` from `agents/engineer/test/trd-gen/evals/workspace/eval-003-nested-prd-to-engineer-trd`.
- Fixture SHA-256: `9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc`
- Prompt SHA-256: `8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `73cec46ef0287c25bd7a41d37b6bcee4e1ea25b1101672fb45bd299ecec77b0d`
- Skill overlay SHA-256: `8f09b52303d9393824dd3e732e656dd74f7ac606a082939547181274986dfb2d`
- Judge schema SHA-256: `10a807298f91a20d6e9b68f75881e7ea6287d8afeff10727bea551d980d3535f`
- Eval definition SHA-256: `f3397b62fc4d049158e92b00f525e136ca990d6c804b1f211ce557bfaf30d03e`
- Metadata SHA-256: `de0335f1a182c8496f115f68dc77dc691a79abeae555386cc002141eada43865`
- Executor SHA-256: `ed1e952e9fe823936a2bd3d21b88e0b0d6870350be1dd767dd6052065f14b0eb`
- Evidence normalization: historical sections and transient Python bytecode exclusion were normalized without rerunning candidate or judge; recorded behavior and verdict are unchanged.
- Runtime SHA-256: `9ed43d4c2c0e4dbf09b289476d4fe9240c9ba0e61bc3ba75633ffd6e514d710d`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `mirrors_nested_feature_path` | PASS | with_skill TRD is delivered at docs/engineer/chat-interface/messages/history/search/TRD.md. |
| `preserves_feature_metadata` | PASS | TRD.md frontmatter contains feature_path, parent_feature, and feature_level: 4. |
| `related_prd_matches_path` | PASS | TRD.md frontmatter points related_prd to docs/pm/chat-interface/messages/history/search/PRD.md. |
| `blocks_on_missing_or_unclear_prd_path` | PASS | The fixture PRD clearly confirms the feature path and parent; with_skill records that confirmed basis and does not guess a top-level TRD. |
| `no_plan_or_code` | PASS | Locked git evidence shows only documentation files were added; candidate explicitly states no implementation plan or code was created. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4; fixture_sha256=9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc; output_sha256=c27f4993d51236b6da64c85a63baa40d807e7f20c558273b07107bc86fe6db73; snapshot_sha256=545af0a02ad1f0bf2fec28e0369225d61ad74d437e14ef21105effa825d38c31
- Behavior: Created the correctly nested Engineer TRD, API, and ADR with matching metadata and PRD linkage; downstream implementation remains blocked.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=8d0ccec5c9709506559aa1f8a5acdfd87e4bb71acf3bdaa8439f052c01aabae4; fixture_sha256=9c19cf5e49c59929ac5b070de11f3df7bfcbee1e79646cc4eec47c40b398a1bc; output_sha256=0aa203d3b339c28775caae297046c001d6c90328a37bcd8aceb8e753e91bd303; snapshot_sha256=aba096bb3d82eabcc96f1bdaa08c184a5aab33a30e70c5f469fabef979f34584
- Behavior: Created a TRD under docs/tech with the nested path, but used the wrong documentation root and source_prd metadata rather than the required Engineer output convention.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- This durable comparison retains only the latest reviewable conclusion; Git history preserves earlier revisions.
