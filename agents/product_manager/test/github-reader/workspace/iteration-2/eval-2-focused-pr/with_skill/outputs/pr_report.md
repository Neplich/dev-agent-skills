## PR 队列：cli/cli — 2026-03-20

**待 Review — 人工贡献（17 个，按等待时间排序）：**

| # | 标题 | 作者 | 等待 | 标签 |
|---|------|------|------|------|
| [#10423](https://github.com/cli/cli/pull/10423) | [gh env] Introduce `gh env list` subcommand | @iamazeem | 400 天 | external |
| [#10730](https://github.com/cli/cli/pull/10730) | Add support for custom SSH and SCP commands via environment variables | @cmbrose | 349 天 | - |
| [#10783](https://github.com/cli/cli/pull/10783) | fix: `gh cs logs` to use automatic ssh key pair | @franciscoj | 339 天 | external |
| [#11977](https://github.com/cli/cli/pull/11977) | fix: Find pull requests across repositories | @jsoref | 150 天 | external |
| [#12276](https://github.com/cli/cli/pull/12276) | Add PGP key rotation PoC for RPM repositories | @babakks | 101 天 | - |
| [#12460](https://github.com/cli/cli/pull/12460) | Added a --screen-reader flag to gh status. Closes #6496. | @trypsynth | 68 天 | external |
| [#12725](https://github.com/cli/cli/pull/12725) | Fix typo: remove extra space in README.md link | @realMelTuc | 28 天 | needs-triage, external |
| [#12884](https://github.com/cli/cli/pull/12884) | fix(issue): avoid fetching unnecessary fields for discovery | @babakks | 10 天 | - |
| [#12909](https://github.com/cli/cli/pull/12909) | Remove `ChecksStatus` slow path (dead code on all supported GHES) | @BagToad | 8 天 | - |
| [#12906](https://github.com/cli/cli/pull/12906) | Don't count cancelled checks as failures in `pr status` | @BagToad | 8 天 | - |
| [#12938](https://github.com/cli/cli/pull/12938) | fix: suggest gh auth refresh for GraphQL scope errors | @raajheshkannaa | 5 天 | needs-triage, external, unmet-requirements |
| [#12943](https://github.com/cli/cli/pull/12943) | browse: check commit existence for ambiguous decimal-only short hashes | @mateenali66 | 4 天 | needs-triage, external |
| [#12942](https://github.com/cli/cli/pull/12942) | Add `--editor` flag to `gh issue edit` and `gh pr edit` | @maxbeizer | 4 天 | needs-triage, external |
| [#12948](https://github.com/cli/cli/pull/12948) | Clarify `gh run list --created` date syntax | @DeoJin | 3 天 | needs-triage, external, unmet-requirements |
| [#12965](https://github.com/cli/cli/pull/12965) | fix: show user-friendly progress labels in project commands | @mango766 | 1 天 | external, unmet-requirements |
| [#12959](https://github.com/cli/cli/pull/12959) | fix: preserve recovery file on pr create submit failure | @raajheshkannaa | 1 天 | needs-triage, external, unmet-requirements |
| [#12958](https://github.com/cli/cli/pull/12958) | fix: route --visibility private through Search API to exclude internal repos | @raajheshkannaa | 1 天 | external, unmet-requirements |

**Bot/自动化 PR（8 个，可批量处理）：**
- Copilot SWE Agent: 1 个, Dependabot: 7 个

**草稿（12 个）：**
- [#9847 [gh search issues] Support multiple author options](https://github.com/cli/cli/pull/9847) — @Shion1305, 505 天
- [#10253 Include headRepositoryId when creating a new PR](https://github.com/cli/cli/pull/10253) — @jacob-keller, 427 天
- [#10273 Process `--jq` before `--template`](https://github.com/cli/cli/pull/10273) — @heaths, 424 天
- [#10275 Support useful template functions and modules in jq filters](https://github.com/cli/cli/pull/10275) — @heaths, 423 天
- [#11388 Add dynamic user switching based on git config gh.user (POC for #326)](https://github.com/cli/cli/pull/11388) — @MSch, 236 天
- [#11500 Respect `--title` and `--body` in `pr create` web mode](https://github.com/cli/cli/pull/11500) — @babakks, 218 天
- [#11569 Decompress responses](https://github.com/cli/cli/pull/11569) — @heaths, 209 天
- [#11844 fix(pr create): keep tracking upstream at push if already set](https://github.com/cli/cli/pull/11844) — @babakks, 168 天
- [#12433 Add actions_orchestration_id as part of user-agent](https://github.com/cli/cli/pull/12433) — @TingluoHuang, 72 天
- [#12682 Add supports for terminal hyperlinks in output (v2)](https://github.com/cli/cli/pull/12682) — @xzfc, 33 天
- [#12859 Add experimental huh-only prompter gated by GH_EXPERIMENTAL_PROMPTER](https://github.com/cli/cli/pull/12859) — @BagToad, 12 天
- [#12944 Rename install_linux.md to 1install_linux.md](https://github.com/cli/cli/pull/12944) — @ahamedjobayer081-spec, 3 天

**需作者跟进（Changes Requested，1 个）：**
- [#12622 feat(pr create): add --json and --jq output](https://github.com/cli/cli/pull/12622) — @LouisLau-art

### 健康摘要
- 共 38 个 open PR
- 17 个人工 PR 待 review
- 12 个草稿 PR
- 8 个 Bot PR
- 1 个需作者跟进
- ⚠️ 积压风险（等待 > 90 天的人工 PR）：5 个
