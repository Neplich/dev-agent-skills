import { strict as assert } from "node:assert";
import { searchRoute } from "../src/search/routes";

assert.equal(searchRoute({ q: "agent" }).status, 200);
assert.equal(searchRoute({ q: "" }).status, 400);
assert.equal(searchRoute({ q: "agent", limit: 99 }).body.limit, 20);
