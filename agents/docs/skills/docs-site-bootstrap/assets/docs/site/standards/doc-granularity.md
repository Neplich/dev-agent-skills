---
title: 文档粒度
visibility: internal
doc_type: design
stage: dev
owners:
  - docs
related_code:
  - docs/site
last_verified_version: unverified
---

# 文档粒度

文档边界以读者任务和稳定事实边界为准，不按代码文件数量机械拆分。

## 选择单文件

满足以下条件时优先使用单文件：

- 主题只有一个稳定入口和一组紧密关联的事实；
- 页面在合理篇幅内可以完整回答读者任务；
- 子主题没有独立所有者、生命周期或导航价值。

## 选择目录

满足任一条件时使用目录并提供 `index.md`：

- 存在多个可独立阅读和维护的子域；
- 不同子域有不同证据、所有者或更新节奏；
- 单页已经妨碍定位、核验或导航。

## 约束

目录入口负责说明范围和导航，不复制子页面正文。不要按版本复制整套页面；
正式页面保留当前状态，历史由版本控制和发布说明承载。

## Ops 部署文档粒度

`docs/site/ops/deployment/` 固定采用目录形式，因为 Development、Docker 与
Kubernetes/Helm 具有不同证据、命令、网络、存储、配置注入和回滚边界：

```text
ops/deployment/
├── index.md
├── environment-reference.md
├── development/
│   ├── index.md
│   └── image-build.md
├── docker/
│   ├── index.md
│   └── image-sources.md
└── kubernetes-helm/
    ├── index.md
    ├── image-sources.md
    ├── chart-package.md
    └── values-reference.md
```

- 根 `index.md` 只说明三类的适用场景、支持状态、选择指引和导航，不复制
  子页正文；各子目录 `index.md` 是该部署方式的权威 runbook。
- `environment-reference.md` 是三类共享的参数权威页。Development、Docker 与
  Kubernetes/Helm 页面只说明各自注入、覆盖和 secret 映射，不复制参数表。
- 每类分别维护 prerequisites、configuration、commands、success criteria、
  rollback 与 troubleshooting；不得把三类命令合并成一个聚合 runbook。
- Development 的 `image-build.md` 只描述有 Dockerfile、构建脚本或执行结果支持
  的开发验证镜像打包路径，不将其表述为正式部署流程。
- Docker 的 `image-sources.md` 与 Kubernetes/Helm 的 `image-sources.md` 分别核对
  自身 registry、repository、tag、digest、架构、鉴权引用和拉取后验证；不得因
  tag 同名推断来源或 digest 相同。
- `chart-package.md` 按宿主真实 Chart 目录说明包结构和职责；
  `values-reference.md` 按真实 values、schema、模板消费点和环境覆盖说明配置接口。
  不存在的 Chart 文件或 values 分组不得保留为空模板。
- 不支持、缺少配置或缺少执行证据的类别在候选范围中标记为 `unsupported`、
  `blocked` 或 `out-of-scope`，说明缺失证据；其他已确认类别可以继续，禁止生成
  占位命令或伪造成功状态。
- 从聚合部署页迁移时，页面移动、内部链接修复、必要导航、change-map 条目更新
  与重复内容归并必须作为同一候选原子范围展示并确认。
