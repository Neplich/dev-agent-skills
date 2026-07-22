# API Sync Instructions

Load this module only when the confirmed scope contains `doc_type: api`.

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
a separately confirmed migration plan.
