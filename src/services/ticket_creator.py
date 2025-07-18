from uuid import uuid4
import json
from datetime import datetime, timezone
from utils.calculator import calculate_totals
from utils.logger import logger
from db.connection import get_connection
from models.ticket import TicketInput


def create_ticket(config: object, raw_data: dict) -> str:
    ticket = TicketInput(**raw_data)  # Validates everything with Pydantic

    ticket_id = str(uuid4())
    issued_at = datetime.now(timezone.utc).isoformat()

    # Use ticket.items directly — they are already TicketItem objects
    total, tax = calculate_totals(ticket.items)

    public_fields = (
        ticket_id,
        issued_at,
        ticket.location_id,
        json.dumps([i.model_dump() for i in ticket.items]),  # Store as JSON
        total,
        tax,
        ticket.payment_method,
        "completed",
    )

    private_fields = (
        ticket.user_id,
        ticket.terminal_id,
        ticket.session_id,
        ticket.internal_notes,
        ticket.raw_discount,
        None,  # cancellation_reason
        None,  # audit_hash
    )

    conn = get_connection(str(config.db))
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO tickets (
                ticket_id, issued_at, location_id, items, total, tax, payment_method, status,
                user_id, terminal_id, session_id, internal_notes, raw_discount, cancellation_reason, audit_hash
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, public_fields + private_fields)
        conn.commit()
    except Exception as e:
        logger.error(f"✘ Failed to insert ticket in database: {e}")
        return
    finally:
        conn.close()

    logger.success("✓ Success inserting ticket in database")
    return ticket_id
