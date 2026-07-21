import express from "express";
import adminRouter from "./api/admin-routes.js";

const app = express();

function requireAuthenticated(req, res, next) {
  if (!req.user) {
    return res.sendStatus(401);
  }

  next();
}

app.get("/account", requireAuthenticated, (req, res) => {
  res.json({ userId: req.user.id });
});

// Unlike the account route, the admin router is mounted without an auth guard.
app.use(adminRouter);

export default app;
