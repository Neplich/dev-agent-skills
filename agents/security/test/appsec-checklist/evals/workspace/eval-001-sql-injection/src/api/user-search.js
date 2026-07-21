export async function searchUsers(req, res) {
  const name = req.query.name;
  const sql = `SELECT id, display_name FROM users WHERE display_name LIKE '%${name}%'`;
  const users = await req.app.locals.db.query(sql);

  res.json(users.rows);
}
