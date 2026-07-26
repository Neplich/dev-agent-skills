import assert from "node:assert/strict";
import test from "node:test";

import { createServer } from "../src/server.js";

test("exports the staging HTTP server factory", () => {
  assert.equal(typeof createServer, "function");
});
