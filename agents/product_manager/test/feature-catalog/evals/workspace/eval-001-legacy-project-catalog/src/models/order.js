// Order data model: id, customerId, items[], status, total, createdAt
module.exports = {
  create(payload) {
    return { id: "ord_1", status: "created", ...payload };
  },
  findById(id) {
    return { id, status: "paid" };
  },
};
