# With Skill Transcript

## Project Context

- Directory: `agents/product_manager/test/idea-to-spec/workspace/iteration-1/eval-1-existing-project-feature`
- Status: existing-project
- Tech stack: web app with `package.json`; existing docs are partial
- Existing docs: engineering TRD for the apps catalog, no PM feature docs for app tags
- Suggested lane: `existing-project-feature`
- Likely next step: stay in `idea-to-spec`, form delta brief, then incrementally write PM docs

## Section 1: Scope And Goals

Here is the current delta brief:

- Current state: app catalog supports ingestion, admin editing, and frontend listing
- Target change: add app-level tags that can be managed in admin and surfaced in the frontend app catalog
- Constraints inherited from the current system: current search matches app name only; admin editing is modal-based; no existing tag model
- Open risk: whether tags should remain freeform metadata or become a managed object with bindings

Decision point:

- Option A: store `tags: string[]` directly on each app
  Trade-off: fastest v1, but weak for rename/delete/governance
- Option B: create `app_tags` and `app_tag_bindings`
  Trade-off: more work now, but supports clean rename/delete/filter behavior
- Option C: store tags in third-party app config
  Trade-off: avoids local schema work, but couples Portal display logic to integration config

Recommended default: Option B, because tag rename, delete, filtering, and cross-app reuse are product requirements rather than third-party integration settings.

Confirmed by evaluator for this run:

- Tags should be a Portal-owned concept, not part of third-party config
- Direction: managed tag model with bindings

Updated docs:

- `docs/pm/app-tags/DECISIONS.md`

## Section 2: Data Model And Query Semantics

Proposed data shape:

- `app_tags(id, name, normalized_name, created_at, updated_at, created_by, updated_by)`
- `app_tag_bindings(id, app_id, tag_id, created_at, created_by)`

Decision point:

- Option A: allow duplicate labels with different case
  Trade-off: flexible, but creates dirty filters and fragmented analytics
- Option B: enforce uniqueness on normalized name
  Trade-off: stricter, but gives stable filters, rename behavior, and deletion logic

Recommended default: Option B.

Confirmed by evaluator for this run:

- Tag names are case-insensitive unique through `normalized_name`

Updated docs:

- `docs/pm/app-tags/DECISIONS.md`
- `docs/pm/app-tags/design.md`

## Section 3: Interaction Shape

Proposed PM direction:

- Admin app form gets searchable multi-select plus inline tag creation
- User-facing apps page shows tag chips on cards
- Filtering uses explicit tag selection plus name search
- Tag deletion requires a confirmation modal when bindings exist

Current state after this eval run:

- Scope, model direction, and interaction direction are stable enough for a PM working draft
- The design has not yet been fully expanded into a complete PRD

Recommended next step:

- Continue in `idea-to-spec` until remaining sections are confirmed
- Keep `docs/pm/app-tags/design.md` as the working PM artifact
- Promote to `docs/pm/app-tags/PRD.md` once all sections are stable
