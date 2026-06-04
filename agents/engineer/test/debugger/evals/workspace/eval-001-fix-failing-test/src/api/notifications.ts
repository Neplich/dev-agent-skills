export type NotificationStatus = "unread" | "read" | "archived";

export interface Notification {
  id: string;
  title: string;
  status: NotificationStatus;
}

export function listActiveNotifications(
  notifications: Notification[],
): Notification[] {
  return notifications.filter((notification) => notification.status !== "read");
}
