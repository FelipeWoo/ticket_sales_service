from pydantic import BaseModel
from typing import List, Optional


class TicketItem(BaseModel):
    product_id: str
    quantity: float
    unit_price: float


class TicketInput(BaseModel):
    location_id: str
    payment_method: str
    items: List[TicketItem]

    user_id: Optional[str] = None
    terminal_id: Optional[str] = None
    session_id: Optional[str] = None
    internal_notes: Optional[str] = None
    raw_discount: float = 0.0
