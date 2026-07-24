# Executed development evidence

- `scripts/dev/start.sh`: exit 0; `GET http://127.0.0.1:8080/healthz`: HTTP 200
- `docker build --target runtime -t app:dev-git-abcd1234 .`: exit 0 on linux/amd64 and linux/arm64
- `docker image inspect app:dev-git-abcd1234`: entrypoint `python -m app`
- `docker buildx imagetools inspect app:dev-git-abcd1234`: both architectures present
