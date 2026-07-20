export type SearchItem = {
  id: string;
  title: string;
};

export type SearchResponse =
  | { status: 200; body: { items: SearchItem[]; limit: number } }
  | { status: 400; body: { error: string } };

export function searchRoute(query: { q?: string; limit?: number }): SearchResponse {
  if (!query.q?.trim()) return { status: 400, body: { error: "q is required" } };
  const limit = Math.min(Math.max(query.limit ?? 10, 1), 20);
  return { status: 200, body: { items: [], limit } };
}

export const searchHttpRoute = {
  method: "GET",
  path: "/api/search",
  handle: searchRoute,
} as const;
