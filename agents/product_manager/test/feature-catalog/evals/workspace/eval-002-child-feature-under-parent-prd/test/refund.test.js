const test = require("node:test");
const assert = require("node:assert");
const refundService = require("../src/orders/refund/refund-service");

test("refund request starts in requested status", () => {
  assert.strictEqual(refundService.requestRefund("ord_1", {}).status, "requested");
});
