export type SearchItem = {
  id: string;
  title: string;
};

export type SearchResponse =
  | { status: 200; body: { items: SearchItem[]; limit: number } }
  | { status: 400; body: { error: string } };

export function searchRoute(query: { q?: string; limit?: number }): SearchResponse {
  if (typeof query.q !== "string" || !query.q.trim()) {
    return { status: 400, body: { error: "q is required" } };
  }
  if (query.limit !== undefined && !Number.isInteger(query.limit)) {
    return { status: 400, body: { error: "limit must be an integer" } };
  }
  const limit = Math.min(Math.max(query.limit ?? 10, 1), 20);
  return { status: 200, body: { items: [], limit } };
}

export const searchHttpRoute = {
  method: "GET",
  path: "/api/search",
  handle: searchRoute,
} as const;
