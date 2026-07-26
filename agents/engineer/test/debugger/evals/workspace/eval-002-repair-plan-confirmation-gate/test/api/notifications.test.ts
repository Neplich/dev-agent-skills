import assert from "node:assert/strict";
import test from "node:test";

import { normalizeNotificationStatus } from "../../src/api/notifications.ts";

test("accepts archived notification status", () => {
  assert.equal(normalizeNotificationStatus("archived"), "archived");
});
