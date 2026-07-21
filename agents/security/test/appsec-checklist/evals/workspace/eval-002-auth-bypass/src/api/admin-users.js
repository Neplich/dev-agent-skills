const users = [
  { id: "user-001", displayName: "Example Admin", role: "admin" },
  { id: "user-002", displayName: "Example Member", role: "member" },
];

export function listUsers(req, res) {
  return res.json({ users });
}
