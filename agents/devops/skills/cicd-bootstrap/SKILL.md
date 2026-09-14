---
name: cicd-bootstrap
description: "Create or update CI/CD workflows with verified build and test commands, scoped permissions, environment configuration, and deployment checks."
---

# CI/CD Configuration

Inspect the Git platform, existing workflows, package scripts, runtime versions,
lockfiles, and deployment targets. Use the repository's actual build and test
commands. Extend the relevant jobs and preserve existing supported workflows.

## Pipeline design

- CI checks out the intended revision, installs the correct runtime and locked
  dependencies, runs relevant checks, and builds the requested artifact.
- Deployment workflows use the requested trigger and environment. Connect
  successful verification to the intended artifact, destination, and health check.
- Image jobs preserve registry conventions, supported architectures, immutable
  tags or digests, and build contexts for each service or variant.
- Permissions, secrets, environment protection, concurrency, and cache keys
  reflect the needs and trust boundaries of the actual job.

A project may use PR checks, staging deployment on a selected branch, or
production deployment on a release event. Configure the events requested by
the task and existing operating model. Document the names and purpose of
required secrets while keeping their values in protected storage.

Validate workflow syntax and the commands available locally. Use the platform's
actual run results to verify remote behavior when execution is authorized.
Read back published artifacts, image digests, or target health for deployment
claims. Distinguish configuration created, checks executed, and runtime verified
in the delivery report.

Keep operational instructions close to the relevant workflow or deployment
assets. Report remaining environment configuration with a concrete next action.
