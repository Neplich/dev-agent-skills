---
name: trd-gen
description: "Write technical designs, API specifications, and architecture decision records from the requested outcome and verified repository evidence."
---

# Technical Design

Create the technical artifact useful to the task: an implementation design,
API specification, migration design, or architecture decision record. Start
from the user request, existing specifications, issue context, code, and tests.

Describe the current system, the target behavior, affected components, and the
choice that makes the change work. Include interfaces, data, compatibility,
failure handling, observability, security, rollout, and verification when they
matter to the design. Explain tradeoffs using concrete project constraints.

Use [the design outline](./_internal/trd-schema.md) as a selection guide. Keep
small designs in the task or PR; use a durable document for decisions and
interfaces that future work will consume. Choose the project's existing home
for those documents and link the evidence used.

For APIs, specify methods, schemas, authentication, errors, pagination, and
idempotency where relevant. For an ADR, record context, the selected approach,
consequences, and meaningful alternatives. Use diagrams when they explain a
relationship more clearly than prose.

Verify names, paths, dependencies, and contracts against source. Resolve missing
product choices with the user when they materially affect the outcome, and
continue implementation covered by the request once the design is actionable.
