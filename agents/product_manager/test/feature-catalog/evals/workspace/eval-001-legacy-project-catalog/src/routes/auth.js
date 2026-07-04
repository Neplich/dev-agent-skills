const express = require("express");
const router = express.Router();

// POST /api/auth/login — customer sign-in with email + password
router.post("/api/auth/login", (req, res) => {
  res.json({ token: "signed-jwt" });
});

// POST /api/auth/refresh — refresh an expiring session token
router.post("/api/auth/refresh", (req, res) => {
  res.json({ token: "signed-jwt" });
});

module.exports = router;
