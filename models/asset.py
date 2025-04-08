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
        elif self.type == "metal" and self.symbol:
            raise ValueError("Symbol must not be provided for metal assets.")
        return self

class AlertRule(BaseModel):
    asset_name: str
    asset_type: Literal["stock", "metal"]
    trigger_type: Literal["above","below"]
    threshold: float
    active: bool =  True
    symbol: Optional[str] = None

    @model_validator(mode="after")
    def check_symbol_for_stock(self) -> 'AlertRule':
        if self.asset_type == "stock" and not self.symbol:
            raise ValueError("Symbol must be provided for stock assets.")
        elif self.asset_type == "metal" and self.symbol:
            raise ValueError("Symbol must not be provided for metal assets.")
        return self
    