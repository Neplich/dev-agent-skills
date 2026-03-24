# cli/cli — Open PRs Awaiting Review

**Report date:** 2026-03-20
**Source:** `gh pr list --repo cli/cli --state open --limit 100`
**Total open PRs fetched:** 38

> Sorted by time waiting (oldest first). "Wait time" is calculated from the PR creation date to 2026-03-20.
> Tags: `[DRAFT]` = draft PR, `[BOT]` = automated/bot author, `[CHANGES_REQUESTED]` = reviewer has requested changes.

---

## All Open PRs Sorted by Wait Time (Longest First)

| # | PR | Author | Wait Time | Draft | Labels | Review Status |
|---|-----|--------|-----------|-------|--------|---------------|
| 1 | [#9847](https://github.com/cli/cli/pull/9847) [gh search issues] Support multiple author options | Shion1305 | **505d 18h** | DRAFT | — | REVIEW_REQUIRED |
| 2 | [#10253](https://github.com/cli/cli/pull/10253) Include headRepositoryId when creating a new PR | jacob-keller | **427d 23h** | DRAFT | — | REVIEW_REQUIRED |
| 3 | [#10273](https://github.com/cli/cli/pull/10273) Process `--jq` before `--template` | heaths | **424d 13h** | DRAFT | — | REVIEW_REQUIRED |
| 4 | [#10275](https://github.com/cli/cli/pull/10275) Support useful template functions and modules in jq filters | heaths | **423d 16h** | DRAFT | — | REVIEW_REQUIRED |
| 5 | [#10423](https://github.com/cli/cli/pull/10423) [gh env] Introduce `gh env list` subcommand | iamazeem | **400d 10h** | — | external | REVIEW_REQUIRED |
| 6 | [#10730](https://github.com/cli/cli/pull/10730) Add support for custom SSH and SCP commands via environment variables | cmbrose | **349d 5h** | — | — | REVIEW_REQUIRED |
| 7 | [#10783](https://github.com/cli/cli/pull/10783) fix: `gh cs logs` to use automatic ssh key pair | franciscoj | **339d 13h** | — | external | REVIEW_REQUIRED |
| 8 | [#11388](https://github.com/cli/cli/pull/11388) Add dynamic user switching based on git config gh.user (POC for #326) | MSch | **236d 8h** | DRAFT | — | REVIEW_REQUIRED |
| 9 | [#11500](https://github.com/cli/cli/pull/11500) Respect `--title` and `--body` in `pr create` web mode | babakks | **218d 14h** | DRAFT | — | REVIEW_REQUIRED |
| 10 | [#11569](https://github.com/cli/cli/pull/11569) Decompress responses | heaths | **209d 6h** | DRAFT | — | REVIEW_REQUIRED |
| 11 | [#11844](https://github.com/cli/cli/pull/11844) fix(pr create): keep tracking upstream at push if already set | babakks | **168d 10h** | DRAFT | — | REVIEW_REQUIRED |
| 12 | [#11977](https://github.com/cli/cli/pull/11977) fix: Find pull requests across repositories | jsoref | **150d 6h** | — | external | REVIEW_REQUIRED |
| 13 | [#12276](https://github.com/cli/cli/pull/12276) Add PGP key rotation PoC for RPM repositories | babakks | **101d 7h** | — | — | REVIEW_REQUIRED |
| 14 | [#12433](https://github.com/cli/cli/pull/12433) Add actions_orchestration_id as part of user-agent | TingluoHuang | **72d 1h** | DRAFT | external | REVIEW_REQUIRED |
| 15 | [#12460](https://github.com/cli/cli/pull/12460) Added a --screen-reader flag to gh status. Closes #6496. | trypsynth | **68d 21h** | — | external | REVIEW_REQUIRED |
| 16 | [#12581](https://github.com/cli/cli/pull/12581) Fix bump-go.sh to tolerate missing toolchain directive | app/copilot-swe-agent | **49d 4h** | DRAFT | [BOT] | REVIEW_REQUIRED |
| 17 | [#12622](https://github.com/cli/cli/pull/12622) feat(pr create): add --json and --jq output | LouisLau-art | **41d 21h** | — | external | CHANGES_REQUESTED |
| 18 | [#12682](https://github.com/cli/cli/pull/12682) Add supports for terminal hyperlinks in output (v2) | xzfc | **33d 22h** | DRAFT | external | REVIEW_REQUIRED |
| 19 | [#12725](https://github.com/cli/cli/pull/12725) Fix typo: remove extra space in README.md link | realMelTuc | **28d 5h** | — | external, needs-triage | REVIEW_REQUIRED |
| 20 | [#12859](https://github.com/cli/cli/pull/12859) Add experimental huh-only prompter gated by GH_EXPERIMENTAL_PROMPTER | BagToad | **12d 19h** | DRAFT | — | REVIEW_REQUIRED |
| 21 | [#12884](https://github.com/cli/cli/pull/12884) fix(issue): avoid fetching unnecessary fields for discovery | babakks | **10d 12h** | — | — | REVIEW_REQUIRED |
| 22 | [#12903](https://github.com/cli/cli/pull/12903) chore(deps): bump golang.org/x/text from 0.34.0 to 0.35.0 | app/dependabot | **8d 9h** | — | [BOT] dependencies, go | REVIEW_REQUIRED |
| 23 | [#12902](https://github.com/cli/cli/pull/12902) chore(deps): bump golang.org/x/term from 0.40.0 to 0.41.0 | app/dependabot | **8d 9h** | — | [BOT] dependencies, go | REVIEW_REQUIRED |
| 24 | [#12906](https://github.com/cli/cli/pull/12906) Don't count cancelled checks as failures in `pr status` | BagToad | **8d 5h** | — | — | REVIEW_REQUIRED |
| 25 | [#12909](https://github.com/cli/cli/pull/12909) Remove `ChecksStatus` slow path (dead code on all supported GHES) | BagToad | **8d 2h** | — | — | _(no decision)_ |
| 26 | [#12919](https://github.com/cli/cli/pull/12919) chore(deps): bump golang.org/x/crypto from 0.48.0 to 0.49.0 | app/dependabot | **7d 9h** | — | [BOT] dependencies, go | REVIEW_REQUIRED |
| 27 | [#12918](https://github.com/cli/cli/pull/12918) chore(deps): bump advanced-security/filter-sarif from 1.0.1 to 1.1 | app/dependabot | **7d 9h** | — | [BOT] dependencies, github_actions | REVIEW_REQUIRED |
| 28 | [#12938](https://github.com/cli/cli/pull/12938) fix: suggest gh auth refresh for GraphQL scope errors | raajheshkannaa | **5d 6h** | — | external, needs-triage, unmet-requirements | REVIEW_REQUIRED |
| 29 | [#12942](https://github.com/cli/cli/pull/12942) Add `--editor` flag to `gh issue edit` and `gh pr edit` | maxbeizer | **4d 5h** | — | external, needs-triage | REVIEW_REQUIRED |
| 30 | [#12943](https://github.com/cli/cli/pull/12943) browse: check commit existence for ambiguous decimal-only short hashes | mateenali66 | **4d 4h** | — | external, needs-triage | REVIEW_REQUIRED |
| 31 | [#12944](https://github.com/cli/cli/pull/12944) Rename install_linux.md to 1install_linux.md | ahamedjobayer081-spec | **3d 22h** | DRAFT | external, needs-triage | REVIEW_REQUIRED |
| 32 | [#12948](https://github.com/cli/cli/pull/12948) Clarify `gh run list --created` date syntax | DeoJin | **3d 10h** | — | external, needs-triage, unmet-requirements | REVIEW_REQUIRED |
| 33 | [#12951](https://github.com/cli/cli/pull/12951) chore(deps): bump azure/login from 2.3.0 to 3.0.0 | app/dependabot | **2d 9h** | — | [BOT] dependencies, github_actions | REVIEW_REQUIRED |
| 34 | [#12959](https://github.com/cli/cli/pull/12959) fix: preserve recovery file on pr create submit failure | raajheshkannaa | **1d 20h** | — | external, needs-triage, unmet-requirements | REVIEW_REQUIRED |
| 35 | [#12958](https://github.com/cli/cli/pull/12958) fix: route --visibility private through Search API to exclude internal repos | raajheshkannaa | **1d 20h** | — | external, unmet-requirements | REVIEW_REQUIRED |
| 36 | [#12963](https://github.com/cli/cli/pull/12963) chore(deps): bump google.golang.org/grpc from 1.79.2 to 1.79.3 | app/dependabot | **1d 9h** | — | [BOT] dependencies, go | REVIEW_REQUIRED |
| 37 | [#12962](https://github.com/cli/cli/pull/12962) chore(deps): bump github.com/google/go-containerregistry from 0.20.7 to 0.21.3 | app/dependabot | **1d 9h** | — | [BOT] dependencies, go | REVIEW_REQUIRED |
| 38 | [#12965](https://github.com/cli/cli/pull/12965) fix: show user-friendly progress labels in project commands | mango766 | **1d 8h** | — | external, unmet-requirements | REVIEW_REQUIRED |

---

## Summary by Category

### Non-Draft, Non-Bot PRs Awaiting Review (Highest Priority)

These are ready-to-review PRs from human contributors:

| # | PR | Author | Wait Time |
|---|-----|--------|-----------|
| 1 | [#10423](https://github.com/cli/cli/pull/10423) [gh env] Introduce `gh env list` subcommand | iamazeem | **400d 10h** |
| 2 | [#10730](https://github.com/cli/cli/pull/10730) Add support for custom SSH and SCP commands via environment variables | cmbrose | **349d 5h** |
| 3 | [#10783](https://github.com/cli/cli/pull/10783) fix: `gh cs logs` to use automatic ssh key pair | franciscoj | **339d 13h** |
| 4 | [#11977](https://github.com/cli/cli/pull/11977) fix: Find pull requests across repositories | jsoref | **150d 6h** |
| 5 | [#12276](https://github.com/cli/cli/pull/12276) Add PGP key rotation PoC for RPM repositories | babakks | **101d 7h** |
| 6 | [#12460](https://github.com/cli/cli/pull/12460) Added a --screen-reader flag to gh status. Closes #6496. | trypsynth | **68d 21h** |
| 7 | [#12622](https://github.com/cli/cli/pull/12622) feat(pr create): add --json and --jq output | LouisLau-art | **41d 21h** |
| 8 | [#12725](https://github.com/cli/cli/pull/12725) Fix typo: remove extra space in README.md link | realMelTuc | **28d 5h** |
| 9 | [#12884](https://github.com/cli/cli/pull/12884) fix(issue): avoid fetching unnecessary fields for discovery | babakks | **10d 12h** |
| 10 | [#12906](https://github.com/cli/cli/pull/12906) Don't count cancelled checks as failures in `pr status` | BagToad | **8d 5h** |
| 11 | [#12909](https://github.com/cli/cli/pull/12909) Remove `ChecksStatus` slow path (dead code on all supported GHES) | BagToad | **8d 2h** |
| 12 | [#12938](https://github.com/cli/cli/pull/12938) fix: suggest gh auth refresh for GraphQL scope errors | raajheshkannaa | **5d 6h** |
| 13 | [#12942](https://github.com/cli/cli/pull/12942) Add `--editor` flag to `gh issue edit` and `gh pr edit` | maxbeizer | **4d 5h** |
| 14 | [#12943](https://github.com/cli/cli/pull/12943) browse: check commit existence for ambiguous decimal-only short hashes | mateenali66 | **4d 4h** |
| 15 | [#12948](https://github.com/cli/cli/pull/12948) Clarify `gh run list --created` date syntax | DeoJin | **3d 10h** |
| 16 | [#12959](https://github.com/cli/cli/pull/12959) fix: preserve recovery file on pr create submit failure | raajheshkannaa | **1d 20h** |
| 17 | [#12958](https://github.com/cli/cli/pull/12958) fix: route --visibility private through Search API to exclude internal repos | raajheshkannaa | **1d 20h** |
| 18 | [#12965](https://github.com/cli/cli/pull/12965) fix: show user-friendly progress labels in project commands | mango766 | **1d 8h** |

### Statistics

- **Total open PRs:** 38
- **Draft PRs:** 14
- **Bot-authored PRs:** 8 (dependabot: 7, copilot-swe-agent: 1)
- **PRs with `CHANGES_REQUESTED`:** 1 (#12622)
- **PRs with no review decision yet:** 1 (#12909)
- **PRs waiting > 1 year:** 1 (#9847, 505 days)
- **PRs waiting > 100 days:** 13
- **PRs tagged `unmet-requirements`:** 7
- **PRs tagged `needs-triage`:** 9
- **PRs tagged `external`:** 20 (from outside the CLI core team)
