export function buildUserSearch(query) {
  return `SELECT id, display_name FROM users WHERE display_name LIKE '%${query}%'`;
}
