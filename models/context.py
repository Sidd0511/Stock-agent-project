from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

class AssetContext(BaseModel):
    """
    Context model for asset tracking.

    This class defines the context for tracking assets, including the asset name, type, and the time of the last update.

    Attributes:
        asset_name (str): The name of the asset being tracked.
        asset_type (Literal["stock", "metal"]): The type of the asset (either "stock" or "metal").
        symbol (Optional[str]): The symbol of the asset (if applicable).
        current_price (float): The current price of the asset.
        reference_price (float): The reference price for comparison.
        threshold (float): The threshold value for triggering alerts.
        threshold_type (Literal["percent", "absolute"]): The type of threshold.
        direction (Literal["increase", "decrease"]): The direction to monitor for threshold crossing.
        triggered (bool): Whether the threshold has been triggered.
        notes (Optional[str]): Additional notes or comments.
        timestamp (datetime): The timestamp of the context creation or last update.
    """
    asset_name: str  # The name of the asset being tracked
    asset_type: Literal["stock", "metal"]  # The type of the asset ("stock" or "metal")
    symbol: Optional[str] = None  # The symbol of the asset (if applicable)

    current_price: float  # The current price of the asset
    reference_price: float  # The reference price for comparison
    threshold: float  # The threshold value for triggering alerts
    threshold_type: Literal["percent", "absolute"]  # The type of threshold ("percent" or "absolute")
    direction: Literal["increase", "decrease"]  # The direction to monitor for threshold crossing

    triggered: bool = False  # Whether the threshold has been triggered
    notes: Optional[str] = None  # Additional notes or comments
    timestamp: datetime = Field(default_factory=datetime.utcnow)  # The timestamp of the context creation or last update
