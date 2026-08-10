# Documentation granularity

Deployment documentation uses one `ops/deployment/index.md` for scope,
selection guidance, support status, and navigation. Shared environment facts
belong in `ops/deployment/environment-reference.md`.

Development, Docker, and Kubernetes/Helm each use their own directory and
`index.md`. Class-specific build, image-source, chart-package, and values facts
belong in focused child pages. Indexes link those children without duplicating
their commands or parameter tables.
