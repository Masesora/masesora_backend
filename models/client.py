from pydantic import BaseModel, Field
from typing import Optional

class Client(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    name: str
    email: Optional[str] = None
    contract_signed: bool

    model_config = {
        "populate_by_name": True,
        "arbitrary_types_allowed": True
    }