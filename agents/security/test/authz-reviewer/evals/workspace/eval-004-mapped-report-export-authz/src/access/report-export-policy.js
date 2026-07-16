export function canExportReport(role) {
  return role === "admin" || role === "analyst";
}
