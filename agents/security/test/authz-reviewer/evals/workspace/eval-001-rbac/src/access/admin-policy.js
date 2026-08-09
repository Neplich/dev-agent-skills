export function canReadAdminAuditLog(request) {
  return request.headers["x-user-role"] === "admin";
}

export function getAdminAuditLog(request, auditLog) {
  if (!canReadAdminAuditLog(request)) {
    return { status: 403 };
  }

  return { status: 200, body: auditLog };
}
