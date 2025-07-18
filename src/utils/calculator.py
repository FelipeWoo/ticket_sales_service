from utils.logger import logger
from models.ticket import TicketItem

def calculate_totals(items: list[TicketItem], tax_rate: float = 0.16) -> tuple[float, float]:
    try: 
        subtotal = sum(item.quantity * item.unit_price for item in items)
        tax = round(subtotal * tax_rate, 2)
        total = round(subtotal + tax, 2)
    except Exception as e:
        logger.error(f"✘ Failed calculate totals: {e}")
        return 

    return total, tax
