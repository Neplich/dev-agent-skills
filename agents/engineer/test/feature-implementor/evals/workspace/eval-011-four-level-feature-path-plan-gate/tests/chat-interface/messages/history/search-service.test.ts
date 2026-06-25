import { sortMessageSearchResults } from "../../../../../src/chat-interface/messages/history/search-service";

describe("sortMessageSearchResults", () => {
  it("sorts by relevance and then newest message time", () => {
    const sorted = sortMessageSearchResults([
      { id: "older", workspaceId: "workspace-1", relevance: 0.8, createdAt: "2026-06-20T00:00:00.000Z" },
      { id: "newer", workspaceId: "workspace-1", relevance: 0.8, createdAt: "2026-06-21T00:00:00.000Z" },
      { id: "best", workspaceId: "workspace-1", relevance: 0.9, createdAt: "2026-06-19T00:00:00.000Z" },
    ]);

    expect(sorted.map((item) => item.id)).toEqual(["best", "newer", "older"]);
  });
});
