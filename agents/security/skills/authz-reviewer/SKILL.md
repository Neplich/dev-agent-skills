---
name: authz-reviewer
description: "Review authentication, authorization, tenant isolation, and session lifecycle against actual identities, resources, and server-side enforcement."
---

# Authentication and Authorization Review

Identify principals, roles, resources, actions, ownership, and tenant boundaries
from the request, routes, services, tests, and available product evidence.
Build an expected-versus-implemented permission matrix where it helps expose
gaps.

## Trace enforcement

1. Follow login, signup, recovery, and identity-provider callbacks through
   validation and account/session creation.
2. Inspect password hashing, token verification, expiration, refresh, revocation,
   session rotation, logout, and relevant cookie properties.
3. Trace authorization from entry point to the protected operation. Check role,
   object ownership, tenant context, and server-side enforcement.
4. Exercise differences between anonymous, ordinary, elevated, and cross-tenant
   access using safe test identities where authorized.
5. Check alternate routes, bulk operations, background jobs, exports, and
   indirect object references sharing the same resources.

A report includes the resource/action matrix, affected code, reproduction or
trace evidence, preconditions, impact, and proposed correction. Distinguish a
permission design choice from an implementation defect when expectations are
uncertain. Verify legitimate access and denied access when applying a fix.
