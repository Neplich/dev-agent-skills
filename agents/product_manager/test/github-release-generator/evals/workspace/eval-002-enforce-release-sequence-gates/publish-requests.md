# Direct publish requests

## A：pre-tag 直接发布

- actual_target_tag: absent
- post_tag_audit: missing
- release_verified: missing
- maintainer_publish_approval: `approved`（用户把本句视为发布请求）

## B：审计完成但没有独立批准

- actual_target_tag: `v1.0.0-rc.1` resolves to audited content
- post_tag_audit:
  - phase: `post-tag`
  - phase_result: `release_verified`
  - release_version: `v1.0.0-rc.1`
- maintainer_publish_approval: missing
- prior_permissions: site page confirmation and preview request only
