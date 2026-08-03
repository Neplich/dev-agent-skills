---
name: structure-governance
description: Audit the cross-role feature document tree and propose evidence-based merges, splits, or moves without modifying repository documents. Use when users ask for document structure governance, feature tree cleanup, feature_path reorganization, orphan detection, or cross-role path alignment.
---

# Document Structure Governance

Audit the repository's feature document tree across PM, Engineer, Design, QA,
DevOps, and Security. Produce a read-only HTML report with evidence-based
recommendations; never reorganize documents as part of this analysis.

## When to use

- Reviewing the repository feature tree or planning document cleanup.
- Investigating overlong docs, misplaced siblings, duplicate ownership,
  orphans, or cross-role `feature_path` drift.
- Preparing merge, split, or move proposals before user approval.
- **Analysis only** — prompts and reports are read-only. Later structural work
  is a separate `major` change under the repository change-tier contract.

## Scope

Scan all six role roots:

| Role | Scan root | Feature-path interpretation |
| --- | --- | --- |
| PM | `docs/pm/` | `docs/pm/{feature_path}/`; PRD ownership is the primary product-tree evidence |
| Engineer | `docs/engineer/` | `docs/engineer/{feature_path}/`; compare TRD, active implementation plan, API, and ADR ownership with PM |
| Design | `docs/design/` | `docs/design/{feature_path}/`; treat feature-scoped design artifacts as PM mirrors |
| QA | `docs/qa/` | Recognize E2E feature assets only through `docs/qa/e2e/{feature_path}/` and its existing contract |
| DevOps | `docs/devops/` | `docs/devops/{feature_path}/` for feature-scoped operational artifacts |
| Security | `docs/security/` | `docs/security/{feature_path}/` for feature-scoped review artifacts |

- Scan `docs/qa/` completely for inventory, but derive QA feature nodes only
  from the existing E2E structure: `TEST_SUITE.md`, `FLOW_INDEX.md`, `cases/`,
  `scripts/`, `results/`, and `_reports/` under
  `docs/qa/e2e/{feature_path}/`. Do not redefine or migrate that contract.
- Treat QA release-wide reports and shared login flows as shared or repo-wide
  assets, not as orphan feature nodes merely because they lack a PM mirror.
- Exclude `docs/site/` from scanning, recommendations, and restructuring. The
  formal documentation site remains owned by Docs Agent.
- Do not infer feature ownership from generated or runtime directories outside
  the six role roots.

## Workflow

### 1. Inventory and build the current tree

1. Confirm the repository root and verify which of the six role roots exist.
2. Recursively inventory directories and Markdown files. Missing roots are scan
   facts, not directories to create.
3. For each feature-scoped candidate, collect its path, role, line count,
   headings, document type, canonical filename, `feature_path`, `feature`,
   `parent_feature`, `feature_level`, `related_docs`, `related_prd`,
   `related_trd`, legacy references, and parent PRD child links.
4. Derive the path-implied `feature_path` from the role mirror location. For
   QA E2E, derive it only from the segments after `docs/qa/e2e/` and before the
   recognized E2E asset.
5. Build a role-aware tree keyed by PM `feature_path`; attach exact-path role
   mirrors and retain unmatched paths. For every node report parent/children,
   PM owner, role artifacts, frontmatter-versus-directory path, explicit links,
   and canonical/legacy/shared/unresolved status.
6. Preserve uncertainty. Never silently normalize missing metadata, legacy
   single-level docs, or repository-wide artifacts.

Do not require a physical parent PRD for reserved namespace parents whose
existing contract permits the namespace itself to act as the parent. Do not
mistake `docs/engineer/{feature_path}/implementation-plans/archive/` for a child
feature: it is archived implementation-plan storage within the owning feature.

### 2. Detect structure problems

Record each finding with a report-local ID, severity, confidence, evidence,
rationale, affected roles, and references:

1. **Overlong document**
   - Any document over 500 total lines is a critical structure finding.
   - Also record the other L2b signals: at least 3 independent domains, at
     least 15 US/FR table rows, or sections clearly owned by different child
     features. Signals require evaluation, never an automatic split.
2. **Misaligned siblings**
   - A feature is represented as a top-level or sibling path even though its
     content, explicit links, or parent index identifies an existing parent.
   - The same logical feature appears at different depths across role roots.
3. **Duplicate ownership**
   - Two or more paths claim the same feature scope, requirement IDs, or
     canonical downstream ownership.
   - Similar names alone are insufficient; cite overlapping content or links
     and mark semantic inference confidence.
4. **Orphans**
   - A downstream feature-scoped artifact has no identifiable PM owner or
     points to a missing PRD/TRD.
   - A child path has neither a valid parent relationship nor an allowed
     namespace-parent rule.
   - Do not classify shared QA assets, release-wide QA reports, or archived
     implementation plans as orphans solely because they lack direct mirrors.
