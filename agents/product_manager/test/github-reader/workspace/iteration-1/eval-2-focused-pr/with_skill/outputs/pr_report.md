## 项目状态：cli/cli — 2026-03-20

### PR 队列

**待 Review（24 个，非草稿，按等待时间从长到短排序）：**

| # | 标题 | 作者 | 等待天数 |
|---|------|------|----------|
| [#10423](https://github.com/cli/cli/pull/10423) | [gh env] Introduce `gh env list` subcommand | @iamazeem | 400 天 |
| [#10730](https://github.com/cli/cli/pull/10730) | Add support for custom SSH and SCP commands via environment variables | @cmbrose | 349 天 |
| [#10783](https://github.com/cli/cli/pull/10783) | fix: `gh cs logs` to use automatic ssh key pair | @franciscoj | 339 天 |
| [#11977](https://github.com/cli/cli/pull/11977) | fix: Find pull requests across repositories | @jsoref | 150 天 |
| [#12276](https://github.com/cli/cli/pull/12276) | Add PGP key rotation PoC for RPM repositories | @babakks | 101 天 |
| [#12460](https://github.com/cli/cli/pull/12460) | Added a --screen-reader flag to gh status. Closes #6496. | @trypsynth | 68 天 |
| [#12725](https://github.com/cli/cli/pull/12725) | Fix typo: remove extra space in README.md link | @realMelTuc | 28 天 |
| [#12884](https://github.com/cli/cli/pull/12884) | fix(issue): avoid fetching unnecessary fields for discovery | @babakks | 10 天 |
| [#12909](https://github.com/cli/cli/pull/12909) | Remove `ChecksStatus` slow path (dead code on all supported GHES) | @BagToad | 8 天 |
| [#12906](https://github.com/cli/cli/pull/12906) | Don't count cancelled checks as failures in `pr status` | @BagToad | 8 天 |
| [#12903](https://github.com/cli/cli/pull/12903) | chore(deps): bump golang.org/x/text from 0.34.0 to 0.35.0 | @dependabot | 8 天 |
| [#12902](https://github.com/cli/cli/pull/12902) | chore(deps): bump golang.org/x/term from 0.40.0 to 0.41.0 | @dependabot | 8 天 |
| [#12919](https://github.com/cli/cli/pull/12919) | chore(deps): bump golang.org/x/crypto from 0.48.0 to 0.49.0 | @dependabot | 7 天 |
| [#12918](https://github.com/cli/cli/pull/12918) | chore(deps): bump advanced-security/filter-sarif from 1.0.1 to 1.1 | @dependabot | 7 天 |
| [#12938](https://github.com/cli/cli/pull/12938) | fix: suggest gh auth refresh for GraphQL scope errors | @raajheshkannaa | 5 天 |
| [#12943](https://github.com/cli/cli/pull/12943) | browse: check commit existence for ambiguous decimal-only short hashes | @mateenali66 | 4 天 |
| [#12942](https://github.com/cli/cli/pull/12942) | Add `--editor` flag to `gh issue edit` and `gh pr edit` | @maxbeizer | 4 天 |
| [#12948](https://github.com/cli/cli/pull/12948) | Clarify `gh run list --created` date syntax | @DeoJin | 3 天 |
| [#12951](https://github.com/cli/cli/pull/12951) | chore(deps): bump azure/login from 2.3.0 to 3.0.0 | @dependabot | 2 天 |
| [#12965](https://github.com/cli/cli/pull/12965) | fix: show user-friendly progress labels in project commands | @mango766 | 1 天 |
| [#12963](https://github.com/cli/cli/pull/12963) | chore(deps): bump google.golang.org/grpc from 1.79.2 to 1.79.3 | @dependabot | 1 天 |
| [#12962](https://github.com/cli/cli/pull/12962) | chore(deps): bump github.com/google/go-containerregistry from 0.20.7 to 0.21.3 | @dependabot | 1 天 |
| [#12959](https://github.com/cli/cli/pull/12959) | fix: preserve recovery file on pr create submit failure | @raajheshkannaa | 1 天 |
| [#12958](https://github.com/cli/cli/pull/12958) | fix: route --visibility private through Search API to exclude internal repos | @raajheshkannaa | 1 天 |

> 注：#12909 的 `reviewDecision` 为空（未设置），视为待 review。

**草稿 PR（13 个，暂不需要 review）：**

| # | 标题 | 作者 | 等待天数 |
|---|------|------|----------|
| [#9847](https://github.com/cli/cli/pull/9847) | [gh search issues] Support multiple author options | @Shion1305 | 505 天 |
| [#10253](https://github.com/cli/cli/pull/10253) | Include headRepositoryId when creating a new PR | @jacob-keller | 427 天 |
| [#10273](https://github.com/cli/cli/pull/10273) | Process `--jq` before `--template` | @heaths | 424 天 |
| [#10275](https://github.com/cli/cli/pull/10275) | Support useful template functions and modules in jq filters | @heaths | 423 天 |
| [#11388](https://github.com/cli/cli/pull/11388) | Add dynamic user switching based on git config gh.user (POC for #326) | @MSch | 236 天 |
| [#11500](https://github.com/cli/cli/pull/11500) | Respect `--title` and `--body` in `pr create` web mode | @babakks | 218 天 |
| [#11569](https://github.com/cli/cli/pull/11569) | Decompress responses | @heaths | 209 天 |
| [#11844](https://github.com/cli/cli/pull/11844) | fix(pr create): keep tracking upstream at push if already set | @babakks | 168 天 |
| [#12433](https://github.com/cli/cli/pull/12433) | Add actions_orchestration_id as part of user-agent | @TingluoHuang | 72 天 |
| [#12581](https://github.com/cli/cli/pull/12581) | Fix bump-go.sh to tolerate missing toolchain directive | @copilot-swe-agent | 49 天 |
| [#12682](https://github.com/cli/cli/pull/12682) | Add supports for terminal hyperlinks in output (v2) | @xzfc | 33 天 |
| [#12859](https://github.com/cli/cli/pull/12859) | Add experimental huh-only prompter gated by GH_EXPERIMENTAL_PROMPTER | @BagToad | 12 天 |
| [#12944](https://github.com/cli/cli/pull/12944) | Rename install_linux.md to 1install_linux.md | @ahamedjobayer081-spec | 3 天 |

**其他（Changes Requested，1 个）：**

| # | 标题 | 作者 | 等待天数 |
|---|------|------|----------|
| [#12622](https://github.com/cli/cli/pull/12622) | feat(pr create): add --json and --jq output | @LouisLau-art | 42 天 |

### 健康摘要

- 共 **37 个** open PR（含草稿）
- **24 个**非草稿 PR 待 review，其中 **3 个**等待超过 300 天（高风险积压）
- **13 个**草稿 PR，最老的 #9847 已挂 505 天
- Dependabot 依赖更新 PR 占待 review 总数约 40%，可考虑批量处理
- 等待最久的非 bot PR：[#10423](https://github.com/cli/cli/pull/10423)（@iamazeem，400 天）`gh env list` 子命令

#### 积压风险 TOP 3（非草稿，等待 > 90 天）

| # | 标题 | 等待 |
|---|------|------|
| [#10423](https://github.com/cli/cli/pull/10423) | [gh env] Introduce `gh env list` subcommand | 400 天 |
| [#10730](https://github.com/cli/cli/pull/10730) | Add support for custom SSH and SCP commands via environment variables | 349 天 |
| [#10783](https://github.com/cli/cli/pull/10783) | fix: `gh cs logs` to use automatic ssh key pair | 339 天 |
