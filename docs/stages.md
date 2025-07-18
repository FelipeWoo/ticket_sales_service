# Development Stages — `ticket_sales_service`

A structured roadmap to build an append-only, sales-focused ticketing system using Python and SQLite, with PDF generation and SQL-based queries.

---

## MVP

>  Goal: Create, store, and export a simple ticket with public/private data using SQLite and generate a PDF.

### Features:
- [ ] SQLite schema with `tickets` table
- [ ] `create_ticket()` function (Python)
- [ ] `generate_ticket_pdf()` with public data only
- [ ] Hardcoded input for demo ticket
- [ ] Console printout + generated PDF file

### Files:
- `main.py`
- `db/schema.sql`
- `services/ticket_creator.py`
- `services/pdf_generator.py`
- `utils/calculator.py`

---

## Stage 1: Input & Validation Layer

> Add input structure and enforce data integrity

- [ ] Validate ticket input (`validate_ticket_data`)
- [ ] Tax and total calculation (`calculate_totals`)
- [ ] Normalize items (list of dicts)
- [ ] Unique ticket ID + timestamp generation

---

## Stage 2: Ticket Management

> Create a core ticket module with public/private separation

- [ ] Define `Ticket` dataclass with `.to_dict()` split into public/private
- [ ] Store full ticket in DB (JSON where applicable)
- [ ] Add `cancel_ticket(ticket_id)` logic
- [ ] Load ticket by ID
- [ ] JSON export

---

## Stage 3: Query System (Raw SQL)

> Allow flexible filters using real SQL

- [ ] Define safe interface to pass SQL queries (SELECT-only)
- [ ] Create a `public_tickets` view for separation
- [ ] Allow filters by date range, location, payment method, status

---

## Stage 4: PDF Templates

> Improve ticket readability

- [ ] Use a simple template engine (e.g. `jinja2`)
- [ ] Support multiple layouts (80mm POS, full-page A4)
- [ ] Add logo, branding elements (optional)
- [ ] QR code with ticket ID or link (future)

---

## Stage 5: Export and Reports

> Enable data extraction

- [ ] CSV export by range
- [ ] Totals grouped by day, user, location
- [ ] Status summary (completed, cancelled, refunded)

---

## Stage 6: Audit & Integrity

> Ensure tamper-proof records

- [ ] SHA256 hash of ticket JSON body
- [ ] Store hash in `audit_hash`
- [ ] Optionally generate Merkle root or append to hash chain
- [ ] Compare exported PDF hash with DB

---

## Stage 7: CLI / UI / API

> Extend to interactive or automated use

- [ ] CLI with commands: `new`, `show`, `cancel`, `list`, `export`
- [ ] Flask/FastAPI interface for external access (optional)
- [ ] UI frontend (basic HTML or terminal view)

---

## Future: Multi-terminal sync

> Enable syncing between terminals or to cloud

- [ ] Export ticket data as JSON bundle
- [ ] Push/pull changes from remote API
- [ ] Offline-first model with conflict detection

---

