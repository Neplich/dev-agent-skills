# Execution Log — github-reader skill

**Task**: 列出 cli/cli 仓库中等待 review 的 PR，按等待时间排序
**Executed at**: 2026-03-20
**Skill**: github-reader

---

## Step 1 — Establish repo context

```bash
gh repo view cli/cli --json nameWithOwner,url,defaultBranchRef,description
```

**Result**:
- `nameWithOwner`: cli/cli
- `url`: https://github.com/cli/cli
- `defaultBranchRef.name`: trunk
- `description`: GitHub's official command line tool

---

## Step 2 — Determine query scope

User asked specifically about PRs waiting for review → **Focused query** mode.
Skipped: milestones, issue fetching (not needed per skill guidance for focused PR queries).

---

## Step 3 — Fetch data

```bash
gh pr list \
  --repo cli/cli \
  --json number,title,state,author,reviewDecision,createdAt,labels,isDraft \
  --state open --limit 50
```

**Result**: 37 open PRs returned (limit 50, all PRs fit within one page).

---

## Step 4 — Compute health signals

**Criteria applied** (from skill spec):
- **PRs waiting review** = open PRs where `reviewDecision` is `REVIEW_REQUIRED` or null/empty, and `isDraft` is false
- **Draft PRs** = open PRs where `isDraft` is true
- Excluded: 1 PR with `CHANGES_REQUESTED` (#12622) — not waiting for review, author needs to act

**Waiting time** = `2026-03-20` minus `createdAt` date, in whole days.

**Counts**:
- Total open PRs: 37
- Awaiting review (non-draft): 24
- Draft: 13
- Changes requested: 1

**Sorting**: Descending by waiting days (longest wait first).

---

## Step 5 — Format output

Output written to `pr_report.md` following the skill's PR queue section format.
Milestones and issue sections omitted (focused query mode — PR-only).

---

## Notes

- PR #12909 (BagToad) had an empty `reviewDecision` string rather than `REVIEW_REQUIRED`, but was included as awaiting review per skill rule ("REVIEW_REQUIRED or null").
- Dependabot accounts for ~8 of the 24 awaiting-review PRs (dependency bumps). These are typically lower priority for manual review time.
- Three PRs have been waiting over 300 days: #10423, #10730, #10783 — significant backlog risk.
- Temp computation file `compute_prs.js` was created in the outputs directory during execution and can be deleted.
