import assert from "node:assert/strict";
import test from "node:test";

import { formatNotificationStatus } from "../src/notification-status.js";

test("formats supported notification statuses", () => {
  assert.equal(formatNotificationStatus("active"), "Active");
  assert.equal(formatNotificationStatus("read"), "Read");
  assert.equal(formatNotificationStatus("archived"), "Archived");
});
