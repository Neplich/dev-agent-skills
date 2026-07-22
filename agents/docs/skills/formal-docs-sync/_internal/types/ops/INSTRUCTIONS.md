# Operations Sync Instructions

Load this module only when the confirmed scope contains `doc_type: ops`.

## Evidence Checks

For deployment work, first classify the candidate scope as Development,
Docker, and Kubernetes/Helm. For each class report `supported`, `unsupported`,
`blocked`, or `out-of-scope`, its evidence, owner, code glob, target pages,
environment differences, exclusions, and change-map delta. Continue with other
confirmed classes when one is blocked; do not create a page or command that
pretends the blocked class is supported.

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

Build `docs/site/ops/deployment/environment-reference.md` by cross-checking
`.env.example`, configuration schema/settings and actual reads, Compose and
Helm mappings, and tests. Group parameters by domain or service. For every
parameter record its exact name, purpose, type/format, requiredness,
evidence-backed non-secret default, allowed values/constraints, applicable
deployment classes, safe example, secret classification and store reference,
activation timing, and evidence paths. Report missing, deprecated, renamed, or
conflicting definitions. Do not document variables absent from both examples
and reads, or duplicate the full table in deployment-specific pages.

Use the host granularity and ops template contracts for the authoritative page
tree:

- `development/index.md` covers source startup, dependencies, initialization,
  env injection, service order, ports, health/success, reload/debug/logging, and
  environment boundaries. `development/image-build.md` requires real
  Dockerfile/build-script/executed-build evidence for context, target, args,
  dependency sources, architectures, dev tags, build/load/push entry points,
  image entry/content and digest/manifest checks; otherwise block those facts.
- `docker/index.md` covers Compose versions/files/profiles, dependency order,
  env precedence, secrets, volumes, networks, ports, migration/jobs, lifecycle,
  upgrade/backup/restore/rollback, health/log/data checks, and Docker-specific
  differences. `docker/image-sources.md` records each service image coordinate,
  digest, source type, architectures, secure auth reference, pull/mirror/offline
  entry, provenance checks, and pull/permission/architecture/tag diagnostics.
  Exclude Helm-only values, namespace, and release revision steps.
- `kubernetes-helm/index.md` covers cluster/Helm/Ingress/StorageClass/permission
  prerequisites, namespace/release/values layering, ConfigMap/Secret mappings,
  preflight/backup, CRD/hook/job/migration order, install/upgrade, rollout and
  resource checks, and rollback. `image-sources.md` records values image keys,
  Chart/release correspondence, imagePullSecrets/identity, node architecture,
  offline sources, preflight provenance and Pod imageID checks.
  `chart-package.md` documents only the real Chart tree and file duties,
  dependencies, CRDs, hooks, tests, lint/template/package/pull/push sources and
  digest/provenance checks. `values-reference.md` derives grouped parameter
  facts from values, schema, template consumption and environment overrides,
  including path, purpose, type, non-secret default, requiredness, constraints,
  environment difference, sensitivity, consumer, merge precedence and checks.
  Exclude unsupported empty groups and Compose-only assumptions.

Each class owns its prerequisites, configuration, commands, success criteria,
rollback, and troubleshooting. Root and class indexes provide scope and
navigation without copying child-page bodies. If migrating an aggregate page,
include path moves, link repairs, navigation, change-map updates, and duplicate
fact consolidation in the same confirmed atomic scope.

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
