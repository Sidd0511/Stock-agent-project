from pydantic import BaseModel, model_validator
from typing import Literal, Optional


class AssetTrackingConfig(BaseModel):
    name: str
    type: Literal["stock", "metal"]
    threshold: float
    threshold_type: Literal["percent", "absolute"]
    direction: Literal["increase", "decrease"]
    symbol: Optional[str] = None

    @model_validator(mode="after")
    def check_symbol_for_stock(self) -> 'AssetTrackingConfig':
        if self.type == "stock" and not self.symbol:
            raise ValueError("Symbol must be provided for stock assets.")
        return self