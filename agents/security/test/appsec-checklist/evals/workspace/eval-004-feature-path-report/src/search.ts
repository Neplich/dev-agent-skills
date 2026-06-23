export function buildSearchQuery(workspaceId: string, query: string): string {
  return `SELECT * FROM messages WHERE workspace_id = '${workspaceId}' AND body LIKE '%${query}%'`;
}
