ALLOWED_ROLES = {"owner", "admin", "analyst"}


def view_dashboard(role: str, event_count: int, load_failed: bool = False):
    if role not in ALLOWED_ROLES:
        return {"ok": False, "message": "Dashboard access is unavailable.", "recovery": "Ask an admin for the analyst role."}
    if load_failed:
        return {"ok": False, "message": "Activity could not be loaded.", "recovery": "Retry from the dashboard."}
    if event_count == 0:
        return {"ok": True, "state": "empty", "message": "No activity yet."}
    return {"ok": True, "state": "ready", "event_count": event_count}
