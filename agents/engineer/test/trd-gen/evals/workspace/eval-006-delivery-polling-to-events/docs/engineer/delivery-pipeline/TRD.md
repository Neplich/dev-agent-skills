---
type: TRD
feature: delivery-pipeline
feature_path: delivery-pipeline
parent_feature: N/A
feature_level: 1
version: 1.1.0
date: 2026-07-20
last_updated: 2026-07-20
related_prd: docs/pm/delivery-pipeline/PRD.md
---

# Delivery Pipeline TRD

## 投递方案：定时轮询

系统每 60 秒轮询待投递消息表，扫描 `status = pending` 的记录，按渠道批量投递，批大小 100。轮询间隔导致投递延迟平均 30 秒、峰值 60 秒。

## 模块

- `src/delivery/poller.ts`：轮询调度与扫描
- `src/delivery/batch.ts`：批量投递

## 验证

- 轮询频率与扫描边界单测
- 投递批次与重试单测
