# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-001-unreleased-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-001-unreleased-mode`.
- Fixture SHA-256: `6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17`
- Prompt SHA-256: `43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `53f035563de038125d09b7a8997f87e900d099e00223f427a7c690e11ebbe449`
- Skill overlay SHA-256: `9534a5bf71391ac48cfd6a48ca8f80e93da520d6ea9d2026741fd864da0cb720`
- Judge schema SHA-256: `e87b7560e9b11fe6dfc954d0faa2696f04b98bb48f59af2eb521a8e8cfed4660`
- Eval definition SHA-256: `f643e5a44adc95dee4686543e115df7acb899ebc5dec146519d9991e82db553d`
- Metadata SHA-256: `95c0dae43621d97267d71f9000473df424f0f20875022c90f8a0826f1615ee52`
- Executor SHA-256: `69cd64edf8c82e7d3acfb3b8a11159a212cfe9a5b78fc994d0038dd18345990f`
- Runtime SHA-256: `dd143ad6f63df2577f2dff83225ec761f8a9cb05d96aab3f87ee37557e43c6e6`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `unreleased` | PASS | with_skill delivery_snapshot contains `## [Unreleased]`. |
| `pr` | PASS | Entries for PRs #310 and #311 include GitHub PR links with `(#number)` format. |
| `bot_pr_dependabot` | PASS | Raw evidence identifies #312 as authored by dependabot[bot]; it is absent from the with_skill file. |
| `chore_ci_test` | PASS | Raw evidence identifies #313 as CI-only internal maintenance; it is absent from the with_skill file. |
| `versioned_changelog_file` | PASS | with_skill delivery_snapshot directly contains `docs/changelog/changelog-unreleased.md`. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811; fixture_sha256=6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17; output_sha256=6a7129e162585b080cf049f1ecf331bdf61c3b14ef1684054c2485602de1b092; snapshot_sha256=68018826ff931ee3733f3af5ff445d5478f936b6e83cf72e81efe455cf6c1700
- Behavior: Generated the requested Unreleased changelog with user-facing PRs #310 and #311 while excluding dependency-bot and CI-only changes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811; fixture_sha256=6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17; output_sha256=a16c0fd13876947021e5df412cd6e7f6b04625cb1958edaec2967750b5ace9e7; snapshot_sha256=43d5eb13a1d02f71f5ceadd9de7e6a39d79931dac65f722043367da3b3476e2a
- Behavior: Generated a changelog containing user-facing PRs plus the dependency update #312; it excluded the CI-only change.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-001-unreleased-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-001-unreleased-mode`.
- Fixture SHA-256: `6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17`
- Prompt SHA-256: `43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `53f035563de038125d09b7a8997f87e900d099e00223f427a7c690e11ebbe449`
- Skill overlay SHA-256: `9534a5bf71391ac48cfd6a48ca8f80e93da520d6ea9d2026741fd864da0cb720`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f643e5a44adc95dee4686543e115df7acb899ebc5dec146519d9991e82db553d`
- Metadata SHA-256: `95c0dae43621d97267d71f9000473df424f0f20875022c90f8a0826f1615ee52`
- Executor SHA-256: `4759e3eb0124e65ac5500eacae6e1b3cbebfb40e2c8ffb34b2510845238a8a1e`
- Runtime SHA-256: `d518ba38e51999e7aa2b48e05b30b862bf7571b45a739209f707cd796de14a15`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `unreleased` | PASS | with_skill delivery_snapshot contains the exact heading ## [Unreleased]. |
| `pr` | PASS | Both with_skill changelog entries include GitHub PR links in (#310) and (#311) format. |
| `bot_pr_dependabot` | PASS | The with_skill file excludes dependabot PR #312. |
| `chore_ci_test` | PASS | The with_skill file excludes the chore dependency update #312 and internal CI change #313. |
| `versioned_changelog_file` | PASS | with_skill delivery_snapshot directly contains docs/changelog/changelog-unreleased.md. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811; fixture_sha256=6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17; output_sha256=b971b98f2d402f6728bae6bd3474a17163d9856c335c2119b18a51d1e3d5e579; snapshot_sha256=3eae32ed3f79e89f67bb9fb6e522919bcd154e7d8ea3a668ecfd086048b90d86
- Behavior: Created the required Unreleased file with PR-linked user-visible Added and Fixed entries, excluding dependency and CI-only changes.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811; fixture_sha256=6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17; output_sha256=826189cb7166b545a6864e5535b200df43a4a17108d33043fddb69a15111775b; snapshot_sha256=18ccafc549a4ee51ab52d8284baef521565b7e9e9c72988f33b7d440edf77fd7
- Behavior: Created the required file and headings, but included the dependency-maintenance PR #312.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-001-unreleased-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-001-unreleased-mode`.
- Fixture SHA-256: `6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17`
- Prompt SHA-256: `43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811`
- Repository HEAD: `19966d8caa4dbd319c21d0a540286a0f274cf253`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `fd6202eb001e4fcc8e818cb01c9c27ec290ab3c4edabd757735bf984bab469a4`
- Skill overlay SHA-256: `b53e1261ebb5c959b0bf29a37559e89f454013b911c855fd491809032b43b267`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f643e5a44adc95dee4686543e115df7acb899ebc5dec146519d9991e82db553d`
- Metadata SHA-256: `95c0dae43621d97267d71f9000473df424f0f20875022c90f8a0826f1615ee52`
- Executor SHA-256: `e75b266b25353129e41b9505482b256c4f1f809f4eb6ccc1cbecefe663a14631`
- Runtime SHA-256: `8c4a4ba5484af132c8cebb4bf5a10ccf8221fca2f7886b1fa40452042c1e572a`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `unreleased` | PASS | with_skill delivery snapshot contains exactly the required `## [Unreleased]` heading. |
| `pr` | PASS | Both included entries contain GitHub PR links in `([#310](...))` and `([#311](...))` format. |
| `bot_pr_dependabot` | PASS | with_skill omits PR #312, whose author is `dependabot[bot]`. |
| `chore_ci_test` | PASS | with_skill output contains only feature and bug entries; no chore, ci, or test internal changes are present. |
| `versioned_changelog_file` | PASS | Delivery snapshot and workspace status show `docs/changelog/changelog-unreleased.md` was created. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811; fixture_sha256=6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17; output_sha256=ea8f493dacef921361fcd88a6f8d5971807cc340ffb4b994200c079a4d268e03; snapshot_sha256=196211aa52607bd7dc1cff17131223c9175d02b40f18e555c1ed5cfa8df9b155
- Behavior: Created the requested Unreleased changelog, included user-facing PRs #310 and #311 with links, and excluded bot/dependency and CI maintenance PRs.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811; fixture_sha256=6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17; output_sha256=9e6759259ea41689e30ca16fa3764ad280a3a222e72f0cb556526c81cb3703f9; snapshot_sha256=dd7a11ab64bcc29cd6c7fb978219ac562313cc0082b4826c7a13fa12f54492eb
- Behavior: Created the requested file and heading with PR links, but included the dependency-maintenance bot PR #312.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-001-unreleased-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-001-unreleased-mode`.
- Fixture SHA-256: `6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17`
- Prompt SHA-256: `43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `fd6202eb001e4fcc8e818cb01c9c27ec290ab3c4edabd757735bf984bab469a4`
- Skill overlay SHA-256: `b53e1261ebb5c959b0bf29a37559e89f454013b911c855fd491809032b43b267`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f643e5a44adc95dee4686543e115df7acb899ebc5dec146519d9991e82db553d`
- Metadata SHA-256: `95c0dae43621d97267d71f9000473df424f0f20875022c90f8a0826f1615ee52`
- Executor SHA-256: `df470e672d809d58d28b784ae0b206dc66689c1eb5e12ed84f518fc870309d93`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `unreleased` | PASS | with_skill 快照包含 `## [Unreleased]` 标题。 |
| `pr` | PASS | with_skill 输出中的每个条目均包含 `([#310](...))` 或 `([#311](...))` 格式的 PR 链接。 |
| `bot_pr_dependabot` | PASS | 原始证据显示 #312 为 dependabot[bot]；with_skill 输出仅纳入 #310、#311，且明确跳过依赖更新。 |
| `chore_ci_test` | PASS | 原始证据中的 chore 依赖更新 #312 和 ci 内部维护 #313 均未出现在 with_skill 文件中。 |
| `versioned_changelog_file` | PASS | with_skill delivery_snapshot 和 git 状态均证明文件写入 `docs/changelog/changelog-unreleased.md`。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811; fixture_sha256=6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17; output_sha256=20759ed9c22335cd8f8d414e81638ff56a67e015e242e66c28b0f65a50d0aedf; snapshot_sha256=2bcdbbd67fe06761f679209a8dd382cbd7bdb3dc46d201e5c3eae57e18f520c8
- Behavior: 生成了符合要求的 Unreleased 章节，纳入 #310、#311，跳过 bot 依赖更新及内部 CI 维护，并写入目标路径。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811; fixture_sha256=6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17; output_sha256=b17c2b0e90335767e5835672d0cabb4fd3f3d8dddbe6a889f46d86b8b06dc986; snapshot_sha256=e861df5541114641845569263f2f2cc50dd818dc9586eb15e4816c4bfe90c696
- Behavior: 生成了目标文件并纳入 #310、#311、#312；跳过了 #313，但错误纳入了 dependabot 依赖维护 PR #312。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-001-unreleased-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-001-unreleased-mode`.
- Fixture SHA-256: `6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17`
- Prompt SHA-256: `43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811`
- Repository HEAD: `f33a08c427728fb9aa22fc5d146b1d725dcad4f5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `281e1b5c19a67eed1e87d8548e15e7ab23a90d7de9e0bd112a29df45200426a3`
- Skill overlay SHA-256: `f4e3f318f95aeaf018d947cb5144bbc03198d0d62d802018a4946522adbf8065`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `f643e5a44adc95dee4686543e115df7acb899ebc5dec146519d9991e82db553d`
- Metadata SHA-256: `95c0dae43621d97267d71f9000473df424f0f20875022c90f8a0826f1615ee52`
- Executor SHA-256: `bae0dfdc880ac55872337bb8b1e3be6fa01333a78ce2ecdda8aac9cb64c0ac57`
- Runtime SHA-256: `ab4b75f8a9f4eb280f5713c7e6797fcff90753ebaf0ddd07e2e0e28edcc6a9fd`
- Behavior result: **PASS**
- Coverage result: **FULL**
Overall result: PASS

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `unreleased` | PASS | with_skill 文件内容包含 ## [Unreleased] 标题。 |
| `pr` | PASS | 两个条目均包含指向 GitHub PR 的链接，分别为 (#310) 和 (#311)。 |
| `bot_pr_dependabot` | PASS | with_skill 输出未包含 dependabot PR #312。 |
| `chore_ci_test` | PASS | with_skill 输出未包含 chore/deps PR #312 或 ci PR #313。 |
| `versioned_changelog_file` | PASS | delivery_snapshot 和 workspace_manifest 均确认文件写入 docs/changelog/changelog-unreleased.md。 |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811; fixture_sha256=6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17; output_sha256=f7546a978b8198f2ee16d9c102d2900d6baae2ecc2fda242b29d3a344786b5f4; snapshot_sha256=c1fc320d6778cf589ab9f552b24d01060cabb739a13d50c89b3e1a8a6a59ac53
- Behavior: 生成了目标文件，包含 Unreleased 标题和有效 PR 链接，并跳过 dependabot、依赖维护及 CI 内部变更。
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=43cfb6c692393c921f5bd34fe732149f7950dd5ff91e898df22a516e60d25811; fixture_sha256=6c891edd0d2edaa974f9696bff7fd8bce1989edc225daec7356e08843c3ccf17; output_sha256=32746af8ed86fb0bcbf9928cdc2f64b33cb888f9f19de62d6e4f5896d36f2213; snapshot_sha256=eec3f1507d7ce333a9a3514bca1d26dcf9b9cc904da2e3158ae3d4f76ef7ab3f
- Behavior: 生成了目标文件、标题和 PR 链接，但纳入了应跳过的 dependabot 依赖更新 #312。
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: None.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Evaluation Result

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-001-unreleased-mode`

## Current Result

- Evidence status: **FRESH**
- Preflight status: **PASS**
- Judge: third independent fresh judge completed after both candidates were locked.
- Fixture version/source: canonical manifest `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a` from `agents/product_manager/test/changelog-gen/evals/workspace/eval-001-unreleased-mode`.
- Fixture SHA-256: `44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a`
- Prompt SHA-256: `816b4de603f11081701f38913293ff8bf45f51d9500e3f42bbaccf19e6d1cd7c`
- Repository HEAD: `4400ae28f989d139c65fdc4d3f711f6d7fbc2ee5`
- Repository worktree state: **DIRTY**
- Target skill tree SHA-256: `3dfcf246dc4057e8231ee4e2380b4525eeecf840a484daf60bd4e990283d5e5e`
- Skill overlay SHA-256: `5c214a0a2c2365016d6b3bafaa3e6cd9bb33067b007f4407a0b78fe50c4ba935`
- Judge schema SHA-256: `21d43403f9a89e052dc7c8f27bb7f6b25e3aac68a0c2bb24cb181a89e617d64a`
- Eval definition SHA-256: `d79133c1bbb156df00e2bf94905fa052c00f56ec190d786d942617fe98a1c3a2`
- Metadata SHA-256: `2e8886660979e8d508feb617ffafcb0337fa9f27576f749f4ff86dbac479ac74`
- Executor SHA-256: `7b65d7d7a30937e6b3b48ed51b563d70cd10d801a8c222649956a85efbe3ac48`
- Runtime SHA-256: `92bdfb539ae5a9bdf642c9b3eb735e3ccaf253ed3a4c99f8e136ca1d192d295a`
- Behavior result: **PASS**
- Coverage result: **PARTIAL**
Overall result: PASS (partial coverage)

## Assertion Results

| Assertion | Result | Evidence |
| --- | --- | --- |
| `unreleased` | PASS | with_skill delivery snapshot contains the exact heading ## [Unreleased]. |
| `pr` | NOT_EXERCISED | The with_skill output contains no entries, and the fixture directory provides no raw PR evidence to evaluate this criterion. |
| `bot_pr_dependabot` | NOT_EXERCISED | No raw PR list is present in the fixture, so skipping bot PRs cannot be independently verified. |
| `chore_ci_test` | NOT_EXERCISED | No raw PR list is present in the fixture, so exclusion of internal chore/ci/test changes cannot be independently verified. |
| `versioned_changelog_file` | PASS | with_skill workspace_manifest and delivery_snapshot both identify docs/changelog/changelog-unreleased.md. |

## With-Skill Behavior

- Run source: fresh with_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=816b4de603f11081701f38913293ff8bf45f51d9500e3f42bbaccf19e6d1cd7c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=90ecdbd4c1816b3377901ec9dc4c9d7a0253020fb3552f238e6d96491d81abdf; snapshot_sha256=72c252991da4d355b40317539f88c89a1dd688b867b6bf0c3d380a79fae226ff
- Behavior: Created the requested file with an Unreleased heading and claimed no user-facing changes after v0.120.2; no PR-level content was provided.
- The with-skill context was created only after the baseline evidence was locked and destroyed.

## Fresh Without-Skill Baseline

- Run source: fresh without_skill candidate; model=gpt-5.6-luna; effort=medium; returncode=0; timed_out=False; prompt_sha256=816b4de603f11081701f38913293ff8bf45f51d9500e3f42bbaccf19e6d1cd7c; fixture_sha256=44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a; output_sha256=f776d312c769cd3872fdba8394161ace8c6d8d9acb29b5fac9bb2510d590a6a5; snapshot_sha256=cabb63678d1342a76b66cc21488c626cbd56aefa8ed4e9080c9770e4ea43a080
- Behavior: Created the requested file with an Unreleased heading and claimed no changes after v0.121.0.
- The baseline was generated fresh first, its output and delivery snapshot were locked, then its context was destroyed.

## Failures and Next Steps

- None.
- Next: Provide the raw release and merged-PR fixture to evaluate the PR-content assertions.

## Runtime Artifact Policy

- Candidate outputs, snapshots, judge packages, verdict payloads, timing, diagnostics, and other runtime files are deleted before the runner exits, including after FAIL, BLOCKED, or exceptions.
- Only this durable comparison retains the reviewable conclusion and superseded history.

## Historical Context (Superseded)

# Issue #246 Migration Status

## Current Result

- Evidence status: **STALE**
- Migration status: **PENDING**
- Blocking reason: this eval has not yet been rerun under the Issue #246 scenario, lane-isolation, and fresh-judge contract.
Overall result: BLOCKED

## Historical Context (Superseded)

The complete pre-migration comparison follows unchanged. It is retained only as historical context and is not current release evidence.

---

# Eval Result: eval-001-unreleased-mode

## Evaluation Target

- Agent: `product_manager`
- Skill: `changelog-gen`
- Eval: `eval-001-unreleased-mode`
- Test case: `unreleased-mode`
- Prompt:

> 我在 https://github.com/anthropics/anthropic-sdk-python 这个仓库里工作。帮我生成 Unreleased 章节 —— 也就是最新 release tag 之后合并的所有 PR，写成 Keep a Changelog 格式，输出到 docs/changelog/changelog-unreleased.md。

- Expected output:

> 生成 ## [Unreleased] 章节，包含最新 release 之后的 PR 列表，按 Added/Changed/Fixed 分组，每条带 PR 链接，写入 docs/changelog/changelog-unreleased.md

## Test Set / Fresh Run

- Eval schema: `evals.json` v1.0。
- Fixture manifest: `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945`（0 个可见文件；两侧逐字节一致）。
- Repository HEAD: `47adbbc9`。
- Fresh run window: 2026-08-07 00:58–01:14（Asia/Shanghai）。
- Runtime: 3 个独立会话，均为 `gpt-5.6-luna`、`model_reasoning_effort=medium`：fresh without-skill、fresh with-skill、fresh judge。
- Controlled variable: 两个 candidate 使用完全相同的 prompt、fixture manifest、HOME/CODEX_HOME 目录形态与同一份 `auth.json`；唯一变量是 with-skill lane 安装并加载目标 specialist skill。
- Physical isolation: 按 skill 先完成并销毁全部 baseline 随机顶层根，再创建 with-skill 根；32 个 candidate 全部完成并销毁后才创建第三套 judge 根。
- Candidate visibility: lane 中未放入 `eval_metadata.json`、`evals.json`、`expected_output`、assertions、历史 `comparison.md`、README 脚手架或 judge 材料；泄漏扫描为 0 命中。
- External data rule: 实时实体因 GitHub 认证、网络或当时集合缺失而不可得时，相关 assertion 记为 `NOT EXERCISED`，只影响 Coverage，不伪造成 Behavior 的 PASS/FAIL。

## Latest Result

- Behavior result: **PASS**
- Coverage result: **PARTIAL**
- Overall result: PASS (partial coverage)
- With-skill summary: with_skill 实际加载了 changelog-gen（status.json skill_load_hits=2；transcript item_1 读取 SKILL.md），按要求创建并写入目标文件。trace 显示 Git/gh 查询分别因非 Git 工作区和未认证失败，网络查询也无可验证结果；因此 PR 相关断言无法覆盖。未发现读取评测脚手架泄漏。

## Historical Contract Note

- 旧 durable 结果因 issue #234 的 prompt/fixture 泄漏修复或后续 assertion 增强而标记为 `BLOCKED`。本文件已由当前契约下的 fresh paired run 与独立 judge 结论覆盖。
- 本轮没有复用历史 baseline、candidate、verdict 或旧结论；without-skill baseline 仅作行为对照，不参与 with-skill 的 Behavior/Coverage 判定。

## With-Skill Behavior

with_skill 实际加载了 changelog-gen（status.json skill_load_hits=2；transcript item_1 读取 SKILL.md），按要求创建并写入目标文件。trace 显示 Git/gh 查询分别因非 Git 工作区和未认证失败，网络查询也无可验证结果；因此 PR 相关断言无法覆盖。未发现读取评测脚手架泄漏。

## Without-Skill Baseline

without_skill 未加载 skill（skill_load_hits=0），但其 trace 也创建了目标文件并包含 Unreleased 标题；该结果仅作为对照，不影响 with_skill 判定。

## Assertion Review

| Assertion | With skill | Evidence / reason | Without-skill comparison |
| --- | --- | --- | --- |
| `unreleased` | **PASS** | with_skill trace item_16 读取到写入内容，其中包含 `## [Unreleased]`；after-snapshot.json 也确认目标文件已生成。 | without_skill trace item_17 的文件内容同样包含 `## [Unreleased]`。 |
| `pr` | **NOT EXERCISED** | PR 范围属于实时 GitHub 数据；with_skill 的 git 查询因 `not a git repository` 失败，gh 查询因未认证失败，网络查询无可验证返回，不能确认实际 PR 集合或据此判定链接格式。 | without_skill 也没有 PR 条目，trace item_17 仅写入 `No changes yet.`，因此 PR 链接格式未被实际练习。 |
| `bot_pr_dependabot` | **NOT EXERCISED** | 没有可验证的实时 PR 实体可供判断是否跳过 dependabot 等 bot PR；不能把无法取得数据等同于 PASS。 | without_skill 没有 PR 条目，bot PR 过滤未被实际练习。 |
| `chore_ci_test` | **NOT EXERCISED** | 没有可验证的实时 PR 实体及其标题/内容可供判断 chore/ci/test 过滤；相关查询基础设施不可用。 | without_skill 没有 PR 条目，内部变更过滤未被实际练习。 |
| `versioned_changelog_file` | **PASS** | with_skill trace item_14 创建目录，item_15 明确新增 `docs/changelog/changelog-unreleased.md`；after-snapshot.json 确认该路径存在，candidate.md 也提供了该文件链接。 | without_skill trace item_16 的 file_change 同样明确写入 `docs/changelog/changelog-unreleased.md`。 |

## Failures

- 无 with-skill assertion failure。

## Not Exercised

- pr
- bot_pr_dependabot
- chore_ci_test

## Next Steps

- 提供可用的 GitHub/Git 数据或预置 PR fixture 后重跑，以覆盖 PR 链接与过滤断言。

## Runtime Evidence

- With-skill candidate: return code `0`，duration `85.978s`，`skill_load_hits=2`。
- Without-skill candidate: return code `0`，duration `115.481s`，`skill_load_hits=0`。
- Independent judge: return code `0`，duration `90.851s`。
- Judge 已读取两侧最终输出、完整 JSONL 工具 trace、before/after workspace snapshot、fixture manifest 与 session status，并核验读取顺序和零写入边界。
- 所有临时 HOME/CODEX_HOME 与 candidate/judge 随机顶层根均已销毁；持久化证据目录中不存在 `auth.json`。

## Runtime Artifact Policy

- 仓库只持久化本 canonical `comparison.md`。
- Candidate、transcript、judge verdict、timing、status、snapshot 与 diagnostics 仅作为 `/tmp` 运行期证据，不提交到 git。
