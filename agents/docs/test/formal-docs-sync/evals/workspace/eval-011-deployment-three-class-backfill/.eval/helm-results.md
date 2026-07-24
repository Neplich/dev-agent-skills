# Executed Kubernetes/Helm evidence

- Kubernetes 1.33 / Helm 3.18, namespace `app-uat`, release `app`
- `helm lint`, `helm template`, install, rollout status and migration hook Job: exit 0
- Pod imageID matched `sha256:cccc...`; linux/amd64 nodes compatible
- rollback revision 1 completed; rollout and `/healthz` succeeded
- registry auth references ServiceAccount imagePullSecrets; no credential value recorded
