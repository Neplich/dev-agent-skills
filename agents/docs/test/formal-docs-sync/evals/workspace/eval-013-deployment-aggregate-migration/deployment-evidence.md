# Confirmed current evidence

- Development: `scripts/dev/start.sh`, successful source health check, verified development image build
- Docker: `deploy/docker/compose.yaml`, executed start/upgrade/rollback and distinct Docker image digest
- Kubernetes/Helm: `deploy/helm/app/**`, lint/template/install/rollout/rollback results and distinct Pod imageID
- Shared env: `.env.example`, settings reads/tests, Compose and Helm mappings cross-checked
