const searchApiKey = process.env.SEARCH_API_KEY;
const searchIndexName = process.env.SEARCH_INDEX_NAME;

export function configReady(): boolean {
  return Boolean(searchApiKey && searchIndexName);
}
