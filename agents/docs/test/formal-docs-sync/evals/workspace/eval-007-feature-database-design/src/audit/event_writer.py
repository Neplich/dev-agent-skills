class AuditWriter:
    def __init__(self, sink):
        self.sink = sink

    def write(self, event_type, workspace_id, user_id):
        return self.sink.append({
            "event_type": event_type,
            "workspace_id": workspace_id,
            "user_id": user_id,
        })
