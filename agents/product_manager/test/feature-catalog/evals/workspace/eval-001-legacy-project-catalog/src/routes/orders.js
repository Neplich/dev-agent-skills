const express = require("express");
const orderService = require("../services/order-service");
const router = express.Router();

// POST /api/orders — place a new order
router.post("/api/orders", (req, res) => {
  res.status(201).json(orderService.createOrder(req.body));
});

// GET /api/orders/:id — order detail and status
router.get("/api/orders/:id", (req, res) => {
  res.json(orderService.getOrder(req.params.id));
});

module.exports = router;
