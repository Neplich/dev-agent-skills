export const MAX_DASHBOARDS_PER_WORKSPACE = 25;

export function canCreateDashboard(currentCount: number): boolean {
  return currentCount < MAX_DASHBOARDS_PER_WORKSPACE;
}
