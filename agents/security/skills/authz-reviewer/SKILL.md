---
name: authz-reviewer
description: "Review authentication, authorization, RBAC, sessions, tokens, permission models, and access controls against confirmed scope. Use after security-agent routes auth/authz review."
visibility: internal
---

## Reader-Facing Writing Composition

For substantial reader-facing prose, co-load `human-writing` even on direct
invocation; use the same context, not a later pass. This Skill retains evidence,
facts, structure, paths, gates, and verification. Skip code-, config-, schema-,
lockfile-, and data-only output.

## Mandatory Evidence Escalation

When change-map discovery points to a formal page whose
`last_verified_version` is `unverified`, label that page low-trust and expand
verification against code/tests before relying on its auth/authz claims.

When the review proves that a formal documentation, behavior, operational, or
release fact changed, write the Security-owned report under
`docs/security/{feature_path}/`, preserve the mapped document/code evidence and
impact, and return the conclusion to `pm-agent` for classification and
PM-owned issue filing. Do not hand the conclusion directly to `docs-agent` or
edit another role's document.

## PM Handoff Entry Gate

Before auth/authz review, require a PM/Security handoff packet or equivalent
confirmed security context. If the user directly invokes this specialist
without PM handoff context, confirmed roles/permissions scope, or a confirmed
`feature_path` for feature-scoped work, return the request to `pm-agent` for
classification.

Resolve the entry basis from both the user context and repository materials
before declaring it missing. If a repository-root `PM_HANDOFF.md` exists, read
it and validate its confirmed scope, roles or permissions, source documents,
and `feature_path`; do not block merely because the natural-language request
does not repeat those packet fields.

Use the PM-side packet definition in
the plugin-local generated `../security-agent/_internal/_generated/shared-contracts/handoff-contract.md`.

## Execution Steps

### Step 1: Understand User Roles and Permissions

宿主存在 `docs/site/standards/change-map.yaml` 时，项目探索先按 pm-agent 维护的 `consumption-contract.md`（the plugin-local generated `../security-agent/_internal/_generated/shared-contracts/consumption-contract.md`）执行“任务落点 → change-map 反查 → 精准读取 → 关键判断回代码验证”；不存在时静默沿用当前代码探索。

1. **Resolve feature scope**:
   - For feature-scoped review, use the confirmed `feature_path`.
   - Read `docs/pm/{feature_path}/PRD.md`.
   - Read `docs/engineer/{feature_path}/TRD.md` and
     `docs/engineer/{feature_path}/IMPLEMENTATION_PLAN.md` when architecture
     or implementation details affect auth/authz behavior.
   - If `feature_path` is unclear, return to PM for PRD/path clarification or
     Engineer for missing/stale TRD or implementation plan; do not invent a
     new top-level security directory.

2. **Read PM documents**:
   - PRD: identify user roles, permissions, access levels
   - Extract role definitions (e.g., admin, user, guest)

3. **Create role matrix** - document expected permissions for each role

### Step 2: Analyze Authentication Flow

**A. Find authentication code:**
- Search for login/signup endpoints
- Search for password handling
- Search for token generation (JWT, session)

**B. Check authentication security:**
- Password hashing algorithm (bcrypt, argon2)
- Password strength requirements
- Rate limiting on login attempts
- Account lockout mechanism
- Multi-factor authentication (if applicable)

### Step 3: Analyze Authorization Logic

**A. Find authorization checks:**
- Search for permission checks in routes/controllers
- Search for role-based access control (RBAC)
- Search for middleware/decorators handling authorization

**B. Check authorization coverage:**
- All protected endpoints have authorization checks
- Authorization happens server-side (not just client-side)
- Proper role hierarchy enforcement
- Tenant isolation (for multi-tenant apps)

### Step 4: Review Session Management

**A. Session configuration:**
- Session timeout settings
- Secure cookie flags (httpOnly, secure, sameSite)
- Session regeneration after login
- Proper logout implementation

**B. Token security (if using JWT/tokens):**
- Token expiration
- Token refresh mechanism
- Token storage (not in localStorage for sensitive apps)
- Token revocation capability

### Step 5: Generate Authorization Review Report

Create `docs/security/{feature_path}/authz-review.md`:

**Frontmatter:**
```yaml
---
feature: {feature}
feature_path: {feature_path}
parent_feature: {parent_feature}
feature_level: {feature_level}
version: v1
date: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
```

**Report Structure:**

1. **Role Permission Matrix**
   - Table showing roles and their permissions
   - Expected vs actual implementation

2. **Authentication Flow Analysis**
   - Login flow diagram
   - Password security assessment
   - Session/token generation review

3. **Authorization Coverage**
   - Protected endpoints list
   - Authorization check status for each
   - Missing authorization checks (if any)

4. **Session Management Review**
   - Session configuration assessment
   - Security flags status
   - Session lifecycle handling

5. **Security Issues Found**
   - Critical/High/Medium/Low issues
   - Specific locations and fix recommendations

6. **Recommendations**
   - Priority fixes
   - Best practices to implement

## Output Format

Use tables and diagrams for clarity:

```markdown
## Role Permission Matrix

| Role | View Users | Edit Users | Delete Users | Admin Panel |
|------|-----------|-----------|--------------|-------------|
| Admin | ✅ | ✅ | ✅ | ✅ |
| User | ✅ | ❌ | ❌ | ❌ |
| Guest | ❌ | ❌ | ❌ | ❌ |

## Authorization Issues

### [HIGH] Missing Authorization Check on Delete Endpoint

**Location:** `src/api/users.js:78`

**Issue:** DELETE /api/users/:id has no authorization check

**Risk:** Any authenticated user can delete other users

**Fix:**
\`\`\`javascript
app.delete('/api/users/:id', requireRole('admin'), async (req, res) => {
  // delete logic
});
\`\`\`
```

## Closeout

After reaching a confirmed review conclusion, including on a direct invocation,
evaluate `../security-agent/_internal/_generated/shared-contracts/security-escalation.md`.
When it triggers, return the conclusion and evidence to `pm-agent` for
classification and issue filing; do not hand evidence directly to `docs-agent`,
file the issue yourself, or modify formal documentation (`docs/site/` or
documentation owned by other roles). The required Security-owned process report
under `docs/security/{feature_path}/` remains escalation evidence and is not
restricted by this prohibition. Then apply
`../security-agent/_internal/_generated/shared-contracts/closeout-contract.md`
to recommend the next step and wait for user confirmation.
