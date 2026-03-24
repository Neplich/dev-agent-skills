# Execution Log — cli/cli Open PRs Awaiting Review

**Task:** Fetch all open PRs from cli/cli waiting for review, sorted by wait time
**Executed:** 2026-03-20
**Method:** No skill guidance — self-directed approach

---

## Steps Taken

### Step 1: Fetch PR Data via gh CLI

**Command:**
```
gh pr list --repo cli/cli --state open --limit 100 --json number,title,createdAt,updatedAt,author,reviewDecision,labels,isDraft
```

**Result:** Successfully retrieved 38 open PRs.

**Fields requested:**
- `number` — PR number
- `title` — PR title
- `createdAt` — creation timestamp (used to compute wait time)
- `updatedAt` — last update timestamp
- `author` — includes `login`, `name`, `is_bot`
- `reviewDecision` — one of: `REVIEW_REQUIRED`, `APPROVED`, `CHANGES_REQUESTED`, or empty
- `labels` — label names for filtering/categorization
- `isDraft` — whether the PR is a draft

### Step 2: Compute Wait Time

Wait time = `2026-03-20T00:00:00Z` minus `createdAt`.

Using Node.js to process the JSON and compute `days` + `hours` for each PR.

### Step 3: Sort and Classify

- All 38 PRs sorted descending by total hours waiting.
- Classified into:
  - Bot-authored (dependabot, copilot-swe-agent)
  - Draft PRs
  - `unmet-requirements` labeled PRs
  - `needs-triage` labeled PRs
  - `external` labeled PRs (from outside CLI core team)

### Step 4: Create Output Directory

The target directory did not exist and was created:
```
D:/AI/Dev/neplich-skills/agents/product_manager/test/github-reader/workspace/iteration-1/eval-2-focused-pr/without_skill/outputs/
```

### Step 5: Write Output Files

- `pr_report.md` — full sorted table + priority sub-table + statistics
- `execution_log.md` — this file

---

## Key Observations

1. **Oldest PR is 505 days old:** #9847 "[gh search issues] Support multiple author options" (draft, opened 2024-10-30) has been waiting over a year and a half.

2. **13 PRs are over 100 days old**, indicating a significant backlog.

3. **14 of 38 PRs are drafts** — these typically aren't ready for review, so the effective review queue is 24 non-draft PRs.

4. **8 bot PRs** (mostly dependabot dependency bumps) are included in the count; these generally need merge approval rather than code review.

5. **The `unmet-requirements` label** appears on 7 PRs, meaning the core team has already flagged these as not meeting requirements — unlikely to be merged without significant changes.

6. **Only 1 PR has `CHANGES_REQUESTED`** (#12622) and 1 has no review decision at all (#12909 by BagToad, a core team member).

7. **The busiest contributor awaiting review** is `babakks` (Babak K. Shandiz) with 5 PRs open, and `heaths` (Heath Stewart) with 3.

---

## Data Limitations

- `limit 100` was used; the actual number of open PRs is 38, so no truncation occurred.
- Wait time is computed from `createdAt`, not from when a review was last requested. For PRs that have gone through several rounds (like #12622 with CHANGES_REQUESTED), "wait time" reflects time since first opened, not since last action was taken.
- No review comment data was fetched; a PR may have active discussion even if `reviewDecision` is still `REVIEW_REQUIRED`.
