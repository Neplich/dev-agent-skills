const express = require("express");
const refundService = require("./refund-service");
const router = express.Router();

// POST /api/orders/:id/refunds — request a refund for a paid order
router.post("/api/orders/:id/refunds", (req, res) => {
  res.status(201).json(refundService.requestRefund(req.params.id, req.body));
});

// GET /api/orders/:id/refunds — list refunds for an order
router.get("/api/orders/:id/refunds", (req, res) => {
  res.json(refundService.listRefunds(req.params.id));
});

module.exports = router;
