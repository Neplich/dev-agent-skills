import assert from "node:assert/strict";
import test from "node:test";

test("health fixture uses flat node:test style", () => {
  assert.deepEqual({ status: "ok" }, { status: "ok" });
});
