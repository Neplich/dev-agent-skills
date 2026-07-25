# Confirmed Product backfill batch

- Mode: `existing-system backfill`
- Product tree:
  - `product/index.md`
    - `workspace-management/index.md`
      - `invitations/index.md`
        - `member-invitations/index.md`
          - `invite-member.md`
          - `manage-pending-invitation.md`
        - `invitation-acceptance/index.md`
          - `accept-invitation.md`
    - `analytics/index.md`
      - `view-dashboard.md`
- Owners: `collaboration-team` for workspace management; `insights-team` for analytics.
- Reader tasks: navigate each domain and feature level; invite a member; resend
  or revoke a pending invitation; accept an invitation; recover from an
  invalid or expired invitation; view dashboard activity.
- Evidence: confirmed feature catalog, current implementation, and acceptance tests.
- Mapping:
  - `src/product/workspace_management/**` -> the complete workspace-management subtree.
  - `src/product/workspace_management/invitations/**` -> both second-level invitation feature subtrees.
  - `src/product/workspace_management/invitations/member_invitations.py` -> the member-invitations index and its task leaves, with every Product ancestor index.
  - `src/product/workspace_management/invitations/invitation_acceptance.py` -> the invitation-acceptance index and its task leaf, with every Product ancestor index.
  - `src/product/analytics/**` -> the analytics subtree.
- Links: every task is reachable one level at a time from `product/index.md`
  through its domain, first-level feature, and second-level feature; task pages
  link their parent and relevant Design/API/Database/Ops authority indexes
  without copying contracts.
- Exclusions: billing, workspace deletion, exports, role-based duplicate trees, future behavior, and all non-Product writes.
- Stable paths: no Product leaf path exists yet, so no migration or redirect is required.
- Confirmation: the maintainer confirms the full tree, pages, mappings, links, navigation, and exclusions as one finite batch.
