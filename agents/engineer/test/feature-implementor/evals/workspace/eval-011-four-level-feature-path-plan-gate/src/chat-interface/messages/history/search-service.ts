export interface MessageSearchResult {
  id: string;
  workspaceId: string;
  relevance: number;
  createdAt: string;
}

export function sortMessageSearchResults(
  results: MessageSearchResult[],
): MessageSearchResult[] {
  return [...results].sort((left, right) => {
    if (right.relevance !== left.relevance) {
      return right.relevance - left.relevance;
    }

    return Date.parse(right.createdAt) - Date.parse(left.createdAt);
  });
}
