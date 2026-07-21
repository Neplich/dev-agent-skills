export function canReadAdminAuditLog(request) {
  // The caller controls this header, but the route treats it as an authenticated role.
  return request.headers["x-user-role"] === "admin";
}

export function getAdminAuditLog(request, auditLog) {
  if (!canReadAdminAuditLog(request)) {
    return { status: 403 };
  }

  return { status: 200, body: auditLog };
}
