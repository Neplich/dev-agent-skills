import assert from "node:assert/strict";
import test from "node:test";

import { createApp } from "../src/server.js";

test("createApp returns an Express application", () => {
  assert.equal(typeof createApp().listen, "function");
});
