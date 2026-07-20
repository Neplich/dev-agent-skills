import { strict as assert } from "node:assert";
import { searchHttpRoute } from "../src/search/routes.ts";

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
assert.deepEqual(searchHttpRoute.handle({ q: "agent", limit: 0 }), {
  status: 200,
  body: { items: [], limit: 1 },
});
for (const limit of [1.5, Number.NaN, Number.POSITIVE_INFINITY]) {
  assert.deepEqual(searchHttpRoute.handle({ q: "agent", limit }), {
    status: 400,
    body: { error: "limit must be an integer" },
  });
}
assert.deepEqual(searchHttpRoute.handle({ q: "   " }), {
  status: 400,
  body: { error: "q is required" },
});
