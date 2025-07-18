# Project: `ticket_sales_service`

> A minimal, auditable, append-only ticketing system for sales, with SQLite storage, PDF generation, public/private data separation, and SQL-powered queries.

---

### Goal

* Create **immutable tickets** for sales
* Store them securely in **SQLite**
* Split each ticket into:

  * ✅ **Public data** → visible in PDF or UI
  * 🔒 **Private data** → available only for internal queries
* Support **before/during/after** workflow
* Query/filter via raw **SQL**
* Export **PDF versions** with only public data

---

## Data Model — Ticket

### Public Fields (shown in PDF)

| Field            | Type                | Description                       |
| ---------------- | ------------------- | --------------------------------- |
| `ticket_id`      | TEXT (UUID)         | Unique identifier                 |
| `issued_at`      | TEXT (ISO datetime) | UTC timestamp                     |
| `location_id`    | TEXT                | Branch or POS                     |
| `items`          | JSON                | List of `{name, qty, unit_price}` |
| `total`          | REAL                | Final total (after tax/discounts) |
| `tax`            | REAL                | Tax amount                        |
| `payment_method` | TEXT                | 'cash', 'card', 'qr', etc.        |
| `status`         | TEXT                | 'completed', 'cancelled', etc.    |

---

### Private Fields (not shown in PDF)

| Field                 | Type | Description                            |
| --------------------- | ---- | -------------------------------------- |
| `user_id`             | TEXT | ID of the user who made the sale       |
| `terminal_id`         | TEXT | POS terminal used                      |
| `session_id`          | TEXT | Work session (for shift logs)          |
| `internal_notes`      | TEXT | Optional staff note                    |
| `raw_discount`        | REAL | Discount amount                        |
| `cancellation_reason` | TEXT | Only if status = 'cancelled'           |
| `audit_hash`          | TEXT | Optional hash for signature validation |

---

## System Logic & Flow

### Before Ticket Creation

* Validate item prices, tax rules
* Retrieve session, location, payment method
* Check that user is active and terminal is open

### Ticket Creation

* Generate UUID
* Timestamp the event
* Calculate totals, taxes, discount
* Save full ticket to DB
* Generate public PDF
* Return success with ticket ID

### After Ticket

* Allow queries (by date, user, location, etc.)
* Support filters like `WHERE status = 'completed' AND issued_at BETWEEN ...`
* Optional: Generate financial reports, stats

---

## Methods & Functions

### Ticket Lifecycle

```python
def create_ticket(data: dict) -> str
def cancel_ticket(ticket_id: str, reason: str) -> None
def get_ticket_by_id(ticket_id: str) -> dict
def list_tickets(filters: dict) -> List[dict]
```

---

### PDF Generation

```python
def generate_ticket_pdf(ticket_id: str, output_path: str) -> None
```

Only public fields are included.

---

### SQL Queries (raw filters)

```python
def execute_sql_query(query: str) -> List[dict]
```

Secure: restricted to SELECT queries on views/tables.

---

### Export

```python
def export_tickets_to_csv(start_date: str, end_date: str, output_file: str) -> None
```

---

### Validation & Utilities

```python
def validate_ticket_data(data: dict) -> bool
def calculate_totals(items: List[dict], tax_rate: float) -> Tuple[float, float]
def generate_ticket_id() -> str
```

---

## SQLite Schema (Simplified)

```sql
CREATE TABLE tickets (
    ticket_id TEXT PRIMARY KEY,
    issued_at TEXT,
    location_id TEXT,
    items TEXT,               -- JSON
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
```

You can later create views like:

```sql
CREATE VIEW public_tickets AS
SELECT
  ticket_id, issued_at, location_id, items, total, tax, payment_method, status
FROM tickets;
```

---

## Project Folder Structure

```
ticket_sales_service/
├── .private/                    # Internal configs or keys (never tracked)
├── .venv/                       # Virtual environment (local only)
│
├── docs/                        # Project documentation
│   ├── logic.md                 # Explains ticket structure and field logic
│   ├── specs.md                 # System specifications and design
│   ├── stages.md                # Development stages and roadmap
│   └── workflow.md              # Task list with commits and test cases
│
├── exports/                     # PDF or CSV exports
│   └── main.log                 # Optional log of export actions (or move to logs/)
│
├── logs/                        # System/application logs
│   └── main.log
│
├── src/                         # Application source code
│   ├── db/                      # SQLite schema and database connection
│   │   └── schema.sql
│   │   └── connection.py
│   │
│   ├── models/                  # Data models (Ticket, Item, etc.)
│   │   └── ticket.py
│   │
│   ├── services/                # Core business logic
│   │   └── ticket_creator.py
│   │   └── ticket_reader.py
│   │   └── pdf_generator.py
│   │
│   └── utils/                   # Shared tools and helpers
│       └── boot.py             # Startup/init routines (load schema, etc.)
│       └── logger.py           # Logging config
│       └── calculator.py       # Totals and tax
│       └── validators.py       # Input validation
│       └── __init__.py
│
├── tests/                       # All test cases
│   └── __init__.py
│   └── conftest.py             # Pytest fixtures (e.g., temp DB)
│   └── dummy_test.py           # Placeholder (will be removed)
│   └── test_ticket_creation.py
│
├── .env                         # Local environment variables
├── .gitignore                   # Ignore compiled, secrets, etc.
├── .python-version              # For pyenv
├── LICENSE                      # MIT or other
├── Makefile                     # Shortcuts for run/test/lint
├── pyproject.toml               # Project metadata (for uv or poetry)
├── README.md                    # Overview and setup instructions
├── requirements.txt             # pip compatibility
└── uv.lock                      # Dependency lock for uv

```

---
