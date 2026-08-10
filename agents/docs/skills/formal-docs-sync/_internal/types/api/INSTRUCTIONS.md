# API Sync Instructions

Load this module only when a confirmed write scope or an explicitly requested
read-only candidate-planning scope contains `doc_type: api`.

## Evidence Checks

Use direct implementation and contract evidence to verify, as applicable:

- route method and path, handler, and calling purpose;
- authentication, authorization, and role behavior;
- path, query, header, and request-body fields, types, requiredness, defaults,
  and validation constraints;
- success status and response schema;
- error status and error structure;
- streaming termination, content type, and upload/download headers;
- contract, route, schema, and integration tests.

Unsupported fields or behaviors remain unresolved. Do not infer an interface
from a process document when route, schema, handler, or test evidence differs.

## Template and Output Rules

Read the API template linked from the host
`docs/site/standards/index.md`—normally
`docs/site/standards/templates/api-template.md`—and consume its single
`docs-scaffold` block for a new page. Do not copy the template into this skill.

The page must describe the current interface scope, inventory, requests,
responses, errors, and evidence that actually apply. Remove empty placeholder
sections or rows rather than presenting them as facts. Keep API pages and their
API change-map entries in the same confirmed write/read-back scope.

Set `visibility: internal` for new or synced API pages and indexes, including
`docs/site/api/index.md`, unless the confirmed write scope explicitly
authorizes external developer access and states `public` or `both`. For an
existing ancestor index, this default applies only when the ancestor has no
existing `public` or `both` descendant outside the current batch; otherwise
keep the ancestor's existing visibility so out-of-batch public pages remain
reachable from the API root through public navigation.
This default prevents unconfirmed interface details from becoming externally
visible; the two exceptions above are explicit host authorization and
preserving an existing public navigation path.

## Information Architecture

Derive the path hierarchy from confirmed `feature_path` or feature catalog
nodes, then corroborate it with route prefixes/tags, handler ownership, schema,
and contract tests. Use `docs/site/api/index.md` only for global scope and
top-level domain navigation. Give every feature domain and every intermediate
subfeature its own directory and `index.md`; use lower kebab-case for all new
segments.

If no feature catalog exists, first scan API entry points, route prefixes and
tags, schemas, handler ownership, and contract tests. Use that evidence to form
one bounded top-level route group with every ancestor index and route leaf;
show the per-node code glob, owner gap, page, mapping delta, and exclusions,
then wait for confirmation. Discovery without a catalog never authorizes
whole-repository generation or immediate writes.

Leaf pages normally represent one independently understandable route. Merge a
tight route group only when all routes share the same reader task, owner,
lifecycle, and contract boundary. Source-file co-location or page length alone
does not justify merging. Whether split or grouped, every confirmed route must:

- be directly locatable from its immediate parent index and reachable from the
  API root through each ancestor index;
- have a distinct leaf page or page anchor;
- document method, path, authentication/authorization, request, response,
  errors, and implementation/test evidence.

Before writing, present the entire candidate API tree. For each domain,
subfeature, index, and leaf, show its parent, page path, code glob, owner,
classification evidence, proposed change-map delta, and exclusions. After
confirmation, write the complete subtree atomically with its indexes,
navigation, and map entries. Do not move an existing stable flat page without
a separately confirmed migration plan, and do not let that constraint end in
silence: run the common flat-hierarchy drift check with its own two-tier
threshold and resolved-page exceptions rather than a narrower API-specific
trigger. For this type, the evidence that places a page directly under
`docs/site/api/` beneath a domain or subfeature node is route prefix or tag,
handler ownership, and catalog classification. Propose the resulting migration
in the same confirmation instead of appending this batch's pages to the API
root.

### API flat-hierarchy checkpoint

Before presenting that confirmation, inventory every non-`index.md` page
directly under `docs/site/api/` and join each page's frontmatter to the feature
catalog by `related_code`, owner, route prefix/tag, or `feature_path`. Group all
pages that share the catalog's first feature-path/domain parent together even
when only one page is in the current batch. Do not abbreviate or omit the other
groups as “remaining API pages.”

Render the resulting inventory through the common `Hierarchy drift` schema in
`../../INSTRUCTIONS.md` before the candidate API tree. For every positive
in-batch group, enumerate each old path and target path plus its inbound-link,
recursive-navigation, and change-map `required_docs` deltas, and include all
three maintainer choices. For every positive out-of-batch group, enumerate its
page list and target node and keep it read-only. If any root page is unassigned
or any required delta is incomplete, stop and finish the checkpoint instead of
returning a shortened migration proposal.

For each positive in-batch group, render a mandatory migration-delta table with
one row per old path and these non-optional columns: `old_path`, `target_path`,
`inbound_link_delta`, `recursive_navigation_delta`, and
`required_docs_before_after`. Derive inbound links from the current root index,
navigation configuration, and repository links; if none exist, write `none`
with the checked evidence paths. The navigation cell names every affected
parent-child level. The mapping cell names each affected `code_glob` and its
exact `required_docs` list before and after migration. A group-level summary or
one representative row does not complete this table. Present the table before
the three maintainer choices.
