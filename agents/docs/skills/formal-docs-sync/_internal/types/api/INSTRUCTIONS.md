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
