// Refund model: id, orderId, amount, reason, status (requested -> approved -> refunded)
module.exports = {
  requestRefund(orderId, payload) {
    return { id: "rf_1", orderId, status: "requested", ...payload };
  },
  listRefunds(orderId) {
    return [{ id: "rf_1", orderId, status: "approved" }];
  },
};
