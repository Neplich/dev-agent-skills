---
name: appsec-checklist
description: "Review code for injection, XSS, authorization failures, unsafe file handling, secret exposure, and security-sensitive configuration."
---

# Application Security Review

Map the requested surface's inputs, transformations, storage, external calls,
and outputs. Identify the relevant attacker control and trust boundaries from
actual code. Follow candidate paths far enough to verify reachability and
existing mitigations.

## Review surfaces

- SQL, shell, template, and interpreter inputs: parameterization, validation,
  escaping, and the context in which values are executed.
- Browser output: encoding, HTML sinks, script handling, and content policies.
- Authentication and authorization: identity validation, ownership, permissions,
  tenant boundaries, and enforcement on the server.
- Sessions and tokens: issuance, storage, expiration, revocation, and transport.
- Uploads and file access: path resolution, type handling, storage, size limits,
  and exposure to execution or unauthorized reads.
- Remote requests and callbacks: destination control, credentials, redirects,
  verification, and access to internal resources.
- Sensitive data: secret storage, logs, errors, transport, and persistence.
- Configuration and dependencies: actual deployed defaults and relevant
  vulnerable behavior.

For each finding, record file and line, attacker preconditions, source-to-sink
path, existing defenses, impact, and a focused repair. Assign severity from the
actual exploit conditions and affected assets. Label unverified paths and
explain what evidence would resolve them.

Use sanitized, minimal reproductions. When remediation is requested, preserve
legitimate behavior and verify both the failure mode and authorized use after
the fix. Report the scope reviewed and material limits of the evidence.
