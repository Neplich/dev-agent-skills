---
feature: delivery-pipeline
feature_path: delivery-pipeline
parent_feature: N/A
feature_level: 1
version: 1.2.0
date: 2026-08-01
last_updated: 2026-08-06
---

# Delivery Pipeline

## 已确认范围

- 消息通过事件驱动投递：新消息发布 `delivery.created` 事件，消费者异步按渠道投递。
- 失败消息进入重试队列，重试耗尽进入 dead-letter。
- pending、processing 和 delivered 状态可观测。

## P0 验收

- 投递延迟目标小于 30 秒。
- 失败投递不会丢失原始消息和关联 ID。
