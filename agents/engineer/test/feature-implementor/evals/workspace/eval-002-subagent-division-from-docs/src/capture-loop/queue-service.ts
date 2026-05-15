export type QueueStatus = "pending" | "processing" | "failed" | "completed";

export interface QueueItem {
  id: string;
  status: QueueStatus;
  attempts: number;
  lastError?: string;
}

export function markFailed(item: QueueItem, error: string): QueueItem {
  return {
    ...item,
    status: "failed",
    lastError: error,
  };
}
