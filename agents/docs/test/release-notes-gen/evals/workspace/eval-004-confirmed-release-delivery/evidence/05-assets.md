# 交付资产证据

- 镜像：`registry.example.com/ai-hub/web:v1.0.0` 与 `gateway:v1.0.0`，均要求 amd64/arm64。
- 静态资产清单：`dist/manifest.json`，新增 file-card chunk。
- `docker buildx imagetools inspect` 已核对两个镜像均只包含 linux/amd64 与 linux/arm64：
  - `web:v1.0.0` manifest digest：`sha256:1111111111111111111111111111111111111111111111111111111111111111`
  - `gateway:v1.0.0` manifest digest：`sha256:2222222222222222222222222222222222222222222222222222222222222222`
- fixture 只记录已完成的核验结果，不授权重新构建或推送镜像。
