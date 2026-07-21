export async function registerUser(req, db, analytics) {
  const user = await db.users.insert({
    name: req.body.name,
    email: req.body.email,
    signupIp: req.ip,
    userAgent: req.headers["user-agent"]
  });

  analytics.track("account_created", {
    userId: user.id,
    email: user.email,
    ipAddress: req.ip
  });

  return user;
}
