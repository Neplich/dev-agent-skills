export async function refreshSession(database: Database, sessionId: string) {
  return database.query(
    "SELECT user_id, expires_at FROM sessions WHERE id = ?",
    [sessionId],
  );
}
