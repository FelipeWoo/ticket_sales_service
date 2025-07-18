import os
import json
from fpdf import FPDF
from db.connection import get_connection
from models.ticket import TicketItem
from pydantic import TypeAdapter


def generate_ticket_pdf(config: object, ticket_id: str):
    conn = get_connection(config.db)
    cur = conn.cursor()
    cur.execute("""
        SELECT ticket_id, issued_at, location_id, items, total, tax, payment_method 
        FROM tickets WHERE ticket_id = ?
    """, (ticket_id,))
    row = cur.fetchone()
    conn.close()

    if not row:
        raise ValueError("Ticket not found")

    os.makedirs(config.pdf, exist_ok=True)

    ticket_id, issued_at, location_id, items_json, total, tax, payment_method = row
    raw_items = json.loads(items_json)
    adapter = TypeAdapter(list[TicketItem])
    items = adapter.validate_python(raw_items)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, f"Ticket ID: {ticket_id}", ln=True)
    pdf.cell(200, 10, f"Issued at: {issued_at}", ln=True)
    pdf.cell(200, 10, f"Location: {location_id}", ln=True)
    pdf.cell(200, 10, f"Payment method: {payment_method}", ln=True)
    pdf.cell(200, 10, f"--- Items ---", ln=True)

    for item in items:
        pdf.cell(200, 10, f"{item.quantity} x {item.product_id} @ {item.unit_price}", ln=True)

    pdf.cell(200, 10, f"Tax: {tax}", ln=True)
    pdf.cell(200, 10, f"Total: {total}", ln=True)

    pdf.output(f"{config.pdf}/ticket_{ticket_id}.pdf")

