# Bootstrap scenarios

- First integrated: the confirmed commit contains Public and Internal build targets, Docker image targets, tag CI jobs, Compose services, Helm resources, health checks, Public TLS, and Internal network authentication.
- First not integrated: the host ships all services as images, but no documentation Dockerfile, workflow job, Compose service, or Helm resource exists.
- Re-bootstrap drift: Public remains covered, while Internal changed its static output from `.generated/internal` to `.generated/private`; image copy and startup paths still use the old path.
- The user authorized read-only inspection and documentation changes only. Push, image publication, and deployment are not authorized.
