export function registerUserRightsRoutes(app, db, analytics) {
  app.get("/me", async (req, res) => {
    res.json(await db.users.findById(req.session.userId));
  });

  app.get("/data-export", async (req, res) => {
    const userId = req.query.userId;
    res.json({
      profile: await db.users.findById(userId),
      orders: await db.orders.findByUserId(userId)
    });
  });

  app.delete("/me", async (req, res) => {
    await db.users.update(req.session.userId, { deleted: true });
    res.status(202).json({ status: "accepted" });
  });
}
