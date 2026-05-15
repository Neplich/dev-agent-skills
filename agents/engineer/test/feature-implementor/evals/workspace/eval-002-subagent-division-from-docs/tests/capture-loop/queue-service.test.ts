import { markFailed } from "../../src/capture-loop/queue-service";

describe("queue-service", () => {
  it("marks an item failed", () => {
    const item = { id: "evt-1", status: "processing" as const, attempts: 1 };

    expect(markFailed(item, "timeout")).toEqual({
      id: "evt-1",
      status: "failed",
      attempts: 1,
      lastError: "timeout",
    });
  });
});
