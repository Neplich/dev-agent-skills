export function searchRoute(query: { q?: string; limit?: number }) {
  if (!query.q?.trim()) return { status: 400, body: { error: "q is required" } };
  const limit = Math.min(Math.max(query.limit ?? 10, 1), 20);
  return { status: 200, body: { items: [], limit } };
}
