from src.utils.calculator import calculate_totals
from src.models.ticket import TicketItem


def test_calculate_totals_basic():
    items = [
        TicketItem(product_id="coffee", quantity=2, unit_price=50.0),
        TicketItem(product_id="croissant", quantity=1, unit_price=30.0),
    ]

    total, tax = calculate_totals(items)

    expected_subtotal = 2 * 50.0 + 1 * 30.0  # 130.0
    expected_tax = round(expected_subtotal * 0.16, 2)  # 20.8
    expected_total = round(expected_subtotal + expected_tax, 2)  # 150.8

    assert total == expected_total
    assert tax == expected_tax
