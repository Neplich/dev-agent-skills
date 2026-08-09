---
title: "notification-center — Product Requirements Document"
type: PRD
feature: "notification-center"
feature_path: "notification-center"
parent_feature: "N/A"
feature_level: "1"
child_features: "N/A"
version: "1.3.0"
status: Confirmed
author: "Notification Product Team"
date: "2026-07-20"
last_updated: "2026-07-28"
---

# PRD: Notification Center

## Goal

Provide a unified notification center covering delivery strategy, subscription
management, and channel configuration for workspace users.

## User Stories

| ID | Story | Priority |
|----|-------|----------|
| US-01 | As a user, I want to see all notifications in one inbox so nothing is missed. | P0 |
| US-02 | As a user, I want unread counts per category so I can triage quickly. | P0 |
| US-03 | As a user, I want to mark items read in bulk so cleanup is fast. | P1 |
| US-04 | As a user, I want delivery to adapt when I am active so I am not interrupted. | P1 |
| US-05 | As a user, I want digest emails for low-priority items so noise stays low. | P1 |
| US-06 | As an admin, I want to define org-wide default subscriptions so onboarding is consistent. | P0 |
| US-07 | As a user, I want to unsubscribe per topic so I control my feed. | P0 |
| US-08 | As a user, I want mute windows per topic so focus time is respected. | P2 |
| US-09 | As an admin, I want to configure which channels are available so compliance is met. | P0 |
| US-10 | As a user, I want to order my channels by preference so delivery follows my choice. | P1 |

## Functional Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-01 | The system aggregates notifications from all product modules into a single inbox. | P0 |
| FR-02 | The system delivers urgent items via polling every 30 seconds. | P0 |
| FR-03 | The system batches non-urgent items into a configurable digest. | P1 |
| FR-04 | The system tracks read state per user per item. | P0 |
| FR-05 | The system supports per-topic subscription opt-in and opt-out. | P0 |
| FR-06 | The system applies org-level default subscriptions to new members. | P1 |
| FR-07 | The system supports email, in-app, and webhook channels. | P0 |
| FR-08 | The system allows per-user channel ordering and fallback. | P1 |

## Domain: Delivery Strategy

Polling-based delivery with fixed intervals; urgent items poll every 30
seconds, normal items every 5 minutes. Digest batching runs hourly.

## Domain: Subscription Management

Topic hierarchy with org defaults, user overrides, mute windows, and bulk
actions.

## Domain: Channel Configuration

Channel registry with per-user ordering, fallback rules, and admin-controlled
availability.

## Acceptance Criteria

1. Users can complete US-01 through US-07 flows end to end.
2. Delivery latency for urgent items stays under 60 seconds.
3. Channel fallback triggers within two failed attempts.
