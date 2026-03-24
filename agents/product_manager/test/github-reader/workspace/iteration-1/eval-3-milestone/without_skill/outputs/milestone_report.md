# facebook/react Milestone Progress Report

**Report Date:** 2026-03-20
**Repository:** https://github.com/facebook/react
**Data Source:** GitHub API via `gh` CLI

---

## Summary

Facebook/react has **39 milestones** in total (fetched via `?state=all`). Of those, **only 1 milestone is currently open**: `19.0.0` (milestone #40). All other 38 milestones are closed and at 100% completion.

---

## Open Milestones

| Milestone | Number | Open Issues | Closed Issues | Completion | Due Date | Created | Last Updated |
|-----------|--------|-------------|---------------|------------|----------|---------|--------------|
| 19.0.0    | #40    | 5           | 6             | 54.5%      | None     | 2017-11-26 | 2024-06-29 |

---

## Slowest / Most Overdue Milestone: **19.0.0**

### Key Finding

The milestone `19.0.0` is the **only open milestone** and is clearly the most problematic:

- **Created:** November 26, 2017
- **Last Updated:** June 29, 2024
- **Age:** Over **8 years** since creation (as of 2026-03-20)
- **Completion:** 54.5% (6 closed out of 11 total issues/PRs)
- **Due Date:** None set
- **Status:** Despite React 19.x having been released (latest: 19.2.4 on 2026-01-26), this milestone has **never been closed** and still has 5 open issues

### Ironically Stale

React 19.0.0 was actually shipped and is in wide use (versions up to 19.2.4 have been released), yet the GitHub milestone tracking `19.0.0` cleanup tasks is **still open** with 5 lingering issues from 2017-2018. This suggests the milestone was used to track breaking-change cleanup tasks, some of which were never completed.

---

## Open Issues in Milestone 19.0.0

| State | Type | Issue # | Title | Created | Last Updated |
|-------|------|---------|-------|---------|--------------|
| OPEN | Issue | #11972 | Consider removing mouseenter/mouseleave polyfill | 2018-01-05 | 2025-08-26 |
| OPEN | Issue | #11896 | Stop syncing value attribute for controlled inputs | 2017-12-20 | 2018-10-04 |
| OPEN | Issue | #11799 | Consider removing XML compatibility from SSR or hiding it behind an option | 2017-12-07 | 2020-08-25 |
| OPEN | Issue | #11667 | RFC: Drop isAttributeNameSafe() check | 2017-11-26 | 2023-04-21 |
| OPEN | Issue | #10143 | Remove unstable_renderIntoContainer | 2017-07-11 | 2020-01-08 |

**Oldest open issue:** #10143 "Remove unstable_renderIntoContainer" — opened **2017-07-11**, over **8.5 years ago**.

---

## Closed Issues in Milestone 19.0.0

| State | Type | Issue # | Title | Closed/Updated |
|-------|------|---------|-------|----------------|
| CLOSED | PR | #16555 | Add trusted types to react on server side | Updated 2022-10-20 |
| CLOSED | Issue | #13560 | Remove Factory Components | Updated 2024-06-29 |
| CLOSED | Issue | #13224 | Seal or Prevent Extensions on Pooled Events | Updated 2021-03-24 |
| CLOSED | Issue | #11689 | Remove support for TapEventPlugin | Updated 2021-03-24 |
| CLOSED | PR | #11639 | react-dom: remove support for children content in `<textarea/>` | Updated 2020-01-16 |
| CLOSED | PR | #2842 | Generate XML-compatible void tags and boolean attributes | Updated 2017-12-07 |

---

## Context: React's Actual Release Status

React has far surpassed 19.0.0 in terms of actual releases:

| Release | Date |
|---------|------|
| 19.2.4 (Latest) | 2026-01-26 |
| 19.1.5 | 2026-01-26 |
| 19.0.4 | 2026-01-26 |
| 19.0.3 | 2025-12-12 |
| 19.1.4 | 2025-12-12 |

The open milestone `19.0.0` was never formally closed on GitHub, even though the actual React 19.0.0 product shipped. This is a maintenance/housekeeping gap — the milestone acts as a backlog of originally-planned breaking changes that were deferred or deprioritized.

---

## Conclusion

**The 19.0.0 milestone (#40) is the only open milestone and is severely overdue by any measure:**

- It was created **8+ years ago** (November 2017) with no due date set.
- Completion is stuck at **54.5%** with 5 issues unresolved since 2017-2018.
- The actual React 19.0.0 product shipped, but these cleanup tasks were never finalized.
- The milestone has seen **no activity since June 2024** (last updated date).

The issues remaining open are all "consider removing" or "RFC" style tasks, suggesting they were intentionally deferred rather than forgotten — but the milestone itself was never closed or updated to reflect that decision. The team should either resolve these issues, close them as "won't fix/deferred," or close the milestone.
