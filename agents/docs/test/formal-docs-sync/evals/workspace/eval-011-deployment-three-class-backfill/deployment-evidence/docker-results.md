# Executed Docker evidence

- Docker 28 / Compose 2.37 confirmed
- `docker compose -f deploy/docker/compose.yaml up -d`: exit 0
- app health: healthy; `/healthz`: HTTP 200; database volume: `app-data`
- upgrade and rollback both used immutable digests; pull authentication referenced local credential store
