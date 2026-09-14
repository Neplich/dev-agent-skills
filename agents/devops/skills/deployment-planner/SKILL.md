---
name: deployment-planner
description: "Create or update local, Docker, Kubernetes, or Helm deployment assets using the application runtime and requested target environment."
---

# Deployment Planning

Determine the target from the user request and existing deployment assets.
Inspect runtime entry points, build outputs, dependencies, persistence, traffic,
configuration, health checks, and environment differences. Select assets that
serve those targets and extend the project's existing layout.

## Target references

| Target | Useful assets | Verify |
| --- | --- | --- |
| Local development | Startup instructions, environment example, startup script | Prerequisites, dependencies, migrations, application readiness |
| Docker / Compose | Dockerfile, Compose services, environment example | Build context, runtime user, ports, mounts, networking, persistence |
| Kubernetes / Helm | Chart, values, workload, service, ingress, configuration | Image identity, resources, probes, routes, configuration, scaling |

For local startup, document the actual command sequence and external dependencies.
For containers, use a supported base image, a suitable non-root runtime user,
and explicit build/runtime boundaries. Define service dependencies, storage,
networking, and health checks for the application's needs.

For Helm, include the applicable workload, service, configuration, ingress,
and scaling resources. Values expose the relevant image, ports, environment,
resource sizing, and persistence choices. Reference secrets through the chosen
platform's protected mechanism.

For multiple services or documentation variants, identify each build and runtime
unit. Follow the chain from source/build context through artifact or image to
startup and health verification. Record the actual architectures, registry,
immutable version policy, and deployment trigger when used.

Validate configuration with the project's available lint, render, build, or
local startup commands. Inspect readiness and recovery behavior for executed
targets. Continue into requested automation and documentation, preserving the
user's rollout scope and reporting operations that remain unexecuted.
