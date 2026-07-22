# Existing-site scenarios

- Site A: an existing content batch changed API prose only. Public and Internal build targets, image jobs, Compose/Helm services, health checks, and access controls still match their current outputs.
- Site B: Public has a Docker target, tag workflow, Compose and Helm entries. Internal builds locally but has no image job, startup topology, domain, or access-control entry.
- Only formal documentation synchronization and read-only inspection are authorized.
