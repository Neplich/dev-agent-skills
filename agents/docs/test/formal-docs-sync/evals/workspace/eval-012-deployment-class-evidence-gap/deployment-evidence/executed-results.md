# Executed results

All commands below were executed from the repository root.

## Development

- Start: `APP_PORT=8080 ./scripts/dev/start.sh`; exit 0; `GET /healthz` returned HTTP 200.
- Failure diagnosis: `APP_PORT=invalid ./scripts/dev/start.sh`; exit 2 with an invalid-port configuration error.
- Configuration rollback and recovery: restore the last verified value with
  `APP_PORT=8080 ./scripts/dev/start.sh`; exit 0; `GET /healthz` returned HTTP
  200. The invalid process was stopped before restart.
- Troubleshooting compared `APP_PORT` with `.env.example`, then reran the start
  command and health request; the mismatch was isolated without printing
  `DATABASE_URL` or any other secret value.

## Docker Compose

- Prerequisite check: `docker compose version`; exit 0; Docker Compose v2 was
  available.
- Start: `docker compose -f deploy/docker/compose.yaml up -d app`; exit 0.
- Success checks: `docker compose -f deploy/docker/compose.yaml ps app`; exit 0
  with the app container healthy; `GET http://localhost:8080/healthz` returned
  HTTP 200.
- Rollback drill: after restoring the recorded app image coordinate
  `registry.example/app:v2.0.0@sha256:d72b8095defb5aed9affa64bc68b747089d2eab27ddf36edb6ee70a3cdd167e4`,
  run `docker compose -f deploy/docker/compose.yaml pull app` and
  `docker compose -f deploy/docker/compose.yaml up -d --no-deps app`; both
  exited 0; the health request returned HTTP 200.
- Troubleshooting checks: `docker compose -f deploy/docker/compose.yaml ps app`
  and `docker compose -f deploy/docker/compose.yaml logs --tail=100 app`; both
  exited 0. Logs contained no startup error after rollback.

## Kubernetes/Helm

Not executed. No Chart, values, template consumer, cluster authority, or
verification result is available.
