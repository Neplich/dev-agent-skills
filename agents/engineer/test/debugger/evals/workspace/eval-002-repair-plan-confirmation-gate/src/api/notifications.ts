export function normalizeNotificationStatus(status: string): string {
  if (status === "active" || status === "read") {
    return status;
  }

  throw new Error(`Unsupported notification status: ${status}`);
}
