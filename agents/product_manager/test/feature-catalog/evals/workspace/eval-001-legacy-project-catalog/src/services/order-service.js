const Order = require("../models/order");

// Order lifecycle: created -> paid -> shipped -> completed
module.exports = {
  createOrder(payload) {
    return Order.create(payload);
  },
  getOrder(id) {
    return Order.findById(id);
  },
};
