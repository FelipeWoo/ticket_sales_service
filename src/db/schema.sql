CREATE TABLE IF NOT EXISTS tickets (
    ticket_id TEXT PRIMARY KEY,
    issued_at TEXT NOT NULL,
    location_id TEXT NOT NULL,
    items TEXT NOT NULL,               -- JSON string
    total REAL NOT NULL,
    tax REAL NOT NULL,
    payment_method TEXT NOT NULL,
    status TEXT NOT NULL,

    user_id TEXT,
    terminal_id TEXT,
    session_id TEXT,
    internal_notes TEXT,
    raw_discount REAL,
    cancellation_reason TEXT,
    audit_hash TEXT
);
