# Deployment verification record

| Environment | Command | Result |
| --- | --- | --- |
| development | `AI_HUB_PORT=8080 docker compose -f deploy/compose.yaml up -d` | exit 0; app healthy |
| staging | `AI_HUB_PORT=9080 docker compose -f deploy/compose.yaml up -d` | exit 0; app healthy |
| staging upgrade | `AI_HUB_IMAGE=registry.example/ai-hub:v1.4.2 docker compose -f deploy/compose.yaml pull app && AI_HUB_IMAGE=registry.example/ai-hub:v1.4.2 docker compose -f deploy/compose.yaml up -d app` | both commands exit 0 |
| staging health | `curl -fsS http://127.0.0.1:9080/healthz` | HTTP 200, body `ok` |
| rollback drill | `AI_HUB_IMAGE=registry.example/ai-hub:v1.4.1 docker compose -f deploy/compose.yaml up -d app` then the same health check | exit 0 and HTTP 200 |

No Kubernetes or Helm command was executed. Secret values were not recorded.
