# Operations Sync Instructions

Load this module only when the confirmed scope contains `doc_type: ops`.

## Evidence Checks

Use confirmed deployment and runtime evidence to verify, as applicable:

- supported services, components, environments, versions, owners, and
  dependencies;
- required permissions, configuration, secret references, backups, and
  prerequisites;
- exact startup, upgrade, Helm, Compose, migration, and operational commands;
- health endpoints, logs, metrics, jobs, data checks, and explicit success
  criteria;
- environment differences demonstrated by configuration or execution results;
- rollback triggers, executable rollback steps, and post-rollback checks;
- observed failure symptoms and evidence-backed diagnostic entry points.

An unexecuted command, proposed deployment path, placeholder value, or plan is
not current operational fact. Never write credentials, tokens, cookies, or
other secret values; reference the approved secure store instead.

## Template and Output Rules

Read the ops template linked from the host standards entry—normally
`docs/site/standards/templates/ops-runbook.md`—and consume its single
`docs-scaffold` block for a new page. Do not copy the template into this skill.

Keep only currently executable steps, prerequisites, checkpoints, rollback,
and troubleshooting that evidence supports. Upgrade and rollback instructions
are ops pages, not Release Notes; hand off any Release Notes body, index,
metadata, or navigation request to `docs-agent:release-notes-generator`. Keep
ops pages and their change-map entries in the same confirmed write/read-back
scope.
