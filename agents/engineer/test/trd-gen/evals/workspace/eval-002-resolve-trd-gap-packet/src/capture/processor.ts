export type CaptureEvent = {
  organizationId: string;
  clientEventId: string;
  payload: unknown;
};

export async function processCapture(event: CaptureEvent) {
  return {
    idempotencyKey: `${event.organizationId}:${event.clientEventId}`,
    payload: event.payload
  };
}
