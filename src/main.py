from utils.boot import boot
from services.ticket_creator import create_ticket
from services.pdf_generator import generate_ticket_pdf
from utils.logger import logger

def main():
    config = boot("main")
    
    sample = {
    "location_id": "store-001",
    "items": [
        {"product_id": "coffee", "quantity": 2, "unit_price": 50},
        {"product_id": "croissant", "quantity": 1, "unit_price": 35},
    ],
    "payment_method": "cash",
    "user_id": "john.doe",
    "terminal_id": "T-001",
    "session_id": "morning-shift",
    "internal_notes": "Customer requested hot coffee"
}


    try:
        ticket_id = create_ticket(config, sample)
        logger.success(f"✓ Ticket created: {ticket_id}")
    except Exception as e:
        logger.error(f"✘ Failed to create ticket: {e}")
        return

    try:
        generate_ticket_pdf(config, ticket_id)
        logger.success(f"✓ Ticket exported: {ticket_id}")
    except Exception as e:
        logger.error(f"✘ Failed to export ticket: {e}")
        return

if __name__ == "__main__":
    main()
