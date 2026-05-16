import { markFailed, QueueItem } from "./queue-service";

export type HandlerResult =
  | { ok: true }
  | { ok: false; retryable: boolean; error: string };

export function handleResult(item: QueueItem, result: HandlerResult): QueueItem {
  if (result.ok) {
    return { ...item, status: "completed" };
  }

  return markFailed(item, result.error);
}
