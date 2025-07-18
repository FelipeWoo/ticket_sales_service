import sqlite3
import tempfile
from pathlib import Path
from src.services.ticket_creator import create_ticket
from utils.boot import boot

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS tickets (
    ticket_id TEXT PRIMARY KEY,
    issued_at TEXT,
    location_id TEXT,
    items TEXT,
    total REAL,
    tax REAL,
    payment_method TEXT,
    status TEXT,
    user_id TEXT,
    terminal_id TEXT,
    session_id TEXT,
    internal_notes TEXT,
    raw_discount REAL,
    cancellation_reason TEXT,
    audit_hash TEXT
);
"""

def test_ticket_creation_minimal():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=True) as tmp:
        db_path = Path(tmp.name)

        # Create schema in the temp DB
        with sqlite3.connect(db_path) as conn:
            conn.executescript(SCHEMA_SQL)

        # Boot config and override db path
        config = boot("test")
        config.db = db_path

        data = {
            "location_id": "test-loc",
            "items": [{"product_id": "test-item", "quantity": 1, "unit_price": 10}],
            "payment_method": "cash"
        }

        ticket_id = create_ticket(config, data)

        assert isinstance(ticket_id, str)
        assert len(ticket_id) > 10
