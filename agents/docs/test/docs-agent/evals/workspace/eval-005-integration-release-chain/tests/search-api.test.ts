import { strict as assert } from "node:assert";
import { searchHttpRoute } from "../src/search/routes";

assert.equal(searchHttpRoute.method, "GET");
assert.equal(searchHttpRoute.path, "/api/search");
assert.deepEqual(searchHttpRoute.handle({ q: "agent" }), {
  status: 200,
  body: { items: [], limit: 10 },
});
assert.deepEqual(searchHttpRoute.handle({ q: "" }), {
  status: 400,
  body: { error: "q is required" },
});
assert.deepEqual(searchHttpRoute.handle({ q: "agent", limit: 99 }), {
  status: 200,
  body: { items: [], limit: 20 },
});
