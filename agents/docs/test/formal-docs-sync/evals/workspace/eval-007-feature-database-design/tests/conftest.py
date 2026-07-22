from pathlib import Path
from types import SimpleNamespace

import pytest

from src.workspace_access.service import accept_invitation


@pytest.fixture
def schema_text():
    workspace_root = Path(__file__).resolve().parents[1]
    return (workspace_root / "src/workspace_access/schema.sql").read_text(encoding="utf-8")


class WorkspaceServiceHarness:
    def __init__(self):
        self._call_order = []
        self._membership_writes = 0
        self._audit_events = []

    def _run(self, *, expired=False):
        invitation = SimpleNamespace(
            workspace_id="workspace-1",
            user_id="user-1",
            role="editor",
            expired=expired,
        )
        harness = self

        class InvitationStore:
            def find(self, token):
                harness._call_order.append("consume_invitation")
                return invitation

            def mark_consumed(self, token):
                return None

        class Database:
            def execute(self, statement, parameters):
                harness._call_order.append("upsert_membership")
                harness._membership_writes += 1
                return {
                    "workspace_id": parameters[0],
                    "user_id": parameters[1],
                    "role": parameters[2],
                }

        class AuditWriter:
            def write(self, event_type, workspace_id, user_id):
                harness._call_order.append("write_audit")
                harness._audit_events.append(event_type)

        return accept_invitation(
            Database(), InvitationStore(), AuditWriter(), "token-1"
        )

    def call_order(self):
        self._run()
        return self._call_order

    def expired_invitation_error(self):
        try:
            self._run(expired=True)
        except ValueError as error:
            return str(error)
        return None

    def membership_write_count(self):
        return self._membership_writes

    def audit_event(self):
        self._run()
        return self._audit_events[-1]


@pytest.fixture
def workspace_service():
    return WorkspaceServiceHarness()
