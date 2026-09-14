# 运维同步参考

根据配置和运行结果确定 Development、Docker、Kubernetes/Helm 等实际支持方式。分别说明前置条件、配置、命令、成功标准、回滚和排错；已验证方式可以独立交付，证据缺口按类别说明。

共享 environment-reference.md 对照 .env.example、配置 schema、实际读取、Compose/Helm 映射和测试。每个参数记录名称、目的、类型、必填性、真实默认值、约束、敏感性、安全存储引用、生效时点和适用环境。保留 active、deprecated、renamed、missing、conflict 等真实生命周期信息，完整核对示例中的键与实际读取。

| 部署方式 | 重点内容 |
| --- | --- |
| Development | 源码启动、依赖、初始化、注入、服务顺序、端口、健康、调试；有构建证据时说明镜像构建 |
| Docker | Compose 文件与 profile、环境优先级、secret、卷、网络、端口、迁移任务、备份恢复与升级 |
| Kubernetes/Helm | 集群与权限、namespace/release、values 层次、ConfigMap/Secret、CRD/hook/job 顺序、rollout、资源和回滚 |

镜像来源页记录 registry/repository/tag/digest、架构、来源、安全鉴权引用、拉取与校验。Helm Chart 页按实际目录说明文件职责；values 参考对照 schema、模板消费点和环境覆盖。

正文使用真实可执行步骤和已验证结果，凭据用安全存储引用。根据部署边界选择独立页面，索引提供场景选择与导航。更新 runbook、参数页、必要索引和 change-map，逐类核对可执行性与恢复说明。
