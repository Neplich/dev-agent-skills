# Docker Production Runtime

The `app` service runs from an immutable SemVer image tag supplied through `APP_IMAGE_TAG`.

```bash
docker compose -f deploy/docker/docker-compose.yml pull app
docker compose -f deploy/docker/docker-compose.yml up -d app
docker compose -f deploy/docker/docker-compose.yml logs --tail=200 app
curl --fail http://localhost:8080/health
```

The release record identifies the last known healthy tag. Rollback changes only `APP_IMAGE_TAG`, pulls that image, recreates `app`, then verifies container status, logs and `/health`.
