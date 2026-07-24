from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from src.audit.event_writer import AuditWriter
from src.workspace_access.service import accept_invitation


@pytest.fixture
def db():
    database = Mock()
    database.execute.return_value = {"role": "editor"}
    return database


@pytest.fixture
def workspace_store():
    store = Mock()
    store.exists.return_value = True
    return store


@pytest.fixture
def user_store():
    store = Mock()
    store.exists.return_value = True
    return store


@pytest.fixture
def schema_text():
    workspace_root = Path(__file__).resolve().parents[1]
    return (workspace_root / "src/workspace_access/schema.sql").read_text(encoding="utf-8")


class WorkspaceServiceHarness:
    def __init__(self):
        self._call_order = []
        self._membership_writes = 0
        self._audit_events = []

    def _run(self, *, expired=False, found=True, user_id="user-1"):
        invitation = SimpleNamespace(
            workspace_id="workspace-1",
            role="editor",
            expired=expired,
        )
        harness = self

        class InvitationStore:
            def find(self, token):
                harness._call_order.append("find_invitation")
                return invitation if found else None

            def mark_consumed(self, token):
                harness._call_order.append("mark_consumed")

        class Database:
            def execute(self, statement, parameters):
                harness._call_order.append("upsert_membership")
                harness._membership_writes += 1
                return {
                    "workspace_id": parameters[0],
                    "user_id": parameters[1],
                    "role": parameters[2],
                }

        class AuditSink:
            def append(self, event):
                harness._call_order.append("write_audit")
                harness._audit_events.append(event)

        return accept_invitation(
            Database(), InvitationStore(), AuditWriter(AuditSink()), "token-1", user_id
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

    def invalid_invitation_error(self):
        try:
            self._run(found=False)
        except ValueError as error:
            return str(error)
        return None

    def membership_write_count(self):
        return self._membership_writes

    def recorded_call_order(self):
        return self._call_order

    def audit_event_count(self):
        return len(self._audit_events)

    def audit_event(self):
        self._run()
        return self._audit_events[-1]

    def membership_for_user(self, user_id):
        return self._run(user_id=user_id)


@pytest.fixture
def workspace_service():
    return WorkspaceServiceHarness()
