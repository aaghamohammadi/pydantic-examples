from enum import Enum
from pprint import pprint
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, conint, constr


class Size(Enum):
    small = "small"
    medium = "medium"
    large = "large"


class Tshirt(BaseModel):
    brand: constr(min_length=2, strict=True)
    size: Size
    quantity: Optional[conint(ge=1, strict=True)] = 1
    id: UUID
    price: conint(ge=1, strict=True)


t1 = Tshirt(brand="Kappa", size=Size.medium, quantity=3, id=uuid4(), price=10)
pprint(t1)
