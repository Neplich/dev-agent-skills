const test = require("node:test");
const assert = require("node:assert");
const orderService = require("../src/services/order-service");

test("placing an order starts in created status", () => {
  assert.strictEqual(orderService.createOrder({}).status, "created");
});
