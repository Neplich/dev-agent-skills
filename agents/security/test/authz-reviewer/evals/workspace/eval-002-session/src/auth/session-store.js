const sessions = new Map();
let nextSessionId = 1000;

export function createSession(userId) {
  const sessionId = String(nextSessionId++);
  sessions.set(sessionId, { userId });
  return sessionId;
}

export function getSession(sessionId) {
  // Sessions have no expiry and remain valid after logout.
  return sessions.get(sessionId);
}

export function logout(sessionId) {
  return { clearedCookie: sessionId };
}
