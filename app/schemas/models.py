from pydantic import BaseModel
from typing import Optional

class TicketExtraction(BaseModel):
    name: Optional[str]
    order_id: Optional[str]
    issue_type: Optional[str]
    phone: Optional[str]