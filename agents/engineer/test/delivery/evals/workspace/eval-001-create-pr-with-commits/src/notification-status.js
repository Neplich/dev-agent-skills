const labels = {
  active: "Active",
  read: "Read",
  archived: "Archived"
};

export function formatNotificationStatus(status) {
  return labels[status] ?? status;
}
