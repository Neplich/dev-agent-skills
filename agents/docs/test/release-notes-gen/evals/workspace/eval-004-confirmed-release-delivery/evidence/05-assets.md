# 交付资产证据

- 镜像：`registry.example.com/ai-hub/web:v1.0.0` 与 `gateway:v1.0.0`，均要求 amd64/arm64。
- 静态资产清单：`dist/manifest.json`，新增 file-card chunk。
- `docker buildx imagetools inspect` 已核对两个镜像均只包含 linux/amd64 与 linux/arm64；原始 OCI index 捕获保存在 `evidence/manifests/`：
  - `web:v1.0.0` index SHA-256：`sha256:620c7bb6645fe08a9579ad51b9eea91986b4945e04d92d6c6d63940c0de597da`
  - `gateway:v1.0.0` index SHA-256：`sha256:292fcdba804b4743d754eff5e8ec1a1b384cb0323e6017380d8c95ff96f35412`
- 现有发布材料只记录已完成的核验结果，不授权重新构建或推送镜像。
