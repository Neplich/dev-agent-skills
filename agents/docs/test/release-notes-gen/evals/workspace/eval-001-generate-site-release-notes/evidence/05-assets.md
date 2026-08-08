# 交付资产证据

- 镜像：`registry.example.com/ai-hub/web:v1.0.0` 与 `gateway:v1.0.0`，均要求 amd64/arm64。
- 静态资产清单：`dist/manifest.json`，新增 file-card chunk。
- 发布核验必须记录两个镜像的 manifest digest；当前证据包尚未包含 digest 或 `imagetools inspect` 结果。
- 现有发布材料不授权构建或推送镜像；该缺口必须由 release engineering 补证。