5. **Cross-role mirror missing or drifted**
   - A required or explicitly referenced role artifact is missing at the exact
     PM `feature_path`.
   - Directory paths, frontmatter fields, parent relationships, child indexes,
     or `related_*` links disagree across roles.
   - Distinguish a genuinely required mirror from a role that has no artifact
     requirement for the feature; absence alone is not always a defect.

Heuristic matches remain uncertain findings with evidence and a confirmation
question, never confirmed defects.

### 3. Form recommendations

Recommend the smallest suitable action: merge, L2a sibling supporting-doc
split, L2b child-`feature_path` split, move, metadata/link alignment, or no
structural action. Every recommendation includes:

- **Current and target state**: exact source paths, conflicting ownership,
  proposed `feature_path` tree, and target paths.
- **Evidence and rationale**: applicable rule and repository evidence.
- **Content mapping**: map current sections/documents to targets so nothing is
  silently lost.
- **Mirror impact**: affected paths in `docs/pm`, `docs/engineer`,
  `docs/design`, `docs/qa/e2e`, `docs/devops`, and `docs/security`, including
  explicit `no artifact found` entries.
- **Reference impact**: metadata, parent PRD `child_features` index, `related_docs`,
  `related_prd`, `related_trd`, and other direct links that would need updates.
- **Approval needed**: the user decision required before execution.

An L2b recommendation is a proposal only. It must show the proposed child
`feature_path` tree, section migration map, and downstream mirror impact list.
If the user rejects it, preserve the current structure and continue the
existing document flow.

### 4. Apply execution constraints to every proposal

The report must state these constraints for any later approved implementation:

1. A move or split synchronizes `feature_path`, `parent_feature`,
   `feature_level`, `related_docs`, and the parent PRD `child_features` index.
2. Directory moves and file renames use `git mv`; never replace them with
   create-plus-delete. In a pure split, use `git mv` for the file that carries
   the original document body, then create additional child documents normally.
3. Before moving a PM directory, present the complete mirror impact list and
   wait until the user confirms how each mirror will be handled.
4. Keep `docs/engineer/{feature_path}/implementation-plans/archive/` archived;
   never reactivate or reinterpret archived plans.
5. Preserve QA history: files under QA `results/` are append-only and must not
   be overwritten during a move or split.
6. Preserve content traceability: every source section must map to a target
   document, and each changed formal document records the migration in its
   frontmatter changelog.
7. Treat the approved structural implementation as `change_tier: major` and
   route it through the normal PM handoff and confirmation gates. The audit,
   prompts, and report themselves remain read-only.

This module never performs the moves itself.

### 5. Write the runtime HTML report

1. Use `mktemp -d` under `$TMPDIR` (or `/tmp`) and never write the report under
   the repository.
2. Write one self-contained UTF-8 HTML file named
   `structure-governance-report.html` in that directory. Keep styles and any
   filtering behavior inline so the report can be opened directly.
3. Include these sections:
   - scope, scan time, scanned roots, exclusions, and limitations
   - feature tree overview with role coverage
   - summary counts by finding category and severity
   - detailed problem list with evidence and confidence
   - merge/split/move recommendations with target trees and impact surfaces
   - approval checklist and the execution constraints above
4. HTML-escape paths and extracted text. Include concise evidence only, not
   complete repository documents.
5. Verify the file exists, is outside the repository, and contains all required
   sections. Report the absolute temporary path to the user. Do not add or stage
   the HTML file in git.

### 6. Return a conversation summary

Summarize feature-node and artifact counts, critical/high-confidence findings
by category, key proposals, unresolved ownership questions, the absolute HTML
path, and the fact that no repository document was modified.

Do not execute a recommendation in the same turn. Wait for the user to approve
the proposed target tree and mirror handling through the normal PM flow.

## Output Contract

- **Primary artifact**: self-contained HTML report in a runtime temporary
  directory outside the repository
- **Conversation output**: concise finding and recommendation summary plus the
  absolute report path
- **Repository changes**: none
- **Required recommendation fields**: current state, evidence, target state,
  content mapping, six-role mirror impact, reference impact, and approval
  needed

## Failure Handling

- No `docs/` directory -> return a read-only empty-scan summary; do not create
  document roots.
- One or more role roots missing -> scan the remaining roots and list the
  missing roots as limitations, not automatic defects.
- Invalid or unreadable frontmatter -> use path and heading evidence, mark the
  finding unresolved, and do not guess corrected metadata.
- Ambiguous duplicate or parent ownership -> report candidate mappings with
  confidence and ask for confirmation.
- Temporary report write fails -> return the complete conversation summary and
  the error; do not fall back to writing inside the repository.

## Safety Boundaries

- Read-only: do not modify, move, rename, create, or delete repository
  documents, directories, indexes, links, or metadata.
- Do not run `git mv` in this module; it is a constraint for a later approved
  implementation.
- Do not stage, commit, push, or open a pull request.
- Do not change the QA E2E asset contract or overwrite historical results.
- Do not scan, audit, or restructure `docs/site/`.
- Do not access external URLs; base findings on repository evidence supplied in
  the scan.
