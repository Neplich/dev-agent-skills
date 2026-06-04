import assert from "node:assert/strict";
import { test } from "node:test";

import {
  listActiveNotifications,
  type Notification,
} from "../../src/api/notifications.ts";

test("active notifications exclude archived items", () => {
  const notifications: Notification[] = [
    { id: "n-1", title: "Welcome", status: "unread" },
    { id: "n-2", title: "Billing updated", status: "read" },
    { id: "n-3", title: "Old import finished", status: "archived" },
  ];

  const activeIds = listActiveNotifications(notifications).map(
    (notification) => notification.id,
  );

  assert.deepEqual(activeIds, ["n-1", "n-2"]);
});
